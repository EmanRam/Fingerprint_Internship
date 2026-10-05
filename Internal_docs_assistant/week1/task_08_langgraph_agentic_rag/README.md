# Task 8 — Agentic RAG with LangGraph (Spec-Only)

**Course topic:** LangGraph — state machines, nodes/edges, conditional routing,
self-correcting RAG.
**Scaffolding:** 🔴 Spec-only — **no starter code.** You design and build it from
`spec.md`. This is your bridge into the capstone.
**Time budget:** ~one to two days.

## Why this task
Linear RAG chains can't *decide*. They always retrieve, always answer, and never
check their own work. LangGraph lets you build a **graph** where the system can
route queries, grade whether retrieved docs are relevant, rewrite bad queries,
and decide whether to answer or retry — the pattern behind Corrective RAG (CRAG),
Self-RAG, and Adaptive RAG.

## What to build
A LangGraph app that implements **Corrective / Self-correcting RAG**. See
[`spec.md`](./spec.md) for the full node/edge specification, the required state
schema, and the acceptance criteria.

At a high level your graph must:
1. **Route** the question (docs-related → retrieve; smalltalk/out-of-scope → answer
   directly or refuse).
2. **Retrieve** relevant chunks.
3. **Grade** each retrieved doc for relevance (LLM grader).
4. If docs are weak, **rewrite the query** and retry retrieval (bounded loop).
5. **Generate** a grounded answer with citations.
6. **Check** the answer for hallucination; if unsupported, regenerate or say "I
   don't know."

## Deliverable
- `graph.py` (or a small package) that compiles a LangGraph `StateGraph`.
- A `main()` that runs 4–5 sample questions and prints the path each one took
  through the graph (which nodes fired).
- A diagram of your graph (export via `graph.get_graph().draw_mermaid_png()` or
  paste the Mermaid into your PR).
- LangSmith tracing enabled so a mentor can inspect a run.

## Done when…
See the acceptance criteria in `spec.md`. In short: routing works, the grade→
rewrite→retry loop demonstrably fires on a hard query, hallucination-checking
catches an unsupported answer, and every path terminates (no infinite loops).
