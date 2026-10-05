"""
Deterministic answer checks for the Week 3 eval format.

This is the same scorer your mentor uses for the Friday holdout run, so if your
system passes it here, it is being judged by the same rules there. It is NOT a
replacement for your LLM judges — it is a cheap, noise-free floor underneath them.

Rules, per example (see eval/README.md for the full schema):
  * must_include      every entry must appear in the answer (case-insensitive).
                      An entry may list alternatives separated by "|".
  * must_not_include  no entry may appear in the answer.
  * expect_refusal    the answer must contain the refusal string, and nothing
                      from must_not_include.

    from eval.scoring import load_examples, check_answer
"""

from __future__ import annotations

import json
from pathlib import Path

REFUSAL = "I don't know based on the provided documents."
_REFUSAL_VARIANTS = [REFUSAL.lower().rstrip("."), REFUSAL.lower().replace("'", "’").rstrip(".")]


def load_examples(path: str | Path) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def _has(answer: str, entry: str) -> bool:
    a = answer.lower()
    return any(alt.strip().lower() in a for alt in entry.split("|"))


def is_refusal(answer: str) -> bool:
    a = answer.lower()
    return any(v in a for v in _REFUSAL_VARIANTS)


def check_answer(example: dict, answer: str) -> dict:
    """Return {"passed": bool, "reasons": [str]} for one answer."""
    reasons = []
    for entry in example.get("must_include", []):
        if not _has(answer, entry):
            reasons.append(f"missing: {entry!r}")
    for entry in example.get("must_not_include", []):
        if _has(answer, entry):
            reasons.append(f"forbidden content present: {entry!r}")
    refused = is_refusal(answer)
    if example.get("expect_refusal") and not refused:
        reasons.append("expected a refusal")
    if not example.get("expect_refusal") and refused:
        reasons.append("refused an answerable question")
    return {"passed": not reasons, "reasons": reasons}
