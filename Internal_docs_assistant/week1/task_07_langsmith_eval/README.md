# Task 7 — LangSmith: Tracing & Evaluation

**Course topic:** LangSmith — tracing, datasets, and LLM-as-judge evaluation.
**Scaffolding:** 🟡 Mixed — a dataset and skeleton are provided; you wire up the
evaluators.
**Time budget:** ~one day.

## Why this task
"It looks right" is not engineering. Before you can improve a RAG system you need
to *measure* it: is the answer correct? Is it grounded in the retrieved context
(no hallucination)? LangSmith gives you tracing (see every step of a run) and
evaluation (score runs against a dataset).

## Setup
1. Create a free account at https://smith.langchain.com and get an API key.
2. Put it in `.env` (`LANGCHAIN_API_KEY`, and `LANGCHAIN_TRACING_V2=true`).
3. Run any earlier task — then open LangSmith and confirm you can see the trace.

## Goal
1. **Tracing:** confirm your Task 4 RAG chain shows up as traces in LangSmith.
2. **Dataset:** create a LangSmith dataset from `eval_dataset.jsonl` (provided).
3. **Evaluate:** run your RAG chain over the dataset with at least two evaluators:
   - **Correctness** (compare answer to the reference — LLM-as-judge).
   - **Groundedness / faithfulness** (is the answer supported by retrieved context?).
4. Read the results in the LangSmith UI and write down your scores.

## What's provided
- `eval_dataset.jsonl` — 10 Q&A pairs with reference answers over the corpus.
- `starter.py` — loads the dataset, has a `target` function stub that should call
  your RAG chain, and TODOs for defining evaluators and calling `evaluate(...)`.

## Done when…
- [ ] Traces from a RAG run are visible in your LangSmith project.
- [ ] A dataset exists in LangSmith with the 10 examples.
- [ ] `evaluate(...)` runs and produces correctness + groundedness scores.
- [ ] In `NOTES.md`: your two scores, plus one example the system got wrong and
      what the trace told you about *why* (bad retrieval vs bad generation).

## Stretch
- Make a change (e.g. better retriever from Task 6, or a stricter prompt), re-run
  the eval, and compare experiments side by side in LangSmith. Did it improve?
