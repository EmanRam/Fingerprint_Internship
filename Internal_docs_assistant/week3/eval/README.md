# Week 3 eval format

`seed_eval.jsonl` contains 40 examples. Task 2 merges them with your 30 Week 2
examples, grows the set to 100, and splits it into
dev and test. One JSON object per line:

| Field | Type | Meaning |
|---|---|---|
| `id` | str | Stable ID. Never reuse one, even after deleting an example. |
| `category` | str | One of the categories below |
| `user_id` | str | Who is asking — a user in `corpus/_directory.csv` |
| `history` | list | Earlier turns, `[{"role": "user" \| "assistant", "content": ...}]`. Empty for single-turn questions. |
| `question` | str | The question being scored |
| `reference_answer` | str | A correct answer, for LLM judges and for people reading the file |
| `gold_docs` | list[str] | Corpus paths that contain the answer. Empty when the right behaviour is a refusal. |
| `must_include` | list[str] | Each entry must appear in the answer, case-insensitively. Separate alternatives with `\|`: `"3 days\|three days"`. |
| `must_not_include` | list[str] | None of these may appear in the answer |
| `expect_refusal` | bool | The answer must contain the standard refusal string |

The standard refusal string is unchanged from Week 1:
**`I don't know based on the provided documents.`**

## Categories

| Category | What it tests |
|---|---|
| `factual` | A single fact from a single document |
| `table` | The answer is in a table, often in a PDF |
| `keyword` | An exact identifier: error code, part number, policy ID |
| `version` | The current version of something that has changed |
| `conflict` | Sources disagree and nothing marks one as replacing another |
| `draft` | A draft exists and must not be presented as policy |
| `multi_hop` | Two facts must be combined (e.g. country → tier → amount) |
| `multi_part` | The answer has several required parts |
| `ambiguous` | The question has more than one reading |
| `long_doc` | The answer is buried in a long document |
| `cross_lingual` | An English question whose answer exists only in Arabic |
| `follow_up` | Can only be answered using the conversation history |
| `personalized` | The right answer depends on who is asking (tenure, office) |
| `access` | Restricted content: refuse unauthorised users, answer authorised ones |
| `out_of_scope` | The answer isn't in the corpus — refuse |

## Scoring

`scoring.py` holds the deterministic checks. They are cheap, involve no LLM, and
give the same result every time. **They are a floor, not a replacement for your
judges.** An answer can contain "3 days" and still be wrong, but an answer that
doesn't contain it isn't right.

```python
from eval.scoring import load_examples, check_answer
for ex in load_examples("week3/eval/seed_eval.jsonl"):
    answer = my_service(ex)            # replay ex["history"] first for follow-ups
    print(ex["id"], check_answer(ex, answer))
```

Your mentor's Friday holdout uses the same rules, plus a leak check across **every**
answer: no restricted content may reach a user outside its ACL groups, whatever the
question's category.
