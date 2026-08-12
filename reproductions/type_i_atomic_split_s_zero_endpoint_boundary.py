#!/usr/bin/env python3
"""Verify the atomic split admission and the s=0 endpoint boundary.

The verifier replays four fixed integer receipts.  It uses the factorization-
free complete-excess formula from the accompanying claim and performs no
prime-range, denominator, selector-history, or certificate-menu scan.
"""

from __future__ import annotations

import argparse
from math import gcd, lcm


P = 73
B_P = (P - 1) ** 2 // 4
S_ZERO_TREE_DEPTH = 3
S_ZERO_TREE_PARAMETER = (
    3_081_303_956_325_088_557_376_553_319_788_046_874_862_151_069_359_244_625_807_615_652_961_464_503
)
S_ZERO_TREE_MODULUS = (
    549_292_384_417_183_915_231_271_884_719_311_373_697_168_902_443_727_883_898_439_155
)
S_ZERO_ROOT_D0 = 4_799_665
S_ZERO_ROOT_SQUARE_CAPACITY = 23_036_784_112_225


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def complete_excess(value: int, capacity: int) -> tuple[int, int]:
    """Return the full over-capacity block and its residual without factoring."""
    common = gcd(value, capacity)
    exposed = value // common
    exponent = value.bit_length()
    residue = pow(exposed, exponent, value) if value > 1 else 0
    block = gcd(value, residue)
    return block, value // block


def chart(prime: int, parameter: int) -> dict[str, int]:
    g = (prime + 1) // 2
    b = 2 * prime * parameter - 1
    n = (prime + 1) * b - 1
    adjustable = prime * prime * parameter - g
    support = g * adjustable
    capacity = ((prime * prime - 1) // 2) * adjustable
    residual = (prime - 1) * n - 1
    if not (
        support == (prime * n - 1) // 4
        and capacity == support * (prime - 1)
        and prime * residual + 1 == 4 * capacity
    ):
        raise AssertionError("a=1,d=1 chart normalization changed")
    return {
        "g": g,
        "b": b,
        "n": n,
        "adjustable": adjustable,
        "support": support,
        "capacity": capacity,
        "residual": residual,
    }


def peeled_pair(
    data: dict[str, int], anchor: int, layers: int = 1
) -> tuple[int, int]:
    departure = data["residual"] - anchor
    if valuation(departure, P) != layers:
        raise AssertionError("root departure has the wrong p-adic height")
    y = departure // P**layers
    x = data["residual"] - y
    if gcd(x, y) != 1:
        raise AssertionError("raw p-peel unexpectedly needs gcd reduction")
    return x, y


def split_data(data: dict[str, int], x: int, y: int) -> dict[str, int]:
    q_x, beta_x = complete_excess(x, data["capacity"])
    q_y, beta_y = complete_excess(y, data["capacity"])
    g_x = gcd(data["support"], q_x)
    g_y = gcd(data["support"], q_y)
    target_support = lcm(data["support"], q_x, q_y)
    multiplier = target_support // data["support"]
    target_cofactor = pow(4 * target_support, -1, P)
    target_capacity = target_support * target_cofactor
    target_residual = (4 * target_capacity - 1) // P
    if not (
        q_x > 1
        and q_y > 1
        and x == q_x * beta_x
        and y == q_y * beta_y
        and gcd(q_x, beta_x) == 1
        and gcd(q_y, beta_y) == 1
        and gcd(x, y) == 1
        and data["capacity"] % (beta_x * beta_y) == 0
        and (q_x * q_y) % P != 0
        and target_support == data["support"] * multiplier
        and P * target_residual + 1 == 4 * target_capacity
    ):
        raise AssertionError("atomic split arithmetic changed")
    return {
        "q_x": q_x,
        "beta_x": beta_x,
        "q_y": q_y,
        "beta_y": beta_y,
        "g_x": g_x,
        "g_y": g_y,
        "target_support": target_support,
        "multiplier": multiplier,
        "target_cofactor": target_cofactor,
        "target_capacity": target_capacity,
        "target_residual": target_residual,
    }


def endpoint_receipt(data: dict[str, int], endpoint: int) -> dict[str, int]:
    z = data["residual"] - endpoint
    q, beta = complete_excess(z, data["capacity"])
    g_a = gcd(data["support"], q)
    multiplier = q // g_a
    if not (
        data["capacity"] % endpoint == 0
        and gcd(endpoint, z) == 1
        and z == q * beta
        and q > 1
        and data["capacity"] % (endpoint * beta) == 0
        and gcd(q, endpoint * beta) == 1
        and gcd(z, data["capacity"])
        == gcd(P * endpoint + 1, data["capacity"])
    ):
        raise AssertionError("endpoint complete-excess receipt changed")
    result = {
        "endpoint": endpoint,
        "z": z,
        "q": q,
        "beta": beta,
        "g_a": g_a,
        "multiplier": multiplier,
    }
    if q % P:
        result["target_cofactor"] = (-pow(multiplier, -1, P)) % P
    return result


def verify_atomic_split_admission() -> None:
    data = chart(P, 1)
    x, y = peeled_pair(data, anchor=1)
    split = split_data(data, x, y)
    if not (
        (x, y) == (761_905, 10_582)
        and (
            split["q_x"],
            split["beta_x"],
            split["q_y"],
            split["beta_y"],
        )
        == (761_905, 1, 143, 74)
        and split["target_support"] == 21_333_318_666_660
        and split["multiplier"] == 108_952_415
        and split["target_cofactor"] == 67
        and split["target_capacity"] == 1_429_332_350_666_220
        and split["target_residual"] == 78_319_580_858_423
    ):
        raise AssertionError("strict atomic split fixture changed")

    source_rank = (B_P // data["support"], data["capacity"] // data["support"])
    target_rank = (
        B_P // split["target_support"],
        split["target_capacity"] // split["target_support"],
    )
    if not source_rank == (0, 72) or not target_rank == (0, 67):
        raise AssertionError("atomic split rank comparison changed")

def verify_maximality_and_stutter_boundary() -> None:
    data = chart(P, 50)
    x, y = peeled_pair(data, anchor=P + 1)
    split = split_data(data, x, y)
    if not (
        (x, y) == (38_356_274, 532_725)
        and (
            split["q_x"],
            split["beta_x"],
            split["q_y"],
            split["beta_y"],
        )
        == (19_178_137, 2, 177_575, 3)
        and split["multiplier"] == 3_405_557_677_775
        and split["multiplier"] % P == 1
        and split["target_cofactor"] == 72
    ):
        raise AssertionError("canonical split stutter changed")

    # The colored identity and beta-product gate alone admit this false split.
    weak_q_x, weak_beta_x = x, 1
    weak_q_y, weak_beta_y = y, 1
    weak_support = lcm(data["support"], weak_q_x, weak_q_y)
    weak_multiplier = weak_support // data["support"]
    weak_cofactor = pow(4 * weak_support, -1, P)
    if not (
        4 * data["capacity"]
        == P * weak_q_x * weak_beta_x + P * weak_q_y * weak_beta_y + 1
        and data["capacity"] % (weak_beta_x * weak_beta_y) == 0
        and weak_multiplier == 20_433_346_066_650
        and weak_multiplier % P == 6
        and weak_cofactor == 12
    ):
        raise AssertionError("non-maximal arbitrary-rechart control changed")

    relay = (split["multiplier"] - 1) // P
    source_excess = (P - 1) * data["b"] - 1
    target_b = data["b"] * split["multiplier"] - relay
    target_excess = (P - 1) * target_b - 1
    if not (
        valuation(source_excess - 1, P) == 0
        and relay % P == 65
        and target_excess % P == 65
        and valuation(target_excess - 1, P) == 0
    ):
        raise AssertionError("old p-adic rank cannot distinguish split stutter")


def verify_small_endpoint_and_s_zero_restart() -> None:
    small = chart(P, 57)
    x, y = peeled_pair(small, anchor=P + 1)
    split = split_data(small, x, y)
    if not (
        (split["beta_x"], split["beta_y"], split["g_x"], split["g_y"])
        == (2, 3, 1, 1)
        and split["multiplier"] % (P * P) == 1
        and (gcd(x, small["capacity"]), gcd(y, small["capacity"])) == (2, 3)
    ):
        raise AssertionError("minimal s=0 endpoint cell changed")
    h2 = endpoint_receipt(small, 2)
    h3 = endpoint_receipt(small, 3)
    if not (
        (h2["beta"], h2["g_a"], h2["target_cofactor"]) == (21, 1, 21)
        and (h3["beta"], h3["g_a"], h3["target_cofactor"]) == (4, 1, 2)
    ):
        raise AssertionError("small endpoint strict carries changed")

    source = chart(P, 95_979)
    x, y = peeled_pair(source, anchor=P + 1)
    split = split_data(source, x, y)
    multiplier = split["multiplier"]
    if not (
        (
            split["q_x"],
            split["beta_x"],
            split["q_y"],
            split["beta_y"],
            split["g_x"],
            split["g_y"],
        )
        == (36_819_077_401, 2, 340_917_383, 3, 1, 1)
        and multiplier == 12_552_263_512_023_361_583
        and valuation(multiplier - 1, P) == 2
    ):
        raise AssertionError("s=0 root-restart source changed")

    t = (multiplier - 1) // (P * P)
    target_parameter = 95_979 + t * source["adjustable"]
    target = chart(P, target_parameter)
    target_support = source["support"] * multiplier
    if not (
        t == 2_355_463_222_372_558
        and target_parameter == 1_204_753_612_468_350_993_590_111
        and target_parameter % P == P - 1
        and target["adjustable"] == multiplier * source["adjustable"]
        and target["support"] == target_support
        and valuation(target["residual"] - (P + 1), P) == 2
    ):
        raise AssertionError("s=0 second-order relay changed")

    x2, y2 = peeled_pair(target, anchor=P + 1, layers=2)
    if (gcd(x2, target["capacity"]), gcd(y2, target["capacity"])) != (74, 3):
        raise AssertionError("s=0 target p^2-peel capacities changed")
    endpoint = endpoint_receipt(target, 3)
    if not (
        endpoint["beta"] == 4
        and endpoint["g_a"] == 1
        and endpoint["q"] == 234_290_844_523_945_154_425_456_065_041
        and endpoint["target_cofactor"] == 2
    ):
        raise AssertionError("s=0 target h=3 strict exit changed")


def verify_large_endpoint_p_block_boundary() -> None:
    data = chart(P, 21_944_065_678)
    x, y = peeled_pair(data, anchor=P + 1)
    split = split_data(data, x, y)
    if not (
        data["adjustable"] == 116_939_925_998_025
        and data["support"] == 4_326_777_261_926_925
        and data["residual"] == 17_070_025_362_122_663
        and data["capacity"] == 311_527_962_858_738_600
        and (x, y) == (16_836_189_398_257_970, 233_835_963_864_693)
        and (
            split["q_x"],
            split["beta_x"],
            split["q_y"],
            split["beta_y"],
            split["g_x"],
            split["g_y"],
        )
        == (3_158_759_737_009, 5_330, 43_278_912_431, 5_403, 1, 1)
        and split["multiplier"] == 136_707_686_048_581_100_858_879
        and valuation(split["multiplier"] - 1, P) == 2
        and (gcd(x, data["capacity"]), gcd(y, data["capacity"])) == (5_330, 5_403)
    ):
        raise AssertionError("large-endpoint s=0 split changed")

    first = endpoint_receipt(data, 5_330)
    second = endpoint_receipt(data, 5_403)
    if not (
        (first["q"], first["beta"], first["g_a"])
        == (5_690_008_454_039_111, 3, 1)
        and (second["q"], second["beta"], second["g_a"])
        == (43_278_802_703, 394_420, 1)
        and valuation(first["q"], P) == valuation(second["q"], P) == 1
        and first["q"] // P == 77_945_321_288_207
        and second["q"] // P == 592_860_311
        and first["endpoint"] % P == second["endpoint"] % P == 1
        and "target_cofactor" not in first
        and "target_cofactor" not in second
    ):
        raise AssertionError("dual immediate endpoint p-free failures changed")


def verify_s_zero_depth_three_tree() -> None:
    data = chart(P, S_ZERO_TREE_PARAMETER)
    control_parameter = 21_944_065_678
    levels: list[list[int]] = [[P + 1]]
    for _ in range(S_ZERO_TREE_DEPTH):
        levels.append(
            [
                child
                for endpoint in levels[-1]
                for child in (P * endpoint + 1, P * endpoint - P + 1)
            ]
        )
    fixed_base = (P * P - 1) // 2
    tree_modulus = 1
    for endpoint in (item for level in levels for item in level):
        tree_modulus = lcm(tree_modulus, endpoint // gcd(endpoint, fixed_base))
    if not (
        tree_modulus == S_ZERO_TREE_MODULUS
        and data["adjustable"] % tree_modulus == 0
        and S_ZERO_ROOT_D0 == 5 * 13 * 41 * 1801
        and S_ZERO_ROOT_SQUARE_CAPACITY == S_ZERO_ROOT_D0**2
        and data["adjustable"] % S_ZERO_ROOT_SQUARE_CAPACITY == 0
        and S_ZERO_TREE_PARAMETER % (P * P) == 396
        and control_parameter % (P * P) == 396
        and (S_ZERO_TREE_PARAMETER - control_parameter)
        % (P * P * S_ZERO_ROOT_D0)
        == 0
        and all(
            data["capacity"] % endpoint == 0
            for endpoint in (item for level in levels for item in level)
        )
        and all(
            valuation(data["residual"] - endpoint, P) == 1
            for endpoint in (item for level in levels[:-1] for item in level)
        )
    ):
        raise AssertionError("depth-three s=0 capacity tree changed")

    x, y = peeled_pair(data, anchor=P + 1)
    split = split_data(data, x, y)
    if not (
        (gcd(x, data["capacity"]), gcd(y, data["capacity"])) == (5_330, 5_403)
        and (split["beta_x"], split["beta_y"], split["g_x"], split["g_y"])
        == (5_330, 5_403, 1, 1)
        and split["q_x"] == (383_616 * S_ZERO_TREE_PARAMETER - 2_663) // 2_665
        and split["q_y"] == (3_552 * S_ZERO_TREE_PARAMETER - 25) // 1_801
        and split["q_x"] % (P * P) == 3_158_759_737_009 % (P * P)
        and split["q_y"] % (P * P) == 43_278_912_431 % (P * P)
        and split["multiplier"] % (P * P) == 1
    ):
        raise AssertionError("s=0 root cell did not survive the depth-three tree")


def verify() -> None:
    verify_atomic_split_admission()
    verify_maximality_and_stutter_boundary()
    verify_small_endpoint_and_s_zero_restart()
    verify_large_endpoint_p_block_boundary()
    verify_s_zero_depth_three_tree()
    print(
        "verified 2 atomic split controls, 2 small strict endpoints, "
        "1 s=0 root-restart counterexample, 1 dual p-block endpoint boundary, "
        "and 1 depth-3 s=0 capacity tree"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify to replay the fixed receipts")
    verify()


if __name__ == "__main__":
    main()
