# Week 3 — Cost, Latency & Budget

> **Standing rule 3:** every PR states what it cost. **Budget for the week: $25.**

Generator model: `___` · Judge model: `___` · Embedding model: `___`
Pricing assumed: `$___ / 1K input tokens`, `$___ / 1K output tokens`, `$___ / 1K embedding tokens`

---

## Budget tracker

| Date | What ran | Cost | Running total | Remaining of $25 |
|---|---|---:|---:|---:|
| | | | | |

---

## Task 1 — Embedding the real corpus

| | Week 2 corpus (4 docs) | Week 3 corpus (190 docs) |
|---|---:|---:|
| Embedding tokens | | |
| Embedding cost | | |
| Wall clock to build the index | | |
| Index size on disk | | |
| Mean cost per question (`make cost`) | *(from W2 `COST.md`)* | |
| Mean latency per question | *(from W2 `COST.md`)* | |

## Task 2 — What an eval run costs

| Run type | Examples | Wall clock | Cost |
|---|---:|---:|---:|
| Retrieval only (dev) | | | |
| Full pipeline + judges (dev) | | | |
| Full pipeline + judges (test) | | | |

**Runs you can afford with the remaining budget:** ___ retrieval-only, or ___ full.

## Task 3 — Ingestion

| | Wall clock | Embedding calls | Cost |
|---|---:|---:|---:|
| Full re-ingest | | | |
| Incremental (one changed file) | | | |

## Task 4 — Winner vs baseline

| | Baseline | Winner | Delta |
|---|---:|---:|---:|
| Retrieval latency p50 | | | |
| Retrieval latency p95 | | | |
| End-to-end latency p50 | | | |
| Cost per question | | | |
| Projected monthly cost @ 1,000 questions/day | | | |

| Docker image size | *(W2 `RESULTS.md`)* | | |

**Cost by node — Week 2 vs now** (`make cost`, same seed set):

| Node | Week 2 % of spend | Week 3 winner % of spend |
|---|---:|---:|
| `contextualize` (or your history node) | | |
| `route_question` | | |
| `grade_documents` | | |
| `rewrite_query` | | |
| `generate` | | |
| `grade_generation` | | |

**Most expensive node now, and did your Week 2 reduction idea get tested?**

>

**Was the quality gain worth the latency and cost?** One honest paragraph:

>

## Task 5 — Time and truth

| | Before | After |
|---|---:|---:|
| LLM calls per question | | |
| Cost per question | | |

## Task 6 — Access control

| | Before | After |
|---|---:|---:|
| Retrieval latency p50 | | |
| Cache hit rate on the Week 2 workload | | |

*(A drop in hit rate is expected: answers are now cached per access scope.)*

---

## Running log — cost impact per PR

| PR | Change | Latency impact | Cost impact | Notes |
|---|---|---|---|---|
| | Task 1 baseline | n/a | | corpus embed |
| | Task 2 eval | n/a | | eval runs |
| | Task 3 ingestion | | | |
| | Task 4 experiments | | | |
| | Task 5 time and truth | | | |
| | Task 6 access | | | |

---

## The question to be able to answer on Friday

> *"The corpus is 190 documents. The real Northwind has about 40,000. What happens
> to ingestion time, index size, retrieval latency and monthly cost — and which of
> those breaks first?"*

>
