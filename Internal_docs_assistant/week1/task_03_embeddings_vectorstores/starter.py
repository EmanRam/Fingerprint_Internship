"""
Task 3 — Embeddings & Vector Stores (FAISS)

Fill in each TODO. Run with:  python task_03_embeddings_vectorstores/starter.py
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from common.utils import get_embeddings, DATA_DIR

INDEX_DIR = Path(__file__).resolve().parent / "faiss_index"


def build_chunks():
    """Load + split the corpus (same idea as Task 2)."""
    from langchain_community.document_loaders import TextLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    docs = []
    for md in sorted(DATA_DIR.glob("*.md")):
        docs.extend(TextLoader(md, encoding="utf-8").load())
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    return splitter.split_documents(docs)


def build_index(chunks):
    from langchain_community.vectorstores import FAISS

    embeddings = get_embeddings()
    # TODO 1: Build a FAISS index from the chunks with FAISS.from_documents(...).
    vectorstore = ...
    return vectorstore


def save_index(vectorstore):
    # TODO 2: Persist the store to INDEX_DIR with vectorstore.save_local(...).
    ...


def load_index():
    from langchain_community.vectorstores import FAISS

    embeddings = get_embeddings()
    # TODO 3: Load the store from INDEX_DIR. FAISS.load_local needs
    #         allow_dangerous_deserialization=True because it unpickles.
    return ...


if __name__ == "__main__":
    chunks = build_chunks()
    print(f"{len(chunks)} chunks to embed.")

    store = build_index(chunks)
    save_index(store)
    print(f"Index saved to {INDEX_DIR}")

    store = load_index()  # prove it round-trips from disk

    for query in [
        "How much PTO do I get?",
        "What should I do if my laptop is stolen?",
        "What is the payload capacity of the rover?",
    ]:
        print(f"\nQ: {query}")
        results = store.similarity_search(query, k=2)
        for r in results:
            print(f"   [{r.metadata.get('source')}] {r.page_content[:90].strip()}...")
