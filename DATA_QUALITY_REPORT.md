# CSE Dataset — Data Quality Report

Generated: 2026-04-15 21:06

---

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,223,424 |
| Symbols | 288 |
| Date range | 2010-01-01 to 2026-04-14 |
| Columns | 30 |
| Trading-day rows (volume > 0) | 1,223,424 (100.0%) |
| OHLC-invalid rows | 29,736 (2.43%) |
| Outlier rows (\|pct_change\| > 50%) | 0 |
| Rows with macro data (sp500 non-null) | 0 (0.0%) |
| Rows with market sentiment | 175,392 (14.3%) |

---

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `volume_zscore` | 1,223,424 | 100.0% |
| `finbert_label` | 1,223,424 | 100.0% |
| `vader_score_max` | 1,223,424 | 100.0% |
| `vader_score_mean` | 1,223,424 | 100.0% |
| `market_vader_mean` | 1,048,032 | 85.66% |
| `market_news_count` | 1,048,032 | 85.66% |
| `usd_lkr` | 96,768 | 7.91% |
| `close_to_ma200` | 28,512 | 2.33% |
| `inflation_pct` | 21,312 | 1.74% |
| `gdp_growth_pct` | 21,312 | 1.74% |
| `close_to_ma50` | 6,912 | 0.56% |
| `return_20d` | 5,760 | 0.47% |
| `volatility_20d` | 2,880 | 0.24% |
| `return_5d` | 1,440 | 0.12% |
| `return_1d` | 288 | 0.02% |
| `pct_change_1d` | 288 | 0.02% |

---

## Symbols with Thin Coverage (< 250 trading days)

| Symbol | First Date | Last Date | Trading Days |
|---|---|---|---|

---

## Per-Symbol Coverage Stats

| Stat | Value |
|---|---|
| Mean trading days per symbol | 4248 |
| Median trading days per symbol | 4248 |
| Min trading days | 4248 |
| Max trading days | 4248 |
| Symbols with full 10+ year coverage | 288 |
| Symbols with OHLC violations | 7 |

---

## Known Limitations

- `usd_lkr` is **annual** (World Bank) — forward-filled to daily; not daily granularity
- `interest_rates.csv` is a placeholder — T-bill rates require manual CBSL download
- `adj_close` equals `close` — dividend amounts not yet available from the CSE API
- Symbol-level sentiment (`vader_score_mean`) is absent — CSE news records lack dates
- LBO sentiment covers only 2021–present; pre-2021 market sentiment is null
- `finbert_label` is VADER-threshold-mapped, not true FinBERT inference
