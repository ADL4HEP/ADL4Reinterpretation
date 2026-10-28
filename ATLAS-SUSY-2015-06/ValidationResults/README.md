# ATLAS-SUSY-2015-06 — Validation results

**Reference:** official ATLAS relative efficiencies of benchmark 1 (gluino pair, 1600 / 0 GeV), as transcribed in the [MadAnalysis 5 validation note](https://cp3.irmp.ucl.ac.be/projects/madanalysis/raw-attachment/wiki/PublicAnalysisDatabase/multijet.pdf). The MA5 result of the note is shown for comparison.

## Signal models

| Model | Topology | Process and decays | Mass point (GeV) | Regions compared |
|---|---|---|---|---|
| `GG_direct_1600_0` | T1 | g̃g̃, g̃ → qq̄χ̃⁰₁ | m(g̃) = 1600, m(χ̃⁰₁) = 0 | all 7 |

One mass point per model: the benchmark for which ATLAS published a cutflow. Efficiency maps and limit comparisons over the mass plane have not been produced yet. All other sparticles are set to 5 TeV. Topology names as in SModelS where one exists.

## Files

| File | Content |
|---|---|
| `CutflowComparison_GG_direct_1600_0.txt` | relative efficiency of every cut and total efficiency, ADL/CutLang vs ATLAS and MA5 |
| `GG_direct_1600_0_ratio.png` | total efficiency / ATLAS for the 7 regions |

## Result

Cuts that do not depend on additional jets (preselection, Δφ, pT(j2), pT(j4), meff) agree with ATLAS within 1–3%. The 2-jet regions are 10–25% low (MET/√HT cut) and SR5j, SR6jm, SR6jt 21–46% high (jet multiplicity cut), MA5 deviates in the same direction in the 6-jet regions but less. The deviations follow the modelling of additional jets in our LO samples, not the selection.

Error bars and ± values: statistical uncertainty of our Monte Carlo sample only (binomial for efficiencies, √N for yields); the uncertainties of the ATLAS cutflows and of the recasting tools are not included.
