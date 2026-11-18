# CSE Dataset - Data Quality Report

Generated: 2026-11-18T02:21:01Z

## Summary

| Metric | Value |
|---|---|
| Total rows | 1,276,269 |
| Symbols | 303 |
| Date range | 2010-01-01 to 2026-11-18 |
| Columns | 46 |
| Duplicate `(symbol, date)` rows | 0 |
| OHLC-invalid rows | 0 (0.00%) |
| Source OHLC-invalid rows | 41,538 |
| OHLC-repaired rows | 41,538 |
| `volume_zscore` null rate | 0.00% |
| Adjusted-close rows | 0 |
| Adjusted-close symbols | 0 |
| Dividend rows with amount | 0 / 1,776 |
| Interest-rate source rows | 0 / 0 |
| Interest-rate max date | n/a |
| Interest-rate staleness | n/a days |
| Rows with T-bill 3M | 0 |
| Rows with policy rate | 0 |
| Rows with symbol sentiment | 0 |
| Symbols with sentiment | 0 |
| Rows with macro data (sp500 non-null) | 1,224,398 |
| Rows with market sentiment | 176,066 |
| Max-date staleness | 0 days |

## Validation Gates

- PASS: all configured quality gates passed

## Null Values by Column

| Column | Null Count | Null % |
|---|---|---|
| `policy_rate` | 1,276,269 | 100.0% |
| `vader_score_mean` | 1,276,269 | 100.0% |
| `vader_score_max` | 1,276,269 | 100.0% |
| `vader_label` | 1,276,269 | 100.0% |
| `finbert_label` | 1,276,269 | 100.0% |
| `tbill_6m` | 1,276,269 | 100.0% |
| `tbill_3m` | 1,276,269 | 100.0% |
| `tbill_12m` | 1,276,269 | 100.0% |
| `market_vader_mean` | 1,100,203 | 86.2% |
| `market_news_count` | 1,100,203 | 86.2% |
| `gdp_growth_pct` | 51,871 | 4.06% |
| `sp500` | 51,871 | 4.06% |
| `usd_lkr` | 51,871 | 4.06% |
| `nikkei225` | 51,871 | 4.06% |
| `inflation_pct` | 51,871 | 4.06% |
| `hangseng` | 51,871 | 4.06% |
| `close_to_ma200` | 29,329 | 2.3% |
| `close_to_ma50` | 7,146 | 0.56% |
| `return_20d` | 5,962 | 0.47% |
| `volatility_20d` | 3,002 | 0.24% |
| `return_5d` | 1,513 | 0.12% |
| `pct_change_1d` | 460 | 0.04% |
| `return_1d` | 460 | 0.04% |

## Symbols with Thin Coverage (< 250 trading days)

| Symbol | First Date | Last Date | Trading Days |
|---|---|---|---|
| AAF.R0000 | 2026-08-14 | 2026-08-21 | 6 |
| CHL.N0000 | 2026-03-02 | 2026-11-18 | 188 |
| CHL.X0000 | 2026-03-02 | 2026-11-18 | 182 |
| CINS.N0000 | 2026-03-02 | 2026-11-18 | 152 |
| CPRT.R0000 | 2026-10-19 | 2026-10-26 | 6 |
| HNBF.R0000 | 2026-06-10 | 2026-06-18 | 7 |
| HNBF.R0001 | 2026-06-10 | 2026-06-18 | 7 |
| JXG.N0000 | 2026-03-02 | 2026-11-18 | 188 |
| MBSL.R0001 | 2026-07-21 | 2026-07-29 | 7 |
| NAMU.N0000 | 2026-03-02 | 2026-11-18 | 186 |
| SFIN.R0000 | 2026-10-30 | 2026-11-06 | 6 |
| SING.N0000 | 2026-07-23 | 2026-11-18 | 82 |
| TAJ.R0000 | 2026-11-16 | 2026-11-18 | 3 |

## Known Limitations

- `usd_lkr` is annual World Bank data forward-filled to daily rows.
- `interest_rates.csv` is populated from a manual CBSL CSV/XLSX import under `data/raw/macro/`.
- `adj_close` applies only dividend rows with parsed `amount_per_share`; missing amounts are reported.
- `vader_label` is derived from VADER thresholds; true `finbert_label` is reserved for model inference.
- Symbol-level sentiment is partial and depends on dated CSE announcement records.
- `source_*` OHLC columns preserve original CSE values where high/low repairs were needed.
