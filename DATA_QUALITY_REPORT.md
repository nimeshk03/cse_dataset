# CSE Dataset — Data Quality Report

Generated: 2026-04-13 21:11

---

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,218,602 |
| Symbols | 287 |
| Date range | 2010-01-01 to 2026-04-10 |
| Columns | 30 |
| Trading-day rows (volume > 0) | 1,218,602 (100.0%) |
| OHLC-invalid rows | 55,198 (4.53%) |
| Outlier rows (\|pct_change\| > 50%) | 0 |
| Rows with macro data (sp500 non-null) | 0 (0.0%) |
| Rows with market sentiment | 174,783 (14.3%) |

---

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `volume_zscore` | 1,218,602 | 100.0% |
| `finbert_label` | 1,218,602 | 100.0% |
| `vader_score_max` | 1,218,602 | 100.0% |
| `vader_score_mean` | 1,218,602 | 100.0% |
| `market_vader_mean` | 1,043,819 | 85.66% |
| `market_news_count` | 1,043,819 | 85.66% |
| `usd_lkr` | 95,858 | 7.87% |
| `close_to_ma200` | 28,413 | 2.33% |
| `inflation_pct` | 20,664 | 1.7% |
| `gdp_growth_pct` | 20,664 | 1.7% |
| `close_to_ma50` | 6,888 | 0.57% |
| `return_20d` | 5,740 | 0.47% |
| `volatility_20d` | 2,870 | 0.24% |
| `return_5d` | 1,435 | 0.12% |
| `return_1d` | 287 | 0.02% |
| `pct_change_1d` | 287 | 0.02% |

---

## Symbols with Thin Coverage (< 250 trading days)

| Symbol | First Date | Last Date | Trading Days |
|---|---|---|---|

---

## Per-Symbol Coverage Stats

| Stat | Value |
|---|---|
| Mean trading days per symbol | 4246 |
| Median trading days per symbol | 4246 |
| Min trading days | 4246 |
| Max trading days | 4246 |
| Symbols with full 10+ year coverage | 287 |
| Symbols with OHLC violations | 13 |

---

## Known Limitations

- `usd_lkr` is **annual** (World Bank) — forward-filled to daily; not daily granularity
- `interest_rates.csv` is a placeholder — T-bill rates require manual CBSL download
- `adj_close` equals `close` — dividend amounts not yet available from the CSE API
- Symbol-level sentiment (`vader_score_mean`) is absent — CSE news records lack dates
- LBO sentiment covers only 2021–present; pre-2021 market sentiment is null
- `finbert_label` is VADER-threshold-mapped, not true FinBERT inference
