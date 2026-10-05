# Task 1 — Close Week 1, and Prove It

**Focus:** finishing what's open, and verifying rather than assuming.
**Scaffolding:** 🔴 Spec-only.
**Time budget:** half a day (Monday AM).
**Branch:** `week2/task-01-closeout`

---

## Why this task

Shipping new features on top of a broken integration is how a small bug becomes an
architectural one. Before Week 2 builds on your capstone, it has to actually do
what Week 1 said it does — in the **running app**, not just in the code.

You'll also have a Week 1 review from your mentor. This task tests whether you can
close a review **completely** rather than partially. That's most of what code
review involves, for the rest of your career.

---

## What to do

### 1. Close every finding in your Week 1 review

Work through your review one finding at a time. For each one: fix it, **verify
the fix in the running system**, and record what you did. "Changed the code"
doesn't close a finding. "Changed the code, ran the app, and saw the behaviour
change" does.

### 2. Verify the capstone's must-haves in the running app

Whatever your review says, check each of these yourself by running the app:

- **The app runs the graph you think it runs.** Open the file the UI imports its
  graph from and follow the import. Integration bugs hide here: an app that
  imports an earlier task's graph instead of the capstone's will still run and
  answer, with features quietly switched off.
- **Multi-turn memory works.** Ask *"How much PTO do I get?"*, then *"Can I carry
  it over?"*. The second answer must resolve "it" without you repeating "PTO".
  Then check that a different session doesn't see the first one's history.
- **The index is persisted.** Restart the app twice. The second start must
  **load** the index from disk, not embed the corpus again. Add a startup log line
  that says which happened.
- **Refusal works.** An out-of-scope question gets the standard refusal.

### 3. Make it runnable by someone else

- The app's entry point is named as the capstone brief says (`app.py`, not a
  skeleton file).
- The capstone README has a **How to run** section: required environment
  variables, the ingest step, and the run command.
- Every file path is built from `Path(__file__)`, not hardcoded. A path that only
  works from one directory on one operating system will fail in Task 4's container.
- Configuration (model, provider, base URL) comes from the environment, not from
  string literals in the code.

### 4. Run any measurement you didn't run

Week 1 asked for several numbers. If any are missing, produce them now:

- **Task 6 benchmark:** the hit-rate table for every strategy, plus two
  sentences naming the winner and *why*, tied to how the questions are phrased.
- **Capstone eval:** correctness and groundedness over your full dataset (at least
  20 examples), dated, with the LangSmith experiment link.
- **Task 8 node paths:** proof that the rewrite → retry loop fires on an awkward
  query — or a written finding that it doesn't.

### 5. Clean the repo

Build artefacts, indexes and large binaries don't belong in git. Add
`__pycache__/`, `*.pyc`, `**/faiss_index/` and media files to `.gitignore`, and
remove anything already committed with `git rm -r --cached`. If you recorded a
demo video, link to it from the README rather than committing it.

---

## Done when…

- [ ] Every Week 1 review finding is closed, and `RESULTS.md` lists each one with
      how you verified it.
- [ ] The app answers *"How much PTO do I get?"*, then *"Can I carry it over?"*,
      and the second answer resolves "it" correctly. Screenshot committed.
- [ ] Restarting the app twice doesn't re-embed. Both startup log lines (one
      **built**, one **loaded**) are pasted into `RESULTS.md`.
- [ ] `RESULTS.md` has the Task 6 hit-rate table and your two-sentence explanation
      of the winner.
- [ ] The capstone eval results report correctness and groundedness over ≥20
      examples, dated, with the LangSmith experiment link.
- [ ] Every script runs from any working directory.
- [ ] `git ls-files` shows no `__pycache__`, no index files and no media files.
- [ ] One PR, reviewed and merged, before you start Task 2.

---

## A question to answer in the PR description

For the most serious finding you closed: why did it survive Week 1? Write one
honest sentence. It isn't a trick question and there's no wrong answer, but the
answer is usually the reason Task 2 exists, and the reason for this week's rule 2.

---

## Stretch

- If your Task 6 harness builds a separate FAISS index inside every
  `build_*_retriever` call, running it embeds the corpus several times. Build it
  once and pass it in, then record the time saved in `RESULTS.md`. That's your
  first cost measurement of the week.
