#!/usr/bin/env python3
"""Reproduce the internal-gap pullback and single-external cycle boundary."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = (
    ROOT
    / "reproductions"
    / "type-i-f-psi-one-nearest-fiber-escape-boundary-results.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-internal-support-gap-single-external-selector-results.json"
)
EXPECTED_INPUT_SHA256 = (
    "a7babc394423104647090a6bdae4255ff8cc73d2bb06dae6a0e3e1aefce4b2d2"
)
EXPECTED_COUNTS = {
    "state_count": 55,
    "legal_internal_gap_count": 1_102,
    "divisor_residue_check_count": 119_922,
    "internal_gap_hit_count": 62,
    "internal_gap_type_i_hit_count": 49,
    "internal_gap_type_ii_hit_count": 40,
    "internal_gap_both_type_hit_count": 27,
    "internal_selector_hit_state_count": 37,
    "internal_selector_miss_state_count": 18,
    "canonical_type_i_count": 13,
    "canonical_type_ii_count": 24,
    "defect_coordinate_count": 120,
    "legal_defect_gap_count": 60,
    "defect_gap_hit_count": 9,
    "defect_gap_type_i_hit_count": 7,
    "defect_gap_type_ii_hit_count": 8,
    "defect_selector_hit_state_count": 8,
    "q7_defect_coordinate_count": 6,
    "q7_chart_hit_count": 0,
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def factorization(value: int) -> dict[int, int]:
    return {
        int(prime): int(exponent)
        for prime, exponent in sympy.factorint(value).items()
    }


def factorization_payload(value: int) -> list[dict[str, int]]:
    return [
        {"prime": prime, "exponent": exponent}
        for prime, exponent in factorization(value).items()
    ]


def divisors_of_square(value: int) -> list[int]:
    return [int(divisor) for divisor in sympy.divisors(value * value)]


def build_certificate(
    prime: int, gap: int, divisor: int, certificate_type: str
) -> dict[str, int | str]:
    x, remainder = divmod(prime + gap, 4)
    if remainder or x * x % divisor:
        raise AssertionError("invalid gap or square divisor")
    if certificate_type == "I":
        y, y_remainder = divmod(prime * x + divisor, gap)
        z_numerator = prime * (x + prime * x * x // divisor)
        z, z_remainder = divmod(z_numerator, gap)
        if y_remainder or z_remainder:
            raise AssertionError("Type I reconstruction was not integral")
    elif certificate_type == "II":
        if divisor > x:
            raise AssertionError("Type II divisor exceeded the first denominator")
        y_numerator = prime * (x + divisor)
        y, y_remainder = divmod(y_numerator, gap)
        z_numerator = prime * (x + x * x // divisor)
        z, z_remainder = divmod(z_numerator, gap)
        if y_remainder or z_remainder:
            raise AssertionError("Type II reconstruction was not integral")
    else:
        raise ValueError(f"unknown certificate type: {certificate_type}")
    if Fraction(4, prime) != Fraction(1, x) + Fraction(1, y) + Fraction(1, z):
        raise AssertionError("certificate reconstruction lost the unit-fraction identity")
    return {
        "certificate_type": certificate_type,
        "gap": gap,
        "x": x,
        "divisor": divisor,
        "y": y,
        "z": z,
    }


def scan_internal_support() -> dict[str, object]:
    input_hash = sha256(INPUT)
    if input_hash != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen Psi_0=1 input changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    records = payload["records"]
    if not isinstance(records, list) or len(records) != EXPECTED_COUNTS["state_count"]:
        raise AssertionError("the frozen Psi_0=1 state count changed")

    counts: Counter[str] = Counter()
    canonical_certificates = []
    miss_states = []
    defect_rows = []
    q7_rows = []
    defect_hit_states: set[tuple[int, int]] = set()

    for raw_row in records:
        if not isinstance(raw_row, dict):
            raise AssertionError("a frozen state is not an object")
        prime = int(raw_row["prime"])
        modulus = int(raw_row["R"])
        K = int(raw_row["K"])
        defects = {int(value) for value in raw_row["D"]}
        if 4 * K != prime * modulus + 1:
            raise AssertionError("the state identity 4K=pR+1 failed")

        canonical: dict[str, int | str] | None = None
        legal_gap_count = 0
        legal_gaps = []
        hit_gap_count = 0
        gap_profiles: dict[int, dict[str, object]] = {}
        for raw_gap in sympy.divisors(K):
            gap = int(raw_gap)
            if gap % 4 != 3 or not 3 <= gap <= prime - 2:
                continue
            legal_gap_count += 1
            legal_gaps.append(gap)
            counts["legal_internal_gap_count"] += 1
            x = (prime + gap) // 4
            first_type_i: int | None = None
            first_type_ii: int | None = None
            first_at_gap: dict[str, int | str] | None = None
            for divisor in divisors_of_square(x):
                counts["divisor_residue_check_count"] += 1
                direct_type_i = (prime * x + divisor) % gap == 0
                pullback_type_i = (4 * divisor * modulus * modulus + 1) % gap == 0
                direct_type_ii = (x + divisor) % gap == 0
                pullback_type_ii = (4 * divisor * modulus - 1) % gap == 0
                if direct_type_i != pullback_type_i:
                    raise AssertionError("Type I internal-gap pullback mismatch")
                if direct_type_ii != pullback_type_ii:
                    raise AssertionError("Type II internal-gap pullback mismatch")

                if direct_type_i:
                    if first_type_i is None:
                        first_type_i = divisor
                    if first_at_gap is None:
                        first_at_gap = build_certificate(prime, gap, divisor, "I")
                if divisor <= x and direct_type_ii:
                    if first_type_ii is None:
                        first_type_ii = divisor
                    if first_at_gap is None:
                        first_at_gap = build_certificate(prime, gap, divisor, "II")

            type_i_hit = first_type_i is not None
            type_ii_hit = first_type_ii is not None
            gap_profiles[gap] = {
                "type_i_hit": type_i_hit,
                "type_i_first_divisor": first_type_i,
                "type_ii_hit": type_ii_hit,
                "type_ii_first_divisor": first_type_ii,
            }
            if type_i_hit:
                counts["internal_gap_type_i_hit_count"] += 1
            if type_ii_hit:
                counts["internal_gap_type_ii_hit_count"] += 1
            if type_i_hit and type_ii_hit:
                counts["internal_gap_both_type_hit_count"] += 1
            if first_at_gap is not None:
                hit_gap_count += 1
                counts["internal_gap_hit_count"] += 1
                if canonical is None:
                    canonical = first_at_gap

        for defect in sorted(defects):
            counts["defect_coordinate_count"] += 1
            legal = defect % 4 == 3 and 3 <= defect <= prime - 2
            profile = gap_profiles.get(defect)
            if legal != (profile is not None):
                raise AssertionError("defect legality disagreed with the internal-gap menu")
            type_i_hit = bool(profile and profile["type_i_hit"])
            type_ii_hit = bool(profile and profile["type_ii_hit"])
            if legal:
                counts["legal_defect_gap_count"] += 1
            if type_i_hit or type_ii_hit:
                counts["defect_gap_hit_count"] += 1
                defect_hit_states.add((prime, modulus))
            if type_i_hit:
                counts["defect_gap_type_i_hit_count"] += 1
            if type_ii_hit:
                counts["defect_gap_type_ii_hit_count"] += 1
            defect_row = {
                "prime": prime,
                "R": modulus,
                "q": defect,
                "legal_gap": legal,
                "type_i_first_divisor": (
                    None if profile is None else profile["type_i_first_divisor"]
                ),
                "type_ii_first_divisor": (
                    None if profile is None else profile["type_ii_first_divisor"]
                ),
            }
            defect_rows.append(defect_row)
            if defect == 7:
                counts["q7_defect_coordinate_count"] += 1
                chart_hit = modulus % 7 in {1, 2, 4}
                if chart_hit:
                    counts["q7_chart_hit_count"] += 1
                q7_rows.append({**defect_row, "R_mod_7": modulus % 7, "chart_hit": chart_hit})

        state_key = {"prime": prime, "R": modulus}
        if canonical is None:
            miss_states.append(
                {
                    **state_key,
                    "K_factorization": factorization_payload(K),
                    "legal_internal_gap_count": legal_gap_count,
                    "legal_internal_gaps": legal_gaps,
                }
            )
        else:
            certificate_type = str(canonical["certificate_type"])
            counts[f"canonical_type_{certificate_type.lower()}_count"] += 1
            canonical_certificates.append(
                {
                    **state_key,
                    "legal_internal_gap_count": legal_gap_count,
                    "hit_internal_gap_count": hit_gap_count,
                    "gap_is_defect_coordinate": int(canonical["gap"]) in defects,
                    "certificate": canonical,
                }
            )

    counts["state_count"] = len(records)
    counts["internal_selector_hit_state_count"] = len(canonical_certificates)
    counts["internal_selector_miss_state_count"] = len(miss_states)
    counts["defect_selector_hit_state_count"] = len(defect_hit_states)
    normalized_counts = {key: int(counts[key]) for key in EXPECTED_COUNTS}
    if normalized_counts != EXPECTED_COUNTS:
        raise AssertionError(
            f"the frozen internal-gap profile changed: {normalized_counts}"
        )

    smallest_miss = min(miss_states, key=lambda row: (int(row["prime"]), int(row["R"])))
    if (smallest_miss["prime"], smallest_miss["R"]) != (37_793_809, 19):
        raise AssertionError("the smallest internal-gap miss changed")
    if smallest_miss["legal_internal_gaps"] != [7, 371, 483_883, 25_645_799]:
        raise AssertionError("the smallest miss's complete legal gap menu changed")
    return {
        "input": INPUT.name,
        "input_sha256": input_hash,
        "summary": normalized_counts,
        "canonical_certificates": canonical_certificates,
        "miss_states": miss_states,
        "smallest_miss": smallest_miss,
        "defect_coordinate_rows": defect_rows,
        "q7_defect_rows": q7_rows,
    }


def exponent_vector(numerator: int, denominator: int, primes: list[int]) -> list[int]:
    if math.gcd(numerator, denominator) != 1:
        raise AssertionError("cycle ratio is not reduced")
    result = []
    for prime in primes:
        exponent = 0
        value = numerator
        while value % prime == 0:
            value //= prime
            exponent += 1
        value = denominator
        while value % prime == 0:
            value //= prime
            exponent -= 1
        result.append(exponent)
    return result


def ratio_from_vector(primes: list[int], vector: tuple[int, ...]) -> tuple[int, int]:
    numerator = math.prod(
        prime ** max(exponent, 0) for prime, exponent in zip(primes, vector)
    )
    denominator = math.prod(
        prime ** max(-exponent, 0) for prime, exponent in zip(primes, vector)
    )
    return numerator, denominator


def formal_edge(pair: tuple[int, int], selected: int, label: int, modulus: int) -> tuple[int, int]:
    if selected not in pair or selected % label:
        raise AssertionError("invalid formal edge")
    quotient = selected // label
    return tuple(sorted((quotient, modulus - quotient)))


def p178513_boundary() -> dict[str, object]:
    prime = 178_513
    modulus = 183
    K = (prime * modulus + 1) // 4
    K_primes = [2, 5, 7, 17, 6_863]
    if (
        not sympy.isprime(prime)
        or prime % 24 != 1
        or K != 8_166_970
        or factorization(K) != {2: 1, 5: 1, 7: 1, 17: 1, 6_863: 1}
    ):
        raise AssertionError("the p=178513 state arithmetic changed")

    powers = {}
    residue = 1
    for exponent in range(60):
        powers.setdefault(residue, exponent)
        residue = 2 * residue % 61
    if residue != 1 or len(powers) != 60:
        raise AssertionError("2 ceased to be a primitive root modulo 61")
    logs = {str(value): powers[value % 61] for value in K_primes}
    expected_logs = {"2": 1, "5": 22, "7": 49, "17": 47, "6863": 59}
    if logs != expected_logs or powers[60] != 30:
        raise AssertionError("the modulo-61 logarithm certificate changed")

    center_hits = []
    shell_witnesses = []
    for vector in itertools.product(range(-2, 3), repeat=len(K_primes)):
        defect = sum(max(0, abs(exponent) - 1) for exponent in vector)
        residue = math.prod(
            pow(prime_factor, exponent, modulus)
            for prime_factor, exponent in zip(K_primes, vector)
        ) % modulus
        if residue != modulus - 1:
            continue
        if defect == 0:
            center_hits.append(vector)
        elif defect == 1:
            shell_witnesses.append(vector)
    expected_shell = [
        (-1, 1, -2, 1, 0),
        (0, -1, 2, -1, -1),
        (0, 1, -2, 1, 1),
        (1, -1, 2, -1, 0),
    ]
    if center_hits or sorted(shell_witnesses) != expected_shell:
        raise AssertionError("the p=178513 center box or one-layer shell changed")
    shell_rows = []
    for vector in sorted(shell_witnesses):
        numerator, denominator = ratio_from_vector(K_primes, vector)
        shell_rows.append(
            {
                "exponents": list(vector),
                "numerator": numerator,
                "denominator": denominator,
                "multiple_of_R": (numerator + denominator) // modulus,
            }
        )
        if (numerator + denominator) % modulus:
            raise AssertionError("a one-layer shell ratio lost the target residue")

    q13_cycle = [(14, 169), (13, 170), (1, 182)]
    q13_selected = [169, 13, 182]
    for index, pair in enumerate(q13_cycle):
        successor = formal_edge(pair, q13_selected[index], 13, modulus)
        if successor != q13_cycle[(index + 1) % len(q13_cycle)]:
            raise AssertionError("the pure external q=13 subcycle changed")

    raw_cycle = [(85, 98), (14, 169), (13, 170)]
    raw_selected = [98, 169, 170]
    raw_labels = [7, 13, 2]
    for index, pair in enumerate(raw_cycle):
        successor = formal_edge(
            pair, raw_selected[index], raw_labels[index], modulus
        )
        if successor != raw_cycle[(index + 1) % len(raw_cycle)]:
            raise AssertionError("the additional raw three-cycle changed")

    environment = [2, 5, 7, 13, 17, 6_863]
    z0 = exponent_vector(14, 169, environment)
    z1 = exponent_vector(13, 170, environment)
    z2 = exponent_vector(1, 182, environment)
    relation_columns = [
        [second - first for first, second in zip(z0, z1)],
        [second - first for first, second in zip(z0, z2)],
        [2 * value for value in z0],
    ]
    external_row = [column[3] for column in relation_columns]
    if external_row != [3, 1, -4]:
        raise AssertionError("the single-external relation row changed")

    capacity_parameter_candidates = []
    capacity_solutions = []
    for s in (-1, 0, 1):
        # The first internal coordinate gives the complete finite range for u.
        lower_u = -((4 - 4 * s) // 6)
        upper_u = (4 * s - 2) // 6
        for u in range(lower_u, upper_u + 1):
            capacity_parameter_candidates.append({"s": s, "u": u})
            internal = [
                4 * s - 6 * u - 3,
                -s,
                5 * s - 6 * u - 3,
                -s,
                0,
            ]
            if all(abs(value) <= 1 for value in internal):
                capacity_solutions.append({"s": s, "u": u, "internal": internal})
    if capacity_solutions:
        raise AssertionError("the q=13 cycle ceased to be MISS_CAPACITY")

    elimination_vector = tuple(
        first + second - third for first, second, third in zip(z0, z1, z2)
    )
    if elimination_vector != (1, -1, 2, 0, -1, 0):
        raise AssertionError("the nearest external-elimination vector changed")
    type_ii = build_certificate(prime, 7, 2, "II")
    type_i = build_certificate(prime, 7, 5, "I")
    if modulus % 7 != 1 or (4 * 2 * modulus - 1) % 7:
        raise AssertionError("the q=7 R-chart pullback changed")

    return {
        "prime": prime,
        "R": modulus,
        "K": K,
        "K_factorization": factorization_payload(K),
        "mod_61_discrete_logs_base_2": logs,
        "center_box_hit_count": 0,
        "psi_zero": 1,
        "complete_one_layer_shell": shell_rows,
        "external_q13_subcycle": {
            "nodes": [list(pair) for pair in q13_cycle],
            "selected_coordinates": q13_selected,
            "edge_label": 13,
            "edge_label_is_external": K % 13 != 0,
            "relation_external_row": external_row,
            "oriented_external_heights": [2, 1, 1],
            "normalized_heights_have_mixed_parity": True,
            "classification": "MISS_CAPACITY",
            "capacity_first_coordinate_candidates": capacity_parameter_candidates,
            "capacity_box_solutions": capacity_solutions,
            "nearest_external_elimination_vector": list(elimination_vector),
        },
        "additional_raw_cycle": {
            "nodes": [list(pair) for pair in raw_cycle],
            "selected_coordinates": raw_selected,
            "edge_labels": raw_labels,
            "edge_classes": [
                "internal_strict_defect",
                "external_strict_defect",
                "within_K_capacity",
            ],
        },
        "full_scc_contains_at_least": [
            [85, 98],
            [14, 169],
            [13, 170],
            [1, 182],
        ],
        "terminal_first_certificates_at_gap_7": [type_ii, type_i],
    }


def multi_external_boundary() -> dict[str, object]:
    prime = 73
    modulus = 11
    K = (prime * modulus + 1) // 4
    cycle = [(1, 10), (5, 6), (3, 8), (4, 7), (2, 9)]
    selected = [10, 6, 8, 4, 2]
    if K != 201 or factorization(K) != {3: 1, 67: 1}:
        raise AssertionError("the p=73 boundary state changed")
    for index, pair in enumerate(cycle):
        successor = formal_edge(pair, selected[index], 2, modulus)
        if successor != cycle[(index + 1) % len(cycle)]:
            raise AssertionError("the pure-label q=2 five-cycle changed")

    external_rows = {
        "2": [1, 1, 3, 2, 1],
        "5": [1, -1, 0, 0, 0],
        "7": [0, 0, 0, -1, 0],
    }
    counterpart = [1, 5, 3, 7, 9]
    computed_vectors = [
        exponent_vector(numerator, denominator, [2, 5, 7])
        for numerator, denominator in zip(selected, counterpart)
    ]
    computed_rows = {
        str(prime_factor): [vector[index] for vector in computed_vectors]
        for index, prime_factor in enumerate((2, 5, 7))
    }
    if computed_rows != external_rows:
        raise AssertionError("the multi-external exponent rows changed")
    parity_kernel = []
    for coefficients in itertools.product((0, 1), repeat=len(cycle)):
        if all(
            sum(value * coefficient for value, coefficient in zip(row, coefficients))
            % 2
            == 0
            for row in external_rows.values()
        ):
            parity_kernel.append(coefficients)
    if any(sum(coefficients) % 2 for coefficients in parity_kernel):
        raise AssertionError("the multi-external parity obstruction disappeared")
    if not any(value % 2 == 0 for value in external_rows["2"]):
        raise AssertionError("the label-2 row lost its mixed-parity eliminator")
    return {
        "prime": prime,
        "R": modulus,
        "K": K,
        "cycle": [list(pair) for pair in cycle],
        "edge_label": 2,
        "selected_coordinates": selected,
        "external_rows": external_rows,
        "label_row_individually_eliminable": True,
        "joint_external_odd_coset_solution": False,
        "mod_2_external_kernel_size": len(parity_kernel),
        "classification": "MISS_EXTERNAL",
        "scope_note": (
            "A common edge label eliminates only that label row; the other "
            "external coordinate primes must still be eliminated jointly."
        ),
    }


def run() -> dict[str, object]:
    return {
        "schema_version": "internal-support-gap-single-external-selector/v1",
        "scope_note": (
            "The congruence pullback and Smith parity criterion are analytic. "
            "The 55-state counts are a hash-frozen finite profile, not a proof "
            "that every Psi_0=1 state has an internal terminal. Formal cycles "
            "remain analysis evidence unless they end in a direct certificate."
        ),
        "internal_gap_identity": {
            "setup": "4K=pR+1; legal M divides K; x=(p+M)/4",
            "type_I": "M | p*x+d iff 4*d*R^2 == -1 (mod M)",
            "type_II": "M | x+d iff 4*d*R == 1 (mod M)",
        },
        "single_external_smith_parity_criterion": {
            "setup": "e_i are integers, not all zero; g=gcd(abs(e_i)); f_i=e_i/g",
            "external_odd_coset_is_solvable": "not all normalized heights f_i are odd",
            "one_row_smith_invariant": "gcd(e_i-e_0, 2*e_0) is 2g if all f_i are odd, otherwise g",
            "scope_note": (
                "Solvability excludes MISS_EXTERNAL for a unique external row, "
                "but the state may still be MISS_CAPACITY."
            ),
        },
        "psi_one_internal_support_profile": scan_internal_support(),
        "p178513_single_external_capacity_boundary": p178513_boundary(),
        "same_label_multi_external_boundary": multi_external_boundary(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    payload = run()
    if args.verify:
        stored = json.loads(args.output.read_text(encoding="utf-8"))
        if stored != payload:
            raise AssertionError("stored result does not match recomputation")
        print(json.dumps(payload["psi_one_internal_support_profile"]["summary"], indent=2))
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload["psi_one_internal_support_profile"]["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
