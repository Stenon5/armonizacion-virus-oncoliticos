---
name: Entrada en la base de conocimiento de virus
about: Agregar o revisar un archivo de virus en kb/virus/
title: "[base] "
labels: ["fase-0", "base-de-conocimiento"]
---

**Virus**
Especie y cepa.

**Criterios de aceptación**
- [ ] El archivo sigue `kb/virus/_template.yaml`.
- [ ] Todo campo con contenido biológico tiene su propio `evidence_doi`.
- [ ] Todo DOI resuelve y el trabajo citado respalda de verdad lo que se afirma.
- [ ] Los campos sin cita están en `null` y aparecen en `open_questions`.
- [ ] `curation.extracted_by` y `curation.reviewed_by_human` están rellenados.
- [ ] Un virus por pull request.
