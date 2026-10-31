# MC generation of the overlap samples

Nine samples: six Standard Model backgrounds (`background/`) and three gluino signals (`signal/`).
The acceptance tables in `../ATLAS-SUSY-*/acceptance/` are made from these samples.

**Chain:** MadGraph5_aMC@NLO 3.6.7 (leading order, NNPDF2.3 LO, 13 TeV) → Pythia 8.318 → Delphes 3.5.1.

**Files in this folder:**
- `delphes_card_ATLAS_R04_FatJet.tcl`: the Delphes card for every sample. It is the ATLAS card of Delphes 3.5.1 with anti-kt R = 0.4 jets, plus a trimmed R = 1.0 jet collection.
- `pythia_Monash.cmnd`, `pythia_A14.cmnd`, `pythia_A14_MLM.cmnd`: Pythia settings. `<seed>` is listed for each sample.

| Sample | Process | Pythia | Events | σ (LO) |
|---|---|---|---|---|
| `Znunu` | Z(→νν)+jet, 4 slices | Monash | 78 634 | 28.2 pb |
| `Wlnu` | W(→ℓν)+jet, ℓ = e, μ, τ, 4 slices | Monash | 120 000 | 120 pb |
| `ttbar` | tt̄ with ≥ 1 leptonic W, 5 slices | Monash | 157 183 | 42 pb |
| `ZV` | Z(→νν)V(→qq), V = W, Z, 3 slices | Monash | 30 000 | 0.21 pb |
| `ttW_SS` | tt̄W with a forced same-charge e/μ pair | A14 | 25 000 | 10.3 fb |
| `ttZ_ll` | tt̄Z, Z → ee/μμ | A14 | 25 000 | 39.4 fb |
| `GG_onestepCC_1600_1000_100` | g̃g̃, g̃ → qq̄′χ̃±₁, χ̃±₁ → Wχ̃⁰₁ | Monash, no matching | 20 000 | 3.6 fb |
| `GG_onestepCC_2200_1200_200` | same, 2200 / 1200 / 200 GeV | A14, MLM | 6 112 | 0.32 fb |
| `Gtt_1600_600` | g̃g̃, g̃ → tt̄χ̃⁰₁ | A14, MLM | 11 993 | 7.6 fb |

**Notes:**
- Events lists the events used. It excludes zero-weight events for the backgrounds and events rejected by the matching for the MLM signals.
- The background cross sections are the weighted sums after the slices are combined; the zero-weight parts of the inclusive slices are removed.
- Every 5 000-event part was generated with its own MadGraph and Pythia seed. The seeds are in `background/slices.csv` and `signal/README.md`.
- The Delphes seed was the card default (time-based), so the detector smearing can be reproduced statistically.
