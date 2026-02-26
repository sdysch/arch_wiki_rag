import logging
import os
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

BASE_URL = "https://wiki.archlinux.org"
OUTPUT_DIR = "data/raw"


class FetchError(Exception):
    pass


def fetch_page(title: str) -> str:
    url = f"{BASE_URL}/title/{title.replace(' ', '_')}"
    logger.debug("Fetching URL: %s", url)
    resp = requests.get(url)
    if resp.status_code != 200:
        raise FetchError(f"Failed to fetch {title}: HTTP {resp.status_code}")

    soup = BeautifulSoup(resp.text, "html.parser")
    content = soup.find("div", {"id": "bodyContent"})
    if not content:
        raise FetchError(f"No content found for {title}")

    text = content.get_text(separator="\n", strip=True)
    if not text:
        raise FetchError(f"No text extracted for {title}")

    logger.debug("Fetched %d chars for %s", len(text), title)
    return text


def fetch_and_save(title: str) -> str:
    text = fetch_page(title)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    safe_title = "".join(c if c.isalnum() or c in "-_" else "_" for c in title)
    path = os.path.join(OUTPUT_DIR, f"{safe_title}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    logger.info("Saved page %s to %s", title, path)
    return path
