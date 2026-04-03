"""
Generate a data quality report for the published unified dataset.

Output:
    DATA_QUALITY_REPORT.md
"""

import os
import logging
import numpy as np
import pandas as pd
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(levelname)-8s  %(message)s")
log = logging.getLogger(__name__)

UNIFIED  = "data/published/cse_unified.parquet"
METADATA = "data/processed/company_metadata.csv"
OUTPUT   = "DATA_QUALITY_REPORT.md"


def null_summary(df: pd.DataFrame) -> pd.DataFrame:
    total = len(df)
    null_counts = df.isnull().sum()
    pct = (null_counts / total * 100).round(2)
    return pd.DataFrame({"null_count": null_counts, "null_pct": pct}).query("null_count > 0").sort_values("null_pct", ascending=False)


def per_symbol_coverage(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby("symbol")
        .agg(
            first_date=("date", "min"),
            last_date=("date", "max"),
            total_rows=("date", "count"),
            trading_days=("is_trading_day", "sum"),
            ohlc_invalid=("ohlc_invalid", "sum"),
            outlier_rows=("outlier_flag", "sum"),
        )
        .reset_index()
    )
    summary["coverage_years"] = ((summary["last_date"] - summary["first_date"]).dt.days / 365.25).round(1)
    return summary


def main():
    log.info("Loading unified dataset...")
    df = pd.read_parquet(UNIFIED)
    df["date"] = pd.to_datetime(df["date"])

    meta = pd.read_csv(METADATA) if os.path.exists(METADATA) else pd.DataFrame()

    log.info("Computing quality metrics...")
    nulls = null_summary(df)
    sym_cov = per_symbol_coverage(df)

    total_rows       = len(df)
    total_symbols    = df["symbol"].nunique()
    date_min         = df["date"].min().date()
    date_max         = df["date"].max().date()
    trading_days     = int(df["is_trading_day"].sum()) if "is_trading_day" in df.columns else 0
    ohlc_invalid     = int(df["ohlc_invalid"].sum()) if "ohlc_invalid" in df.columns else 0
    outlier_rows     = int(df["outlier_flag"].sum()) if "outlier_flag" in df.columns else 0
    macro_coverage   = df["sp500"].notna().sum() if "sp500" in df.columns else 0
    sentiment_rows   = df["market_vader_mean"].notna().sum() if "market_vader_mean" in df.columns else 0

    # Symbols with fewer than 250 trading days (< ~1 year of data)
    thin_symbols = sym_cov[sym_cov["trading_days"] < 250]

    lines = [
        f"# CSE Dataset — Data Quality Report",
        f"",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"",
        f"---",
        f"",
        f"## Summary",
        f"",
        f"| Metric | Value |",
        f"|---|---|",
        f"| Total rows | {total_rows:,} |",
        f"| Symbols | {total_symbols} |",
        f"| Date range | {date_min} to {date_max} |",
        f"| Columns | {len(df.columns)} |",
        f"| Trading-day rows (volume > 0) | {trading_days:,} ({100*trading_days/total_rows:.1f}%) |",
        f"| OHLC-invalid rows | {ohlc_invalid:,} ({100*ohlc_invalid/total_rows:.2f}%) |",
        f"| Outlier rows (\\|pct_change\\| > 50%) | {outlier_rows:,} |",
        f"| Rows with macro data (sp500 non-null) | {macro_coverage:,} ({100*macro_coverage/total_rows:.1f}%) |",
        f"| Rows with market sentiment | {sentiment_rows:,} ({100*sentiment_rows/total_rows:.1f}%) |",
        f"",
        f"---",
        f"",
        f"## Null Values by Column",
        f"",
        f"| Column | Null Count | Null % |",
        f"|---|---|---|",
    ]

    for col, row in nulls.iterrows():
        lines.append(f"| `{col}` | {int(row['null_count']):,} | {row['null_pct']}% |")

    lines += [
        f"",
        f"---",
        f"",
        f"## Symbols with Thin Coverage (< 250 trading days)",
        f"",
        f"| Symbol | First Date | Last Date | Trading Days |",
        f"|---|---|---|---|",
    ]

    for _, row in thin_symbols.iterrows():
        lines.append(f"| {row['symbol']} | {str(row['first_date'])[:10]} | {str(row['last_date'])[:10]} | {int(row['trading_days'])} |")

    lines += [
        f"",
        f"---",
        f"",
        f"## Per-Symbol Coverage Stats",
        f"",
        f"| Stat | Value |",
        f"|---|---|",
        f"| Mean trading days per symbol | {sym_cov['trading_days'].mean():.0f} |",
        f"| Median trading days per symbol | {sym_cov['trading_days'].median():.0f} |",
        f"| Min trading days | {sym_cov['trading_days'].min()} |",
        f"| Max trading days | {sym_cov['trading_days'].max()} |",
        f"| Symbols with full 10+ year coverage | {(sym_cov['coverage_years'] >= 10).sum()} |",
        f"| Symbols with OHLC violations | {(sym_cov['ohlc_invalid'] > 0).sum()} |",
        f"",
        f"---",
        f"",
        f"## Known Limitations",
        f"",
        f"- `usd_lkr` is **annual** (World Bank) — forward-filled to daily; not daily granularity",
        f"- `interest_rates.csv` is a placeholder — T-bill rates require manual CBSL download",
        f"- `adj_close` equals `close` — dividend amounts not yet available from the CSE API",
        f"- Symbol-level sentiment (`vader_score_mean`) is absent — CSE news records lack dates",
        f"- LBO sentiment covers only 2021–present; pre-2021 market sentiment is null",
        f"- `finbert_label` is VADER-threshold-mapped, not true FinBERT inference",
        f"",
    ]

    report = "\n".join(lines)
    with open(OUTPUT, "w") as f:
        f.write(report)
    log.info("Saved: %s", OUTPUT)


if __name__ == "__main__":
    main()
