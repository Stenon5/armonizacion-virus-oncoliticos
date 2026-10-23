# Harmonization schema

Working document for phase 1. It is written **while** the three starting
papers are being harmonized, not before. The version in this commit is the
starting proposal, with no data behind it yet.

## Why this document exists

Two screens of the same cell line panel with the same viral genus are not
comparable out of the box. The assays differ, the multiplicity of infection
differs, the timepoints differ and the reported metric differs. The schema has
to record those differences instead of hiding them, because hiding them is
what makes an aggregated dataset useless.

Everything below is a proposal until the first paper is actually extracted. A
field that turns out to be unfillable gets removed and the removal is recorded
in `decision-log.md`.

## Tables

The tables live in `data/harmonized/` as CSV, so that a git diff stays
readable. A Parquet export can be added later for consumption. In this commit
the files hold headers only.

### `measurements.csv`

One row per measurement of one virus in one model.

| Field | Type | Notes |
|---|---|---|
| `measurement_id` | str | Key |
| `assay_id` | str | Foreign key to `assays.csv` |
| `virus_id` | str | Foreign key to `kb/virus/` |
| `model_id` | str | Foreign key to `models.csv` |
| `value` | float | In the unit of the assay |
| `value_unit` | str | For example viability fraction, or log10 PFU/mL |
| `value_type` | enum | `continuous` or `category` |
| `direction` | enum | `higher_is_more_permissive` or `lower_is_more_permissive`. Without this field, metrics cannot be compared at all |
| `confidence` | enum | `high`, `medium`, `low`. Low when the value was read off a figure instead of a table |
| `read_method` | str | `table`, `text`, or the tool used to digitise a figure |
| `source_doi` | str | |
| `source_location` | str | For example `Table S3` or `Figure 2B` |
| `extracted_by` | enum | `human` or `agent` |
| `notes` | str | Free text, kept short |

### `assays.csv`

One row per experimental condition. This is the table that decides whether the
project works.

| Field | Notes |
|---|---|
| `assay_id` | Key |
| `source_doi` | The paper the condition comes from |
| `readout` | Viability (MTT, crystal violet), viral titre, flow cytometry, imaging |
| `moi` | Multiplicity of infection, as reported |
| `moi_basis` | What the MOI was computed against, when the paper says so |
| `timepoint_h` | Hours post infection |
| `replicates` | |
| `normalization` | What the value was normalised against |
| `media_serum` | Culture conditions, when reported |
| `comparable_group` | Identifier shared by conditions judged comparable. Assigned by hand, with the reason in `decision-log.md` |

### `models.csv`

| Field | Notes |
|---|---|
| `model_id` | Key |
| `model_type` | `cell_line`, `pdx`, `organoid`, `patient` |
| `name_as_published` | The name exactly as printed in the paper |
| `cellosaurus_id` | Canonical identifier where one exists |
| `tissue` | |
| `depmap_id` | Bridge to public expression profiles, where one exists |
| `name_resolution_note` | How an ambiguous name was resolved |

### Virus annotation

Viruses are not a CSV table. They live as one YAML file per virus in
`kb/virus/`, because the content is curated annotation with a citation per
field, and that reviews better as YAML in a pull request. The template is
`kb/virus/_template.yaml`.

## Open questions, phase 1

These are answered by the attempt to harmonize the three papers, not before.

1. Can viability and viral titre live in the same table, or do they need
   separate tables?
2. When one paper reports only a category (high, medium, low susceptibility)
   and another reports a continuous value, is the continuous value stored and
   the category derived, or are both stored?
3. What happens to values read off a figure? Proposal: accept them with
   `confidence: low` and record the tool in `read_method`.
4. How many models are really shared between the three papers after names are
   resolved? If very few are, the dataset does not support cross study
   comparison, and that is itself a result worth reporting.
5. How many models have a public expression profile? Without expression there
   is no interferon layer.
6. Is `comparable_group` defensible at all, or does every paper end up alone in
   its own group?

## Decisions

Every harmonization decision is recorded in
[`decision-log.md`](decision-log.md) with a date and a reason. A decision that
later turns out to be wrong stays in the log and is corrected below it. It is
not deleted.
