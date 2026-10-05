"""
Task 7 — LangSmith evaluation.

Prereq: LANGCHAIN_API_KEY and LANGCHAIN_TRACING_V2=true set in .env.

Run with:  python task_07_langsmith_eval/starter.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from common.utils import get_llm

# Reuse your Task 4 pipeline as the system-under-test.
sys.path.append(str(Path(__file__).resolve().parents[1] / "task_04_naive_rag"))
# from starter import build_retriever, build_rag_chain   # uncomment once Task 4 is done

DATASET_PATH = Path(__file__).resolve().parent / "eval_dataset.jsonl"
DATASET_NAME = "rag-internship-eval"


def load_examples():
    with open(DATASET_PATH, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def ensure_dataset(client):
    """Create the LangSmith dataset if it doesn't exist, and upload examples."""
    from langsmith import Client  # noqa

    # TODO 1: If the dataset doesn't exist, client.create_dataset(DATASET_NAME),
    #         then client.create_examples(...) with inputs={"question": ...}
    #         and outputs={"answer": ...} from load_examples().
    ...


def target(inputs: dict) -> dict:
    """Adapter: LangSmith passes {'question': ...}; return {'answer': ...}."""
    # TODO 2: Build your RAG chain (from Task 4) once, then:
    #         return {"answer": rag_chain.invoke(inputs["question"])}
    raise NotImplementedError


def make_evaluators():
    """Return a list of evaluators for correctness and groundedness."""
    judge = get_llm()

    # TODO 3: Define two evaluators. Simplest path is the openevals / built-in
    #         LLM-as-judge helpers, or write your own function evaluators that
    #         return {"key": "correctness", "score": 0..1}.
    #         - correctness: compare outputs['answer'] to reference answer
    #         - groundedness: is the answer supported by the source docs?
    return []


if __name__ == "__main__":
    from langsmith import Client
    from langsmith import evaluate

    client = Client()
    ensure_dataset(client)

    # TODO 4: Call evaluate(target, data=DATASET_NAME,
    #                        evaluators=make_evaluators(),
    #                        experiment_prefix="naive-rag")
    #         Then open the printed URL in LangSmith to inspect results.
    print("Wire up evaluate(...) — see TODO 4. Then check smith.langchain.com.")
