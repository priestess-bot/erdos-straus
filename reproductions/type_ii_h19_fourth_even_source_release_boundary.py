#!/usr/bin/env python3
"""Locate the first odd-distance even-source descent for the 1b H19 outlier."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ADAPTIVE_SCRIPT = ROOT / "reproductions" / "type_ii_h19_adaptive_even_source_descent.py"
PRIME = 640_775_689
FIRST_DISTANCE = 34_091
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-ii-h19-fourth-even-source-release-640775689-results.json"
)


def load_adaptive_script():
    spec = importlib.util.spec_from_file_location(
        "type_ii_h19_fourth_even_source_adaptive", ADAPTIVE_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_h19_adaptive_even_source_descent.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


adaptive = load_adaptive_script()


def run_audit(distance_cap: int = FIRST_DISTANCE) -> dict[str, object]:
    """Exhaustively scan the complete odd-distance fan through the given cap."""
    if distance_cap < 1 or distance_cap % 2 == 0:
        raise ValueError("distance cap must be a positive odd integer")
    spf = adaptive.targeted.TrialSmallestFactors(PRIME)
    first = None
    for distance in range(1, distance_cap + 1, 2):
        witness = adaptive.short_certificate.even_source_distance_descent_witness(
            PRIME, distance, spf
        )
        if witness is None:
            continue
        adaptive.verify_witness(PRIME, distance, witness)
        first = {
            "distance": distance,
            "source_denominator": witness.source_denominator,
            "k": witness.k,
            "q": witness.q,
            "factor": witness.factor,
            "source_solution": list(witness.source_solution),
            "target_solution": list(witness.target_solution),
            "certificate": {
                "type": witness.certificate.certificate_type,
                "gap": witness.certificate.gap,
                "x": witness.certificate.x,
                "divisor": witness.certificate.divisor,
                "y": witness.certificate.y,
                "z": witness.certificate.z,
            },
        }
        break
    return {
        "arithmetic": (
            "exact trial-prime factorization for every odd distance in the "
            "complete even-source fan, with exact rational lift checks"
        ),
        "scope_note": (
            "This establishes the first hit only for the named finite prime "
            "and finite odd-distance fan; it is not a universal bound."
        ),
        "prime": PRIME,
        "scanned_odd_distances_through": distance_cap,
        "first_strict_descent": first,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--distance-cap", type=int, default=FIRST_DISTANCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(args.distance_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
