# Task 4 — Your First RAG Pipeline (Naive RAG)

**Course topic:** Retrievers + the RAG chain (retrieve → stuff into prompt → generate).
**Scaffolding:** 🟢 Guided — fill in the `# TODO`s in `starter.py`.
**Time budget:** ~half to one day.

## Why this task
This is the payoff of Tasks 1–3. You now connect a **retriever** to an **LLM** so
the model answers using *your* documents instead of its training data. This is the
canonical RAG loop you'll refine for the rest of the week.

## Goal
Build an end-to-end question-answering chain:
`question → retrieve top-k chunks → format them into a prompt → LLM → answer`,
and make the answer **cite its sources**.

## Steps
1. Reuse Task 3's index (rebuild it here for a self-contained script).
2. Turn the vector store into a retriever with `.as_retriever()`.
3. Build the RAG chain with LCEL (`RunnablePassthrough` + `RunnableParallel`).
4. Add a rule to the prompt: *if the context doesn't contain the answer, say
   "I don't know based on the provided documents."* (This prevents hallucination.)

## Done when…
- [ ] Asking "How many sick days do I get?" returns the correct number (10) grounded
      in the docs.
- [ ] The answer lists which source file(s) it used.
- [ ] Asking something NOT in the docs ("What is the CEO's home address?") returns
      the "I don't know" fallback rather than a made-up answer.
- [ ] In `NOTES.md`, record one question the pipeline answered wrong and your guess
      at the cause (retrieval? chunking? prompt?).

## Stretch
- Make `k` configurable and observe how answers change with k=1 vs k=6.
- Add the retrieved chunk text to the output so you can debug what the model saw.
