#!/usr/bin/env python3
"""Verify the least-C=3 high-support complete-excess carry no-go."""

from __future__ import annotations

import argparse
from math import gcd, lcm

import sympy

import type_i_bottom_sink_scc_complete_excess_bundle as bottom


def valuation(value: int, prime: int) -> int:
    """Return the exponent of prime in a positive integer."""
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def least_c3_boundary(prime: int) -> dict[str, int]:
    """Construct the least support above B_p in the canonical C=3 class."""
    if not sympy.isprime(prime) or prime % 24 != 1:
        raise ValueError("expected a core prime congruent to 1 modulo 24")
    h = (prime - 1) // 24
    bound = (prime - 1) ** 2 // 4
    support = (prime - 1) * (3 * prime - 1) // 12
    K = 3 * support
    R = 3 * prime - 4
    if not (
        h >= 3
        and support == 4 * h * (36 * h + 1)
        and support == bound + (prime - 1) // 6
        and support - prime < bound < support
        and 12 * support == prime * R + 1
        and K == (prime - 1) * (3 * prime - 1) // 4
        and 4 * K == prime * R + 1
        and K // support == 3
    ):
        raise AssertionError("least C=3 boundary formulas failed")
    return {"p": prime, "h": h, "B": bound, "A": support, "R": R, "K": K}


def low_cofactor_classes(prime: int) -> tuple[tuple[int, int], ...]:
    """List every 2 <= L < R with cL = 3 (mod p), for c <= 3."""
    classes = (
        (1, 3),
        (1, prime + 3),
        (1, 2 * prime + 3),
        (2, (prime + 3) // 2),
        (2, 3 * (prime + 1) // 2),
        (2, (5 * prime + 3) // 2),
        (3, prime + 1),
        (3, 2 * prime + 1),
    )
    R = 3 * prime - 4
    exhaustive = tuple(
        (cofactor, L)
        for cofactor in range(1, 4)
        for L in range(2, R)
        if (cofactor * L - 3) % prime == 0
    )
    if not (
        tuple(sorted(classes)) == exhaustive
        and all(2 <= L < R for _cofactor, L in classes)
    ):
        raise AssertionError("low-cofactor multiplier classification failed")
    return classes


def global_low_cofactor_obstructions() -> dict[str, tuple[int, ...]]:
    """Check the finite divisor contradictions used in the universal proof."""
    middle_divisors = tuple(
        divisor for divisor in sympy.divisors(20) if divisor >= 11 and divisor % 4 == 3
    )
    half_divisors = tuple(
        divisor for divisor in sympy.divisors(87) if divisor >= 21 and divisor % 16 == 5
    )
    last_divisors = tuple(divisor for divisor in sympy.divisors(21) if divisor >= 29)
    if middle_divisors or half_divisors or last_divisors:
        raise AssertionError("a universal low-cofactor divisor obstruction changed")
    return {
        "middle": middle_divisors,
        "half": half_divisors,
        "last": last_divisors,
    }


def structural_no_go(boundary: dict[str, int]) -> dict[str, object]:
    """Verify every c <= 3 multiplier class is structurally impossible."""
    prime, h, support, R, K = (
        boundary["p"],
        boundary["h"],
        boundary["A"],
        boundary["R"],
        boundary["K"],
    )
    classes = low_cofactor_classes(prime)
    if not (
        valuation(K, 2) == valuation(support, 2) == 2 + valuation(h, 2)
        and valuation(K, 3) == valuation(support, 3) + 1
        and valuation(3, 3) == valuation(3 * (prime + 1) // 2, 3) == 1
    ):
        raise AssertionError("C=3 full-block valuation gates changed")

    two_adic_classes = (prime + 3, (5 * prime + 3) // 2, prime + 1)
    two_adic_lower_bounds = {
        L: (2 ** valuation(support, 2)) * L for L in two_adic_classes
    }
    if not all(
        L % 2 == 0 and lower_bound > R
        for L, lower_bound in two_adic_lower_bounds.items()
    ):
        raise AssertionError("C=3 full-block 2-adic exclusion changed")
    one_three_classes = (3, 3 * (prime + 1) // 2)
    if not all(L % 3 == 0 and L % 9 != 0 for L in one_three_classes):
        raise AssertionError("C=3 one-3-adic multiplier exclusion changed")

    half_class = (prime + 3) // 2
    half_lower_bound = (2 ** valuation(support, 2)) * half_class
    if h % 2 == 0:
        if half_lower_bound <= R:
            raise AssertionError("even-h half multiplier escaped its 2-adic exclusion")
        half_case = {"h_parity": "even", "lower_bound": half_lower_bound}
    else:
        Q = 4 * half_class
        x = R - Q
        d = 8 * h - 3
        if not (
            Q > R // 2
            and Q < R
            and x == 3 * d
            and (4 * K // 3) % d == 87 % d
            and d % 16 == 5
            and d >= 21
        ):
            raise AssertionError("odd-h half multiplier divisor obstruction changed")
        half_case = {"h_parity": "odd", "Q": Q, "x": x, "residual_factor": d}

    L_middle = 2 * prime + 3
    L_last = 2 * prime + 1
    d_middle = 4 * h - 1
    if not (
        R // 2 < L_middle < R
        and R - L_middle == 6 * d_middle
        and (4 * K // 3) % d_middle == 40 % d_middle
        and d_middle >= 11
    ):
        raise AssertionError("C=3 middle odd multiplier geometry changed")

    last_case: dict[str, int | str]
    if valuation(L_last, 3) == 1:
        last_case = {"status": "one_3_adic_layer"}
    else:
        d_last = 6 * h - 1
        if not (
            h % 3 == 2
            and R // 2 < L_last < R
            and R - L_last == 4 * d_last
            and (3 * K) % d_last == 42 % d_last
            and d_last >= 17
        ):
            raise AssertionError("C=3 last odd multiplier geometry changed")
        last_case = {"status": "forced_residual", "residual_factor": d_last}
    return {
        "classes": classes,
        "two_adic_lower_bounds": two_adic_lower_bounds,
        "one_three_classes": one_three_classes,
        "half_class": half_case,
        "middle_odd_class": L_middle,
        "last_odd_class": last_case,
        "global_divisor_obstructions": global_low_cofactor_obstructions(),
    }


def bottom_complete_excess_rows(
    boundary: dict[str, int],
) -> tuple[int, list[tuple[object, ...]]]:
    """Enumerate the complete-excess rows only for named finite controls."""
    prime, support, R, K = (
        boundary["p"],
        boundary["A"],
        boundary["R"],
        boundary["K"],
    )
    factors = bottom.factorization(K)
    adjacency, _labels = bottom.bottom_graph(R, factors)
    sinks = bottom.sink_components(adjacency)
    if len(sinks) != 1:
        raise AssertionError("focused C=3 control lost its unique sink")
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
            target = 3 * pow(multiplier, -1, prime) % prime
            if not (2 <= multiplier <= Q < R and target > 3):
                raise AssertionError("a legal C=3 row escaped the strict carry no-go")
            rows.append((node, Q, beta, residual, multiplier, target))
    return len(sinks[0]), rows


def verify_controls() -> list[dict[str, object]]:
    """Run two small independent sink controls after the symbolic gate checks."""
    fixtures = {
        73: {"sink_size": 4, "candidate_count": 4, "minimum_target": 27},
        193: {"sink_size": 15, "candidate_count": 7, "minimum_target": 19},
    }
    controls = []
    for prime, fixture in fixtures.items():
        boundary = least_c3_boundary(prime)
        structural = structural_no_go(boundary)
        sink_size, rows = bottom_complete_excess_rows(boundary)
        if not (
            sink_size == fixture["sink_size"]
            and len(rows) == fixture["candidate_count"]
            and min(row[-1] for row in rows) == fixture["minimum_target"]
            and all(row[-1] > 3 for row in rows)
        ):
            raise AssertionError(f"p={prime} C=3 focused sink control changed")
        controls.append(
            {
                "p": prime,
                "state": (boundary["R"], boundary["K"], boundary["A"]),
                "sink_size": sink_size,
                "candidate_count": len(rows),
                "minimum_target_cofactor": min(row[-1] for row in rows),
                "structural": structural,
            }
        )
    return controls


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    controls = verify_controls()
    print("verified least-C=3 high-support complete-excess carry no-go")
    for row in controls:
        print(
            f"p={row['p']} state={row['state']} "
            f"sink_candidates={row['candidate_count']} "
            f"min_c={row['minimum_target_cofactor']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
