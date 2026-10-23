# oncolytic-virus-harmonization

A documented attempt to put oncolytic virus screening results from published
preclinical papers into one schema, so that measurements from different studies
can be compared or shown to be incomparable.

**Status: scaffold. No data has been extracted yet.** The schema, the templates
and the empty tables are here. The `data/harmonized/` tables contain headers
only. Nothing in this repository has been measured, scored or benchmarked.

## The question

Two screens of the same cell line panel with the same viral genus can
differ in assay, multiplicity of infection, timepoint and metric. Can those results be placed in a single table without
hiding the differences that make them incomparable, and how many models are
actually shared once names are resolved?

## Why it matters

Published screens are a practical source of permissivity data for anyone
without a laboratory. If they cannot be compared, then a claim about one
virus being better than another across studies rests on a comparison nobody
has checked. Finding out
exactly where the comparison breaks is the useful outcome, whether or not a
usable table comes out of it.

A catalogue of this literature already exists in the form of OvirusTdb
(Raghava group, IIIT-Delhi, <https://webs.iiitd.edu.in/raghava/ovirustdb/>).
It answers what has been tried. It does not answer whether two reported
numbers mean the same thing.

## What this is NOT

* **Not a treatment selector.** It cannot be used to choose a therapy for a
  patient.
* **Not clinical decision support.**
* **Not a guide to self-administering any virus.** Nothing here describes how
  to obtain, handle or administer a virus to a person or an animal.
* **No laboratory protocols.** This repository holds data about published
  experiments, not instructions for performing them.
* **Nothing here is clinically actionable.** The underlying studies work with
  small numbers of models, and organoid work in this field runs with
  single-digit to low double-digit patient counts.

## Scope of the public work

Phase 0 and phase 1 only.

| Phase | Deliverable | In this repository |
|---|---|---|
| 0 | A versioned knowledge base, one YAML file per virus, every biological field carrying its own citation | template only, no virus files yet |
| 1 | Harmonization of three published studies into one schema, with assay metadata and a per value confidence label | schema and empty tables |

A scoring engine and a benchmark are out of scope until there is data to
validate them against. Starting with the engine produces something with
nothing to test it on.

## Sources

Three studies open phase 1. Their identifiers, licenses and the reason each
one was chosen are in [`docs/sources.md`](docs/sources.md). No PDFs and no
figures from those papers are redistributed here. Only extracted values, their
citation and their location inside the paper.

## Design decision that does not change

Output never collapses to a single number. Every virus returns separate
layers, each with its own evidence level:

1. clinical trial
2. patient derived organoid
3. cell line
4. mechanistic reasoning only

A ranking that mixes clinical evidence with expression based inference and
emits one score is misinformation with good formatting.

## Repository layout

```
kb/virus/              one YAML file per virus (phase 0)
data/harmonized/       related CSV tables (phase 1), headers only for now
gold-standard/         one paper extracted by hand, sealed before agents run
docs/schema.md         table definitions and the open questions
docs/preregistration.md  expected failures, written before extraction
docs/decision-log.md   every harmonization decision, with date and reason
docs/sources.md        the three studies, with DOI and license
docs/issues-backlog.md the task list, ready to open as issues
src/ovh/               package (skeleton)
tests/                 tests (skipped until the code exists)
```

## How the order of work is fixed

One paper is extracted by hand first and sealed in a commit before any agent
runs. Agent output is then compared against that sealed extraction. The
protocol is in [`gold-standard/README.md`](gold-standard/README.md). The
failures the schema is expected to hit are written down before extraction
starts, in [`docs/preregistration.md`](docs/preregistration.md), so that a
failure cannot be reinterpreted afterwards as a success.

## Metrics this project will report

Counts and rates, defined now and filled in later from the actual run.

* Number of papers, assays, models and measurements. `(fill from run)`
* Share of values by confidence level. `(fill from run)`
* Models shared between the three studies after name resolution. `(fill from run)`
* Field level agreement between two independent agent extractions, and how
  many disagreements a human had to arbitrate. `(fill from run)`
* Raw count of errors against the hand extracted paper, not a percentage.
  `(fill from run)`
* Minutes per paper, agent assisted against by hand. `(fill from run)`

## Install

```
python -m pip install -e .
pytest
```

The tests currently skip with an explicit reason, because the code they
describe is not written yet.

## How to contribute

Issues and pull requests are welcome, in English or Spanish.

* One virus per pull request for `kb/virus/`. Every field with biological
  content needs its own DOI. A field without a citation stays `null` and goes
  into `open_questions`.
* Changes to the schema go through an issue first, and land together with a
  row in `docs/decision-log.md`.
* Values read off a figure are accepted with low confidence and must say which
  tool was used to read them.
* Do not add PDFs, figures or full supplementary tables from third party
  papers. Add values with their citation and location.

## License

Code is MIT, see [`LICENSE`](LICENSE). Data, schema documents and prose are
CC BY 4.0, see [`LICENSE-DATA.md`](LICENSE-DATA.md).

## Citation

See [`CITATION.cff`](CITATION.cff). A citable archived release is a
possibility once there is data, not a commitment.
