#!/usr/bin/env python3
"""Replay the R4/R6 h-supported carrier partition.

The universal assertions live in the matching claim's elementary
factorization and modulo-three proofs.  The records below are typed controls
for tie-breaks and rejection codes; they are not actual persistent receipts.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, replace
from math import prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECEIPT_PATH = ROOT / "data" / "t6-wave1" / "f3-tr1-h-supported-carrier-v1.json"

R4 = "R4_M3_NONQ5_H_SUPPORTED"
R6 = "R6_MGT3_H_SUPPORTED"

R4_RESIDUAL = "R4_H_MENU_AND_DSTAR_TERMINALS_MISS_NO_TR1_TARGET"
R6_RESIDUAL = "R6_H_MENU_AND_DSTAR_TERMINALS_MISS_NO_TR1_TARGET"


class PartitionError(ValueError):
    """Reject a fixture outside the frozen R4/R6 arithmetic projection."""


@dataclass(frozen=True)
class CarrierHeaderV1:
    route_code: str
    h: int
    m: int
    k: int
    d_star: int
    terminal_first_hit: bool = False
    root_menu_hit: bool = False
    dstar_menu_hit: bool = False


def factorization(value: int) -> dict[int, int]:
    if value < 1:
        raise PartitionError("factorization expects a positive integer")
    result: dict[int, int] = {}
    divisor = 2
    remaining = value
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            result[divisor] = result.get(divisor, 0) + 1
            remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        result[remaining] = result.get(remaining, 0) + 1
    return result


def k_perp(k: int, h: int) -> int:
    return prod(
        prime**exponent
        for prime, exponent in factorization(k).items()
        if h % prime
    )


def least_prime(value: int) -> int:
    factors = factorization(value)
    if not factors:
        raise PartitionError("one has no prime carrier")
    return min(factors)


def r4_root_carrier(header: CarrierHeaderV1) -> int:
    if header.m != 3 or header.k % 3:
        raise PartitionError("R4 requires m=3 and k=3*kappa")
    kappa = header.k // 3
    if not (kappa >= 31 and kappa % 24 == 7):
        raise PartitionError("R4 primitive kappa guard failed")
    candidates = [prime for prime in factorization(kappa) if prime % 12 == 7]
    if not candidates:
        raise PartitionError("kappa=7 mod24 lost its 7 mod12 prime")
    carrier = min(candidates)
    if header.h % carrier or carrier == 3:
        raise PartitionError("R4 canonical carrier is not root-supported")
    return carrier


def r6_root_carrier(header: CarrierHeaderV1) -> int | None:
    if header.m <= 3:
        raise PartitionError("R6 requires m>3")
    if header.m % 3 == 1:
        if header.k % 3 == 0:
            raise PartitionError("m=1 mod3 cannot have 3|k")
        carrier = least_prime(header.k)
    elif header.m % 3 == 0:
        if header.k % 3 or (header.k // 3) % 3 == 0:
            raise PartitionError("m=0 mod3 requires v3(k)=1")
        if header.k == 3:
            return None
        carrier = least_prime(header.k // 3)
    else:
        raise PartitionError("actual m cannot be 2 mod3")
    if carrier == 3 or header.h % carrier:
        raise PartitionError("R6 canonical carrier is not root-supported")
    return carrier


def classify(header: CarrierHeaderV1) -> dict[str, object]:
    if header.route_code not in {R4, R6}:
        raise PartitionError("route is not owned by Agent 6")
    if not (header.h >= 2 and header.k > 1 and header.d_star > 1):
        raise PartitionError("low-height arithmetic payload is incomplete")
    if k_perp(header.k, header.h) != 1:
        raise PartitionError("QUOTIENT_ONLY_NOT_OWNED")
    if header.route_code == R4 and header.d_star % 5 == 0:
        raise PartitionError("M3_Q5_NOT_OWNED")
    if header.terminal_first_hit:
        return {"outcome": "TERMINAL_FIRST", "recursive": False}

    root_carrier = (
        r4_root_carrier(header)
        if header.route_code == R4
        else r6_root_carrier(header)
    )
    transverse_factor = least_prime(header.d_star)
    if header.h % transverse_factor == 0:
        raise PartitionError("D_star carrier is not transverse")
    if header.root_menu_hit:
        if root_carrier is None:
            raise PartitionError("k=3 has no nonthree root carrier")
        return {
            "outcome": "ROOT_SUPPORTED_MENU_TERMINAL",
            "root_carrier": root_carrier,
            "recursive": False,
        }
    if header.dstar_menu_hit:
        return {
            "outcome": "DSTAR_MENU_TERMINAL",
            "transverse_factor_candidate": transverse_factor,
            "recursive": False,
        }
    return {
        "outcome": "OPEN_MINIMAL_RESIDUAL",
        "residual_code": R4_RESIDUAL if header.route_code == R4 else R6_RESIDUAL,
        "root_carrier": root_carrier,
        "transverse_factor_candidate": transverse_factor,
        "integer_raw_occurrence_bound": False,
        "E1_status": "OPEN",
        "whole_d_star": header.d_star,
        "k_perp": 1,
        "recursive": False,
    }


def fixture(**updates: object) -> CarrierHeaderV1:
    base = CarrierHeaderV1(
        route_code=R4,
        h=3 * 7 * 31,
        m=3,
        k=3 * 31,
        d_star=13,
    )
    return replace(base, **updates)


def verify_receipt() -> None:
    receipt = json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))
    if receipt.get("theorem_status") != "ESTABLISHED_MENU_FACTOR_PARTITION":
        raise AssertionError("menu/factor theorem status changed")
    if receipt.get("physicalization_status") != "OPEN_MINIMAL_RESIDUALS":
        raise AssertionError("physicalization was silently closed")
    if receipt.get("proved_empty") != ["NO_DSTAR_ARITHMETIC_FACTOR"]:
        raise AssertionError("empty-family boundary changed")
    boundaries = set(receipt.get("does_not_claim", []))
    for item in ("TR1PhysicalTransitionV1", "R4 closure", "R6 closure", "F3 closure"):
        if item not in boundaries:
            raise AssertionError(f"missing boundary {item}")


def verify() -> None:
    verify_receipt()
    r4 = classify(fixture())
    if not (
        r4["residual_code"] == R4_RESIDUAL
        and r4["root_carrier"] == 31
        and r4["transverse_factor_candidate"] == 13
        and not r4["integer_raw_occurrence_bound"]
        and r4["k_perp"] == 1
        and not r4["recursive"]
    ):
        raise AssertionError("R4 carrier partition changed")

    r6_one = classify(
        fixture(route_code=R6, h=3 * 7 * 13, m=4, k=7 * 13, d_star=17)
    )
    if not (
        r6_one["residual_code"] == R6_RESIDUAL
        and r6_one["root_carrier"] == 7
        and r6_one["transverse_factor_candidate"] == 17
    ):
        raise AssertionError("R6 m=1 mod3 branch changed")

    r6_zero = classify(
        fixture(route_code=R6, h=3 * 7 * 13, m=6, k=3 * 7, d_star=11)
    )
    if r6_zero["root_carrier"] != 7:
        raise AssertionError("R6 m=0 mod3 branch changed")

    r6_k_three = classify(fixture(route_code=R6, h=3 * 7, m=6, k=3, d_star=11))
    if not (
        r6_k_three["root_carrier"] is None
        and r6_k_three["transverse_factor_candidate"] == 11
        and r6_k_three["residual_code"] == R6_RESIDUAL
    ):
        raise AssertionError("R6 k=3 transverse-only leaf changed")

    try:
        classify(fixture(h=3 * 31, k=3 * 31 * 37))
    except PartitionError as error:
        if str(error) != "QUOTIENT_ONLY_NOT_OWNED":
            raise
    else:
        raise AssertionError("quotient-only carrier entered the h-supported track")

    try:
        classify(fixture(d_star=5 * 13))
    except PartitionError as error:
        if str(error) != "M3_Q5_NOT_OWNED":
            raise
    else:
        raise AssertionError("m=3 q=5 entered the R4 track")

    if classify(fixture(terminal_first_hit=True))["outcome"] != "TERMINAL_FIRST":
        raise AssertionError("terminal-first lost precedence")

    print("verified R4/R6 h-menu eligibility and D_star factor partition")
    print("fixtures are typed controls, not actual persistent receipt evidence")
    print("D_star is an arithmetic factor candidate; integer E1 and TR1 remain open")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
