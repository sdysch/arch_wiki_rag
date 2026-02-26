import logging
from arch_wiki_rag.rag.chunking import chunk_page
from arch_wiki_rag.rag.embeddings import embed_texts, add_vectors, save_index

logger = logging.getLogger(__name__)


def process_page(title: str) -> None:
    chunks = chunk_page(title)
    if not chunks:
        logger.warning("No chunks found for %s", title)
        return
    vectors = embed_texts(chunks)
    if not vectors:
        logger.warning("No embeddings generated for %s", title)
        return
    add_vectors(vectors, chunks)
    save_index()
    logger.info("Added %d chunks for %s", len(chunks), title)
