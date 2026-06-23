# CSE Dataset - Data Quality Report

Generated: 2026-06-23T21:51:44Z

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,246,557 |
| Symbols | 297 |
| Date range | 2010-01-01 to 2026-06-23 |
| Columns | 46 |
| Duplicate `(symbol, date)` rows | 0 |
| OHLC-invalid rows | 0 (0.00%) |
| Source OHLC-invalid rows | 39,252 |
| OHLC-repaired rows | 39,252 |
| `volume_zscore` null rate | 0.00% |
| Adjusted-close rows | 0 |
| Adjusted-close symbols | 0 |
| Dividend rows with amount | 0 / 1,685 |
| Interest-rate source rows | 0 / 0 |
| Interest-rate max date | n/a |
| Interest-rate staleness | n/a days |
| Rows with T-bill 3M | 0 |
| Rows with policy rate | 0 |
| Rows with symbol sentiment | 0 |
| Symbols with sentiment | 0 |
| Rows with macro data (sp500 non-null) | 1,224,398 |
| Rows with market sentiment | 178,747 |
| Max-date staleness | 0 days |

## Validation Gates

- PASS: all configured quality gates passed

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `policy_rate` | 1,246,557 | 100.0% |
| `vader_score_mean` | 1,246,557 | 100.0% |
| `vader_score_max` | 1,246,557 | 100.0% |
| `vader_label` | 1,246,557 | 100.0% |
| `finbert_label` | 1,246,557 | 100.0% |
| `tbill_6m` | 1,246,557 | 100.0% |
| `tbill_3m` | 1,246,557 | 100.0% |
| `tbill_12m` | 1,246,557 | 100.0% |
| `market_vader_mean` | 1,067,810 | 85.66% |
| `market_news_count` | 1,067,810 | 85.66% |
| `usd_lkr` | 112,077 | 8.99% |
| `gdp_growth_pct` | 36,097 | 2.9% |
| `inflation_pct` | 36,097 | 2.9% |
| `close_to_ma200` | 29,129 | 2.34% |
| `nikkei225` | 22,159 | 1.78% |
| `hangseng` | 22,159 | 1.78% |
| `sp500` | 22,159 | 1.78% |
| `close_to_ma50` | 7,094 | 0.57% |
| `return_20d` | 5,914 | 0.47% |
| `volatility_20d` | 2,964 | 0.24% |
| `return_5d` | 1,485 | 0.12% |
| `pct_change_1d` | 297 | 0.02% |
| `return_1d` | 297 | 0.02% |

## Symbols with Thin Coverage (< 250 trading days)

| Symbol | First Date | Last Date | Trading Days |
|---|---|---|---|
| CHL.N0000 | 2026-03-02 | 2026-06-23 | 82 |
| CHL.X0000 | 2026-03-02 | 2026-06-23 | 82 |
| CINS.N0000 | 2026-03-02 | 2026-06-23 | 77 |
| HNBF.R0000 | 2026-06-10 | 2026-06-18 | 7 |
| HNBF.R0001 | 2026-06-10 | 2026-06-18 | 7 |
| JXG.N0000 | 2026-03-02 | 2026-06-23 | 82 |
| NAMU.N0000 | 2026-03-02 | 2026-06-23 | 82 |

## Known Limitations

- `usd_lkr` is annual World Bank data forward-filled to daily rows.
- `interest_rates.csv` is populated from a manual CBSL CSV/XLSX import under `data/raw/macro/`.
- `adj_close` applies only dividend rows with parsed `amount_per_share`; missing amounts are reported.
- `vader_label` is derived from VADER thresholds; true `finbert_label` is reserved for model inference.
- Symbol-level sentiment is partial and depends on dated CSE announcement records.
- `source_*` OHLC columns preserve original CSE values where high/low repairs were needed.
