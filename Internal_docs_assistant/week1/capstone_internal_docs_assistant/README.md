# ⭐ Capstone — Northwind Internal Docs Assistant

**Scaffolding:** 🔴 Spec-only. You architect and build the whole thing, reusing
everything from Tasks 1–8. A thin app skeleton is provided so you don't burn time
on plumbing; the RAG brain is yours to build.
**Time budget:** ~2 days (the back half of Week 1). Demo on Friday.

---

## The brief
Build an **internal knowledge assistant** for a company (our fictional *Northwind
Robotics*, using the docs in `../data/`). An employee should be able to ask
natural-language questions about HR policies, IT procedures, and product specs and
get a **correct, grounded, cited** answer — through a simple chat UI.

This is the real job of an applied RAG engineer: not a notebook, but a small
*product* that is retrieval-quality-aware, evaluated, traceable, and honest about
what it doesn't know.

## Required capabilities (the "must-haves")
1. **Ingestion pipeline** — load the corpus, chunk it sensibly, embed it, and
   persist a vector index. Re-running the app must not re-embed from scratch.
   Support adding a new document without a full rebuild if feasible.
2. **Agentic retrieval + answering** — reuse your **LangGraph** graph from Task 8
   (routing, doc grading, query rewrite, hallucination check). The assistant must
   refuse (not hallucinate) when the answer isn't in the docs.
3. **Conversational memory** — multi-turn follow-ups work (Task 5), isolated per
   user session.
4. **Citations** — every answer shows which source file(s)/section it used.
5. **Chat UI** — a Streamlit app (`app.py`) with a chat box, streaming answers,
   visible sources, and a session reset button.
6. **Evaluation** — a LangSmith eval suite (extend Task 7's dataset to ≥20
   examples) reporting correctness + groundedness. Commit your latest scores in
   `EVAL_RESULTS.md`.
7. **Tracing** — LangSmith tracing on, so a reviewer can inspect any answer's path.

## Nice-to-haves (pick based on time / ambition)
- **Metadata filtering** (e.g. restrict to `source = it_faq.md` when the user asks
  an IT question) driven by the router.
- **Access control** demo: tag some docs "HR-only" and filter by a fake user role.
- **Streaming tokens** in the UI.
- **Feedback capture**: 👍/👎 buttons that log to LangSmith.
- **Answer caching** for repeated questions.
- **Dockerfile** so the app runs with one command.

## Architecture you should end up with
```
                 ┌─────────────┐
   documents ───▶│  Ingestion  │──▶ vector index (persisted)
                 └─────────────┘            │
                                            ▼
 user ──▶ Streamlit UI ──▶ LangGraph agentic RAG ──▶ grounded, cited answer
              ▲   │              │  (route → retrieve → grade → rewrite?
              │   │              │   → generate → hallucination-check)
              │   └── session memory        │
              └──────────── answer + sources ┘
                                            │
                              LangSmith  ◀──┘  (tracing + evaluation)
```

## Deliverables (what you hand in Friday)
1. Working `app.py` (Streamlit) + supporting modules.
2. `README` in this folder updated with **how to run it** (commands).
3. `EVAL_RESULTS.md` — your correctness/groundedness scores + a short note on the
   biggest failure mode and how you'd fix it next.
4. A **5-minute demo**: show a correct answer with citation, a refused
   out-of-scope question, and a multi-turn follow-up. Walk through one LangSmith
   trace.
5. A short architecture diagram (Mermaid is fine).

## How you'll be graded
Your mentor holds the full rubric. Headline weighting:
correctness & grounding (30%), retrieval quality (20%), agentic design (20%),
evaluation rigor (15%), code quality & UX (15%).

## Getting started
- Read `app_skeleton.py` — it has the Streamlit plumbing wired and clearly marked
  `# TODO` spots where your RAG backend plugs in. Copy it to `app.py` to begin.
- Reuse aggressively: your Task 8 `graph.py`, Task 6 retriever, Task 5 memory,
  Task 7 eval harness. The capstone is *integration*, not reinvention.
- Start with the thinnest end-to-end slice (ingest → ask → answer in the UI), get
  it working, *then* layer in grading, memory, and evaluation.
