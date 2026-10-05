# Week 3 — these targets EXTEND your Week 2 Makefile. Merge them into it; don't
# keep two. Week 2's check / check-live / run / run-ui / eval / cost all stay,
# and keep their budgets: `make check` < 5 s, no API key.

.PHONY: ingest ingest-full eval-retrieval eval-test

ingest:            ## incremental: re-embed only changed documents, invalidate their cached answers (Task 3)
	python scripts/ingest.py

ingest-full:       ## rebuild the whole index from scratch
	python scripts/ingest.py --full

eval-retrieval:    ## retrieval-only, dev split: seconds, cents (Task 2)
	python scripts/run_eval.py --retrieval-only --split dev

# `make eval` (Week 2) now defaults to the dev split of the v3 dataset, cache bypassed.
eval-test:         ## frozen test split — run ONLY to confirm a decision (rule 5)
	python scripts/run_eval.py --split test --no-cache
