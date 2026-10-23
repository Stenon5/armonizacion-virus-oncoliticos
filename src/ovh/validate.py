"""Validation of the harmonized tables and of the virus knowledge base.

Not implemented yet. The schema these functions are supposed to enforce is in
docs/schema.md, and the template they check against is in
kb/virus/_template.yaml.
"""

from __future__ import annotations

from pathlib import Path

NOT_IMPLEMENTED = (
    "not implemented yet: see docs/issues-backlog.md, phase 1. "
    "The schema is defined in docs/schema.md."
)


def validate_tables(data_dir: Path) -> None:
    """Check measurements, assays and models against docs/schema.md.

    Intended checks: required columns present, enum values inside their
    allowed set, every foreign key resolvable, every row carrying a
    source_doi and a source_location.
    """
    raise NotImplementedError(NOT_IMPLEMENTED)


def validate_kb(kb_dir: Path) -> None:
    """Check every kb/virus/*.yaml against the template.

    Intended checks: every field with biological content has an evidence_doi
    or is null, every null is mentioned in open_questions, every DOI is
    syntactically well formed.
    """
    raise NotImplementedError(NOT_IMPLEMENTED)


def main() -> int:
    """Entry point for the ovh-validate command."""
    print(NOT_IMPLEMENTED)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
