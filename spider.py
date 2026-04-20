import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited_urls = set()

HEADERS = {
    "User-Agent": "Mozilla/5.0 (SpiderBot)"
}

def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def spider_urls(url, keyword, max_depth=2, depth=0):
    if depth > max_depth:
        return

    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
    except requests.exceptions.RequestException:
        print(f"[ERROR] Failed to fetch: {url}")
        return

    if response.status_code != 200:
        return

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup.find_all("a", href=True):
        href = tag.get("href")
        full_url = urljoin(url, href)

        if not is_valid_url(full_url):
            continue

        if full_url in visited_urls:
            continue

        visited_urls.add(full_url)

        if keyword.lower() in full_url.lower():
            print(f"[FOUND] {full_url}")

        spider_urls(full_url, keyword, max_depth, depth + 1)


if __name__ == "__main__":
    start_url = "https://example.com"
    keyword = "login"

    print(f"Starting crawl on: {start_url}")
    spider_urls(start_url, keyword)
