# Decision log

Every harmonization decision goes here with a date and a reason. A decision
that later turns out to be wrong stays written and is corrected in a new row
below. Rows are never deleted.

The table is empty because no value has been extracted yet.

## Decisions

| Date | Decision | Reason | Affects |
|---|---|---|---|
| | | | |

## Reversals

| Date | Row reversed | What replaced it | Why the first one was wrong |
|---|---|---|---|
| | | | |

## Open questions carried from the schema

These stay open until the extraction answers them. Each one gets a row above
when it is closed.

1. Can viability and viral titre live in the same table, or do they need
   separate tables?
2. When one paper reports a category and another a continuous value, is the
   continuous value stored and the category derived, or are both stored?
3. What is done with values read off a figure, beyond marking them low
   confidence?
4. How many models are shared between the three papers after name resolution?
5. How many models have a public expression profile?
6. Is `comparable_group` defensible, or does every paper end up alone in its
   own group?
7. Is one YAML file per virus species enough, or does each engineered strain
   need its own file?

## How to add a row

One decision per row. The decision is what was done, not what was considered.
The reason says what would have gone wrong otherwise. `Affects` names the
files or fields that change because of it.
