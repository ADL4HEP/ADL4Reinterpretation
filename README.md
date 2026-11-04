# **ADL4Reinterpretation**

This repository collects validated LHC analyses written in **ADL (Analysis Description Language)** and executed using the **CutLang runtime interpreter**.
The purpose of this project is to provide a reproducible set of analyses that can be directly used for **phenomenology studies** and **reinterpretation workflows**.

---

## **Repository structure**

The repository is organized into three branches:

- **The main branch** contains final ADL files and any necessary auxiliary materials such as ML models.
- **The validation branch** contains MC generation information and validation results, including cutflow comparisons, efficiency maps and comparisons, and limit comparisons for each analysis.
- **The overlap branch** contains overlap studies between the signal regions of different analyses. For every pair of signal regions it gives the static relation derived from the ADL files with the ADL Overlap Analyzer (EQUAL, SUBSET, SUPERSET, DISJOINT or OVERLAP), and the dynamic overlap measured with CutLang on simulated events: per-event pass flags, correlations between signal regions with bootstrap uncertainties, and the sets of signal regions that can be combined.

---

## **CutLang Repository**

[https://github.com/unelg/CutLang](https://github.com/unelg/CutLang)

