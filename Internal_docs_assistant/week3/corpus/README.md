# Northwind Knowledge Export — snapshot 2026-10-01

*From the Knowledge Platform team.*

This is a one-off export of everything the assistant is going to be allowed to read:
the policy portal, the wiki, the shared drive, the intranet newsletter archive, the
scanned-records archive, and the old intranet that was migrated in January. It is
what we have. It has not been cleaned, deduplicated or reviewed for accuracy — that
is part of your job.

## What's in here

| Folder | Source system | What it is |
|---|---|---|
| `policies/` | policy portal | Official HR, Finance and IT policies (PDF) |
| `product/` | shared drive | Data sheets, manuals, error codes, parts, release notes |
| `wiki/` | wiki | Wiki pages, exported as HTML with the page chrome |
| `newsletters/` | intranet | Monthly internal newsletter |
| `meetings/` | shared drive | Meeting notes from many teams |
| `cairo/` | wiki (Cairo space) | Cairo office pages, maintained locally in Arabic |
| `hr_restricted/` | shared drive | People Operations material with restricted access |
| `scanned_archive/` | scanned records | OCR output from old paper documents |
| `legacy_intranet/` | old intranet | Pages migrated from the 2024 intranet |

Formats: PDF, HTML, Markdown, plain text, XLSX, CSV.

## The two CSV files

**`_metadata.csv`** — the document-management export, one row per document:

| Column | Meaning |
|---|---|
| `path` | Relative to this folder |
| `title` | Title as recorded in the source system |
| `owner_team` | Owning team |
| `acl_groups` | `;`-separated groups allowed to read it. A user may read a document if they belong to **any** of its groups. `all` = every employee. |
| `last_modified` | As reported by the source system |
| `source_system` | Where it came from |

The ACL column is authoritative and is the access model you must enforce. Treat
everything else in the export with professional suspicion.

**`_directory.csv`** — an export from the identity provider of the demo users you
will test with: user id, name, title, department, office, groups, hire date. In
production these would come from the SSO token; for the internship, the service
looks them up by `user_id`.

## Known issues we're aware of

- Wiki pages include navigation menus, breadcrumbs and footers in every file.
- Some PDFs have page headers and footers repeated on every page.

There are others we haven't found yet. If you find one, tell us — write it down in
`week3/RESULTS.md` under Task 1.

## Classification reminder

`hr_restricted/` contains **Restricted** data (see the Data Classification Standard
in `policies/it/`). An assistant that shows Restricted content to someone outside
the listed groups is a security incident, not a bug.
