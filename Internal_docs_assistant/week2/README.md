# AI Engineering Internship — Week 2: Ship It For Real

Week 1 built a RAG system. Week 2 turns it into a **service**: something other
software can call, that you can deploy, that tells you what it cost, and that
refuses to let you break it.

Same product — the Northwind Internal Docs Assistant. No new corpus, no new
domain. Everything you build this week sits on the code you already wrote.

---

## How this week works

Eight tasks and a Friday release. Seven of the nine are **spec-only**: a brief
and acceptance criteria, no starter code. That's deliberate: Week 1 ended with
spec-only work (Task 8 and the capstone), so Week 2 starts at that level.

| # | Task | Focus | Scaffolding |
|---|------|-------|-------------|
| 1 | Close Week 1 — and prove it | Finishing what's open | 🔴 Spec-only |
| 2 | The golden-path test harness | Regression safety | 🟡 Mixed |
| 3 | Wrap it in a service | FastAPI, streaming, sessions | 🔴 Spec-only |
| 4 | Containerize & configure | Docker, 12-factor config | 🟡 Mixed |
| 5 | Observability | Traces, tokens, cost, latency | 🔴 Spec-only |
| 6 | Caching | Making a number move | 🔴 Spec-only |
| 7 | The eval gate in CI | Automated quality floor | 🔴 Spec-only |
| 8 | Resilience & guardrails | Failure paths | 🔴 Spec-only |
| ★ | Release v1.0 | Tag, runbook, demo | 🔴 Spec-only |

🟡 = partial skeleton + written spec.  🔴 = requirements and acceptance criteria only.

---

## The three standing rules

These apply to every task this week, and they are graded.

### 1. A task is done when the number is in the repo

Not when the code runs. Every task's "Done when…" checklist names the file its
measurement belongs in — `RESULTS.md` or `COST.md`, both at the root of `week2/`.
If the number isn't committed, the task isn't finished.

> The most common way good work loses marks is shipping working code with no
> recorded result. A benchmark that was built but never run, or an eval whose
> scores were never written down, can't be credited, however good the code is.
> The code is the easy half.

### 2. One branch, one PR, per task

Branch names are given in each task README (`week2/task-03-api`, etc.). Open the
PR when the checklist passes, and get it reviewed the same day — including for
tasks that "only touch config."

> Integration bugs — a one-line wrong import that silently switches off a
> required capability — are exactly what a same-day review catches in thirty
> seconds. One big commit at the end of the week is how they reach the demo.

### 3. Every PR description states what it cost

Latency and token/dollar impact, measured — even when the answer is "no change."
From Task 5 onward you'll have the tooling to make this automatic. Before that,
time it by hand.

---

## Setup

You already have a working environment from Week 1. This week adds a few things:

```bash
pip install -r week2/requirements.txt
cp week2/.env.example week2/.env     # then fill it in
```

New keys/settings beyond Week 1 are marked in `.env.example`. Everything from
Week 1's `.env` still applies.

Verify your Week 1 capstone still runs before you start Task 1, using whatever
command your capstone README documents. If your README doesn't document one,
that's the first finding for Task 1.

---

## Where things live

```
week2/
├── README.md              ← you are here
├── SCHEDULE.md            day-by-day grid
├── RESULTS.md             ← rule 1: measurements go here
├── COST.md                ← rule 1: cost/latency numbers go here
├── requirements.txt
├── .env.example
├── Makefile               make check / check-live / run / eval
└── task_0N_*/README.md    one folder per task
```

Your **code** goes where it belongs in the product, not in the task folder — the
task folders hold briefs and skeletons only. By Friday there should be a real
service layout (`app/`, `tests/`, `scripts/`), not nine folders of scripts.

---

## Definition of done for the week

A mentor can clone the repo, run one command, ask the assistant a question,
follow that answer from a log line to a LangSmith trace to a cost figure, open a
bad PR and watch CI reject it — and you can explain every one of those steps and
name the weakest part of your own system without being asked.

Good luck. Week 1 was about building. This week is about whether you can tell us
how well it works. 🚀
