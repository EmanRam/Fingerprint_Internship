"""
Task 5 — cost report skeleton.

Runs the eval questions through the graph with instrumentation on, then prints
what it cost. Copy to `scripts/cost_report.py`.

    make cost
    # or: python scripts/cost_report.py

The output of this script fills in week2/COST.md. That file is the deliverable;
this script is how you get the numbers into it.
"""

from __future__ import annotations

import json
import os
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# Pricing comes from .env so it tracks whatever model you're actually on.
COST_PER_1K_IN = float(os.getenv("COST_PER_1K_INPUT_TOKENS", "0.00015"))
COST_PER_1K_OUT = float(os.getenv("COST_PER_1K_OUTPUT_TOKENS", "0.0006"))

# The eval set lives with your capstone, not next to this script. Set
# EVAL_DATASET_PATH in .env if yours is somewhere else (relative to the repo root).
REPO_ROOT = Path(__file__).resolve().parents[1]
DATASET_PATH = REPO_ROOT / os.getenv(
    "EVAL_DATASET_PATH", "week1/capstone_internal_docs_assistant/eval_dataset.jsonl")


def load_questions() -> list[dict]:
    with open(DATASET_PATH, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


# ---------------------------------------------------------------------------
# Token accounting
# ---------------------------------------------------------------------------

def get_token_usage(response) -> tuple[int, int]:
    """Pull (input_tokens, output_tokens) out of a model response.

    TODO 1: LangChain surfaces this on `response.usage_metadata` for most
            providers, and on `response.response_metadata["token_usage"]` for
            others. Handle both, and return (0, 0) rather than raising if
            neither is present — a missing count should degrade the report,
            not kill it.
    """
    raise NotImplementedError("TODO 1")


def cost_usd(tokens_in: int, tokens_out: int) -> float:
    return (tokens_in / 1000) * COST_PER_1K_IN + (tokens_out / 1000) * COST_PER_1K_OUT


# ---------------------------------------------------------------------------
# Instrumented run
# ---------------------------------------------------------------------------

def run_one(graph, question: str) -> dict:
    """Run one question and return everything worth knowing about it.

    TODO 2: stream the graph (stream_mode="updates") so you capture the node
            path, and time each node as it fires.

    Return:
        {
          "question": str,
          "answer": str,
          "node_path": [str],
          "retries": int,
          "refused": bool,
          "latency_ms": float,
          "per_node": {node: {"calls": n, "ms": f, "tokens_in": n, "tokens_out": n}},
          "tokens_in": int, "tokens_out": int, "cost_usd": float,
        }

    The per-node breakdown is the point. `grade_documents` calls the model once
    per retrieved document, so with k=4 it's four calls to everyone else's one —
    expect it to dominate, and confirm rather than assume.
    """
    raise NotImplementedError("TODO 2")


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def percentile(values: list[float], p: float) -> float:
    """TODO 3: p50 and p95 over a small list. Sort and index — no numpy needed."""
    raise NotImplementedError("TODO 3")


def print_report(runs: list[dict]) -> None:
    """TODO 4: print three tables.

    1. Per question:  question | latency | calls | tokens | cost | path length
    2. Aggregate:     mean/p95 latency, mean calls, mean tokens, mean cost,
                      and PROJECTED MONTHLY COST at 1,000 questions/day.
    3. Per node:      calls/question | tokens | cost | % of total spend
                      ...sorted by cost descending, so the answer to
                      "what's expensive?" is the first row.

    Then print the node-path distribution:

        route→retrieve→grade→generate→check→END          14  (70%)
        ...with 1 rewrite loop                            4  (20%)
        route→direct→END                                  2  (10%)

    If the rewrite loop shows 0%, say so loudly. It means the doc grader never
    rejects anything and your self-correction machinery is decorative. That's a
    finding worth writing up in RESULTS.md, not a bug to hide.
    """
    raise NotImplementedError("TODO 4")


def main() -> None:
    # TODO 5: build the graph once, run every question, print the report.
    #
    # Print the totals for the whole run at the end — you are about to spend
    # real money every time you run this, and knowing how much is the lesson.
    raise NotImplementedError("TODO 5")


if __name__ == "__main__":
    main()
