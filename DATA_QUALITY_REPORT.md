# CSE Dataset — Data Quality Report

Generated: 2026-04-28 21:20

---

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,221,759 |
| Symbols | 287 |
| Date range | 2010-01-01 to 2026-04-27 |
| Columns | 30 |
| Trading-day rows (volume > 0) | 1,221,759 (100.0%) |
| OHLC-invalid rows | 55,341 (4.53%) |
| Outlier rows (\|pct_change\| > 50%) | 0 |
| Rows with macro data (sp500 non-null) | 0 (0.0%) |
| Rows with market sentiment | 49,938 (4.1%) |

---

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `volume_zscore` | 1,221,759 | 100.0% |
| `finbert_label` | 1,221,759 | 100.0% |
| `vader_score_max` | 1,221,759 | 100.0% |
| `vader_score_mean` | 1,221,759 | 100.0% |
| `market_vader_mean` | 1,171,821 | 95.91% |
| `market_news_count` | 1,171,821 | 95.91% |
| `usd_lkr` | 99,015 | 8.1% |
| `close_to_ma200` | 28,413 | 2.33% |
| `inflation_pct` | 23,821 | 1.95% |
| `gdp_growth_pct` | 23,821 | 1.95% |
| `close_to_ma50` | 6,888 | 0.56% |
| `return_20d` | 5,740 | 0.47% |
| `volatility_20d` | 2,870 | 0.23% |
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
| Mean trading days per symbol | 4257 |
| Median trading days per symbol | 4257 |
| Min trading days | 4257 |
| Max trading days | 4257 |
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
