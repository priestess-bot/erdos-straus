#!/usr/bin/env python3
"""Verify focused universal-source, capacity-anchor, and overflow-dual receipts."""

from __future__ import annotations

import argparse
import json
from math import gcd, isqrt, lcm, prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-universal-anchor-overflow-dual-results.json"
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def factorization(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = 1
    return factors


def divisors(value: int) -> list[int]:
    result = [1]
    for prime, exponent in factorization(value).items():
        old = tuple(result)
        power = 1
        for _ in range(exponent):
            power *= prime
            result.extend(item * power for item in old)
    return sorted(result)


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def jacobi_symbol(numerator: int, denominator: int) -> int:
    if denominator <= 0 or denominator % 2 == 0:
        raise ValueError("Jacobi denominator must be positive and odd")
    numerator %= denominator
    result = 1
    while numerator:
        while numerator % 2 == 0:
            numerator //= 2
            if denominator % 8 in (3, 5):
                result = -result
        numerator, denominator = denominator, numerator
        if numerator % 4 == denominator % 4 == 3:
            result = -result
        numerator %= denominator
    return result if denominator == 1 else 0


def canonical_chart(prime: int, support: int) -> tuple[int, int]:
    modulus = 4 * support
    R = (-pow(prime, -1, modulus)) % modulus
    if not 1 <= R < modulus:
        raise AssertionError("canonical chart representative left its range")
    K = (prime * R + 1) // 4
    if K % support:
        raise AssertionError("canonical support did not divide its K")
    return R, K


def complete_bundle(value: int, K: int) -> tuple[int, int]:
    K_factors = factorization(K)
    Q = prod(
        prime**exponent
        for prime, exponent in factorization(value).items()
        if exponent > K_factors.get(prime, 0)
    )
    return Q, value // Q


def universal_p_source(prime: int, R: int) -> dict[str, object]:
    K = (prime * R + 1) // 4
    U = prime
    V = R * (prime - 1) - prime
    m = prime - 1
    if not (
        is_prime(prime)
        and prime % 24 == 1
        and 3 <= R <= prime - 2
        and U + V == R * m
        and gcd(U, V) == 1
        and K % prime != 0
        and valuation(U, prime) > valuation(K, prime)
    ):
        raise AssertionError("universal p-source normal form failed")
    shift = 1
    destination = (U // prime, (V + R * shift) // prime, (m + shift) // prime)
    if destination != (1, R - 1, 1) or gcd(destination[0], destination[1]) != 1:
        raise AssertionError("universal p-source did not reach the anchor")
    return {
        "source": [U, V, m],
        "edge": {
            "q": prime,
            "shift": shift,
            "gcd_reduction": 1,
            "destination": list(destination),
        },
    }


def G_separator(R: int, K: int) -> dict[str, object]:
    values = {
        str(prime): jacobi_symbol(prime, R) for prime in factorization(K)
    }
    target = jacobi_symbol(-1, R)
    if target == 1 or any(value != 1 for value in values.values()):
        raise AssertionError("focused state did not have the stated G separator")
    return {"support_values": values, "target_minus_one": target}


def strip_to_capacity(selected: int, R: int, K: int) -> dict[str, object]:
    if gcd(selected, R) != 1:
        raise AssertionError("capacity stripping requires a primitive bottom side")
    target = gcd(selected, K)
    current = selected
    steps: list[dict[str, object]] = []
    K_factors = factorization(K)
    for prime in sorted(factorization(selected)):
        while valuation(current, prime) > K_factors.get(prime, 0):
            source = sorted((current, R - current))
            current //= prime
            destination = sorted((current, R - current))
            if gcd(current, R) != 1:
                raise AssertionError("capacity stripping introduced a gcd reduction")
            steps.append(
                {
                    "source": source,
                    "q": prime,
                    "destination": destination,
                }
            )
    if current != target:
        raise AssertionError("capacity stripping did not end at gcd(selected,K)")
    return {"selected": selected, "target": target, "steps": steps}


def anchor_orbit(prime: int, R: int, A: int) -> dict[str, object]:
    K = (prime * R + 1) // 4
    if K % A:
        raise AssertionError("absorbed support did not divide K")
    h = 1
    seen: list[int] = []
    rows: list[dict[str, object]] = []
    while h not in seen:
        seen.append(h)
        other = R - h
        if K % other == 0:
            rows.append({"h": h, "other": other, "classification": "terminal"})
            return {"orbit": seen, "rows": rows, "terminal": h}
        Q, beta = complete_bundle(other, K)
        if Q <= 1 or K % (h * beta) or gcd(Q, h * beta) != 1:
            raise AssertionError("path-anchored complete bundle failed")
        overlap = gcd(Q, K)
        next_h = beta * overlap
        if next_h != gcd(other, K):
            raise AssertionError("capacity anchor formula failed")
        excess_quotient = Q // overlap
        if other != excess_quotient * next_h:
            raise AssertionError("capacity quotient factorization failed")
        M = lcm(A, Q)
        R_M, K_M = canonical_chart(prime, M)
        rows.append(
            {
                "h": h,
                "other": other,
                "Q": Q,
                "beta": beta,
                "overlap": overlap,
                "next_h": next_h,
                "excess_quotient": excess_quotient,
                "M": M,
                "R_M": R_M,
                "K_M": K_M,
                "classification": "marked_absorb" if R_M < prime else "overflow",
                "strip": strip_to_capacity(other, R, K),
            }
        )
        h = next_h
    start = seen.index(h)
    cycle = seen[start:]
    cycle_rows = rows[start:]
    quotient_product = prod(int(row["excess_quotient"]) for row in cycle_rows)
    if quotient_product % R != (-1 if len(cycle) % 2 else 1) % R:
        raise AssertionError("capacity-cycle telescoping identity failed")
    return {
        "orbit": seen,
        "rows": rows,
        "cycle": cycle,
        "cycle_excess_quotient_product": quotient_product,
        "cycle_product_mod_R": quotient_product % R,
    }


def overflow_receipt(prime: int, M: int) -> dict[str, int]:
    R_M, K_M = canonical_chart(prime, M)
    if R_M <= prime:
        raise AssertionError("focused carrier was not an overflow")
    C = K_M // M
    n = 4 * M - R_M
    d = prime - C
    if min(n, d) <= 0 or prime * n != 4 * M * d + 1:
        raise AssertionError("overflow determinant failed")
    return {"M": M, "R_M": R_M, "K_M": K_M, "C": C, "n": n, "d": d}


def symmetric_dual(prime: int, M: int, d: int) -> dict[str, object]:
    r = M % prime
    if not 1 <= r < prime or not 1 <= d < prime:
        raise AssertionError("symmetric residues left (0,p)")
    numerator = 4 * r * d + 1
    if numerator % prime:
        raise AssertionError("symmetric quotient was not integral")
    s = numerator // prime
    R_d = 4 * d - s
    R_r = 4 * r - s
    K_d = d * (prime - r)
    K_r = r * (prime - d)
    if not (
        canonical_chart(prime, d) == (R_d, K_d)
        and canonical_chart(prime, r) == (R_r, K_r)
        and min(R_d, R_r) < prime
    ):
        raise AssertionError("symmetric dual-chart theorem failed")
    return {
        "r": r,
        "s": s,
        "d_chart": {"support": d, "R": R_d, "K": K_d},
        "r_chart": {"support": r, "R": R_r, "K": K_r},
        "smaller_chart_supports": [
            value
            for value, chart_R in ((d, R_d), (r, R_r))
            if chart_R < prime
        ],
    }


def fixed_n_window(prime: int, A: int, receipt: dict[str, int]) -> dict[str, object]:
    n = receipt["n"]
    S = receipt["M"] * receipt["d"]
    if 4 * S != prime * n - 1:
        raise AssertionError("fixed-n product changed")
    candidates = [
        L
        for L in divisors(S)
        if L % A == 0 and L > A and n < 4 * L < prime + n
    ]
    rows = []
    B_p = (prime - 1) ** 2 // 4
    for L in candidates:
        R_L = 4 * L - n
        K_L = L * (prime - S // L)
        if canonical_chart(prime, L) != (R_L, K_L):
            raise AssertionError("fixed-n atlas chart failed")
        if not (R_L < prime and B_p // L < B_p // A):
            raise AssertionError("fixed-n atlas edge did not descend")
        rows.append({"L": L, "R_L": R_L, "K_L": K_L})
    return {
        "S": S,
        "lower_numerator": n,
        "upper_numerator": prime + n,
        "support_preserving_candidates": rows,
    }


def root_dual_profile(prime: int, R: int, Q: int) -> dict[str, object]:
    if not Q < R < prime:
        raise AssertionError("root dual requires Q<R<p")
    receipt = overflow_receipt(prime, Q)
    d = receipt["d"]
    n = receipt["n"]
    R_d = 4 * d - n
    K_d = d * (prime - Q)
    B_p = (prime - 1) ** 2 // 4
    if not (
        d >= 2
        and canonical_chart(prime, d) == (R_d, K_d)
        and 3 <= R_d <= prime - 2
        and B_p // d < B_p
    ):
        raise AssertionError("A=1 overflow dual edge failed")
    window = fixed_n_window(prime, 1, receipt)
    if d not in [row["L"] for row in window["support_preserving_candidates"]]:
        raise AssertionError("root d was absent from the fixed-n divisor window")
    return {
        "prime": prime,
        "R": R,
        "Q": Q,
        "overflow": receipt,
        "dual_edge": {"support": d, "R": R_d, "K": K_d},
        "fixed_n_window": window,
    }


def lcm_dual_cycle_profile() -> dict[str, object]:
    prime, R, A, Q = 73, 47, 66, 23
    K = (prime * R + 1) // 4
    if K % A or complete_bundle(R - 1, K) != (Q, 2):
        raise AssertionError("focused lcm-cycle source state changed")
    M_0 = lcm(A, Q)
    receipt_0 = overflow_receipt(prime, M_0)
    M_1 = lcm(A, receipt_0["d"])
    receipt_1 = overflow_receipt(prime, M_1)
    M_2 = lcm(A, receipt_1["d"])
    if not (
        (M_0, receipt_0["R_M"], receipt_0["n"], receipt_0["d"])
        == (1518, 3743, 2329, 28)
        and (M_1, receipt_1["R_M"], receipt_1["n"], receipt_1["d"])
        == (924, 1367, 2329, 46)
        and M_2 == M_0
    ):
        raise AssertionError("support-preserving lcm dual two-cycle changed")
    return {
        "prime": prime,
        "R": R,
        "K": K,
        "A": A,
        "steps": [receipt_0, receipt_1],
        "returned_M": M_2,
        "classification": "support_preserving_lcm_dual_two_cycle",
    }


def bottom_reach(R: int, K: int, start: tuple[int, int]) -> list[tuple[int, int]]:
    pending = [tuple(sorted(start))]
    seen: set[tuple[int, int]] = set()
    while pending:
        node = pending.pop()
        if node in seen:
            continue
        seen.add(node)
        left, right = node
        for prime in factorization(left * right):
            if valuation(left * right, prime) <= valuation(K, prime):
                continue
            selected = left if left % prime == 0 else right
            destination = tuple(sorted((selected // prime, R - selected // prime)))
            if gcd(*destination) != 1:
                raise AssertionError("bottom raw edge introduced a gcd reduction")
            pending.append(destination)
    return sorted(seen)


def reachable_accumulated_conflict_profile() -> dict[str, object]:
    prime, root_R = 73, 39
    root_K = (prime * root_R + 1) // 4
    root_Q, root_beta = complete_bundle(root_R - 1, root_K)
    if (root_K, root_Q, root_beta) != (712, 19, 2):
        raise AssertionError("reachable conflict root changed")
    state_R, state_K = canonical_chart(prime, root_Q)
    A = root_Q
    if (state_R, state_K) != (51, 931):
        raise AssertionError("reachable conflict absorbed state changed")

    nodes = bottom_reach(state_R, state_K, (1, state_R - 1))
    if [node[0] for node in nodes] != [
        1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 19, 20, 22, 23, 25
    ]:
        raise AssertionError("reachable conflict bottom Reach changed")
    if any((left * right) and state_K % (left * right) == 0 for left, right in nodes):
        raise AssertionError("reachable conflict unexpectedly acquired a raw terminal")

    receipts: list[dict[str, object]] = []
    for node in nodes:
        for x, y in (node, tuple(reversed(node))):
            Q, beta = complete_bundle(y, state_K)
            if Q <= 1 or state_K % (x * beta) or gcd(Q, x * beta) != 1:
                continue
            M = lcm(A, Q)
            overflow = overflow_receipt(prime, M)
            dual = symmetric_dual(prime, M, overflow["d"])
            support_preserving = []
            for key in ("d_chart", "r_chart"):
                chart = dual[key]
                support = int(chart["support"])
                charged = lcm(A, support)
                if (
                    int(chart["R"]) < prime
                    and int(chart["K"]) % charged == 0
                    and charged > A
                ):
                    support_preserving.append(
                        {"carrier": support, "charged_support": charged, "chart": key}
                    )
            receipts.append(
                {
                    "node": list(node),
                    "orientation": [x, y],
                    "Q": Q,
                    "beta": beta,
                    "M": M,
                    "overflow": overflow,
                    "dual": dual,
                    "support_preserving_duals": support_preserving,
                }
            )
    receipts.sort(key=lambda row: int(row["Q"]))
    if [row["Q"] for row in receipts] != [2, 32, 44, 50]:
        raise AssertionError("reachable conflict bundle menu changed")
    if any(row["support_preserving_duals"] for row in receipts):
        raise AssertionError("reachable conflict unexpectedly acquired a dual edge")
    return {
        "prime": prime,
        "root": {
            "R": root_R,
            "K": root_K,
            "classification": "G",
            "G_separator": G_separator(root_R, root_K),
            "source_receipt": universal_p_source(prime, root_R),
            "anchor_bundle": {"Q": root_Q, "beta": root_beta},
        },
        "absorbed_state": {
            "R": state_R,
            "K": state_K,
            "A": A,
            "classification": "not_needed_for_receipt",
        },
        "reachable_nodes": [list(node) for node in nodes],
        "bundle_receipts": receipts,
        "classification": "reachable_accumulated_support_conflict_for_current_menu",
    }


def build_results() -> dict[str, object]:
    G_absorb_p, G_absorb_R = 73, 71
    G_absorb_K = (G_absorb_p * G_absorb_R + 1) // 4
    G_over_p, G_over_R = 73, 35
    G_over_K = (G_over_p * G_over_R + 1) // 4

    G_absorb_orbit = anchor_orbit(G_absorb_p, G_absorb_R, 1)
    G_over_orbit = anchor_orbit(G_over_p, G_over_R, 1)
    accumulated_cycle = anchor_orbit(409, 251, 5)
    if not (
        G_absorb_orbit["rows"][0]["Q"] == 35
        and G_absorb_orbit["rows"][0]["R_M"] == 23
        and G_absorb_orbit["rows"][0]["classification"] == "marked_absorb"
        and G_over_orbit["rows"][0]["Q"] == 34
        and G_over_orbit["rows"][0]["R_M"] == 95
        and G_over_orbit["rows"][0]["classification"] == "overflow"
        and accumulated_cycle["cycle"] == [1, 5, 3]
        and all(row["classification"] == "overflow" for row in accumulated_cycle["rows"])
    ):
        raise AssertionError("focused anchor classifications changed")

    overlap_strip = strip_to_capacity(328, 335, 56_364)
    if overlap_strip["target"] != 4 or [step["q"] for step in overlap_strip["steps"]] != [2, 41]:
        raise AssertionError("overlapping capacity strip changed")

    root_profiles = [
        root_dual_profile(73, 35, 34),
        root_dual_profile(241, 79, 71),
    ]
    if root_profiles[1]["dual_edge"]["R"] != 79:
        raise AssertionError("same-chart determinant charge changed")

    positive = overflow_receipt(409, 250)
    positive_window = fixed_n_window(409, 5, positive)
    if 200 not in [row["L"] for row in positive_window["support_preserving_candidates"]]:
        raise AssertionError("positive accumulated dual edge disappeared")

    d_one = overflow_receipt(73, 91)
    if d_one["d"] != 1 or lcm(7, d_one["d"]) != 7:
        raise AssertionError("d=1 accumulated boundary changed")

    empty_window_receipt = overflow_receipt(241, 190)
    empty_window = fixed_n_window(241, 38, empty_window_receipt)
    if empty_window["support_preserving_candidates"]:
        raise AssertionError("fixed-n empty divisor window unexpectedly acquired an edge")

    conflict = overflow_receipt(241, 568)
    conflict_dual = symmetric_dual(241, 568, conflict["d"])
    if not (
        conflict_dual["d_chart"]["R"] == 319
        and conflict_dual["r_chart"]["R"] == 167
        and conflict_dual["smaller_chart_supports"] == [86]
    ):
        raise AssertionError("symmetric support-conflict boundary changed")
    t = 86
    L = lcm(8, t)
    if conflict_dual["r_chart"]["K"] % L == 0:
        raise AssertionError("small symmetric chart unexpectedly retained old support")

    return {
        "schema_version": 1,
        "scope": "Focused algebraic receipts only; no historical census is rerun.",
        "universal_anchor": {
            "G_marked_absorb": {
                "prime": G_absorb_p,
                "R": G_absorb_R,
                "K": G_absorb_K,
                "G_separator": G_separator(G_absorb_R, G_absorb_K),
                "source_receipt": universal_p_source(G_absorb_p, G_absorb_R),
                "anchor_orbit": G_absorb_orbit,
            },
            "G_bundle_overflow": {
                "prime": G_over_p,
                "R": G_over_R,
                "K": G_over_K,
                "G_separator": G_separator(G_over_R, G_over_K),
                "source_receipt": universal_p_source(G_over_p, G_over_R),
                "anchor_orbit": G_over_orbit,
            },
            "accumulated_all_overflow_cycle": {
                "prime": 409,
                "R": 251,
                "K": 25_665,
                "A": 5,
                "source_receipt": universal_p_source(409, 251),
                "anchor_orbit": accumulated_cycle,
            },
            "overlapping_capacity_strip": {
                "prime": 673,
                "R": 335,
                "K": 56_364,
                "node": [7, 328],
                "strip": overlap_strip,
            },
        },
        "overflow_dual": {
            "root_edges": root_profiles,
            "accumulated_positive_fixed_n_edge": {
                "prime": 409,
                "A": 5,
                "overflow": positive,
                "window": positive_window,
            },
            "accumulated_d_one_boundary": {
                "prime": 73,
                "R": 23,
                "K": 420,
                "A": 7,
                "node": [10, 13],
                "Q": 13,
                "overflow": d_one,
            },
            "empty_fixed_n_window": {
                "prime": 241,
                "R": 111,
                "K": 6_688,
                "A": 38,
                "node": [1, 110],
                "Q": 5,
                "overflow": empty_window_receipt,
                "window": empty_window,
            },
            "symmetric_small_chart_support_conflict": {
                "prime": 241,
                "R": 79,
                "K": 4_760,
                "A": 8,
                "node": [8, 71],
                "Q": 71,
                "overflow": conflict,
                "dual": conflict_dual,
                "small_chart_required_support": L,
            },
            "lcm_dual_cycle": lcm_dual_cycle_profile(),
            "reachable_accumulated_full_menu_conflict": (
                reachable_accumulated_conflict_profile()
            ),
        },
        "summary": {
            "universal_p_source_count": 3,
            "G_source_gap_eliminated_count": 2,
            "capacity_anchor_cycle_count": 1,
            "root_dual_verified_edge_count": len(root_profiles),
            "accumulated_fixed_n_positive_count": len(
                positive_window["support_preserving_candidates"]
            ),
            "accumulated_support_conflict_count": 5,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    results = build_results()
    rendered = json.dumps(results, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.verify:
        if not args.output.exists() or args.output.read_text(encoding="utf-8") != rendered:
            raise SystemExit("stored focused result does not match regenerated output")
        print("verified", args.output)
        return
    args.output.write_text(rendered, encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
