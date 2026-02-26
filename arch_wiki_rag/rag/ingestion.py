import os
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://wiki.archlinux.org'
OUTPUT_DIR = 'data/raw'

def download_page(title: str):
    url = f'{BASE_URL}/index.php/{title.replace(" ", "_")}'
    resp = requests.get(url)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, 'html.parser')
    content = soup.find('div', {'id': 'bodyContent'})
    text = content.get_text(separator='\n', strip=True) if content else ''

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, f'{title}.txt')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
