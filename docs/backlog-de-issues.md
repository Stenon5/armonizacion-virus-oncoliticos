# Backlog de issues

Cada tarea de abajo está lista para abrirse como un issue de GitHub. El título,
la etiqueta y los criterios de aceptación están escritos, así que abrirlas es
mecánico.

La fase 3 es condicional y no se promete en ninguna parte.

## Fase 0, base de conocimiento

**[base] Elegir los cinco primeros virus y justificar la elección**
Etiqueta: `fase-0`
Se acepta cuando: una fila en `docs/registro-de-decisiones.md` nombra los cinco
virus y dice por qué cada uno está en el conjunto inicial, y la elección cubre
al menos dos genomas distintos.

**[base] Escribir las entradas de kb/virus/ para los virus elegidos**
Etiqueta: `fase-0`
Se acepta cuando: existe un archivo por virus, todo campo con contenido
biológico tiene un `evidence_doi` que resuelve, todo campo sin cita está en
`null` y aparece listado en `open_questions`, y cada archivo llegó en su propio
pull request.

**[base] Verificar que cada DOI de la base de conocimiento respalda la frase a la que está puesto**
Etiquetas: `fase-0`, `verificación`
Se acepta cuando: una persona abrió cada trabajo citado y confirmó que afirma
lo que se le atribuye, y queda registrada la proporción de campos con cita
verificada.

**[código] Implementar validate_kb**
Etiquetas: `fase-0`, `código`
Se acepta cuando: `ovh-validate` revisa cada archivo YAML contra la plantilla,
falla ante un campo con contenido y sin cita, y la prueba correspondiente en
`tests/test_schema.py` deja de estar omitida.

## Fase 1, armonización

**[extracción] Extraer a mano el primer artículo y sellarlo**
Etiquetas: `fase-1`, `referencia-manual`
Se acepta cuando: existen los archivos descritos en
`referencia-manual/README.md`, el tiempo ocupado queda registrado, y llegan en
un commit propio cuyo mensaje dice que la extracción está sellada.

**[extracción] Correr dos extracciones independientes del artículo sellado con agentes**
Etiquetas: `fase-1`, `agentes`
Se acepta cuando: las dos extracciones están commiteadas con
`extracted_by: agent`, el modelo y el prompt quedan registrados, y ninguna de
las dos tocó `referencia-manual/`.

**[análisis] Comparar las extracciones de los agentes contra el artículo sellado**
Etiquetas: `fase-1`, `agentes`
Se acepta cuando: la concordancia se reporta campo por campo, los desacuerdos
quedan listados con la forma en que se resolvió cada uno, y el conteo de
errores se reporta como un conteo con su denominador, nunca como un porcentaje
a secas.

**[extracción] Extraer el estudio NCI-60 de 2020**
Etiquetas: `fase-1`, `extracción`
Se acepta cuando: existen filas de ese artículo en las tres tablas y cada
juicio de criterio tiene una fila en `docs/registro-de-decisiones.md`.

**[extracción] Extraer el estudio de cultivos derivados de paciente de 2024**
Etiquetas: `fase-1`, `extracción`
Se acepta cuando: igual que arriba, más una nota sobre si `model_type` y los
campos existentes sobrevivieron a un estudio que no es un panel de líneas
celulares.

**[análisis] Resolver los nombres de los modelos contra Cellosaurus y contar el traslape**
Etiquetas: `fase-1`, `análisis`
Se acepta cuando: `cellosaurus_id` está rellenado donde existe uno, los nombres
que no se pueden resolver quedan listados con la razón, y se reporta la
cantidad de modelos compartidos entre los tres estudios. Un traslape chico o
igual a cero es un resultado publicable y se escribe como tal.

**[análisis] Medir la concordancia entre los dos tamizajes del NCI-60**
Etiquetas: `fase-1`, `análisis`
Depende de que estén extraídos los estudios de 2011 y 2020 y resueltos los
nombres de los modelos.

Pregunta: en los modelos que los dos estudios comparten, ¿ordenan igual su
permisividad? Los dos tamizan el mismo panel con el mismo género viral bajo
ensayos, multiplicidades de infección y tiempos distintos, así que esta es la
comparación que la armonización existe para poder hacer.

Qué se fija antes de correrlo, en `docs/preregistro.md`: qué estadístico de
concordancia se usa, cómo se tratan los valores de confianza baja y qué
resultado se consideraría acuerdo. Nada de eso se decide después de ver los
números.

Se acepta cuando: el conteo de modelos comparados queda escrito, el resultado
se reporta tal como salga, y se dice de forma explícita si sostiene o no
comparar permisividad entre estudios. Un desacuerdo es un resultado y se
escribe como tal, porque significa que las condiciones del ensayo pesan más
que el modelo.

**[código] Implementar validate_tables**
Etiquetas: `fase-1`, `código`
Se acepta cuando: se revisan las claves foráneas, los valores enumerados y las
columnas obligatorias, el comando falla ante una tabla rota, y las pruebas
correspondientes dejan de estar omitidas.

**[doc] Marcar cada falla predicha en el preregistro como ocurrida o no**
Etiquetas: `fase-1`, `preregistro`
Se acepta cuando: cada predicción numerada de `docs/preregistro.md` tiene una
fila en `docs/registro-de-decisiones.md` que dice qué pasó en realidad. El
archivo del preregistro no se edita.

**[doc] Escribir el informe de armonización**
Etiquetas: `fase-1`, `documentación`
Se acepta cuando: las métricas del README están rellenadas con la ejecución
real, y el informe dice con claridad qué comparaciones no sostiene el conjunto
de datos.

## Fase 2, publicación

**[publicación] Congelar la versión 0.1 del conjunto de datos**
Etiquetas: `fase-2`, `publicación`
Se acepta cuando: existe una versión etiquetada, las tablas validan, y las
notas de la versión listan las preguntas abiertas que siguen abiertas.

**[publicación] Decidir si vale la pena una versión archivada con DOI**
Etiquetas: `fase-2`, `publicación`
Se acepta cuando: la decisión queda registrada con su razón. Archivar es una
posibilidad, no un compromiso, y nada en este repositorio lo promete.

**[doc] Abrir BITACORA_DE_AGENTES.md para este repositorio**
Etiquetas: `fase-2`, `agentes`
Se acepta cuando: hay al menos una entrada real y fechada de este proyecto. El
archivo a propósito no se crea el primer día, porque un registro vacío es peor
que no tener registro.

## Fase 3, condicional

Solo si las fases 0 a 2 terminaron y el conteo de errores de los agentes
resultó aceptable. Nada de esto está prometido.

**[extracción] Extender a más artículos**
Etiqueta: `fase-3`
Se acepta cuando: el esquema absorbió los artículos nuevos sin un cambio que
rompa nada, o el cambio que rompe algo queda documentado.

**[código] Reimplementar con pruebas la firma publicada de genes estimulados por interferón**
Etiqueta: `fase-3`
Se acepta cuando: la implementación reproduce los números publicados sobre
datos públicos, o se reporta la diferencia. Condicionado a que los datos de
origen estén disponibles públicamente bajo una licencia que lo permita.

**[doc] Decidir si vale la pena escribir un preprint**
Etiqueta: `fase-3`
Se acepta cuando: la decisión y su razón quedan registradas.
