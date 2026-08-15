#!/usr/bin/env python3
"""Verify the finite secondary p-primary screen for the H4 q-block swap.

This factors a fixed 11,495-constant supermenu.  It does not scan prime
ranges, denominators, raw Reach graphs, or H4 predecessors.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

import sympy

from type_ii_q_one_c2_19_phase_fourth_anchor_terminal_gate import (
    FINAL_RESIDUAL,
    phase_u,
    selector_a,
)


MAX_DELTA = 1_535
EXPECTED_RESIDUAL_PHASE_RECORDS = (
    (84_673, 92, 1_761, 225, 885, 885),
    (145_777, 40, 184, 1_352, 555, 37),
    (161_281, 57, 830, 706, 449, 449),
    (620_929, 85, 1_894, 358, 881, 881),
    (708_481, 62, 526, 1_010, 1_410, 94),
    (734_017, 90, 1_457, 79, 260, 10),
    (745_873, 103, 2_179, 643, 950, 38),
)


@dataclass(frozen=True)
class GateControl:
    prime: int
    d: int
    e: int
    expected_constant: int
    expected_p_primary: bool


GATE_CONTROLS = (
    GateControl(73, 1, 1, -5, False),
    # This shows why the actual phase/provenance screen is needed.
    GateControl(2_161, 23, 1, -2_161, True),
)


def secondary_constant(d: int, e: int) -> int:
    return 1 - 2 * d + 4 * d * d * (1 - 2 * e)


def audit_gate_control(control: GateControl) -> dict[str, int | bool]:
    p = control.prime
    d = control.d
    e = control.e
    q, remainder = divmod(p + 1, 2 * d)
    constant = secondary_constant(d, e)
    p_primary = (q * q - q + 1 - 2 * e) % p == 0

    if not (
        p % 24 == 1
        and remainder == 0
        and q > 1
        and e in sympy.divisors(d)
        and constant == control.expected_constant < 0
        and p_primary == (constant % p == 0) == control.expected_p_primary
    ):
        raise AssertionError("secondary p-primary gate control changed")

    return {
        "p": p,
        "d": d,
        "e": e,
        "q": q,
        "p_primary": p_primary,
    }


def finite_phase_screen() -> dict[str, object]:
    constant_pairs = 0
    phase_factor_records = 0
    residual_phase_records: list[tuple[int, int, int, int, int, int]] = []
    admissible_records: list[tuple[int, int, int, int, int, int]] = []

    for d in range(1, MAX_DELTA + 1):
        for e in sympy.divisors(d):
            constant_pairs += 1
            constant = secondary_constant(d, e)
            if constant >= 0:
                raise AssertionError("secondary p-primary constant unexpectedly vanished")

            for p in sympy.factorint(-constant):
                if p < 73 or p % 24 != 1 or p % 912 != 769:
                    continue
                phase_factor_records += 1
                u = phase_u(p)
                if u not in FINAL_RESIDUAL:
                    continue

                a = selector_a(p)
                delta = abs(1_536 - a)
                record = (p, u, a, delta, d, e)
                residual_phase_records.append(record)

                if delta == 0 or delta % d:
                    continue
                q, remainder = divmod(p + 1, 2 * d)
                if remainder or q <= 1:
                    continue
                if (q * q - q + 1 - 2 * e) % p:
                    raise AssertionError("constant-to-gate reduction changed")
                admissible_records.append(record)

    result = {
        "constant_pairs": constant_pairs,
        "phase_factor_records": phase_factor_records,
        "residual_phase_records": tuple(sorted(residual_phase_records)),
        "admissible_records": tuple(sorted(admissible_records)),
    }
    expected = {
        "constant_pairs": 11_495,
        "phase_factor_records": 48,
        "residual_phase_records": EXPECTED_RESIDUAL_PHASE_RECORDS,
        "admissible_records": (),
    }
    if result != expected:
        raise AssertionError(f"secondary p-primary finite screen changed: {result}")
    return result


def verify() -> None:
    controls = tuple(audit_gate_control(control) for control in GATE_CONTROLS)
    screen = finite_phase_screen()
    if controls != (
        {"p": 73, "d": 1, "e": 1, "q": 37, "p_primary": False},
        {"p": 2_161, "d": 23, "e": 1, "q": 47, "p_primary": True},
    ):
        raise AssertionError("secondary p-primary algebraic controls changed")
    if screen["admissible_records"]:
        raise AssertionError("actual H4 secondary p-primary candidate appeared")
    print("verified 11,495 fixed secondary p-primary constants with zero actual candidates")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the exact finite phase screen")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
