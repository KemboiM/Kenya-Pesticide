# scraper/fetch_pesticides_kenya.py

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def fetch_tables_from_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"❌ Failed to fetch {url} — Status Code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table")

    if not table:
        print(f"⚠️ No table found on {url}")
        return None

    # Extract headers
    headers = [th.get_text(strip=True) for th in table.find_all("th")]

    # Extract rows
    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = [td.get_text(strip=True) for td in tr.find_all("td")]
        if cells:
            rows.append(cells)

    return pd.DataFrame(rows, columns=headers if headers else None)


def scrape_all_pages(base_url, page_param="page", max_pages=50, delay=1):
    all_data = []

    for page_num in range(1, max_pages + 1):
        full_url = "https://www.pcpb.go.ke/pesticides"
        print(f"🔍 Scraping: {full_url}")
        df = fetch_tables_from_url(full_url)

        if df is None or df.empty:
            print("✅ No more data or end of pages.")
            break

        all_data.append(df)
        time.sleep(delay)

    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        combined_df.to_csv("kenya_pesticides.csv", index=False)
        print(f"\n✅ Done! Total records saved: {len(combined_df)}")
    else:
        print("⚠️ No data collected.")


if __name__ == "__main__":
    # Example: replace this with the actual pesticide listing URL
    BASE_URL = "https://www.pcpb.go.ke/?s=pesticides+"

    scrape_all_pages(
        base_url=BASE_URL,
        page_param="page",  # or another one like "pg", depending on the site
        max_pages=100,
        delay=2  # seconds between requests to avoid overloading the server
    )
