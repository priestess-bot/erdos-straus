#!/usr/bin/env python3
"""Run the complete fixed-offset shifted-quadratic search for one prime."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
OFFSET_PROFILE = ROOT / "reproductions" / "type_ii_tail_shifted_quadratic_offset_profile.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


offset_profile = load_module("tail_shifted_single_offset_profile", OFFSET_PROFILE)


def run_search(prime: int, offset_bound: int) -> dict[str, object]:
    if prime % 24 != 1 or prime <= 2:
        raise ValueError("prime must be a positive p == 1 (mod 24) core candidate")
    if offset_bound <= 0:
        raise ValueError("offset bound must be positive")
    spf = offset_profile.targeted_descent.TrialSmallestFactors(prime)
    witness, shift, candidate_pairs = offset_profile.first_offset_witness(prime, spf, offset_bound)
    serialized = None
    if witness is not None:
        serialized = offset_profile.serialize_witness(witness, int(shift), candidate_pairs)
        if Fraction(4, prime) != sum(
            (Fraction(1, value) for value in witness.target_solution), Fraction()
        ):
            raise AssertionError("stored target certificate did not verify")
    return {
        "arithmetic": (
            "exact increasing fixed-offset enumeration, complete compatible k | (p-s)/4 "
            "enumeration at each s, complete square-product tail enumeration, and rational lift checks"
        ),
        "prime": prime,
        "offset_bound": offset_bound,
        "offset_descent": serialized,
        "candidate_pairs_examined": candidate_pairs,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime", type=int, required=True)
    parser.add_argument("--offset-bound", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run_search(args.prime, args.offset_bound)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
