import faiss
import numpy as np

dimension = 1536
index = faiss.IndexFlatL2(dimension)

def add_vectors(vectors):
    arr = np.array(vectors).astype('float32')
    index.add(arr)

def search(query_vector, k=5):
    D, I = index.search(np.array([query_vector], dtype='float32'), k)
    return I

import numpy as np
import faiss

# === FAISS Index Setup ===
DIMENSION = 1536  # Match your embedding model
index = faiss.IndexFlatL2(DIMENSION)
vector_store = []  # Optional: store text chunks corresponding to embeddings

# === Embedding Function ===
def embed_texts(texts: list[str]) -> list[np.ndarray]:
    """
    Convert a list of texts into embeddings.
    Replace this with your actual embedding model (OpenAI, bge-small, etc.)
    """
    embeddings = []
    for text in texts:
        # Placeholder: random embeddings for testing
        emb = np.random.rand(DIMENSION).astype('float32')
        embeddings.append(emb)
    return embeddings

def add_vectors(vectors: list[np.ndarray], texts: list[str] | None = None) -> None:
    """
    Add embeddings to FAISS index.
    Optionally store corresponding text chunks.
    """
    # Stack into 2D array
    arr = np.stack(vectors).astype('float32')
    index.add(arr)
    if texts:
        vector_store.extend(texts)
