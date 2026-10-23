---
name: Schema change
about: Add, remove or redefine a field in the harmonization schema
title: "[schema] "
labels: ["schema"]
---

**Field**
Table and field name.

**What breaks without the change**
Name the paper and the value that cannot be recorded correctly today.

**Proposed definition**
Type, allowed values, and whether it is required.

**Acceptance criteria**
- [ ] `docs/schema.md` updated.
- [ ] A row added to `docs/decision-log.md` with the date and the reason.
- [ ] The CSV headers in `data/harmonized/` updated.
- [ ] The header test in `tests/test_schema.py` updated.
- [ ] Rows already extracted either migrated or listed as needing migration.
