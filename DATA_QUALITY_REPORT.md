# CSE Dataset — Data Quality Report

Generated: 2026-05-07 21:19

---

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,253,616 |
| Symbols | 294 |
| Date range | 2010-01-01 to 2026-05-06 |
| Columns | 30 |
| Trading-day rows (volume > 0) | 1,253,616 (100.0%) |
| OHLC-invalid rows | 29,848 (2.38%) |
| Outlier rows (\|pct_change\| > 50%) | 0 |
| Rows with macro data (sp500 non-null) | 0 (0.0%) |
| Rows with market sentiment | 178,752 (14.3%) |

---

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `volume_zscore` | 1,253,616 | 100.0% |
| `finbert_label` | 1,253,616 | 100.0% |
| `vader_score_max` | 1,253,616 | 100.0% |
| `vader_score_mean` | 1,253,616 | 100.0% |
| `market_vader_mean` | 1,074,864 | 85.74% |
| `market_news_count` | 1,074,864 | 85.74% |
| `usd_lkr` | 103,488 | 8.26% |
| `close_to_ma200` | 29,106 | 2.32% |
| `inflation_pct` | 26,460 | 2.11% |
| `gdp_growth_pct` | 26,460 | 2.11% |
| `close_to_ma50` | 7,056 | 0.56% |
| `return_20d` | 5,880 | 0.47% |
| `volatility_20d` | 2,940 | 0.23% |
| `return_5d` | 1,470 | 0.12% |
| `return_1d` | 294 | 0.02% |
| `pct_change_1d` | 294 | 0.02% |

---

## Symbols with Thin Coverage (< 250 trading days)

| Symbol | First Date | Last Date | Trading Days |
|---|---|---|---|

---

## Per-Symbol Coverage Stats

| Stat | Value |
|---|---|
| Mean trading days per symbol | 4264 |
| Median trading days per symbol | 4264 |
| Min trading days | 4264 |
| Max trading days | 4264 |
| Symbols with full 10+ year coverage | 294 |
| Symbols with OHLC violations | 7 |

---

## Known Limitations

- `usd_lkr` is **annual** (World Bank) — forward-filled to daily; not daily granularity
- `interest_rates.csv` is a placeholder — T-bill rates require manual CBSL download
- `adj_close` equals `close` — dividend amounts not yet available from the CSE API
- Symbol-level sentiment (`vader_score_mean`) is absent — CSE news records lack dates
- LBO sentiment covers only 2021–present; pre-2021 market sentiment is null
- `finbert_label` is VADER-threshold-mapped, not true FinBERT inference
