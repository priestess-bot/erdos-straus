#!/usr/bin/env python3
"""Replay target-derived universal raw words for two strict root receipts.

The word proves actual raw reachability to the root endpoint.  It deliberately
does not create a persistent state or a recursive edge: its universal source
and both peeling blocks are reconstructed from the target chart itself.
"""

from __future__ import annotations

import argparse
from math import gcd, lcm

from type_i_root_capacity_general_endpoint_divisor_gate import chart


def is_prime_64(value: int) -> bool:
    """Deterministically recognize the fixed 64-bit raw labels."""
    if value < 2:
        return False
    for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if value % prime == 0:
            return value == prime
    odd = value - 1
    exponent = 0
    while odd % 2 == 0:
        odd //= 2
        exponent += 1
    for base in (2, 325, 9_375, 28_178, 450_775, 9_780_504, 1_795_265_022):
        if base % value == 0:
            continue
        witness = pow(base, odd, value)
        if witness in (1, value - 1):
            continue
        for _ in range(exponent - 1):
            witness = witness * witness % value
            if witness == value - 1:
                break
        else:
            return False
    return True


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def complete_excess(value: int, capacity: int) -> tuple[int, int]:
    """Return the maximal complete-excess block without factoring value."""
    common = gcd(value, capacity)
    exposed = value // common
    block = gcd(value, pow(exposed, value.bit_length(), value))
    return block, value // block


def replay_m_one_word(
    modulus: int,
    capacity: int,
    start: tuple[int, int],
    labels: tuple[int, ...],
) -> tuple[int, int]:
    """Replay a canonical m=1 capacity-peeling word with no gcd reduction."""
    left, right = start
    if not (
        left > 0
        and right > 0
        and left + right == modulus
        and gcd(left, right) == 1
    ):
        raise AssertionError("raw word has no primitive m=1 start")

    for index, prime in enumerate(labels, start=1):
        if not is_prime_64(prime):
            raise AssertionError(f"raw label {index} is not prime")
        selected = [side for side in (left, right) if side % prime == 0]
        if len(selected) != 1:
            raise AssertionError(f"raw label {index} has no unique selected side")
        selected_side = selected[0]
        other_side = right if selected_side == left else left
        if not (
            valuation(selected_side, prime) > valuation(capacity, prime)
            and gcd(prime, modulus * other_side) == 1
        ):
            raise AssertionError(f"raw label {index} fails capacity or unit gate")

        divided = selected_side // prime
        translated = other_side + (prime - 1) * divided
        if not (
            divided > 0
            and translated > 0
            and divided + translated == modulus
            and gcd(divided, translated) == 1
        ):
            raise AssertionError(f"raw label {index} changed the primitive node")
        left, right = sorted((divided, translated))
    return left, right


def universal_p_source_step(prime: int, modulus: int, capacity: int) -> tuple[int, int]:
    """Replay universal_p_source_v1 through its unique p-edge."""
    source = (prime, modulus * (prime - 1) - prime, prime - 1)
    if not (
        min(source) > 0
        and source[0] + source[1] == modulus * source[2]
        and gcd(source[0], source[1]) == 1
        and gcd(prime, modulus) == 1
        and valuation(source[0], prime) > valuation(capacity, prime)
    ):
        raise AssertionError("universal p source changed")

    selected = source[0] // prime
    other = (source[1] + modulus) // prime
    layer = (source[2] + 1) // prime
    if not (selected == 1 and other == modulus - 1 and layer == 1):
        raise AssertionError("universal p source no longer reaches the anchor")
    return selected, other


def product(values: tuple[int, ...]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def canonical_target(prime: int, support: int) -> dict[str, int]:
    cofactor = pow(4 * support, -1, prime)
    capacity = support * cofactor
    remainder = (4 * capacity - 1) // prime
    return {
        "cofactor": cofactor,
        "capacity": capacity,
        "remainder": remainder,
        "deficit": prime - cofactor,
        "denominator": 4 * support - remainder,
    }


def replay_root_word(
    prime: int,
    parameter: int,
    anchor_labels: tuple[int, ...],
    endpoint_labels: tuple[int, ...],
    expected_cofactor: int,
) -> dict[str, int]:
    data = chart(prime, parameter)
    R = data["R"]
    K = data["K"]
    A = data["A"]
    h = data["h"]
    b = 2 * parameter * (prime - 1) - 1
    anchor_quotient = (R - 1) // (prime + 1)
    endpoint_quotient = (R - (prime + 1)) // h

    if not (
        prime % 24 == 1
        and R % prime == 1
        and R - 1 == prime * (prime + 1) * b
        and K == (prime + 1) * (prime - 1) // 2 * data["T"]
        and gcd(R - 1, K) == prime + 1
        and gcd(R - (prime + 1), K) == h
        and product(anchor_labels) == anchor_quotient
        and product(endpoint_labels) == endpoint_quotient
        and tuple(sorted(anchor_labels)) == anchor_labels
        and tuple(sorted(endpoint_labels)) == endpoint_labels
    ):
        raise AssertionError("root capacity quotients changed")

    anchor = universal_p_source_step(prime, R, K)
    if anchor != (1, R - 1):
        raise AssertionError("universal source anchor changed")
    root_anchor = replay_m_one_word(R, K, anchor, anchor_labels)
    if root_anchor != (prime + 1, R - (prime + 1)):
        raise AssertionError("capacity word no longer reaches p+1")
    endpoint = replay_m_one_word(R, K, root_anchor, endpoint_labels)
    if endpoint != (h, R - h):
        raise AssertionError("capacity word no longer reaches 3u")

    z = endpoint[1]
    Q, beta = complete_excess(z, K)
    g_A = gcd(A, Q)
    E = Q // g_A
    D = beta * g_A
    support = lcm(A, Q)
    target = canonical_target(prime, support)
    bound = (prime - 1) ** 2 // 4
    source_rank = (bound // A, K // A)
    target_rank = (bound // support, target["capacity"] // support)
    endpoint_cofactor = D * pow(h - 1, -1, prime) % prime

    if not (
        data["u"] < data["M"]
        and Q > 1
        and z == Q * beta
        and gcd(Q, beta) == 1
        and K % (h * beta) == 0
        and Q % prime != 0
        and E == Q // g_A
        and D == beta * g_A
        and support == A * E
        and target["cofactor"] == endpoint_cofactor == expected_cofactor < prime - 1
        and source_rank == (0, prime - 1)
        and target_rank == (0, expected_cofactor)
        and target_rank < source_rank
    ):
        raise AssertionError("strict root receipt or rank descent changed")

    return {
        "anchor_quotient": anchor_quotient,
        "endpoint_quotient": endpoint_quotient,
        "h": h,
        "z": z,
        "Q": Q,
        "beta": beta,
        "E": E,
        "D": D,
        "cofactor": target["cofactor"],
    }


def verify() -> None:
    first = replay_root_word(
        73,
        3,
        anchor_labels=(73, 431),
        endpoint_labels=(73, 10_631),
        expected_cofactor=37,
    )
    second = replay_root_word(
        313,
        271,
        anchor_labels=(11, 313, 15_373),
        endpoint_labels=(313, 97_787),
        expected_cofactor=298,
    )
    if not (
        first["anchor_quotient"] == 31_463
        and first["endpoint_quotient"] == 776_063
        and first["z"] == 2_328_260
        and (first["Q"], first["beta"], first["E"], first["D"])
        == (10_583, 220, 10_583, 220)
        and second["anchor_quotient"] == 52_929_239
        and second["endpoint_quotient"] == 30_607_331
        and second["z"] == 16_619_780_504
        and (second["Q"], second["beta"], second["E"], second["D"])
        == (2_077_472_563, 8, 2_077_472_563, 8)
    ):
        raise AssertionError("fixed root-word controls changed")

    try:
        replay_root_word(
            313,
            271,
            anchor_labels=(11, 313, 15_372),
            endpoint_labels=(313, 97_787),
            expected_cofactor=298,
        )
    except AssertionError:
        pass
    else:
        raise AssertionError("target-derived word accepted a tampered factor label")

    print(
        "verified two target-derived universal root words, their strict receipts, "
        "and the analysis-only E1 policy boundary"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
