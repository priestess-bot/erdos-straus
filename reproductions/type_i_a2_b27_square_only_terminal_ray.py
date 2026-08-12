#!/usr/bin/env python3
"""Verify the square-only (A,B)=(2,27) Type-I terminal and descent rays."""

from __future__ import annotations

import argparse
from math import gcd, isqrt

from type_i_24c_minus_one_adaptive_divisor_terminal_family import seven_route_dispatch
from type_i_complete_divisor_layer_normal_form import direct_hits


def is_prime(value: int) -> bool:
    """Use trial division only for the two named ray controls."""
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def certificate(*, p: int, c: int) -> dict[str, int] | None:
    """Construct this family on one gap, or return None outside its selector."""
    if not (is_prime(p) and p % 24 == 1):
        raise ValueError("p must be a core prime")
    h = (p - 1) // 24
    if not 1 <= c <= h:
        raise ValueError("c is outside the natural gap range")
    m = 24 * c - 1
    s = h + c
    if s % 9 or (27 * p + 2) % m:
        return None
    C = s // 9
    x = 54 * C
    d = 4 * C
    y = (p * x + d) // m
    z = p * (x + p * x * x // d) // m
    if not (
        x == (p + m) // 4
        and x * x % d == 0
        and x % d != 0
        and (p * x + d) % m == 0
        and gcd(2 * C, m) == 1
        and 4 * x * y * z == p * (x * y + x * z + y * z)
    ):
        raise AssertionError("Type-I reconstruction failed")
    g = gcd(d, x)
    A, B, recovered_C = d // g, x // g, g // (d // g)
    if (A, B, recovered_C) != (2, 27, C):
        raise AssertionError("wrong coprime normal form")
    return {
        "p": p,
        "c": c,
        "m": m,
        "s": s,
        "C": C,
        "x": x,
        "d": d,
        "A": A,
        "B": B,
        "y": y,
        "z": z,
    }


def factor_selector(*, p: int) -> tuple[dict[str, int], ...]:
    """Recover this entire family from eligible divisors of 27p+2."""
    if not (is_prime(p) and p % 24 == 1):
        raise ValueError("p must be a core prime")
    target = 27 * p + 2
    records = []
    for trial in range(1, isqrt(target) + 1):
        if target % trial:
            continue
        for m in {trial, target // trial}:
            if not (23 <= m <= p - 2 and (p + m) % 216 == 0):
                continue
            c = (m + 1) // 24
            record = certificate(p=p, c=c)
            if record is None or record["m"] != m:
                raise AssertionError("factor selector and gap selector disagree")
            records.append(record)
    return tuple(sorted(records, key=lambda item: item["m"]))


def eight_route_dispatch(*, p: int) -> dict[str, object]:
    """Append the complete square-only (A,B)=(2,27) selector to seven routes."""
    record = seven_route_dispatch(p=p)
    if record["branch"] != "seven_route_residual":
        return {**record, "a2_b27_terminal": None, "a2_b27_descent": None}
    terminals = factor_selector(p=p)
    terminal = terminals[0] if terminals else None
    descent = normal_tail_descent(p=p, c=terminal["c"]) if terminal else None
    return {
        **record,
        "a2_b27_terminal": terminal,
        "a2_b27_descent": descent,
        "branch": "a2_b27_square_only_terminal" if terminal else "eight_route_residual",
    }


def normal_tail_descent(*, p: int, c: int) -> dict[str, int] | None:
    """Apply the exact keep-two-denominators descent gate to this certificate."""
    record = certificate(p=p, c=c)
    if record is None:
        return None
    C, m = record["C"], record["m"]
    R = (4 * 27 * 27 * C + 1) // m
    H = 2 * R - 27
    K = 27 * C * H
    if 4 * K % (R + 1):
        return None
    n = 4 * K // (R + 1)
    x, y = record["x"], record["y"]
    if not (
        4 * K == p * R + 1
        and n < p
        and 4 * x * y * K == n * (x * y + x * K + y * K)
        and 4 * x * y * (p * K) == p * (x * y + x * (p * K) + y * (p * K))
    ):
        raise AssertionError("normal-tail source or lift reconstruction failed")
    return {**record, "R": R, "H": H, "K": K, "n": n}


def fixed_gap_deflation_is_rigid(*, a: int) -> bool:
    """Test the reduced exact gate on p=2521+341928a."""
    if a < 0:
        raise ValueError("a must be nonnegative")
    return (21 * a - 47) % (1 + 81 * a) == 0


def descent_ray(*, a: int) -> dict[str, int]:
    """Construct the fixed-R=35 square-only strict-descent ray."""
    if a < 0:
        raise ValueError("a must be nonnegative")
    C = 19 + 70 * a
    p = 2521 + 9288 * a
    m = 1583 + 5832 * a
    c = (m + 1) // 24
    record = certificate(p=p, c=c)
    if record is None:
        raise AssertionError("fixed-R ray did not pass its Type-I selector")
    descent = normal_tail_descent(p=p, c=c)
    if descent is None:
        raise AssertionError("fixed-R ray did not pass the normal-tail descent gate")
    R, H, K, n = descent["R"], descent["H"], descent["K"], descent["n"]
    if not (
        record["C"] == C
        and record["m"] == m
        and R == 35
        and H == 43
        and K == 1161 * C
        and n == 129 * C
        and p - n == 70 + 258 * a
        and 4 * K == R * p + 1
    ):
        raise AssertionError("fixed-R ray parameterization failed")
    return descent


def full_square_hits(*, p: int) -> tuple[dict[str, int], ...]:
    """Exhaust all gap certificates d|x^2 for the small named control only."""
    h = (p - 1) // 24
    records = []
    for c in range(1, h + 1):
        m = 24 * c - 1
        x = 6 * (h + c)
        for trial in range(1, isqrt(x * x) + 1):
            if (x * x) % trial:
                continue
            for d in {trial, x * x // trial}:
                if (p * x + d) % m == 0:
                    records.append({"c": c, "m": m, "x": x, "d": d})
    return tuple(sorted(records, key=lambda item: (item["c"], item["d"])))


def ray_prime(a: int) -> int:
    """Return the fixed-m=1583 specialization p=2521+341928a."""
    if a < 0:
        raise ValueError("a must be nonnegative")
    return 2521 + 341928 * a


def verify() -> None:
    first = certificate(p=2521, c=66)
    later = certificate(p=ray_prime(6), c=66)
    assert first == {
        "p": 2521,
        "c": 66,
        "m": 1583,
        "s": 171,
        "C": 19,
        "x": 1026,
        "d": 76,
        "A": 2,
        "B": 27,
        "y": 1634,
        "z": 55610739,
    }
    assert later == {
        "p": 2054089,
        "c": 66,
        "m": 1583,
        "s": 85653,
        "C": 9517,
        "x": 513918,
        "d": 38068,
        "A": 2,
        "B": 27,
        "y": 666856190,
        "z": 18492056520222285,
    }
    assert is_prime(2521) and is_prime(ray_prime(6))
    assert gcd(2521, 341928) == 1
    assert certificate(p=2521, c=1) is None
    assert factor_selector(p=2521) == (first,)
    assert factor_selector(p=ray_prime(6)) == (later,)
    descent = normal_tail_descent(p=2521, c=66)
    assert descent == {
        **first,
        "R": 35,
        "H": 43,
        "K": 22059,
        "n": 2451,
    }
    assert normal_tail_descent(p=ray_prime(6), c=66) is None
    assert fixed_gap_deflation_is_rigid(a=0)
    assert not fixed_gap_deflation_is_rigid(a=1)
    assert tuple(d for d in range(1, 3829) if 3828 % d == 0 and d % 81 == 1) == (1,)
    descent_control = descent_ray(a=210)
    assert descent_control == {
        "p": 1953001,
        "c": 51096,
        "m": 1226303,
        "s": 132471,
        "C": 14719,
        "x": 794826,
        "d": 58876,
        "A": 2,
        "B": 27,
        "y": 1265834,
        "z": 33374363415759,
        "R": 35,
        "H": 43,
        "K": 17088759,
        "n": 1898751,
    }
    assert is_prime((3 * descent_control["p"] + 1) // 4)
    assert seven_route_dispatch(p=descent_control["p"])["branch"] == "seven_route_residual"
    p2521_dispatch = eight_route_dispatch(p=2521)
    p1953001_dispatch = eight_route_dispatch(p=1953001)
    p2054089_dispatch = eight_route_dispatch(p=2054089)
    assert (
        p2521_dispatch["branch"] == "a2_b27_square_only_terminal"
        and p2521_dispatch["a2_b27_terminal"] == first
        and p2521_dispatch["a2_b27_descent"] == descent
    )
    assert (
        p1953001_dispatch["branch"] == "a2_b27_square_only_terminal"
        and p1953001_dispatch["a2_b27_descent"] == descent_control
    )
    assert (
        p2054089_dispatch["branch"] == "gap11_strict_descent"
        and p2054089_dispatch["a2_b27_terminal"] is None
        and p2054089_dispatch["a2_b27_descent"] is None
    )
    assert eight_route_dispatch(p=313)["branch"] == "r11_terminal"
    assert direct_hits(p=2521) == ()
    assert seven_route_dispatch(p=2521)["branch"] == "seven_route_residual"
    assert full_square_hits(p=2521) == (
        {"c": 1, "m": 23, "x": 636, "d": 848},
        {"c": 66, "m": 1583, "x": 1026, "d": 76},
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    print("verified the square-only (A,B)=(2,27) Type-I terminal ray")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
