#!/usr/bin/env python3
"""Exact modulus and transversal-entropy data for canonical Type II fans."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-canonical-fan-geometry-results.json"
CANONICAL_SCRIPT = ROOT / "reproductions" / "type_ii_canonical_ray.py"


def load_canonical_script():
    spec = importlib.util.spec_from_file_location(
        "type_ii_canonical_ray", CANONICAL_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_canonical_ray.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


canonical = load_canonical_script()


def euler_phi(value: int) -> int:
    result = value
    remaining = value
    factor = 2
    while factor * factor <= remaining:
        if remaining % factor == 0:
            result -= result // factor
            while remaining % factor == 0:
                remaining //= factor
        factor = 3 if factor == 2 else factor + 2
    if remaining > 1:
        result -= result // remaining
    return result


def lcm_through(limit: int) -> int:
    result = 1
    for value in range(1, limit + 1):
        result = math.lcm(result, value)
    return result


def fan_geometry(shift_bound: int) -> dict[str, object]:
    if shift_bound < 2:
        raise ValueError("shift_bound must be at least two")
    combined_modulus = 24
    total_phi = 0
    rows = []
    for shift in range(1, shift_bound + 1):
        a, c = canonical.canonical_pair(shift)
        modulus = 4 * a * c
        if (4 * shift) % modulus:
            raise AssertionError("canonical ray modulus must divide 4*s")
        combined_modulus = math.lcm(combined_modulus, modulus)
        phi = euler_phi(modulus)
        total_phi += phi
        rows.append(
            {
                "shift": shift,
                "a": a,
                "c": c,
                "modulus": modulus,
                "phi": phi,
            }
        )
    lcm_bound = lcm_through(4 * shift_bound)
    if lcm_bound % combined_modulus:
        raise AssertionError("fan modulus must divide lcm(1,...,4H)")
    return {
        "shift_bound": shift_bound,
        "combined_modulus": str(combined_modulus),
        "combined_modulus_digits": len(str(combined_modulus)),
        "lcm_through_4h": str(lcm_bound),
        "modulus_divides_lcm_through_4h": True,
        "sum_phi": total_phi,
        "transversal_choice_log2_upper_bound": total_phi // 2,
        "coarse_transversal_choice_log2_upper_bound": shift_bound
        * (shift_bound + 1),
        "rows": rows,
    }


def run_report(bounds: tuple[int, ...]) -> dict[str, object]:
    if not bounds or any(bound < 2 for bound in bounds):
        raise ValueError("all shift bounds must be at least two")
    geometries = [fan_geometry(bound) for bound in bounds]
    return {
        "arithmetic": (
            "exact canonical factorizations, integer lcms, and Euler phi values"
        ),
        "scope_note": (
            "These are combinatorial inputs for a possible uniform sieve. They do "
            "not by themselves supply a growing-shift coverage theorem."
        ),
        "geometries": geometries,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bounds", type=int, nargs="+", default=[14, 50, 100])
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_report(tuple(args.bounds))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
