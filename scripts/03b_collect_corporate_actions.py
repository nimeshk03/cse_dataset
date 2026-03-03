import requests
import pandas as pd
import time
import logging
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def fetch_corporate_calendar(year, month):
    url = 'https://www.cse.lk/api/corporateCalender'
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        # Based on testing, data dict with year and month works
        r = requests.post(url, data={'year': str(year), 'month': str(month)}, headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            return data.get('approvedCoopCalAnnouncements', [])
    except Exception as e:
        logging.error(f"Error fetching {year}-{month}: {e}")
    return []

def collect_corporate_actions():
    os.makedirs('data/raw/fundamentals', exist_ok=True)
    os.makedirs('data/processed/fundamentals', exist_ok=True)
    
    # We will fetch data from 2010 to 2026.
    years = range(2010, 2027)
    months = range(1, 13)
    
    tasks = [(y, m) for y in years for m in months]
    logging.info(f"Fetching corporate actions for {len(tasks)} months...")
    
    all_events = []
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(fetch_corporate_calendar, y, m): (y, m) for (y, m) in tasks}
        
        for future in as_completed(futures):
            events = future.result()
            if events:
                all_events.extend(events)
                
    logging.info(f"Found {len(all_events)} total corporate actions.")
    
    if len(all_events) == 0:
        return
        
    df = pd.DataFrame(all_events)
    
    # Drop duplicates just in case there's overlap in the API responses
    if 'id' in df.columns:
        df = df.drop_duplicates(subset=['id'])
    
    df.to_csv('data/raw/fundamentals/all_corporate_actions_raw.csv', index=False)
    
    # Filter for dividends and splits (Subdivision of shares)
    dividends = df[df['announcementCategory'].str.contains('DIVIDEND', na=False, case=False)]
    splits = df[df['announcementCategory'].str.contains('SUBDIVISION|SPLIT', na=False, case=False)]
    
    logging.info(f"Filtered {len(dividends)} dividends and {len(splits)} splits.")
    
    dividends.to_csv('data/processed/fundamentals/dividends.csv', index=False)
    splits.to_csv('data/processed/fundamentals/splits.csv', index=False)
    
if __name__ == '__main__':
    collect_corporate_actions()
