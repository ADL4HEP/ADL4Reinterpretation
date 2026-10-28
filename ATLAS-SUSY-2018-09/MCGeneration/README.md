# ATLAS-SUSY-2018-09 — MC generation

| Files | Model (masses in GeV) | Setup | Events |
|---|---|---|---|
| `TT_tN2_800_625_525_520` | stop pair, t̃₁ → tχ̃⁰₂, χ̃⁰₂ → W∓χ̃±₁, 800 / 625 / 525 (χ̃⁰₁ 520) | MLM 0+1 parton | 12 259 after matching |
| `BB_tC1_850_500_400` | sbottom pair, b̃₁ → tχ̃⁻₁, χ̃±₁ → Wχ̃⁰₁, 850 / 500 / 400 | MLM 0+1 parton | 24 422 after matching |

`<model>.txt`: MadGraph process card. `<model>.slha`: parameter card with masses and decay tables (all other sparticles at 5 TeV).

Chain: MadGraph5_aMC@NLO 3.6.7 (LO, NNPDF2.3 LO) → Pythia 8.318 with the ATLAS A14 tune (`Tune:pp = 21`) → Delphes 3.5.1.
MLM: `ickkw = 1`, `xqcut = 100` GeV in MadGraph; `JetMatching:qCut = 150` GeV, `nJetMax = 1` in Pythia.
Delphes card: `delphes_card_ATLAS_R04_FatJet.tcl`, the ATLAS card of Delphes 3.5.1 with anti-kt R = 0.4 jets (default 0.6) and an added trimmed R = 1.0 jet collection.
