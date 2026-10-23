# Referencia manual

Un artículo, extraído completo a mano, sellado en un commit antes de que corra
cualquier agente. Todo lo que produzca un agente más adelante se mide contra lo
que hay en esta carpeta. A esta referencia también se le llama "estándar de oro".

**Estado: vacía. La extracción a mano todavía no se ha hecho.**

## Por qué existe

La tasa de error de un agente no se puede medir contra la salida de otro
agente, y tampoco se puede medir contra una referencia que se armó después de
ver la respuesta del agente. La referencia tiene que existir primero y tiene
que quedar fija, porque si no, cada desacuerdo se resuelve hacia el lado que
resulte más conveniente.

## Protocolo

1. **Elegir el artículo.** El estudio NCI-60 de 2011 es el candidato, porque es
   el más grande de los tres y tiene más metadatos de ensayo que se pueden
   equivocar. La elección queda registrada en
   `docs/registro-de-decisiones.md` cuando se tome.
2. **Extraer a mano.** Cada campo del esquema, para cada medición, leído del
   artículo y de su material suplementario por una persona. El tiempo ocupado
   queda registrado, porque es el denominador de cualquier afirmación sobre
   ahorro de tiempo.
3. **Registrar la ubicación.** Cada valor carga su `source_location`, por
   ejemplo `Table S3, row 12`. Un valor cuya ubicación no se puede declarar no
   entra.
4. **Marcar lo que no se pudo leer.** Un campo que el artículo no declara queda
   vacío con una nota. No se adivina, y no se rellena desde otro artículo.
5. **Sellarlo.** Los archivos se commitean solos, con un mensaje de commit que
   dice que la extracción está sellada y nombra el artículo. Ningún commit
   posterior edita estos archivos.
6. **Solo entonces correr agentes.** Las extracciones del mismo artículo hechas
   por agentes van a `data/harmonized/` con `extracted_by: agent`, nunca a esta
   carpeta.
7. **Comparar.** Concordancia campo por campo, la lista de desacuerdos, y el
   conteo bruto de errores de los agentes contra esta carpeta, con el
   denominador declarado.

## Si la extracción sellada resulta estar equivocada

Se queda. La corrección va a un archivo nuevo en esta carpeta llamado
`correcciones-<fecha>.md`, que dice qué valor estaba mal, cuál es el valor
correcto, y cómo se encontró el error. El archivo original no se edita, porque
la comparación con los agentes que ya lo usó tiene que seguir siendo
interpretable.

## Archivos que van a vivir aquí

```
referencia-manual/
  README.md                este archivo
  <clave-del-articulo>/
    measurements.csv       extraído a mano, sellado
    assays.csv             extraído a mano, sellado
    models.csv             extraído a mano, sellado
    notas-de-extraccion.md tiempo ocupado, qué no se pudo leer, juicios de criterio
```
