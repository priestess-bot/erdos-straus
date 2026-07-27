#!/usr/bin/env python3
"""Audit the pairwise-distinct primitive quotient forms p-c over odd distances."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-pressure-odd-distance-primitive-form-growth-2097152.json"
TARGET_SEED = 748_375_048_866_405_601
DEFAULT_MAX_DISTANCE = 99


def run_audit(payload: dict[str, object], max_distance: int = DEFAULT_MAX_DISTANCE) -> dict[str, object]:
    """Verify the finite instance of the general pairwise-distinct quotient-form lemma."""
    if max_distance < 1 or max_distance % 2 == 0:
        raise ValueError("max_distance must be a positive odd integer")
    row = next(row for row in payload["rows"] if int(row["prime_seed"]) == TARGET_SEED)
    prime = int(row["prime_seed"])
    coefficient = int(row["pressure_prime_coefficient"])
    if max_distance >= prime:
        raise ValueError("max_distance must be smaller than the seed prime")
    forms = []
    for distance in range(1, max_distance + 1, 2):
        base = math.gcd(prime - distance, coefficient)
        form = (coefficient // base, (prime - distance) // base)
        if math.gcd(*form) != 1 or form[0] <= 0 or form[1] <= 0:
            raise AssertionError(f"nonprimitive quotient form at c={distance}")
        forms.append((distance, base, form))
    if len({form for _, _, form in forms}) != len(forms):
        raise AssertionError("distinct odd distances unexpectedly share a quotient form")
    return {
        "arithmetic": (
            "for p(t)=p0+P*t, ell_c(t)=(p(t)-c)/gcd(p0-c,P) is primitive; equality "
            "of two such affine forms forces equal gcd normalizers and then equal distances"
        ),
        "scope_note": (
            "This proves only a limitation of the one-prime quotient compilation used by "
            "the bounded even-source escape audits. It does not preclude a different proof "
            "controlling unbounded distances without requiring every ell_c to be prime."
        ),
        "seed_prime": prime,
        "maximum_odd_distance": max_distance,
        "odd_distance_count": len(forms),
        "all_quotient_forms_primitive": True,
        "all_quotient_forms_pairwise_distinct": True,
        "rows": [
            {"distance": distance, "base_factor": base, "coefficient": form[0], "constant": form[1]}
            for distance, base, form in forms
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--max-distance", type=int, default=DEFAULT_MAX_DISTANCE)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload, args.max_distance)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "rows"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
