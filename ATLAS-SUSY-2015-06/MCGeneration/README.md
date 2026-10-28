# ATLAS-SUSY-2015-06 — MC generation

| Files | Model (masses in GeV) | Setup | Events |
|---|---|---|---|
| `GG_direct_1600_0` | gluino pair, g̃ → qq̄χ̃⁰₁, 1600 / 0 | gluino decays computed by MadGraph, no extra parton | 5 000 |

`<model>.txt`: MadGraph process card. `<model>.slha`: parameter card with masses and decay tables (all other sparticles at 5 TeV).

Chain: MadGraph5_aMC@NLO 3.6.7 (LO, NNPDF2.3 LO) → Pythia 8.318 with the ATLAS A14 tune (`Tune:pp = 21`) → Delphes 3.5.1.
MLM: `ickkw = 1`, `xqcut = 100` GeV in MadGraph; `JetMatching:qCut = 150` GeV, `nJetMax = 1` in Pythia.
Delphes card: `delphes_card_ATLAS_R04_FatJet.tcl`, the ATLAS card of Delphes 3.5.1 with anti-kt R = 0.4 jets (default 0.6) and an added trimmed R = 1.0 jet collection.
The neutralino mass is set to 0.5 GeV ("massless"). The gluino decays are done in MadGraph because the three-body decay g̃ → qq̄χ̃⁰₁ is then generated with its matrix element (with decays in Pythia (uniform phase space) the jet momenta are softer).
