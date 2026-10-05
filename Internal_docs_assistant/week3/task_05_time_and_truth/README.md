# Task 5 — Time and Truth

**Focus:** answering from the *current, approved* source, and saying so.
**Scaffolding:** 🔴 Spec-only.
**Time budget:** half a day (Thursday AM).
**Branch:** `week3/task-05-truth`

---

## Why this task

The corpus contains several documents that state different rules for the same
question:

- the 2024 handbook,
- a 2025 policy,
- a 2026 policy that replaces the 2025 one,
- a draft proposing to replace that,
- a wiki summary written before any of it changed,
- and a meeting note where someone mentions it in passing.

All of them are relevant to the question, and only one is correct. A retriever
can't sort that out: similarity tells it what a document is about, not whether
the document is still in force. Choosing the right source has to happen in your
graph.

This is where a fluent, well-cited answer can still be wrong. Groundedness won't
catch it either, because the answer is faithfully grounded in a superseded
document.

---

## What to build

### 1. Supersession

When the retrieved documents include several versions of the same policy, answer
from the **current approved** one and say which it is, e.g. *"Under HR-POL-004
v3.0, effective 2026-03-01, …"*.

"Current" depends on the date, so add an `AS_OF_DATE` setting (default
`2026-10-01`, the date of the corpus snapshot). A version whose effective date is
in the future isn't current yet.

### 2. Drafts

A draft is never presented as policy. It may be *mentioned* — "there is a draft
proposal to …, not yet approved" — and for some questions that's the most helpful
answer.

### 3. Conflicts with no version information

A wiki page and a policy can disagree without either one saying it replaces the
other. Define a **source authority order** (for example: policy portal > product
documentation > wiki > newsletter > meeting notes > legacy and scans), justify it,
and use it. When a conflict matters to the user, mention it — e.g. *"The VPN Setup
Guide on the wiki still describes GlobalConnect, but IT-STD-007 retired it on June
30, 2026."*

### 4. Ambiguity

Some questions can't be answered as asked: "the rover" could mean the R2 or the
R3, and they differ. Decide whether the system asks a clarifying question or
answers for every reading, and document why. Either is acceptable. Picking one
reading silently is not.

### 5. Better citations

Citations now include the document, its version (where it has one) and its
section, not just a filename.

This changes your Week 2 API contract. `ChatResponse.sources` is currently
`list[str]`. Change it to a list of structured objects
(`{path, title, version, effective_date, section}`), update the `done` event in
`/chat/stream` to match, and update the Streamlit UI to display them. Treat it as a
real API change: say in the PR what breaks for an existing client, and update the
Week 2 tests that assert on `sources`. Add the cited versions to your Week 2 log
line too, so an operator can see which version of a policy an answer relied on.

---

## Done when…

- [ ] `RESULTS.md` has before/after scores on **dev** for the `version`,
      `conflict`, `draft` and `ambiguous` categories (deterministic, correctness,
      groundedness).
- [ ] **The time-travel test passes:** with `AS_OF_DATE=2026-02-15`, the system
      says the PTO carry-over limit is **5 days** (v2.0 was still current then).
      With the default date, it says **3 days**. Both are covered by fast tests
      using fixture documents, and they join the Week 2 fast tier within its 5 s
      budget.
- [ ] `/chat` and `/chat/stream` return structured sources, and the UI shows the
      version and section.
- [ ] Your source authority order is written down, with one sentence of
      justification per level, in `RESULTS.md` (it moves into `ARCHITECTURE.md` on
      Friday).
- [ ] Your ambiguity policy is written down, and at least one test pins it.
- [ ] `COST.md`: what did this add per question? If you added an LLM call, report
      its cost; if you solved it with metadata, report that it added nothing.

---

## A design question to answer in the PR

Where should supersession be decided:

- at **ingestion time** (mark superseded chunks, filter them out),
- at **retrieval time** (down-rank them),
- or at **generation time** (let the model see every version and choose)?

Each option fails differently. Ingestion-time filtering breaks the time-travel
test. Generation-time choice relies on the model reading dates correctly every
time. Pick one, and say what it costs you.
