# Week 2 — Day-by-Day Schedule

Full days on tasks; no course running alongside. Roughly 8 hours of build time
per day, so most slots are half a day and Tuesday is a full one.

| Day | AM | PM | Milestone |
|-----|----|----|-----------|
| **Mon** | Task 1 · Close Week 1 | Task 2 · Test harness | ✅ **Hard gate:** app works, memory works, tests guard the app's wiring |
| **Tue** | Task 3 · Service API | Task 3 continued | Assistant reachable over HTTP, streaming |
| **Wed** | Task 4 · Containerize | Task 5 · Observability | ✅ **Halfway:** runs in a container, first cost numbers on the board |
| **Thu** | Task 6 · Caching | Task 7 · Eval gate in CI | ✅ **Keystone:** CI blocks a regression |
| **Fri** | Task 8 · Resilience | ★ Release v1.0 + demo | Tagged release, runbook, 10-minute demo |

## Daily rhythm

- **09:00 — standup, 15 minutes.** Yesterday / today / one blocker.
- **Mid-afternoon — PR review, same day.** Short, focused on the decision rather
  than style. Same-day review isn't optional.
- **17:00 — the number.** Before you stop, whatever you measured today goes into
  `RESULTS.md` or `COST.md`. Two minutes. This is the habit the week exists to build.

## Checkpoints

| When | Gate | If it slips |
|---|---|---|
| **Mon 17:00** | Task 1 closed. App demonstrably does multi-turn. Index does not rebuild on restart. | Nothing else starts. Finish it Tuesday morning and compress Task 3. |
| **Wed 17:00** | Service running in a container. First cost-per-question figure committed. | Drop Task 6 (caching) from the week. |
| **Thu 17:00** | CI eval gate live and blocking a bad PR. | Drop Task 8, not this. |

## If you fall behind

Priority order to still reach a real Friday deliverable:

1. **Task 1** — closeout. Non-negotiable; everything else builds on a working app.
2. **Task 3** — the service. This is the week's headline deliverable.
3. **Task 7** — the eval gate. The keystone of what this week is teaching.
4. **Task 5** — observability. A service you can't see inside isn't finished.

Tasks 2, 4, 6 and 8 are enrichment in that order of value. The week survives
without any of them; it does not survive without 1, 3, 7.

## Definition of done for the week

You have "passed" Week 2 when the assistant runs from a clean checkout with one
command, answers over HTTP with streaming and citations, isolates sessions,
reports what each answer cost, blocks its own regressions in CI, and degrades
gracefully when the model provider fails — and `RESULTS.md` and `COST.md` contain
every number the tasks asked for.
