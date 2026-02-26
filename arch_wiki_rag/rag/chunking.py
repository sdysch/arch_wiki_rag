import logging
from arch_wiki_rag.rag.fetch import fetch_page, FetchError

logger = logging.getLogger(__name__)


def chunk_page(title: str, max_chunk_size: int = 500) -> list[str]:
    try:
        text = fetch_page(title)
    except FetchError as e:
        logger.error("Failed to fetch page %s: %s", title, e)
        return []

    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
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
