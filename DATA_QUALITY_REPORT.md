# CSE Dataset — Data Quality Report

Generated: 2026-05-08 21:17

---

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,262,440 |
| Symbols | 296 |
| Date range | 2010-01-01 to 2026-05-07 |
| Columns | 30 |
| Trading-day rows (volume > 0) | 1,262,440 (100.0%) |
| OHLC-invalid rows | 51,180 (4.05%) |
| Outlier rows (\|pct_change\| > 50%) | 0 |
| Rows with macro data (sp500 non-null) | 0 (0.0%) |
| Rows with market sentiment | 179,672 (14.2%) |

---

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `volume_zscore` | 1,262,440 | 100.0% |
| `finbert_label` | 1,262,440 | 100.0% |
| `vader_score_max` | 1,262,440 | 100.0% |
| `vader_score_mean` | 1,262,440 | 100.0% |
| `market_vader_mean` | 1,082,768 | 85.77% |
| `market_news_count` | 1,082,768 | 85.77% |
| `usd_lkr` | 104,488 | 8.28% |
| `close_to_ma200` | 29,304 | 2.32% |
| `inflation_pct` | 26,936 | 2.13% |
| `gdp_growth_pct` | 26,936 | 2.13% |
| `close_to_ma50` | 7,104 | 0.56% |
| `return_20d` | 5,920 | 0.47% |
| `volatility_20d` | 2,960 | 0.23% |
| `return_5d` | 1,480 | 0.12% |
| `return_1d` | 296 | 0.02% |
| `pct_change_1d` | 296 | 0.02% |

---

## Symbols with Thin Coverage (< 250 trading days)

| Symbol | First Date | Last Date | Trading Days |
|---|---|---|---|

---

## Per-Symbol Coverage Stats

| Stat | Value |
|---|---|
| Mean trading days per symbol | 4265 |
| Median trading days per symbol | 4265 |
| Min trading days | 4265 |
| Max trading days | 4265 |
| Symbols with full 10+ year coverage | 296 |
| Symbols with OHLC violations | 12 |

---

## Known Limitations

- `usd_lkr` is **annual** (World Bank) — forward-filled to daily; not daily granularity
- `interest_rates.csv` is a placeholder — T-bill rates require manual CBSL download
- `adj_close` equals `close` — dividend amounts not yet available from the CSE API
- Symbol-level sentiment (`vader_score_mean`) is absent — CSE news records lack dates
- LBO sentiment covers only 2021–present; pre-2021 market sentiment is null
- `finbert_label` is VADER-threshold-mapped, not true FinBERT inference
