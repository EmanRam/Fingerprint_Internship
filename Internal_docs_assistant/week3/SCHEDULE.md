# Week 3 — Day-by-Day Schedule

Full days on tasks. Wednesday is entirely experiments, because that's where the
real learning of the week happens.

| Day | AM | PM | Milestone |
|-----|----|----|-----------|
| **Mon** | Task 1 · Meet the corpus | Task 2 · Eval at scale | ✅ **The cliff is measured:** Week 2 system vs real corpus, by category |
| **Tue** | Task 2 continued | Task 3 · Ingestion | 100-example eval with dev/test split; retrieval scored separately |
| **Wed** | Task 4 · Experiments | Task 4 continued | ✅ **Halfway:** ≥5 experiments logged hypothesis-first; winner chosen on dev, confirmed on test |
| **Thu** | Task 5 · Time and truth | Task 6 · Who's asking | ✅ **Hard gate:** leak matrix green. **Code freeze 18:00**, tag `v1.1-rc` |
| **Fri** | ★ Holdout run + gap analysis | ★ RFC for Week 4 + demo | Holdout scored, RFC reviewed, 10-minute demo |

## Daily rhythm

- **09:00 — standup, 15 minutes.** Yesterday / today / one blocker, plus **the
  number you moved yesterday**.
- **Mid-afternoon — PR review, same day.**
- **17:00 — the number.** Whatever you measured goes into `RESULTS.md`,
  `COST.md` or `EXPERIMENTS.md` before you stop.

## Checkpoints

| When | Gate | If it slips |
|---|---|---|
| **Mon 17:00** | Seed eval run against the Week 2 system on the new corpus; scores split by category; failing Week 2 tests triaged. | Nothing else starts. Without a baseline, no later number means anything. |
| **Wed 17:00** | ≥5 retrieval experiments logged, hypothesis committed before result, noise floor measured. | Drop Task 5's conflict handling to "documented, not built". Keep the experiments. |
| **Thu 18:00** | Access-control leak matrix passes for all users. `make check` < 5 s. A clean clone of the tag comes up with `docker compose up`. Code frozen and tagged for the holdout. | **The holdout does not run against a system that leaks.** Fix the leak first; the RFC slips instead. |

## If you fall behind

Priority order:

1. **Task 1** — the baseline. Every later number is a delta against it.
2. **Task 2** — the eval. Without per-category retrieval metrics, Task 4 is guesswork.
3. **Task 6** — access control. A leak is a security incident, not a quality issue.
4. **Task 4** — experiments. This is the main skill the week teaches.

Tasks 3 and 5 are where the quality gains come from, but you can run the
experiments in Task 4 on rough ingestion and come back to them.

## Definition of done for the week

See `README.md`. In short: you know where your system is weak, with numbers to
show it. It cites current truth, never leaks, and generalises to questions it
hasn't seen. And you've written next week's spec.
