"""
Task 5 — Conversational RAG with memory.

This is a LIGHTER skeleton than tasks 1-4. The retriever builder is given to you;
you design the history-aware retrieval + memory yourself. Read the README first.

Run with:  python task_05_conversational_rag/starter.py
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from common.utils import get_llm, get_embeddings, DATA_DIR


def build_base_retriever(k=4):
    """Provided for you — a plain vector retriever over the corpus."""
    from langchain_community.document_loaders import TextLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_community.vectorstores import FAISS

    docs = []
    for md in sorted(DATA_DIR.glob("*.md")):
        docs.extend(TextLoader(md, encoding="utf-8").load())
    chunks = RecursiveCharacterTextSplitter(
        chunk_size=800, chunk_overlap=100).split_documents(docs)
    store = FAISS.from_documents(chunks, get_embeddings())
    return store.as_retriever(search_kwargs={"k": k})


# ---------------------------------------------------------------------------
# YOUR WORK STARTS HERE.
#
# Implement a conversational RAG chain. Suggested API (feel free to change it):
#
#   conversational_rag = build_conversational_rag(retriever, llm)
#   conversational_rag.invoke(
#       {"input": "How much PTO do I get?"},
#       config={"configurable": {"session_id": "user-123"}},
#   )
#
# Requirements:
#   - follow-up questions must be contextualized against per-session history
#   - history must be isolated per session_id
#   - out-of-scope questions must still be refused
# ---------------------------------------------------------------------------

def build_conversational_rag(retriever, llm):
    raise NotImplementedError("Implement me — see the README for building blocks.")


if __name__ == "__main__":
    retriever = build_base_retriever()
    llm = get_llm()
    bot = build_conversational_rag(retriever, llm)

    session = {"configurable": {"session_id": "demo"}}
    turns = [
        "How much PTO do I get?",
        "Can I carry it over to next year?",   # <- must resolve "it" = PTO
    ]
    for t in turns:
        print(f"\nUser: {t}")
        result = bot.invoke({"input": t}, config=session)
        # create_retrieval_chain returns a dict with an "answer" key.
        print("Bot:", result["answer"] if isinstance(result, dict) else result)
