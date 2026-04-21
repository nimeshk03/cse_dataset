# CSE Dataset — Data Quality Report

Generated: 2026-04-21 21:08

---

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,254,340 |
| Symbols | 295 |
| Date range | 2010-01-01 to 2026-04-20 |
| Columns | 30 |
| Trading-day rows (volume > 0) | 1,254,340 (100.0%) |
| OHLC-invalid rows | 38,268 (3.05%) |
| Outlier rows (\|pct_change\| > 50%) | 0 |
| Rows with macro data (sp500 non-null) | 0 (0.0%) |
| Rows with market sentiment | 179,655 (14.3%) |

---

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `volume_zscore` | 1,254,340 | 100.0% |
| `finbert_label` | 1,254,340 | 100.0% |
| `vader_score_max` | 1,254,340 | 100.0% |
| `vader_score_mean` | 1,254,340 | 100.0% |
| `market_vader_mean` | 1,074,685 | 85.68% |
| `market_news_count` | 1,074,685 | 85.68% |
| `usd_lkr` | 100,300 | 8.0% |
| `close_to_ma200` | 29,205 | 2.33% |
| `inflation_pct` | 23,010 | 1.83% |
| `gdp_growth_pct` | 23,010 | 1.83% |
| `close_to_ma50` | 7,080 | 0.56% |
| `return_20d` | 5,900 | 0.47% |
| `volatility_20d` | 2,950 | 0.24% |
| `return_5d` | 1,475 | 0.12% |
| `return_1d` | 295 | 0.02% |
| `pct_change_1d` | 295 | 0.02% |

---

## Symbols with Thin Coverage (< 250 trading days)

| Symbol | First Date | Last Date | Trading Days |
|---|---|---|---|

---

## Per-Symbol Coverage Stats

| Stat | Value |
|---|---|
| Mean trading days per symbol | 4252 |
| Median trading days per symbol | 4252 |
| Min trading days | 4252 |
| Max trading days | 4252 |
| Symbols with full 10+ year coverage | 295 |
| Symbols with OHLC violations | 9 |

---

## Known Limitations

- `usd_lkr` is **annual** (World Bank) — forward-filled to daily; not daily granularity
- `interest_rates.csv` is a placeholder — T-bill rates require manual CBSL download
- `adj_close` equals `close` — dividend amounts not yet available from the CSE API
- Symbol-level sentiment (`vader_score_mean`) is absent — CSE news records lack dates
- LBO sentiment covers only 2021–present; pre-2021 market sentiment is null
- `finbert_label` is VADER-threshold-mapped, not true FinBERT inference
