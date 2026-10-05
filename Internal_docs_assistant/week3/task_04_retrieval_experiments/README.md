# Task 4 — Retrieval Experiments

**Focus:** changing one thing at a time, and believing only differences bigger
than the noise.
**Scaffolding:** 🔴 Spec-only.
**Time budget:** one full day (Wednesday).
**Branch:** `week3/task-04-experiments` (one PR, many experiments — commit per experiment)

---

## Why this task

This is the most important task of the week.

Week 1's retrieval benchmark compared four strategies on six questions over four
documents, a setting where the strategies barely differ. This week you design the
experiments yourself, against a corpus where retrieval choices really do change
the outcome, using an eval cheap enough to run dozens of times.

Most RAG quality work in practice is this loop: form a hypothesis, change one
thing, measure it, keep or revert the change, and write it down.

---

## What to do

### 1. Measure the noise floor first

Run your baseline retrieval eval on dev **three times**. If any part of retrieval
is non-deterministic (multi-query rewriting, an LLM in the loop), the scores will
vary from run to run. That spread is your **noise floor**. Any later difference
smaller than it counts as "no change", however much you'd like it to be an
improvement.

If retrieval is fully deterministic, say so and explain why. That's a valid
finding too.

### 2. Run at least five experiments

Choose from this list, or design your own. **Each experiment changes exactly one
thing.**

| Lever | Example question |
|---|---|
| Chunking strategy | Structure-aware chunks (by heading or table row) vs fixed size? |
| Chunk size / overlap | Where is the sweet spot for this corpus? |
| Contextual chunk headers | Does prepending `title > section` to each chunk before embedding help? |
| Hybrid weights | BM25 / dense split — does `keyword` improve without hurting `version`? |
| Re-ranking | A cross-encoder over the top 20 — what does it gain, and what does it cost in latency? |
| Metadata filters / boosts | Prefer `policy-portal` over `meetings/`? Down-weight `status: superseded`? |
| Embedding model | Does a multilingual model fix `cross_lingual`, and what does it break? |
| Query rewriting | HyDE or multi-query — does it help `follow_up` or `ambiguous`? |

### 3. Log every experiment in `EXPERIMENTS.md` before you run it

Each row needs: ID, hypothesis, the single change, the config diff, then the
results — recall@5 and MRR overall and **by category**, latency per query, and
cost per query. Commit the hypothesis, then run, then commit the result. Git
history shows the order (rule 4).

### 4. Choose, then confirm once on test

Choose the winning configuration **on dev**, then run it **once** on test. If the
test result disagrees with dev, report that honestly — don't go back and pick a
different winner because test liked it better. Re-selecting on test would make
test just another dev set.

### 5. Re-measure what Week 2 measured

Run your Week 2 cost report (`make cost`) on the winning configuration. In Week 2
you named the most expensive node and proposed a way to reduce it. Is it still the
most expensive node? A re-ranker can change that: if it lets you send fewer
documents to `grade_documents`, the graph might get *cheaper* while retrieval gets
better. Check whether that happened.

A re-ranker or a new embedding model also has a deployment cost. Rebuild the
Week 2 image and record the size change. `sentence-transformers` brings in torch,
which can add gigabytes. If the gain doesn't justify that, it's a legitimate
reason to reject the winner, and you should write that up.

### 6. Update the gate

Your Week 2 CI eval gate now gets a retrieval baseline as well. A PR that drops
recall@5 by more than your tolerance goes red. Measure a reasonable tolerance from
the noise floor rather than guessing one.

Decide which CI job it belongs in. Retrieval with an API embedding model needs a
key, and Week 2's rule is no API keys in the per-PR fast job. Either put the check
in the eval-gate job (nightly or manual), or make the fast job key-free by using a
local embedding model or embeddings cached in the repo. Write down which you chose
and what it costs: a regression caught nightly is a regression that has already
been merged.

---

## Done when…

- [ ] Noise floor measured (3 baseline runs), recorded in `EXPERIMENTS.md`.
- [ ] At least **5 experiments**, each with its hypothesis committed before its
      result, and per-category numbers.
- [ ] At least one experiment **made things worse**, and you understand why. If
      nothing got worse, your experiments weren't ambitious enough.
- [ ] Winner chosen on dev, confirmed once on test; both numbers in `RESULTS.md`.
- [ ] `COST.md` records the winner's latency and cost per query against the
      baseline, the cost by node compared with your Week 2 table, and the Docker
      image size before and after.
- [ ] The CI gate includes a retrieval check, with its tolerance derived from the
      noise floor.

---

## Traps

- **Averages hide trade-offs.** Hybrid search will very likely help `keyword` and
  may hurt `cross_lingual`, because BM25 can't match English query words against
  Arabic text. Look at the per-category numbers before declaring a winner.
- **Re-rankers cost latency.** A cross-encoder over 20 candidates on CPU can add
  more latency than the whole rest of retrieval. Measure it, and decide whether
  the gain is worth it.
- **Access control changes recall.** Once Task 6 is in, re-run your winner. Recall
  can drop when users can no longer retrieve documents they shouldn't have seen —
  that drop is correct behaviour, not a regression.
