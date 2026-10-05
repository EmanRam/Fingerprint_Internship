# Week 2 — Cost & Latency

> **Standing rule 3:** every PR states what it cost. This file is where those
> numbers accumulate. Measure over the same 20-example eval set every time so the
> rows are comparable.

Model / provider used for these figures: `___`
Pricing assumed: `$___ / 1K input tokens`, `$___ / 1K output tokens`

---

## Baseline — the agentic graph as it stands after Task 1

| Metric | Value |
|---|---:|
| Mean latency per question | |
| p95 latency per question | |
| Mean LLM calls per question | |
| Mean tokens per question (in / out) | / |
| Mean cost per question | |
| **Projected monthly cost @ 1,000 questions/day** | |

### Cost by node

Which node is actually spending the money? `grade_documents` calls the LLM once
*per retrieved document*, so start by checking whether it dominates.

| Node | Calls per question | Tokens | Cost | % of total |
|---|---:|---:|---:|---:|
| `contextualize` (or your history node) | | | | |
| `route_question` | | | | |
| `grade_documents` | | | | |
| `rewrite_query` | | | | |
| `generate` | | | | |
| `grade_generation` | | | | |

**Most expensive node:** `___`

**One concrete idea for reducing it:**

>

---

## Task 6 — Caching, before and after

Same 20 examples, cold cache vs warm cache.

| | Mean latency | p95 latency | Mean cost / question | Total run cost |
|---|---:|---:|---:|---:|
| Cold cache (no reuse) | | | | |
| Warm cache (second run) | | | | |
| **Delta** | | | | |

**Cache hit rate:** `___`

**Was it worth it?** One honest paragraph — including the cases where caching is
the wrong answer:

>

---

## Task 3 — Streaming vs non-streaming, as the user experiences it

| | Time to first token | Time to complete | Perceived improvement |
|---|---:|---:|---|
| `POST /chat` | n/a | | |
| `POST /chat/stream` | | | |

---

## Task 2 — Cold vs warm start

| | Wall clock | Embedding calls |
|---|---:|---:|
| Cold start (index built) | | |
| Warm start (index loaded) | | 0 |

---

## Task 8 — Worst case for a single request

Logical retries (`MAX_RETRIES`) × transport retries (`LLM_MAX_RETRIES`) × LLM calls per path.

| | Value |
|---|---:|
| Max LLM calls in one request (show the arithmetic) | |
| Worst-case cost of one request | |
| Worst-case latency (with timeouts) | |

---

## Task 8 stretch — Load test (50 requests over 30 s)

| p50 | p95 | Error rate | Point where it degrades |
|---:|---:|---:|---|
| | | | |

---

## Running log — cost impact per PR

Fill one row per merged PR. "No change" is a valid and useful entry.

| PR | Change | Latency impact | Cost impact | Notes |
|---|---|---|---|---|
| #1 | Task 1 closeout | | | |
| #2 | Task 2 test harness | n/a | n/a | tests only |
| #3 | Task 3 service API | | | |
| #4 | Task 4 containerize | | | |
| #5 | Task 5 observability | | | instrumentation overhead? |
| #6 | Task 6 caching | | | |
| #7 | Task 7 eval gate | n/a | | CI run cost per PR |
| #8 | Task 8 resilience | | | retries add cost on failure paths |

---

## The question to be able to answer on Friday

> *"If Northwind rolls this out to 200 employees asking 5 questions a day, what
> does it cost per month, and what's the first thing you'd optimise?"*

>
