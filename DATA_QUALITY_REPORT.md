# CSE Dataset — Data Quality Report

Generated: 2026-04-09 21:08

---

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,196,808 |
| Symbols | 282 |
| Date range | 2010-01-01 to 2026-04-08 |
| Columns | 30 |
| Trading-day rows (volume > 0) | 1,196,808 (100.0%) |
| OHLC-invalid rows | 59,416 (4.96%) |
| Outlier rows (\|pct_change\| > 50%) | 0 |
| Rows with macro data (sp500 non-null) | 0 (0.0%) |
| Rows with market sentiment | 172,020 (14.4%) |

---

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `volume_zscore` | 1,196,808 | 100.0% |
| `finbert_label` | 1,196,808 | 100.0% |
| `vader_score_max` | 1,196,808 | 100.0% |
| `vader_score_mean` | 1,196,808 | 100.0% |
| `market_vader_mean` | 1,024,788 | 85.63% |
| `market_news_count` | 1,024,788 | 85.63% |
| `usd_lkr` | 93,624 | 7.82% |
| `close_to_ma200` | 27,918 | 2.33% |
| `inflation_pct` | 19,740 | 1.65% |
| `gdp_growth_pct` | 19,740 | 1.65% |
| `close_to_ma50` | 6,768 | 0.57% |
| `return_20d` | 5,640 | 0.47% |
| `volatility_20d` | 2,820 | 0.24% |
| `return_5d` | 1,410 | 0.12% |
| `return_1d` | 282 | 0.02% |
| `pct_change_1d` | 282 | 0.02% |

---

## Symbols with Thin Coverage (< 250 trading days)

| Symbol | First Date | Last Date | Trading Days |
|---|---|---|---|

---

## Per-Symbol Coverage Stats

| Stat | Value |
|---|---|
| Mean trading days per symbol | 4244 |
| Median trading days per symbol | 4244 |
| Min trading days | 4244 |
| Max trading days | 4244 |
| Symbols with full 10+ year coverage | 282 |
| Symbols with OHLC violations | 14 |

---

## Known Limitations

- `usd_lkr` is **annual** (World Bank) — forward-filled to daily; not daily granularity
- `interest_rates.csv` is a placeholder — T-bill rates require manual CBSL download
- `adj_close` equals `close` — dividend amounts not yet available from the CSE API
- Symbol-level sentiment (`vader_score_mean`) is absent — CSE news records lack dates
- LBO sentiment covers only 2021–present; pre-2021 market sentiment is null
- `finbert_label` is VADER-threshold-mapped, not true FinBERT inference
