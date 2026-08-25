#!/usr/bin/env python3
"""Show that the q=1 runtime slice has a named local terminal scope only."""

from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
for directory in (ROOT / "scripts", ROOT / "reproductions"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import t6_q_one_full_carrier_runtime_slice_v1 as runtime_slice  # noqa: E402


def bradford_gap_eleven_control() -> dict[str, int]:
    prime, gap, x, divisor = 241_441, 11, 60_363, 1_083
    if not (
        4 * x == prime + gap
        and x * x % divisor == 0
        and divisor <= x
        and (x + divisor) % gap == 0
        and (x + x * x // divisor) % gap == 0
    ):
        raise AssertionError("gap-eleven control no longer satisfies the Type II criterion")
    y = prime * (x + divisor) // gap
    z = prime * (x + x * x // divisor) // gap
    if sum((Fraction(1, value) for value in (x, y, z)), Fraction()) != Fraction(4, prime):
        raise AssertionError("gap-eleven terminal reconstruction changed")
    return {"p": prime, "m": gap, "x": x, "d": divisor, "y": y, "z": z}


def verify() -> None:
    control = bradford_gap_eleven_control()
    local_initial = runtime_slice.initial_dispatch(control["p"])
    if local_initial["kind"] != "q_one_g":
        raise AssertionError("local q=1 schedule unexpectedly became a complete terminal oracle")
    slice_result = runtime_slice.run_q_one_runtime_slice(control["p"])
    if slice_result["final_reentry"].reason_code.value != "DEAD_END":
        raise AssertionError("q=1 local runtime control no longer reaches its declared boundary")
    print("verified gap-11 terminal lies outside the q=1 runtime slice named terminal scope")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
