# Registro de decisiones

Cada decisión de armonización va aquí con una fecha y una razón. Una decisión
que después resulta equivocada se queda escrita y se corrige en una fila nueva
más abajo. Las filas nunca se borran.

La tabla está vacía porque todavía no se ha extraído ningún valor.

## Decisiones

| Fecha | Decisión | Razón | Afecta |
|---|---|---|---|
| | | | |

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
