# Registro de decisiones

Cada decisión de armonización va aquí con una fecha y una razón. Una decisión
que después resulta equivocada se queda escrita y se corrige en una fila nueva
más abajo. Las filas nunca se borran.

Todavía no se ha extraído ningún valor, así que las filas de más abajo son
decisiones de alcance y de citas, no de armonización de datos.

## Decisiones

| Fecha | Decisión | Razón | Afecta |
|---|---|---|---|
| 2026-10-23 | Se trae a este repositorio el encuadre y las capas de evidencia que estaban en un repositorio privado anterior, y se dejan fuera su motor de puntuación y la reimplementación del clasificador | Las dos líneas de trabajo apuntan a la misma pregunta, y mantenerlas separadas duplicaba el tema. El motor sigue fuera de alcance porque no hay datos con los que validarlo | `README.md`, `docs/origen-de-la-pregunta.md`, `docs/capas-de-evidencia.md` |
| 2026-10-23 | No se traen cuatro cifras que venían de ese repositorio privado: el tamaño de la firma de genes, el número de xenoinjertos de validación, un coeficiente de correlación atribuido a un solo gen y los conteos de OvirusTdb | Al contrastarlas contra los resúmenes en PubMed no aparecieron, y el sitio de OvirusTdb no respondió. Una cifra sin fuente verificada no entra a un repositorio público | `docs/capas-de-evidencia.md`, `docs/fuentes.md` |

## Reversiones

| Fecha | Fila revertida | Qué la reemplazó | Por qué la primera estaba mal |
|---|---|---|---|
| | | | |

## Preguntas abiertas que vienen del esquema

Estas quedan abiertas hasta que la extracción las responda. Cada una recibe una
fila más arriba cuando se cierra.

1. ¿Pueden convivir la viabilidad y el título viral en la misma tabla, o
   necesitan tablas separadas?
2. Cuando un artículo reporta una categoría y otro un valor continuo, ¿se
   guarda el valor continuo y se deriva la categoría, o se guardan los dos?
3. ¿Qué se hace con los valores leídos de una figura, más allá de marcarlos con
   confianza baja?
4. ¿Cuántos modelos se comparten entre los tres artículos después de resolver
   los nombres?
5. ¿Cuántos modelos tienen un perfil público de expresión?
6. ¿`comparable_group` se puede defender, o cada artículo termina solo en su
   propio grupo?
7. ¿Alcanza con un archivo YAML por especie de virus, o cada cepa modificada
   necesita el suyo?

## Cómo agregar una fila

Una decisión por fila. La decisión es lo que se hizo, no lo que se consideró.
La razón dice qué habría salido mal de otra forma. `Afecta` nombra los archivos
o campos que cambian por esa decisión.
