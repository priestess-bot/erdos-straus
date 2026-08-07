#!/usr/bin/env python3
"""Verify the complete D=6303 Type-II candidate-fiber boundary at core-19 v=5."""

from __future__ import annotations

import argparse
import json
from itertools import product
from math import gcd, isqrt


P = 1_202_376_916_441
R = 5_210_299_971_231
D = 6_303
M = 4 * D
Q = 19
ZETA = 150
MU0 = 13
MU1 = 4_387_621_028_405
FIBERS = {
    1: ((89, 1), (107, 1), (151, 1), (836_161, 1)),
    3: ((19, 1), (45_667, 1), (1_385_749, 1)),
    11: ((7, 2), (347, 1), (70_715_591, 1)),
    33: ((1_202_377_748_437, 1),),
    191: ((67, 1), (157, 1), (114_305_707, 1)),
    573: ((17, 1), (19, 3), (53, 2), (3_671, 1)),
    2_101: ((13, 1), (92_494_606_681, 1)),
    6_303: ((809, 1), (1_486_447_253, 1)),
}
PRIME_FACTORS_D = (3, 11, 191)


def admissible_a_values() -> tuple[int, ...]:
    """Generate the squarefree divisor labels of the fixed D."""
    values = [1]
    for prime in PRIME_FACTORS_D:
        values += [value * prime for value in values]
    return tuple(sorted(values))


def is_squarefree(value: int) -> bool:
    """Check squarefreeness by deterministic trial division at this fixed scale."""
    if value <= 0:
        return False
    divisor = 2
    while divisor <= isqrt(value):
        if value % (divisor * divisor) == 0:
            return False
        divisor = 3 if divisor == 2 else divisor + 2
    return True


def is_prime(value: int) -> bool:
    """Use deterministic trial division for the fixed declared factors."""
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


def product_of_factors(factors: tuple[tuple[int, int], ...]) -> int:
    """Multiply a declared complete prime factorization."""
    value = 1
    for prime, exponent in factors:
        value *= prime**exponent
    return value


def divisors(factors: tuple[tuple[int, int], ...]) -> list[int]:
    """Enumerate one complete finite candidate-fiber divisor set."""
    values = []
    for exponents in product(*(range(exponent + 1) for _, exponent in factors)):
        value = 1
        for (prime, _), exponent in zip(factors, exponents):
            value *= prime**exponent
        values.append(value)
    return sorted(values)


def valuation(value: int, prime: int) -> int:
    """Return the exact positive valuation."""
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def chi(value: int) -> int:
    """Project a unit modulo M to the fixed order-19 character."""
    if gcd(value, M) != 1:
        raise AssertionError("character requested for a nonunit")
    return pow(value, 10, 191)


def phase_exponent(value: int) -> int:
    """Decode the declared zeta power in the character image."""
    table = {pow(ZETA, exponent, 191): exponent for exponent in range(19)}
    return table[chi(value)]


def verify_fiber(a: int, factors: tuple[tuple[int, int], ...]) -> dict[str, object]:
    """Verify one of the eight complete same-modulus parameter fibers."""
    N = P + 4 * D * a
    values = divisors(factors)
    if not (
        D % a == 0
        and 4 * D * a < P
        and product_of_factors(factors) == N
        and all(is_prime(prime) for prime, _ in factors)
        and N % M == P % M == 21_733
        and gcd(N, M) == 1
        and all(gcd(value, M) == 1 for value in values)
        and not [value for value in values if value % M == M - 1]
    ):
        raise AssertionError(f"D=6303 fiber A={a} changed")
    return {
        "A": a,
        "N": N,
        "factorization": [list(item) for item in factors],
        "v19": valuation(N, Q),
        "divisor_count": len(values),
        "target_hits": [],
        "phase_16": [value for value in values if phase_exponent(value) == 16],
        "phase_8": [value for value in values if phase_exponent(value) == 8],
    }


def verify_complete_catalog() -> dict[str, object]:
    """Exhaust the whole eight-fiber A divisor lattice and its 102 divisors."""
    records = [verify_fiber(a, factors) for a, factors in FIBERS.items()]
    by_A = {int(record["A"]): record for record in records}
    allowed_A = admissible_a_values()
    tagged_divisor_records = [
        (a, value) for a, factors in FIBERS.items() for value in divisors(factors)
    ]
    unlabeled_divisors = {value for _, value in tagged_divisor_records}
    expected_counts = {1: 16, 3: 8, 11: 12, 33: 2, 191: 8, 573: 48, 2101: 4, 6303: 4}
    expected_v19 = {1: 0, 3: 1, 11: 0, 33: 0, 191: 0, 573: 3, 2101: 0, 6303: 0}
    if not (
        D == 3 * 11 * 191
        and PRIME_FACTORS_D == (3, 11, 191)
        and tuple(FIBERS) == allowed_A
        and all(D % a == 0 and is_squarefree(D // a) for a in allowed_A)
        and D * D * 4 == 158_911_236 < P
        and len(tagged_divisor_records) == 102
        and len(unlabeled_divisors) == 94
        and {a: int(by_A[a]["divisor_count"]) for a in by_A} == expected_counts
        and {a: int(by_A[a]["v19"]) for a in by_A} == expected_v19
        and [a for a in by_A if int(by_A[a]["v19"]) > 0] == [3, 573]
    ):
        raise AssertionError("D=6303 finite catalog changed")

    residues_A1 = {value % 11 for value in divisors(FIBERS[1])}
    residues_A11 = {value % 11 for value in divisors(FIBERS[11])}
    if not (
        residues_A1 == {1, 7, 8, 9}
        and residues_A11 == {1, 5, 6, 7, 8, 9}
        and all(value % 3 == 1 for value in divisors(FIBERS[3]))
        and all(value % 3 == 1 for value in divisors(FIBERS[33]))
        and all(value % 3 == 1 for value in divisors(FIBERS[191]))
        and all(value % 3 == 1 for value in divisors(FIBERS[2_101]))
        and all(value % 4 == 1 for value in divisors(FIBERS[6_303]))
    ):
        raise AssertionError("short target-odd obstructions changed")

    phase_zero_A573 = [
        value for value in divisors(FIBERS[573]) if chi(value) == 1
    ]
    if not (
        ZETA != 1
        and pow(ZETA, 19, 191) == 1
        and len({pow(ZETA, exponent, 191) for exponent in range(19)}) == 19
        and phase_zero_A573 == [1, 53_371, 70_237_243]
        and all(value % 3 == 1 for value in phase_zero_A573)
    ):
        raise AssertionError("A=573 character target obstruction changed")
    return {
        "fibers": records,
        "tagged_divisor_record_count": len(tagged_divisor_records),
        "distinct_unlabeled_divisor_count": len(unlabeled_divisors),
        "target_odd_status": "no h congruent to -1 modulo 25212 in any A fiber",
        "short_obstructions": {
            "A_1_mod_11": sorted(residues_A1),
            "A_11_mod_11": sorted(residues_A11),
            "A_3_33_191_2101_mod_3": 1,
            "A_6303_mod_4": 1,
            "A_573_phase_zero_mod_3": phase_zero_A573,
        },
    }


def verify_phase_and_qheight_boundary() -> dict[str, object]:
    """Separate a two-factor character control from candidate-record claims."""
    catalog = verify_complete_catalog()
    records = {int(record["A"]): record for record in catalog["fibers"]}
    H0 = 13
    H1 = 2_809
    N0 = int(records[2_101]["N"])
    N1 = int(records[573]["N"])
    relative = MU1 * pow(MU0, -1, R) % R
    phase_16 = {a: list(record["phase_16"]) for a, record in records.items()}
    phase_8 = {a: list(record["phase_8"]) for a, record in records.items()}
    phase_16_with_qheight = [
        (a, value)
        for a, values in phase_16.items()
        for value in values
        if valuation(value, Q) > 0
    ]
    phase_8_with_qheight = [
        (a, value)
        for a, values in phase_8.items()
        for value in values
        if valuation(value, Q) > 0
    ]
    if not (
        N0 % H0 == 0
        and N1 % H1 == 0
        and gcd(N0, N1) == 1
        and gcd(H0, H1) == 1
        and all(N1 % (H1 * Q**exponent) == 0 for exponent in range(4))
        and chi(H0) == pow(MU0, 10, 191) == pow(ZETA, 16, 191)
        and chi(H1) == pow(MU1, 10, 191) == pow(ZETA, 8, 191)
        and chi(H1 * pow(H0, -1, M) % M) == pow(relative, 10, 191) == pow(ZETA, 11, 191)
        and phase_16 == {
            1: [1_437_973],
            3: [],
            11: [],
            33: [],
            191: [],
            573: [194_563],
            2101: [13],
            6303: [],
        }
        and phase_8 == {
            1: [11_237_167_679],
            3: [],
            11: [],
            33: [],
            191: [],
            573: [2_809, 3_696_697],
            2101: [],
            6303: [],
        }
        and not phase_16[3]
        and not phase_8[3]
        and phase_16_with_qheight == []
        and phase_8_with_qheight == [(573, 3_696_697)]
        and gcd(194_563, 2_809) == 53
        and gcd(194_563, 3_696_697) == 194_563
    ):
        raise AssertionError("D=6303 signed phase and q-height boundary changed")
    return {
        "separated_character_cofactors": {
            "A0": 2_101,
            "H0": H0,
            "A1": 573,
            "H1": H1,
            "gcd_N0_N1": gcd(N0, N1),
            "gcd_H0_H1": gcd(H0, H1),
        },
        "q_active_fibers": {a: int(records[a]["v19"]) for a in (3, 573)},
        "q_active_candidate_record_boundary": (
            "A=3 has q-height one but neither signed phase; both phases can occur "
            "only in the A=573 candidate record, not across distinct q-active labels."
        ),
        "cofactor_qheight_boundary": (
            "No phase-16 cofactor itself has positive q-height; the only phase-8 "
            "cofactor with positive q-height is (A,h)=(573,3696697)."
        ),
    }


def build_result() -> dict[str, object]:
    """Build the exact D=6303 catalog, not a global Type-II classification."""
    return {
        "certificate_type": "v5_d6303_complete_candidate_fiber_boundary_v1",
        "status": "analysis_evidence_only",
        "complete_catalog": verify_complete_catalog(),
        "phase_and_qheight_boundary": verify_phase_and_qheight_boundary(),
        "scope": (
            "Complete only for D=D_star=6303 and A dividing D; it does not rule out "
            "other parameter moduli, raw-to-fiber functors, or the already known direct terminal."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified v=5 D=6303 complete candidate-fiber boundary")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
