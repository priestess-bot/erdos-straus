#!/usr/bin/env python3
"""Show that the 28 variable-even-scale misses are residue, not size, obstructions."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
VARIABLE = ROOT / "reproductions" / "type-i-h19-variable-even-scale-after-k6-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-h19-variable-even-scale-residue-boundary-1b-results.json"


def divisors(factors: dict[int, int]) -> list[int]:
    result = [1]
    for factor, exponent in factors.items():
        result = [value * factor**power for value in result for power in range(exponent + 1)]
    return sorted(result)


def run_audit(variable: dict[str, object]) -> dict[str, object]:
    misses = variable["variable_even_scale_misses"]
    if len(misses) != 28:
        raise AssertionError("input is not the exact 28-point variable-scale boundary")
    profiles = []
    for entry in misses:
        prime = int(entry["prime"])
        scales = [int(value) for value in entry["eligible_even_scales"]]
        scale_profiles = []
        for k in scales:
            q = 4 * k - 1
            source = (q * prime + 1) // (4 * k)
            if 4 * k * source != q * prime + 1 or source % 2:
                raise AssertionError("input scale was not an integral even source")
            factors = {int(factor): int(exponent) for factor, exponent in sympy.factorint(k * source).items()}
            all_divisors = divisors(factors)
            hits = [g for g in all_divisors if g % q == q - 1]
            if hits:
                raise AssertionError("a supposedly complete variable-scale miss had an unrestricted residue hit")
            scale_profiles.append(
                {
                    "k": k,
                    "q": q,
                    "source_denominator": source,
                    "divisor_count": len(all_divisors),
                    "residue_minus_one_divisor_count": len(hits),
                }
            )
        profiles.append({"prime": prime, "scale_count": len(scale_profiles), "scales": scale_profiles})
    return {
        "arithmetic": (
            "for every residual prime and every integral even affine scale k|(p-1)/4, enumerate all "
            "positive divisors g|kn without the terminal size condition, and test g=-1 (mod 4k-1)"
        ),
        "scope_note": (
            "The result isolates the obstruction inside the same finite terminal affine mixed-factor family: "
            "all its misses fail the required residue before the bound g<=n is imposed."
        ),
        "input_variable_even_scale_miss_count": len(profiles),
        "all_scale_profiles": sum(profile["scale_count"] for profile in profiles),
        "unrestricted_residue_hit_count": sum(
            scale["residue_minus_one_divisor_count"]
            for profile in profiles
            for scale in profile["scales"]
        ),
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--variable", type=Path, default=VARIABLE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.variable.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "profiles"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
