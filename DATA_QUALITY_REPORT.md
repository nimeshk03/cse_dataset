# CSE Dataset — Data Quality Report

Generated: 2026-04-17 21:02

---

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,249,500 |
| Symbols | 294 |
| Date range | 2010-01-01 to 2026-04-16 |
| Columns | 30 |
| Trading-day rows (volume > 0) | 1,249,500 (100.0%) |
| OHLC-invalid rows | 34,000 (2.72%) |
| Outlier rows (\|pct_change\| > 50%) | 0 |
| Rows with macro data (sp500 non-null) | 0 (0.0%) |
| Rows with market sentiment | 179,046 (14.3%) |

---

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `volume_zscore` | 1,249,500 | 100.0% |
| `finbert_label` | 1,249,500 | 100.0% |
| `vader_score_max` | 1,249,500 | 100.0% |
| `vader_score_mean` | 1,249,500 | 100.0% |
| `market_vader_mean` | 1,070,454 | 85.67% |
| `market_news_count` | 1,070,454 | 85.67% |
| `usd_lkr` | 99,372 | 7.95% |
| `close_to_ma200` | 29,106 | 2.33% |
| `inflation_pct` | 22,344 | 1.79% |
| `gdp_growth_pct` | 22,344 | 1.79% |
| `close_to_ma50` | 7,056 | 0.56% |
| `return_20d` | 5,880 | 0.47% |
| `volatility_20d` | 2,940 | 0.24% |
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
| Mean trading days per symbol | 4250 |
| Median trading days per symbol | 4250 |
| Min trading days | 4250 |
| Max trading days | 4250 |
| Symbols with full 10+ year coverage | 294 |
| Symbols with OHLC violations | 8 |

---

## Known Limitations

- `usd_lkr` is **annual** (World Bank) — forward-filled to daily; not daily granularity
- `interest_rates.csv` is a placeholder — T-bill rates require manual CBSL download
- `adj_close` equals `close` — dividend amounts not yet available from the CSE API
- Symbol-level sentiment (`vader_score_mean`) is absent — CSE news records lack dates
- LBO sentiment covers only 2021–present; pre-2021 market sentiment is null
- `finbert_label` is VADER-threshold-mapped, not true FinBERT inference
