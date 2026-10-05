# AI Engineering Internship — Week 3: Make It Hard

Week 1 built a RAG system. Week 2 made it a service you can deploy, measure and
defend. Week 3 asks a different question: **is it actually any good?**

Until now the assistant has read four tidy markdown files, about 6 KB in total. At
that size nearly every retriever finds the right chunk, and a high eval score
mostly reflects how easy the questions are. Real internal knowledge doesn't look like that.

This week the assistant gets the real thing: **190 documents** exported from five
source systems. PDFs with tables, wiki pages wrapped in navigation menus, a
23-page manual, a spreadsheet of error codes, policies that changed twice in two
years, a draft nobody approved, meeting notes that mention "PTO" in passing,
scanned pages with OCR errors, pages written in Arabic, and a folder of salary data
that most users must never see.

Same product, same codebase — the Northwind Internal Docs Assistant you shipped
last Friday. A much harder world to run it in.

---

## Extend, don't rebuild

Nothing from Week 2 gets thrown away. Every Week 2 deliverable is still in use
this week, and each task below says which one it extends. If you find yourself
writing something Week 2 already gave you — a second eval script, a second log
format, a second cache — stop and extend the original.

| Week 2 deliverable | What happens to it in Week 3 |
|---|---|
| **T1** Closed Week 1 app | It's the system under test in Task 1 |
| **T2** Test harness, `make check` < 5 s | New fast tests (leak matrix, time travel, incremental ingest) go into the **same** suite, under the **same** time budget |
| **T3** FastAPI service | Still the only place RAG logic lives. `/chat` and `/chat/stream` gain `user_id`; sessions are bound to their user; `/readyz` reports which index and corpus snapshot are loaded |
| **T4** Docker / compose | Still one command. The corpus and the new index are mounted volumes; new dependencies come with a measured image-size delta |
| **T5** Structured logs, cost report | New log fields (`user_id`, access scope, documents and versions cited). The node-path distribution is re-measured on the hard corpus |
| **T6** Answer + embedding cache | The cache key gains access scope; incremental re-ingest invalidates affected entries |
| **T7** CI eval gate, 30 examples, `eval_baseline.json` | Your 30 examples are **migrated** into the Week 3 eval; the baseline is re-set on the new corpus; the gate gains a retrieval threshold |
| **T8** Guardrails, rate limiting, degradation table | Injection checks extended to access-control attacks; rate limiting moves from per-session to per-user; the degradation table gains new rows |
| **Release** v1.0, `RUNBOOK`, `ARCHITECTURE`, `CHANGELOG` | Friday ships **v1.1**: all three documents updated, not rewritten |

---

## How this week works

| # | Task | Focus | Scaffolding |
|---|------|-------|-------------|
| 1 | Meet the corpus | Baseline, triage, profiling | 🔴 Spec-only |
| 2 | An eval that tells you *where* it broke | Retrieval vs generation metrics, 100 examples | 🟡 Mixed |
| 3 | Ingestion that tells the truth | Parsing, metadata, dedup, incremental indexing | 🔴 Spec-only |
| 4 | Retrieval experiments | Controlled experiments, noise floor | 🔴 Spec-only |
| 5 | Time and truth | Versions, drafts, conflicts, ambiguity | 🔴 Spec-only |
| 6 | Who's asking? | Access control at every layer | 🔴 Spec-only |
| ★ | Holdout + RFC | Generalisation, and you write Week 4's spec | 🔴 Spec-only |

There's less scaffolding than in Week 2. Task 2 includes a metrics skeleton because
the metric definitions are conventions, not design decisions. Everything else is a
brief and acceptance criteria.

---

## The standing rules

Week 2's three rules still apply:

1. **A task is done when the number is in the repo** (`RESULTS.md`, `COST.md`,
   `EXPERIMENTS.md`).
2. **One branch, one PR, per task.** Reviewed the same day.
3. **Every PR states what it cost.** Latency and dollars, measured.

Week 3 adds two more:

### 4. Write the hypothesis before you run the experiment

Every experiment in `EXPERIMENTS.md` has a hypothesis — *what you expect to
change, and why* — committed **before** its result. Git history shows the order,
so your reviewer can check it.

> If you write the hypothesis after seeing the number, every experiment "confirms"
> what you expected. That isn't measurement, it's storytelling.

### 5. Tune on dev, report on test

Task 2 splits your eval set into **dev** (iterate as often as you like) and **test**
(frozen; run it only to confirm a decision). Day-to-day progress is reported on
dev. Any claim that a change made the system better is confirmed on test, and
every test run is committed so a reviewer can count them.

Your mentor also holds a **hidden holdout set** — questions you won't see — which
runs against your service on Friday. A large gap between your test score and your
holdout score means you tuned the system to your own questions.

---

## Setup

```bash
pip install -r week1/requirements.txt -r week2/requirements.txt -r week3/requirements.txt
cp week3/.env.example week3/.env      # merge with your Week 2 .env
```

The corpus is in `week3/corpus/`. Read `week3/corpus/README.md` first — it's the
note the Knowledge Platform team sent with the export, and it describes the
access model you'll have to enforce.

The eval format and the deterministic scorer are in `week3/eval/` (see
`eval/README.md`).

**Budget:** $25 of API spend for the week. Keep the running total in `COST.md`.
For scale: embedding the whole corpus once costs a few cents, while running a
100-example eval through the agentic graph costs real money. Retrieval-only
evals cost almost nothing, and that's deliberate — see Task 2.

---

## Where things live

```
week3/
├── README.md              ← you are here
├── SCHEDULE.md
├── RESULTS.md             ← behaviour and quality numbers
├── COST.md                ← spend, latency, budget
├── EXPERIMENTS.md         ← rule 4: hypothesis, then result
├── corpus/                the export (do not hand-edit — treat it as upstream data)
├── eval/                  seed set (40), schema, deterministic scorer
└── task_0N_*/README.md    one brief per task
```

As in Week 2, code goes where it belongs in the service (`app/`, `ingest/`,
`scripts/`, `tests/`), not into the task folders. Week 2's `RESULTS.md` and
`COST.md` stay as they are — they are your before-picture. Week 3's files sit
beside them.

---

## Definition of done for the week

`docker compose up` from a clean checkout of the `v1.1` tag still brings up a
working assistant, and `make check` is still green in under 5 seconds. Your
assistant answers correctly over the full corpus, and you can show which
category it is weakest in, with a number. It cites the current version of a
policy rather than whichever version it happened to retrieve. It never shows
Restricted content to someone outside the listed groups, through any path. Every
retrieval change you shipped is backed by an experiment whose hypothesis was
written first. Your holdout score is close to your test score. And you have
written a spec for next week that your mentor would approve.

Last week was about proving the system works. This week is about finding where it
doesn't. 🔍
