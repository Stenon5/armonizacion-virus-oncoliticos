# Preregistro

Escrito el 2026-10-22, antes de extraer ningún valor. Nada de este archivo se
puede editar una vez que empieza la extracción. Los cambios van a un archivo
nuevo llamado `preregistro-enmienda-<fecha>.md` que dice qué cambió y por qué.

El propósito de este archivo es simple. Se espera que el esquema falle de
maneras específicas. Si esas fallas quedan escritas primero, una falla sigue
siendo una falla y no se puede recategorizar después como un hallazgo.

## Qué cuenta como éxito

El éxito no es una tabla completa. El éxito es una respuesta defendible a esta
pregunta: ¿se pueden comparar las mediciones de estos tres artículos y, si no,
qué campo exactamente las vuelve incomparables?

Los dos resultados que vienen son aceptables y los dos se publican:

* Una tabla armonizada más una lista explícita de las comparaciones que no
  sostiene.
* Una demostración documentada de que la comparación no es posible, nombrando
  los campos que la rompen.

## Fallas esperadas del esquema

Cada una es una predicción. Después de la extracción, cada una queda marcada
como ocurrió, no ocurrió, u ocurrió de otra forma, en
`registro-de-decisiones.md`.

1. **Incompatibilidad entre ensayos.** La viabilidad y el título viral no van a
   caber en una sola columna `value` de ninguna manera que permita compararlos.
   Efecto esperado: `direction` y `value_unit` los mantienen separables, pero
   no hay ninguna comparación posible entre métricas.
2. **La MOI no es un solo número.** Al menos un artículo va a reportar la MOI
   de una forma que no es directamente comparable con las otras, por ejemplo
   calculada contra otra base o dada como un rango. `moi` por sí solo no va a
   alcanzar.
3. **Los tiempos de medición no van a coincidir.** Los tiempos elegidos van a
   diferir lo suficiente para que `timepoint_h` no se pueda emparejar exacto
   entre artículos, solo agrupar en rangos, y agruparlos va a ser un juicio de
   criterio.
4. **Categoría contra continuo.** Al menos un artículo reporta una categoría de
   susceptibilidad y otro un valor continuo. Derivar la categoría del continuo
   va a exigir un umbral que los autores originales no usaron.
5. **Pocos modelos compartidos.** Después de resolver los nombres, la cantidad
   de modelos compartidos por los tres artículos va a ser chica. El tercer
   artículo usa cultivos derivados de paciente, así que la intersección con el
   panel de líneas celulares puede ser cero.
6. **Los nombres no se van a resolver limpio.** Algunos nombres de líneas
   celulares publicados van a corresponder a más de una entrada de Cellosaurus,
   o a ninguna.
7. **Valores que solo están en figuras.** Algunos valores existen solo dentro de
   una figura. Van a entrar con confianza baja, y la dispersión de los valores
   digitalizados va a ser más ancha que la precisión que el artículo sugiere.
8. **`comparable_group` puede quedar inservible.** El campo puede terminar con
   un grupo por artículo, lo que significaría que no carga ninguna información.
9. **La normalización muchas veces no se declara.** `normalization` va a quedar
   vacío en una proporción importante de las filas.
10. **El virus no es un solo objeto.** Las cepas modificadas de la misma
    especie difieren en cosas que importan, así que puede hacer falta un
    archivo YAML por cepa en vez de uno por especie.

## Modos de falla esperados de los agentes

Escritos antes de que corra cualquier agente, por la misma razón.

1. Dos agentes independientes van a coincidir en los campos fáciles (nombre del
   modelo, nombre del virus) y a discrepar en los metadatos del ensayo, que es
   donde vive realmente la armonización.
2. Un agente va a reportar con confianza alta un valor que venía de una figura.
3. Un agente va a normalizar una unidad en silencio, por ejemplo convirtiendo
   un porcentaje en una fracción, sin decir que lo hizo.
4. Un agente va a rellenar un campo que el artículo no declara, usando un valor
   por defecto plausible.
5. Un agente va a citar el DOI correcto y la tabla equivocada.

## Cómo se mide la calidad de los agentes

Decidido ahora, para que la métrica no se pueda elegir después de ver los
números.

* **Concordancia.** Concordancia campo por campo entre dos extracciones
  independientes del mismo artículo, reportada por campo, no como un solo
  número global.
* **Arbitraje.** Conteo de los desacuerdos que tuvo que resolver una persona, y
  cómo se resolvió cada uno.
* **Errores.** Conteo bruto de valores equivocados contra el artículo extraído a
  mano, como un conteo con el denominador declarado, nunca como un porcentaje a
  secas.
* **Tiempo.** Minutos por artículo, con ayuda de agentes contra a mano, medidos
  sobre el mismo artículo.

Un artículo con pocos campos hace que cualquier porcentaje se vea impresionante.
Por eso la métrica de error es un conteo.

## Regla de detención

Si la extracción a mano y la extracción por agente del primer artículo
discrepan en más de un puñado de campos, la extracción de los artículos
restantes se detiene hasta que la causa quede escrita en
`registro-de-decisiones.md`. Escalar un proceso roto a tres artículos solo
produce tres extracciones rotas.
