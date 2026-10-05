# ★ Friday — The Holdout, and Next Week's Spec

**Focus:** whether it generalises, and whether you can design the next step.
**Scaffolding:** 🔴 Spec-only (an RFC template is provided).
**Time budget:** full day.
**Branch:** `week3/friday-rfc`

---

## Morning — the holdout

Your mentor holds a set of questions you haven't seen, covering the same categories
as your eval. At 09:30 they run it against your `v1.1-rc` tag, brought up the
Week 2 way — a clean clone, `.env` supplied, `docker compose up` — through
`POST /chat`, using the contract from Task 6. If the container doesn't come up,
the holdout doesn't run; it's the same pass-or-fail test as last Friday's demo
step 1. Scoring uses the same deterministic rules as `eval/scoring.py`, plus a
leak check on every answer.

Your job this morning is the **gap analysis**:

| | Deterministic pass rate | Notes |
|---|---:|---|
| Dev (what you tuned on) | | |
| Test (frozen, run once per decision) | | |
| Holdout (unseen) | | |

- A **small gap** between test and holdout means your system generalises. Say so,
  with the numbers.
- A **large gap** means you tuned to your own questions somewhere. Find where, by
  category. That finding is worth more than a high score.

You also get the list of holdout examples you failed, but not their wording.
Diagnose at least three as **retrieval** or **generation** failures, using your
own tools: re-run the closest dev example, check recall, and read the trace.

---

## Afternoon — write next week's spec

**Week 4 is "The assistant takes actions."** So far the assistant has only read
documents. Next it will do things on the user's behalf: file an IT ticket, submit
a PTO request, book a demo rover. That brings tool calling, actions with side
effects, confirmation steps, and humans approving actions.

Until now you've worked from specs other people wrote. This time you write the
spec. Use `RFC_TEMPLATE.md`. It must cover:

- **Problem and goals**, including **non-goals**. What you deliberately won't do
  matters as much as what you will.
- **Design:** which actions, how the graph changes, where confirmation happens, and
  what happens if an action fails halfway through.
- **Safety:** what the assistant may do without asking, what needs confirmation,
  and what it must never do. How does Task 6's access model carry over to *actions*?
- **Evaluation plan:** how you'll measure whether an action-taking assistant is
  good, and which new eval categories it needs.
- **Cost and latency estimate**, from your Week 2 and Week 3 numbers rather than
  intuition.
- **Risks and open questions.**
- **A Monday–Friday plan** with a definition of done for each day.

Your mentor reviews it the way a senior engineer reviews a real RFC: they comment,
you revise, and the approved version becomes Week 4's brief. Expect at least one
round of revision. A spec that's approved without changes usually wasn't
ambitious enough.

---

## The demo (10 minutes)

0. **`docker compose up` from a clean clone of `v1.1`** — the Week 2 opener, still
   binary.
1. **The cliff and the climb.** The seed eval by category: Monday's baseline
   against Friday's system, one chart.
2. **The best experiment and the worst.** One that helped, one that hurt, and why.
3. **Time travel.** The same question at two `AS_OF_DATE`s, with two correct answers.
4. **The leak attempt.** An employee tries three ways to get salary data, live.
5. **The gap.** Dev against test against holdout.
6. **The RFC in two minutes.**
7. **Answer this:** *"What's the weakest category now, what's its number, and is it
   a retrieval or a generation problem?"*

---

## Done when…

- [ ] The holdout has been run, and the gap table is in `RESULTS.md`.
- [ ] Three holdout failures have been diagnosed as retrieval or generation.
- [ ] The RFC is committed as `docs/RFC-001-actions.md` and has had one round of
      review.
- [ ] **Release v1.1**, tagged after the holdout. Update the Week 2 release
      documents rather than rewriting them:
  - `CHANGELOG.md`: a v1.1 entry, in your own words, including the API change
    to `sources` and the new `user_id` requirement.
  - `ARCHITECTURE.md`: ingestion pipeline, ACL filtering, source authority, the
    winning retrieval configuration, and the updated Mermaid diagram.
  - `RUNBOOK.md`: new sections on **re-ingesting after a document changes**,
    **responding to a suspected data leak** (who to tell, how to find affected
    requests from the logs, how to roll back), and **the CI gate going red on the
    new baseline**.
- [ ] `RESULTS.md`, `COST.md` and `EXPERIMENTS.md` have no empty required cells.
- [ ] Week total API spend in `COST.md`, against the $25 budget.
