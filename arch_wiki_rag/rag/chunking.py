from bs4 import BeautifulSoup
import requests

def chunk_page(title: str, max_chunk_size: int = 500) -> list[str]:
    url = f"https://wiki.archlinux.org/title/{title.replace(' ', '_')}"
    resp = requests.get(url)
    if resp.status_code != 200:
        print(f"Failed to download {title}: {resp.status_code}")
        return []

    soup = BeautifulSoup(resp.text, 'html.parser')

    # Corrected main content selector
    content_div = soup.find('div', {'id': 'bodyContent'})
    if not content_div:
        print(f"No content found for {title}")
        return []

    text = content_div.get_text(separator='\n').strip()
    if not text:
        print(f"No text found inside content for {title}")
        return []

    # Split into chunks
    paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
    chunks = []
    current_chunk = ""
    for p in paragraphs:
        if len(current_chunk) + len(p) + 1 > max_chunk_size:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = p
        else:
            current_chunk += "\n" + p if current_chunk else p
    if current_chunk:
        chunks.append(current_chunk)

    return chunks
