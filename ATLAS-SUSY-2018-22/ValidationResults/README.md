# ATLAS-SUSY-2018-22 — Validation results

**Reference:** official ATLAS cutflows of three benchmarks (squark 1600/400, gluino 2200/600, one-step gluino 2200/1200/200 GeV), as transcribed in the [CheckMATE validation note](https://github.com/CheckMATE2/checkmate2/tree/master/data/validationNotes/atlas_2010_14293) (cutflows of ATLAS-CONF-2019-040). Our yields are normalised after event cleaning, CheckMATE's after the preselection.

## Signal models

| Model | Topology | Process and decays | Mass point (GeV) | Regions compared |
|---|---|---|---|---|
| `SS_direct_1600_400` | T2 | q̃q̃*, q̃ → qχ̃⁰₁ (ũ, d̃, s̃, c̃; L and R) | m(q̃) = 1600, m(χ̃⁰₁) = 400 | 2j-1600, 2j-2200, 2j-2800 |
| `GG_direct_2200_600` | T1 | g̃g̃, g̃ → qq̄χ̃⁰₁ | m(g̃) = 2200, m(χ̃⁰₁) = 600 | 4j-1000, 4j-2200, 4j-3400 |
| `GG_onestepCC_2200_1200_200` | T5WW | g̃g̃, g̃ → qq̄′χ̃±₁, χ̃±₁ → W±χ̃⁰₁ | m(g̃) = 2200, m(χ̃±₁) = 1200, m(χ̃⁰₁) = 200 | 5j-1600, 6j-1000, 6j-2200, 6j-3400 |

One mass point per model: the benchmark for which ATLAS published a cutflow. Efficiency maps and limit comparisons over the mass plane have not been produced yet. All other sparticles are set to 5 TeV. 

## Files

| File | Content |
|---|---|
| `CutflowComparison_<model>.txt` | every cutflow row of the 10 regions: ADL/CutLang vs ATLAS, and CheckMATE / ATLAS |
| `ATLAS-SUSY-2018-22_ratio.png` | final yield / ATLAS, with CheckMATE |
| `<model>_cutflow.png` | yield / ATLAS after every cut of each region, with CheckMATE |

## Result

7/10 regions within 20%, all intermediate rows within 16%. The largest deviations are the highest-meff tails, 2j-2800 (0.76) and 4j-3400 (1.56), where CheckMATE also has its largest (0.92, 0.94), and 6j-1000/6j-2200 (0.84), which arise at the MET/√HT cut.

Error bars and ± values: statistical uncertainty of our Monte Carlo sample only (binomial for efficiencies, √N for yields); the uncertainties of the ATLAS cutflows and of the recasting tools are not included.
