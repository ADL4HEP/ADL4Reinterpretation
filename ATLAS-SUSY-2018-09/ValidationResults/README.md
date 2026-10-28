# ATLAS-SUSY-2018-09 — Validation results

**Reference:** official ATLAS cutflows of the sbottom (850/500/400 GeV) and stop (800/625/525 GeV) benchmarks, as transcribed in the [CheckMATE validation note](https://github.com/CheckMATE2/checkmate2/tree/master/data/validationNotes/atlas_1909_08457). The trigger is not emulated: yields are normalised after the two same-charge leptons.

## Signal models

| Model | Topology | Process and decays | Mass point (GeV) | Regions compared |
|---|---|---|---|---|
| `BB_tC1_850_500_400` | — | b̃₁b̃₁*, b̃₁ → tχ̃∓₁, χ̃±₁ → W±χ̃⁰₁ | m(b̃₁) = 850, m(χ̃±₁) = 500, m(χ̃⁰₁) = 400 | Rpc2L1b, Rpc2L2b |
| `TT_tN2_800_625_525_520` | — | t̃₁t̃₁*, t̃₁ → tχ̃⁰₂, χ̃⁰₂ → W∓χ̃±₁, χ̃±₁ → χ̃⁰₁ + soft | m(t̃₁) = 800, m(χ̃⁰₂) = 625, m(χ̃±₁) = 525, m(χ̃⁰₁) = 520 | Rpc3LSS1b |

One mass point per model: the benchmark for which ATLAS published a cutflow. Efficiency maps and limit comparisons over the mass plane have not been produced yet. All other sparticles are set to 5 TeV. 

## Files

| File | Content |
|---|---|
| `CutflowComparison_<model>.txt` | every cutflow row of Rpc2L1b, Rpc2L2b (sbottom) and Rpc3LSS1b (stop): ADL/CutLang vs ATLAS, and CheckMATE / ATLAS |
| `ATLAS-SUSY-2018-09_ratio.png` | final yield / ATLAS, with CheckMATE |
| `<model>_cutflow.png` | yield / ATLAS after every cut of each region, with CheckMATE |

## Result

Rpc2L1b 1.24 ± 0.20 and Rpc2L2b 0.91 ± 0.24 (CheckMATE 0.92, 0.62); Rpc3LSS1b 1.4 ± 0.4, an excess also seen by CheckMATE (1.55), which notes that the ATLAS uncertainties of this cutflow are implausible. Rpv2L and Rpc2L0b are not yet validated against ATLAS.

Error bars and ± values: statistical uncertainty of our Monte Carlo sample only (binomial for efficiencies, √N for yields); the uncertainties of the ATLAS cutflows and of the recasting tools are not included.
