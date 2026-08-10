#!/usr/bin/env python3
"""Verify the least-C=2 carry no-go and its internal dyadic transduction."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd, lcm

import sympy

import type_i_bottom_sink_scc_complete_excess_bundle as bottom


def valuation_two(value: int) -> int:
    if value <= 0:
        raise ValueError("2-adic valuation expects a positive integer")
    exponent = 0
    while value % 2 == 0:
        value //= 2
        exponent += 1
    return exponent


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def least_c2_boundary(prime: int) -> dict[str, int]:
    if not sympy.isprime(prime) or prime % 24 != 1:
        raise ValueError("expected a core prime congruent to 1 modulo 24")
    bound = (prime - 1) ** 2 // 4
    support = (prime - 1) * (2 * prime - 1) // 8
    K = 2 * support
    R = (8 * support - 1) // prime
    if not (
        support == bound + (prime - 1) // 8
        and support - prime < bound < support
        and 8 * support == prime * R + 1
        and R == 2 * prime - 3
        and K == (prime - 1) * (2 * prime - 1) // 4
        and 4 * K == prime * R + 1
        and K // support == 2
    ):
        raise AssertionError("least C=2 boundary formulas failed")
    return {"p": prime, "B": bound, "A": support, "R": R, "K": K}


def structural_no_go(boundary: dict[str, int]) -> dict[str, object]:
    prime = boundary["p"]
    support = boundary["A"]
    K = boundary["K"]
    R = boundary["R"]

    c_one_multipliers = tuple(L for L in range(2, R) if L % prime == 2)
    c_two_multipliers = tuple(L for L in range(2, R) if L % prime == 1)
    if c_one_multipliers != (2, prime + 2):
        raise AssertionError("c=1 multiplier interval changed")
    if c_two_multipliers != (prime + 1,):
        raise AssertionError("c=2 multiplier interval changed")

    # At the least offending exponent, every odd full block adds an odd
    # factor to L, while a 2-full-block adds at least 2^2.
    full_block_checks = []
    for q in (*bottom.factorization(K), 17):
        support_exponent = valuation(support, q)
        K_exponent = valuation(K, q)
        offending_exponent = K_exponent + 1
        multiplier_exponent = offending_exponent - support_exponent
        if q == 2:
            if K_exponent != support_exponent + 1 or multiplier_exponent < 2:
                raise AssertionError("2-full-block no-L=2 gate failed")
        elif K_exponent != support_exponent or multiplier_exponent < 1:
            raise AssertionError("odd full-block no-L=2 gate failed")
        full_block_checks.append((q, multiplier_exponent))

    t = (prime - 5) // 4
    if not (
        prime % 24 == 1
        and t > 1
        and gcd(t, 9) == 1
        and K == (t + 1) * (8 * t + 9)
        and gcd(t, K) == 1
    ):
        raise AssertionError("L=p+2 residual contradiction failed")
    if not (prime - 4 > 21 and (4 * K) % (prime - 4) == 21):
        raise AssertionError("L=p+1 residual contradiction failed")

    return {
        "c_one_multiplier_candidates": c_one_multipliers,
        "c_two_multiplier_candidates": c_two_multipliers,
        "full_block_multiplier_exponents": full_block_checks,
        "p_minus_five_coprime_part": t,
        "p_minus_four_remainder": (4 * K) % (prime - 4),
    }


def bottom_complete_excess_rows(
    boundary: dict[str, int],
) -> tuple[int, list[tuple[object, ...]]]:
    prime = boundary["p"]
    support = boundary["A"]
    R = boundary["R"]
    K = boundary["K"]
    factors = bottom.factorization(K)
    adjacency, _labels = bottom.bottom_graph(R, factors)
    sinks = bottom.sink_components(adjacency)
    if len(sinks) != 1:
        raise AssertionError("focused boundary control lost its unique sink")

    rows: list[tuple[object, ...]] = []
    for node in sorted(sinks[0]):
        for selected, other in ((node[1], node[0]), (node[0], node[1])):
            Q = 1
            beta = 1
            for q, exponent in bottom.factorization(selected).items():
                if exponent > factors.get(q, 0):
                    Q *= q**exponent
                else:
                    beta *= q**exponent
            residual = other * beta
            if (
                Q <= 1
                or selected != Q * beta
                or gcd(Q, residual) != 1
                or K % residual
                or K % Q == 0
            ):
                continue
            target_support = lcm(support, Q)
            multiplier = target_support // support
            if multiplier < 2 or target_support % prime == 0:
                continue
            target = 2 * pow(multiplier, -1, prime) % prime
            if not (2 <= multiplier <= Q < R and target > 2):
                raise AssertionError(
                    "a legal complete-excess row escaped the strict no-go"
                )
            rows.append((node, Q, beta, residual, multiplier, target))
    return len(sinks[0]), rows


def dyadic_transduction(boundary: dict[str, int]) -> dict[str, object]:
    prime = boundary["p"]
    support = boundary["A"]
    R = boundary["R"]
    K = boundary["K"]
    L = 2 * K
    e = valuation_two(prime - 1)
    if valuation_two(K) != e - 2 or valuation_two(L) != e - 1:
        raise AssertionError("boundary 2-adic valuations changed")

    deficit_rows = []
    for s in range(1, e + 1):
        a = 1
        b = (prime - 1) // (2**s)
        j = s + 1
        budget = valuation_two(L) + valuation_two(a) - valuation_two(b)
        formal_E = Fraction(L * a, (2 ** (j - 1)) * b)
        if not (
            L % b == 0
            and gcd(a, b) == 1
            and (a - pow(2, j, R) * b) % R == 0
            and budget == s - 1
            and j - budget == 2
            and formal_E == Fraction(2 * prime - 1, 2)
        ):
            raise AssertionError("natural R+1 two-bit deficit changed")
        deficit_rows.append((s, j, budget))

    a, b, j = 4, 2 * prime - 1, 1
    budget = valuation_two(L) + valuation_two(a) - valuation_two(b)
    E = L * a // b
    n = (2 * L - E) // R
    alpha = n * K // E
    if not (
        L % a == 0
        and L % b == 0
        and gcd(a, b) == 1
        and (a - 2 * b) % R == 0
        and a < 2 * b
        and 1 <= j <= budget
        and E == 2 * (prime - 1) == R + 1
        and E % R == 1
        and L * L % E == 0
        and n == prime - 1
        and alpha == support
        and (2 * pow(b, -1, R)) % R == 1
        and Fraction(E, 4 * K) == Fraction(2, b)
    ):
        raise AssertionError("internal dyadic transduction failed")

    relation_vector = {}
    b_factors = bottom.factorization(b)
    for q, K_exponent in bottom.factorization(K).items():
        relation_exponent = (1 if q == 2 else 0) - b_factors.get(q, 0)
        if not -K_exponent <= relation_exponent <= K_exponent:
            raise AssertionError("short relation left the symmetric exponent box")
        relation_vector[q] = relation_exponent
    if any(q not in relation_vector for q in b_factors):
        raise AssertionError("short relation denominator left K support")

    if Fraction(4, n) - Fraction(1, alpha) != Fraction(R, K):
        raise AssertionError("source marker identity failed")
    if Fraction(4, prime) - Fraction(1, prime * K) != Fraction(R, K):
        raise AssertionError("target marker identity failed")

    return {
        "naive_deficit_rows": deficit_rows,
        "relation": {"a": a, "b": b, "j": j, "budget": budget},
        "relation_vector": relation_vector,
        "E": E,
        "n": n,
        "alpha": alpha,
    }


def centered_residues(R: int, K: int) -> set[int]:
    residues = {1}
    for q, exponent in bottom.factorization(K).items():
        residues = {
            left * pow(q, z, R) % R
            for left in residues
            for z in range(-exponent, exponent + 1)
        }
    return residues


def verify_direct_certificate(prime: int, denominators: tuple[int, int, int]) -> None:
    x, y, z = denominators
    if Fraction(1, x) + Fraction(1, y) + Fraction(1, z) != Fraction(4, prime):
        raise AssertionError("direct certificate identity failed")


def verify_controls() -> list[dict[str, object]]:
    controls = []
    expected = {
        73: {
            "sink_size": 24,
            "candidate_count": 10,
            "bounded_count": 86,
            "terminal": (20, 219, 4380),
        },
        193: {
            "sink_size": 6,
            "candidate_count": 6,
            "bounded_count": 319,
            "terminal": (50, 1380, 1331700),
        },
    }
    for prime, fixture in expected.items():
        boundary = least_c2_boundary(prime)
        structural = structural_no_go(boundary)
        sink_size, rows = bottom_complete_excess_rows(boundary)
        dyadic = dyadic_transduction(boundary)
        bounded = centered_residues(boundary["R"], boundary["K"])
        if not (
            sink_size == fixture["sink_size"]
            and len(rows) == fixture["candidate_count"]
            and min(row[-1] for row in rows) > 2
            and len(bounded) == fixture["bounded_count"]
            and boundary["R"] - 1 not in bounded
        ):
            raise AssertionError(f"p={prime} focused F/sink control changed")
        verify_direct_certificate(prime, fixture["terminal"])

        if prime == 73:
            gap, x, divisor = 7, 20, 1
            if not (
                x == (prime + gap) // 4
                and x * x % divisor == 0
                and divisor <= x
                and (x + divisor) % gap == 0
            ):
                raise AssertionError("p=73 gap-7 Type II conditions changed")
            witness = pow(2, -3, boundary["R"]) * pow(5, -3, boundary["R"])
            if witness % boundary["R"] != boundary["R"] - 1:
                raise AssertionError("p=73 unbounded F witness changed")
        else:
            if not (
                sympy.isprime(prime + 4)
                and (prime + 4) % 4 == 1
                and pow(5, 191, boundary["R"]) == boundary["R"] - 1
            ):
                raise AssertionError("p=193 D=1/F control changed")
            gap, x, divisor = 7, 50, 10
            if not (x == (prime + gap) // 4 and x * x % divisor == 0):
                raise AssertionError("p=193 gap-7 divisor conditions changed")
            if (prime * x + divisor) % gap:
                raise AssertionError("p=193 gap-7 Type I congruence changed")

        controls.append(
            {
                "p": prime,
                "state": (boundary["R"], boundary["K"], boundary["A"]),
                "sink_size": sink_size,
                "candidate_count": len(rows),
                "minimum_target_cofactor": min(row[-1] for row in rows),
                "dyadic": dyadic,
                "structural": structural,
                "direct_terminal": fixture["terminal"],
            }
        )
    return controls


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--verify", action="store_true", help="run focused theorem controls"
    )
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    controls = verify_controls()
    print("verified least-C=2 carry/dyadic capacity transduction")
    for row in controls:
        print(
            f"p={row['p']} state={row['state']} "
            f"sink_candidates={row['candidate_count']} "
            f"min_c={row['minimum_target_cofactor']} "
            f"n={row['dyadic']['n']} alpha={row['dyadic']['alpha']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
