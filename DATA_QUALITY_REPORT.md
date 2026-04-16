# CSE Dataset — Data Quality Report

Generated: 2026-04-16 21:05

---

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,227,961 |
| Symbols | 289 |
| Date range | 2010-01-01 to 2026-04-15 |
| Columns | 30 |
| Trading-day rows (volume > 0) | 1,227,961 (100.0%) |
| OHLC-invalid rows | 46,739 (3.81%) |
| Outlier rows (\|pct_change\| > 50%) | 0 |
| Rows with macro data (sp500 non-null) | 0 (0.0%) |
| Rows with market sentiment | 176,290 (14.4%) |

---

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `volume_zscore` | 1,227,961 | 100.0% |
| `finbert_label` | 1,227,961 | 100.0% |
| `vader_score_max` | 1,227,961 | 100.0% |
| `vader_score_mean` | 1,227,961 | 100.0% |
| `market_vader_mean` | 1,051,671 | 85.64% |
| `market_news_count` | 1,051,671 | 85.64% |
| `usd_lkr` | 97,393 | 7.93% |
| `close_to_ma200` | 28,611 | 2.33% |
| `inflation_pct` | 21,675 | 1.77% |
| `gdp_growth_pct` | 21,675 | 1.77% |
| `close_to_ma50` | 6,936 | 0.56% |
| `return_20d` | 5,780 | 0.47% |
| `volatility_20d` | 2,890 | 0.24% |
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
| Mean trading days per symbol | 4249 |
| Median trading days per symbol | 4249 |
| Min trading days | 4249 |
| Max trading days | 4249 |
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
