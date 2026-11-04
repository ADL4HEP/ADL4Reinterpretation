"""Region-pair overlaps from the acceptance tables of the overlap branch.

For every pair of regions (a, b) and every sample (or background mixture):
  n_a, n_b, n_ab      unweighted event counts (n_ab: events passing both)
  sigma_a, sigma_b, sigma_ab   weighted sums of the event weights [pb for backgrounds]
  kappa  = sigma_ab / sqrt(sigma_a sigma_b)     correlation of the observed counts
  rho    = weighted Pearson correlation of the pass flags
  jaccard = sigma_ab / (sigma_a + sigma_b - sigma_ab)
  *_err  = standard deviation over 200 bootstrap replicas (each event reweighted by Poisson(1))
Mixtures: union of the samples with their weights (sigma_slice / N_slice):
  mixture_0L = Znunu + Wlnu + ttbar + ZV (background of the zero-lepton analyses; Wlnu, ttbar enter via lost leptons), mixture_SS = ttW_SS + ttZ_ll, mixture_all = all six.
usage: python3 compute_overlap.py <overlap dir>"""
import sys, os, itertools, glob
import numpy as np, pandas as pd

D = sys.argv[1]
ANAS = ["ATLAS-SUSY-2015-06", "ATLAS-SUSY-2016-07", "ATLAS-SUSY-2018-22", "ATLAS-SUSY-2018-09"]
SAMPLES = ["Znunu", "Wlnu", "ttbar", "ZV", "ttW_SS", "ttZ_ll", "GG_onestepCC_1600_1000_100", "GG_onestepCC_2200_1200_200", "Gtt_1600_600"]
MIX = {"mixture_0L": ["Znunu", "Wlnu", "ttbar", "ZV"], "mixture_SS": ["ttW_SS", "ttZ_ll"],
       "mixture_all": ["Znunu", "Wlnu", "ttbar", "ZV", "ttW_SS", "ttZ_ll"]}
NBOOT, SEED = 200, 12345
KEYS = ["sample", "slice", "event", "weight"]


def load(ana, sample):
    return pd.read_csv(f"{D}/{ana}/acceptance/{sample}.csv.gz")


def table(anas, samples):
    """flags of the regions of `anas` side by side, for the union of `samples`"""
    parts = []
    for s in samples:
        dfs = [load(a, s) for a in anas]
        for x in dfs[1:]:
            assert (x[KEYS[:3]].values == dfs[0][KEYS[:3]].values).all()
        parts.append(pd.concat([dfs[0][KEYS]] + [x.drop(columns=KEYS) for x in dfs], axis=1))
    return pd.concat(parts, ignore_index=True)


def stats(F, w):
    S = F.T @ w; S2 = (F * w[:, None]).T @ F; W = w.sum()
    p = S / W; pab = S2 / W
    with np.errstate(divide="ignore", invalid="ignore"):
        kappa = S2 / np.sqrt(np.outer(S, S))
        rho = (pab - np.outer(p, p)) / np.sqrt(np.outer(p * (1 - p), p * (1 - p)))
        jac = S2 / (S[:, None] + S[None, :] - S2)
    return S, S2, kappa, rho, jac


def pairs_table(df, regs_a, regs_b, same):
    F = df[regs_a + regs_b if not same else regs_a].to_numpy(np.float64)
    w = df.weight.to_numpy(np.float64)
    S, S2, kappa, rho, jac = stats(F, w)
    N = F.T @ F
    rng = np.random.default_rng(SEED); boots = []
    for _ in range(NBOOT):
        wb = w * rng.poisson(1.0, len(w))
        boots.append(np.stack(stats(F, wb)[2:]))
    err = np.nanstd(np.array(boots), axis=0)
    ia = range(len(regs_a)); ib = range(len(regs_a)) if same else range(len(regs_a), len(regs_a) + len(regs_b))
    names = regs_a if same else regs_a + regs_b
    rows = []
    for i in ia:
        for j in ib:
            if same and j <= i: continue
            rows.append(dict(region_a=names[i], region_b=names[j], n_a=int(N[i, i]), n_b=int(N[j, j]), n_ab=int(N[i, j]),
                             sigma_a=S[i], sigma_b=S[j], sigma_ab=S2[i, j],
                             kappa=kappa[i, j], kappa_err=err[0, i, j], rho=rho[i, j], rho_err=err[1, i, j],
                             jaccard=jac[i, j], jaccard_err=err[2, i, j]))
    return pd.DataFrame(rows)


def regions(ana):
    return [c for c in load(ana, "ZV").columns if c not in KEYS]


targets = {**{s: [s] for s in SAMPLES}, **MIX}
for ana in ANAS:
    os.makedirs(f"{D}/{ana}/correlations", exist_ok=True)
    for name, smp in targets.items():
        df = table([ana], smp)
        pairs_table(df, regions(ana), [], True).to_csv(f"{D}/{ana}/correlations/{name}.csv", index=False, float_format="%.6g")
    print("within", ana)
for a, b in itertools.combinations(ANAS, 2):
    tag = f"{a.replace('ATLAS-SUSY-', '')}_vs_{b.replace('ATLAS-SUSY-', '')}"
    os.makedirs(f"{D}/pairwise/{tag}/correlations", exist_ok=True)
    for name, smp in targets.items():
        df = table([a, b], smp)
        pairs_table(df, regions(a), regions(b), False).to_csv(f"{D}/pairwise/{tag}/correlations/{name}.csv", index=False, float_format="%.6g")
    print("pair", tag)
