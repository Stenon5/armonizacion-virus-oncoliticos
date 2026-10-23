---
name: Virus knowledge base entry
about: Add or revise one virus file in kb/virus/
title: "[kb] "
labels: ["phase-0", "knowledge-base"]
---

**Virus**
Species and strain.

**Acceptance criteria**
- [ ] File follows `kb/virus/_template.yaml`.
- [ ] Every field with biological content has its own `evidence_doi`.
- [ ] Every DOI resolves and the cited work actually supports the statement.
- [ ] Fields without a citation are `null` and appear in `open_questions`.
- [ ] `curation.extracted_by` and `curation.reviewed_by_human` are filled in.
- [ ] One virus per pull request.
