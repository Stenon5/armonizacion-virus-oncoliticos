# De dónde sale esta pregunta

Este documento explica por qué existe el repositorio. No contiene datos ni
métodos. Los límites de uso están en la sección "Lo que esto NO es" del
[README](../README.md) y valen también para lo que se dice aquí.

## El caso publicado que motivó la pregunta

En 2024 se publicó el reporte de un caso único: una viróloga de 50 años con
cáncer de mama recurrente localmente invasivo que se aplicó, por su cuenta y en
su propio laboratorio, inyecciones intratumorales de preparaciones de grado de
investigación. Primero una cepa vacunal de sarampión Edmonston-Zagreb y después
un virus de la estomatitis vesicular, cepa Indiana. Dos meses después el tumor
se extirpó con cirugía simple, el tejido extirpado mostró infiltración
linfocitaria, y la paciente completó un año de trastuzumab adyuvante y seguía
sin recurrencia 45 meses después de la cirugía.

* Forčić D, Mršić K, Perić-Balja M, Kurtović T, Ramić S, Silovski T,
  Pedišić I, Milas I, Halassy B. *An Unconventional Case Study of Neoadjuvant
  Oncolytic Virotherapy for Recurrent Breast Cancer.* Vaccines 2024, 12(9):958.
  DOI [10.3390/vaccines12090958](https://doi.org/10.3390/vaccines12090958),
  PMID 39339989, PMCID PMC11435696.
* Los propios autores lo describen como un caso aislado, y lo presentan como
  motivo para considerar la viroterapia oncolítica como tratamiento
  neoadyuvante, no como evidencia de eficacia.

Metadatos y resumen leídos del registro de PubMed el 2026-10-23.

## Qué problema de investigación deja a la vista

Ese caso lo hizo posible una persona con laboratorio propio, formación en
virología y capacidad para preparar y caracterizar los virus ella misma. Nada
de eso es replicable para un equipo que parte de cero, y menos todavía fuera de
un laboratorio.

Pero hay una parte del problema que no depende del laboratorio y que sigue sin
resolverse: **no existe una base comparable para decidir qué virus tiene
sentido probar contra qué perfil de tumor.** Esa decisión hoy se toma estudio
por estudio. Quien quiera fundamentarla con la literatura se encuentra con
tamizajes publicados que no se pueden poner juntos, porque usan ensayos,
multiplicidades de infección, tiempos de medición y métricas distintas.

Ese es el hueco que este repositorio intenta cerrar, y es un hueco de datos
para diseñar estudios preclínicos, no de tratamiento.

## Por qué la cantidad a predecir es la permisividad

Un virus oncolítico no necesita compatibilidad antigénica con el tumor. Mata por
replicación lítica, y el efecto inmunológico viene después. Entonces lo que hay
que poder anticipar es si un tumor deja que un virus entre y se replique. Esa es
una propiedad medible en modelos preclínicos, y es justo la que reportan los
tamizajes publicados.

Las capas en las que se puede descomponer esa pregunta, con la evidencia que hay
para cada una, están en [`capas-de-evidencia.md`](capas-de-evidencia.md).

## Hasta dónde llega este repositorio

Solo fase 0 y fase 1, como dice el README: la base de conocimiento de virus con
citas y la armonización de tres estudios publicados. Un motor que reciba un
perfil de expresión y devuelva candidatos queda fuera del alcance mientras no
haya datos armonizados con los que ponerlo a prueba.

El resultado útil no es un ranking. Es saber qué se puede comparar de verdad y
qué no.
