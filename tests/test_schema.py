"""Pruebas de las tablas armonizadas.

Las pruebas que describen código sin escribir están omitidas a propósito, con
la razón en el mensaje de omisión, para que la integración continua de un
repositorio de andamiaje reporte la verdad en vez de un build rojo.
"""

from __future__ import annotations

import csv
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "data" / "harmonized"

EXPECTED_HEADERS = {
    "measurements.csv": [
        "measurement_id",
        "assay_id",
        "virus_id",
        "model_id",
        "value",
        "value_unit",
        "value_type",
        "direction",
        "confidence",
        "read_method",
        "source_doi",
        "source_location",
        "extracted_by",
        "notes",
    ],
    "assays.csv": [
        "assay_id",
        "source_doi",
        "readout",
        "moi",
        "moi_basis",
        "timepoint_h",
        "replicates",
        "normalization",
        "media_serum",
        "comparable_group",
    ],
    "models.csv": [
        "model_id",
        "model_type",
        "name_as_published",
        "cellosaurus_id",
        "tissue",
        "depmap_id",
        "name_resolution_note",
    ],
}


@pytest.mark.parametrize("filename", sorted(EXPECTED_HEADERS))
def test_table_headers_match_the_schema(filename: str) -> None:
    """Esta sí corre hoy. Los encabezados tienen que coincidir con docs/esquema.md."""
    path = DATA / filename
    with path.open(newline="", encoding="utf-8") as handle:
        header = next(csv.reader(handle))
    assert header == EXPECTED_HEADERS[filename]


def test_virus_template_exists() -> None:
    """Esta sí corre hoy."""
    assert (REPO / "kb" / "virus" / "_template.yaml").is_file()


@pytest.mark.skip(
    reason="todavía no implementado: validate_tables, ver docs/backlog-de-issues.md fase 1"
)
def test_every_measurement_has_a_resolvable_assay() -> None:
    raise AssertionError("inalcanzable mientras esté omitida")


@pytest.mark.skip(
    reason="todavía no implementado: validate_tables, ver docs/backlog-de-issues.md fase 1"
)
def test_every_measurement_carries_a_doi_and_a_location() -> None:
    raise AssertionError("inalcanzable mientras esté omitida")


@pytest.mark.skip(
    reason="todavía no implementado: validate_kb, ver docs/backlog-de-issues.md fase 0"
)
def test_every_kb_field_with_content_has_a_citation() -> None:
    raise AssertionError("inalcanzable mientras esté omitida")


@pytest.mark.skip(
    reason="todavía no implementado: no hay datos extraídos, ver referencia-manual/README.md"
)
def test_shared_models_between_the_three_studies_are_counted() -> None:
    raise AssertionError("inalcanzable mientras esté omitida")
