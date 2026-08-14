#!/usr/bin/env python3
"""Verify the rigid q=1 d=1 regeneration closure.

This focused verifier replays the finite odd contradiction, two fixed even
q=1 macro receipts, and one complete two-relay receipt. It does not scan a
prime range, enumerate Egyptian-fraction solutions, or claim a total selector.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, lcm

import type_ii_q_one_full_carrier_second_anchor_fixed_n_macro as q_one_macro
import type_ii_q_one_full_carrier_second_anchor_overflow as second_anchor
import type_ii_q_one_type_i_carrier_rail_dispatch as rail


@dataclass(frozen=True)
class OddCandidate:
    prime: int
    t: int
    j: int
    n: int
    g: int
    obstruction: int


@dataclass(frozen=True)
class EvenFixture:
    name: str
    t: int
    expected_prime: int
    expected_capacity: int


# This is the exact finite candidate table forced by p <= 790 in the proof,
# not a historical prime-range experiment.
ODD_CANDIDATES = (
    OddCandidate(73, 3, 1, 17, 1, 76),
    OddCandidate(313, 13, 9, 673, 1, 132),
    OddCandidate(409, 17, 1, 97, 1, 76),
    OddCandidate(457, 19, 5, 545, 1, 104),
    OddCandidate(601, 25, 11, 1577, 1, 146),
)

EVEN_FIXTURES = (
    EvenFixture("p193_q23_rigid_two_step", 8, 193, 78),
    EvenFixture("p13441_q23_rigid_formula", 560, 13_441, 2_689),
)


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def universal_p_source(prime: int, residual: int, capacity: int) -> bool:
    """Replay the primitive p-source when its raw gate is open."""
    source = (prime, residual * (prime - 1) - prime, prime - 1)
    destination = (
        source[0] // prime,
        (source[1] + residual) // prime,
        (source[2] + 1) // prime,
    )
    return bool(
        min(source) > 0
        and source[0] + source[1] == residual * source[2]
        and gcd(source[0], source[1]) == 1
        and capacity % prime
        and source[0] % prime == 0
        and (source[1] + residual) % prime == 0
        and (source[2] + 1) % prime == 0
        and destination == (1, residual - 1, 1)
    )


def odd_regeneration_exclusion() -> list[dict[str, int]]:
    """Replay all candidates left by the symbolic odd-branch p <= 790 bound."""
    prime_table = tuple(
        24 * t + 1 for t in range(3, 33, 2) if rail.is_prime(24 * t + 1)
    )
    if prime_table != tuple(row.prime for row in ODD_CANDIDATES):
        raise AssertionError("odd finite core-prime table changed")

    receipts: list[dict[str, int]] = []
    for row in ODD_CANDIDATES:
        prime, t = row.prime, row.t
        j_values = tuple(j for j in range(1, 14) if (j * prime - 3) % 14 == 0)
        if j_values != (row.j,):
            raise AssertionError(f"p={prime}: odd j congruence changed")
        j = j_values[0]
        delta = (j * prime - 3) // 14
        n = (5 * j * prime + 7 * j - 15) // 21
        alpha, v = (prime + 1) // 2, (n + 1) // 2
        g = gcd(alpha, v)
        obstruction = 7 * j + 42 * g + 27
        multiplier = (prime - 1) * (v // g) - (alpha // g)
        if not (
            prime == 24 * t + 1
            and t % 2 == 1
            and 73 <= prime <= 790
            and 1 <= j <= 13
            and 14 * delta + 3 == j * prime
            and 21 * n == 5 * j * prime + 7 * j - 15
            and 3 * (7 * v) - 5 * j * alpha == j + 3
            and (j + 3) % g == 0
            and (n, g, obstruction) == (row.n, row.g, row.obstruction)
            and obstruction % prime != 0
            and multiplier % prime != 1
        ):
            raise AssertionError(f"p={prime}: odd regeneration exclusion changed")
        receipts.append(
            {
                "prime": prime,
                "t": t,
                "j": j,
                "n": n,
                "g": g,
                "obstruction": obstruction,
            }
        )
    return receipts


def even_rigid_form(fixture: EvenFixture) -> dict[str, int | str]:
    """Replay a q=1 macro instance in the proved rigid regeneration form."""
    row = q_one_macro.even_macro(fixture.t)
    postmacro = q_one_macro.postmacro_full_product(row)
    if postmacro["status"] != "strict_full_product_fold":
        raise AssertionError(f"{fixture.name}: macro did not reach a d=1 receiver")

    prime = int(row["prime"])
    s = fixture.t // 2
    q_star = int(row["selected_carrier"]["q_star"])
    fold = row["fold"]
    delta, n = int(fold["delta"]), int(fold["n"])
    receiver = postmacro["successor"]
    A, R, K = (int(receiver[field]) for field in ("support", "R", "K"))
    j, remainder = divmod(3 * q_star * delta - 4, prime)
    alpha, v = (prime + 1) // 2, (n + 1) // 2
    g = gcd(alpha, v)
    a, b = alpha // g, v // g
    multiplier = (prime - 1) * b - a
    relay = (multiplier - 1) // prime

    excess = second_anchor.complete_excess(R - 1, K)
    Q = int(excess["Q"])
    carrier = lcm(A, Q)
    target = second_anchor.canonical_chart(prime, carrier)
    target_R, target_K = int(target["R"]), int(target["K"])
    target_n = (4 * carrier + 1) // prime
    first_capacity = target_K // carrier

    next_b = b * multiplier - a * relay
    next_multiplier = (prime - 1) * next_b - a
    next_capacity = (-pow(next_multiplier, -1, prime)) % prime
    inverse_four = pow(4, -1, prime)
    inverse_five = pow(5, -1, prime)

    if not (
        prime == fixture.expected_prime
        and prime == 48 * s + 1
        and rail.is_prime(prime)
        and prime % 24 == 1
        and q_star == 23
        and q_star >= 5
        and (6 * s - 1) % q_star == 0
        and remainder == 0
        and 1 <= j < 3 * q_star < prime
        and j % 3 == 2
        and 4 * n == j * prime + 4 - j
        and 4 * v - j * alpha == 4 - j
        and g == 1
        and j == 20
        and n == 5 * prime - 4
        and A == (prime * n - 1) // 4
        and R == (prime - 1) * n - 1
        and K == A * (prime - 1)
        and multiplier == (5 * prime * prime - 9 * prime + 2) // 2
        and multiplier % prime == 1
        and relay == (5 * prime - 9) // 2
        and valuation(multiplier - 1, prime) == 1
        and Q % prime != 0
        and carrier == A * multiplier
        and first_capacity == prime - 1
        and prime * target_n == 4 * carrier + 1
        and target_n == multiplier * n - relay
        and target_R == (prime - 1) * target_n - 1
        and target_K == carrier * (prime - 1)
        and b % prime != 0
        and b % prime != (-a) % prime
        and next_b % prime == (3 * inverse_four) % prime
        and next_multiplier % prime == (-5 * inverse_four) % prime
        and next_b % prime != 0
        and next_b % prime != (-a) % prime
        and next_multiplier % prime != 1
        and next_capacity == (4 * inverse_five) % prime
        and 1 <= next_capacity <= prime - 2
        and next_capacity == fixture.expected_capacity
        and universal_p_source(prime, R, K)
        and universal_p_source(prime, target_R, target_K)
    ):
        raise AssertionError(f"{fixture.name}: rigid regeneration form changed")

    return {
        "name": fixture.name,
        "prime": prime,
        "q_star": q_star,
        "j": j,
        "n": n,
        "g": g,
        "multiplier": multiplier,
        "regeneration_eta": valuation(multiplier - 1, prime),
        "next_multiplier_residue": next_multiplier % prime,
        "next_capacity": next_capacity,
        "carrier": carrier,
        "target_n": target_n,
        "target_R": target_R,
        "target_K": target_K,
    }


def complete_two_step_receipt(first: dict[str, int | str]) -> dict[str, object]:
    """Materialize the second bundle for the small fixed p=193 receipt."""
    prime = int(first["prime"])
    if prime != 193:
        raise AssertionError("the full second-bundle receipt is fixed at p=193")

    carrier, R, K = (int(first[field]) for field in ("carrier", "target_R", "target_K"))
    alpha = (prime + 1) // 2
    target_n = int(first["target_n"])
    v = (target_n + 1) // 2
    g = gcd(alpha, v)
    a, b = alpha // g, v // g
    exact_excess = second_anchor.complete_excess(R - 1, K)
    Q = int(exact_excess["Q"])
    next_carrier = lcm(carrier, Q)
    multiplier = next_carrier // carrier
    target = second_anchor.canonical_chart(prime, next_carrier)
    next_R, next_K = int(target["R"]), int(target["K"])
    capacity = next_K // next_carrier
    B_p = (prime - 1) ** 2 // 4
    source_potential = (B_p // carrier, prime - 1, 0)
    target_potential = (B_p // next_carrier, capacity, 0)

    if not (
        g == 1
        and a == alpha
        and multiplier == (prime - 1) * b - a
        and multiplier % prime == 47
        and Q % prime != 0
        and next_carrier == carrier * multiplier
        and capacity == 78
        and 1 <= capacity <= prime - 2
        and prime * next_R + 1 == 4 * next_K
        and next_K == next_carrier * capacity
        and universal_p_source(prime, R, K)
        and source_potential > target_potential
    ):
        raise AssertionError("p=193 second strict capacity relay changed")
    return {
        "prime": prime,
        "second_multiplier": multiplier,
        "capacity": capacity,
        "source_potential": source_potential,
        "target_potential": target_potential,
        "raw_source_ok": True,
        "p_free_bundle_ok": Q % prime != 0,
    }


def verify() -> None:
    odd = odd_regeneration_exclusion()
    even = [even_rigid_form(fixture) for fixture in EVEN_FIXTURES]
    two_step = complete_two_step_receipt(even[0])
    if not (
        len(odd) == 5
        and all(int(row["q_star"]) == 23 for row in even)
        and all(int(row["regeneration_eta"]) == 1 for row in even)
        and two_step["capacity"] == 78
        and two_step["raw_source_ok"]
        and two_step["p_free_bundle_ok"]
    ):
        raise AssertionError("q=1 regeneration closure classification changed")
    print(
        "verified q=1 d=1 regeneration closure: 5 exact odd contradictions, "
        "2 rigid q*=23 even forms, and 1 full two-step capacity receipt"
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
