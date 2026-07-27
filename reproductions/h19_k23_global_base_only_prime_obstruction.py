#!/usr/bin/env python3
"""Lift every finite global-base pressure seed to a prime-parameter obstruction."""

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
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-global-tail-base-only-descent-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-global-base-only-prime-obstruction-2097152.json"
GLOBAL_CLOSURE = ROOT / "reproductions" / "h19_k23_full_global_tail_closure.py"
BRANCHES = ROOT / "reproductions" / "mixed_factor_h19_uniform_affine_boundary.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


global_closure = load_module("h19_k23_global_base_prime_menu", GLOBAL_CLOSURE)
boundary = load_module("h19_k23_global_base_prime_branches", BRANCHES)


def valuation(value: int, prime: int) -> int:
    """Return the exact prime-adic valuation of a positive integer."""
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def base_only_residue_divisor(
    prime: int, gap: int, base_primes: set[int], require_size_bound: bool
) -> int | None:
    """Return the least base divisor in the target residue, optionally with d<=x."""
    q, remainder = divmod(gap + 1, 4)
    if remainder or (prime - 1) % (gap + 1):
        raise ValueError("not an ordinary global Type II tail")
    u = (prime + gap) // (gap + 1)
    x = q * u
    values = [1]
    for factor in sorted(base_primes):
        exponent = valuation(x, factor)
        values = [
            value * factor**power
            for value in values
            for power in range(2 * exponent + 1)
        ]
    target = (-x) % gap
    candidates = [divisor for divisor in values if divisor % gap == target]
    if require_size_bound:
        candidates = [divisor for divisor in candidates if divisor <= x]
    return min(candidates) if candidates else None


def branch_parameter(
    prime: int, forms: dict[int, tuple[int, int]]
) -> tuple[int, int, int, int]:
    """Recover the unique residual branch and nonnegative parameter of a seed."""
    matches = [
        (residue, coefficient, constant, (prime - constant) // coefficient)
        for residue, (coefficient, constant) in forms.items()
        if prime >= constant and (prime - constant) % coefficient == 0
    ]
    if len(matches) != 1:
        raise AssertionError("pressure seed is not on exactly one residual branch")
    return matches[0]


def period_for_seed(
    prime: int, bases: dict[int, set[int]]
) -> tuple[int, list[dict[str, object]]]:
    """Freeze every target residue and every canonical-base valuation."""
    period = math.lcm(*bases)
    rows = []
    for gap, base_primes in sorted(bases.items()):
        u = (prime + gap) // (gap + 1)
        valuations = {str(factor): valuation(u, factor) for factor in sorted(base_primes)}
        for factor, exponent in valuations.items():
            period = math.lcm(period, int(factor) ** (int(exponent) + 1))
        rows.append(
            {
                "tail_gap": gap,
                "base_primes": sorted(base_primes),
                "u_base_valuations": valuations,
            }
        )
    return period, rows


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Construct primitive prime progressions preserving every base-only miss."""
    global_factor, bases = global_closure.global_tail_bases()
    forms = {
        int(branch["v_mod_29"]): (
            int(branch["prime_form"]["coefficient"]),
            int(branch["prime_form"]["constant"]),
        )
        for branch in boundary.remaining_branches()
    }
    all_gaps = sorted(bases)
    families = []
    for record in payload["global_base_only_pressure_records"]:
        prime = int(record["prime"])
        residue, coefficient, constant, parameter = branch_parameter(prime, forms)
        if any(
            base_only_residue_divisor(prime, gap, bases[gap], False) is not None
            for gap in all_gaps
        ):
            raise AssertionError(
                "pressure seed has a target-residue base divisor before the size bound"
            )
        period, valuation_rows = period_for_seed(prime, bases)
        for row in valuation_rows:
            gap = int(row["tail_gap"])
            if period % gap:
                raise AssertionError("period does not freeze a Type II target residue")
            slope = coefficient // (gap + 1)
            original_u = (prime + gap) // (gap + 1)
            shifted_u = original_u + slope * period
            for factor, exponent in row["u_base_valuations"].items():
                factor = int(factor)
                exponent = int(exponent)
                if (slope * period) % factor ** (exponent + 1):
                    raise AssertionError("period does not freeze a base valuation")
                if valuation(shifted_u, factor) != exponent:
                    raise AssertionError("base valuation changed under the period")
        shifted_prime = coefficient * (parameter + period) + constant
        shifted_misses = [
            gap
            for gap in all_gaps
            if base_only_residue_divisor(
                shifted_prime, gap, bases[gap], False
            )
            is None
        ]
        if shifted_misses != all_gaps:
            raise AssertionError("valuation-freezing period changed a base-only state")
        progression_step = coefficient * period
        if math.gcd(progression_step, prime) != 1:
            raise AssertionError("Dirichlet progression is not primitive")
        if prime % 24 != 1 or progression_step % 24:
            raise AssertionError("prime progression left the core-prime congruence class")
        families.append(
            {
                "prime_seed": prime,
                "branch_v_mod_29": residue,
                "parameter_seed": parameter,
                "parameter_period": period,
                "prime_progression_offset": prime,
                "prime_progression_step": progression_step,
                "prime_progression_gcd": math.gcd(progression_step, prime),
                "core_prime_residue_mod_24": prime % 24,
                "canonical_base_only_miss_gaps": all_gaps,
                "unit_shift_base_only_miss_gaps": shifted_misses,
                "valuation_constraints": valuation_rows,
            }
        )
    if len(families) != int(payload["global_base_only_pressure_count"]):
        raise AssertionError("not every pressure seed lifted to a progression")
    return {
        "arithmetic": (
            "for each global tail, the Type II target is fixed by t modulo its gap, "
            "while the canonical base-only divisor set is fixed by the valuations of "
            "u=(p+m)/(m+1) at its finitely many base primes. Taking the least common "
            "multiple of all gaps and ell^(v_ell(u)+1) freezes both data. Exact "
            "base-only divisor enumeration finds no divisor in the target residue even "
            "before applying d<=x, so the miss holds for every period translate; the "
            "primitive affine p progression then has infinitely many prime terms by "
            "Dirichlet's theorem"
        ),
        "scope_note": (
            "An infinite prime-parameter obstruction to canonical base-only global-tail "
            "certificates. It does not exclude a certificate using an adaptive nonbase "
            "factor, nor does it disprove the Erdos-Straus conjecture."
        ),
        "input_parameter_limit_exclusive": payload["input_parameter_limit_exclusive"],
        "global_p_minus_one_factor": global_factor,
        "global_tail_count": len(bases),
        "prime_progression_family_count": len(families),
        "families": families,
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
            {key: value for key, value in result.items() if key != "families"},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
