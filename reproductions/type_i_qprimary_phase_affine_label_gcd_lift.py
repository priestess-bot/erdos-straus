#!/usr/bin/env python3
"""Verify the q-primary affine phase-lift gcd and interval gate."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd


@dataclass(frozen=True)
class Fixture:
    name: str
    q: int
    exponent: int
    offset: int
    step: int
    lower: int
    upper: int
    phase: int
    expected_branch: str
    expected_labels: tuple[int, ...]


FIXTURES = (
    Fixture("gcd_lifted", 5, 2, 3, 10, 0, 40, 13, "PHASE_LIFTED", (13,)),
    Fixture("gcd_obstructed", 5, 2, 3, 10, 0, 40, 14, "PHASE_GCD_OBSTRUCTED", ()),
    Fixture("interval_empty", 7, 2, 4, 14, 0, 10, 18, "PHASE_INTERVAL_EMPTY", ()),
)


def ceil_div(numerator: int, denominator: int) -> int:
    return -((-numerator) // denominator)


def phase_lifts(fixture: Fixture) -> tuple[str, tuple[int, ...]]:
    modulus = fixture.q ** fixture.exponent
    delta = (fixture.phase - fixture.offset) % modulus
    step_gcd = gcd(fixture.step, modulus)
    if delta % step_gcd:
        return "PHASE_GCD_OBSTRUCTED", ()

    reduced_step = fixture.step // step_gcd
    reduced_modulus = modulus // step_gcd
    if reduced_modulus == 1:
        t0 = 0
    else:
        t0 = (
            (delta // step_gcd)
            * pow(reduced_step, -1, reduced_modulus)
        ) % reduced_modulus

    t_min = ceil_div(fixture.lower - fixture.offset, fixture.step)
    t_max = (fixture.upper - fixture.offset) // fixture.step
    k_min = ceil_div(t_min - t0, reduced_modulus)
    k_max = (t_max - t0) // reduced_modulus
    if k_min > k_max:
        return "PHASE_INTERVAL_EMPTY", ()
    labels = tuple(
        fixture.offset + fixture.step * (t0 + reduced_modulus * k)
        for k in range(k_min, k_max + 1)
    )
    return "PHASE_LIFTED", labels


def audit_fixture(fixture: Fixture) -> None:
    branch, labels = phase_lifts(fixture)
    if branch != fixture.expected_branch or labels != fixture.expected_labels:
        raise AssertionError(f"{fixture.name}: phase-lift result changed")


def verify_shared_slot_deficit() -> None:
    fixture = FIXTURES[0]
    branch, labels = phase_lifts(fixture)
    if branch != "PHASE_LIFTED" or labels != (13,):
        raise AssertionError("shared-slot control lost its local lift")
    requests = 2
    multiplicity = 1
    capacity = multiplicity * len(labels)
    if requests <= capacity or requests - capacity != 1:
        raise AssertionError("shared-slot Hall deficit changed")


def verify() -> None:
    for fixture in FIXTURES:
        audit_fixture(fixture)
    verify_shared_slot_deficit()
    print(f"verified {len(FIXTURES)} affine phase-lift controls and one slot deficit")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact check")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
