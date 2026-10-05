# Task 2 — An Eval That Tells You *Where* It Broke

**Focus:** separating retrieval failures from generation failures, at a scale where
the numbers mean something.
**Scaffolding:** 🟡 Mixed — the metric definitions are provided in
`retrieval_metrics.py`; the dataset and the harness are yours to build.
**Time budget:** one day (Monday PM + Tuesday AM).
**Branch:** `week3/task-02-eval`

---

## Why this task

Your Week 2 eval answers *"was the final answer right?"* That's the question users
care about, but it's no help for debugging. When an answer is wrong, you need to
know which stage failed:

- **Retrieval:** the right document never reached the model.
- **Generation:** the right document was there and the model misused it.

These have different fixes, and Wednesday's experiments depend on knowing which is
which.

There's also a practical benefit. Retrieval metrics need no LLM calls at all, so
they run in seconds and cost almost nothing. That means you can afford to run
dozens of experiments on Wednesday instead of three.

---

## What to build

### 1. Grow the dataset to 100 — starting from what you already have

You already have two sources of examples. Use both before writing new ones:

| Source | Count | What to do |
|---|---:|---|
| Your Week 2 eval set (Task 7) | 30 | **Migrate** to the Week 3 schema: add `user_id`, `gold_docs`, `must_include` and a Week 3 category. Apply your Task 1 verdicts: update "world changed" examples to the new truth, and drop or fix any that only made sense on the 4-file corpus. Keep their original IDs. |
| `eval/seed_eval.jsonl` | 40 | Merge in. Where one duplicates a Week 2 example, keep yours and note the overlap. |
| New examples | the rest | Fill the categories that are still short. |

Week 2 → Week 3 category mapping: Factual → `factual` · Multi-hop → `multi_hop` ·
Multi-part → `multi_part` · Near-miss out-of-scope and Refusal → `out_of_scope` ·
Follow-up → `follow_up` · Keyword-precise → `keyword`. Week 3 adds nine new
categories; see `eval/README.md`.

Use the same schema throughout (see `eval/README.md`). Requirements:

- **At least 5 examples in every category** listed in `eval/README.md`.
- **Every answerable example has `gold_docs`.** Without them, retrieval can't be
  scored.
- **Access examples cover all six users** in `corpus/_directory.csv`. Include both
  directions: users who should be refused, and users who should get an answer.

You may use an LLM to generate candidate questions from chunks, and you should —
this is how it's done in practice. But **every generated example is reviewed by
you before it goes in.** Record how many you generated, how many you accepted,
and the most common reasons you rejected one. That acceptance rate is a useful
measure of how much to trust synthetic data.

### 2. Split it

Divide the 100 examples into **dev** (~70) and **test** (~30), stratified so every
category appears in both. Commit the split. From now on, **test is frozen**: you
iterate on dev and run test only to confirm a decision.

### 3. Score retrieval on its own

Implement the functions in `retrieval_metrics.py`:

- **recall@k** (document level) — did any gold document appear in the top k?
- **MRR** — how high did the first gold document rank?

Run them directly against your retriever, with no generation step. Report them by
category, at k = 1, 3, 5 and 10.

### 4. Score generation, with a judge that isn't the generator

Run the full pipeline, then score it with the deterministic scorer plus your
correctness and groundedness judges, by category.

**The judge must be a different model from the generator this week.** In Week 2
this was only a named limitation; now it's a requirement. Set it with
`JUDGE_MODEL`.

### 5. Check the judge against a human

Label 20 dev examples correct or incorrect **yourself**, then compare with the
judge's verdicts. Report the agreement rate, and list every disagreement with a
note on who you think was right.

### 6. Extend the Week 2 harness and gate — don't write new ones

Add the retrieval-only mode, the dev/test split and the Week 3 categories to your
Week 2 `scripts/run_eval.py`, so that `make eval` remains the single entry point.
Each run writes a JSON results file named after the git SHA and the dataset split,
which is what lets you compare runs across the week. Dev runs stay local
(`eval/runs/dev/` is gitignored). **Commit every test run** (`eval/runs/test/`).
That way a reviewer can count how many times test was used.

Then **re-set the baseline**: run the full pipeline on dev and commit a new
`eval_baseline.json`, with the dataset version bumped (e.g. `northwind-eval-v3`).
Keep your Week 2 tolerance and its justification unless the noise in Task 4 tells
you otherwise. The CI gate now protects *this* system.

---

## Done when…

- [ ] 100 examples, every category ≥5, committed with the dev/test split. All 30
      Week 2 examples are accounted for in `RESULTS.md`: migrated, updated, or
      dropped with a reason.
- [ ] New `eval_baseline.json` (dataset v3) committed; the CI gate uses it.
- [ ] Synthetic-generation numbers recorded: generated, accepted, rejected, and the
      top rejection reasons.
- [ ] `RESULTS.md` has retrieval metrics (recall@1/3/5/10 and MRR) by category on dev.
- [ ] `RESULTS.md` has generation metrics (deterministic, correctness,
      groundedness) by category on dev.
- [ ] Judge–human agreement on 20 examples is recorded, with the disagreements listed.
- [ ] A retrieval-only eval run takes **under 30 seconds** and costs **under $0.05**.
      Record both numbers.
- [ ] The Week 3 `make` targets (from `week3/Makefile`, merged into your Week 2
      Makefile) work.

---

## The question this task should answer

Look again at your Task 1 guess about the biggest drop. For that category, compare
recall@5 with the generation pass rate:

- **Low recall, low pass rate:** a retrieval problem. Wednesday is for you.
- **High recall, low pass rate:** a generation problem. Retriever tuning won't fix
  it; Task 5 probably will.

Write down which one it was, and whether your guess was right.
