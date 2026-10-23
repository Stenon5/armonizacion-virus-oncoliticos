# Esquema de armonización

Documento de trabajo para la fase 1. Se escribe **mientras** se armonizan los
tres artículos iniciales, no antes. La versión que está en este commit es la
propuesta de partida, todavía sin datos que la respalden.

## Por qué existe este documento

Dos tamizajes del mismo panel de líneas celulares con el mismo género viral no
son comparables sin más. Los ensayos difieren, la multiplicidad de infección
difiere, los tiempos de medición difieren y la métrica reportada difiere. El
esquema tiene que registrar esas diferencias en lugar de esconderlas, porque
esconderlas es lo que vuelve inútil un conjunto de datos agregado.

Todo lo que viene abajo es una propuesta hasta que el primer artículo esté
realmente extraído. Un campo que resulte imposible de rellenar se elimina y la
eliminación queda registrada en `registro-de-decisiones.md`.

## Tablas

Las tablas viven en `data/harmonized/` como CSV, para que un diff de git siga
siendo legible. Más adelante se puede agregar una exportación a Parquet para
consumirla. En este commit los archivos tienen solo los encabezados.

### `measurements.csv`

Una fila por medición de un virus en un modelo.

| Campo | Tipo | Notas |
|---|---|---|
| `measurement_id` | str | Clave |
| `assay_id` | str | Clave foránea hacia `assays.csv` |
| `virus_id` | str | Clave foránea hacia `kb/virus/` |
| `model_id` | str | Clave foránea hacia `models.csv` |
| `value` | float | En la unidad del ensayo |
| `value_unit` | str | Por ejemplo fracción de viabilidad, o log10 PFU/mL |
| `value_type` | enum | `continuous` o `category` |
| `direction` | enum | `higher_is_more_permissive` o `lower_is_more_permissive`. Sin este campo las métricas no se pueden comparar de ninguna forma |
| `confidence` | enum | `high`, `medium`, `low`. Baja cuando el valor se leyó de una figura en vez de una tabla |
| `read_method` | str | `table`, `text`, o la herramienta con que se digitalizó una figura |
| `source_doi` | str | |
| `source_location` | str | Por ejemplo `Table S3` o `Figure 2B` |
| `extracted_by` | enum | `human` o `agent` |
| `notes` | str | Texto libre, breve |

### `assays.csv`

Una fila por condición experimental. Esta es la tabla que decide si el
proyecto funciona.

| Campo | Notas |
|---|---|
| `assay_id` | Clave |
| `source_doi` | El artículo del que viene la condición |
| `readout` | Viabilidad (MTT, cristal violeta), título viral, citometría de flujo, imágenes |
| `moi` | Multiplicidad de infección, tal como se reporta |
| `moi_basis` | Contra qué se calculó la MOI, cuando el artículo lo dice |
| `timepoint_h` | Horas post infección |
| `replicates` | |
| `normalization` | Contra qué se normalizó el valor |
| `media_serum` | Condiciones de cultivo, cuando se reportan |
| `comparable_group` | Identificador que comparten las condiciones que se juzgan comparables. Se asigna a mano, con la razón en `registro-de-decisiones.md` |

### `models.csv`

| Campo | Notas |
|---|---|
| `model_id` | Clave |
| `model_type` | `cell_line`, `pdx`, `organoid`, `patient` |
| `name_as_published` | El nombre tal como está impreso en el artículo |
| `cellosaurus_id` | Identificador canónico cuando existe |
| `tissue` | |
| `depmap_id` | Puente hacia perfiles públicos de expresión, cuando existe |
| `name_resolution_note` | Cómo se resolvió un nombre ambiguo |

### Anotación de los virus

Los virus no son una tabla CSV. Viven como un archivo YAML por virus en
`kb/virus/`, porque el contenido es anotación curada con una cita por campo, y
eso se revisa mejor como YAML en un pull request. La plantilla es
`kb/virus/_template.yaml`.

## Preguntas abiertas, fase 1

Estas las responde el intento de armonizar los tres artículos, no antes.

1. ¿Pueden convivir la viabilidad y el título viral en la misma tabla, o
   necesitan tablas separadas?
2. Cuando un artículo reporta solo una categoría (susceptibilidad alta, media,
   baja) y otro reporta un valor continuo, ¿se guarda el valor continuo y se
   deriva la categoría, o se guardan los dos?
3. ¿Qué pasa con los valores leídos de una figura? Propuesta: aceptarlos con
   `confidence: low` y registrar la herramienta en `read_method`.
4. ¿Cuántos modelos se comparten de verdad entre los tres artículos después de
   resolver los nombres? Si son muy pocos, el conjunto de datos no sostiene la
   comparación entre estudios, y eso ya es un resultado que vale la pena
   reportar.
5. ¿Cuántos modelos tienen un perfil público de expresión? Sin expresión no hay
   capa de interferón.
6. ¿`comparable_group` se puede defender siquiera, o cada artículo termina solo
   en su propio grupo?

## Decisiones

Cada decisión de armonización queda registrada en
[`registro-de-decisiones.md`](registro-de-decisiones.md) con una fecha y una
razón. Una decisión que después resulta equivocada se queda en el registro y se
corrige más abajo. No se borra.
