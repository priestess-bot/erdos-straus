#!/usr/bin/env python3
"""Verify focused overflow-to-D-only square-excess boundaries."""

from __future__ import annotations

import argparse
import json
from math import gcd, isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-overflow-d-only-square-excess-no-go-results.json"
)

RECEIPTS = (
    {
        "name": "clean_overflow_p73",
        "prime": 73,
        "rank": 17,
        "support": 31,
        "expected_non_source_deltas": [],
        "provenance": "clean_large_slab",
        "source_R": 63,
        "Q": 31,
        "q": 31,
        "e": 1,
        "alpha": 2,
        "beta": 1,
    },
    {
        "name": "clean_overflow_p241",
        "prime": 241,
        "rank": 33,
        "support": 71,
        "expected_non_source_deltas": [],
        "provenance": "clean_large_slab",
        "source_R": 215,
        "Q": 71,
        "q": 71,
        "e": 1,
        "alpha": 3,
        "beta": 2,
    },
    {
        "name": "clean_overflow_p13177",
        "prime": 13_177,
        "rank": 1_737,
        "support": 4_096,
        "expected_non_source_deltas": [],
        "provenance": "clean_large_slab",
        "source_R": 12_299,
        "Q": 4_096,
        "q": 2,
        "e": 12,
        "alpha": 3,
        "beta": 11,
    },
    {
        "name": "layer_supported_delta_no_go",
        "prime": 1_129,
        "rank": 1_125,
        "support": 1_021,
        "expected_non_source_deltas": [5, 405],
        "provenance": "clean_large_slab",
        "source_R": 1_023,
        "Q": 1_021,
        "q": 1_021,
        "e": 1,
        "alpha": 1,
        "beta": 2,
    },
    {
        "name": "square_excess_parameter_still_empty",
        "prime": 193,
        "rank": 185,
        "support": 8_926,
        "expected_non_source_deltas": [25],
        "provenance": "abstract_overflow_receipt",
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


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % divisor for divisor in range(3, isqrt(n) + 1, 2))


def factorization(n: int) -> list[tuple[int, int]]:
    factors: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor:
            divisor = 3 if divisor == 2 else divisor + 2
            continue
        exponent = 0
        while n % divisor == 0:
            n //= divisor
            exponent += 1
        factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if n > 1:
        factors.append((n, 1))
    return factors


def in_d_only_set(prime: int, rank: int, D: int) -> bool:
    distance = prime - rank
    product = prime * rank
    modulus = 4 * distance
    return (
        product * product % D == 0
        and 0 < D < rank * rank
        and (D - product) % modulus == 0
        and (product * product // D - product) % modulus == 0
    )


def normalized_target_hits(
    prime: int, lam: int, mu: int
) -> list[dict[str, int]]:
    targets = {
        0: (-prime * lam) % mu,
        1: (-lam) % mu,
        2: (-pow(prime, -1, mu) * lam) % mu,
    }
    hits: list[dict[str, int]] = []
    for divisor in divisors(lam * lam):
        if divisor >= lam:
            continue
        for p_exponent, target in targets.items():
            if divisor % mu == target:
                hits.append(
                    {
                        "p_exponent": p_exponent,
                        "lambda_square_divisor": divisor,
                    }
                )
    return hits


def exponent_profile(value: int) -> dict[int, int]:
    return {prime: exponent for prime, exponent in factorization(value)}


def analyze_non_source_parameter(
    prime: int, rank: int, delta: int
) -> dict[str, object]:
    distance = prime - rank
    D = prime * delta
    assert in_d_only_set(prime, rank, D)
    assert rank * rank % delta == 0

    product = prime * rank
    modulus = 4 * distance
    a = (product - D) // modulus
    a_prime = (product * product // D - product) // modulus
    assert a % prime == 0
    assert a_prime % prime == 0
    t = a // prime
    lam = a_prime // prime
    mu = 4 * lam - 1
    H = rank * rank // delta
    assert H == prime + mu * distance
    assert 4 * lam * lam % H == 0
    target_hits = normalized_target_hits(prime, lam, mu)

    rank_profile = exponent_profile(rank)
    delta_profile = exponent_profile(delta)
    square_excess_primes = [
        q
        for q, exponent in delta_profile.items()
        if exponent > rank_profile.get(q, 0)
    ]
    layer_supported = rank % delta == 0
    assert layer_supported == (not square_excess_primes)

    layer_normal_form = None
    square_carrier_normal_form = None
    if layer_supported:
        h = rank // delta
        assert lam % rank == 0
        ell = lam // rank
        assert h == 1 + 4 * ell * distance
        assert h > 1 and rank % h == 0
        assert 2 * lam < mu
        assert prime + 4 * (lam - 1) < 2 * mu
        assert 4 * ell < 3 * h
        assert 16 * ell < h
        assert not target_hits
        layer_normal_form = {"h": h, "ell": ell}
    else:
        assert delta >= 9
        assert rank * rank > 9 * prime
        assert rank * (rank + 3) > 12 * prime
        assert 13 * rank >= 12 * prime + 9
        common = gcd(rank, delta)
        square_a = rank // common
        w = delta // common
        assert gcd(square_a, w) == 1
        assert common % w == 0
        c = common // w
        assert w >= 3 and w % 2 == 1
        assert delta == c * w * w
        assert rank == square_a * c * w
        assert t % (c * w) == 0
        b = t // (c * w)
        assert lam == square_a * b * c
        assert square_a == w + 4 * distance * b
        square_carrier_normal_form = {
            "a": square_a,
            "b": b,
            "c": c,
            "w": w,
            "t": t,
        }

    return {
        "D": D,
        "delta": delta,
        "delta_factorization": [list(item) for item in factorization(delta)],
        "layer_supported": layer_supported,
        "square_excess_primes": square_excess_primes,
        "a": a,
        "a_prime": a_prime,
        "lambda": lam,
        "mu": mu,
        "H": H,
        "layer_normal_form": layer_normal_form,
        "square_carrier_normal_form": square_carrier_normal_form,
        "normalized_target_hits": target_hits,
        "marked_fiber_nonempty": bool(target_hits),
    }


def analyze_receipt(case: dict[str, object]) -> dict[str, object]:
    name = str(case["name"])
    prime = int(case["prime"])
    rank = int(case["rank"])
    support = int(case["support"])
    expected_deltas = [int(value) for value in case["expected_non_source_deltas"]]
    distance = prime - rank
    product = prime * rank

    assert prime % 24 == 1
    assert 2 <= rank < prime
    assert rank % 4 == 1
    assert distance % 4 == 0 and distance >= 4
    d, remainder = divmod(product - 1, 4 * support)
    assert remainder == 0 and d > 0
    R_M = 4 * support - rank
    C = prime - d
    K_M = support * C
    assert R_M > prime
    assert 1 <= R_M < 4 * support
    assert 4 * K_M == prime * R_M + 1
    assert gcd(support, product) == 1
    assert gcd(d, product) == 1
    assert gcd(distance, product) == 1
    assert rank * C - R_M * d == 1
    assert C * (prime + rank) > prime * prime + 1
    assert 2 * C > prime

    source_slab = None
    if case["provenance"] == "clean_large_slab":
        source_R = int(case["source_R"])
        Q = int(case["Q"])
        q = int(case["q"])
        e = int(case["e"])
        alpha = int(case["alpha"])
        beta = int(case["beta"])
        source_K = (prime * source_R + 1) // 4
        assert 4 * source_K == prime * source_R + 1
        assert Q == q**e and is_prime(q)
        assert support == Q
        assert Q * alpha + beta == source_R
        assert gcd(Q * alpha, beta) == 1
        assert source_K % (alpha * beta) == 0
        assert source_K % q != 0
        source_slab = {
            "R": source_R,
            "K": source_K,
            "Q": Q,
            "q": q,
            "e": e,
            "alpha": alpha,
            "beta": beta,
        }

    source_parameters = [
        D for D in divisors(rank * rank) if in_d_only_set(prime, rank, D)
    ]
    non_source_deltas = [
        delta
        for delta in divisors(rank * rank)
        if in_d_only_set(prime, rank, prime * delta)
    ]
    assert non_source_deltas == expected_deltas
    all_parameters = source_parameters + [
        prime * delta for delta in non_source_deltas
    ]
    assert all(gcd(D, support * d * distance) == 1 for D in all_parameters)

    non_source_parameters = [
        analyze_non_source_parameter(prime, rank, delta)
        for delta in non_source_deltas
    ]
    low_rank_square_excess_excluded = rank * (rank + 3) < 12 * prime
    if low_rank_square_excess_excluded:
        assert not any(
            parameter["square_excess_primes"]
            for parameter in non_source_parameters
        )

    return {
        "name": name,
        "provenance": case["provenance"],
        "source_slab": source_slab,
        "prime": prime,
        "rank": rank,
        "distance": distance,
        "support": support,
        "R_M": R_M,
        "K_M": K_M,
        "C": C,
        "d": d,
        "support_erasure_verified": True,
        "rank_times_rank_plus_three": rank * (rank + 3),
        "twelve_p": 12 * prime,
        "low_rank_square_excess_excluded": low_rank_square_excess_excluded,
        "source_supported_D": source_parameters,
        "non_source_parameters": non_source_parameters,
    }


def run() -> dict[str, object]:
    records = [analyze_receipt(case) for case in RECEIPTS]
    non_source_parameters = [
        parameter
        for record in records
        for parameter in record["non_source_parameters"]
    ]
    observed = [
        (
            record["name"],
            record["rank"],
            record["R_M"],
            [
                parameter["delta"]
                for parameter in record["non_source_parameters"]
            ],
        )
        for record in records
    ]
    expected = [
        ("clean_overflow_p73", 17, 107, []),
        ("clean_overflow_p241", 33, 251, []),
        ("clean_overflow_p13177", 1_737, 14_647, []),
        ("layer_supported_delta_no_go", 1_125, 2_959, [5, 405]),
        ("square_excess_parameter_still_empty", 185, 35_519, [25]),
    ]
    if observed != expected:
        raise AssertionError(f"focused overflow boundary changed: {observed}")

    return {
        "schema_version": "overflow-d-only-square-excess-boundary/v1",
        "scope_note": (
            "Focused exact verification of five overflow receipts, support "
            "erasure, one layer-supported no-go parameter, and two square-excess "
            "parameters. It is not a historical scan or a universal E4 claim."
        ),
        "summary": {
            "receipt_count": len(records),
            "clean_large_slab_receipt_count": sum(
                record["provenance"] == "clean_large_slab"
                for record in records
            ),
            "support_erasure_verified_count": sum(
                bool(record["support_erasure_verified"]) for record in records
            ),
            "non_source_parameter_count": len(non_source_parameters),
            "layer_supported_no_go_count": sum(
                bool(parameter["layer_supported"])
                for parameter in non_source_parameters
            ),
            "square_excess_parameter_count": sum(
                bool(parameter["square_excess_primes"])
                for parameter in non_source_parameters
            ),
            "marked_nonempty_count": sum(
                bool(parameter["marked_fiber_nonempty"])
                for parameter in non_source_parameters
            ),
            "low_rank_square_excess_excluded_count": sum(
                bool(record["low_rank_square_excess_excluded"])
                for record in records
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
