# Capas de evidencia

En qué se puede descomponer la pregunta de permisividad, y qué evidencia
publicada hay para cada capa. Este documento ordena la literatura y fija una
decisión de diseño. No es un método de puntuación, y no se usa para elegir
tratamientos, ver "Lo que esto NO es" en el [README](../README.md).

Los campos biológicos que aparecen aquí van a `kb/virus/` en la fase 0, y la
regla del repositorio es que cada uno llega con su propia cita. Los que todavía
no la tienen quedan marcados abajo.

## Las capas

| Capa | Pregunta | Qué dato hace falta | Madurez |
|---|---|---|---|
| 1. Entrada | ¿Expresa el tumor el receptor que usa este virus? | Expresión, RNA-seq o inmunohistoquímica | Lectura directa, pero ver la advertencia de más abajo |
| 2. Estado antiviral | ¿Está activa la vía de interferón tipo I? | RNA-seq, firma de genes estimulados por interferón | La de mejor evidencia |
| 3. Replicación | ¿Están alteradas las vías que el virus explota? | Panel mutacional o exoma | Media |
| 4. Inmunidad previa | ¿Hay anticuerpos neutralizantes contra ese virus? | Suero, no biopsia | Buen dato, pero ajeno al tumor |
| 5. Microambiente | ¿Cómo está el infiltrado inmune? | Deconvolución del RNA-seq | Media |

Los receptores de entrada de cada virus (por ejemplo CD46, nectina-4 y SLAM para
sarampión, LDLR para estomatitis vesicular, CAR para adenovirus y nectina-1 para
herpes simple) son anotación de la fase 0 y **todavía no están citados en este
repositorio**. Cada uno entra a `kb/virus/` con su DOI o se queda en `null`.

## La capa 2 es la que tiene evidencia

Kurokawa et al. construyeron un clasificador por análisis discriminante lineal
diagonal (DLDA) a partir de RNA-seq, comparando xenoinjertos de glioblastoma
derivados de paciente resistentes (n = 3) y permisivos (n = 2) al virus de
sarampión. Lo validaron en más xenoinjertos de glioblastoma y de cáncer de
ovario, y en 10 pacientes de glioblastoma de un ensayo fase I. En los tumores de
paciente, la replicación viral correlacionó de forma inversa con la firma de
resistencia, con rho igual a -0,717 y P igual a 0,03. El inhibidor de JAK
ruxolitinib aumentó la producción de virus unas 1000 veces, con P igual a 0,03.

* Kurokawa C, Iankov ID, Anderson SK, Aderca I, Leontovich AA, Maurer MJ,
  Oberg AL, Schroeder MA, Giannini C, Greiner SM, Becker MA, Thompson EA,
  Haluska P, Jentoft ME, Parney IF, Weroha SJ, Jen J, Sarkaria JN, Galanis E.
  *Constitutive Interferon Pathway Activation in Tumors as an Efficacy
  Determinant Following Oncolytic Virotherapy.* J Natl Cancer Inst 2018,
  110(10):1123-1132. DOI
  [10.1093/jnci/djy033](https://doi.org/10.1093/jnci/djy033), PMID 29788332,
  PMCID PMC6186520.

Cifras verificadas contra el resumen en PubMed el 2026-10-23. **Por verificar en
el texto completo:** cuántos genes tiene la firma y cuántos xenoinjertos se
usaron en la validación. El resumen no da esos números, así que este
repositorio no los afirma.

## Por qué la salida nunca puede ser un solo número

El tamizaje de Schäfer et al. en 14 cultivos de cáncer de páncreas derivados de
paciente, con cinco virus oncolíticos de relevancia clínica, encontró que 12 de
los 14 cultivos respondieron a por lo menos un virus y que **ningún virus
resultó superior ni inferior en todos los cultivos.** Además la expresión de los
receptores de entrada en general no correlacionó con la sensibilidad, con una
excepción, y la expresión alta de genes estimulados por interferón correlacionó
con resistencia relativa al sarampión oncolítico. Los autores concluyen que
ningún biomarcador por sí solo explica el espectro de respuestas.

Cita completa en [`fuentes.md`](fuentes.md), estudio 3. Verificado contra el
resumen en PubMed el 2026-10-23.

Eso tiene dos consecuencias de diseño que el repositorio ya adoptó:

1. No existe un ranking universal de virus. Solo rankings condicionados a un
   perfil, y la capa 1 por sí sola no basta para construirlos.
2. La salida se entrega por capas, cada una con su nivel de evidencia, y nunca
   colapsada en un puntaje único.

## Propuesta de Claude, no adoptada

Las fases posteriores que aparecían en el repositorio privado del que viene este
documento, que eran reimplementar el clasificador DLDA como paquete instalable y
construir un motor de puntuación multicapa, quedan **fuera del alcance** y se
anotan solo como contexto. Sin datos armonizados no hay con qué validarlas.
