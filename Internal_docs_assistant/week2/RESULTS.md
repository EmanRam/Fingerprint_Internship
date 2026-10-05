# Week 2 — Results

> **Standing rule 1:** a task is done when its number is in this file (or `COST.md`).
> Fill these in as you go, not on Friday. Every heading below is required by a
> task's "Done when…" checklist.

---

## Task 1 — Week 1 closeout

### Week 1 review findings — closed and verified

| # | Finding | What I changed | How I verified it in the running app |
|---|---|---|---|
| 1 | | | |

### Task 6 retrieval benchmark

| Strategy | Hit rate |
|---|---:|
| baseline (dense similarity) | |
| mmr | |
| multiquery | |
| hybrid (BM25 + dense) | |

**Winner and why** — two sentences, tied to how the questions are phrased:

>

### Capstone eval, re-run over 20 examples

| Metric | Score | Date | LangSmith experiment |
|---|---:|---|---|
| Correctness | | | |
| Groundedness | | | |

### Multi-turn memory working

- [ ] Screenshot committed at: `___`
- [ ] Cold start vs warm start log lines:

```
(paste the two startup lines here — one building the index, one loading it)
```

---

## Task 2 — Test harness

| Tier | Tests | Wall clock | API cost |
|---|---:|---:|---:|
| Fast (`make check`) | | | $0.00 |
| Live (`make check-live`) | | | |

**The regression test:** which test fails if the app is wired to the wrong graph?

> `tests/___::___`

---

## Task 3 — Service API

| Endpoint | p50 latency | p95 latency | n |
|---|---:|---:|---:|
| `POST /chat` | | | 20 |
| `POST /chat/stream` (time to first token) | | | 20 |
| `POST /chat/stream` (time to last token) | | | 20 |

**Session isolation** — the test that proves it:

> `tests/___::___`

**Concurrency (stretch):** 5 simultaneous requests — did latency degrade, and where?

>

---

## Task 4 — Containerize

| | Value |
|---|---|
| Image size | |
| Biggest contributor to size | |
| Runs as non-root | ☐ |
| Cold-checkout `docker compose up` works | ☐ |
| Provider switchable by `.env` alone | ☐ |

---

## Task 5 — Observability

*(Latency and cost figures live in `COST.md`. This section is for behaviour.)*

**Node-path distribution over the eval set** — how often does each path actually fire?

| Path | Count | % |
|---|---:|---:|
| route→retrieve→grade→generate→check→END | | |
| …with 1 rewrite loop | | |
| …with 2 rewrite loops | | |
| route→direct→END | | |

**Does the rewrite→retry loop fire in practice?**

>

---

## Task 6 — Caching

*(Before/after cost table lives in `COST.md`.)*

| | Value |
|---|---|
| Cache hit rate on defined workload | |
| Workload used (describe it) | |
| Invalidation test | `tests/___::___` |

**Semantic cache — implemented, or argued against?** Two paragraphs either way:

>

---

## Task 7 — Eval gate

**Baseline committed in** `eval_baseline.json` — scores and date:

| Metric | Baseline | Date |
|---|---:|---|
| Correctness | | |
| Groundedness | | |

**Category-split scores** (this is the point — a blended average hides the roadmap):

| Category | n | Correctness | Groundedness |
|---|---:|---:|---:|
| Factual (single doc) | | | |
| Multi-hop (two docs) | | | |
| Multi-part answers | | | |
| Refusal / out-of-scope | | | |
| Follow-up (needs history) | | | |
| Keyword-precise | | | |

**The 10 new adversarial examples** — what each is designed to break:

| # | Question | Designed to break |
|---|---|---|
| 21 | | |
| 22 | | |
| … | | |

**The red build:** link to the CI run that blocked the deliberately-weakened prompt.

>

**Real weakness found by the adversarial set:**

>

---

## Task 8 — Resilience

**Degradation table** — what degrades to what:

| Failure | Behaviour | Tested by |
|---|---|---|
| LLM provider timeout | | |
| `grade_documents` fails mid-loop | | |
| Embedding call fails at startup | | |
| Rate limit exceeded | | |

**Prompt-injection attempts:**

| # | Attempt | Outcome |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

---

## Friday — Release v1.0

- [ ] Tagged `v1.0`
- [ ] `CHANGELOG.md`
- [ ] `RUNBOOK.md`
- [ ] `ARCHITECTURE.md` with current Mermaid diagram
- [ ] `RESULTS.md` and `COST.md` complete

**The weakest part of this system, in my own words:**

>
