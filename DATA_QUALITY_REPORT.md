# CSE Dataset — Data Quality Report

Generated: 2026-05-05 21:16

---

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,248,766 |
| Symbols | 293 |
| Date range | 2010-01-01 to 2026-05-04 |
| Columns | 30 |
| Trading-day rows (volume > 0) | 1,248,766 (100.0%) |
| OHLC-invalid rows | 17,048 (1.37%) |
| Outlier rows (\|pct_change\| > 50%) | 0 |
| Rows with macro data (sp500 non-null) | 0 (0.0%) |
| Rows with market sentiment | 115,442 (9.2%) |

---

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `volume_zscore` | 1,248,766 | 100.0% |
| `finbert_label` | 1,248,766 | 100.0% |
| `vader_score_max` | 1,248,766 | 100.0% |
| `vader_score_mean` | 1,248,766 | 100.0% |
| `market_vader_mean` | 1,133,324 | 90.76% |
| `market_news_count` | 1,133,324 | 90.76% |
| `usd_lkr` | 102,550 | 8.21% |
| `close_to_ma200` | 29,007 | 2.32% |
| `inflation_pct` | 25,784 | 2.06% |
| `gdp_growth_pct` | 25,784 | 2.06% |
| `close_to_ma50` | 7,032 | 0.56% |
| `return_20d` | 5,860 | 0.47% |
| `volatility_20d` | 2,930 | 0.23% |
| `return_5d` | 1,465 | 0.12% |
| `return_1d` | 293 | 0.02% |
| `pct_change_1d` | 293 | 0.02% |

---

## Symbols with Thin Coverage (< 250 trading days)

| Symbol | First Date | Last Date | Trading Days |
|---|---|---|---|

---

## Per-Symbol Coverage Stats

| Stat | Value |
|---|---|
| Mean trading days per symbol | 4262 |
| Median trading days per symbol | 4262 |
| Min trading days | 4262 |
| Max trading days | 4262 |
| Symbols with full 10+ year coverage | 293 |
| Symbols with OHLC violations | 4 |

---

## Known Limitations

- `usd_lkr` is **annual** (World Bank) — forward-filled to daily; not daily granularity
- `interest_rates.csv` is a placeholder — T-bill rates require manual CBSL download
- `adj_close` equals `close` — dividend amounts not yet available from the CSE API
- Symbol-level sentiment (`vader_score_mean`) is absent — CSE news records lack dates
- LBO sentiment covers only 2021–present; pre-2021 market sentiment is null
- `finbert_label` is VADER-threshold-mapped, not true FinBERT inference
