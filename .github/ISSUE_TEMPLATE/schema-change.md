---
name: Cambio en el esquema
about: Agregar, quitar o redefinir un campo del esquema de armonización
title: "[esquema] "
labels: ["esquema"]
---

**Campo**
Tabla y nombre del campo.

**Qué se rompe sin el cambio**
Nombra el artículo y el valor que hoy no se puede registrar bien.

**Definición propuesta**
Tipo, valores permitidos, y si es obligatorio.

**Criterios de aceptación**
- [ ] `docs/esquema.md` actualizado.
- [ ] Una fila agregada a `docs/registro-de-decisiones.md` con la fecha y la razón.
- [ ] Los encabezados de los CSV en `data/harmonized/` actualizados.
- [ ] La prueba de encabezados en `tests/test_schema.py` actualizada.
- [ ] Las filas ya extraídas quedan migradas o listadas como pendientes de migración.
