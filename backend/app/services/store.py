from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# FAISS index (384 dims for MiniLM)
dimension = 384
index = faiss.IndexFlatL2(dimension)

# Store metadata separately
DOCUMENTS = []


def add_chunks(source, chunks):
    texts = [chunk for chunk in chunks]

    # Batch embeddings (FAST)
    vectors = model.encode(texts, convert_to_numpy=True)

    # Add to FAISS
    index.add(vectors)

    # Store metadata
    for i, chunk in enumerate(chunks):
        DOCUMENTS.append({
            "source": source,
            "page": i + 1,
            "text": chunk
        })


def search_chunks(query, top_k=5):
    if index.ntotal == 0:
        return []

    query_vec = model.encode([query], convert_to_numpy=True)

    distances, indices = index.search(query_vec, top_k)

    results = []
    for idx in indices[0]:
        if idx < len(DOCUMENTS):
            results.append(DOCUMENTS[idx])

    return results