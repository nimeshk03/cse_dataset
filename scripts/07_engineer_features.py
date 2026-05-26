"""
Feature engineering on cleaned OHLCV data.

Steps:
  1. Compute adj_close by back-adjusting for cash dividends
  2. Compute return_1d, return_5d, return_20d from adj_close
  3. Compute volatility_20d (rolling std of return_1d)
  4. Compute volume_zscore (rolling 20-day z-score)
  5. Compute close_to_ma50, close_to_ma200

Outputs:
    data/processed/all_stocks_features.parquet
"""

import os
import logging
import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(levelname)-8s  %(message)s")
log = logging.getLogger(__name__)

CLEANED   = "data/processed/all_stocks_cleaned.parquet"
DIVIDENDS = "data/processed/fundamentals/dividends.csv"
OUTPUT    = "data/processed/all_stocks_features.parquet"


# ---------------------------------------------------------------------------
# 1. Load
# ---------------------------------------------------------------------------

def load() -> tuple[pd.DataFrame, pd.DataFrame]:
    df = pd.read_parquet(CLEANED)
    df["date"] = pd.to_datetime(df["date"])

    div = pd.DataFrame(columns=["symbol", "xd_date", "amount"])
    if os.path.exists(DIVIDENDS):
        raw = pd.read_csv(DIVIDENDS)
        # xd column is a datetime string; extract just the date portion
        raw["xd_date"] = pd.to_datetime(raw["xd"], errors="coerce").dt.normalize()
        # Only keep rows with a valid symbol mapping
        raw = raw.dropna(subset=["symbol", "xd_date"])
        # The CSE API does not return a dividend amount — use 0 as placeholder
        # (adj_close will equal close until amount data is available)
        raw["amount"] = 0.0
        div = raw[["symbol", "xd_date", "amount"]].copy()
        log.info("Loaded %d dividend records (%d symbols)", len(div), div["symbol"].nunique())
    else:
        log.warning("Dividends file not found — adj_close will equal close")

    log.info("Loaded %d price rows, %d symbols", len(df), df["symbol"].nunique())
    return df, div


# ---------------------------------------------------------------------------
# 2. adj_close — backward ratio adjustment
# ---------------------------------------------------------------------------

def compute_adj_close(df: pd.DataFrame, div: pd.DataFrame) -> pd.DataFrame:
    """
    Standard backward ratio-adjustment formula:
      For each ex-dividend date, multiply all PRIOR closes by (close_on_xd - dividend) / close_on_xd

    Since dividend amounts are currently 0 (not available from the CSE API),
    adj_close == close for all stocks until amounts are populated.
    The column is added now so the schema is correct for future enrichment.
    """
    df = df.sort_values(["symbol", "date"]).copy()
    df["adj_close"] = df["close"].astype("float64")

    if div.empty or div["amount"].sum() == 0:
        log.info("No dividend amounts available — adj_close set equal to close")
        return df

    for symbol, grp in df.groupby("symbol", sort=False):
        sym_div = div[div["symbol"] == symbol].sort_values("xd_date")
        if sym_div.empty:
            continue

        idx = grp.index
        adj = grp["close"].values.copy().astype(float)

        for _, row in sym_div.iterrows():
            xd = row["xd_date"]
            amount = row["amount"]
            if amount == 0:
                continue
            prior_mask = grp["date"] < xd
            xd_close_rows = grp[grp["date"] == xd]["close"]
            if xd_close_rows.empty:
                continue
            xd_close = xd_close_rows.iloc[0]
            if xd_close <= 0:
                continue
            factor = (xd_close - amount) / xd_close
            adj[prior_mask.values] *= factor

        df.loc[idx, "adj_close"] = adj

    log.info("adj_close computed")
    return df


# ---------------------------------------------------------------------------
# 3. Feature computation (vectorised per-symbol)
# ---------------------------------------------------------------------------

def engineer(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values(["symbol", "date"]).copy()

    g = df.groupby("symbol", sort=False)

    log.info("Computing returns...")
    df["return_1d"]  = g["adj_close"].pct_change(1)
    df["return_5d"]  = g["adj_close"].pct_change(5)
    df["return_20d"] = g["adj_close"].pct_change(20)

    log.info("Computing volatility_20d...")
    df["volatility_20d"] = g["return_1d"].transform(
        lambda x: x.rolling(20, min_periods=10).std()
    )

    log.info("Computing volume_zscore...")
    vol_mean = g["volume"].transform(lambda x: x.rolling(20, min_periods=10).mean())
    vol_std  = g["volume"].transform(lambda x: x.rolling(20, min_periods=10).std())
    df["volume_zscore"] = ((df["volume"] - vol_mean) / vol_std).replace([np.inf, -np.inf], np.nan)
    df["volume_zscore"] = df["volume_zscore"].fillna(0.0)

    log.info("Computing MA ratios...")
    ma50  = g["adj_close"].transform(lambda x: x.rolling(50,  min_periods=25).mean())
    ma200 = g["adj_close"].transform(lambda x: x.rolling(200, min_periods=100).mean())
    df["close_to_ma50"]  = df["adj_close"] / ma50.replace(0, np.nan)
    df["close_to_ma200"] = df["adj_close"] / ma200.replace(0, np.nan)

    return df


# ---------------------------------------------------------------------------
# 4. Verify & save
# ---------------------------------------------------------------------------

def verify(df: pd.DataFrame):
    required = ["adj_close", "return_1d", "return_5d", "return_20d",
                "volatility_20d", "volume_zscore", "close_to_ma50", "close_to_ma200"]
    for col in required:
        assert col in df.columns, f"Missing column: {col}"
    log.info("All %d required feature columns present.", len(required))

    non_null_ret = df["return_1d"].notna().sum()
    log.info("return_1d non-null: %d / %d (%.1f%%)",
             non_null_ret, len(df), 100 * non_null_ret / len(df))
    z_null_pct = df["volume_zscore"].isna().mean()
    assert z_null_pct < 0.20, f"volume_zscore null rate too high: {z_null_pct:.1%}"


def save(df: pd.DataFrame):
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    df.to_parquet(OUTPUT, index=False)
    log.info("Saved: %s  (%d rows, %d cols)", OUTPUT, len(df), len(df.columns))


def main():
    df, div = load()
    df = compute_adj_close(df, div)
    df = engineer(df)
    verify(df)
    save(df)


if __name__ == "__main__":
    main()
