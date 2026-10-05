# Task 1 — Meet the Corpus

**Focus:** measuring the cliff before you try to climb it.
**Scaffolding:** 🔴 Spec-only.
**Time budget:** half a day (Monday AM).
**Branch:** `week3/task-01-corpus`

---

## Why this task

Before you change anything, you need to know how badly the system you shipped on
Friday does on a real corpus — and *where*. Every improvement you make this week is
a delta against the number this task produces. Without the baseline, "it got
better" can't be checked.

The second purpose is to get to know the data. Engineers who skip this step spend
the week tuning retrievers to fix what are really parsing problems.

---

## What to do

### 1. Point the Week 2 system at the new corpus — unchanged

Change only the corpus path. Don't fix loaders or tune anything yet. Note which
formats your current ingestion can't read at all, and what it does when it hits
one: crash, skip silently, or load garbage. **Silent skipping is the worst of the
three** — write down whether that's what yours does.

### 2. Run the seed eval and record the cliff

Run all 40 examples in `eval/seed_eval.jsonl` through your Week 2 service. Score
each one with both:

- the deterministic scorer in `eval/scoring.py`, and
- your Week 2 correctness and groundedness judges.

Report the results **by category**. A single overall percentage is not an
acceptable result for this task.

Your Week 2 service has no notion of `user_id` yet, so expect the `access`
category to fail: it will show restricted content to everyone. That's the
baseline Task 6 fixes, so record it rather than patching it now. Until then, run
the service only on your own machine.

### 3. Run your whole Week 2 toolchain — and triage what breaks

Run every Week 2 entry point against the new corpus. Record each one's outcome,
even when it passes:

| Week 2 tool | What to record |
|---|---|
| `make check` | Still green? Still under 5 s? |
| `make check-live` | Which golden-path tests fail? |
| The eval gate (`make eval` + `check_baseline.py`) | Your 30-example scores against `eval_baseline.json` |
| `make cost` | Cost per question, and the node-path distribution |
| `docker compose up` | Does it start with the new corpus mounted? Does it rebuild the index? |

Some of your Week 2 tests and eval examples will fail against the new corpus.
**Not every failure is a bug.** The company changed some policies during 2026, and
a test can fail because the system is now *right*.

For every failure, decide which kind it is:

| Verdict | Meaning | What you do |
|---|---|---|
| **Regression** | The system got worse | Keep the test; it's doing its job |
| **The world changed** | The expected answer is out of date | Update the expectation, cite the document that changed it, and note it in the PR |
| **Bad test** | The test was too brittle to begin with | Fix the test and explain why it was brittle |

Deleting a failing test without a verdict is not an option.

**Your Week 2 `eval_baseline.json` no longer describes this system.** Don't edit
it in place. Archive it as `eval_baseline_w2.json`, so the CI gate can't compare
against stale numbers. Task 2 sets the new baseline.

### 3b. Ask Week 2's open question again

In Week 2, Task 5 asked whether the rewrite → retry loop ever fires. On four tidy
documents the answer may well have been "almost never". On this corpus the
document grader finally has something to reject. Re-run `make cost` on the seed
set and compare the node-path distribution with your Week 2 number. If the loop
*still* never fires, that's an important finding: write it down.

### 4. Profile the corpus

Produce a profile of the corpus as your system sees it after loading:

- documents by source system and by format, and how many failed to load
- total characters and total chunks at your current chunk settings
- languages present
- the time and dollar cost to embed the whole corpus once — **measured**, not
  estimated

### 5. Find what the Knowledge Platform team didn't

`corpus/README.md` lists two known data-quality issues. There are more. Find **at
least five others** and, for each, write down what it would do to retrieval or to
answers if left alone.

---

## Done when…

- [ ] `RESULTS.md` has the cliff table: seed-set scores by category for the Week 2
      system on the new corpus (deterministic pass rate, correctness, groundedness).
- [ ] `RESULTS.md` has the Week 2 toolchain table (all five tools) and the triage
      table: every failing Week 2 test or eval example, its verdict, and a
      one-line reason.
- [ ] `eval_baseline_w2.json` archived; the CI gate no longer compares against it.
- [ ] `RESULTS.md` has the node-path distribution on the new corpus next to your
      Week 2 number.
- [ ] `RESULTS.md` has the corpus profile and at least five newly found data issues.
- [ ] `COST.md` has the measured full-corpus embedding cost and time, and cost per
      question on the new corpus next to your Week 2 figure.
- [ ] One PR, reviewed and merged, before Task 2 starts.

---

## A question to answer in the PR

Which category had the biggest drop, and is it a **retrieval** problem or a
**generation** problem? You don't have the tools to prove it yet — Task 2 builds
them. Write down your guess now, so you can check it against the evidence later.
