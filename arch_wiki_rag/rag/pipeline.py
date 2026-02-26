from arch_wiki_rag.rag.chunking import chunk_page
from arch_wiki_rag.rag.embeddings import embed_texts, add_vectors

def process_page(title: str):
    chunks = chunk_page(title)
    if not chunks:
        print(f"No chunks found for {title}")
        return
    vectors = embed_texts(chunks)
    if not vectors:
        print(f"No embeddings generated for {title}")
        return
    add_vectors(vectors, chunks)
