#!/usr/bin/env python3
"""Measure exponent deficits of finite-product tail obstructions."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
OBSTRUCTION_INPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-tail-obstruction-1b-results.json"
EXPONENT_SCRIPT = ROOT / "reproductions" / "type_ii_h19_fourth_even_source_exponent_profile.py"
DEFAULT_POWER_CAP = 9
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-finite-product-exponent-1b-results.json"


def load_exponent_module():
    spec = importlib.util.spec_from_file_location(
        "bounded_r_finite_product_exponent", EXPONENT_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {EXPONENT_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


exponent = load_exponent_module()


def first_cover_power(
    modulus: int, factors: dict[int, int], target: int, power_cap: int
) -> int | None:
    for power in range(3, power_cap + 1):
        if target in exponent.divisor_residues(modulus, factors, power):
            return power
    return None


def run_audit(payload: dict[str, object], power_cap: int = DEFAULT_POWER_CAP) -> dict[str, object]:
    """Find first residue entrance above the square tail for every finite-product state."""
    if power_cap < 3:
        raise ValueError("power cap must be at least three")
    records = []
    for row in payload["records"]:
        prime = int(row["prime"])
        for state in row["states"]:
            if state["classification"] != "finite-product-set":
                continue
            r = int(state["r"])
            m = (r * prime + 1) // 4
            factors = {int(q): int(e) for q, e in sympy.factorint(m).items()}
            first_power = first_cover_power(
                r, factors, int(state["target_residue"]), power_cap
            )
            records.append(
                {
                    "prime": prime,
                    "r": r,
                    "m_factorization": {
                        str(q): e for q, e in sorted(factors.items())
                    },
                    "first_cover_power_through_cap": first_power,
                }
            )
    histogram = Counter(
        str(record["first_cover_power_through_cap"])
        if record["first_cover_power_through_cap"] is not None
        else f">{power_cap}"
        for record in records
    )
    return {
        "arithmetic": (
            "exact factorization of M=(r*p+1)/4 and exhaustive residue sets of "
            "all divisors of M to powers three through the requested cap"
        ),
        "scope_note": (
            "This records residue entrance, not a new square-tail certificate: "
            "the original descent only permits divisors of M squared."
        ),
        "prime_limit": payload["prime_limit"],
        "r_cap": payload["r_cap"],
        "power_cap": power_cap,
        "finite_product_state_count": len(records),
        "first_cover_power_histogram": dict(sorted(histogram.items())),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=OBSTRUCTION_INPUT)
    parser.add_argument("--power-cap", type=int, default=DEFAULT_POWER_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload, args.power_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
