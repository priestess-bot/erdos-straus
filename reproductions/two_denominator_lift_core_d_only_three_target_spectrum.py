#!/usr/bin/env python3
"""Verify focused D-only support-dichotomy and three-target examples."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "two-denominator-lift-core-d-only-three-target-spectrum-results.json"
)

CASES = (
    {
        "name": "core_source_supported_nonempty",
        "prime": 73,
        "rank": 33,
        "D": 9,
        "expected_z": 11,
    },
    {
        "name": "core_non_source_supported_empty",
        "prime": 73,
        "rank": 65,
        "D": 73,
        "expected_z": None,
    },
    {
        "name": "noncore_non_source_supported_z_one",
        "prime": 7,
        "rank": 6,
        "D": 14,
        "expected_z": 1,
        "pell_u": 1,
        "pell_v": 1,
    },
    {
        "name": "noncore_non_source_supported_nontrivial",
        "prime": 239,
        "rank": 238,
        "D": 23422,
        "expected_z": 25,
        "pell_u": 5,
        "pell_v": 7,
    },
)


def divisors(n: int) -> list[int]:
    low: list[int] = []
    high: list[int] = []
    for divisor in range(1, isqrt(n) + 1):
        if n % divisor:
            continue
        low.append(divisor)
        if divisor * divisor != n:
            high.append(n // divisor)
    return low + high[::-1]


def in_d_only_set(prime: int, rank: int, D: int) -> bool:
    r = prime - rank
    N = rank * prime
    C = 4 * r
    return (
        N * N % D == 0
        and 0 < D < rank * rank
        and (D - N) % C == 0
        and (N * N // D - N) % C == 0
    )


def p_adic_exponent(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def analyze_case(case: dict[str, object]) -> dict[str, object]:
    name = str(case["name"])
    prime = int(case["prime"])
    rank = int(case["rank"])
    D = int(case["D"])
    expected_z_value = case["expected_z"]
    expected_z = None if expected_z_value is None else int(expected_z_value)
    r = prime - rank
    N = rank * prime
    C = 4 * r

    assert 2 <= rank < prime
    assert in_d_only_set(prime, rank, D)

    a = (N - D) // C
    a_prime = (N * N // D - N) // C
    assert a_prime % prime == 0
    lam = a_prime // prime
    delta = gcd(4 * lam - 1, prime)

    M = 4 * a - rank
    S = rank * a
    tail_gcd = gcd(M, S)
    mu = M // tail_gcd
    sigma = S // tail_gcd
    assert (mu, sigma) == (
        (4 * lam - 1) // delta,
        prime * lam // delta,
    )

    source_supported = rank * rank % D == 0
    assert (delta == prime) == source_supported

    normal_form: dict[str, int] | None
    target_rows: list[dict[str, int]]
    if source_supported:
        assert 4 * lam == prime * mu + 1
        assert sigma == lam
        normal_form = None
        target_rows = []
    else:
        assert D % prime == 0
        d = D // prime
        assert rank * rank % d == 0
        assert a % prime == 0
        t = a // prime
        H = prime + (4 * lam - 1) * r
        assert H == rank * rank // d
        assert 4 * lam * lam % H == 0
        s = 4 * lam * lam // H
        assert t == lam - r * s
        assert d * lam == rank * t
        assert D == prime * rank * rank // H
        assert gcd(prime, lam) == 1
        assert (mu, sigma) == (4 * lam - 1, prime * lam)
        normal_form = {"d": d, "H": H, "s": s, "t": t}

        target_rows = []
        inverse_prime = pow(prime, -1, mu)
        expected_targets = {
            0: (-prime * lam) % mu,
            1: (-lam) % mu,
            2: (-inverse_prime * lam) % mu,
        }
        for z in divisors(sigma * sigma):
            exponent = p_adic_exponent(z, prime)
            assert exponent <= 2
            u = z // prime**exponent
            assert lam * lam % u == 0
            marked_hit = (z + sigma) % mu == 0
            target_hit = u % mu == expected_targets[exponent]
            assert marked_hit == target_hit
            if marked_hit:
                target_rows.append({"z": z, "e": exponent, "u": u})

        if prime % 24 == 1:
            assert mu % 4 == 3 and mu >= 3
            assert (sigma + 1) % mu != 0
            assert all(row["u"] != lam for row in target_rows)

    witnesses = [
        z for z in divisors(sigma * sigma) if (z + sigma) % mu == 0
    ]
    if not source_supported:
        assert [row["z"] for row in target_rows] == witnesses

    if prime % 24 == 1:
        assert mu % 4 == 3 and mu >= 3
        assert (sigma + 1) % mu != 0

    if expected_z is None:
        assert not witnesses
        selected_tail = None
    else:
        assert expected_z in witnesses
        b = (sigma + expected_z) // mu
        c = (sigma + sigma * sigma // expected_z) // mu
        assert Fraction(1, b) + Fraction(1, c) == Fraction(mu, sigma)
        assert Fraction(1, a) + Fraction(1, b) + Fraction(1, c) == Fraction(
            4, rank
        )
        assert Fraction(1, a_prime) + Fraction(1, b) + Fraction(
            1, c
        ) == Fraction(4, prime)
        selected_tail = {"z": expected_z, "b": b, "c": c}

    pell_parameters = None
    if "pell_u" in case:
        u_pell = int(case["pell_u"])
        v_pell = int(case["pell_v"])
        assert v_pell * v_pell - 2 * u_pell * u_pell == -1
        assert r == 1
        assert prime == 4 * u_pell * (u_pell + v_pell) - 1
        assert rank == prime - 1
        assert lam == u_pell * (v_pell + 2 * u_pell)
        assert D == 2 * prime * v_pell * v_pell
        assert a == prime * u_pell * v_pell
        assert expected_z == u_pell * u_pell
        assert prime % 8 == 7
        assert selected_tail == {
            "z": u_pell * u_pell,
            "b": u_pell * (u_pell + v_pell),
            "c": prime * (u_pell + v_pell) * (v_pell + 2 * u_pell),
        }
        pell_parameters = {"u": u_pell, "v": v_pell}

    return {
        "name": name,
        "prime": prime,
        "core_prime": prime % 24 == 1,
        "rank": rank,
        "r": r,
        "D": D,
        "source_supported": source_supported,
        "a": a,
        "a_prime": a_prime,
        "lambda": lam,
        "delta": delta,
        "mu": mu,
        "sigma": sigma,
        "normal_form": normal_form,
        "pell_parameters": pell_parameters,
        "tail_witness_count": len(witnesses),
        "three_target_witnesses": target_rows,
        "selected_tail": selected_tail,
    }


def run() -> dict[str, object]:
    records = [analyze_case(case) for case in CASES]
    observed = [
        (
            record["name"],
            record["lambda"],
            record["mu"],
            record["sigma"],
            record["source_supported"],
            record["tail_witness_count"],
        )
        for record in records
    ]
    expected = [
        ("core_source_supported_nonempty", 55, 3, 55, True, 4),
        ("core_non_source_supported_empty", 130, 519, 9490, False, 0),
        ("noncore_non_source_supported_z_one", 3, 11, 21, False, 2),
        (
            "noncore_non_source_supported_nontrivial",
            85,
            339,
            20315,
            False,
            2,
        ),
    ]
    if observed != expected:
        raise AssertionError(f"focused D-only boundary changed: {observed}")

    return {
        "schema_version": "two-denominator-core-d-only-three-target/v1",
        "scope_note": (
            "Focused exact verification of the support dichotomy, one empty core "
            "non-source-supported fiber, and two noncore positive boundary cases. "
            "It is not an exhaustive search or a universal three-target hit claim."
        ),
        "summary": {
            "case_count": len(records),
            "source_supported_count": sum(
                bool(record["source_supported"]) for record in records
            ),
            "non_source_supported_count": sum(
                not bool(record["source_supported"]) for record in records
            ),
            "nonempty_fiber_count": sum(
                int(record["tail_witness_count"]) > 0 for record in records
            ),
            "empty_fiber_count": sum(
                int(record["tail_witness_count"]) == 0 for record in records
            ),
        },
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    payload = run()
    if args.verify:
        stored = json.loads(args.output.read_text(encoding="utf-8"))
        if stored != payload:
            raise AssertionError("stored result does not match recomputation")
    else:
        args.output.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(payload["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
