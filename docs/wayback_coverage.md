# Wayback Machine Coverage

*Probed on 2026-03-02*

## Status: BLOCKED

Attempts to probe the Wayback Machine CDX API (`web.archive.org/cdx/search/cdx`) consistently resulted in `TIMEOUT` errors during Phase 0 reconnaissance.

This indicates that `web.archive.org` is blocked either by the local ISP or a network firewall on the machine executing the data collection.

## Pivot Strategy

Fortunately, during deep-dive reconnaissance using Playwright to intercept network traffic on `cse.lk`, we discovered an undocumented internal REST API (`/api/tradeSummary`). 

By sending a `POST` request with `multipart/form-data` containing a `date` parameter (e.g., `2012-08-14`), the CSE server returns the complete market summary for that day, including the OHLCV data for all listed equities.

Because this native, structured API is available and functions correctly for historical dates deep into the past (tested back to 2012), **we no longer need to rely on the Wayback Machine to fill historical price gaps.**

The historical price collection strategy in Phase 2 will exclusively use the internal CSE `tradeSummary` API.
