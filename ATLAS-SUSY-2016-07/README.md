# ATLAS-SUSY-2016-07: overlaps between its own signal regions

Zero leptons, Meff-based regions, 36.1 fb⁻¹. The ADL file is `ATLAS-SUSY-2016-07/ATLAS-SUSY-2016-07_Delphes.adl` on the `main` branch. There are 24 signal regions:
`s16Meff2j1200`, `s16Meff2j1600`, `s16Meff2j2000`, `s16Meff2j2100`, `s16Meff2j2400`, `s16Meff2j2800`, `s16Meff2j3600`, `s16Meff2jB1600`, `s16Meff2jB2400`, `s16Meff3j1300`, `s16Meff4j1000`, `s16Meff4j1400`, `s16Meff4j1800`, `s16Meff4j2200`, `s16Meff4j2600`, `s16Meff4j3000`, `s16Meff5j1600`, `s16Meff5j1700`, `s16Meff5j2000`, `s16Meff5j2600`, `s16Meff6j1200`, `s16Meff6j1800`, `s16Meff6j2200`, `s16Meff6j2600`.

## Files
| Folder | Content |
|---|---|
| `acceptance/<sample>.csv.gz` | One row per event, for each of the 9 samples in `MCGeneration`. Columns: `sample`, `slice`, `event`, `weight` (pb for backgrounds, 1 for signals), then one 0/1 column per region (1 = the event passes the region). |
| `correlations/<sample>.csv` | One row per region pair, for each of the 9 samples and the mixtures `mixture_0L`, `mixture_SS` and `mixture_all`. The columns are defined in README. |
| `static/verdicts.csv` | Static verdict of CutLang-Overlap-Analyzer for each region pair (EQUAL, SUBSET, SUPERSET, DISJOINT, OVERLAP). |
| `static/analyzer_output.txt` | Full analyzer output of the comparison of the ADL file with itself. |
| `figures/correlations_mixture_vs_signal.png` | Correlation ρ of all region pairs: `mixture_0L` on the left, `GG_onestepCC_1600_1000_100` on the right. |

## Static verdicts
276 pairs: 264 OVERLAP, 12 SUPERSET. The pairs that are not OVERLAP are:

| Region a | Region b | Verdict |
|---|---|---|
| `s16Meff2j1600` | `s16Meff2j2000` | SUPERSET |
| `s16Meff2j1600` | `s16Meff2j2400` | SUPERSET |
| `s16Meff2j1600` | `s16Meff2j2800` | SUPERSET |
| `s16Meff2j2000` | `s16Meff2j2400` | SUPERSET |
| `s16Meff2j2000` | `s16Meff2j2800` | SUPERSET |
| `s16Meff2j2400` | `s16Meff2j2800` | SUPERSET |
| `s16Meff2jB1600` | `s16Meff2jB2400` | SUPERSET |
| `s16Meff4j1400` | `s16Meff4j1800` | SUPERSET |
| `s16Meff4j1400` | `s16Meff4j2200` | SUPERSET |
| `s16Meff4j1800` | `s16Meff4j2200` | SUPERSET |
| `s16Meff4j2600` | `s16Meff4j3000` | SUPERSET |
| `s16Meff5j2000` | `s16Meff5j2600` | SUPERSET |

Every nesting holds in all nine samples.

## Figure
The figure puts the background mixture and the signal side by side:
- **Boxes** mark the static nestings.
- **(n)** is the number of MC events in each region.
- **–** marks a pair with no event in common.
- **n/a** marks a pair in which one of the regions is empty in that sample.

Signal correlations are much larger than background correlations, because the signal populates the regions near their thresholds. The correlation therefore depends on the process. For a combination, the covariance of the observed counts comes from the background mixture.
