#!/usr/bin/env python3
"""Find strict nonmultiple scaled-source descents on bounded-r source rays."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import sys
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
OBSTRUCTION_INPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-tail-obstruction-1b-results.json"
CANDIDATE_SCRIPT = ROOT / "reproductions" / "type_ii_h19_bounded_r_scaled_source_candidate_profile.py"
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-scaled-source-descent-1b-results.json"


def load_script(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


candidates = load_script("bounded_r_scaled_source_candidates", CANDIDATE_SCRIPT)
short_certificate = load_script("bounded_r_scaled_source_short_certificate", SHORT_CERTIFICATE)


def factorization(value: int) -> dict[int, int]:
    return {int(prime): int(exponent) for prime, exponent in sympy.factorint(value).items()}


def scaled_tail_witness(
    prime: int, source: int, a: int, b: int, shift: int
) -> tuple[dict[str, object] | None, int]:
    """Search all forced-multiple square-tail divisors for one finite candidate."""
    first = a * source // b
    tail_scale = a * source
    modulus = 4 * a - b
    multiple = b * shift
    factors = factorization(tail_scale)
    multiple_factors = factorization(multiple)
    if any(multiple_factors.get(prime_factor, 0) > 2 * factors.get(prime_factor, 0)
           for prime_factor in multiple_factors):
        return None, 0

    exponent_ranges = [
        (
            prime_factor,
            multiple_factors.get(prime_factor, 0),
            2 * exponent,
        )
        for prime_factor, exponent in factors.items()
    ]
    exponent_ranges.sort(reverse=True)
    checked = 0

    def visit(index: int, divisor: int) -> dict[str, object] | None:
        nonlocal checked
        if divisor > tail_scale:
            return None
        if index == len(exponent_ranges):
            checked += 1
            if (tail_scale + divisor) % modulus:
                return None
            companion = tail_scale * tail_scale // divisor
            if (tail_scale + companion) % modulus:
                return None
            u = (tail_scale + divisor) // modulus
            v = (tail_scale + companion) // modulus
            gap = (4 * divisor + b * shift) // modulus
            if (
                4 * u - prime != gap
                or not 3 <= gap <= prime - 2
                or (multiple * u * u) % divisor
            ):
                return None
            certificate_divisor = multiple * u * u // divisor
            certificate = short_certificate.GapCertificate(
                prime,
                "I",
                gap,
                u,
                certificate_divisor,
                v,
                first * prime // shift,
            )
            if not short_certificate.verify_certificate(certificate):
                raise AssertionError("scaled-source Type I certificate did not verify")
            source_solution = (first, u, v)
            target_solution = (first * prime // shift, u, v)
            if (
                Fraction(4, source)
                != sum((Fraction(1, value) for value in source_solution), Fraction())
                or Fraction(4, prime)
                != sum((Fraction(1, value) for value in target_solution), Fraction())
            ):
                raise AssertionError("scaled-source descent identity did not verify")
            return {
                "tail_factor": divisor,
                "source_solution": list(source_solution),
                "target_solution": list(target_solution),
                "certificate": {
                    "type": "I",
                    "gap": gap,
                    "x": u,
                    "divisor": certificate_divisor,
                    "y": v,
                    "z": first * prime // shift,
                },
            }

        prime_factor, lower, upper = exponent_ranges[index]
        power = prime_factor**lower
        for _ in range(lower, upper + 1):
            witness = visit(index + 1, divisor * power)
            if witness is not None:
                return witness
            power *= prime_factor
        return None

    return visit(0, 1), checked


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Jointly test every deduplicated structural candidate and its full tail."""
    candidate_rows: set[tuple[int, int, int, int, int]] = set()
    primes = [int(row["prime"]) for row in payload["records"]]
    for row in payload["records"]:
        prime = int(row["prime"])
        for state in row["states"]:
            for ray in candidates.small_r.compatible_rays(prime, int(state["r"])):
                source = prime - int(ray["distance"])
                for candidate in candidates.scaled_candidates(prime, source):
                    candidate_rows.add(
                        (
                            prime,
                            source,
                            candidate["a"],
                            candidate["b"],
                            candidate["shift"],
                        )
                    )

    first_witness: dict[int, dict[str, object]] = {}
    hits_by_prime = {prime: 0 for prime in primes}
    tail_divisor_test_count = 0
    for prime, source, a, b, shift in sorted(candidate_rows):
        witness, tested = scaled_tail_witness(prime, source, a, b, shift)
        tail_divisor_test_count += tested
        if witness is None:
            continue
        hits_by_prime[prime] += 1
        first_witness.setdefault(
            prime,
            {
                "source_denominator": source,
                "a": a,
                "b": b,
                "shift": shift,
                **witness,
            },
        )

    records = [
        {
            "prime": prime,
            "hit_candidate_count": hits_by_prime[prime],
            "first_witness": first_witness.get(prime),
        }
        for prime in primes
    ]
    misses = [record["prime"] for record in records if record["first_witness"] is None]
    return {
        "arithmetic": (
            "complete factor-table enumeration of nonmultiple scaled-source "
            "candidates, exact forced-multiple square-tail enumeration, and "
            "exact rational plus Type I certificate verification"
        ),
        "scope_note": (
            "A finite audit on the source rays of the supplied r-capped "
            "residual. It does not establish a global scaled-source selector."
        ),
        "prime_limit": payload["prime_limit"],
        "r_cap": payload["r_cap"],
        "residual_prime_count": len(primes),
        "unique_scaled_source_candidate_count": len(candidate_rows),
        "tail_divisor_test_count": tail_divisor_test_count,
        "hit_candidate_count": sum(hits_by_prime.values()),
        "covered_prime_count": len(primes) - len(misses),
        "uncovered_primes": misses,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=OBSTRUCTION_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
