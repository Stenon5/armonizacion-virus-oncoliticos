---
name: Data extraction
about: Extract values from one paper into the harmonized tables
title: "[extract] "
labels: ["phase-1", "extraction"]
---

**Paper**
DOI and title.

**What is being extracted**
Which table or figure, and which fields of the schema.

**Who or what extracts it**
Human, or agent with the model and the prompt recorded.

**Acceptance criteria**
- [ ] Every row has `source_doi` and `source_location`.
- [ ] Every row has a `confidence` value, low for anything read off a figure.
- [ ] `read_method` says table, text, or which tool digitised the figure.
- [ ] Values the paper does not state are left empty, not guessed.
- [ ] No PDF, figure or complete supplementary table is committed.
- [ ] Any new judgement call has a row in `docs/decision-log.md`.
