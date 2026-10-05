# Week 1 — Suggested Day-by-Day Schedule

The course and the tasks run in parallel: interns watch the relevant course
sections in the morning and apply them in the tasks the same day. Adjust to your
team's pace — the tasks are modular.

| Day | Watch (course) | Build (tasks) | Milestone |
|-----|----------------|---------------|-----------|
| **Mon** | LangChain intro, prompts, LCEL; document loaders & splitters | Task 1 · Task 2 | Comfortable with chains + chunking |
| **Tue** | Embeddings, vector stores; retrievers & RAG chains | Task 3 · Task 4 | ✅ First working, grounded RAG with citations |
| **Wed** | Conversational RAG / memory; advanced retrieval | Task 5 · Task 6 | Multi-turn bot + a retrieval benchmark |
| **Thu** | LangSmith tracing & evaluation; LangGraph | Task 7 · Task 8 | Evaluated + agentic self-correcting RAG |
| **Fri** | (catch-up / advanced sections) | **Capstone** build + **demos** | Shipped internal-docs assistant + demo |

## Daily rhythm
- **09:30** — 15-min standup (yesterday / today / blockers).
- **Morning** — watch the day's course sections, take notes.
- **Afternoon** — build the day's task(s); open a PR when the "Done when…"
  checklist passes.
- **End of day** — mentor PR review + a 2-line reflection in `NOTES.md`.

## If an intern falls behind
Priority order to still reach a demo:
1. **Task 4** (naive RAG) — non-negotiable foundation.
2. **Task 8** (LangGraph graph) — the capstone's brain.
3. **Capstone MVP** — ingest → ask → grounded, cited answer in the UI.
4. Then, time permitting: memory (Task 5), advanced retrieval (Task 6), full eval
   (Task 7).

## Definition of done for the week
An intern has "passed" Week 1 when they can demo an internal-docs assistant that
answers correctly with citations, refuses out-of-scope questions instead of
hallucinating, handles a follow-up question, and has at least a basic LangSmith
evaluation with honest failure analysis.
