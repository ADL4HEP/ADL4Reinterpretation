# CMS-SUS-21-006 — Validation Results

This directory contains the validation outputs for the ADL/CutLang implementation of the CMS disappearing-track search:

CMS-SUS-21-006 

Official CMS numerical results used for validation are taken from:
HEPData record INS2705044.

---

## Signal Models

Validation is provided for the following simplified models:

### 1. T5btbtLL (ctau = 10 cm)

Gluino pair production with long-lived charginos leading to disappearing tracks.

Results provided:
- Signal selection efficiency maps (A×ε)
- Cutflow comparison for the benchmark point:
- m_gluino = 1.5 TeV
- m_LSP = 1.1 TeV
- Pearson correlation coefficient between our efficiencies and official CMS efficiencies
- Relative discrepancy per signal region

Official CMS efficiencies are taken from HEPData and used as reference.

---

### 2. C1C1

Chargino pair production with nearly mass-degenerate neutralino LSP.

Results provided:
- Signal selection efficiency maps (A×ε)

---

### 3. C1N1

Chargino–neutralino associated production with a long-lived chargino.

Results provided:
- Signal selection efficiency maps (A×ε)

---

## Efficiency Definition

Efficiencies correspond to:

A × ε = N_selected / N_generated

for each CMS-SUS-21-006 signal region.

They are obtained using Delphes-level simulation and the ADL/CutLang implementation.

