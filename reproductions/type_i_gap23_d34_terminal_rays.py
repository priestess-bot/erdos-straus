#!/usr/bin/env python3
"""Verify the gap-23, d=34 Type-I terminal rays."""

from __future__ import annotations

import argparse
from math import gcd, isqrt


def is_prime(value: int) -> bool:
    """Use trial division only for the p=1201 control."""
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor <= isqrt(value):
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def assert_egyptian_identity(denominator: int, terms: tuple[int, int, int]) -> None:
    """Check a positive three-unit-fraction identity exactly."""
    first, second, third = terms
    if min(terms) <= 0:
        raise AssertionError("unit-fraction denominator was nonpositive")
    if 4 * first * second * third != denominator * (
        second * third + first * third + first * second
    ):
        raise AssertionError("Egyptian-fraction identity failed")


def verify_d34_terminal(*, h: int) -> dict[str, int]:
    """Reconstruct the Type-I terminal for either CRT class of h."""
    p = 24 * h + 1
    s = h + 1
    x = 6 * s
    divisor = 34
    if not (
        h % 17 == 16
        and s * s % 23 == 2
        and x * x % divisor == 0
        and (p * x + divisor) % 23 == 0
    ):
        raise AssertionError("gap-23 d=34 gate failed")
    first = x
    second = (p * x + divisor) // 23
    third = p * (x + p * x * x // divisor) // 23
    assert_egyptian_identity(p, (first, second, third))
    return {"p": p, "h": h, "x": x, "d": divisor, "y": second, "z": third}


def verify_dirichlet_rays() -> tuple[dict[str, int], dict[str, int]]:
    """Check both CRT representatives and their primitive p progressions."""
    records = []
    for h0 in (50, 339):
        p0 = 24 * h0 + 1
        step = 24 * 17 * 23
        if not (
            h0 % 17 == 16
            and (h0 + 1) % 23 in {5, 18}
            and gcd(p0, step) == 1
        ):
            raise AssertionError("Dirichlet ray ceased to be primitive")
        records.append({"h0": h0, "p0": p0, "step": step})
    return tuple(records)


def build_result() -> dict[str, object]:
    """Return symbolic and p=1201 controls without a coverage scan."""
    first = verify_d34_terminal(h=50)
    second = verify_d34_terminal(h=339)
    rays = verify_dirichlet_rays()
    if not (
        is_prime(first["p"])
        and first == {"p": 1201, "h": 50, "x": 306, "d": 34, "y": 15980, "z": 172727820}
        and second["p"] == 8137
        and rays[0] == {"h0": 50, "p0": 1201, "step": 9384}
        and rays[1] == {"h0": 339, "p0": 8137, "step": 9384}
    ):
        raise AssertionError("gap-23 d=34 controls changed")
    return {
        "certificate_type": "gap23_d34_type_i_terminal_ray_v1",
        "scope": "Two explicit terminal rays; no coverage claim outside their CRT classes.",
        "p1201_control": first,
        "second_crt_control": second,
        "primitive_dirichlet_rays": rays,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified gap-23 d=34 terminal ray controls")


if __name__ == "__main__":
    main()
