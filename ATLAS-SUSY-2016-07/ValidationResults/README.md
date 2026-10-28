# ATLAS-SUSY-2016-07 — Validation results

**Reference:** official ATLAS final yields (36.1 fb⁻¹) of the gluino (2000 / 0 GeV) and squark (1500 / 0 GeV) benchmarks, as given in the [MadAnalysis 5 validation note](https://cp3.irmp.ucl.ac.be/projects/madanalysis/raw-attachment/wiki/PublicAnalysisDatabase/validation_atlas_susy_16_07.pdf), with the MA5 result for comparison. Our yields are normalised to the ATLAS initial yield.

## Signal models

| Model | Topology | Process and decays | Mass point (GeV) | Regions compared |
|---|---|---|---|---|
| `GG_direct_2000_0` | T1 | g̃g̃, g̃ → qq̄χ̃⁰₁ | m(g̃) = 2000, m(χ̃⁰₁) = 0 | the 20 regions with an ATLAS number |
| `SS_direct_1500_0` | T2 | q̃q̃*, q̃ → qχ̃⁰₁ (ũ, d̃, s̃, c̃; L and R) | m(q̃) = 1500, m(χ̃⁰₁) = 0 | the 20 regions with an ATLAS number |

One mass point per model: the benchmark for which ATLAS published a cutflow. Efficiency maps and limit comparisons over the mass plane have not been produced yet. All other sparticles are set to 5 TeV. 


## Files

| File | Content |
|---|---|
| `CutflowComparison_GG_direct_2000_0.txt`, `CutflowComparison_SS_direct_1500_0.txt` | final yield in the 20 compared regions, ADL/CutLang vs ATLAS and MA5 |
| `GG_direct_2000_0_ratio.png`, `SS_direct_1500_0_ratio.png` | yield / ATLAS, with MA5 |

## Result

Squarks 16/20 regions within 20% (median deviation 10%), gluinos 11/20 (median 18%).

Error bars and ± values: statistical uncertainty of our Monte Carlo sample only (binomial for efficiencies, √N for yields); the uncertainties of the ATLAS cutflows and of the recasting tools are not included.
