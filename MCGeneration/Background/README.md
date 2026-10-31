# Background samples

- `<sample>.txt`: the MadGraph process card. Its commented lines are the changes to the default run card. `<…>` values depend on the slice.
- `slices.csv`: one row per slice, with these columns:
  - generator-level cut;
  - cross section σ (the mean of the MadGraph parts);
  - generated events, and events with non-zero weight;
  - MadGraph and Pythia seeds (one per 5 000-event part);
  - Pythia card;
  - event-weight rule.

## Event weights
Each event gets the weight w = σ_slice / N_slice, in pb. The weights are in the `weight` column of the acceptance tables. Summing w over the events in a region gives that region's cross section.

Two samples have an inclusive slice that overlaps dedicated slices:
- **Znunu**, slice 1: events with LHE jet pT ≥ 300 GeV.
- **ttbar**, slice 1: events with parton MET ≥ 200 GeV, or with MET < 200 GeV and parton HT > 400 GeV.

These events get weight 0, because the dedicated slices cover them. They are left out of the acceptance tables.

## Generator-level cuts
- **No lepton cuts** for Wlnu, ttbar, ttW_SS and ttZ_ll (`ptl 0`, `etal -1`, `drjl 0`). Leptons that are soft, forward or close to a jet are the ones that are lost, so these events enter the 0-lepton regions.
- **ttbar** uses `cut_decays True`. The parton MET cut (the summed neutrino pT) then acts on the decay products, while every other decay cut is switched off.
- **ZV** keeps `cut_decays False` and sets `drjj 0`, so that collimated V → qq pairs from boosted bosons are kept.

## Mixtures used in `correlations/`
- **mixture_0L:** Znunu + Wlnu + ttbar + ZV, the background of the zero-lepton analyses.
- **mixture_SS:** ttW_SS + ttZ_ll, the background of the same-charge-lepton analysis.
- **mixture_all:** all six samples.

Every mixture combines the samples with their weights. All cross sections are leading order, so the mixtures are indicative.
