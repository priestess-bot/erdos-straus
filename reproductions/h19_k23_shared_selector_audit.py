#!/usr/bin/env python3
"""Audit shared-divisor Type II certificates on the 14 H19-k23 residuals.

For every prime p=P*t+C in the first PARAMETER_LIMIT parameter layers, scan
the legal gaps m<=GAP_CAP.  At x=(p+m)/4 a hit requires both a nontrivial
shared divisor D|4x with D=1 (mod m), and a Type II divisor d|x^2 with
d=-x (mod m).  The shared divisor supplies the scaled-first marked descent;
the Type II divisor is independently checked as a direct certificate.

This is an exact finite audit, not a bounded-gap theorem.
"""

from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
import importlib.util
import json
import math
import os
import sys
from fractions import Fraction
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "h19-k23-shared-selector-audit.json"
MIXED_BOUNDARY_SCRIPT = ROOT / "reproductions" / "mixed_factor_h19_uniform_affine_boundary.py"
SHORT_CERTIFICATE_SCRIPT = ROOT / "reproductions" / "short_certificate.py"
PARAMETER_LIMIT = 1_024
GAP_CAP = 239


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


mixed_boundary = load_module(
    "h19_k23_shared_selector_mixed_boundary", MIXED_BOUNDARY_SCRIPT
)
short_certificate = load_module(
    "h19_k23_shared_selector_short_certificate", SHORT_CERTIFICATE_SCRIPT
)


def is_prime_64(value: int) -> bool:
    """Deterministic Miller--Rabin for every input used by this audit."""
    if not 2 <= value < 2**64:
        raise ValueError("audit primality input must be in the 64-bit range")
    for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if value == prime:
            return True
        if value % prime == 0:
            return False
    exponent = value - 1
    power = 0
    while exponent % 2 == 0:
        exponent //= 2
        power += 1
    for base in (2, 325, 9_375, 28_178, 450_775, 9_780_504, 1_795_265_022):
        reduced_base = base % value
        if reduced_base == 0:
            continue
        residue = pow(reduced_base, exponent, value)
        if residue in (1, value - 1):
            continue
        for _ in range(power - 1):
            residue = residue * residue % value
            if residue == value - 1:
                break
        else:
            return False
    return True


def factorization(value: int) -> tuple[tuple[int, int], ...]:
    """Return a complete 64-bit factorization independently checked for use."""
    factors = tuple(
        sorted((int(prime), int(power)) for prime, power in sympy.factorint(value).items())
    )
    if math.prod(prime**power for prime, power in factors) != value:
        raise AssertionError("factorization product mismatch")
    if not all(is_prime_64(prime) for prime, _ in factors):
        raise AssertionError("factorization contains a composite factor")
    return factors


def divisors(
    factors: tuple[tuple[int, int], ...], multiplier: int = 1
) -> tuple[int, ...]:
    values = [1]
    for prime, exponent in factors:
        values = [
            value * prime**power
            for value in values
            for power in range(multiplier * exponent + 1)
        ]
    return tuple(sorted(values))


def extend_by_four(
    factors: tuple[tuple[int, int], ...]
) -> tuple[tuple[int, int], ...]:
    result = dict(factors)
    result[2] = result.get(2, 0) + 2
    return tuple(sorted(result.items()))


def witness_at_gap(prime: int, gap: int) -> dict[str, object] | None:
    """Find and fully verify a shared Type II certificate at one gap."""
    x = (prime + gap) // 4
    if 4 * x != prime + gap:
        raise AssertionError("nonintegral first denominator")
    factors = factorization(x)
    shared = next(
        (
            divisor
            for divisor in divisors(extend_by_four(factors))
            if divisor > 1 and divisor % gap == 1
        ),
        None,
    )
    if shared is None:
        return None
    candidate = next(
        (
            divisor
            for divisor in divisors(factors, 2)
            if divisor % gap == (-x) % gap
        ),
        None,
    )
    if candidate is None:
        return None
    divisor = min(candidate, x * x // candidate)
    if divisor > x or x * x % divisor or (x + divisor) % gap:
        raise AssertionError("Type II complement reduction failed")
    first_scale = (shared - 1) // gap
    source_denominator = first_scale * (prime + gap) // shared
    y = prime * (x + divisor) // gap
    z = prime * (x + x * x // divisor) // gap
    certificate = short_certificate.GapCertificate(
        prime, "II", gap, x, divisor, y, z
    )
    if not short_certificate.verify_certificate(certificate):
        raise AssertionError("shared Type II certificate failed verification")
    if (
        shared * source_denominator != first_scale * (prime + gap)
        or not 2 <= source_denominator < prime
        or y % prime
        or z % prime
    ):
        raise AssertionError("shared divisor did not produce a strict source")
    source_solution = (first_scale * x, y // prime, z // prime)
    target_solution = (x, y, z)
    if (
        Fraction(4, source_denominator)
        != sum((Fraction(1, value) for value in source_solution), Fraction())
        or Fraction(4, prime)
        != sum((Fraction(1, value) for value in target_solution), Fraction())
    ):
        raise AssertionError("shared marked descent identities failed")
    return {
        "gap": gap,
        "x": x,
        "x_factorization": [
            {"prime": factor_prime, "exponent": exponent}
            for factor_prime, exponent in factors
        ],
        "shared_divisor": shared,
        "first_scale": first_scale,
        "source_denominator": source_denominator,
        "type_ii_divisor": divisor,
        "source_solution": list(source_solution),
        "target_solution": list(target_solution),
    }


def selector_witness(prime: int, gap_cap: int) -> dict[str, object] | None:
    """Return the least-gap shared Type II witness up to the requested cap."""
    for gap in range(3, min(gap_cap, prime - 2) + 1, 4):
        witness = witness_at_gap(prime, gap)
        if witness is not None:
            return witness
    return None


def compact_witness(witness: dict[str, object]) -> dict[str, int]:
    """Keep only the fields required by the ordinary two-tail closure."""
    return {
        "gap": int(witness["gap"]),
        "x": int(witness["x"]),
        "type_ii_divisor": int(witness["type_ii_divisor"]),
    }


def audit_branch(
    task: tuple[dict[str, object], int, int, bool]
) -> tuple[list[dict[str, object]], list[dict[str, int]], int, dict[int, int]]:
    """Classify one independent H19-k23 progression in a worker process."""
    branch, parameter_limit, gap_cap, compact = task
    form = branch["prime_form"]
    coefficient = int(form["coefficient"])
    constant = int(form["constant"])
    v_mod_29 = int(branch["v_mod_29"])
    records: list[dict[str, object]] = []
    misses: list[dict[str, int]] = []
    gap_histogram: Counter[int] = Counter()
    prime_count = 0
    for parameter in range(parameter_limit):
        prime = coefficient * parameter + constant
        if not is_prime_64(prime):
            continue
        prime_count += 1
        witness = selector_witness(prime, gap_cap)
        if witness is None:
            misses.append(
                {
                    "v_mod_29": v_mod_29,
                    "parameter": parameter,
                    "prime": prime,
                }
            )
            continue
        gap = int(witness["gap"])
        gap_histogram[gap] += 1
        records.append(
            {
                "v_mod_29": v_mod_29,
                "parameter": parameter,
                "prime": prime,
                "first_witness": compact_witness(witness) if compact else witness,
            }
        )
    return records, misses, prime_count, dict(gap_histogram)


def run_audit(
    parameter_limit: int = PARAMETER_LIMIT,
    gap_cap: int = GAP_CAP,
    workers: int = 1,
    compact: bool = False,
) -> dict[str, object]:
    """Classify every prime in the stated finite residual sample."""
    if parameter_limit < 1 or gap_cap < 3 or workers < 1:
        raise ValueError("parameter_limit and workers must be positive and gap_cap at least 3")
    branches = mixed_boundary.remaining_branches()
    records: list[dict[str, object]] = []
    misses: list[dict[str, int]] = []
    gap_histogram: Counter[int] = Counter()
    branch_prime_count: Counter[int] = Counter()
    tasks = [(branch, parameter_limit, gap_cap, compact) for branch in branches]
    if workers == 1:
        branch_results = [audit_branch(task) for task in tasks]
    else:
        with ProcessPoolExecutor(max_workers=min(workers, len(tasks))) as executor:
            branch_results = executor.map(audit_branch, tasks)
    for branch, (branch_records, branch_misses, prime_count, branch_histogram) in zip(branches, branch_results):
        records.extend(branch_records)
        misses.extend(branch_misses)
        branch_prime_count[int(branch["v_mod_29"])] += prime_count
        gap_histogram.update(branch_histogram)

    if len(branches) != 14:
        raise AssertionError("expected fourteen post-affine residual branches")
    if len(records) + len(misses) != sum(branch_prime_count.values()):
        raise AssertionError("prime classification is incomplete")
    return {
        "arithmetic": (
            "deterministic 64-bit primality, complete x factorization, "
            "exhaustive divisors of 4x and x^2, Type II certificate checks, "
            "and exact shared marked-descent identity verification"
        ),
        "scope_note": (
            "A finite residual-sample audit. It does not prove that the "
            "shared Type II selector has a uniform gap bound or covers every "
            "core prime."
        ),
        "parameter_limit_exclusive": parameter_limit,
        "gap_cap": gap_cap,
        "record_format": "compact-tail" if compact else "full",
        "state_count": len(branches),
        "prime_count": sum(branch_prime_count.values()),
        "prime_count_by_branch": {
            str(branch): count for branch, count in sorted(branch_prime_count.items())
        },
        "captured_count": len(records),
        "misses": misses,
        "largest_minimum_gap": max(gap_histogram) if records else None,
        "minimum_gap_histogram": {
            str(gap): count for gap, count in sorted(gap_histogram.items())
        },
        "records": records,
    }


def run_compact_audit_to_file(
    output: Path, parameter_limit: int, gap_cap: int, workers: int
) -> dict[str, object]:
    """Stream compact branch records so million-layer audits avoid a giant parent list."""
    branches = mixed_boundary.remaining_branches()
    tasks = [(branch, parameter_limit, gap_cap, True) for branch in branches]
    misses: list[dict[str, int]] = []
    gap_histogram: Counter[int] = Counter()
    branch_prime_count: Counter[int] = Counter()
    captured_count = 0
    first_record = True
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        handle.write('{"record_format":"compact-tail","records":[\n')
        with ProcessPoolExecutor(max_workers=min(workers, len(tasks))) as executor:
            branch_results = executor.map(audit_branch, tasks)
            for branch, (records, branch_misses, prime_count, branch_histogram) in zip(
                branches, branch_results
            ):
                for record in records:
                    if not first_record:
                        handle.write(",\n")
                    json.dump(record, handle, ensure_ascii=False, separators=(",", ":"))
                    first_record = False
                captured_count += len(records)
                misses.extend(branch_misses)
                branch_prime_count[int(branch["v_mod_29"])] += prime_count
                gap_histogram.update(branch_histogram)
        prime_count = sum(branch_prime_count.values())
        if captured_count + len(misses) != prime_count:
            raise AssertionError("prime classification is incomplete")
        payload = {
            "arithmetic": (
                "deterministic 64-bit primality, complete x factorization, exhaustive "
                "divisors of 4x and x^2, Type II certificate checks, and exact shared "
                "marked-descent identity verification; compact records retain the fields "
                "needed for ordinary two-tail closure"
            ),
            "scope_note": (
                "A finite residual-sample audit. It does not prove that the shared Type II "
                "selector has a uniform gap bound or covers every core prime."
            ),
            "parameter_limit_exclusive": parameter_limit,
            "gap_cap": gap_cap,
            "state_count": len(branches),
            "prime_count": prime_count,
            "prime_count_by_branch": {
                str(branch): count for branch, count in sorted(branch_prime_count.items())
            },
            "captured_count": captured_count,
            "misses": misses,
            "largest_minimum_gap": max(gap_histogram) if captured_count else None,
            "minimum_gap_histogram": {
                str(gap): count for gap, count in sorted(gap_histogram.items())
            },
        }
        handle.write("],")
        for index, (key, value) in enumerate(payload.items()):
            if index:
                handle.write(",")
            json.dump(key, handle, ensure_ascii=False)
            handle.write(":")
            json.dump(value, handle, ensure_ascii=False, separators=(",", ":"))
        handle.write("}\n")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parameter-limit", type=int, default=PARAMETER_LIMIT)
    parser.add_argument("--gap-cap", type=int, default=GAP_CAP)
    parser.add_argument(
        "--workers",
        type=int,
        default=min(14, os.cpu_count() or 1),
        help="independent H19-k23 progressions to audit concurrently",
    )
    parser.add_argument("--output", type=Path, default=RESULTS)
    parser.add_argument(
        "--compact",
        action="store_true",
        help="stream only the fields required by ordinary two-tail closure",
    )
    args = parser.parse_args()
    if args.compact:
        payload = run_compact_audit_to_file(
            args.output, args.parameter_limit, args.gap_cap, args.workers
        )
    else:
        payload = run_audit(args.parameter_limit, args.gap_cap, args.workers)
        args.output.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    summary = {
        key: payload[key]
        for key in (
            "parameter_limit_exclusive",
            "gap_cap",
            "prime_count",
            "captured_count",
            "largest_minimum_gap",
            "minimum_gap_histogram",
            "misses",
        )
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
