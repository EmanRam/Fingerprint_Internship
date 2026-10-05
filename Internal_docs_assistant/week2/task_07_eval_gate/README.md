# Task 7 — The Eval Gate In CI

**Focus:** making quality a thing a machine enforces, not a thing you remember.
**Scaffolding:** 🔴 Spec-only — a workflow skeleton is provided.
**Time budget:** half a day (Thursday PM).
**Branch:** `week2/task-07-ci`

---

## Why this task

**This is the keystone of the week.** If everything else slips, this is the task
that stays.

In Week 1 you built a measuring instrument: LLM judges, a dataset and a target
adapter. A measurement that runs only when someone remembers to run it isn't a
safeguard. Task 7 makes the measurement mandatory and automatic, and hands enforcement to something that
doesn't forget on a Friday afternoon.

---

## What to build

### 1. CI on every PR

GitHub Actions running `ruff` + the fast test tier. Under a minute, no API key,
no cost. This is the gate that catches wiring bugs, like an app importing the wrong graph, the day they're introduced.

### 2. An eval job

Runs the LangSmith suite and publishes correctness and groundedness. Nightly on a
schedule, `workflow_dispatch` to trigger it by hand, and on any PR labelled
**`run-eval`**. It doesn't run on every PR, because it costs real money and takes
minutes. Label the PRs that touch prompts, retrieval or the graph, and make the
job a required check, so that a red eval blocks the merge.

### 3. The threshold gate

The eval job **fails** if correctness or groundedness drops below the committed
baseline. Set the baseline from your Task 1 re-run and commit it as
`eval_baseline.json` — a fact under version control, not a memory.

Include a tolerance. LLM judges are noisy; a gate that fires on ±0.02 will be
disabled within a week because everyone stops believing it. Pick a tolerance,
justify it, and write the justification in the file.

### 4. Dataset expansion to 30 examples

Ten new ones, adversarial on purpose. At least two of each:

| Category | What it's designed to break |
|---|---|
| **Multi-hop** | The answer needs facts from *two* documents combined |
| **Multi-part** | E.g. "What are the password requirements?" — plural, where the model tends to answer with the first one and stop |
| **Near-miss out-of-scope** | Sounds internal, isn't in the corpus. Must refuse, not improvise from adjacent chunks |
| **Follow-up** | Only answerable with conversation history |
| **Keyword-precise** | An error code or part number where dense retrieval alone misses |

### 5. Category-split scoring

Report correctness and groundedness **per category**, not one blended average.

This is the growth item of the task. A blended 0.85 hides everything: if refusal
scores 1.0 and multi-hop scores 0.4, the average looks fine and the roadmap is
invisible. The split *is* the roadmap.

### 6. A regression report

Post a PR comment showing which examples changed verdict versus baseline. "Score
went from 0.90 to 0.85" is not actionable. "Examples 7 and 22 flipped from correct
to incorrect" is.

---

## What's provided

`workflows/ci_skeleton.yml` — job structure, triggers, and secret handling, with
`# TODO`s. Copy to `.github/workflows/`.

---

## Done when…

- [ ] A PR that **deliberately weakens the generate prompt** (delete the refusal
      instruction) is blocked by CI. Show the red build in your PR description,
      then revert it.
- [ ] `eval_baseline.json` is committed: scores, date, dataset version, and the
      tolerance with its justification.
- [ ] The dataset has **30 examples**. The 10 new ones are listed in
      `week2/RESULTS.md` with a note on what each is designed to break.
- [ ] The eval reports scores **split by category** — factual, multi-hop,
      multi-part, refusal, follow-up, keyword.
- [ ] At least **one real weakness** is found by the new adversarial examples and
      written up. If nothing fails, your examples aren't adversarial enough — make
      them harder.
- [ ] Fast CI runs in under 60 seconds. Record the time.

---

## The thing to be honest about

If your judge is the same model as your generator (the Week 1 starter uses
`get_llm()` for both), self-grading inflates scores — a model is a soft touch on its own output.

You don't have to change it this week. You **do** have to name it as a limitation
in `EVAL_RESULTS.md`, and ideally spend twenty minutes checking: run five examples
with a different model as judge and see whether the verdicts move. If they do,
that number belongs in the write-up.

---

## Stretch

- Run the improvement experiment from your Week 1 `EVAL_RESULTS.md` failure
  analysis: you named a failure and a fix, so test it now. (A common one:
  strengthen the `generate` prompt to list *every* relevant fact when a question
  has several parts.) Put the before/after in the experiment log.
- Fail the gate on **cost** as well as quality: if mean cost per question rises
  more than 20% against baseline, that's a regression too.
