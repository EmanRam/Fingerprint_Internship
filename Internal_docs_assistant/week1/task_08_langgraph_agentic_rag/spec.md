# Task 8 Spec — Corrective / Self-Correcting RAG in LangGraph

You are building an **agentic RAG graph**. No starter code is provided — this
spec is your contract. Build it however you like as long as it meets the
acceptance criteria.

## 1. State schema
Define a `TypedDict` (or Pydantic) graph state with at least:

| Field | Type | Purpose |
|-------|------|---------|
| `question` | `str` | The original user question |
| `rewritten_question` | `str` | Query after rewriting (starts = question) |
| `documents` | `list[Document]` | Currently retrieved chunks |
| `generation` | `str` | The model's answer |
| `route` | `str` | `"retrieve"` or `"direct"` |
| `retries` | `int` | Retrieval-rewrite attempts so far |

## 2. Nodes (each is a function `state -> partial state`)
1. **`route_question`** — LLM (or rules) decides `retrieve` vs `direct`. Route
   HR/IT/Product/policy questions to `retrieve`; greetings and clearly
   out-of-domain questions to `direct`.
2. **`retrieve`** — fetch top-k chunks for `rewritten_question` (reuse your
   Task 6 retriever — hybrid is a good choice).
3. **`grade_documents`** — for each doc, an LLM grader returns yes/no "is this
   relevant to the question?" Keep only relevant docs. Record whether *any*
   relevant docs survived.
4. **`rewrite_query`** — if retrieval was weak, rewrite the question to be more
   retrievable, increment `retries`.
5. **`generate`** — produce a grounded, cited answer from surviving docs.
6. **`grade_generation`** — LLM checks (a) is the answer grounded in the docs
   (no hallucination) and (b) does it actually address the question.
7. **`direct_answer`** — handle smalltalk, or refuse out-of-scope questions with
   the standard "I don't know based on the provided documents" line.

## 3. Edges (control flow)
- `START → route_question`
- `route_question` --conditional--> `retrieve` **or** `direct_answer`
- `retrieve → grade_documents`
- `grade_documents` --conditional-->
  - relevant docs found → `generate`
  - no relevant docs **and** `retries < MAX_RETRIES` → `rewrite_query`
  - no relevant docs **and** `retries >= MAX_RETRIES` → `generate` (which will
    then produce the "I don't know" answer) or straight to END with a refusal
- `rewrite_query → retrieve`
- `generate → grade_generation`
- `grade_generation` --conditional-->
  - grounded & answers question → `END`
  - not grounded & `retries < MAX_RETRIES` → `generate` again (or `rewrite_query`)
  - give up → `END` with the refusal answer
- `direct_answer → END`

Set `MAX_RETRIES = 2`. **Every path must terminate.**

## 4. Acceptance criteria
- [ ] `"How much PTO do I get?"` routes to `retrieve`, retrieves, grades, and
      answers correctly with a citation.
- [ ] `"hello, who are you?"` routes to `direct` and does **not** retrieve.
- [ ] A deliberately awkward query (e.g. *"time off carry rules?"*) triggers at
      least one `rewrite_query → retrieve` loop before answering. Show this in the
      printed node path.
- [ ] An out-of-scope factual question (e.g. *"what's the capital of France?"*)
      ends in a refusal, not a hallucinated answer.
- [ ] No run exceeds `MAX_RETRIES`; there are no infinite loops.
- [ ] You can print/return the ordered list of nodes each question visited.
- [ ] A Mermaid diagram of the compiled graph is included.

## 5. Hints
- `from langgraph.graph import StateGraph, START, END`.
- Conditional edges use `graph.add_conditional_edges(node, router_fn, {...})`.
- Use structured output (`with_structured_output`) for the graders so you get a
  clean boolean back instead of parsing text.
- Stream with `graph.stream(inputs)` and collect the keys to see the node path.
- Keep each node small and single-purpose — it makes debugging in LangSmith easy.

## 6. What "great" looks like
A mentor can hand your graph a question, watch the trace in LangSmith, and see the
system *reason about its own retrieval* — grading docs, rewriting when they're
weak, and refusing to make things up. That is the exact capability your capstone
builds a product around.
