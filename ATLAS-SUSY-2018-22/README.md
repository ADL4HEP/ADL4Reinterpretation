# ATLAS-SUSY-2018-22: overlaps between its own signal regions

Zero leptons, full Run 2, 139 fb⁻¹. The ADL file is `ATLAS-SUSY-2018-22/ATLAS-SUSY-2018-22_Delphes.adl` on the `main` branch. There are 10 signal regions:
`s1822SR2j1600`, `s1822SR2j2200`, `s1822SR2j2800`, `s1822SR4j1000`, `s1822SR4j2200`, `s1822SR4j3400`, `s1822SR5j1600`, `s1822SR6j1000`, `s1822SR6j2200`, `s1822SR6j3400`.

## Files
| Folder | Content |
|---|---|
| `acceptance/<sample>.csv.gz` | One row per event, for each of the 9 samples in `MCGeneration`. Columns: `sample`, `slice`, `event`, `weight` (pb for backgrounds, 1 for signals), then one 0/1 column per region (1 = the event passes the region). |
| `correlations/<sample>.csv` | One row per region pair, for each of the 9 samples and the mixtures `mixture_0L`, `mixture_SS` and `mixture_all`. The columns are defined in the top-level README. |
| `static/verdicts.csv` | Static verdict of ADL-Overlap-Analyzer for each region pair (EQUAL, SUBSET, SUPERSET, DISJOINT, OVERLAP). |
| `static/analyzer_output.txt` | Full analyzer output of the comparison of the ADL file with itself. |
| `figures/correlations_mixture_vs_signal.png` | Correlation ρ of all region pairs: `mixture_0L` on the left, `GG_onestepCC_2200_1200_200` on the right. |

## Static verdicts
45 pairs: 42 OVERLAP, 3 SUPERSET. The pairs that are not OVERLAP are:

| Region a | Region b | Verdict |
|---|---|---|
| `s1822SR2j1600` | `s1822SR2j2800` | SUPERSET |
| `s1822SR4j1000` | `s1822SR4j2200` | SUPERSET |
| `s1822SR6j1000` | `s1822SR6j2200` | SUPERSET |

Every nesting holds in all nine samples.

## Figure
The figure puts the background mixture and the signal side by side:
- **Boxes** mark the static nestings.
- **(n)** is the number of MC events in each region.
- **–** marks a pair with no event in common.
- **n/a** marks a pair in which one of the regions is empty in that sample.

Signal correlations are much larger than background correlations, because the signal populates the regions near their thresholds. The correlation therefore depends on the process. For a combination, the covariance of the observed counts comes from the background mixture.
