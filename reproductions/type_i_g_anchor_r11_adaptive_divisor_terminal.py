#!/usr/bin/env python3
"""Verify the R=11 adaptive-divisor Type I terminal family.

The verifier checks one symbolic construction and three fixed controls.  It
does not scan primes or claim coverage outside the stated divisor condition.
"""

from __future__ import annotations

import argparse
from math import gcd, isqrt


def is_prime(value: int) -> bool:
    """Use trial division only for the three fixed control primes."""
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
    """Check one positive three-unit-fraction identity exactly."""
    first, second, third = terms
    if min(terms) <= 0:
        raise AssertionError("unit-fraction denominator was nonpositive")
    if 4 * first * second * third != denominator * (
        second * third + first * third + first * second
    ):
        raise AssertionError("Egyptian-fraction identity failed")


def verify_adaptive_divisor_terminal(*, p: int, divisor: int) -> dict[str, int]:
    """Construct the terminal from one actual 8 mod 11 divisor."""
    if not is_prime(p) or p % 24 != 1:
        raise AssertionError("input is not a core prime")
    h = (p - 1) // 24
    numerator = 22 * h + 1
    if divisor <= 0 or numerator % divisor or divisor % 11 != 8:
        raise AssertionError("adaptive R=11 divisor condition failed")
    companion = numerator // divisor
    K = 3 * numerator
    factor = 3 * companion + 1
    if (divisor * companion) % 11 != 1 or factor % 11:
        raise AssertionError("mod-11 integrality gate failed")

    u = divisor * factor // 11
    v = 3 * divisor * companion * factor // 11
    terminal = (u, v, p * K)
    if not (
        K == (11 * p + 1) // 4
        and 11 * p + 1 == 4 * K
        and K % divisor == 0
        and divisor % 11 == (-K) % 11
        and 11 * u - K == divisor
        and 11 * v - K == K * K // divisor
        and (11 * u - K) * (11 * v - K) == K * K
        and u < v < p * K
    ):
        raise AssertionError("R=11 fixed-tail factorization changed")
    assert_egyptian_identity(p, terminal)
    return {
        "p": p,
        "h": h,
        "r": divisor,
        "s": companion,
        "K": K,
        "u": u,
        "v": v,
        "third_denominator": p * K,
    }


def verify_full_r11_box_terminal(*, p: int, divisor: int) -> dict[str, int]:
    """Check one of the three exact residue classes in the full R=11 box."""
    if not is_prime(p) or p % 24 != 1:
        raise AssertionError("input is not a core prime")
    h = (p - 1) // 24
    N = 22 * h + 1
    if divisor <= 0 or N * N % divisor:
        raise AssertionError("full R=11 box divisor failed")
    powers = {8: 0, 10: 1, 7: 2}
    if divisor % 11 not in powers:
        raise AssertionError("full R=11 box residue failed")
    K = 3 * N
    e = 3**powers[divisor % 11] * divisor
    if K * K % e or e % 11 != (-K) % 11:
        raise AssertionError("full R=11 box did not recover the fixed-tail divisor")
    u = (K + e) // 11
    v = (K + K * K // e) // 11
    if not (
        (K + e) % 11 == 0
        and (K + K * K // e) % 11 == 0
        and (11 * u - K) * (11 * v - K) == K * K
        and u > 0
        and v > 0
    ):
        raise AssertionError("full R=11 box factorization changed")
    assert_egyptian_identity(p, (u, v, p * K))
    return {"p": p, "h": h, "N": N, "d": divisor, "e": e, "u": u, "v": v}


def verify_dirichlet_ray(*, divisor: int) -> dict[str, int]:
    """Check the primitive progression attached to one allowed divisor."""
    if divisor <= 1 or divisor % 2 == 0 or divisor % 11 != 8 or gcd(divisor, 22) != 1:
        raise AssertionError("ray divisor must be an odd 8 mod 11 unit")
    h0 = (-pow(22, -1, divisor)) % divisor
    p0 = 24 * h0 + 1
    step = 24 * divisor
    if not (0 < h0 < divisor and (22 * h0 + 1) % divisor == 0 and gcd(p0, step) == 1):
        raise AssertionError("Dirichlet progression ceased to be primitive")
    return {"r": divisor, "h0": h0, "p0": p0, "step": step}


def verify_raw_self_loop_intersection() -> dict[str, int]:
    """Check the terminal-first subray inside the raw physical self-loop family."""
    p0, step = 601, 17784
    h0, hstep = (p0 - 1) // 24, step // 24
    numerator0, numerator_step = 22 * h0 + 1, 22 * hstep
    if not (
        p0 % 936 == 601
        and step % 936 == 0
        and (h0, hstep) == (25, 741)
        and (numerator0, numerator_step) == (551, 16302)
        and numerator0 % 19 == 0
        and numerator_step % 19 == 0
        and gcd(p0, step) == 1
    ):
        raise AssertionError("raw self-loop terminal intersection changed")
    return {
        "p0": p0,
        "step": step,
        "h0": h0,
        "hstep": hstep,
        "r": 19,
        "cofactor0": numerator0 // 19,
        "cofactor_step": numerator_step // 19,
    }


def verify_two_nonresidue_box_miss() -> dict[str, object]:
    """Exhibit the sharp failure of a one-nonresidue R=11 selector."""
    ell, other = 13, 17
    N = ell * other
    p = (12 * N - 1) // 11
    residues = {
        pow(ell, exponent_ell, 11) * pow(other, exponent_other, 11) % 11
        for exponent_ell in range(3)
        for exponent_other in range(3)
    }
    if not (
        is_prime(ell)
        and is_prime(other)
        and ell % 11 == 2
        and other % 11 == 6
        and N % 22 == 1
        and is_prime(p)
        and p % 24 == 1
        and (p - 1) // 24 == (N - 1) // 22
        and residues == {1, 2, 3, 4, 6}
        and not residues.intersection({7, 8, 10})
    ):
        raise AssertionError("two-nonresidue R=11 box-miss control changed")
    return {"ell": ell, "m": other, "N": N, "p": p, "residues": sorted(residues)}


def r11_divisor_box_residues(factors: tuple[tuple[int, int], ...]) -> set[int]:
    """Return residues of all divisors of the square of a factored integer."""
    residues = {1}
    for prime, exponent in factors:
        if not is_prime(prime) or exponent <= 0 or prime % 11 == 0:
            raise AssertionError("factorization is not a valid mod-11 unit factorization")
        residues = {
            residue * pow(prime, power, 11) % 11
            for residue in residues
            for power in range(2 * exponent + 1)
        }
    return residues


def classify_r11_fixed_tail_miss(factors: tuple[tuple[int, int], ...]) -> dict[str, object]:
    """Check the exact mod-11 factor-pattern classification of a box miss."""
    numerator = 1
    total_two = 0
    total_six = 0
    all_quadratic_residues = True
    paired_two_six_with_one_tail = True
    for prime, exponent in factors:
        numerator *= prime**exponent
        residue = prime % 11
        if residue == 2:
            total_two += exponent
        elif residue == 6:
            total_six += exponent
        if residue not in {1, 3, 4, 5, 9}:
            all_quadratic_residues = False
        if residue not in {1, 2, 6}:
            paired_two_six_with_one_tail = False

    if numerator % 11 != 1:
        raise AssertionError("R=11 numerator must be 1 modulo 11")
    residues = r11_divisor_box_residues(factors)
    box_miss = not residues.intersection({7, 8, 10})
    predicted_miss = all_quadratic_residues or (
        total_two == 1 and total_six == 1 and paired_two_six_with_one_tail
    )
    if box_miss != predicted_miss:
        raise AssertionError("R=11 fixed-tail residual classification changed")
    return {
        "N": numerator,
        "factorization": list(factors),
        "box_residues": sorted(residues),
        "box_miss": box_miss,
        "all_quadratic_residues": all_quadratic_residues,
        "two_class_multiplicity": total_two,
        "six_class_multiplicity": total_six,
        "paired_two_six_with_one_tail": paired_two_six_with_one_tail,
    }


def verify_fixed_tail_residual_classification() -> list[dict[str, object]]:
    """Exercise both residual types and two constructive escape mechanisms."""
    controls = (
        ((67, 1),),
        ((3, 1), (37, 1)),
        ((13, 1), (17, 1)),
        ((3, 1), (13, 1), (17, 1), (37, 1)),
        ((3, 1), (13, 2)),
    )
    results = [classify_r11_fixed_tail_miss(factors) for factors in controls]
    if not (
        results[0]["box_miss"]
        and results[1]["box_miss"]
        and results[2]["box_miss"]
        and not results[3]["box_miss"]
        and not results[4]["box_miss"]
        and results[2]["box_residues"] == [1, 2, 3, 4, 6]
    ):
        raise AssertionError("R=11 residual controls ceased to separate the cases")
    return results


CONTROLS = (
    (313, 41),
    (601, 19),
    (1993, 63),
)

FULL_BOX_CONTROLS = (
    (313, 7),
    (313, 41),
    (2017, 43),
)


def build_result() -> dict[str, object]:
    """Return terminal and progression receipts without a coverage scan."""
    terminals = [verify_adaptive_divisor_terminal(p=p, divisor=r) for p, r in CONTROLS]
    full_box = [verify_full_r11_box_terminal(p=p, divisor=d) for p, d in FULL_BOX_CONTROLS]
    rays = [verify_dirichlet_ray(divisor=r) for r in (19, 41, 63)]
    self_loop_intersection = verify_raw_self_loop_intersection()
    two_nonresidue_miss = verify_two_nonresidue_box_miss()
    residual_classification = verify_fixed_tail_residual_classification()
    if terminals[0]["third_denominator"] != 269493:
        raise AssertionError("p=313 control changed")
    if terminals[1]["third_denominator"] != 993453:
        raise AssertionError("p=601 control changed")
    if terminals[2]["third_denominator"] != 10923633:
        raise AssertionError("p=1993 control changed")
    return {
        "certificate_type": "r11_adaptive_8_mod_11_divisor_terminal_v1",
        "scope": (
            "Every core prime whose 22h+1 has a divisor congruent to 8 modulo 11; "
            "the terminal is direct and does not assert global coverage."
        ),
        "terminal_controls": terminals,
        "full_box_controls": full_box,
        "primitive_dirichlet_rays": rays,
        "raw_self_loop_terminal_intersection": self_loop_intersection,
        "two_nonresidue_box_miss": two_nonresidue_miss,
        "fixed_tail_residual_classification": residual_classification,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified R=11 adaptive-divisor Type I terminal controls")


if __name__ == "__main__":
    main()
