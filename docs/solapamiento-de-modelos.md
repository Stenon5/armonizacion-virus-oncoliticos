# Cuántos modelos comparten los tres estudios

Conteo preliminar del 23 de octubre de 2026, hecho antes de extraer los datos,
para saber si una comparación entre estudios es posible. Es la pregunta 4 de
las preguntas abiertas de [`esquema.md`](esquema.md).

**Resultado corto.** Los dos estudios del panel NCI-60 comparten al menos 45
modelos. El estudio de 2024 comparte 0 con ellos, porque usa cultivos de
pacientes con su propia nomenclatura. Una comparación entre los tres a nivel de
modelo no es posible, y eso es en sí un resultado.

## Conteo

| Estudio | Modelos con medición reportada | Tipo |
| --- | --- | --- |
| Ascierto 2011 | 74 entradas, 69 líneas si se juntan los pasajes repetidos | Líneas establecidas |
| Berchtold 2020 | 54 | Líneas establecidas del NCI-60, sin las 6 de leucemia |
| Schäfer 2024 | 14 cultivos de paciente, más 4 especímenes quirúrgicos | Cultivos derivados de paciente |

| Par | Coinciden por nombre | Nota |
| --- | --- | --- |
| 2011 y 2020 | 45 de 54 | Coincidencia exacta tras quitar mayúsculas, guiones y espacios |
| 2011 y 2024 | 0 | |
| 2020 y 2024 | 0 | |

Las 9 líneas de 2020 sin pareja exacta en 2011 son A549, CAKI1, HT29, IGR-OV1,
MALME-3M, MDA-MB-468, OVCAR-3, PC-3 y SK-OV-1. Casi todas existen en 2011 con
otra grafía, por ejemplo `HT29 p6` y `HT29 p155`, `PC3 p7`, `Caki I` o
`A549 p4`. Son nombres que incluyen el número de pasaje o que separan distinto
las palabras. Resolverlos a mano con Cellosaurus debería subir el conteo por
encima de 45, así que 45 es un piso y no el número final.

## Qué significa para el proyecto

1. **La comparación entre 2011 y 2020 sí es posible a nivel de modelo.** Ambos
   usan el mismo panel y el mismo género viral, que es justo el caso que el
   esquema tiene que soportar.
2. **El estudio de 2024 no entra en esa comparación.** Usa modelos distintos,
   varios virus y otra métrica. Sirve para probar si el esquema soporta otro
   tipo de modelo, no para comparar valores con los otros dos.
3. **La resolución de nombres no es un detalle.** Con coincidencia exacta se
   pierden 9 de 54 modelos, un 17 %. Un dataset que una los estudios sin
   resolver los nombres subestima el solapamiento.
4. **El número de pasaje viaja en el nombre.** El esquema necesita un campo
   para eso, o la misma línea aparece como modelos distintos. Está anotado en
   [`registro-de-decisiones.md`](registro-de-decisiones.md).

## Cómo se hizo y qué le falta

Los nombres de 2020 y 2024 salen de un agente que leyó el texto completo en XML
de Europe PMC. Los de 2011 vienen de un borrador de extracción que todavía no
ha sido verificado por una persona.

Lo que falta para que este conteo sea definitivo:

* Verificar las etiquetas de 2020, porque el agente las leyó de una imagen de
  figura y dudó de varias (`SK-OV-1` parece `SK-OV-3`, `IGR-OV1` parece
  `IGROV1`, `HS-578T` parece `Hs 578T`).
* Resolver los nombres contra Cellosaurus, que es la tarea
  [`[análisis] Resolver los nombres de los modelos contra Cellosaurus`](../docs/backlog-de-issues.md).
* Decidir si los 4 especímenes quirúrgicos de 2024 cuentan como modelos.
