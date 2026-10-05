"""
Task 4 — Naive RAG pipeline

Fill in each TODO. Run with:  python task_04_naive_rag/starter.py
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from common.utils import get_llm, get_embeddings, DATA_DIR


def build_retriever(k=4):
    from langchain_community.document_loaders import TextLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_community.vectorstores import FAISS

    docs = []
    for md in sorted(DATA_DIR.glob("*.md")):
        docs.extend(TextLoader(md, encoding="utf-8").load())
    chunks = RecursiveCharacterTextSplitter(
        chunk_size=800, chunk_overlap=100).split_documents(docs)
    store = FAISS.from_documents(chunks, get_embeddings())

    # TODO 1: Return a retriever from the store: store.as_retriever(search_kwargs={"k": k})
    return ...


def format_docs(docs):
    """Turn retrieved Documents into a single context string with source tags."""
    # TODO 2: Join each doc as "[source] content". Include metadata['source'].
    return ...


def build_rag_chain(retriever):
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.runnables import RunnableParallel, RunnablePassthrough

    llm = get_llm()

    system = (
        "You are Northwind Robotics' internal assistant. Answer ONLY using the "
        "context below. If the answer is not in the context, say: "
        "'I don't know based on the provided documents.' "
        "After your answer, list the source files you used.\n\n"
        "Context:\n{context}"
    )
    prompt = ChatPromptTemplate.from_messages(
        [("system", system), ("human", "{question}")]
    )

    # TODO 3: Build the LCEL chain. A common shape is:
    #   {"context": retriever | format_docs, "question": RunnablePassthrough()}
    #       | prompt | llm | StrOutputParser()
    chain = ...
    return chain


if __name__ == "__main__":
    retriever = build_retriever(k=4)
    rag = build_rag_chain(retriever)

    questions = [
        "How many sick days do I get per year?",
        "What is the max payload of the Warehouse Rover R2?",
        "What is the CEO's home address?",   # not in the docs -> should say I don't know
    ]
    for q in questions:
        print(f"\nQ: {q}\nA: {rag.invoke(q)}")
