# ATLAS-SUSY-2015-06: overlaps between its own signal regions

Zero leptons, 2–6 jets, 3.2 fb⁻¹. The ADL file is `ATLAS-SUSY-2015-06/ATLAS-SUSY-2015-06_Delphes.adl` on the `main` branch. There are 7 signal regions:
`s15SR2jl`, `s15SR2jm`, `s15SR2jt`, `s15SR4jt`, `s15SR5j`, `s15SR6jm`, `s15SR6jt`.

## Files
| Folder | Content |
|---|---|
| `acceptance/<sample>.csv.gz` | One row per event, for each of the 9 samples in `MCGeneration`. Columns: `sample`, `slice`, `event`, `weight` (pb for backgrounds, 1 for signals), then one 0/1 column per region (1 = the event passes the region). |
| `correlations/<sample>.csv` | One row per region pair, for each of the 9 samples and the mixtures `mixture_0L`, `mixture_SS` and `mixture_all`. The columns are defined in the top-level README. |
| `static/verdicts.csv` | Static verdict of CutLang-Overlap-Analyzer for each region pair (EQUAL, SUBSET, SUPERSET, DISJOINT, OVERLAP). |
| `static/analyzer_output.txt` | Full analyzer output of the comparison of the ADL file with itself. |
| `figures/correlations_mixture_vs_signal.png` | Correlation ρ of all region pairs: `mixture_0L` on the left, `GG_onestepCC_1600_1000_100` on the right. |

## Static verdicts
21 pairs: 20 OVERLAP, 1 SUPERSET. The pairs that are not OVERLAP are:

| Region a | Region b | Verdict |
|---|---|---|
| `s15SR2jl` | `s15SR2jt` | SUPERSET |

Every nesting holds in all nine samples.

## Figure
The figure puts the background mixture and the signal side by side:
- **Boxes** mark the static nestings.
- **(n)** is the number of MC events in each region.
- **–** marks a pair with no event in common.
- **n/a** marks a pair in which one of the regions is empty in that sample.

Signal correlations are much larger than background correlations, because the signal populates the regions near their thresholds. The correlation therefore depends on the process. For a combination, the covariance of the observed counts comes from the background mixture.
