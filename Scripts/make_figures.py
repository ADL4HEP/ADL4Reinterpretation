"""Background mixture vs signal: weighted Pearson correlation of region pairs, side by side.
Boxes: nestings derived by the static method (any control comparison). Dashes: no shared event.
usage: python3 make_figures.py <overlap dir>"""
import sys, os
import numpy as np, pandas as pd, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle

D = sys.argv[1]
CM = LinearSegmentedColormap.from_list("c", ["#FFFFFF", "#BFDDF1", "#0678C1", "#03436d"])
INK, MARK = "#1B1B1B", "#B4681E"
plt.rcParams.update({"font.family": "DejaVu Sans"})
SIGLAB = {"GG_onestepCC_1600_1000_100": "signal: g̃g̃ one-step 1600/1000/100", "GG_onestepCC_2200_1200_200": "signal: g̃g̃ one-step 2200/1200/200",
          "Gtt_1600_600": "signal: Gtt 1600/600"}
MIXLAB = {"mixture_0L": "background mixture: Z(νν), W(ℓν), tt̄, ZV", "mixture_SS": "background mixture: tt̄W, tt̄Z"}


def short(r):
    for p in ("s1822SR", "s1809", "s16Meff", "s15"):
        if r.startswith(p): return r[len(p):]
    return r


def matrix(df, ra, rb, key="rho"):
    M = np.full((len(ra), len(rb)), np.nan); Z = np.zeros_like(M, bool)
    idx = {(r.region_a, r.region_b): r for r in df.itertuples()}
    for i, a in enumerate(ra):
        for j, b in enumerate(rb):
            r = idx.get((a, b)) or idx.get((b, a))
            if r is None: continue
            M[i, j] = getattr(r, key); Z[i, j] = r.n_ab == 0
    return M, Z


def draw(ax, M, Z, ra, rb, nest, title, tri, n):
    shown = np.where(np.isnan(M), 0, np.clip(M, 0, None))
    if tri: shown = np.ma.masked_where(np.triu(np.ones_like(M, bool), k=1), shown)
    ax.imshow(shown, cmap=CM, vmin=0, vmax=1, aspect="auto")
    fs = 6.5 if len(rb) > 15 else 8
    for i in range(len(ra)):
        for j in range(len(rb)):
            if tri and j > i: continue
            if np.isnan(M[i, j]): ax.text(j, i, "n/a", ha="center", va="center", fontsize=fs - 1, color="#aaa"); continue
            if Z[i, j]: ax.text(j, i, "–", ha="center", va="center", fontsize=fs + 2, color="#888"); continue
            ax.text(j, i, f"{M[i, j]:.2f}", ha="center", va="center", fontsize=fs, color="white" if M[i, j] > 0.55 else INK)
            if (ra[i], rb[j]) in nest or (rb[j], ra[i]) in nest:
                ax.add_patch(Rectangle((j - .45, i - .45), .9, .9, fill=False, edgecolor=MARK, lw=2))
    ax.set_xticks(range(len(rb))); ax.set_xticklabels([f"{short(x)} ({n.get(x, 0)})" for x in rb], rotation=60, ha="right", fontsize=fs + 0.5)
    ax.set_yticks(range(len(ra))); ax.set_yticklabels([f"{short(x)} ({n.get(x, 0)})" for x in ra], fontsize=fs + 0.5)
    ax.set_title(title, fontsize=9, color=INK); ax.tick_params(length=0)
    for s in ax.spines.values(): s.set_visible(False)


def figure(path, ra, rb, mix_df, sig_df, mix, sig, nest, suptitle, tri=False):
    w = max(7, 0.42 * len(rb) * 2 + 2) if not tri else max(8, 0.5 * len(rb) * 2 + 2)
    fig, axes = plt.subplots(1, 2, figsize=(w, 0.42 * len(ra) + 2.4))
    for ax, df, lab in ((axes[0], mix_df, MIXLAB[mix]), (axes[1], sig_df, SIGLAB[sig])):
        M, Z = matrix(df, ra, rb)
        n = {**dict(zip(df.region_a, df.n_a)), **dict(zip(df.region_b, df.n_b))}
        draw(ax, M, Z, ra, rb, nest, lab, tri, n)
    fig.suptitle(suptitle, fontsize=10, color=INK)
    fig.text(0.01, 0.005, "Numbers: weighted Pearson correlation ρ of the region pass flags.  Boxes: nestings derived by the static method.  –: no shared event.  n/a: a region has no event.  (n): MC events in the region.",
             fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.03, 1, 0.95)); fig.savefig(path, dpi=150); plt.close(fig)


def nestings(csv):
    v = pd.read_csv(csv); out = set()
    for c in [c for c in v.columns if c.startswith("verdict")]:
        for r in v[v[c].isin(["SUBSET", "SUPERSET", "EQUAL"])].itertuples():
            out.add((r.region_a, r.region_b))
    return out


# within each analysis
for ana, mix, sig in (("ATLAS-SUSY-2015-06", "mixture_0L", "GG_onestepCC_1600_1000_100"), ("ATLAS-SUSY-2016-07", "mixture_0L", "GG_onestepCC_1600_1000_100"),
                      ("ATLAS-SUSY-2018-22", "mixture_0L", "GG_onestepCC_2200_1200_200"), ("ATLAS-SUSY-2018-09", "mixture_SS", "Gtt_1600_600")):
    c = f"{D}/{ana}/correlations"; m, s = pd.read_csv(f"{c}/{mix}.csv"), pd.read_csv(f"{c}/{sig}.csv")
    r = list(dict.fromkeys(list(m.region_a) + list(m.region_b)))
    os.makedirs(f"{D}/{ana}/figures", exist_ok=True)
    figure(f"{D}/{ana}/figures/correlations_mixture_vs_signal.png", r[1:], r[:-1], m, s, mix, sig, nestings(f"{D}/{ana}/static/verdicts.csv"),
           f"{ana}: correlations between its own signal regions", tri=True)
    print(ana)
# zero-lepton pairs
for tag, sig in (("2015-06_vs_2016-07", "GG_onestepCC_1600_1000_100"), ("2015-06_vs_2018-22", "GG_onestepCC_2200_1200_200"), ("2016-07_vs_2018-22", "GG_onestepCC_2200_1200_200")):
    p = f"{D}/pairwise/{tag}"; m, s = pd.read_csv(f"{p}/correlations/mixture_0L.csv"), pd.read_csv(f"{p}/correlations/{sig}.csv")
    ra, rb = list(dict.fromkeys(m.region_a)), list(dict.fromkeys(m.region_b))
    os.makedirs(f"{p}/figures", exist_ok=True)
    a, b = tag.split("_vs_")
    figure(f"{p}/figures/correlations_mixture_vs_signal.png", ra, rb, m, s, "mixture_0L", sig, nestings(f"{p}/static/verdicts.csv"),
           f"ATLAS-SUSY-{a} (rows) × ATLAS-SUSY-{b} (columns)")
    print(tag)
