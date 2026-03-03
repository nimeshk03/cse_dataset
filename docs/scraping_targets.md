# Scraping Targets

*Probed and confirmed on 2026-03-02*

Based on Phase 0 reconnaissance, third-party APIs (Yahoo Finance, Alpha Vantage, Finnhub) do not cover CSE stocks. Furthermore, the Wayback Machine is blocked on the current network. 

However, during Playwright interception analysis, we discovered **undocumented internal CSE REST APIs** that provide full historical data without requiring complex DOM scraping or PDF parsing.

## 1. CSE Daily Market Summary (Hidden API)

This is the most critical discovery. Instead of downloading and parsing Daily Market Summary PDFs (which are prone to OCR errors and format changes), we can directly hit the API that powers the daily summary page.

* **Endpoint**: `https://www.cse.lk/api/tradeSummary`
* **Method**: POST
* **Payload**: `multipart/form-data` with a single field `date` (format: `YYYY-MM-DD`)
* **Response**: A JSON object containing the `reqTradeSummery` array. This array contains the OHLCV data for *every single listed equity* for that specific date.
* **Coverage**: Tested back to 2012. It returns accurate historical data for all stocks that traded on that day.
* **Fields Extracted**: `symbol`, `open`, `high`, `low`, `closingPrice`, `sharevolume`, `tradevolume`, `turnover`, `percentageChange`.

**Data Collection Strategy (Phase 2):**
To build the historical price database, we will iterate through all trading days from 2010 to present and call this API for each day. This completely eliminates the need for `pdfplumber` and provides structured, clean data instantly.

## 2. LBO (Lanka Business Online) Archive

LBO uses WordPress, and their REST API is fully exposed and functional.

* **Endpoint**: `https://www.lankabusinessonline.com/wp-json/wp/v2/posts`
* **Method**: GET
* **Params**: `per_page` (max 100), `page`, `orderby=date`, `order=desc|asc`
* **Coverage**: The API reports 1,438 total posts spanning from **2021-03-30 to present**. 
* **Data Extraction**: The JSON response contains the full article date, title, URL, and HTML content. No BeautifulSoup scraping is required.

## 3. Daily FT Archive

Daily FT is a server-rendered site and does not expose a WordPress REST API. It requires traditional HTML scraping.

* **Target URL**: `https://www.ft.lk/front-page/page/{n}` and `https://www.ft.lk/business/page/{n}`
* **Method**: GET (requires standard `User-Agent` headers)
* **Extraction Strategy**: Use BeautifulSoup to parse the `<article>` or list items. Dates, headlines, and URLs must be extracted from the DOM.
* **Note**: We will implement this in Phase 4.

## 4. Annual Reports

* **Target**: `cse.lk/company/financial-reports/{SYMBOL}`
* **Strategy**: We will use Playwright to locate the PDF download links for the top 50 market-cap companies, download them, and use `pdfplumber` to extract historical EPS, NAV, and revenue.

## Abandoned Targets (Due to limitations)
* **Wayback Machine**: API times out on the current network. Abandoned in favor of the internal CSE API.
* **Yahoo / Alpha Vantage / Finnhub**: CSE tickers are not listed on these platforms. Abandoned.
* **Daily Market Summary PDFs**: Abandoned in favor of the internal `tradeSummary` API which provides the exact same data in structured JSON format.
