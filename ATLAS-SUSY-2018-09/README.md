# ATLAS-SUSY-2018-09: overlaps between its own signal regions

Same-charge leptons or three leptons, full Run 2, 139 fb⁻¹. The ADL file is `ATLAS-SUSY-2018-09/ATLAS-SUSY-2018-09_Delphes.adl` on the `main` branch. There are 5 signal regions:
`s1809Rpc2L0b`, `s1809Rpc2L1b`, `s1809Rpc2L2b`, `s1809Rpc3LSS1b`, `s1809Rpv2L`.

## Files
| Folder | Content |
|---|---|
| `acceptance/<sample>.csv.gz` | One row per event, for each of the 9 samples in `MCGeneration`. Columns: `sample`, `slice`, `event`, `weight` (pb for backgrounds, 1 for signals), then one 0/1 column per region (1 = the event passes the region). |
| `correlations/<sample>.csv` | One row per region pair, for each of the 9 samples and the mixtures `mixture_0L`, `mixture_SS` and `mixture_all`. The columns are defined in the top-level README. |
| `static/verdicts.csv` | Static verdict of ADL-Overlap-Analyzer for each region pair (EQUAL, SUBSET, SUPERSET, DISJOINT, OVERLAP). |
| `static/analyzer_output.txt` | Full analyzer output of the comparison of the ADL file with itself. |
| `figures/correlations_mixture_vs_signal.png` | Correlation ρ of all region pairs: `mixture_SS` on the left, `Gtt_1600_600` on the right. |

## Static verdicts
10 pairs: 7 OVERLAP, 3 DISJOINT. The pairs that are not OVERLAP are:

| Region a | Region b | Verdict |
|---|---|---|
| `s1809Rpc2L0b` | `s1809Rpc2L1b` | DISJOINT |
| `s1809Rpc2L0b` | `s1809Rpc2L2b` | DISJOINT |
| `s1809Rpc2L0b` | `s1809Rpc3LSS1b` | DISJOINT |

The three DISJOINT pairs follow from the b-jet multiplicity, which is `== 0` in Rpc2L0b and `>= 1` in the other regions. No sample has an event in any of these pairs.

## Figure
The figure puts the background mixture and the signal side by side:
- **Boxes** mark the static nestings.
- **(n)** is the number of MC events in each region.
- **–** marks a pair with no event in common.
- **n/a** marks a pair in which one of the regions is empty in that sample.

Signal correlations are much larger than background correlations, because the signal populates the regions near their thresholds. The correlation therefore depends on the process. For a combination, the covariance of the observed counts comes from the background mixture.
