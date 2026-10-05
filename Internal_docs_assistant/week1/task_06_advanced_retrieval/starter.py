"""
Task 6 — Advanced retrieval benchmark.

The harness (loader, baseline, question set, scorer) is provided.
Implement the build_*_retriever functions, then run:

    python task_06_advanced_retrieval/starter.py
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from common.utils import get_llm, get_embeddings, DATA_DIR


# --- provided: corpus + chunks ------------------------------------------------
def load_chunks():
    from langchain_community.document_loaders import TextLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    docs = []
    for md in sorted(DATA_DIR.glob("*.md")):
        docs.extend(TextLoader(md, encoding="utf-8").load())
    return RecursiveCharacterTextSplitter(
        chunk_size=600, chunk_overlap=80).split_documents(docs)


CHUNKS = load_chunks()


def build_baseline_retriever(k=4):
    from langchain_community.vectorstores import FAISS
    store = FAISS.from_documents(CHUNKS, get_embeddings())
    return store.as_retriever(search_kwargs={"k": k})


# --- YOUR WORK: implement these ----------------------------------------------
def build_mmr_retriever(k=4):
    # TODO: same FAISS store but search_type="mmr".
    raise NotImplementedError


def build_multiquery_retriever(k=4):
    # TODO: wrap the baseline in MultiQueryRetriever.from_llm(retriever, llm=get_llm()).
    raise NotImplementedError


def build_hybrid_retriever(k=4):
    # TODO: EnsembleRetriever([bm25, dense], weights=[0.5, 0.5]).
    #       BM25Retriever.from_documents(CHUNKS) + the baseline dense retriever.
    raise NotImplementedError


# --- provided: evaluation ----------------------------------------------------
# Each question is labeled with the file that SHOULD be retrieved.
QUESTIONS = [
    ("How many vacation days do full-time staff accrue?", "hr_policies.md,employee_handbook.md"),
    ("What do I do if my company laptop gets stolen?", "it_faq.md"),
    ("How fast can the rover go when carrying a load?", "product_specs.md"),
    ("What's the daily meal budget when traveling abroad?", "hr_policies.md"),
    ("How long is parental leave for an adoptive parent?", "employee_handbook.md"),
    ("How do I connect to the VPN from home?", "it_faq.md"),
]


def hit_rate(retriever):
    """Fraction of questions where a retrieved chunk came from a gold source file."""
    hits = 0
    for question, gold in QUESTIONS:
        gold_files = set(gold.split(","))
        docs = retriever.invoke(question)
        sources = {Path(d.metadata.get("source", "")).name for d in docs}
        if sources & gold_files:
            hits += 1
    return hits / len(QUESTIONS)


if __name__ == "__main__":
    strategies = {
        "baseline": build_baseline_retriever,
        "mmr": build_mmr_retriever,
        "multiquery": build_multiquery_retriever,
        "hybrid": build_hybrid_retriever,
    }
    print(f"{'strategy':<14} hit_rate")
    print("-" * 26)
    for name, builder in strategies.items():
        try:
            score = hit_rate(builder())
            print(f"{name:<14} {score:.2f}")
        except NotImplementedError:
            print(f"{name:<14} (not implemented yet)")
