# Task 6 — Advanced Retrieval

**Course topic:** Improving retrieval quality — multi-query, MMR, hybrid
(dense + BM25), and re-ranking / contextual compression.
**Scaffolding:** 🟡 Mixed — a benchmark harness is provided; you implement the
retrievers.
**Time budget:** ~one day.

## Why this task
Naive top-k similarity is a floor, not a ceiling. When users phrase things
differently from the docs, or when the answer needs keyword precision (an error
code, a part number), plain dense retrieval misses. This task is about
**measuring** retrieval and then **improving** it deliberately.

## Goal
Implement and compare at least **three** retrieval strategies against the baseline:
1. **Baseline** — plain vector `similarity` search (given).
2. **MMR** — maximal marginal relevance for diversity.
3. **Multi-Query** — `MultiQueryRetriever` (LLM rewrites the query several ways).
4. **Hybrid** — `EnsembleRetriever` combining dense + `BM25Retriever`.
5. *(stretch)* **Compression / re-rank** — `ContextualCompressionRetriever`.

Then evaluate them on the provided mini question set and report hit-rate
(did the retrieved chunks contain the gold source file?).

## What's provided
`starter.py` gives you the corpus loader, the baseline retriever, a small labeled
question set (`QUESTIONS`), and a `hit_rate()` scorer. You implement the
`build_*_retriever` functions and fill the results table.

## Done when…
- [ ] At least 3 strategies are implemented and run through the harness.
- [ ] You print a comparison table of hit-rate per strategy.
- [ ] In `NOTES.md`, you state which strategy won on this corpus and give a
      hypothesis for *why* (tie it to how the questions are phrased).

## Stretch
- Add a cross-encoder re-ranker (e.g. `sentence-transformers` cross-encoder or
  Cohere rerank) via `ContextualCompressionRetriever` and see if precision improves.
