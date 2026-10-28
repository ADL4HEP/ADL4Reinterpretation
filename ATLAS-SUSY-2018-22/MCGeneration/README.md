# ATLAS-SUSY-2018-22 — MC generation

| Files | Model (masses in GeV) | Setup | Events |
|---|---|---|---|
| `SS_direct_1600_400` | squark–antisquark (ũ, d̃, s̃, c̃; L and R), q̃ → qχ̃⁰₁, 1600 / 400 | MLM 0+1 parton | 5 845 after matching |
| `GG_direct_2200_600` | gluino pair, g̃ → qq̄χ̃⁰₁, 2200 / 600 | MLM 0+1 parton | 6 322 after matching |
| `GG_onestepCC_2200_1200_200` | gluino pair, g̃ → qq̄′χ̃±₁, χ̃±₁ → Wχ̃⁰₁, 2200 / 1200 / 200 | MLM 0+1 parton | 6 112 after matching |

`<model>.txt`: MadGraph process card. `<model>.slha`: parameter card with masses and decay tables (all other sparticles at 5 TeV).

Chain: MadGraph5_aMC@NLO 3.6.7 (LO, NNPDF2.3 LO) → Pythia 8.318 with the ATLAS A14 tune (`Tune:pp = 21`) → Delphes 3.5.1.
MLM: `ickkw = 1`, `xqcut = 100` GeV in MadGraph; `JetMatching:qCut = 150` GeV, `nJetMax = 1` in Pythia.
Delphes card: `delphes_card_ATLAS_R04_FatJet.tcl`, the ATLAS card of Delphes 3.5.1 with anti-kt R = 0.4 jets (default 0.6) and an added trimmed R = 1.0 jet collection.
