#!/usr/bin/env python3
"""
make_analyses_json.py -- build the HEPData `analyses.json` for ADL/CutLang.

HEPData asks every public reinterpretation tool to publish a JSON file saying
which analyses it implements and where those implementations live, following

    https://github.com/HEPData/hepdata/tree/main/hepdata/templates/analyses_schema/1.0.0

This script walks an ADL analysis repository (by default the one it sits in),
reads the `info analysis` block out of each .adl file, merges it with the
hand-maintained metadata in analyses_meta.yml, resolves any missing INSPIRE IDs
through the INSPIRE REST API, and writes a schema-valid analyses.json.

Usage
-----
    python3 make_analyses_json.py                      # write ./analyses.json
    python3 make_analyses_json.py --check              # verify it is up to date
    python3 make_analyses_json.py --repo /path/to/repo --out /tmp/a.json
    python3 make_analyses_json.py --offline            # never touch the network

Dependencies: pyyaml, jsonschema (validation is skipped with a warning if
jsonschema is missing).
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
import urllib.request
from pathlib import Path

import yaml

SCHEMA_VERSION = "1.0.0"
SCHEMA_URL = (
    "https://raw.githubusercontent.com/HEPData/hepdata/main/"
    "hepdata/templates/analyses_schema/1.0.0/analyses_schema.json"
)
INSPIRE_API = "https://inspirehep.net/api/arxiv/{arxiv_id}"

# Keys we know how to read out of an ADL `info analysis` block.
INFO_KEYS = (
    "title",
    "experiment",
    "id",
    "publication",
    "sqrtS",
    "sqrts",
    "lumi",
    "arXiv",
    "arxiv",
    "hepdata",
    "doi",
    "authors",
    "adlauthor",
)
_INFO_RE = re.compile(
    r"^\s*(?:#\s*)?(" + "|".join(INFO_KEYS) + r")\s+(.+?)\s*$",
    re.IGNORECASE,
)
_ANALYSIS_DIR_RE = re.compile(r"^(ATLAS|CMS)-[A-Z0-9]+-\d{2,4}-\d+$")


# --------------------------------------------------------------------------- #
# reading the ADL files
# --------------------------------------------------------------------------- #
def read_adl_info(path: Path) -> dict:
    """Pull the `info analysis` fields out of an ADL file.

    ADL info blocks are frequently commented out with '#', so leading comment
    markers are stripped before matching. Only the header of the file is read:
    parsing stops at the first real block statement so that e.g. a `table`
    column called 'doi' can never be picked up by accident.
    """
    info: dict[str, str] = {}
    for line in path.read_text(errors="replace").splitlines():
        bare = line.lstrip("# \t")
        if re.match(r"^(object|region|algo|define|table|composite|countsformat)\b",
                    bare, re.IGNORECASE):
            break
        m = _INFO_RE.match(line)
        if m:
            key, val = m.group(1).lower(), m.group(2).strip()
            if key == "sqrts":
                key = "sqrts"
            if key == "arxiv":
                key = "arxiv"
            info.setdefault(key, val.strip('"').strip())
    return info


def is_auxiliary(stem: str, suffixes: list[str]) -> bool:
    return any(stem.endswith(s) for s in suffixes)


# --------------------------------------------------------------------------- #
# INSPIRE lookup
# --------------------------------------------------------------------------- #
def resolve_inspire_id(arxiv_id: str, offline: bool = False) -> int | None:
    """Return the INSPIRE control number for an arXiv identifier."""
    if offline or not arxiv_id:
        return None
    url = INSPIRE_API.format(arxiv_id=arxiv_id)
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "ADL-CutLang-analyses-json/1.0"}
        )
        with urllib.request.urlopen(req, timeout=30) as fh:
            payload = json.load(fh)
        return int(payload["metadata"]["control_number"])
    except Exception as exc:  # noqa: BLE001 - the caller decides what to do
        print(f"  ! INSPIRE lookup failed for arXiv:{arxiv_id}: {exc}",
              file=sys.stderr)
        return None


# --------------------------------------------------------------------------- #
# building the document
# --------------------------------------------------------------------------- #
def build(repo: Path, meta: dict, offline: bool = False,
          fixed_date: str | None = None) -> tuple[dict, dict]:
    repo_meta = meta["repository"]
    aux = meta.get("auxiliary_suffixes", [])
    base = f"https://github.com/{repo_meta['owner']}/{repo_meta['name']}"

    url_templates = {
        "main_url": f"{base}/blob/{repo_meta['main_branch']}/{{path}}/{{name}}.adl",
        "val_url": f"{base}/tree/{repo_meta['validation_branch']}/{{path}}",
        # Non-standard extras: the schema explicitly allows additional fields,
        # and SModelS publishes the same two.
        "publication": "https://doi.org/{publication_doi}",
        "arXiv": "https://arxiv.org/abs/{arXiv_id}",
    }

    analyses = []
    resolved: dict[str, int] = {}

    for folder in sorted(p for p in repo.iterdir()
                         if p.is_dir() and _ANALYSIS_DIR_RE.match(p.name)):
        adl_files = sorted(folder.glob("*.adl"))
        if not adl_files:
            print(f"  - {folder.name}: no .adl files, skipped")
            continue

        entry_meta = (meta.get("analyses") or {}).get(folder.name)
        if entry_meta is None:
            print(f"  ! {folder.name}: not listed in analyses_meta.yml, skipped",
                  file=sys.stderr)
            continue

        # merge the info blocks of all ADL files of this analysis
        info: dict[str, str] = {}
        for f in adl_files:
            for k, v in read_adl_info(f).items():
                info.setdefault(k, v)

        implementations = [
            {"name": f.stem, "path": folder.name}
            for f in adl_files
            if not is_auxiliary(f.stem, aux)
        ]
        if not implementations:  # every file was auxiliary: list them all
            implementations = [{"name": f.stem, "path": folder.name}
                               for f in adl_files]

        arxiv_id = str(entry_meta.get("arxiv_id") or info.get("arxiv") or "").strip()
        inspire_id = entry_meta.get("inspire_id")
        if not inspire_id:
            print(f"  . {folder.name}: resolving INSPIRE ID from arXiv:{arxiv_id}")
            inspire_id = resolve_inspire_id(arxiv_id, offline=offline)
            if inspire_id:
                resolved[folder.name] = inspire_id
            else:
                print(f"  ! {folder.name}: no INSPIRE ID -- analysis omitted",
                      file=sys.stderr)
                continue

        entry = {
            "inspire_id": int(inspire_id),
            "ana_id": folder.name,
            "implementations": implementations,
        }
        if entry_meta.get("pretty_name"):
            entry["pretty_name"] = str(entry_meta["pretty_name"]).strip()
        if entry_meta.get("signature_type"):
            entry["signature_type"] = entry_meta["signature_type"]
        doi = entry_meta.get("publication_doi") or info.get("doi")
        if doi:
            entry["publication_doi"] = str(doi).replace("https://doi.org/", "")
        if arxiv_id:
            entry["arXiv_id"] = arxiv_id
        if info.get("title"):
            entry["title"] = info["title"]
        if entry_meta.get("title"):  # override a paraphrased ADL title
            entry["title"] = str(entry_meta["title"]).strip()
        if info.get("experiment"):
            entry["experiment"] = info["experiment"]
        analyses.append(entry)
        print(f"  + {folder.name}: {len(implementations)} implementation(s), "
              f"INSPIRE {inspire_id}")

    date = fixed_date or _dt.datetime.now(_dt.timezone.utc).isoformat(
        timespec="seconds")

    doc = {
        "schema_version": SCHEMA_VERSION,
        "tool": meta["tool"]["name"],
        "version": str(meta["tool"]["version"]),
        "date_created": date,
        "implementations_description":
            meta["tool"]["implementations_description"].strip(),
        "link_types": list(url_templates),
        "url_templates": url_templates,
        "analyses": analyses,
    }
    if meta.get("license"):
        doc["implementations_license"] = {
            "name": meta["license"]["name"],
            "url": meta["license"]["url"],
        }
    return doc, resolved


# --------------------------------------------------------------------------- #
# validation
# --------------------------------------------------------------------------- #
def validate(doc: dict, schema_path: Path | None, offline: bool) -> bool:
    try:
        import jsonschema
    except ImportError:
        print("! jsonschema not installed -- skipping validation", file=sys.stderr)
        return True

    schema = None
    if schema_path and schema_path.exists():
        schema = json.loads(schema_path.read_text())
    elif not offline:
        try:
            with urllib.request.urlopen(SCHEMA_URL, timeout=30) as fh:
                schema = json.load(fh)
        except Exception as exc:  # noqa: BLE001
            print(f"! could not fetch schema: {exc}", file=sys.stderr)
    if schema is None:
        print("! no schema available -- skipping validation", file=sys.stderr)
        return True

    jsonschema.validate(instance=doc, schema=schema)
    print("validation: OK against analyses_schema 1.0.0")
    return True


# --------------------------------------------------------------------------- #
def main() -> int:
    here = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", type=Path, default=here,
                    help="root of the ADL analysis repository (default: script dir)")
    ap.add_argument("--meta", type=Path, default=here / "analyses_meta.yml")
    ap.add_argument("--out", type=Path, default=here / "analyses.json")
    ap.add_argument("--schema", type=Path, default=here / "analyses_schema.json",
                    help="local copy of the HEPData schema (optional)")
    ap.add_argument("--offline", action="store_true",
                    help="never contact INSPIRE or fetch the schema")
    ap.add_argument("--check", action="store_true",
                    help="exit non-zero if the file on disk is out of date")
    ap.add_argument("--date", default=None,
                    help="fix date_created (RFC 3339); used by --check")
    args = ap.parse_args()

    meta = yaml.safe_load(args.meta.read_text())

    print(f"scanning {args.repo}")
    fixed = args.date
    if args.check and args.out.exists() and not fixed:
        try:
            fixed = json.loads(args.out.read_text())["date_created"]
        except Exception:  # noqa: BLE001
            fixed = None

    doc, resolved = build(args.repo, meta, offline=args.offline, fixed_date=fixed)

    if not doc["analyses"]:
        print("! no analyses collected -- refusing to write", file=sys.stderr)
        return 2

    validate(doc, args.schema, args.offline)

    rendered = json.dumps(doc, indent=2, ensure_ascii=False) + "\n"

    if args.check:
        current = args.out.read_text() if args.out.exists() else ""
        if current != rendered:
            print("! analyses.json is out of date -- re-run without --check",
                  file=sys.stderr)
            return 1
        print("analyses.json is up to date")
        return 0

    args.out.write_text(rendered)
    print(f"wrote {args.out} ({len(doc['analyses'])} analyses, "
          f"{sum(len(a['implementations']) for a in doc['analyses'])} implementations)")

    # write newly resolved INSPIRE IDs back into the metadata file
    if resolved:
        text = args.meta.read_text()
        for folder, iid in resolved.items():
            text = re.sub(
                rf"(^  {re.escape(folder)}:\n(?:.*\n)*?    inspire_id:)\s*$",
                rf"\1 {iid}",
                text,
                flags=re.MULTILINE,
            )
        args.meta.write_text(text)
        print(f"cached INSPIRE IDs for: {', '.join(resolved)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
