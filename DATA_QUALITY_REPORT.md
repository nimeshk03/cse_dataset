# CSE Dataset - Data Quality Report

Generated: 2026-05-26T21:55:15Z

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,240,806 |
| Symbols | 295 |
| Date range | 2010-01-01 to 2026-05-26 |
| Columns | 46 |
| Duplicate `(symbol, date)` rows | 0 |
| OHLC-invalid rows | 0 (0.00%) |
| Source OHLC-invalid rows | 38,936 |
| OHLC-repaired rows | 38,936 |
| `volume_zscore` null rate | 0.00% |
| Adjusted-close rows | 0 |
| Adjusted-close symbols | 0 |
| Dividend rows with amount | 0 / 1,656 |
| Interest-rate source rows | 0 / 0 |
| Interest-rate max date | n/a |
| Interest-rate staleness | n/a days |
| Rows with T-bill 3M | 0 |
| Rows with policy rate | 0 |
| Rows with symbol sentiment | 0 |
| Symbols with sentiment | 0 |
| Rows with macro data (sp500 non-null) | 1,224,398 |
| Rows with market sentiment | 178,506 |
| Max-date staleness | 0 days |

## Validation Gates

- PASS: all configured quality gates passed

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `policy_rate` | 1,240,806 | 100.0% |
| `vader_score_mean` | 1,240,806 | 100.0% |
| `vader_score_max` | 1,240,806 | 100.0% |
| `vader_label` | 1,240,806 | 100.0% |
| `finbert_label` | 1,240,806 | 100.0% |
| `tbill_6m` | 1,240,806 | 100.0% |
| `tbill_3m` | 1,240,806 | 100.0% |
| `tbill_12m` | 1,240,806 | 100.0% |
| `market_vader_mean` | 1,062,300 | 85.61% |
| `market_news_count` | 1,062,300 | 85.61% |
| `usd_lkr` | 106,326 | 8.57% |
| `gdp_growth_pct` | 30,346 | 2.45% |
| `inflation_pct` | 30,346 | 2.45% |
| `close_to_ma200` | 29,020 | 2.34% |
| `nikkei225` | 16,408 | 1.32% |
| `hangseng` | 16,408 | 1.32% |
| `sp500` | 16,408 | 1.32% |
| `close_to_ma50` | 7,080 | 0.57% |
| `return_20d` | 5,900 | 0.48% |
| `volatility_20d` | 2,950 | 0.24% |
| `return_5d` | 1,475 | 0.12% |
| `pct_change_1d` | 295 | 0.02% |
| `return_1d` | 295 | 0.02% |

## Symbols with Thin Coverage (< 250 trading days)

| Symbol | First Date | Last Date | Trading Days |
|---|---|---|---|
| CHL.N0000 | 2026-03-02 | 2026-05-26 | 62 |
| CHL.X0000 | 2026-03-02 | 2026-05-26 | 62 |
| CINS.N0000 | 2026-03-02 | 2026-05-26 | 62 |
| JXG.N0000 | 2026-03-02 | 2026-05-26 | 62 |
| NAMU.N0000 | 2026-03-02 | 2026-05-26 | 62 |

## Known Limitations

- `usd_lkr` is annual World Bank data forward-filled to daily rows.
- `interest_rates.csv` is populated from a manual CBSL CSV/XLSX import under `data/raw/macro/`.
- `adj_close` applies only dividend rows with parsed `amount_per_share`; missing amounts are reported.
- `vader_label` is derived from VADER thresholds; true `finbert_label` is reserved for model inference.
- Symbol-level sentiment is partial and depends on dated CSE announcement records.
- `source_*` OHLC columns preserve original CSE values where high/low repairs were needed.
