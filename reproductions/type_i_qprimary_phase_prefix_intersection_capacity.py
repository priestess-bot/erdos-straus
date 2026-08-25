#!/usr/bin/env python3
"""Verify Fourier phase and q-prefix intersection capacity."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd


@dataclass(frozen=True)
class Fixture:
    name: str
    p: int
    q: int
    phase_exponent: int
    phase: int
    offset: int
    step: int
    lower: int
    upper: int
    prefix_exponent: int
    expected_branch: str
    expected_labels: tuple[int, ...]


FIXTURES = (
    Fixture(
        "layer_one",
        23,
        5,
        2,
        13,
        3,
        10,
        0,
        220,
        1,
        "PHASE_PREFIX_LIFTED",
        (13, 63, 113, 163, 213),
    ),
    Fixture(
        "layer_two",
        23,
        5,
        2,
        13,
        3,
        10,
        0,
        220,
        2,
        "PHASE_PREFIX_LIFTED",
        (13, 63, 113, 163, 213),
    ),
    Fixture(
        "layer_three",
        23,
        5,
        2,
        13,
        3,
        10,
        0,
        220,
        3,
        "PHASE_PREFIX_LIFTED",
        (213,),
    ),
    Fixture(
        "phase_prefix_conflict",
        23,
        5,
        2,
        13,
        3,
        10,
        0,
        220,
        2,
        "PHASE_PREFIX_LIFTED",
        (13, 63, 113, 163, 213),
    ),
)


def ceil_div(numerator: int, denominator: int) -> int:
    return -((-numerator) // denominator)


def prefix_residue(p: int, q: int, exponent: int) -> int:
    modulus = q**exponent
    return (-p * pow(4, -1, modulus)) % modulus


def intersection(
    fixture: Fixture,
    *,
    override_prefix: int | None = None,
) -> tuple[str, tuple[int, ...]]:
    _phase_modulus = fixture.q**fixture.phase_exponent
    prefix_modulus = fixture.q**fixture.prefix_exponent
    beta = (
        prefix_residue(fixture.p, fixture.q, fixture.prefix_exponent)
        if override_prefix is None
        else override_prefix % prefix_modulus
    )
    common_modulus = fixture.q ** min(fixture.phase_exponent, fixture.prefix_exponent)
    if fixture.phase % common_modulus != beta % common_modulus:
        return "PHASE_PREFIX_CONFLICT", ()

    exponent = max(fixture.phase_exponent, fixture.prefix_exponent)
    modulus = fixture.q**exponent
    residue = (
        fixture.phase % modulus
        if fixture.phase_exponent >= fixture.prefix_exponent
        else beta
    )
    delta = (residue - fixture.offset) % modulus
    step_gcd = gcd(fixture.step, modulus)
    if delta % step_gcd:
        return "PHASE_PREFIX_GCD_OBSTRUCTED", ()

    reduced_step = fixture.step // step_gcd
    reduced_modulus = modulus // step_gcd
    t0 = (
        0
        if reduced_modulus == 1
        else (delta // step_gcd) * pow(reduced_step, -1, reduced_modulus) % reduced_modulus
    )
    t_min = ceil_div(fixture.lower - fixture.offset, fixture.step)
    t_max = (fixture.upper - fixture.offset) // fixture.step
    k_min = ceil_div(t_min - t0, reduced_modulus)
    k_max = (t_max - t0) // reduced_modulus
    if k_min > k_max:
        return "PHASE_PREFIX_INTERVAL_EMPTY", ()
    labels = tuple(
        fixture.offset + fixture.step * (t0 + reduced_modulus * k)
        for k in range(k_min, k_max + 1)
    )
    return "PHASE_PREFIX_LIFTED", labels


def verify_controls() -> None:
    for fixture in FIXTURES[:3]:
        branch, labels = intersection(fixture)
        if (branch, labels) != (fixture.expected_branch, fixture.expected_labels):
            raise AssertionError(f"{fixture.name}: intersection changed")

    conflict = FIXTURES[3]
    branch, labels = intersection(conflict, override_prefix=3)
    if branch != "PHASE_PREFIX_CONFLICT" or labels:
        raise AssertionError("phase/prefix conflict control changed")


def verify_layer_deficit() -> None:
    fixture = FIXTURES[2]
    branch, labels = intersection(fixture)
    if branch != "PHASE_PREFIX_LIFTED" or labels != (213,):
        raise AssertionError("high-layer slot control changed")
    requests = 2
    multiplicity = 1
    capacity = multiplicity * len(labels)
    if requests - capacity != 1:
        raise AssertionError("phase/prefix layer deficit changed")


def verify() -> None:
    verify_controls()
    verify_layer_deficit()
    print("verified three phase/prefix layers and one conflict/deficit control")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact check")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
