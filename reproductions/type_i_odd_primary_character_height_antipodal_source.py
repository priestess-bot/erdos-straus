#!/usr/bin/env python3
"""Verify character-height and antipodal source controls for odd-primary records."""

from __future__ import annotations

import argparse
from math import gcd

from type_i_core_jacobi_punctured_kernel_primary_selector import (
    analyze_core,
    multiplicative_order,
)
from type_i_odd_primary_component_kernel_crt_rechart_descent import odd_primary_data


def content(vector: tuple[int, ...]) -> int:
    result = 0
    for entry in vector:
        result = gcd(result, abs(entry))
    assert result > 0
    return result


def power_image(H: set[int], modulus: int, exponent: int) -> set[int]:
    return {pow(value, exponent, modulus) for value in H}


def character_height(H: set[int], modulus: int, ell: int, value: int) -> int:
    assert multiplicative_order(value, modulus) % ell == 0
    height = 0
    exponent = ell
    while value in power_image(H, modulus, exponent):
        height += 1
        exponent *= ell
    return height


def cyclic_logs(H: set[int], modulus: int) -> tuple[int, dict[int, int]]:
    for generator in sorted(H):
        if multiplicative_order(generator, modulus) != len(H):
            continue
        logs = {1: 0}
        current = 1
        for exponent in range(1, len(H)):
            current = current * generator % modulus
            logs[current] = exponent
        assert set(logs) == H
        return generator, logs
    raise AssertionError("focused controls require a cyclic generated group")


def cyclic_character(logs: dict[int, int], ell: int, height: int, value: int) -> int:
    return logs[value] % (ell ** (height + 1))


def check_record_source(
    prime: int,
    modulus: int,
    K: int,
    vector: tuple[int, ...],
    ell: int,
    expected: dict[str, object],
) -> tuple[set[int], dict[int, int], dict[str, int]]:
    core = analyze_core(prime, modulus, K)
    assert not core["target_hits"] and not core["collisions"]
    H = core["H"]
    assert isinstance(H, set)
    records = {row[0] for row in core["negative_records"]}
    assert tuple(-entry for entry in vector) in records

    primary = odd_primary_data(prime, modulus, K, vector, ell)
    phase = primary["phase"]
    source = primary["normalized"]
    omega = primary["omega"]
    assert isinstance(phase, int) and isinstance(source, int) and isinstance(omega, int)
    assert source == (-phase) % modulus

    generator, logs = cyclic_logs(H, modulus)
    source_height = character_height(H, modulus, ell, source)
    delta = tuple(2 * entry for entry in vector)
    target_modulus = ell ** (source_height + 1)
    source_character = cyclic_character(logs, ell, source_height, source)
    phase_character = cyclic_character(logs, ell, source_height, phase)
    antipodal_character = (2 * phase_character) % target_modulus

    assert cyclic_character(logs, ell, source_height, modulus - 1) == 0
    assert source_character == phase_character != 0
    assert antipodal_character != 0
    assert source_height == 0
    assert content(delta) % ell != 0

    actual = {
        "generator": generator,
        "H_order": len(H),
        "phase": phase,
        "source": source,
        "omega": omega,
        "source_height": source_height,
        "source_character": source_character,
        "antipodal_character": antipodal_character,
        "delta_content": content(delta),
    }
    assert actual == expected
    return H, logs, primary


def verify() -> None:
    H97, logs97, primary97 = check_record_source(
        97,
        67,
        1625,
        (-3, 0),
        11,
        {
            "generator": 2,
            "H_order": 66,
            "phase": 52,
            "source": 15,
            "omega": 24,
            "source_height": 0,
            "source_character": 10,
            "antipodal_character": 9,
            "delta_content": 6,
        },
    )
    assert character_height(H97, 67, 11, primary97["omega"]) == 0

    H2521, logs2521, primary2521 = check_record_source(
        2521,
        163,
        102731,
        (0, 1),
        3,
        {
            "generator": 2,
            "H_order": 162,
            "phase": 12,
            "source": 151,
            "omega": 104,
            "source_height": 0,
            "source_character": 1,
            "antipodal_character": 2,
            "delta_content": 2,
        },
    )

    omega = primary2521["omega"]
    omega_height = character_height(H2521, 163, 3, omega)
    assert omega_height == 3
    assert omega in power_image(H2521, 163, 3**3)
    assert omega not in power_image(H2521, 163, 3**4)
    for height in range(omega_height):
        assert cyclic_character(logs2521, 3, height, omega) == 0
    assert cyclic_character(logs2521, 3, omega_height, omega) == 54

    print("verified odd-primary character-height and antipodal-source controls")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused controls")
    args = parser.parse_args()
    if args.verify:
        verify()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
