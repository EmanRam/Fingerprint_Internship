# Task 5 — Observability: Traces, Tokens, Cost, Latency

**Focus:** making the system's behaviour and cost legible.
**Scaffolding:** 🔴 Spec-only — a `cost_report.py` skeleton is provided.
**Time budget:** half a day (Wednesday PM).
**Branch:** `week2/task-05-observability`

---

## Why this task

Your agentic graph makes somewhere between **four and a dozen** LLM calls per
question, depending on which path it takes — and right now nobody knows which,
including you. `grade_documents` alone calls the model once *per retrieved
document*.

This task is the antidote to cost blindness. The most common Week 1 example is a
script that re-embeds the whole corpus on every run because nobody measured it.
You can't manage what you never look at.

It also settles something a demo can't. Week 1's Task 8 required showing that
the rewrite→retry loop fires on one awkward query. Here you find out how often it
fires on real traffic, as a **statistic**.

---

## What to build

### 1. Structured logging

One JSON line per request, containing at minimum:

```
request_id · session_id · route · node_path · retries · latency_ms
tokens_in · tokens_out · estimated_cost_usd · refused (bool) · cache_hit (bool)
```

Use `structlog`. `print()` is not logging — you can't filter it, ship it, or query
it. Add `cache_hit` now even though it's always `false` until Task 6; adding a
field later means your history has a hole in it.

### 2. Per-node timing

Wrap each graph node so you know where the time and money actually go. A decorator
is the clean way; a context manager works too. You need enough granularity to fill
in the "cost by node" table in `COST.md`.

### 3. LangSmith correlation

Tag every run with `session_id` and `request_id` as metadata. The test is
operational: **given a log line, can you find its trace in under 10 seconds?**
If you have to search by timestamp, it isn't wired.

### 4. The cost report

`scripts/cost_report.py` — runs the eval set and prints, per question and in
aggregate: LLM calls, tokens, cost, wall-clock, and the distribution of node paths.
Skeleton provided.

### 5. A metrics endpoint

`GET /metrics` (or a `prometheus_client` registry): total requests, refusal rate,
mean retries, cache hit rate, p50/p95 latency. Counters, not stories.

---

## Done when…

- [ ] One request produces **one** structured log line containing every field above.
      Paste an example into your PR.
- [ ] Given a `request_id` from a log line, the matching LangSmith trace is found
      in under 10 seconds. Demonstrate it live in standup.
- [ ] `week2/COST.md` is filled in: mean and p95 latency, mean LLM calls per
      question, mean tokens, mean cost per question, and **projected monthly cost
      at 1,000 questions/day**.
- [ ] `week2/COST.md` names the **most expensive node** and one concrete idea for
      reducing it.
- [ ] `week2/RESULTS.md` has the node-path distribution — how often each path
      actually fires, in real numbers.
- [ ] `/metrics` returns live counters.

---

## The interesting question

Does the rewrite→retry loop ever actually fire?

If the data says it fires on 0 of 20 questions, **that is a finding, not a
failure** — it means your document grader is too permissive to ever reject a
retrieval, and the self-correction machinery you built is decorative. Write that
up honestly in `RESULTS.md`. Reporting it is worth more than a passing checkbox,
and Task 7's adversarial examples are where you'd fix it.

This is the same kind of honest diagnosis Week 1's `EVAL_RESULTS.md` asked for.
Do it again here.

---

## Stretch

- **Argue a cost reduction from your own data.** If `grade_documents` is 60% of
  spend, what would grading 2 documents instead of 4 cost you in correctness?
  Run it and find out. That's a real experiment with a real trade-off, and it's
  exactly the shape of Task 7's improvement work.
- Log the retrieved chunk IDs so you can tell *retrieval* drift from *generation*
  drift when a score moves.
