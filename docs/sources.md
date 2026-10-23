# Sources

The three studies that open phase 1. They were chosen because the first two
screen the same cell line panel with the same viral genus under different
conditions, which is the exact case the schema has to survive, and the third
uses a different model type and a different virus set, which tests whether the
schema generalises beyond cell lines.

No PDF, figure or complete supplementary table from these papers is
redistributed in this repository. Extracted values are stored with their DOI
and their location inside the paper, as individual data points.

Metadata and license below were read from Crossref and Europe PMC records on
2026-10-22.

## 1. NCI-60 panel, vaccinia GLV-1h68, 2011

* Ascierto ML, Worschech A, Yu Z, Adams S, Reinboth J, Chen NG, Pos Z,
  Roychoudhuri R, Di Pasquale G, Bedognetti D, Uccellini L, Rossano F,
  Ascierto PA, Stroncek DF, Restifo NP, Wang E, Szalay AA, Marincola FM.
  *Permissivity of the NCI-60 cancer cell lines to oncolytic Vaccinia Virus
  GLV-1h68.* BMC Cancer 2011, 11:451.
* DOI: [10.1186/1471-2407-11-451](https://doi.org/10.1186/1471-2407-11-451)
* PMID 22011439, PMCID PMC3213037
* License: Creative Commons Attribution, open access (Europe PMC license field
  `cc by`)
* Why it is here: it reports permissivity across a large panel together with
  pre infection transcriptional profiles, which is the combination the later
  layers would need.

## 2. NCI-60 panel, vaccinia GLV-1h94, 2020

* Berchtold S, Beil J, Raff C, Smirnow I, Schell M, D'Alvise J, Gross S,
  Lauer UM. *Assessing and Overcoming Resistance Phenomena against a
  Genetically Modified Vaccinia Virus in Selected Cancer Cell Lines.*
  International Journal of Molecular Sciences 2020, 21(20):7618.
* DOI: [10.3390/ijms21207618](https://doi.org/10.3390/ijms21207618)
* PMID 33076270, PMCID PMC7589280
* License: Creative Commons Attribution 4.0
  (<https://creativecommons.org/licenses/by/4.0/>)
* Why it is here: it screens the same panel with the same viral genus, and
  about half the lines were highly sensitive to the virus alone, according to
  the abstract. Different assay, different conditions, same panel. This is the
  pair that forces the schema to be explicit.

## 3. Patient derived pancreatic cancer cultures, five viruses, 2024

* Schäfer TE, Knol LI, Haas FV, Hartley A, Pernickel SCS, Jády A,
  Finkbeiner MSC, Achberger J, Arelaki S, Modic Ž, Schröer K, Zhang W,
  Schmidt B, Schuster P, Haferkamp S, Doerner J, Gebauer F, Ackermann M,
  Kvasnicka HM, Kulkarni A, Bots STF, Kemp V, Hawinkels LJAC, Poetsch AR,
  Hoeben RC, Ehrhardt A, Marchini A, Ungerechts G, Ball CR, Engeland CE.
  *Biomarker screen for efficacy of oncolytic virotherapy in patient-derived
  pancreatic cancer cultures.* eBioMedicine 2024, 105:105219.
* DOI: [10.1016/j.ebiom.2024.105219](https://doi.org/10.1016/j.ebiom.2024.105219)
* PMID 38941955, PMCID PMC11260584
* License: Creative Commons Attribution NonCommercial NoDerivatives 4.0
  (<http://creativecommons.org/licenses/by-nc-nd/4.0/>)
* Why it is here: patient derived cultures instead of cell lines, and several
  different viruses, so it breaks any schema that silently assumes one virus
  per study and one model type.

### Note on the third license

CC BY-NC-ND covers redistribution of the article itself. Nothing of the
article is redistributed here. Extracted factual values are stored with their
citation. If a later release needs to redistribute any part of that article,
the license has to be checked again for that specific use.

## Background reading

Not extraction targets, listed because they shaped the design.

* Matveeva OV, Chumakov PM. *Defects in interferon pathways as potential
  biomarkers of sensitivity to oncolytic viruses.* Rev Med Virol 2018,
  28:e2008. DOI [10.1002/rmv.2008](https://doi.org/10.1002/rmv.2008)
* Forčić D et al. Vaccines 2024, 12:958. PMID 39339989.
* OvirusTdb, Raghava group, IIIT-Delhi.
  <https://webs.iiitd.edu.in/raghava/ovirustdb/>

## Adding a source

A new source needs, in this file: full citation, DOI, PMID or PMCID when one
exists, the license as read from the publisher record with the date it was
read, and one sentence saying what it tests about the schema.
