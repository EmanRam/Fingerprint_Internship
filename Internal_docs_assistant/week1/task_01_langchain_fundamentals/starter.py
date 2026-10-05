"""
Task 1 — LangChain Fundamentals (LCEL)

Fill in each TODO. Run with:  python task_01_langchain_fundamentals/starter.py
"""

import sys
from pathlib import Path

# Make the repo root importable so `from common.utils import ...` works.
sys.path.append(str(Path(__file__).resolve().parents[1]))

from pydantic import BaseModel, Field

from common.utils import get_llm, DATA_DIR

llm = get_llm()


# ---------------------------------------------------------------------------
# Chain 1 — prompt | model | output parser
# ---------------------------------------------------------------------------
def chain_one_shot():
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser

    # TODO 1a: Build a ChatPromptTemplate with a {topic} variable that asks the
    #          model to explain the topic to a 10-year-old in 2 sentences.
    prompt = ...

    # TODO 1b: Compose prompt | llm | StrOutputParser() using the LCEL pipe.
    chain = ...

    # TODO 1c: Invoke the chain with {"topic": "vector databases"} and return it.
    return ...


# ---------------------------------------------------------------------------
# Chain 2 — structured / validated output
# ---------------------------------------------------------------------------
class DocClassification(BaseModel):
    """Schema the model MUST fill in."""
    category: str = Field(description="One of: HR, IT, Product, Finance")
    summary: str = Field(description="One sentence summary")
    contains_pii: bool = Field(description="True if the text contains personal data")


def chain_structured(text: str):
    # TODO 2a: Use llm.with_structured_output(DocClassification) to get a model
    #          that returns a DocClassification object instead of raw text.
    structured_llm = ...

    # TODO 2b: Invoke it on `text` and return the object.
    return ...


# ---------------------------------------------------------------------------
# Chain 3 — summarize a document from data/
# ---------------------------------------------------------------------------
def chain_summarize(doc_path: Path):
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser

    text = doc_path.read_text(encoding="utf-8")

    # TODO 3a: Prompt the model to summarize {document} as exactly 3 bullet points.
    prompt = ...

    # TODO 3b: Build and invoke the chain with {"document": text}. Return the result.
    chain = ...
    return ...


if __name__ == "__main__":
    print("=== Chain 1: one-shot ===")
    print(chain_one_shot())

    print("\n=== Chain 2: structured output ===")
    sample = "Employees accrue 20 days of PTO per year; contact jane.doe@corp.com."
    print(chain_structured(sample))

    print("\n=== Chain 3: summarize product_specs.md ===")
    print(chain_summarize(DATA_DIR / "product_specs.md"))
