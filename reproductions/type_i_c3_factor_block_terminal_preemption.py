#!/usr/bin/env python3
"""Verify symbolic terminal-first preemption of c=3 factor-block raw rays.

Each ray is already known to have actual raw provenance whenever its affine p
value is prime.  This verifier proves, without scanning prime values, that a
fixed Type II square-tail certificate and a strict smaller-instance lift exist
on every such prime point.  The core-19 raw ray is checked separately.
"""

from __future__ import annotations

import argparse
from math import gcd


RAYS = (
    ("compact_7_2", 73, 720720, 2, 1),
    ("class_3_7_2", 73, 5045040, 2, 1),
    ("class_1_7_46", 1033, 135944368560, 3, 3),
    ("class_0_79_202", 3313, 5335268223383280, 9, 3),
    ("class_4_15_2", 26737, 22604400, 6, 3),
    ("core19_7_2_intersection", 6121, 13693680, 2, 1),
)


def verify_square_tail_ray(
    *, name: str, p0: int, step: int, q: int, divisor: int
) -> dict[str, int | str]:
    """Prove a fixed Type II square-tail certificate on one affine ray."""
    if min(p0, step, q, divisor) <= 0 or (p0 - 1) % (4 * q) or step % (4 * q):
        raise AssertionError(f"{name}: ray is not in the square-tail normal form")
    T0 = (p0 - 1) // (4 * q)
    Tstep = step // (4 * q)
    m = 4 * q - 1
    if not (
        gcd(p0, step) == 1
        and p0 % 24 == 1
        and step % 24 == 0
        and q * q % divisor == 0
        and T0 % m == (-4 * divisor - 1) % m
        and Tstep % m == 0
        and q * T0 % 6 == 0
        and q * Tstep % 6 == 0
        and divisor <= q * (T0 + 1)
    ):
        raise AssertionError(f"{name}: square-tail hypotheses changed")

    # A fixed control checks the displayed p-level certificate and its lift.
    p, T = p0, T0
    x = q * (T + 1)
    y = p * (x + divisor) // m
    z = p * (x + x * x // divisor) // m
    lower_y = (x + divisor) // m
    lower_z = (x + x * x // divisor) // m
    if not (
        divisor <= x
        and x * x % divisor == 0
        and (x + divisor) % m == 0
        and (x + x * x // divisor) % m == 0
        and 4 * x * y * z == p * (y * z + x * z + x * y)
        and 4 * x * lower_y * lower_z
        == (T + 1) * (lower_y * lower_z + x * lower_z + x * lower_y)
        and T + 1 < p
    ):
        raise AssertionError(f"{name}: Type II terminal or strict lift changed")
    return {
        "name": name,
        "p0": p0,
        "step": step,
        "q": q,
        "m": m,
        "d": divisor,
        "T0": T0,
        "Tstep": Tstep,
        "strict_smaller_instance": T + 1,
        "terminal_denominators_at_s_zero": [x, y, z],
    }


def verify_core19_raw_parameter_ray() -> dict[str, int]:
    """Check that the preempted core-19 ray satisfies the established raw sieve."""
    t0, tstep = 18, 40755
    h0, hstep = 3 + 14 * t0, 14 * tstep
    p0, pstep = 73 + 336 * t0, 336 * tstep
    if not (
        (h0, hstep, p0, pstep) == (255, 570570, 6121, 13693680)
        and h0 % 19 == 8
        and hstep % 19 == 0
        and t0 % 3 == 0
        and tstep % 3 == 0
        and t0 % 5 != 4
        and tstep % 5 == 0
        and t0 % 11 != 3
        and tstep % 11 == 0
        and t0 % 13 != 9
        and tstep % 13 == 0
        and gcd(p0, pstep) == 1
        and p0 % 7 == 3
        and pstep % 7 == 0
    ):
        raise AssertionError("core-19 raw parameter ray changed")
    return {
        "t0": t0,
        "tstep": tstep,
        "h0": h0,
        "hstep": hstep,
        "p0": p0,
        "pstep": pstep,
    }


def build_result() -> dict[str, object]:
    """Return the fixed symbolic preemption certificate family."""
    core19 = verify_core19_raw_parameter_ray()
    controls = [
        verify_square_tail_ray(
            name=name,
            p0=p0,
            step=step,
            q=q,
            divisor=divisor,
        )
        for name, p0, step, q, divisor in RAYS
    ]
    if controls[-1]["p0"] != core19["p0"] or controls[-1]["step"] != core19["pstep"]:
        raise AssertionError("core-19 terminal control no longer matches the raw ray")
    return {
        "certificate_type": "c3_factor_block_terminal_preemption_v1",
        "scope": (
            "Affine raw-source rays only. Every prime point has a direct Type II "
            "terminal and strict two-tail descent; this does not classify other c=3 paths."
        ),
        "core19_raw_parameter_ray": core19,
        "preempted_rays": controls,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified c=3 factor-block affine terminal-preemption controls")


if __name__ == "__main__":
    main()
