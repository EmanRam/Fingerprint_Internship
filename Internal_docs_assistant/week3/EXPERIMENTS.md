# Week 3 — Experiment Log

> **Standing rule 4:** write the hypothesis and commit it **before** you run the
> experiment. Then run it, fill in the result, and commit again. Your reviewer will
> check the order in `git log -p EXPERIMENTS.md`.
>
> **Standing rule 5:** tune on dev. Run test only to confirm the final choice.

---

## Noise floor

Three runs of the unchanged baseline on dev.

| Run | recall@5 | MRR | Notes |
|---|---:|---:|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| **Spread (max − min)** | | | |

**Is retrieval deterministic? Why or why not?**

>

**Smallest difference I'll treat as real:** recall@5 ± ___ · MRR ± ___

---

## Experiments

Copy this block once per experiment. Commit the top half first.

### EXP-01 — <short name>

**Hypothesis** *(committed before running)*: If I change ___, then ___ will
improve/worsen in categories ___, because ___.

**The one change:** 

**Config diff:**
```
```

**Result** *(committed after running)*:

| | Baseline | This | Delta | Bigger than noise? |
|---|---:|---:|---:|---|
| recall@5 (all) | | | | |
| MRR (all) | | | | |
| Latency / query | | | | |
| Cost / query | | | | |

Categories that moved by more than the noise floor:

| Category | Baseline R@5 | This R@5 |
|---|---:|---:|
| | | |

**Hypothesis confirmed?** Yes / No / Partly — and what I learned:

>

**Decision:** keep / revert / follow up with EXP-__

---

## Summary

| ID | Change | R@5 Δ | MRR Δ | Latency Δ | Decision |
|---|---|---:|---:|---:|---|
| EXP-01 | | | | | |
| EXP-02 | | | | | |
| EXP-03 | | | | | |
| EXP-04 | | | | | |
| EXP-05 | | | | | |
