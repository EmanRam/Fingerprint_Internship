# Task 3 — Embeddings & Vector Stores

**Course topic:** Embeddings and vector databases (FAISS / Chroma).
**Scaffolding:** 🟢 Guided — fill in the `# TODO`s in `starter.py`.
**Time budget:** ~half a day.

## Why this task
An embedding turns text into a vector so that "similar meaning" becomes "close in
space." A vector store indexes those vectors so you can find the nearest ones
fast. This is the retrieval engine underneath every RAG system.

## Goal
1. Reuse your Task 2 chunking to produce chunks.
2. Embed them and build a **FAISS** index.
3. Run similarity search and inspect the results.
4. **Persist** the index to disk and reload it (so you don't re-embed every run).

## Steps
1. Complete the TODOs in `starter.py`.
2. Try several queries and look at which chunks come back and their scores.
3. Save the index, then reload it in a second run.

## Done when…
- [ ] You build a FAISS index from the chunks.
- [ ] `similarity_search("How much PTO do I get?", k=3)` returns relevant chunks
      from `hr_policies.md` / `employee_handbook.md`.
- [ ] You save the index to `faiss_index/` and reload it without re-embedding.
- [ ] In `NOTES.md`, note one query where retrieval was *wrong* and hypothesize why.

## Stretch
- Swap FAISS for **Chroma** (`langchain_chroma.Chroma`) and compare the API.
- Print similarity scores with `similarity_search_with_score` and reason about the
  numbers (is lower better or worse for your store?).
