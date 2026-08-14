#!/usr/bin/env python3
"""Verify q=1 postmacro d=1 p-free-gate exclusion and strict relays.

The input is only the persistent full-product successor produced by the q=1
second-anchor macro. This verifier checks the two symbolic parity normal
forms which exclude the p-free failure gate, then materializes one actual
complete-excess relay. It does not search for Egyptian-fraction solutions or
claim a total selector after a later d=1 regeneration target.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, lcm

import type_ii_q_one_full_carrier_second_anchor_fixed_n_macro as q_one_macro
import type_ii_q_one_full_carrier_second_anchor_overflow as second_anchor
import type_ii_q_one_type_i_carrier_rail_dispatch as rail


@dataclass(frozen=True)
class Fixture:
    name: str
    branch: str
    t: int
    expected_source_prime: int
    expected_case: str
    expected_capacity: int


FIXTURES = (
    Fixture("odd_low_support_capacity", "odd", 3, 73, "capacity", 27),
    Fixture("odd_low_support_capacity_large", "odd", 105, 2521, "capacity", 316),
    Fixture("even_regeneration", "even", 8, 193, "regeneration", 192),
    Fixture("even_high_support_capacity", "even", 10, 241, "capacity", 73),
    Fixture("even_raw_p_gate_relay", "even", 32, 7, "capacity", 2),
    Fixture("even_shared_gcd_capacity", "even", 112, 2689, "capacity", 1127),
)


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def least_coprime_prime(forbidden: int) -> int:
    candidate = 2
    while True:
        if rail.is_prime(candidate) and forbidden % candidate:
            return candidate
        candidate += 1


def alternate_anchor_source(prime: int, R: int, K: int) -> dict[str, object]:
    """Use the deterministic source only when the raw p-source is nonprimitive."""
    if R % prime:
        receipt = q_one_macro.universal_p_source(prime, R, K)
        return {"kind": "universal_p", "prime": prime, **receipt}

    q = least_coprime_prime(R * K * (R - 1))
    U, V, m = q, R * (q - 1) - q, q - 1
    destination = (U // q, (V + R) // q, (m + 1) // q)
    if not (
        q != prime
        and rail.is_prime(q)
        and (R * K * (R - 1)) % q
        and V > 0
        and U + V == R * m
        and gcd(U, V) == 1
        and K % q
        and destination == (1, R - 1, 1)
    ):
        raise AssertionError("least-coprime anchor source did not replay")
    return {
        "kind": "least_coprime_prime",
        "prime": q,
        "source": [U, V, m],
        "q": q,
        "shift": 1,
        "gcd_reduction": 1,
        "destination": list(destination),
    }


def odd_gate_certificate(prime: int, t: int, L: int, delta: int, n: int) -> dict[str, int]:
    """Recover the odd-t closed form used to exclude n == -2 mod p."""
    numerator = 14 * delta + 3
    j, remainder = divmod(numerator, prime)
    if not (
        t % 2 == 1
        and L == (5 * prime + 7) // 6
        and 4 * L == (10 * prime + 14) // 3
        and remainder == 0
        and 1 <= j <= 13
        and 14 * delta + 3 == j * prime
        and 21 * n == 5 * j * prime + 7 * j - 15
        and prime >= 73
        and n % prime != prime - 2
    ):
        raise AssertionError("odd q=1 p-free gate exclusion did not replay")
    return {"j": j, "would_be_failure_multiple": 7 * j + 27}


def even_gate_certificate(
    prime: int, s: int, q_star: int, L: int, delta: int, n: int
) -> dict[str, int]:
    """Recover the even-t closed form used to exclude n == -2 mod p."""
    numerator = 3 * q_star * delta - 4
    j, remainder = divmod(numerator, prime)
    if not (
        q_star >= 5
        and rail.is_prime(q_star)
        and (6 * s - 1) % q_star == 0
        and L == 9 * s * q_star
        and 4 * L == 3 * q_star * (prime - 1) // 4
        and remainder == 0
        and 1 <= j < 3 * q_star < prime
        and 3 * q_star * delta - 4 == j * prime
        and 4 * n == j * prime + 4 - j
        and j % 3 == 2
        and n % prime != prime - 2
    ):
        raise AssertionError("even q=1 p-free gate exclusion did not replay")
    return {"j": j, "raw_p_gate_failure_exactly_when_j": 8}


def complete_excess_relay(fixture: Fixture) -> dict[str, object]:
    macro = (
        q_one_macro.odd_macro(fixture.t)
        if fixture.branch == "odd"
        else q_one_macro.even_macro(fixture.t)
    )
    postmacro = q_one_macro.postmacro_full_product(macro)
    if postmacro["status"] != "strict_full_product_fold":
        raise AssertionError("fixture did not reach the persistent d=1 overflow receiver")

    prime = int(macro["prime"])
    fold = macro["fold"]
    n = int(fold["n"])
    delta = int(fold["delta"])
    L = int(macro["target"]["support"])
    source_state = postmacro["successor"]
    A, R, K = (int(source_state[field]) for field in ("support", "R", "K"))
    Bp = (prime - 1) ** 2 // 4

    if fixture.branch == "odd":
        gate_certificate = odd_gate_certificate(prime, fixture.t, L, delta, n)
    else:
        s = fixture.t // 2
        q_star = int(macro["selected_carrier"]["q_star"])
        gate_certificate = even_gate_certificate(prime, s, q_star, L, delta, n)

    alpha, v = (prime + 1) // 2, (n + 1) // 2
    g = gcd(alpha, v)
    a, b = alpha // g, v // g
    excess = second_anchor.complete_excess(R - 1, K)
    Q, beta = int(excess["Q"]), int(excess["beta"])
    carrier = lcm(A, Q)
    E = carrier // A
    p_free_bundle = Q % prime != 0
    source_receipt = alternate_anchor_source(prime, R, K)
    raw_p_source = source_receipt["kind"] == "universal_p"
    target_chart = second_anchor.canonical_chart(prime, carrier)
    target_R, target_K = int(target_chart["R"]), int(target_chart["K"])
    capacity = target_K // carrier
    source_eta = valuation(E - 1, prime)
    source_potential = (Bp // A, K // A, source_eta)

    if E % prime == 1:
        step_case = "regeneration"
        quotient = (E - 1) // prime
        target_n = E * n - quotient
        target_excess = second_anchor.complete_excess(target_R - 1, target_K)
        target_Q = int(target_excess["Q"])
        target_E = lcm(carrier, target_Q) // carrier
        target_eta = valuation(target_E - 1, prime)
        normal_form = "q_one_full_carrier_d_one_regeneration_relay_v1"
        if not (
            capacity == prime - 1
            and target_n > 1
            and prime * target_n == 4 * carrier + 1
            and target_eta == source_eta - 1
        ):
            raise AssertionError("d=1 regeneration relay did not replay")
        target_potential = (Bp // carrier, capacity, target_eta)
    else:
        step_case = "capacity"
        target_n = 0
        normal_form = "q_one_full_carrier_d_one_capacity_relay_v1"
        if not (1 <= capacity <= prime - 2):
            raise AssertionError("nonregenerating d=1 relay did not lower capacity")
        target_potential = (Bp // carrier, capacity, 0)

    target_state = q_one_macro.macro_state(
        prime,
        target_R,
        target_K,
        carrier,
        "overflow",
        normal_form,
    )
    e1_e5 = {
        "E1": bool(
            postmacro["e1_e5"]["E1"]
            and source_receipt["destination"] == [1, R - 1, 1]
            and Q * beta == R - 1
            and K % beta == 0
            and gcd(Q, beta) == 1
            and K % Q != 0
        ),
        "E2": bool(
            carrier == A * E
            and carrier % Q == 0
            and target_K % carrier == 0
            and prime * target_R + 1 == 4 * target_K
        ),
        "E3": bool(
            source_state["source_tree_scope"] == target_state["source_tree_scope"]
            and source_state["equation_target"] == target_state["equation_target"]
            and source_state["state_id"] != target_state["state_id"]
            and target_R > prime
            and target_state["normal_form"] == normal_form
        ),
        "E4": bool(
            source_state["marked_solution_set"]
            == target_state["marked_solution_set"]
            == "Sol(p)"
        ),
        "E5": target_potential < source_potential,
    }
    if not (
        rail.is_prime(prime)
        and prime % 24 == 1
        and n > 1
        and n % 4 == 1
        and prime * n == 4 * A + 1
        and R == (prime - 1) * n - 1
        and K == A * (prime - 1)
        and p_free_bundle
        and n % prime != prime - 2
        and E == ((prime - 1) * b - a)
        and carrier > prime * prime > Bp
        and target_R > prime
        and raw_p_source == (n % prime != prime - 1)
        and int(source_receipt["prime"]) == fixture.expected_source_prime
        and step_case == fixture.expected_case
        and capacity == fixture.expected_capacity
        and all(e1_e5.values())
    ):
        raise AssertionError(f"{fixture.name}: q=1 d=1 relay receipt changed")

    return {
        "name": fixture.name,
        "prime": prime,
        "n": n,
        "gate_certificate": gate_certificate,
        "raw_source": source_receipt["kind"],
        "source_prime": source_receipt["prime"],
        "p_free_bundle": p_free_bundle,
        "normalized_g": g,
        "multiplier": E,
        "case": step_case,
        "capacity": capacity,
        "source_potential": source_potential,
        "target_potential": target_potential,
        "e1_e5": e1_e5,
    }


def verify() -> None:
    receipts = [complete_excess_relay(fixture) for fixture in FIXTURES]
    raw_alternate = sum(r["raw_source"] == "least_coprime_prime" for r in receipts)
    regenerations = sum(r["case"] == "regeneration" for r in receipts)
    odd = sum(fixture.branch == "odd" for fixture in FIXTURES)
    even = len(FIXTURES) - odd
    if not (
        all(r["p_free_bundle"] for r in receipts)
        and all(all(r["e1_e5"].values()) for r in receipts)
        and raw_alternate == 1
        and regenerations == 1
        and (odd, even) == (2, 4)
    ):
        raise AssertionError("focused q=1 d=1 relay classification changed")
    print(
        "verified 6 q=1 postmacro d=1 p-free exclusions and strict relays: "
        "2 odd, 4 even, 1 least-coprime raw-source repair, and 1 regeneration"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
