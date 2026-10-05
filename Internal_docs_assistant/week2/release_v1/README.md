# ★ Friday — Release v1.0

**Focus:** handing it over.
**Scaffolding:** 🔴 Spec-only.
**Time budget:** half a day + the demo (Friday PM).
**Branch:** `week2/release-v1`

---

## The brief

Everything you built this week becomes something a colleague could take over on
Monday without you in the room. That's the whole test.

---

## Deliverables

### 1. Tagged release `v1.0`

With `CHANGELOG.md` summarising the week **in your own words**. Not a git log
dump — what changed about the system and why it matters.

### 2. `RUNBOOK.md`

Written for someone who is not you. It must answer:

- How do I deploy this? How do I roll it back?
- What do the log fields mean? How do I find the trace for a bad answer a user
  reported?
- **What do I do when the eval gate goes red?** (Not "at 2am" — but the runbook
  shouldn't assume office hours either.)
- What are the failure modes, and what does each look like from the outside?
- What does it cost, and what's the first knob to turn if that becomes a problem?
- Who owns this?

A runbook that documents only the happy path isn't a runbook.

### 3. `ARCHITECTURE.md`

A Mermaid diagram of the system **as it now stands** — UI → API → graph → index,
with the cache, the traces, and the CI gate on it. Plus a short paragraph on each
boundary: what crosses it, and what happens when the thing on the other side is
down.

### 4. `RESULTS.md` and `COST.md` complete

Every number the week asked for, in one place. This is the deliverable that
reviewers open first, and it's the one that shows most.

### 5. A 10-minute demo

---

## The demo, in order

Your mentor will run roughly this. Rehearse it once — a demo that works on the
second attempt is a demo that failed.

1. **`docker compose up` from a clean checkout.** Binary: it comes up or it doesn't.
2. **A grounded question, streaming.** Tokens arriving; citation visible.
3. **An out-of-scope question**, then a prompt-injection attempt. Both refused.
4. **A two-turn follow-up.** Memory works across turns and is isolated per session.
5. **Open a log line, then the LangSmith trace it points to.** Narrate the node
   path — including *why* the graph took that path for that question.
6. **Show the cost report.** Be ready for: *what's the most expensive node, and
   what would you do about it?*
7. **Open a PR that weakens the prompt, live.** Watch CI go red.
8. **Answer:** *"Which eval category is weakest, and what's your plan?"*

---

## The question that matters most

The last one. The best possible answer is **specific and slightly
uncomfortable** — a real weakness, with a real number attached, and a plan you
actually believe in.

Your Week 1 `EVAL_RESULTS.md` asked for exactly this kind of failure analysis:
find a genuine miss, diagnose whether it's a retrieval or a generation problem,
and propose a specific fix.

Do that again, out loud, about a system ten times bigger.

---

## Done when…

- [ ] `v1.0` tagged, `CHANGELOG.md` written.
- [ ] `RUNBOOK.md` — hand it to someone who hasn't seen the project and watch them
      try to deploy it. Whatever they ask you is what's missing from it.
- [ ] `ARCHITECTURE.md` with a current Mermaid diagram.
- [ ] `RESULTS.md` and `COST.md` have no empty cells left.
- [ ] The demo ran start to finish without a fix in the middle.
- [ ] You can name the weakest part of your own system, with a number.
