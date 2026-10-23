# Escenarios de recursos

Hasta dónde puede llegar este proyecto según el acceso que tenga. Está escrito
para que el alcance declarado no dependa del entusiasmo del momento, y para que
quien lea el repositorio sepa en qué nivel está hoy.

## Los tres niveles

| Nivel | Qué desbloquea | Techo de lo que se puede publicar |
|---|---|---|
| A. Solo datos públicos, **el nivel actual** | Suplementarios de artículos publicados, y perfiles públicos de expresión como CCLE o DepMap, GEO y ArrayExpress | Un paquete y un dataset armonizado, citables con DOI |
| B. Acceso institucional o colaboración clínica | Repositorios de acceso controlado, cómputo universitario, y el criterio de un patólogo o un oncólogo sobre qué comparación tiene sentido | Lo anterior, más un caso de uso real revisado por alguien del área |
| C. Validación experimental | Cerrar el ciclo de predecir, medir y corregir | Un informe de validación prospectiva |

## Por qué el nivel C no es para entrenar nada

Un experimento al alcance de un estudiante produce del orden de diez
mediciones. Diez puntos no entrenan un modelo.

Para lo que sí sirven es para validación prospectiva: registrar las
predicciones antes de medir, medir después, y reportar los aciertos y los
errores tal como salgan. Diez predicciones registradas de antemano dicen más
que doscientas comparaciones hechas después de conocer el resultado. Es la
misma lógica que ya usa el repositorio en
[`preregistro.md`](preregistro.md).

## Por qué el nivel C queda fuera de alcance

No por falta de interés. Porque trabajar con virus en laboratorio exige
respaldo que este proyecto no tiene:

* Un laboratorio institucional con supervisión.
* Las autorizaciones sanitarias que correspondan en el país donde se trabaje.
  En Chile eso pasa por el Instituto de Salud Pública.
* La aprobación del comité de bioseguridad de la universidad.

Mientras no exista ese respaldo, el repositorio se queda en el nivel A, que es
donde está, y en las fases 0 y 1 que declara el [README](../README.md). Nada en
este repositorio describe cómo conseguir, manipular o administrar un virus.

## Qué cambiaría al subir de nivel

Pasar de nivel no cambia el esquema ni las reglas de citación. Cambia qué
preguntas se pueden responder, y por eso cada nivel declara su techo antes de
empezar, en vez de ajustarlo después según lo que haya salido.
