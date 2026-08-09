#!/usr/bin/env python3
"""Verify the d=3 high-carrier overflow reduction window."""

from __future__ import annotations

import argparse


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def smallest_prime_factor(value: int) -> int:
    if value % 2 == 0:
        return 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return divisor
        divisor += 2
    return value


def canonical_chart(p: int, n: int, modulus: int, depth: int) -> dict[str, int]:
    remainder = 4 * modulus - n
    cofactor = modulus * (p - depth)
    assert remainder > 0
    assert cofactor > 0
    assert p * remainder + 1 == 4 * cofactor
    assert remainder % 4 == 3
    return {"M": modulus, "d": depth, "R": remainder, "K": cofactor}


def classify(p: int, n: int, modulus: int, depth: int, support: int) -> dict[str, object]:
    assert p % 24 == 1
    assert depth == 3
    assert 3 * p - 2 <= n <= 4 * p - 11
    assert p * n == 12 * modulus + 1
    budget = (p - 1) ** 2 // 4
    assert modulus > budget
    assert modulus % support == 0
    assert 1 <= support <= budget

    c = (p - 1) // 4
    result: dict[str, object] = {
        "p": p,
        "n": n,
        "M": modulus,
        "d": depth,
        "A": support,
        "B": budget,
        "c": c,
    }
    if support < c:
        assert budget // c < budget // support
        assert (p - 1) % 4 == 0
        result.update({"status": "D3_FIXED_S", "L": c, "rd": c})
        return result

    b = modulus // support
    assert b > 1
    result["b"] = b
    if not is_prime(b):
        q = smallest_prime_factor(b)
        assert q * q <= b
        assert 3 * q < p
        successor = canonical_chart(p, n, modulus // q, 3 * q)
        assert successor["M"] < modulus
        assert successor["M"] % support == 0
        result.update({
            "status": "D3_COFACTOR_FACTOR_TRANSFER",
            "q": q,
            "successor": successor,
        })
        return result

    assert b != p
    if b < p:
        if b in (2, 3):
            successor = canonical_chart(p, n, support, 3 * b)
            route = "D3_SMALL_PRIME_FACTOR_TRANSFER"
        else:
            assert 3 < b
            successor = canonical_chart(p, n, 3 * support, b)
            route = "D3_PRIME_COFACTOR_EXCHANGE"
        assert successor["M"] < modulus
        assert successor["M"] % support == 0
        result.update({"status": route, "successor": successor})
        return result

    assert b > p
    L = b
    S = modulus * depth
    assert S % L == 0
    assert support < L <= budget
    assert 4 * L > n
    assert budget // L < budget // support
    successor = canonical_chart(p, n, L, S // L)
    result.update({
        "status": "D3_FIXED_N_SUPPORT_RESET",
        "L": L,
        "successor": successor,
    })
    return result


def verify() -> None:
    fixtures = {
        "support_below_c": (193, 577, 9280, 3, 1),
        "composite_cofactor": (193, 577, 9280, 3, 58),
        "prime_two": (193, 577, 9280, 3, 4640),
        "prime_three": (193, 601, 9666, 3, 3222),
        "prime_between": (193, 577, 9280, 3, 320),
        "prime_above_p": (193, 721, 11596, 3, 52),
    }
    receipts = {
        name: classify(*values) for name, values in fixtures.items()
    }
    assert receipts["support_below_c"]["status"] == "D3_FIXED_S"
    assert receipts["composite_cofactor"]["status"] == "D3_COFACTOR_FACTOR_TRANSFER"
    assert receipts["composite_cofactor"]["q"] == 2
    assert receipts["prime_two"]["status"] == "D3_SMALL_PRIME_FACTOR_TRANSFER"
    assert receipts["prime_two"]["successor"]["d"] == 6
    assert receipts["prime_three"]["status"] == "D3_SMALL_PRIME_FACTOR_TRANSFER"
    assert receipts["prime_three"]["successor"]["d"] == 9
    assert receipts["prime_between"]["status"] == "D3_PRIME_COFACTOR_EXCHANGE"
    assert receipts["prime_between"]["successor"]["M"] == 960
    assert receipts["prime_above_p"]["status"] == "D3_FIXED_N_SUPPORT_RESET"
    assert receipts["prime_above_p"]["L"] == 223

    for receipt in receipts.values():
        if "successor" in receipt:
            successor = receipt["successor"]
            assert successor["R"] > 0
            assert successor["K"] > 0

    print("verified d=3 overflow capacity-window reduction controls")
    for name, receipt in receipts.items():
        print(name, receipt["status"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
