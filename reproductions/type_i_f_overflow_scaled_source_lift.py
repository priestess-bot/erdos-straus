#!/usr/bin/env python3
"""Audit the b in {1,2,4} scaled-source lift family from square terminals."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import json
from math import gcd
from pathlib import Path

from sympy import divisors


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-f-overflow-square-terminal-lift-results.json"
OUTPUT = ROOT / "reproductions" / "type-i-f-overflow-scaled-source-lift-results.json"
EXPECTED_INPUT_SHA256 = "ca3d74768cf90586834dfa7f8a127c760871cf5b5d27cc98be8ec96ec58dc9a1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_tail(
    prime: int,
    source: int,
    b: int,
    a: int,
    d: int,
    e: int,
) -> dict[str, int] | None:
    L = a * source
    A = L // b
    q = 4 * a - b
    if q <= 0 or L % b or d <= 0 or d >= prime or A % d:
        return None
    if e <= 0 or e > L or e % (b * d):
        return None
    if (L + e) % q or (L + (L * L) // e) % q:
        return None
    u = (L + e) // q
    m_numerator = 4 * e + b * d
    if m_numerator % q:
        return None
    m = m_numerator // q
    if m != 4 * u - prime or not 3 <= m <= prime - 2:
        return None
    v_numerator = L * u
    if v_numerator % e:
        return None
    v = v_numerator // e
    D_numerator = b * d * u * u
    if D_numerator % e:
        return None
    D = D_numerator // e
    if u <= 0 or v <= 0 or D <= 0 or (u * u) % D:
        return None
    source_solution = (A, u, v)
    target_solution = (A * prime // d, u, v)
    if (A * prime) % d:
        return None
    if Fraction(4, source) != sum(
        (Fraction(1, value) for value in source_solution), Fraction()
    ):
        raise AssertionError("scaled source identity failed")
    if Fraction(4, prime) != sum(
        (Fraction(1, value) for value in target_solution), Fraction()
    ):
        raise AssertionError("scaled target identity failed")
    if A * prime // d <= 0 or source >= prime:
        return None
    return {
        "prime": prime,
        "source": source,
        "b": b,
        "a": a,
        "d": d,
        "e": e,
        "L": L,
        "A": A,
        "q": q,
        "u": u,
        "v": v,
        "m": m,
        "D": D,
    }


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the square-terminal input changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    candidates = list(payload.get("candidates", []))
    if len(candidates) != 253:
        raise AssertionError(f"unexpected candidate count: {len(candidates)}")

    admissible_ab: list[dict[str, int]] = []
    parameters: list[dict[str, int]] = []
    b_counts: Counter[int] = Counter()
    a_loop_count = 0
    e_divisor_count = 0
    e_candidate_count = 0

    for candidate in candidates:
        prime = int(candidate["prime"])
        source = int(candidate["source"])
        distance = prime - source
        if distance <= 0 or source % 2:
            raise AssertionError("invalid square-terminal source")
        for b in (1, 2, 4):
            if source % b:
                continue
            max_a = (b * prime - 1) // (4 * distance)
            for a in range(1, max_a + 1):
                a_loop_count += 1
                if gcd(a, b) != 1 or (4 * a * distance) % b:
                    continue
                d_numerator = 4 * a * distance
                d = prime - d_numerator // b
                if not 0 < d < prime:
                    continue
                if (a * source) % b:
                    continue
                A = (a * source) // b
                if A % d:
                    continue
                q = 4 * a - b
                if q <= 0:
                    continue
                L = a * source
                e_values = [
                    int(value)
                    for value in divisors(L * L)
                    if value <= L and value % (b * d) == 0
                ]
                e_divisor_count += len(e_values)
                local_parameters: list[dict[str, int]] = []
                for e in e_values:
                    if (L + e) % q or (L + (L * L) // e) % q:
                        continue
                    e_candidate_count += 1
                    parameter = verify_tail(prime, source, b, a, d, e)
                    if parameter is not None:
                        local_parameters.append(parameter)
                record = {
                    "prime": prime,
                    "source": source,
                    "b": b,
                    "a": a,
                    "d": d,
                    "L": L,
                    "q": q,
                    "e_divisor_count": len(e_values),
                    "e_candidate_count": len(local_parameters),
                }
                admissible_ab.append(record)
                b_counts[b] += 1
                parameters.extend(local_parameters)

    hit_primes = sorted({int(item["prime"]) for item in parameters})
    return {
        "arithmetic": (
            "For every saved square-terminal source, enumerate b in {1,2,4}, every positive "
            "coprime a with d=p-4a(p-n)/b>0, enforce b|n and d|(an/b), then enumerate every "
            "e|(an)^2 with the complete scaled-source square-tail and Type I checks."
        ),
        "scope_note": (
            "Finite targeted audit of the b in {1,2,4} scaled-source family. It is complete "
            "for the 253 saved square-terminal sources; a miss does not rule out other source "
            "families, non-shared tails, or a global selector."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "candidate_count": len(candidates),
        "a_loop_count": a_loop_count,
        "admissible_ab_count": len(admissible_ab),
        "admissible_b_histogram": {
            str(b): int(count) for b, count in sorted(b_counts.items())
        },
        "e_divisor_count": e_divisor_count,
        "e_candidate_count": e_candidate_count,
        "parameter_count": len(parameters),
        "hit_prime_count": len(hit_primes),
        "hit_primes": hit_primes,
        "admissible_ab": admissible_ab,
        "parameters": parameters,
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    result = run()
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "candidate_count",
                    "a_loop_count",
                    "admissible_ab_count",
                    "admissible_b_histogram",
                    "e_divisor_count",
                    "e_candidate_count",
                    "parameter_count",
                    "hit_prime_count",
                    "hit_primes",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
