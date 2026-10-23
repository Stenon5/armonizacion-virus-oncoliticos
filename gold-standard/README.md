# Gold standard

One paper, extracted entirely by hand, sealed in a commit before any agent
runs. Everything an agent produces later is measured against what is in this
folder.

**Status: empty. The hand extraction has not been done yet.**

## Why this exists

Agent error rate cannot be measured against another agent's output, and it
cannot be measured against a reference that was built after seeing the agent's
answer. The reference has to exist first and has to be fixed, otherwise every
disagreement gets resolved in whichever direction is more convenient.

## Protocol

1. **Choose the paper.** The 2011 NCI-60 study is the candidate, because it is
   the largest of the three and has the most assay metadata to get wrong. The
   choice is recorded in `docs/decision-log.md` when it is made.
2. **Extract by hand.** Every field of the schema, for every measurement, read
   from the paper and its supplementary material by a human. Time spent is
   recorded, because it is the denominator for the time saving claim.
3. **Record the location.** Every value carries `source_location`, for example
   `Table S3, row 12`. A value whose location cannot be stated does not go in.
4. **Mark what could not be read.** A field the paper does not state is left
   empty with a note. It is not guessed, and it is not filled from another
   paper.
5. **Seal it.** The files are committed on their own, with a commit message
   that says the extraction is sealed and names the paper. No later commit
   edits these files.
6. **Only then run agents.** Agent extractions of the same paper go to
   `data/harmonized/` with `extracted_by: agent`, never into this folder.
7. **Compare.** Field level agreement, the list of disagreements, and the raw
   count of agent errors against this folder, with the denominator stated.

## If the sealed extraction turns out to be wrong

It stays. A correction goes into a new file in this folder named
`corrections-<date>.md`, saying which value was wrong, what the right value
is, and how the error was found. The original file is not edited, because the
agent comparison that already used it has to remain interpretable.

## Files that will live here

```
gold-standard/
  README.md                this file
  <paper-key>/
    measurements.csv       hand extracted, sealed
    assays.csv             hand extracted, sealed
    models.csv             hand extracted, sealed
    extraction-notes.md    time spent, what could not be read, judgement calls
```
