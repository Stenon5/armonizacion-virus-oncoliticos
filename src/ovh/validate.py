"""Validación de las tablas armonizadas y de la base de conocimiento de virus.

Todavía no está implementada. El esquema que estas funciones tendrían que
hacer cumplir está en docs/esquema.md, y la plantilla contra la que revisan
está en kb/virus/_template.yaml.
"""

from __future__ import annotations

from pathlib import Path

NOT_IMPLEMENTED = (
    "todavía no implementado: ver docs/backlog-de-issues.md, fase 1. "
    "El esquema está definido en docs/esquema.md."
)


def validate_tables(data_dir: Path) -> None:
    """Revisa measurements, assays y models contra docs/esquema.md.

    Revisiones previstas: que estén las columnas obligatorias, que los valores
    enumerados estén dentro del conjunto permitido, que toda clave foránea
    resuelva, y que cada fila cargue un source_doi y un source_location.
    """
    raise NotImplementedError(NOT_IMPLEMENTED)


def validate_kb(kb_dir: Path) -> None:
    """Revisa cada kb/virus/*.yaml contra la plantilla.

    Revisiones previstas: que todo campo con contenido biológico tenga un
    evidence_doi o esté en null, que todo null aparezca mencionado en
    open_questions, y que todo DOI esté bien formado sintácticamente.
    """
    raise NotImplementedError(NOT_IMPLEMENTED)


def main() -> int:
    """Punto de entrada del comando ovh-validate."""
    print(NOT_IMPLEMENTED)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
