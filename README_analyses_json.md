# `analyses.json` for ADL/CutLang

HEPData asks each public reinterpretation tool to publish a machine-readable list
of the analyses it implements, following the
[HEPData analyses schema 1.0.0](https://github.com/HEPData/hepdata/tree/main/hepdata/templates/analyses_schema/1.0.0).
`analyses.json` in this directory is that list for ADL/CutLang, and HEPData reads
it from:

```
https://raw.githubusercontent.com/ADL4HEP/ADL4Reinterpretation/main/analyses.json
```

It currently covers 5 analyses / 6 implementations. It is generated from the ADL
files themselves, not written by hand.

## Files

| File | Role |
|---|---|
| `analyses.json` | the generated output — do not edit by hand |
| `make_analyses_json.py` | generator: reads the ADL headers, validates against the schema |
| `analyses_meta.yml` | the only file you edit by hand |
| `analyses_schema.json` | local copy of the HEPData schema |
| `.github/workflows/analyses-json.yml` | regenerates and commits on every push to `main` |

## Adding a new analysis

1. Commit the `.adl` file(s) in a folder named after the analysis
   (`ATLAS-SUSY-YYYY-NN` or `CMS-XXX-YY-NNN`), with an `info analysis` block
   containing at least the arXiv number.
2. Add a block for it under `analyses:` in `analyses_meta.yml`:

   ```yaml
     CMS-SUS-22-001:
       inspire_id:                      # leave empty, the script fills it in
       signature_type: prompt           # or: displaced
       pretty_name: 0 lepton + jets
   ```
3. Run the generator:

   ```bash
   pip install pyyaml jsonschema
   python3 make_analyses_json.py
   ```
   It resolves the INSPIRE ID from the arXiv number, writes it back into
   `analyses_meta.yml`, and regenerates `analyses.json`.
4. Commit both files. (Or just push the ADL and let the workflow do steps 3–4.)

Other options: `--check` (exit 1 if `analyses.json` is stale, used by CI),
`--offline` (no INSPIRE lookup), `--repo PATH` (run against another repository).

## How fields are filled

Title, experiment, arXiv number and DOI come from the `info analysis` block of
the ADL file, so the ADL stays the single source of truth. `analyses_meta.yml`
supplies: INSPIRE ID, signature type, pretty name, and
overrides where an ADL header is incomplete or paraphrased.

Files ending in `_Cutflow`, `_results` or `_signals` are treated as auxiliary and
are not listed as separate implementations. The suffix list is in
`analyses_meta.yml`.

URLs are built from two templates: `main_url` points at the individual `.adl`
file on `main`, `val_url` at the analysis folder on the `validation` branch.

`tool.version` in `analyses_meta.yml` is the current CutLang release. Bump it
when CutLang makes a new one.
