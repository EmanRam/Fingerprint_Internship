# Week 3 — Results

> **Standing rule 1:** a task is done when its number is in this file, `COST.md`
> or `EXPERIMENTS.md`. Fill these in as you go, not on Friday.
>
> **Standing rule 5:** unless a heading says otherwise, numbers are on **dev**.
> Test numbers appear only where a task asks you to confirm a decision.

Category order used in every table below (15 categories):
`factual · table · keyword · version · conflict · draft · multi_hop · multi_part ·
ambiguous · long_doc · cross_lingual · follow_up · personalized · access · out_of_scope`

---

## Task 1 — Meet the corpus

### The cliff — Week 2 system, new corpus, seed set (40)

| Category | n | Deterministic pass | Correctness | Groundedness |
|---|---:|---:|---:|---:|
| factual | | | | |
| table | | | | |
| keyword | | | | |
| version | | | | |
| conflict | | | | |
| draft | | | | |
| multi_hop | | | | |
| multi_part | | | | |
| ambiguous | | | | |
| long_doc | | | | |
| cross_lingual | | | | |
| follow_up | | | | |
| personalized | | | | |
| access | | | | |
| out_of_scope | | | | |
| **All** | 40 | | | |

**Formats the Week 2 loader couldn't read, and what it did with them** (crashed /
skipped silently / loaded garbage):

>

### The Week 2 toolchain against the new corpus

| Week 2 tool | Outcome on the new corpus |
|---|---|
| `make check` (green? wall clock?) | |
| `make check-live` (which tests failed?) | |
| Eval gate: your 30 examples vs `eval_baseline.json` | |
| `make cost`: cost per question | |
| `docker compose up` (starts? loads or rebuilds index?) | |

### Does the rewrite → retry loop fire now? (Week 2 Task 5's question, re-asked)

| Path | Week 2 corpus (from W2 `RESULTS.md`) | Week 3 corpus (seed set) |
|---|---:|---:|
| No rewrite | | |
| 1 rewrite loop | | |
| 2 rewrite loops | | |
| Direct (no retrieval) | | |

>

### Week 2 tests and eval examples that failed — triage

| Test or example | Verdict (regression / world changed / bad test) | Reason, and the document that proves it |
|---|---|---|
| | | |

### Corpus profile

| | Value |
|---|---|
| Documents loaded / total | / 190 |
| By source system | |
| By format | |
| Languages | |
| Total characters | |
| Total chunks (current settings) | |

### Data-quality issues found (beyond the two in `corpus/README.md`)

| # | Issue | Where | Effect if left alone |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

**My guess at the biggest drop — retrieval or generation?** (Task 2 checks this.)

>

---

## Task 2 — Eval at scale

| | Value |
|---|---|
| Total examples | 100 |
| From Week 2 (migrated / updated / dropped) | / / |
| From the seed set (merged / duplicate of a Week 2 example) | / |
| New | |
| Dev / test split | / |
| New `eval_baseline.json`: dataset version, date, correctness, groundedness | |
| Synthetic candidates generated / accepted / rejected | / / |
| Top 3 rejection reasons | |
| Judge model / generator model | / |
| Judge–human agreement (20 examples) | |
| Retrieval-only eval: wall clock / cost | / |

### Retrieval by category (dev)

| Category | n | R@1 | R@3 | R@5 | R@10 | MRR |
|---|---:|---:|---:|---:|---:|---:|
| factual | | | | | | |
| table | | | | | | |
| keyword | | | | | | |
| version | | | | | | |
| conflict | | | | | | |
| draft | | | | | | |
| multi_hop | | | | | | |
| multi_part | | | | | | |
| ambiguous | | | | | | |
| long_doc | | | | | | |
| cross_lingual | | | | | | |
| follow_up | | | | | | |
| personalized | | | | | | |
| access *(authorised users only)* | | | | | | |
| **All** | | | | | | |

### Generation by category (dev)

| Category | n | Deterministic | Correctness | Groundedness |
|---|---:|---:|---:|---:|
| factual | | | | |
| table | | | | |
| keyword | | | | |
| version | | | | |
| conflict | | | | |
| draft | | | | |
| multi_hop | | | | |
| multi_part | | | | |
| ambiguous | | | | |
| long_doc | | | | |
| cross_lingual | | | | |
| follow_up | | | | |
| personalized | | | | |
| access | | | | |
| out_of_scope | | | | |
| **All** | | | | |

**Judge–human disagreements:**

| Example | Judge said | I said | Who was right, and why |
|---|---|---|---|
| | | | |

**Was the Task 1 guess right?**

>

---

## Task 3 — Ingestion

| | Before | After |
|---|---:|---:|
| Documents loaded | | |
| Documents skipped (with reasons listed below) | | |
| Chunks | | |
| Duplicates detected | — | |
| recall@5, all (dev) | | |

recall@5 by category, before → after: *(only categories that moved by more than the
noise floor)*

| Category | Before | After |
|---|---:|---:|
| | | |

**Dedup policy, and why:**

>

**Incremental-index + cache-invalidation test:** `tests/___::___`

**Warm `docker compose up` startup log line** (must say "loaded"):

```
```

**`make check` wall clock after Task 3's tests:** ___ s (budget 5 s)

**Skipped documents and reasons:**

>

---

## Task 4 — Retrieval experiments

*(Every experiment is in `EXPERIMENTS.md`. This section is the outcome.)*

| | Baseline | Winner |
|---|---:|---:|
| Config summary | | |
| recall@5 dev | | |
| recall@5 **test** (run once) | | |
| MRR dev | | |
| MRR **test** | | |
| Latency per query | | |

**Why this winner, citing per-category numbers:**

>

**Did test agree with dev?**

>

**CI retrieval gate tolerance, and how it was derived from the noise floor:**

>

---

## Task 5 — Time and truth

| Category | Before (dev) | After (dev) |
|---|---:|---:|
| version | | |
| conflict | | |
| draft | | |
| ambiguous | | |

**Time-travel test:** `tests/___::___` — with `AS_OF_DATE=2026-02-15`: ___ days.
With the default date: ___ days.

**Source authority order** (highest first, with one sentence of justification each):

1.
2.
3.
4.
5.
6.

**Ambiguity policy** (clarify, or answer every reading?), and the test that pins it:

>

---

## Task 6 — Who's asking

| Test | Name | Passes |
|---|---|---|
| Leak matrix (6 users × restricted docs) | `tests/___::___` | ☐ |
| Cache scope | `tests/___::___` | ☐ |
| Session binding (403) | `tests/___::___` | ☐ |
| Unknown user (401) | `tests/___::___` | ☐ |

**`access` category on dev:** leaks: ___ · authorised users answered: ___ / ___

**New rows for the Week 2 degradation table:**

| Failure | Behaviour | Tested by |
|---|---|---|
| Directory file missing or unreadable | | |
| Unknown `user_id` | | |
| Chunk with no ACL metadata | | |

**Rate limit keyed by `user_id`:** `tests/___::___`

**`make check` wall clock with the leak matrix:** ___ s (budget 5 s) · CI: ___ s (budget 60 s)

**Injection attempts** (outcome with the Week 2 injection check on / off):

| # | User | Attempt | Outcome (check on) | Outcome (check off) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

**Why filtering after retrieval isn't good enough:**

>

---

## Friday — Holdout

| | Deterministic pass rate | Leaks |
|---|---:|---:|
| Dev | | |
| Test | | |
| Holdout | | |

**Gap by category (test → holdout), largest first:**

| Category | Test | Holdout | Gap |
|---|---:|---:|---:|
| | | | |

**Three holdout failures, diagnosed:**

| Holdout ID | Category | Retrieval or generation? | Evidence |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

### Release v1.1

- [ ] Holdout ran against a clean-clone `docker compose up` of `v1.1-rc`
- [ ] Tagged `v1.1`
- [ ] `CHANGELOG.md` v1.1 entry
- [ ] `ARCHITECTURE.md` updated (diagram included)
- [ ] `RUNBOOK.md`: re-ingest, suspected-leak response, gate red on new baseline
- [ ] `docs/RFC-001-actions.md` reviewed

**The weakest category now, its number, and whether it's retrieval or generation:**

>
