#!/usr/bin/env python3
"""Find two forbidden first-power residue factors at every global pressure tail."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-global-base-only-prime-obstruction-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-global-first-power-forbidden-pair-boundary-2097152.json"
GLOBAL_CLOSURE = ROOT / "reproductions" / "h19_k23_full_global_tail_closure.py"
BASE_OBSTRUCTION = ROOT / "reproductions" / "h19_k23_global_base_only_prime_obstruction.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


global_closure = load_module("h19_k23_forbidden_pair_global", GLOBAL_CLOSURE)
base_obstruction = load_module(
    "h19_k23_forbidden_pair_base_obstruction", BASE_OBSTRUCTION
)


def base_divisor_residues(x: int, gap: int, base_primes: set[int]) -> set[int]:
    """Enumerate all canonical base-only divisor residues of x squared."""
    values = [1]
    for prime in sorted(base_primes):
        exponent = base_obstruction.valuation(x, prime)
        values = [
            value * prime**power
            for value in values
            for power in range(2 * exponent + 1)
        ]
    residues = {value % gap for value in values}
    if any(math.gcd(value, gap) != 1 for value in residues):
        raise AssertionError("a Type II base divisor residue is not a unit")
    return residues


def forbidden_pair(
    prime: int, gap: int, base_primes: set[int]
) -> dict[str, int]:
    """Express the adaptive nonbase residue as two forbidden prime residues."""
    q = (gap + 1) // 4
    u = (prime + gap) // (gap + 1)
    x = q * u
    target = (-x) % gap
    base_residues = base_divisor_residues(x, gap, base_primes)
    allowed = {
        target * pow(residue, -1, gap) % gap
        for residue in base_residues
    }
    units = {
        residue for residue in range(1, gap) if math.gcd(residue, gap) == 1
    }
    forbidden = units - allowed
    base_part = 1
    for factor in base_primes:
        base_part *= factor ** base_obstruction.valuation(u, factor)
    nonbase = u // base_part
    if math.gcd(nonbase, gap) != 1:
        raise AssertionError("nonbase residue is not a unit")
    pairs = [
        (left, nonbase * pow(left, -1, gap) % gap)
        for left in sorted(forbidden)
        if nonbase * pow(left, -1, gap) % gap in forbidden
    ]
    if not pairs:
        raise AssertionError("total nonbase residue has no forbidden two-factor model")
    left, right = pairs[0]
    return {
        "tail_gap": gap,
        "nonbase_residue": nonbase % gap,
        "allowed_first_power_residue_count": len(allowed),
        "forbidden_first_power_residue_count": len(forbidden),
        "forbidden_pair_count": len(pairs),
        "forbidden_left_residue": left,
        "forbidden_right_residue": right,
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Construct a forbidden two-factor residue model at every pressure tail."""
    _, bases = global_closure.global_tail_bases()
    rows = []
    for family in payload["families"]:
        prime = int(family["prime_seed"])
        for gap, base_primes in sorted(bases.items()):
            row = forbidden_pair(prime, gap, base_primes)
            row["prime"] = prime
            rows.append(row)
    expected = len(payload["families"]) * len(bases)
    if len(rows) != expected:
        raise AssertionError("forbidden-pair audit did not cover every pressure tail")
    return {
        "arithmetic": (
            "for each canonical base state, exact enumeration of base divisor residues "
            "and the complete unit complement; a direct inverse lookup expresses the "
            "actual nonbase residue as a product of two first-power forbidden residues"
        ),
        "scope_note": (
            "A local residue-information boundary across all 72 tails of the finite "
            "pressure set. It does not construct compatible prime factorizations or "
            "exclude a proof using cross-tail factor correlations."
        ),
        "pressure_family_count": len(payload["families"]),
        "global_tail_count": len(bases),
        "pressure_tail_state_count": len(rows),
        "forbidden_pair_miss_count": 0,
        "minimum_forbidden_pair_count": min(
            int(row["forbidden_pair_count"]) for row in rows
        ),
        "maximum_forbidden_pair_count": max(
            int(row["forbidden_pair_count"]) for row in rows
        ),
        "unique_forbidden_pair_state_count": sum(
            int(row["forbidden_pair_count"]) == 1 for row in rows
        ),
        "rows": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {key: value for key, value in result.items() if key != "rows"},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
