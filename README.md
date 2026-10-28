# Overlaps of the signal regions of LHC searches

This branch holds the overlap study of several LHC searches. For every pair of signal regions it gives two results:
- the **static** relation that ADL-Overlap-Analyzer derives from the ADL files: EQUAL, SUBSET, SUPERSET, DISJOINT or OVERLAP;
- the **dynamic** overlap measured with CutLang on simulated events: how many events two regions share, and how strongly their counts are correlated.

The ADL files are on the `main` branch (`<analysis>/<analysis>_Delphes.adl`). Their validation is on the `validation` branch.

```
overlap/
├── README.md
├── MCGeneration/                       how the 9 samples were made
│   ├── background/                     Znunu, Wlnu, ttbar, ZV, ttW_SS, ttZ_ll: process cards, slices.csv
│   ├── signal/                         3 gluino models: process cards, SLHA files
│   ├── delphes_card_ATLAS_R04_FatJet.tcl
│   └── pythia_*.cmnd
├── ATLAS-SUSY-<id>/                    one folder per analysis: pairs inside the analysis
│   ├── acceptance/<sample>.csv.gz      per-event pass flags of every region
│   ├── correlations/<sample>.csv       κ, ρ, Jaccard of every region pair
│   ├── static/                         analyzer verdicts
│   └── figures/
├── pairwise/<A>_vs_<B>/                one folder per pair of analyses
│   ├── correlations/  static/  figures/  pair_summary.csv
│   └── combinability/                  only 2018-22_vs_2018-09
└── scripts/                            compute_overlap.py, make_figures.py
```

## Samples
| Sample | Role | Events |
|---|---|---|
| `Znunu`, `Wlnu`, `ttbar`, `ZV` | background of the zero-lepton analyses | 78 634, 120 000, 157 183, 30 000 |
| `ttW_SS`, `ttZ_ll` | background of the same-charge-lepton analysis | 25 000, 25 000 |
| `GG_onestepCC_1600_1000_100`, `GG_onestepCC_2200_1200_200`, `Gtt_1600_600` | signals | 20 000, 6 112, 11 993 |

All samples were processed with all four analyses. The details are in `MCGeneration/README.md`.

## Acceptance tables
`acceptance/<sample>.csv.gz` has one row per event. It holds the 0/1 decision of every signal region, from CutLang run with `-r 1` on the Delphes file. Running the `main`-branch ADL files with CutLang v2.15.2 reproduces these tables, checked on the GG_onestepCC_1600, Gtt_1600 and ttW_SS samples for all four analyses.

The `weight` column gives σ_slice/N_slice in pb for the backgrounds and 1 for the signals. Events of an inclusive slice that a dedicated slice covers have weight 0 and are not stored.

The tables of the four analyses have identical event lists (`sample`, `slice`, `event`). Tables of different analyses can therefore be joined event by event, this is how `pairwise/` is made.

## Correlation tables
Each region pair (a, b) has one row in `correlations/<sample>.csv`. For a weighted sample, σ_x is the sum of the event weights that pass x:

| Column | Definition |
|---|---|
| `n_a`, `n_b`, `n_ab` | Unweighted MC events passing a, passing b, and passing both. |
| `sigma_a`, `sigma_b`, `sigma_ab` | Weighted sums: pb for backgrounds, event counts for signals. |
| `kappa` | κ = σ_ab / √(σ_a σ_b). Observed counts are Poisson, so cov(N_a, N_b) = L σ_ab and var(N_a) = L σ_a, and κ is the correlation of the observed counts. This is the quantity a combination needs. |
| `rho` | Weighted Pearson correlation of the two 0/1 pass flags. It is related to κ, but it takes a small negative value for disjoint regions, because the sample has a fixed number of events, while κ is 0. |
| `jaccard` | σ_ab / (σ_a + σ_b − σ_ab), the fraction of the union that both regions select. |
| `*_err` | MC statistical uncertainty: the standard deviation over 200 bootstrap replicas, in which every event is reweighted by a Poisson(1) number (seed 12345). |

Besides the nine samples there are three cross-section weighted mixtures:
- `mixture_0L` = Znunu + Wlnu + ttbar + ZV;
- `mixture_SS` = ttW_SS + ttZ_ll;
- `mixture_all` = all six backgrounds.

For a combination the relevant matrix is that of the background mixture. It determines the covariance of the observed counts under the background-only hypothesis. The signal matrices show how strongly the correlation depends on the process.

When two analyses use different data sets (3.2, 36.1 and 139 fb⁻¹, each containing the smaller ones), the count correlation is ℓκ with ℓ = √(L_small/L_large). See `pairwise/README.md`.

## Static verdicts
The verdicts come from the corrected version of CutLang-Overlap-Analyzer: github.com/BerkayA8/CutLang-Overlap-Analyzer, commit 6471de2, plus the correction that pairs the guard conditions of the lepton vetoes. The correction is not yet in the public repository; the outputs here are those of the corrected version.

`verdicts.csv` lists one verdict per region pair, and `analyzer_output*.txt` contains the full analyzer output. In every sample, each SUBSET or SUPERSET verdict holds (n_ab equals the n of the smaller region) and each DISJOINT verdict holds (n_ab = 0).

## Reproducing
```
python3 scripts/compute_overlap.py .     # correlations/ of every analysis and pair, from acceptance/  (≈ 10 min)
python3 scripts/make_figures.py .        # figures/
```
