#!/usr/bin/env python3
"""Verify the finite exceptional gate in the H4 q0 re-entry p-primary proof.

The positive-k branch is discharged by an integer inequality in the claim.
This script factors only the 1,535 fixed diagonal constants needed for the
k=0 exception. It does not scan prime ranges, denominators, Reach graphs, or
H4 predecessors.
"""

from __future__ import annotations

import argparse

import sympy


MAX_DELTA = 1_535
PHASE_MODULUS = 912
PHASE_RESIDUE = 769
EXPECTED_PHASE_FACTOR_RECORDS = (
    (769, 31),
    (77_377, 311),
    (97_441, 349),
    (769, 385),
    (161_281, 449),
    (2_593, 459),
    (232_417, 539),
    (769, 738),
    (769, 800),
    (620_929, 881),
    (84_673, 885),
    (212_353, 950),
    (229_681, 988),
    (769, 1_154),
    (2_593, 1_297),
    (769, 1_507),
)


def diagonal_constant(d: int) -> int:
    """Return the k=0 p-primary constant after the clean H4 equality e=d."""
    return 1 - 2 * d + 4 * d * d * (1 - 2 * d)


def exceptional_phase_screen() -> dict[str, object]:
    phase_factor_records: list[tuple[int, int]] = []
    q_compatible_records: list[tuple[int, int, int]] = []

    for d in range(1, MAX_DELTA + 1):
        constant = diagonal_constant(d)
        if constant >= 0:
            raise AssertionError("the diagonal p-primary constant vanished")

        for prime in sympy.factorint(-constant):
            if prime < 73 or prime % PHASE_MODULUS != PHASE_RESIDUE:
                continue
            phase_factor_records.append((prime, d))
            q, remainder = divmod(prime + 1, 2 * d)
            if remainder == 0 and q > 1:
                q_compatible_records.append((prime, d, q))

    result = {
        "fixed_constants": MAX_DELTA,
        "phase_factor_records": tuple(phase_factor_records),
        "q_compatible_records": tuple(q_compatible_records),
    }
    expected = {
        "fixed_constants": 1_535,
        "phase_factor_records": EXPECTED_PHASE_FACTOR_RECORDS,
        "q_compatible_records": (),
    }
    if result != expected:
        raise AssertionError(f"q0 re-entry exceptional screen changed: {result}")
    return result


def positive_k_normal_form_control() -> None:
    """Check the final forced-ell inequality used by the symbolic branch."""
    for d, q0, r in ((3, 3, 1), (5, 3, 1), (11, 5, 3)):
        if not (d >= 1 and q0 >= 3 and q0 % 2 == 1 and 0 < r < 2 * d):
            raise AssertionError("invalid positive-k control")
        gamma = 2 * d - r
        forced_ell = (2 * d - r) * (q0 * r + 1) - 1
        maximum_ell = 2 * d - 1 - q0 * r
        excess = forced_ell - maximum_ell
        expected_excess = r * (q0 * (2 * d - r + 1) - 1)
        if not (
            0 < gamma < 2 * d
            and forced_ell > maximum_ell
            and excess == expected_excess > 0
        ):
            raise AssertionError("positive-k q0 re-entry inequality changed")


def verify() -> None:
    screen = exceptional_phase_screen()
    positive_k_normal_form_control()
    if screen["q_compatible_records"]:
        raise AssertionError("an exceptional q0 re-entry p-primary candidate appeared")
    print(
        "verified q0 re-entry p-primary exclusion: "
        "1,535 diagonal constants and the positive-k normal-form inequality"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
