# Signal samples

- `<model>.txt`: the MadGraph process card, with its run-card changes in the comment lines.
- `<model>.slha`: the parameter card, with the masses and the decay table that Pythia applies. All other sparticles are at 5 TeV.

Model names follow `<production>_<decay>_<masses in GeV>`.

| Model | Masses (g̃ / χ̃±₁ / χ̃⁰₁) | Decay | Setup | MadGraph seeds | Pythia seeds | Events |
|---|---|---|---|---|---|---|
| `GG_onestepCC_1600_1000_100` | 1600 / 1000 / 100 | g̃ → qq̄′χ̃±₁ (q = u, d, s, c), χ̃±₁ → Wχ̃⁰₁ | LO g̃g̃, Monash (`pythia_Monash.cmnd`) | 8101–8104 | 8201–8204 | 20 000 |
| `GG_onestepCC_2200_1200_200` | 2200 / 1200 / 200 | as above | MLM 0+1 parton, A14 (`pythia_A14_MLM.cmnd`) | 9501–9502 | 9521–9522 | 6 112 after matching |
| `Gtt_1600_600` | 1600 / – / 600 | g̃ → tt̄χ̃⁰₁ | MLM 0+1 parton, A14 (`pythia_A14_MLM.cmnd`) | 9801–9804 | 9821–9824 | 11 993 after matching |

**MLM settings:**
- MadGraph: `ickkw = 1`, `xqcut = 100` GeV.
- Pythia: `JetMatching:qCut = 150` GeV, `nJetMax = 1`.

**Weights:** each signal event has weight 1. Signal correlations do not depend on the normalisation.

**Which signal goes with which analysis:**
- `GG_onestepCC_1600_1000_100`: the zero-lepton analyses 2015-06 and 2016-07.
- `GG_onestepCC_2200_1200_200`: the 2018-22 benchmark. It is used for 2018-22, both internally and in its pairs.
- `Gtt_1600_600`: gives same-charge leptons. It is used for 2018-09.
