# CSE Dataset — Data Quality Report

Generated: 2026-05-15 21:18

---

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,234,030 |
| Symbols | 289 |
| Date range | 2010-01-01 to 2026-05-14 |
| Columns | 30 |
| Trading-day rows (volume > 0) | 1,234,030 (100.0%) |
| OHLC-invalid rows | 46,970 (3.81%) |
| Outlier rows (\|pct_change\| > 50%) | 0 |
| Rows with macro data (sp500 non-null) | 0 (0.0%) |
| Rows with market sentiment | 176,290 (14.3%) |

---

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `volume_zscore` | 1,234,030 | 100.0% |
| `finbert_label` | 1,234,030 | 100.0% |
| `vader_score_max` | 1,234,030 | 100.0% |
| `vader_score_mean` | 1,234,030 | 100.0% |
| `market_vader_mean` | 1,057,740 | 85.71% |
| `market_news_count` | 1,057,740 | 85.71% |
| `usd_lkr` | 103,462 | 8.38% |
| `close_to_ma200` | 28,611 | 2.32% |
| `inflation_pct` | 27,744 | 2.25% |
| `gdp_growth_pct` | 27,744 | 2.25% |
| `close_to_ma50` | 6,936 | 0.56% |
| `return_20d` | 5,780 | 0.47% |
| `volatility_20d` | 2,890 | 0.23% |
| `return_5d` | 1,445 | 0.12% |
| `return_1d` | 289 | 0.02% |
| `pct_change_1d` | 289 | 0.02% |

---

## Symbols with Thin Coverage (< 250 trading days)

| Symbol | First Date | Last Date | Trading Days |
|---|---|---|---|

---

## Per-Symbol Coverage Stats

| Stat | Value |
|---|---|
| Mean trading days per symbol | 4270 |
| Median trading days per symbol | 4270 |
| Min trading days | 4270 |
| Max trading days | 4270 |
| Symbols with full 10+ year coverage | 289 |
| Symbols with OHLC violations | 11 |

---

## Known Limitations

- `usd_lkr` is **annual** (World Bank) — forward-filled to daily; not daily granularity
- `interest_rates.csv` is a placeholder — T-bill rates require manual CBSL download
- `adj_close` equals `close` — dividend amounts not yet available from the CSE API
- Symbol-level sentiment (`vader_score_mean`) is absent — CSE news records lack dates
- LBO sentiment covers only 2021–present; pre-2021 market sentiment is null
- `finbert_label` is VADER-threshold-mapped, not true FinBERT inference
