# ATLAS-SUSY-2016-07 — MC generation

| Files | Model (masses in GeV) | Setup | Events |
|---|---|---|---|
| `GG_direct_2000_0` | gluino pair, g̃ → qq̄χ̃⁰₁, 2000 / 0 | decays in MadGraph, no extra parton | 5 000 |
| `SS_direct_1500_0` | squark–antisquark (ũ, d̃, s̃, c̃; L and R), q̃ → qχ̃⁰₁, 1500 / 0 | MLM 0+1 parton | 10 000 (5 857 after matching) |

`<model>.txt`: MadGraph process card. `<model>.slha`: parameter card with masses and decay tables (all other sparticles at 5 TeV).

Chain: MadGraph5_aMC@NLO 3.6.7 (LO, NNPDF2.3 LO) → Pythia 8.318 with the ATLAS A14 tune (`Tune:pp = 21`) → Delphes 3.5.1.
MLM: `ickkw = 1`, `xqcut = 100` GeV in MadGraph; `JetMatching:qCut = 150` GeV, `nJetMax = 1` in Pythia.
Delphes card: `delphes_card_ATLAS_R04_FatJet.tcl`, the ATLAS card of Delphes 3.5.1 with anti-kt R = 0.4 jets (default 0.6) and an added trimmed R = 1.0 jet collection.
The trimmed R = 1.0 jets are needed by the boosted 2jB regions. The neutralino mass is set to 0.5 GeV.
