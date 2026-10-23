---
name: Extracción de datos
about: Extraer valores de un artículo hacia las tablas armonizadas
title: "[extracción] "
labels: ["fase-1", "extracción"]
---

**Artículo**
DOI y título.

**Qué se está extrayendo**
Qué tabla o figura, y qué campos del esquema.

**Quién o qué lo extrae**
Una persona, o un agente con el modelo y el prompt registrados.

**Criterios de aceptación**
- [ ] Cada fila tiene `source_doi` y `source_location`.
- [ ] Cada fila tiene un valor de `confidence`, bajo para todo lo que se haya leído de una figura.
- [ ] `read_method` dice tabla, texto, o qué herramienta digitalizó la figura.
- [ ] Los valores que el artículo no declara quedan vacíos, no adivinados.
- [ ] No se commitea ningún PDF, figura ni tabla suplementaria completa.
- [ ] Todo juicio de criterio nuevo tiene una fila en `docs/registro-de-decisiones.md`.
