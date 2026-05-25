# CSE Dataset — Data Quality Report

Generated: 2026-05-25 21:25

---

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,240,040 |
| Symbols | 290 |
| Date range | 2010-01-01 to 2026-05-22 |
| Columns | 30 |
| Trading-day rows (volume > 0) | 1,240,040 (100.0%) |
| OHLC-invalid rows | 38,484 (3.10%) |
| Outlier rows (\|pct_change\| > 50%) | 0 |
| Rows with macro data (sp500 non-null) | 0 (0.0%) |
| Rows with market sentiment | 177,770 (14.3%) |

---

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `volume_zscore` | 1,240,040 | 100.0% |
| `finbert_label` | 1,240,040 | 100.0% |
| `vader_score_max` | 1,240,040 | 100.0% |
| `vader_score_mean` | 1,240,040 | 100.0% |
| `market_vader_mean` | 1,062,270 | 85.66% |
| `market_news_count` | 1,062,270 | 85.66% |
| `usd_lkr` | 105,560 | 8.51% |
| `inflation_pct` | 29,580 | 2.39% |
| `gdp_growth_pct` | 29,580 | 2.39% |
| `close_to_ma200` | 28,710 | 2.32% |
| `close_to_ma50` | 6,960 | 0.56% |
| `return_20d` | 5,800 | 0.47% |
| `volatility_20d` | 2,900 | 0.23% |
| `return_5d` | 1,450 | 0.12% |
| `return_1d` | 290 | 0.02% |
| `pct_change_1d` | 290 | 0.02% |

---

## Symbols with Thin Coverage (< 250 trading days)

| Symbol | First Date | Last Date | Trading Days |
|---|---|---|---|

---

## Per-Symbol Coverage Stats

| Stat | Value |
|---|---|
| Mean trading days per symbol | 4276 |
| Median trading days per symbol | 4276 |
| Min trading days | 4276 |
| Max trading days | 4276 |
| Symbols with full 10+ year coverage | 290 |
| Symbols with OHLC violations | 9 |

---

## Known Limitations

- `usd_lkr` is **annual** (World Bank) — forward-filled to daily; not daily granularity
- `interest_rates.csv` is a placeholder — T-bill rates require manual CBSL download
- `adj_close` equals `close` — dividend amounts not yet available from the CSE API
- Symbol-level sentiment (`vader_score_mean`) is absent — CSE news records lack dates
- LBO sentiment covers only 2021–present; pre-2021 market sentiment is null
- `finbert_label` is VADER-threshold-mapped, not true FinBERT inference
