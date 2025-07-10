import requests
from bs4 import BeautifulSoup
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

with open('urls.json', 'r') as f:
    urls = json.load(f)

def scrape(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        soup_b = BeautifulSoup(response.text, 'html.parser')
        solo_body = soup.body
        body = len(solo_body.text.lower())
        title = soup.find("h1").get_text(strip=True)
        paragraph_count = len(soup.find_all("p"))
        return {
            "url": url,
            "title": title,
            "paragraph_count": paragraph_count,
            "word_count": body,
        }
    except Exception as e:
        return {
            "url": url,
            "error": str(e)
        }

results = []

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(scrape, url) for url in urls]
    for future in as_completed(futures):
        results.append(future.result())

with open("wiki_data.json", "w", encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)


