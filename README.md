# armonizacion-virus-oncoliticos

Un intento documentado de poner los resultados de tamizaje de virus oncolíticos
publicados en estudios preclínicos dentro de un solo esquema, para que las
mediciones de estudios distintos se puedan comparar o quede demostrado que no
son comparables.

**Estado: andamiaje. Todavía no se ha extraído ningún dato.** Están el esquema,
las plantillas y las tablas vacías. Las tablas de `data/harmonized/` tienen
solo los encabezados. Nada en este repositorio ha sido medido, puntuado ni
sometido a un benchmark.

## La pregunta

Dos tamizajes del mismo panel de líneas celulares con el mismo género viral
pueden diferir en el ensayo, la multiplicidad de infección, el tiempo de
medición y la métrica. ¿Se pueden poner esos resultados en una sola tabla sin
esconder las diferencias que los hacen incomparables, y cuántos modelos se
comparten de verdad una vez que se resuelven los nombres?

## Por qué importa

Los tamizajes publicados son una fuente práctica de datos de permisividad para
cualquiera que no tenga laboratorio. Si no se pueden comparar, entonces
afirmar que un virus es mejor que otro entre estudios se apoya en una
comparación que nadie ha revisado. Averiguar dónde exactamente se rompe la
comparación es el resultado útil, salga o no una tabla aprovechable de todo
esto.

Ya existe un catálogo de esta literatura, OvirusTdb
(grupo Raghava, IIIT-Delhi, <https://webs.iiitd.edu.in/raghava/ovirustdb/>).
Responde qué se ha probado. No responde si dos números reportados significan
lo mismo.

## Lo que esto NO es

* **No es un selector de tratamiento.** No sirve para elegir una terapia para
  un paciente.
* **No es apoyo a la decisión clínica.**
* **No es una guía para autoadministrarse ningún virus.** Nada de lo que hay
  aquí describe cómo conseguir, manipular o administrar un virus a una persona
  o a un animal.
* **No contiene protocolos de laboratorio.** Este repositorio guarda datos
  sobre experimentos publicados, no instrucciones para hacerlos.
* **Nada de lo que hay aquí es clínicamente aplicable.** Los estudios de base
  trabajan con pocos modelos, y el trabajo con organoides en este campo corre
  con números de pacientes de un dígito o de dos dígitos bajos.

## Alcance del trabajo público

Solo fase 0 y fase 1.

| Fase | Entregable | En este repositorio |
|---|---|---|
| 0 | Una base de conocimiento versionada, un archivo YAML por virus, con cada campo biológico cargando su propia cita | solo la plantilla, todavía sin archivos de virus |
| 1 | Armonización de tres estudios publicados en un solo esquema, con metadatos del ensayo y una etiqueta de confianza por valor | el esquema y las tablas vacías |

Un motor de puntuación y un benchmark quedan fuera del alcance hasta que haya
datos contra los que validarlos. Empezar por el motor produce algo que no
tiene con qué ponerse a prueba.

## Fuentes

Tres estudios abren la fase 1. Sus identificadores, sus licencias y la razón
por la que se eligió cada uno están en [`docs/fuentes.md`](docs/fuentes.md).
Aquí no se redistribuye ningún PDF ni ninguna figura de esos artículos. Solo
los valores extraídos, su cita y su ubicación dentro del artículo.

## Decisión de diseño que no cambia

La salida nunca se reduce a un solo número. Cada virus devuelve capas
separadas, cada una con su propio nivel de evidencia:

1. ensayo clínico
2. organoide derivado de paciente
3. línea celular
4. solo razonamiento mecanístico

Un ranking que mezcla evidencia clínica con inferencia basada en expresión y
emite un único puntaje es desinformación bien formateada.

## Distribución del repositorio

```
kb/virus/              un archivo YAML por virus (fase 0)
data/harmonized/       tablas CSV relacionadas (fase 1), por ahora solo encabezados
referencia-manual/     un artículo extraído a mano, sellado antes de que corran los agentes
docs/esquema.md        definiciones de las tablas y las preguntas abiertas
docs/preregistro.md    fallas esperadas, escritas antes de la extracción
docs/registro-de-decisiones.md  cada decisión de armonización, con fecha y razón
docs/fuentes.md        los tres estudios, con DOI y licencia
docs/backlog-de-issues.md  la lista de tareas, lista para abrirse como issues
src/ovh/               paquete (esqueleto)
tests/                 pruebas (omitidas hasta que exista el código)
```

## Cómo queda fijado el orden del trabajo

Primero se extrae un artículo a mano y se sella en un commit antes de que corra
cualquier agente. Después la salida de los agentes se compara contra esa
extracción sellada. El protocolo está en
[`referencia-manual/README.md`](referencia-manual/README.md). Las fallas que se
espera que el esquema encuentre quedan escritas antes de que empiece la
extracción, en [`docs/preregistro.md`](docs/preregistro.md), para que una falla
no pueda reinterpretarse después como un éxito.

## Métricas que este proyecto va a reportar

Conteos y tasas, definidos ahora y rellenados más adelante con la ejecución
real.

* Cantidad de artículos, ensayos, modelos y mediciones. `(rellenar desde la ejecución)`
* Proporción de valores por nivel de confianza. `(rellenar desde la ejecución)`
* Modelos compartidos entre los tres estudios después de resolver los nombres. `(rellenar desde la ejecución)`
* Concordancia campo por campo entre dos extracciones independientes hechas por
  agentes, y cuántos desacuerdos tuvo que arbitrar una persona. `(rellenar desde la ejecución)`
* Conteo bruto de errores contra el artículo extraído a mano, no un porcentaje.
  `(rellenar desde la ejecución)`
* Minutos por artículo, con ayuda de agentes contra a mano. `(rellenar desde la ejecución)`

## Instalación

```
python -m pip install -e .
pytest
```

Por ahora las pruebas se omiten con una razón explícita, porque el código que
describen todavía no está escrito.

## Cómo contribuir

Los issues y los pull requests son bienvenidos, en español o en inglés.

* Un virus por pull request para `kb/virus/`. Todo campo con contenido
  biológico necesita su propio DOI. Un campo sin cita se queda en `null` y pasa
  a `open_questions`.
* Los cambios al esquema pasan primero por un issue, y llegan junto con una
  fila en `docs/registro-de-decisiones.md`.
* Los valores leídos de una figura se aceptan con confianza baja y tienen que
  decir con qué herramienta se leyeron.
* No agregues PDF, figuras ni tablas suplementarias completas de artículos de
  terceros. Agrega valores con su cita y su ubicación.

## Licencia

El código es MIT, ver [`LICENSE`](LICENSE). Los datos, los documentos del
esquema y la prosa son CC BY 4.0, ver
[`LICENCIA-DATOS.md`](LICENCIA-DATOS.md).

## Cómo citar

Ver [`CITATION.cff`](CITATION.cff). Una versión archivada y citable es una
posibilidad cuando haya datos, no un compromiso.
