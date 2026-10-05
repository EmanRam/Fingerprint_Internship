"""
Task 2 — Document Loading & Chunking

Fill in each TODO. Run with:  python task_02_document_loading_chunking/starter.py
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from common.utils import DATA_DIR


def load_documents():
    """Load every .md file in data/ into LangChain Document objects."""
    from langchain_community.document_loaders import TextLoader

    docs = []
    for md_file in sorted(DATA_DIR.glob("*.md")):
        # TODO 1: Use TextLoader(md_file, encoding="utf-8").load() and extend `docs`.
        #         Each loader returns a list of Document objects.
        ...
    return docs


def split_documents(docs, chunk_size=800, chunk_overlap=100):
    """Split Documents into overlapping chunks."""
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    # TODO 2: Create a RecursiveCharacterTextSplitter with the given chunk_size
    #         and chunk_overlap, then call .split_documents(docs).
    splitter = ...
    chunks = ...
    return chunks


if __name__ == "__main__":
    docs = load_documents()
    print(f"Loaded {len(docs)} documents.")
    for d in docs:
        print("  -", d.metadata.get("source"), f"({len(d.page_content)} chars)")

    print("\nChunk-size experiment:")
    for size in (400, 800, 1500):
        chunks = split_documents(docs, chunk_size=size, chunk_overlap=size // 8)
        print(f"  chunk_size={size:>4} -> {len(chunks)} chunks")

    # Inspect one chunk so you can see what the retriever will actually see.
    sample = split_documents(docs, 800, 100)[0]
    print("\nExample chunk metadata:", sample.metadata)
    print("Example chunk text:\n", sample.page_content[:300], "...")

    # ---- Reflection (answer in NOTES.md) -----------------------------------
    # 1. What happened to the chunk count as chunk_size grew? Why?
    # 2. If a policy answer spans two paragraphs, how does overlap help?
    # 3. Which chunk size do you think will retrieve best for these docs, and why?
