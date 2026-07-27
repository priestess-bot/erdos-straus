#!/usr/bin/env python3
"""Seek later shifted rays certified by either structural symmetric-box layer."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
OUTER_SATURATION = ROOT / "reproductions" / "type_ii_tail_shifted_quadratic_outer_saturation_profile.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-opposite-pair-profile-200m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-outer-structural-profile-200m-results.json"
DEFAULT_OFFSET_BOUND = 202_521


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


outer_saturation = load_module("tail_shifted_outer_structural_saturation", OUTER_SATURATION)


def run_audit(payload: dict[str, object], offset_bound: int = DEFAULT_OFFSET_BOUND) -> dict[str, object]:
    if offset_bound <= 0:
        raise ValueError("offset bound must be positive")
    records_in = [
        record
        for record in payload["records"]
        if not record["symmetric_box_subgroup_saturation_witness_count"]
        and not record["inverse_pairing_parity_witness_count"]
    ]
    if not records_in:
        raise ValueError("input has no minimal-offset structural misses")
    primes = [int(record["prime"]) for record in records_in]
    spf = outer_saturation.opposite_profile.square_audit.targeted_descent.TrialSmallestFactors(max(primes))
    records = []
    for record in records_in:
        prime = int(record["prime"])
        minimal_offset = int(record["minimal_offset"])
        witness, candidates = outer_saturation.first_later_structural_witness(
            prime, minimal_offset, spf, offset_bound
        )
        records.append(
            {
                "prime": prime,
                "minimal_offset_without_structural_certificate": minimal_offset,
                "later_structural_certificate": witness,
                "candidate_pairs_examined_after_minimal_offset": candidates,
            }
        )
    misses = [record["prime"] for record in records if record["later_structural_certificate"] is None]
    mechanism_counts: dict[str, int] = {}
    for record in records:
        witness = record["later_structural_certificate"]
        if witness is not None:
            mechanism = str(witness["mechanism"])
            mechanism_counts[mechanism] = mechanism_counts.get(mechanism, 0) + 1
    return {
        "arithmetic": (
            "for each minimal-offset miss of both structural layers, exact enumeration of every "
            "compatible k at every later shift through the stated bound; saturation or "
            "inverse-pairing-parity hits are followed by verified tail descent construction"
        ),
        "scope_note": (
            "This is a finite later-offset selector audit. A miss does not rule out shifted "
            "quadratic descent or either mechanism at offsets beyond the stated bound."
        ),
        "prime_limit": payload["prime_limit"],
        "input_minimal_structural_miss_count": len(records),
        "offset_bound": offset_bound,
        "later_structural_certificate_count": len(records) - len(misses),
        "later_structural_mechanism_counts": mechanism_counts,
        "later_structural_miss_primes": misses,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--offset-bound", type=int, default=DEFAULT_OFFSET_BOUND)
    args = parser.parse_args()
    result = run_audit(json.loads(args.input.read_text(encoding="utf-8")), args.offset_bound)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
