#!/usr/bin/env python3
"""Verify the C=2 rank-one retention exhaustion and chart reindexing."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd

import sympy


def valuation_two(value: int) -> int:
    exponent = 0
    while value % 2 == 0:
        value //= 2
        exponent += 1
    return exponent


def chart_menu(prime: int) -> tuple[int, ...]:
    n = prime - 1
    return tuple(E for E in sympy.divisors(n * n // 4) if E % 4 == 0)


def all_d_only_candidates(prime: int) -> tuple[int, ...]:
    n = prime - 1
    N = prime * n
    return tuple(
        D
        for D in sympy.divisors(N * N)
        if D < n * n and D % 4 == 0 and (N * N // D) % 4 == 0
    )


def centered_certificates(prime: int, E: int) -> tuple[tuple[int, int, int, int], ...]:
    n = prime - 1
    R = E - 1
    K = (prime * R + 1) // 4
    rows = []
    for z in sympy.divisors(K * K):
        if z >= K or (z + K) % R:
            continue
        x = (K + z) // R
        y = (K + K * K // z) // R
        gap = (4 * z + 1) // R
        divisor = x * x // z
        alpha = n * K // E
        if not (
            4 * K == prime * R + 1
            and (4 * K - E) // R == n
            and Fraction(4, n) - Fraction(1, alpha) == Fraction(R, K)
            and Fraction(4, prime) - Fraction(1, prime * K) == Fraction(R, K)
            and Fraction(1, alpha) + Fraction(1, x) + Fraction(1, y) == Fraction(4, n)
            and Fraction(1, prime * K) + Fraction(1, x) + Fraction(1, y)
            == Fraction(4, prime)
            and 3 <= gap <= prime - 2
            and gap % 4 == 3
            and x * x % divisor == 0
            and (prime * x + divisor) % gap == 0
            and (prime * x + divisor) // gap == y
        ):
            raise AssertionError("centered Type I reconstruction failed")
        rows.append((z, gap, x, divisor))
    return tuple(rows)


def d_only_marked_fiber_has_witness(prime: int, D: int) -> bool:
    n = prime - 1
    N = prime * n
    a = (N - D) // 4
    M = 4 * a - n
    S = n * a
    common = gcd(M, S)
    mu = M // common
    sigma = S // common
    return any((z + sigma) % mu == 0 for z in sympy.divisors(sigma * sigma))


def verify_menu_bijection(prime: int) -> dict[str, object]:
    if not sympy.isprime(prime) or prime % 24 != 1:
        raise ValueError("expected a core prime")
    n = prime - 1
    menu = chart_menu(prime)
    candidates = all_d_only_candidates(prime)
    source = tuple(D for D in candidates if n * n % D == 0)
    non_source = tuple(D for D in candidates if n * n % D)
    mapped_source = tuple(sorted(n * n // E for E in menu))

    e = valuation_two(n)
    odd_part = n // (2**e)
    expected_capacity = (2 * e - 3) * sympy.divisor_count(odd_part * odd_part)
    if not (
        len(menu) == expected_capacity
        and source == mapped_source
        and set(candidates) == set(source) | set(non_source)
        and set(source).isdisjoint(non_source)
    ):
        raise AssertionError("D-only/source-chart bijection failed")

    for E in menu:
        R = E - 1
        K = (prime * R + 1) // 4
        D = n * n // E
        alpha = n * K // E
        a = (prime * n - D) // 4
        a_prime = ((prime * n) ** 2 // D - prime * n) // 4
        if not (
            E % 4 == 0
            and (n * n // 4) % E == 0
            and D in source
            and a == alpha
            and a_prime == prime * K
            and Fraction(4, n) - Fraction(1, alpha) == Fraction(R, K)
            and Fraction(4, prime) - Fraction(1, prime * K) == Fraction(R, K)
        ):
            raise AssertionError("source-supported chart reindexing failed")

    for D in non_source:
        if not (
            D % prime == 0
            and D % (prime * prime) != 0
            and not d_only_marked_fiber_has_witness(prime, D)
        ):
            raise AssertionError("rank-one non-source empty-fiber control failed")

    c2_E = 2 * n
    c2_R = 2 * prime - 3
    c2_K = n * (2 * prime - 1) // 4
    c2_D = n // 2
    c2_alpha = n * (2 * prime - 1) // 8
    if not (
        c2_E in menu
        and (c2_E - 1, (prime * (c2_E - 1) + 1) // 4) == (c2_R, c2_K)
        and n * n // c2_E == c2_D
        and n * c2_K // c2_E == c2_alpha
        and not centered_certificates(prime, c2_E)
    ):
        raise AssertionError("natural C=2 chart did not embed as the expected miss")

    hits = tuple((E, *row) for E in menu for row in centered_certificates(prime, E))
    return {
        "p": prime,
        "menu_size": len(menu),
        "candidate_count": len(candidates),
        "source_count": len(source),
        "non_source_count": len(non_source),
        "c2_E": c2_E,
        "hits": hits,
    }


def common_denominator_witnesses(
    prime: int, denominator: int
) -> tuple[tuple[int, int, int], ...]:
    R = 4 * denominator - prime
    S = prime * denominator
    rows = []
    for factor in sympy.divisors(S * S):
        complement = S * S // factor
        if (factor + S) % R or (complement + S) % R:
            continue
        rows.append(
            (
                factor,
                (S + factor) // R,
                (S + complement) // R,
            )
        )
    return tuple(rows)


def verify_gap_three_priority() -> None:
    prime = 97
    source = (25, 1200, 1200)
    target = (25, 970, 4850)
    if not (
        sum((Fraction(1, value) for value in source), Fraction())
        == Fraction(4, prime - 1)
        and sum((Fraction(1, value) for value in target), Fraction())
        == Fraction(4, prime)
        and source[0] == target[0] == (prime + 3) // 4
        and source[0] < (prime + 7) // 4
    ):
        raise AssertionError("gap-3 terminal-first priority control failed")


def verify_gap_seven(
    prime: int, expected_factor: int, expected_target: tuple[int, int, int]
) -> dict[str, object]:
    n = prime - 1
    marker = (prime + 7) // 4
    tail = n * (prime + 7) // 16
    if Fraction(1, marker) + Fraction(2, tail) != Fraction(4, n):
        raise AssertionError("universal gap-7 source slice failed")

    witnesses = common_denominator_witnesses(prime, marker)
    selected = next((row for row in witnesses if row[0] == expected_factor), None)
    if selected is None:
        raise AssertionError("expected gap-7 target factor disappeared")
    target = tuple(sorted((marker, selected[1], selected[2])))
    reduced_gate = tuple(
        q
        for q in sympy.divisors(marker * marker)
        if (4 * q + 1) % 7 == 0 or (marker + q) % 7 == 0
    )
    if not (
        4 * marker - prime == 7
        and reduced_gate
        and target == expected_target
        and sum((Fraction(1, value) for value in target), Fraction())
        == Fraction(4, prime)
    ):
        raise AssertionError("gap-7 terminal equivalence control failed")
    return {
        "marker": marker,
        "tail": tail,
        "target_factor": expected_factor,
        "target": target,
        "reduced_gate_count": len(reduced_gate),
    }


def verify_controls() -> list[dict[str, object]]:
    verify_gap_three_priority()
    expected = {
        73: {
            "counts": (22, 15, 7),
            "hits": (
                (4, 5, 7, 20, 80),
                (4, 11, 15, 22, 44),
                (24, 40, 7, 20, 10),
                (24, 63, 11, 21, 7),
            ),
            "factor": 73,
            "target": (20, 219, 4380),
        },
        193: {
            "counts": (40, 27, 13),
            "hits": (
                (4, 5, 7, 50, 500),
                (4, 29, 39, 58, 116),
                (8, 26, 15, 52, 104),
                (144, 250, 7, 50, 10),
            ),
            "factor": 10,
            "target": (50, 1380, 1331700),
        },
    }
    controls = []
    for prime, fixture in expected.items():
        menu = verify_menu_bijection(prime)
        counts = (
            menu["candidate_count"],
            menu["source_count"],
            menu["non_source_count"],
        )
        if counts != fixture["counts"] or menu["hits"] != fixture["hits"]:
            raise AssertionError(f"p={prime} focused complete menu changed")
        gap_seven = verify_gap_seven(
            prime,
            expected_factor=fixture["factor"],
            expected_target=fixture["target"],
        )
        controls.append({**menu, "gap_seven": gap_seven})
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
    print("verified C=2 rank-one retention exhaustion")
    for row in controls:
        hit_charts = sorted({item[0] for item in row["hits"]})
        print(
            f"p={row['p']} menu={row['menu_size']} "
            f"D={row['candidate_count']}="
            f"{row['source_count']}+{row['non_source_count']} "
            f"hit_E={hit_charts} c2_E={row['c2_E']} "
            f"gap7={row['gap_seven']['target']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
