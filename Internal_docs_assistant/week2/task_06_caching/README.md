# Task 6 — Caching, And Prove The Savings

**Focus:** making a number move, deliberately.
**Scaffolding:** 🔴 Spec-only.
**Time budget:** half a day (Thursday AM).
**Branch:** `week2/task-06-cache`

---

## Why this task

An internal assistant gets asked the same twenty questions forever. "How much PTO
do I get?" is not a research problem after the first time.

This is placed immediately after Task 5 on purpose: it is the first task of the
week where you get to **make a number move**, and you now have the instrument to
measure it. Build the cache, then prove it was worth building. If it isn't worth
it, that's a legitimate result — say so with numbers.

---

## What to build

### Layer 1 — exact-match answer cache

Key on the normalised question. Normalise properly: lowercase, strip whitespace
and trailing punctuation, so *"How much PTO do I get?"* and *"how much pto do i
get"* hit the same entry.

**The hard part is the key, not the cache.** A follow-up question like *"can I
carry it over?"* means something different in every conversation — if your key
ignores session context, you will serve the wrong answer to the right question.
Decide what belongs in the key and write down why.

### Layer 2 — embedding cache

Identical text should not be embedded twice, across runs. LangChain ships
`CacheBackedEmbeddings` for exactly this; wrap your embeddings with it and back
it with a local file store.

### Layer 3 — semantic cache (a decision, not a default)

Near-duplicate questions hit the cache: *"how many vacation days"* vs *"how much
PTO do I get"*.

**Implement it, or write two paragraphs arguing why it's wrong here.** Both are
acceptable answers. An unargued default is not. Things worth weighing: the
similarity threshold's false-positive risk on a corpus where HR topics cluster
tightly (the same problem as Week 1 Task 3's related-but-wrong chunks, where a PTO
question can retrieve the expense policy), and the fact that a semantic cache lookup costs an embedding call, so
it isn't free.

### Invalidation

What happens to cached answers when a document changes? Your capstone's ingestion
step can already add documents (or should — the capstone brief asked for it). Wire
the two together so a stale answer cannot be served after
the corpus changes.

---

## Done when…

- [ ] `week2/COST.md` has the before/after table: mean latency, p95 latency, and
      cost per question, **cold cache vs warm cache**, over the same 20 examples.
- [ ] Cache hit rate reported over a repeated-question workload **you define** —
      and the workload is described, so the number means something.
- [ ] An invalidation test proves a stale answer is not served after
      `add_document` runs. Name the test in `week2/RESULTS.md`.
- [ ] The semantic-cache decision is written down with its reasoning, either way.
- [ ] `cache_hit` shows up in the Task 5 log line and in `/metrics`.
- [ ] `CACHE_ENABLED=false` in `.env` fully disables it — with a test proving the
      uncached path still works.

---

## Two traps

**Don't cache refusals.** If the assistant says *"I don't know based on the
provided documents"* and someone then adds the document that answers it, a cached
refusal is worse than no cache — the system now confidently withholds an answer it
has. Either skip caching refusals entirely, or give them a much shorter TTL. Say
which you chose and why.

**Don't let the cache hide a regression.** Task 7's eval gate must measure the
*real* pipeline. Make sure the eval run bypasses the cache, or your gate will
happily pass a broken generate node because it never called it.

---

## Stretch

- Cache the retrieval step separately from the answer. Retrieval is deterministic
  and cheap to cache; generation is where the money is. Two TTLs, two hit rates —
  which one carries the saving?
- Pre-warm the cache at startup with the top 10 questions from your eval set, and
  measure the effect on p95 latency for a cold-start user.
