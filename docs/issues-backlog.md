# Issue backlog

Every task below is ready to open as a GitHub issue. Title, label and
acceptance criteria are written out, so opening them is mechanical.

Phase 3 is conditional and is not promised anywhere.

## Phase 0, knowledge base

**[kb] Choose the first five viruses and justify the choice**
Label: `phase-0`
Accepted when: a row in `docs/decision-log.md` names the five viruses and says
why each one is in the starting set, and the choice covers at least two
different genomes.

**[kb] Write kb/virus/ entries for the chosen viruses**
Label: `phase-0`
Accepted when: one file per virus exists, every field with biological content
has a resolving `evidence_doi`, every uncited field is `null` and listed in
`open_questions`, and each file arrived in its own pull request.

**[kb] Verify every DOI in the knowledge base supports the sentence it is attached to**
Label: `phase-0`, `verification`
Accepted when: a human has opened each cited work and confirmed it states the
claim, and the share of fields with a verified citation is recorded.

**[code] Implement validate_kb**
Label: `phase-0`, `code`
Accepted when: `ovh-validate` checks every YAML file against the template,
fails on a field with content and no citation, and the matching test in
`tests/test_schema.py` is no longer skipped.

## Phase 1, harmonization

**[extract] Hand extract the first paper and seal it**
Label: `phase-1`, `gold-standard`
Accepted when: the files described in `gold-standard/README.md` exist, time
spent is recorded, and they land in a commit of their own whose message says
the extraction is sealed.

**[extract] Run two independent agent extractions of the sealed paper**
Label: `phase-1`, `agents`
Accepted when: both extractions are committed with `extracted_by: agent`, the
model and prompt are recorded, and neither one touched `gold-standard/`.

**[analysis] Compare agent extractions against the sealed paper**
Label: `phase-1`, `agents`
Accepted when: field level agreement is reported per field, disagreements are
listed with how each was resolved, and the error count is reported as a count
with its denominator, never as a percentage alone.

**[extract] Extract the 2020 NCI-60 study**
Label: `phase-1`, `extraction`
Accepted when: rows for that paper exist in the three tables and every
judgement call has a row in `docs/decision-log.md`.

**[extract] Extract the 2024 patient derived culture study**
Label: `phase-1`, `extraction`
Accepted when: as above, plus a note on whether `model_type` and the existing
fields survived a study that is not a cell line panel.

**[analysis] Resolve model names against Cellosaurus and count the overlap**
Label: `phase-1`, `analysis`
Accepted when: `cellosaurus_id` is filled wherever one exists, unresolvable
names are listed with the reason, and the number of models shared between the
three studies is reported. A small or zero overlap is a publishable result and
is written up as one.

**[code] Implement validate_tables**
Label: `phase-1`, `code`
Accepted when: foreign keys, enums and required columns are checked, the
command fails on a broken table, and the matching tests stop being skipped.

**[docs] Mark each predicted failure in the preregistration as happened or not**
Label: `phase-1`, `preregistration`
Accepted when: every numbered prediction in `docs/preregistration.md` has a
row in `docs/decision-log.md` saying what actually happened. The
preregistration file itself is not edited.

**[docs] Write the harmonization report**
Label: `phase-1`, `docs`
Accepted when: the README metrics are filled in from the real run, and the
report states plainly which comparisons the dataset does not support.

## Phase 2, release

**[release] Freeze dataset version 0.1**
Label: `phase-2`, `release`
Accepted when: a tagged release exists, the tables validate, and the release
notes list the open questions that are still open.

**[release] Decide whether an archived release with a DOI is worth it**
Label: `phase-2`, `release`
Accepted when: the decision is recorded with its reason. Archiving is a
possibility, not a commitment, and nothing in this repository promises it.

**[docs] Open AGENT_LOG.md for this repository**
Label: `phase-2`, `agents`
Accepted when: there is at least one real dated entry from this project. The
file is deliberately not created on day one, because an empty log is worse
than no log.

## Phase 3, conditional

Only if phases 0 to 2 finished and the agent error count turned out
acceptable. None of this is promised.

**[extract] Extend to more papers**
Label: `phase-3`
Accepted when: the schema absorbed the new papers without a breaking change,
or the breaking change is documented.

**[code] Reimplement the published interferon stimulated gene signature with tests**
Label: `phase-3`
Accepted when: the implementation reproduces the published numbers on public
data, or the gap is reported. Conditional on the source data being publicly
available under a license that allows it.

**[docs] Decide whether a preprint is worth writing**
Label: `phase-3`
Accepted when: the decision and its reason are recorded.
