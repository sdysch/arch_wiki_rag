import logging
import os

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

logger = logging.getLogger(__name__)

DIMENSION = 384
INDEX_PATH = "data/faiss/index.bin"

model = SentenceTransformer("all-MiniLM-L6-v2")

index: faiss.IndexFlatIP
vector_store: list[str] = []


def load_index() -> None:
    global index, vector_store
    if os.path.exists(INDEX_PATH):
        index = faiss.read_index(INDEX_PATH)
        texts_path = INDEX_PATH.replace(".bin", "_texts.txt")
        if os.path.exists(texts_path):
            with open(texts_path, "r", encoding="utf-8") as f:
                vector_store = f.read().split("\n|||split|||\n")
        logger.info("Loaded index with %d vectors", index.ntotal)
    else:
        index = faiss.IndexFlatIP(DIMENSION)


def save_index() -> None:
    os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)
    faiss.write_index(index, INDEX_PATH)
    texts_path = INDEX_PATH.replace(".bin", "_texts.txt")
    with open(texts_path, "w", encoding="utf-8") as f:
        f.write("\n|||split|||\n".join(vector_store))
    logger.info("Saved index with %d vectors", index.ntotal)


def embed_texts(texts: list[str]) -> list[np.ndarray]:
    logger.debug("Embedding %d texts", len(texts))
    embeddings = model.encode(texts, convert_to_numpy=True)
    return [np.array(e, dtype=np.float32) for e in embeddings]


def add_vectors(vectors: list[np.ndarray], texts: list[str] | None = None) -> None:
    arr = np.stack(vectors).astype("float32")
    index.add(arr)
    if texts:
        vector_store.extend(texts)
    logger.debug("Added %d vectors to index", len(vectors))


def search(query_vector: np.ndarray, k: int = 5) -> tuple[np.ndarray, np.ndarray]:
    query = np.array([query_vector]).astype("float32")
    distances, indices = index.search(query, k)
    return distances, indices


def get_texts(indices: np.ndarray) -> list[str]:
    return [vector_store[i] for i in indices[0] if i < len(vector_store)]


def query_index(query: str, k: int = 5) -> list[tuple[str, float]]:
    load_index()
    query_vector = embed_texts([query])[0]
    distances, indices = search(query_vector, k=k)
    results = get_texts(indices)
    return [(r, distances[0][i]) for i, r in enumerate(results)]
