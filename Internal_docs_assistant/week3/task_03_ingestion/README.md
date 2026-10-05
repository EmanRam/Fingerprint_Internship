# Task 3 — Ingestion That Tells the Truth

**Focus:** parsing, metadata and deduplication. Most "retrieval problems" start here.
**Scaffolding:** 🔴 Spec-only.
**Time budget:** half a day (Tuesday PM).
**Branch:** `week3/task-03-ingestion`

---

## Why this task

Whatever your loader produces is everything the retriever can ever find. If a table
loses its structure, a page footer ends up in every chunk, or "Effective date" is
read as text rather than recorded as a field, no retriever can make up for it.

Treat this task as an experiment in its own right. You have Task 2's
retrieval-only eval, so measure recall before and after. Hold yourself to the same
standard as on Wednesday: a hypothesis first, then a number.

---

## What to build

### 1. A loader per format, chosen deliberately

The corpus contains PDF, HTML, Markdown, plain text, XLSX and CSV. For each format,
decide what a good chunk looks like and write down why. (`corpus/README.md`,
`_metadata.csv` and `_directory.csv` describe the corpus; they aren't documents
for the assistant to answer from.) In particular:

- **PDF tables.** Text extraction flattens a table into one cell per line, so
  "Germany" and "$260" end up several lines apart with nothing connecting them.
  Rebuild the rows — for example, `Tier A | Germany, ... | $90 | $260` — or use a
  table-aware extractor.
- **Page furniture.** Repeated headers and footers ("Page 7 of 23",
  "CONFIDENTIAL…") are noise in every chunk. Remove them.
- **Wiki chrome.** Every HTML file includes the navigation sidebar and footer.
  Keep the content, drop the chrome.
- **Spreadsheets.** A row like `E-217 | Drive | Left drive motor overcurrent | …`
  means nothing without its column headers. Decide how to keep them attached.
- **Text normalisation.** PDF extraction produces ligatures (`ﬀ`, `ﬁ`), so
  "time off" may not match "time oﬀ". Normalise the text (Unicode NFKC) and check
  that Arabic survives the process unchanged.

### 2. Metadata on every chunk

At minimum:

| Field | Where it comes from |
|---|---|
| `path`, `source_system`, `acl_groups` | `_metadata.csv` |
| `title`, `section` | The document itself (heading structure) |
| `language` | Detected |
| `effective_date`, `version`, `status` | **Parsed from the document text** where present |

Pay attention to the last row. `_metadata.csv` has a `last_modified` column, and
it's tempting to use it as a version date. Before you do, check what it actually
records for each source system. Task 5 depends on this being right.

### 3. Deduplication

Some content exists in more than one place, either exactly or nearly. Detect
duplicates and choose a policy (keep one, keep the most authoritative, or keep both
but rank them). Report how many you found, how you found them, and what you did
with them.

### 4. Incremental indexing

Store a hash of each document's content. Re-running ingestion after editing one
file should re-embed **only that file's chunks**. Prove it with a test that counts
embedding calls.

Build this on your capstone's existing ingestion code and on the Week 2 Task 6
embedding cache (`CacheBackedEmbeddings`). Between them, most of the mechanism
already exists.

### 5. Connect it to what Week 2 built

- **Answer cache (W2 Task 6).** In Week 2 you wired document additions to
  invalidate cached answers. Incremental re-ingest must do the same, for every document it
  adds, changes or removes. Your Week 2 invalidation test should still pass, and
  should now also cover a document being **changed**, not just added.
- **Container (W2 Task 4).** Mount the corpus into the container read-only, and
  keep the index on the named volume. `docker compose up` on a warm volume must
  **load** the index, not rebuild it. Your Week 2 startup log line ("index
  loaded" / "index built") is how you prove that.
- **Readiness (W2 Task 3).** `/readyz` reports the corpus snapshot date, the
  document count and the index build time, so an operator can see which data a
  running instance is serving.
- **Logging (W2 Task 5).** Ingestion writes structured log lines (documents added,
  changed, skipped with reasons, embedding calls, duration), in the same format as
  your request logs.

---

## Done when…

- [ ] Every document in the corpus loads, or is skipped **deliberately** and listed
      in an ingestion report with the reason. Nothing is skipped silently.
- [ ] `RESULTS.md` has before/after recall@5 by category on **dev**. The before
      number is your Task 2 baseline.
- [ ] `RESULTS.md` records duplicates found, your dedup policy, and chunk counts
      before and after.
- [ ] A test proves that changing one document re-embeds only that document, and
      invalidates its cached answers. Name it in `RESULTS.md`. It runs in the fast
      tier with fake embeddings, and `make check` stays under 5 s.
- [ ] `docker compose up` on a warm volume logs "index loaded", and `/readyz` shows
      the corpus snapshot.
- [ ] `COST.md` has full re-ingest time and cost, and incremental re-ingest time
      and cost for one changed file.
- [ ] The hypothesis for this change was committed before its result
      (`EXPERIMENTS.md`, rule 4).

---

## Trap

**Don't use `last_modified` as the version date.** Check what it actually means for
the `intranet-legacy` source before relying on it.
