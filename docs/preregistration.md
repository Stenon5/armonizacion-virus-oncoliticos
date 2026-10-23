# Preregistration

Written on 2026-10-22, before any value has been extracted. Nothing in this
file may be edited after extraction starts. Changes go into a new file named
`preregistration-amendment-<date>.md` that says what changed and why.

The point of this file is simple. The schema is expected to fail in specific
ways. If those failures are written down first, a failure stays a failure and
cannot be recast afterwards as a finding.

## What counts as success

Success is not a full table. Success is a defensible answer to this question:
can measurements from these three papers be compared, and if not, exactly
which field makes them incomparable.

Both of these are acceptable outcomes and both get published:

* A harmonized table plus an explicit list of comparisons it does not support.
* A documented demonstration that the comparison is not possible, naming the
  fields that break it.

## Expected failures of the schema

Each one is a prediction. After extraction, each gets marked as happened, did
not happen, or happened differently, in `decision-log.md`.

1. **Assay incompatibility.** Viability and viral titre will not fit in one
   `value` column in any way that allows them to be compared. Expected effect:
   `direction` and `value_unit` keep them separable, but no cross metric
   comparison is possible.
2. **MOI is not a single number.** At least one paper will report MOI in a way
   that is not directly comparable to the others, for example computed against
   a different basis or given as a range. `moi` alone will not be enough.
3. **Timepoints will not line up.** The chosen timepoints will differ enough
   that `timepoint_h` cannot be matched exactly between papers, only binned, and
   binning will be a judgement call.
4. **Category against continuum.** At least one paper reports a susceptibility
   category and another a continuous value. Deriving the category from the
   continuum will require a threshold that the original authors did not use.
5. **Few shared models.** After name resolution the number of models shared
   across all three papers will be small. The third paper uses patient derived
   cultures, so the intersection with the cell line panel may be zero.
6. **Names will not resolve cleanly.** Some published cell line names will map
   to more than one Cellosaurus entry, or to none.
7. **Figure only values.** Some values exist only inside a figure. They will
   enter with low confidence, and the spread of digitised values will be wider
   than the precision the paper implies.
8. **`comparable_group` may be unusable.** The field may end up with one group
   per paper, which would mean it carries no information.
9. **Normalisation is often unstated.** `normalization` will be empty for a
   substantial share of rows.
10. **The virus is not one object.** Engineered strains of the same species
    differ in ways that matter, so one YAML file per strain may be needed
    rather than per species.

## Expected agent failure modes

Written before any agent runs, for the same reason.

1. Two independent agents will agree on the easy fields (model name, virus
   name) and disagree on assay metadata, which is where the harmonization
   actually lives.
2. An agent will report a value with high confidence that came from a figure.
3. An agent will silently normalise a unit, for example converting a
   percentage to a fraction, without saying it did.
4. An agent will fill a field that the paper does not state, using a plausible
   default.
5. An agent will cite the right DOI and the wrong table.

## How agent quality is measured

Decided now, so the metric cannot be chosen after seeing the numbers.

* **Agreement.** Field level agreement between two independent extractions of
  the same paper, reported per field, not as one global number.
* **Arbitration.** Count of disagreements that a human had to resolve, and how
  each was resolved.
* **Errors.** Raw count of wrong values against the hand extracted paper, as a
  count with the denominator stated, never as a percentage alone.
* **Time.** Minutes per paper, agent assisted against by hand, measured on the
  same paper.

A paper with few fields makes any percentage look impressive. That is why the
error metric is a count.

## Stopping rule

If the hand extraction and the agent extraction of the first paper disagree on
more than a handful of fields, extraction of the remaining papers stops until
the cause is written up in `decision-log.md`. Scaling a broken process across
three papers only produces three broken extractions.
