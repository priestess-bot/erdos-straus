#!/usr/bin/env python3
"""Close the constrained minimum faces of the two residual carrier states.

The input is the frozen four-hard-core audit.  For each of its two unresolved
states, this script reconstructs the locally isolated heavy coordinate and its
factor bounds, separates the zero-capacity boundary from the block-height-compatible
one-layer surrogate, and then:

* exhausts every capped unit-overflow shell through the first hit;
* checks every shell size against a truncated generating function;
* independently recounts every target vector by meet in the middle;
* checks every inversion-pair sum against the complete shared-gap Type II form;
* exhausts three finite prime-power subfactor Type II menus;
* for each still-overloaded pattern coordinate, factors every q-divisible
  label/modulus difference in the complete frozen linear-source spectrum and
  checks every resulting legal gap by the complete Type II normal form.

The calculation is deliberately state- and face-scoped.  It does not assert
that these menus exhaust all possible Type I/II certificates for either prime.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
from itertools import combinations, product
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
REPRODUCTIONS = ROOT / "reproductions"
sys.path.insert(0, str(REPRODUCTIONS))

import type_i_f_overflow_lower_modulus_min_overflow_shared_gap as shared_gap
import type_i_global_linear_b1_failure_general_b_profile_500m as source


HARD_CORE_INPUT = (
    REPRODUCTIONS
    / "type-i-f-overflow-four-hard-core-collision-selector-results.json"
)
CARRIER_INPUT = (
    REPRODUCTIONS
    / "type-i-f-overflow-lower-modulus-omega-carrier-boundary-results.json"
)
MINIMUM_SHARED_GAP_HELPER = (
    REPRODUCTIONS / "type_i_f_overflow_lower_modulus_min_overflow_shared_gap.py"
)
TYPE_II_HELPER = (
    REPRODUCTIONS / "type_i_f_overflow_lower_modulus_shared_gap_type_ii.py"
)
SOURCE_HELPER = (
    REPRODUCTIONS / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
)
OUTPUT = (
    REPRODUCTIONS
    / "type-i-f-overflow-two-residual-constrained-minimum-face-results.json"
)

EXPECTED_HASHES = {
    HARD_CORE_INPUT: "b632b02ebc13d7d6b73fee29269eec15f3c9a1c1736d171edd0935e3aa229260",
    CARRIER_INPUT: "695b20832c683222b3021d444f5bdcb04f706ab10aeeec9801a3ad85fe85c0fb",
    MINIMUM_SHARED_GAP_HELPER: "5557ec9d3cc989a92e22d0e624f306c92d66184a854feb6ff45b4495ace10352",
    TYPE_II_HELPER: "eb9905b8fb7428d0d8ce04fdf78f31e9ef937abb26b4fdc43bf93a39f7dc8802",
    SOURCE_HELPER: "96ee0c6711a4995fe387686a4915b41f1fcefa70cd4fe808c05a4092bf05e07d",
}

EXPECTED = {
    (99_151_369, 27_337): {
        "orientation": "reverse",
        "original_R": 82_011,
        "gap": 3,
        "forbidden_q": 115_561,
        "unconstrained_omega": 9,
        "zero_capacity_omega": 12,
        "zero_capacity_minimum_vector_count": 4,
        "zero_capacity_inverse_pair_count": 2,
        "zero_capacity_menu_counts": (636, 3_479, 137),
        "zero_capacity_shared_candidate_gaps": (
            3,
            7,
            371,
            82_011,
            191_359,
            10_142_027,
        ),
        "capacity_one_omega": 12,
        "minimum_vector_count": 6,
        "inverse_pair_count": 3,
        "menu_counts": (963, 5_594, 172),
        "shared_candidate_gaps": (
            3,
            7,
            371,
            46_203,
            82_011,
            90_339,
            191_359,
            10_142_027,
            77_896_563,
        ),
        "pattern_collision_hit_gaps": {
            (0, 0, 11, 1, 0): (71,),
            (0, 1, 10, 0, 1): (71,),
            (0, 5, 0, 7, 0): (19, 55, 87, 95, 311, 435, 803),
        },
        "unique_heavy_q_block": (31, 82_011, 2_542_342),
        "capacity_curve": (
            (0, 12, 4),
            (1, 12, 6),
            (2, 12, 6),
            (3, 12, 6),
            (4, 12, 6),
            (5, 12, 8),
            (6, 10, 2),
            (7, 9, 2),
        ),
    },
    (487_572_409, 106_017): {
        "orientation": "forward",
        "original_R": 318_051,
        "gap": 3,
        "forbidden_q": 6_965_317,
        "unconstrained_omega": 8,
        "zero_capacity_omega": 15,
        "zero_capacity_minimum_vector_count": 2,
        "zero_capacity_inverse_pair_count": 1,
        "zero_capacity_menu_counts": (1_512, 11_603, 143),
        "zero_capacity_shared_candidate_gaps": (
            3,
            39,
            35_339,
            178_439,
            318_051,
            459_407,
            1_605_951,
            2_319_707,
            4_134_663,
            20_877_363,
        ),
        "capacity_one_omega": 12,
        "minimum_vector_count": 2,
        "inverse_pair_count": 1,
        "menu_counts": (864, 6_188, 103),
        "shared_candidate_gaps": (
            3,
            7,
            11,
            27,
            63,
            99,
            231,
            567,
            891,
            2_079,
            17_583,
            35_339,
            41_027,
            64_471,
            158_247,
            318_051,
            369_243,
            580_239,
            742_119,
            1_166_187,
            1_353_891,
            2_721_103,
            2_862_459,
            3_323_187,
            5_222_151,
            6_679_071,
            10_495_683,
            12_185_019,
            24_489_927,
            207_121_879,
            220_409_343,
        ),
        "pattern_collision_hit_gaps": {
            (0, 6, 1, 4, 1): (31, 43, 7_967),
        },
        "unique_heavy_q_block": (219, 318_051, 69_653_170),
        "capacity_curve": (
            (0, 15, 2),
            (1, 12, 2),
            (2, 10, 2),
            (3, 9, 2),
            (4, 8, 2),
        ),
    },
}

EXPECTED_DUAL_NORMAL_FORMS = {
    99_151_369: {
        "gap": 19,
        "type_I": (60_019, 1, 413),
        "type_II": (59, 60_019, 7),
    },
    487_572_409: {
        "gap": 31,
        "type_I": (2, 11_855, 5_141),
        "type_II": (53, 970, 2_371),
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def overflow_vector(
    exponents: tuple[int, ...], bounds: tuple[int, ...]
) -> tuple[int, ...]:
    return tuple(
        max(abs(exponent) - bound, 0)
        for exponent, bound in zip(exponents, bounds)
    )


def relation_residue(
    factors: tuple[int, ...], modulus: int, exponents: tuple[int, ...]
) -> int:
    value = 1 % modulus
    for prime, exponent in zip(factors, exponents):
        if math.gcd(prime, modulus) != 1:
            raise AssertionError("a relation coordinate is not a unit modulo t")
        value = value * pow(prime, exponent, modulus) % modulus
    return value


def valuation(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("q-adic valuation of a zero difference is not used")
    value = abs(value)
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def best_difference_height(
    all_values: set[int], current_values: set[int], prime: int
) -> int:
    return max(
        (
            valuation(other - current, prime)
            for current in current_values
            for other in all_values
            if other != current
        ),
        default=0,
    )


def reconstructed_channel_heights(
    factors_with_bounds: tuple[tuple[int, int], ...],
    original_R: int,
    states_by_R: dict[int, list[tuple[int, int]]],
    frozen_heights: list[dict[str, int]],
) -> list[dict[str, int]]:
    """Rebuild the old three-channel capacities from the complete source set."""
    current_states = states_by_R[original_R]
    current_labels = {label for pair in current_states for label in pair}
    all_labels = {
        label for states in states_by_R.values() for pair in states for label in pair
    }
    all_moduli = set(states_by_R)
    frozen_by_q = {int(row["q"]): row for row in frozen_heights}
    reconstructed: list[dict[str, int]] = []
    for q, bound in factors_with_bounds:
        block_max = max(
            max(valuation(a * original_R + 1, q), valuation(s * original_R + 1, q))
            for a, s in current_states
        )
        label_max = best_difference_height(all_labels, current_labels, q)
        modulus_max = best_difference_height(all_moduli, {original_R}, q)
        row = {
            "q": q,
            "nu": bound,
            "block_max": block_max,
            "label_difference_max": label_max,
            "modulus_difference_max": modulus_max,
            "three_channel_sum": block_max + label_max + modulus_max,
        }
        frozen = frozen_by_q.get(q)
        if frozen is None or any(
            int(frozen[field]) != value for field, value in row.items()
        ):
            raise AssertionError("a reconstructed three-channel height changed")
        reconstructed.append(row)
    return reconstructed


def complete_source_q_blocks(
    states_by_R: dict[int, list[tuple[int, int]]], q: int
) -> list[dict[str, int]]:
    blocks = {
        (label, R, label * R + 1)
        for R, states in states_by_R.items()
        for a, s in states
        for label in (a, s)
        if (label * R + 1) % q == 0
    }
    return [
        {
            "label": label,
            "R": R,
            "block": block,
            "q": q,
            "q_valuation": valuation(block, q),
            "block_divided_by_q": block // q,
        }
        for label, R, block in sorted(blocks)
    ]


def exact_constrained_shell(
    bounds: tuple[int, ...],
    cost: int,
    constrained_index: int,
    constrained_overflow_capacity: int,
):
    """Yield every exact-cost vector with a capped coordinate overflow."""
    vector = [0] * len(bounds)

    def visit(index: int, remaining: int):
        if index == len(bounds):
            if remaining == 0:
                yield tuple(vector)
            return

        bound = bounds[index]
        for exponent in range(-bound, bound + 1):
            vector[index] = exponent
            yield from visit(index + 1, remaining)

        maximum_excess = remaining
        if index == constrained_index:
            maximum_excess = min(maximum_excess, constrained_overflow_capacity)
        if maximum_excess:
            for excess in range(1, maximum_excess + 1):
                for exponent in (bound + excess, -bound - excess):
                    vector[index] = exponent
                    yield from visit(index + 1, remaining - excess)
        vector[index] = 0

    yield from visit(0, cost)


def constrained_shell_counts_from_generating_function(
    bounds: tuple[int, ...],
    maximum_cost: int,
    constrained_index: int,
    constrained_overflow_capacity: int,
) -> list[int]:
    """Coefficients of the exact constrained shell generating function."""
    coefficients = [1] + [0] * maximum_cost
    for index, bound in enumerate(bounds):
        coordinate = [2 * bound + 1] + [0] * maximum_cost
        if index != constrained_index:
            coordinate[1:] = [2] * maximum_cost
        else:
            coordinate[1 : constrained_overflow_capacity + 1] = [2] * min(
                constrained_overflow_capacity, maximum_cost
            )
        updated = [0] * (maximum_cost + 1)
        for left_cost, left_count in enumerate(coefficients):
            for right_cost in range(maximum_cost - left_cost + 1):
                updated[left_cost + right_cost] += (
                    left_count * coordinate[right_cost]
                )
        coefficients = updated
    return coefficients


def complete_constrained_minimum_face(
    factors: tuple[int, ...],
    bounds: tuple[int, ...],
    modulus: int,
    constrained_index: int,
    constrained_overflow_capacity: int,
    valid_upper_bound: int,
) -> tuple[int, list[tuple[int, ...]], dict[str, object]]:
    """Prove the first target shell and retain every vector on it."""
    generating_counts = constrained_shell_counts_from_generating_function(
        bounds,
        valid_upper_bound,
        constrained_index,
        constrained_overflow_capacity,
    )
    shell_audit: list[dict[str, int]] = []
    minimum_cost = -1
    minimum_vectors: list[tuple[int, ...]] = []

    for cost in range(valid_upper_bound + 1):
        shell_count = 0
        target_vectors: list[tuple[int, ...]] = []
        for vector in exact_constrained_shell(
            bounds, cost, constrained_index, constrained_overflow_capacity
        ):
            shell_count += 1
            if relation_residue(factors, modulus, vector) == modulus - 1:
                target_vectors.append(vector)
        if shell_count != generating_counts[cost]:
            raise AssertionError(
                "constrained shell enumeration disagreed with its generating function"
            )
        shell_audit.append(
            {
                "cost": cost,
                "enumerated_vector_count": shell_count,
                "generating_function_coefficient": generating_counts[cost],
                "target_vector_count": len(target_vectors),
            }
        )
        if target_vectors:
            minimum_cost = cost
            minimum_vectors = sorted(target_vectors)
            break

    if minimum_cost < 0:
        raise AssertionError("the frozen valid upper bound did not reach the target")
    if minimum_cost != valid_upper_bound:
        raise AssertionError("the frozen constrained upper bound was not exact")
    if len(minimum_vectors) != len(set(minimum_vectors)):
        raise AssertionError("the constrained shell enumerator produced a duplicate")
    for vector in minimum_vectors:
        pattern = overflow_vector(vector, bounds)
        if (
            pattern[constrained_index] > constrained_overflow_capacity
            or sum(pattern) != minimum_cost
        ):
            raise AssertionError("a minimum vector violates the constrained unit cost")

    return minimum_cost, minimum_vectors, {
        "method": "ascending_exact_shell_DFS",
        "generating_function": (
            "product_i((2*nu_i+1)+2*x/(1-x)), with the constrained "
            "coordinate tail truncated at its stated overflow capacity"
        ),
        "constrained_coordinate_index": constrained_index,
        "constrained_overflow_capacity": constrained_overflow_capacity,
        "valid_upper_bound": valid_upper_bound,
        "enumerated_through_cost": minimum_cost,
        "enumerated_vector_count": sum(
            int(row["enumerated_vector_count"]) for row in shell_audit
        ),
        "shell_audit": shell_audit,
    }


def side_vectors_for_mitm(
    factors: tuple[int, ...],
    bounds: tuple[int, ...],
    modulus: int,
    global_indices: tuple[int, ...],
    constrained_index: int,
    constrained_overflow_capacity: int,
    maximum_cost: int,
) -> list[tuple[int, int, tuple[int, ...]]]:
    """Enumerate a finite exponent box, independently of the shell DFS."""
    ranges = []
    for local_index, bound in enumerate(bounds):
        global_index = global_indices[local_index]
        radius = bound + maximum_cost
        if global_index == constrained_index:
            radius = bound + min(maximum_cost, constrained_overflow_capacity)
        ranges.append(range(-radius, radius + 1))

    rows: list[tuple[int, int, tuple[int, ...]]] = []
    for vector in product(*ranges):
        cost = sum(overflow_vector(tuple(vector), bounds))
        if cost > maximum_cost:
            continue
        residue = relation_residue(factors, modulus, tuple(vector))
        rows.append((cost, residue, tuple(vector)))
    return rows


def independent_mitm_audit(
    factors: tuple[int, ...],
    bounds: tuple[int, ...],
    modulus: int,
    constrained_index: int,
    constrained_overflow_capacity: int,
    maximum_cost: int,
    direct_minimum_vectors: list[tuple[int, ...]],
) -> dict[str, object]:
    """Independently count and reconstruct all target vectors by MITM."""
    split = len(factors) // 2
    left = side_vectors_for_mitm(
        factors[:split],
        bounds[:split],
        modulus,
        tuple(range(split)),
        constrained_index,
        constrained_overflow_capacity,
        maximum_cost,
    )
    right = side_vectors_for_mitm(
        factors[split:],
        bounds[split:],
        modulus,
        tuple(range(split, len(factors))),
        constrained_index,
        constrained_overflow_capacity,
        maximum_cost,
    )
    right_by_cost_residue: dict[
        tuple[int, int], list[tuple[int, ...]]
    ] = defaultdict(list)
    for cost, residue, vector in right:
        right_by_cost_residue[(cost, residue)].append(vector)

    target = modulus - 1
    target_count_by_cost: list[int] = []
    reconstructed: set[tuple[int, ...]] = set()
    for total_cost in range(maximum_cost + 1):
        target_count = 0
        for left_cost, left_residue, left_vector in left:
            if left_cost > total_cost:
                continue
            needed = target * pow(left_residue, -1, modulus) % modulus
            matches = right_by_cost_residue.get(
                (total_cost - left_cost, needed), []
            )
            target_count += len(matches)
            if total_cost == maximum_cost:
                reconstructed.update(left_vector + right_vector for right_vector in matches)
        target_count_by_cost.append(target_count)

    direct_set = set(direct_minimum_vectors)
    if any(target_count_by_cost[:maximum_cost]):
        raise AssertionError("MITM found a target below the claimed constrained minimum")
    if target_count_by_cost[maximum_cost] != len(direct_set):
        raise AssertionError("MITM target count disagreed with the direct minimum face")
    if reconstructed != direct_set:
        raise AssertionError("MITM reconstructed a different constrained minimum face")

    return {
        "method": "finite_box_meet_in_the_middle",
        "independence_note": (
            "Each half is enumerated by Cartesian exponent ranges and filtered by "
            "cost; it does not call the exact-shell DFS."
        ),
        "split_index": split,
        "left_side_vector_count": len(left),
        "right_side_vector_count": len(right),
        "target_count_by_cost": target_count_by_cost,
        "minimum_target_vector_count": target_count_by_cost[maximum_cost],
        "reconstructed_minimum_vectors_sha256": vector_set_sha256(reconstructed),
    }


def canonical_pair(left: int, right: int) -> tuple[int, int]:
    return (left, right) if left <= right else (right, left)


def prime_power_divisors(prime_powers: list[tuple[int, int]]) -> list[int]:
    divisors = [1]
    for prime, exponent in prime_powers:
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(exponent + 1)
        ]
    return sorted(divisors)


def subfactor_menus(
    factors: tuple[int, ...], vectors: list[tuple[int, ...]]
) -> dict[str, set[tuple[int, int]]]:
    """Build all three finite coprime prime-power pair menus."""
    oriented: set[tuple[int, int]] = set()
    repartition: set[tuple[int, int]] = set()
    two_coordinate: set[tuple[int, int]] = set()

    for vector in vectors:
        positive = [
            (prime, exponent)
            for prime, exponent in zip(factors, vector)
            if exponent > 0
        ]
        negative = [
            (prime, -exponent)
            for prime, exponent in zip(factors, vector)
            if exponent < 0
        ]
        for left in prime_power_divisors(positive):
            for right in prime_power_divisors(negative):
                oriented.add(canonical_pair(left, right))

        coordinate_options: list[list[tuple[int, int]]] = []
        for prime, exponent in zip(factors, vector):
            budget = abs(exponent)
            coordinate_options.append(
                [(1, 1)]
                + [(prime**power, 1) for power in range(1, budget + 1)]
                + [(1, prime**power) for power in range(1, budget + 1)]
            )
        for choices in product(*coordinate_options):
            left = math.prod(choice[0] for choice in choices)
            right = math.prod(choice[1] for choice in choices)
            repartition.add(canonical_pair(left, right))

        active = [
            (prime, abs(exponent))
            for prime, exponent in zip(factors, vector)
            if exponent
        ]
        for (left_prime, left_bound), (right_prime, right_bound) in combinations(
            active, 2
        ):
            for left_power in range(1, left_bound + 1):
                for right_power in range(1, right_bound + 1):
                    two_coordinate.add(
                        canonical_pair(
                            left_prime**left_power,
                            right_prime**right_power,
                        )
                    )

    if not oriented <= repartition or not two_coordinate <= repartition:
        raise AssertionError("a restricted pair menu left the repartition menu")
    for pairs in (oriented, repartition, two_coordinate):
        if any(math.gcd(left, right) != 1 for left, right in pairs):
            raise AssertionError("a subfactor menu lost coordinate coprimality")
    return {
        "oriented_subfactors": oriented,
        "all_coordinate_repartitions": repartition,
        "pure_two_coordinate_pairs": two_coordinate,
    }


def direct_normal_form_candidates(
    prime: int, pairs: set[tuple[int, int]]
) -> list[dict[str, int]]:
    """Exhaust h | A+B and p+h=4ABC on a finite coprime pair menu."""
    candidates: list[dict[str, int]] = []
    for left, right in sorted(pairs):
        step = 4 * left * right
        gap = (-prime) % step
        limit = min(prime - 2, left + right)
        while gap <= limit:
            if gap >= 3 and gap % 4 == 3 and (left + right) % gap == 0:
                common = (prime + gap) // step
                quotient = (left + right) // gap
                x = left * right * common
                y = prime * left * common * quotient
                z = prime * right * common * quotient
                if (
                    common < 1
                    or prime + gap != 4 * left * right * common
                    or Fraction(4, prime)
                    != Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
                ):
                    raise AssertionError("a direct Type II candidate did not verify")
                candidates.append(
                    {
                        "gap": gap,
                        "A": left,
                        "B": right,
                        "C": common,
                        "D": quotient,
                        "x": x,
                        "y": y,
                        "z": z,
                    }
                )
            gap += step
    return candidates


def pair_set_sha256(pairs: set[tuple[int, int]]) -> str:
    payload = json.dumps(
        [list(pair) for pair in sorted(pairs)], separators=(",", ":")
    ).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def vector_set_sha256(vectors) -> str:
    payload = json.dumps(
        [list(vector) for vector in sorted(vectors)], separators=(",", ":")
    ).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def same_gap_dual_normal_form_certificate(prime: int) -> dict[str, object]:
    """Verify one frozen Type I/II pair sharing the same p, h, and x."""
    expected = EXPECTED_DUAL_NORMAL_FORMS[prime]
    gap = int(expected["gap"])
    type_i = tuple(int(value) for value in expected["type_I"])
    type_ii = tuple(int(value) for value in expected["type_II"])
    if prime % 4 != 1 or gap % 4 != 3 or not 3 <= gap <= prime - 2:
        raise AssertionError("an exit gap is not admissible")
    x = (prime + gap) // 4
    if 4 * x != prime + gap or math.prod(type_i) != x or math.prod(type_ii) != x:
        raise AssertionError("the dual normal forms do not share their first denominator")

    A_i, B_i, C_i = type_i
    if math.gcd(A_i, B_i) != 1 or (B_i * prime + A_i) % gap:
        raise AssertionError("the frozen Type I normal form conditions failed")
    divisor_i = A_i * A_i * C_i
    numerator_y_i = prime * x + divisor_i
    numerator_z_i = prime * (x + prime * x * x // divisor_i)
    if x * x % divisor_i or numerator_y_i % gap or numerator_z_i % gap:
        raise AssertionError("the Type I tail denominators are not integral")
    solution_i = (
        x,
        numerator_y_i // gap,
        numerator_z_i // gap,
    )
    if Fraction(4, prime) != sum(
        (Fraction(1, denominator) for denominator in solution_i), Fraction()
    ):
        raise AssertionError("the Type I unit-fraction identity failed")

    A_ii, B_ii, C_ii = type_ii
    if (
        math.gcd(A_ii, B_ii) != 1
        or A_ii > B_ii
        or (A_ii + B_ii) % gap
    ):
        raise AssertionError("the frozen Type II normal form conditions failed")
    divisor_ii = A_ii * A_ii * C_ii
    numerator_y_ii = prime * (x + divisor_ii)
    numerator_z_ii = prime * (x + x * x // divisor_ii)
    if x * x % divisor_ii or numerator_y_ii % gap or numerator_z_ii % gap:
        raise AssertionError("the Type II tail denominators are not integral")
    solution_ii = (
        x,
        numerator_y_ii // gap,
        numerator_z_ii // gap,
    )
    if Fraction(4, prime) != sum(
        (Fraction(1, denominator) for denominator in solution_ii), Fraction()
    ):
        raise AssertionError("the Type II unit-fraction identity failed")

    return {
        "prime": prime,
        "gap": gap,
        "shared_first_denominator": x,
        "scope_note": (
            "One verified finite same-gap coincidence; it does not assert that "
            "dual normal forms exist in general."
        ),
        "type_I": {
            "A": A_i,
            "B": B_i,
            "C": C_i,
            "divisor_A2C": divisor_i,
            "conditions": {
                "gcd_A_B": math.gcd(A_i, B_i),
                "B_p_plus_A_divided_by_gap": (B_i * prime + A_i) // gap,
                "p_plus_gap_equals_4ABC": True,
            },
            "solution": list(solution_i),
        },
        "type_II": {
            "A": A_ii,
            "B": B_ii,
            "C": C_ii,
            "divisor_A2C": divisor_ii,
            "conditions": {
                "gcd_A_B": math.gcd(A_ii, B_ii),
                "A_le_B": A_ii <= B_ii,
                "A_plus_B_divided_by_gap": (A_ii + B_ii) // gap,
                "p_plus_gap_equals_4ABC": True,
            },
            "solution": list(solution_ii),
        },
    }


def inversion_pairs(
    vectors: list[tuple[int, ...]],
) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    vector_set = set(vectors)
    pairs: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    visited: set[tuple[int, ...]] = set()
    for vector in vectors:
        if vector in visited:
            continue
        inverse = tuple(-entry for entry in vector)
        if inverse not in vector_set or inverse == vector:
            raise AssertionError("the constrained minimum face is not freely inversion paired")
        canonical, other = sorted((vector, inverse))
        pairs.append((canonical, other))
        visited.update((canonical, other))
    return sorted(pairs)


def shared_gap_profiles(
    prime: int,
    factors: tuple[int, ...],
    pairs: list[tuple[tuple[int, ...], tuple[int, ...]]],
    type_ii_cache: dict[tuple[int, int], list[dict[str, int]]],
) -> list[dict[str, object]]:
    """Completely factor each pair sum and check every admissible divisor gap."""
    profiles: list[dict[str, object]] = []
    for canonical, inverse in pairs:
        numerator, denominator = shared_gap.rational_representation(
            list(factors), canonical
        )
        inverse_numerator, inverse_denominator = shared_gap.rational_representation(
            list(factors), inverse
        )
        total = numerator + denominator
        if (inverse_numerator, inverse_denominator) != (denominator, numerator):
            raise AssertionError("inversion did not swap the reduced numerator and denominator")
        factorization = shared_gap.certified_factorization(total)
        candidate_gaps = [
            divisor
            for divisor in shared_gap.divisors_from_factorization(list(factorization))
            if divisor % 4 == 3 and 3 <= divisor <= prime - 2
        ]
        hit_profiles: list[dict[str, object]] = []
        for gap in candidate_gaps:
            cache_key = (prime, gap)
            if cache_key not in type_ii_cache:
                certificates = shared_gap.type_ii_certificates(prime, gap)
                shared_gap.verify_complete_type_ii_check(prime, gap, certificates)
                type_ii_cache[cache_key] = certificates
            certificates = type_ii_cache[cache_key]
            if certificates:
                hit_profiles.append(
                    {
                        "gap": gap,
                        "type_ii_certificate_count": len(certificates),
                        "type_ii_certificates": certificates,
                    }
                )
        profiles.append(
            {
                "canonical_vector": list(canonical),
                "inverse_vector": list(inverse),
                "a": numerator,
                "b": denominator,
                "sum": total,
                "sum_factorization": [list(item) for item in factorization],
                "candidate_gap_count": len(candidate_gaps),
                "candidate_gaps": candidate_gaps,
                "type_ii_hit_gap_count": len(hit_profiles),
                "type_ii_hit_profiles": hit_profiles,
            }
        )
    return profiles


def finite_face_menu_audit(
    prime: int,
    factors: tuple[int, ...],
    minimum_vectors: list[tuple[int, ...]],
    type_ii_cache: dict[tuple[int, int], list[dict[str, int]]],
) -> dict[str, object]:
    pairs = inversion_pairs(minimum_vectors)
    shared_profiles = shared_gap_profiles(prime, factors, pairs, type_ii_cache)
    all_shared_gaps = sorted(
        {
            int(candidate_gap)
            for profile in shared_profiles
            for candidate_gap in profile["candidate_gaps"]
        }
    )
    menus = subfactor_menus(factors, minimum_vectors)
    menu_profiles: list[dict[str, object]] = []
    definitions = {
        "oriented_subfactors": (
            "choose arbitrary prime-power subfactors from the positive and "
            "negative sides of a minimum vector"
        ),
        "all_coordinate_repartitions": (
            "for each active coordinate choose one side and any power no larger "
            "than its absolute minimum-vector exponent, or omit it"
        ),
        "pure_two_coordinate_pairs": (
            "choose two active coordinates and one positive power from each "
            "within its minimum-vector exponent budget"
        ),
    }
    for name, pair_menu in menus.items():
        candidates = direct_normal_form_candidates(prime, pair_menu)
        menu_profiles.append(
            {
                "menu": name,
                "finite_definition": definitions[name],
                "coprime_pair_count": len(pair_menu),
                "pair_set_sha256": pair_set_sha256(pair_menu),
                "direct_type_ii_normal_form_candidate_count": len(candidates),
                "direct_type_ii_normal_form_candidates": candidates,
            }
        )
    return {
        "minimum_inverse_pair_count": len(pairs),
        "shared_gap_inverse_pair_profiles": shared_profiles,
        "shared_gap_candidate_count": len(all_shared_gaps),
        "shared_gap_candidate_gaps": all_shared_gaps,
        "shared_gap_type_ii_hit_gaps": sorted(
            {
                int(hit["gap"])
                for profile in shared_profiles
                for hit in profile["type_ii_hit_profiles"]
            }
        ),
        "subfactor_menu_profiles": menu_profiles,
        "direct_subfactor_type_ii_candidate_count": sum(
            int(row["direct_type_ii_normal_form_candidate_count"])
            for row in menu_profiles
        ),
    }


def legal_divisor_gaps(
    difference: int,
    prime: int,
    factor_cache: dict[int, tuple[tuple[int, int], ...]],
) -> tuple[tuple[tuple[int, int], ...], list[int]]:
    if difference not in factor_cache:
        factor_cache[difference] = shared_gap.certified_factorization(difference)
    factorization = factor_cache[difference]
    gaps = [
        divisor
        for divisor in shared_gap.divisors_from_factorization(list(factorization))
        if divisor % 4 == 3 and 3 <= divisor <= prime - 2
    ]
    return factorization, gaps


def q_divisible_difference_menu(
    prime: int,
    original_R: int,
    q: int,
    states_by_R: dict[int, list[tuple[int, int]]],
    factor_cache: dict[int, tuple[tuple[int, int], ...]],
    type_ii_cache: dict[tuple[int, int], list[dict[str, int]]],
) -> dict[str, object]:
    """Factor every q-divisible label/modulus difference and test its gaps."""
    current_states = states_by_R[original_R]
    current_labels = sorted({label for pair in current_states for label in pair})
    all_labels = sorted(
        {label for states in states_by_R.values() for pair in states for label in pair}
    )
    edges: list[dict[str, object]] = []

    for current_label in current_labels:
        for other_label in all_labels:
            if current_label == other_label:
                continue
            difference = abs(current_label - other_label)
            q_height = valuation(difference, q)
            if not q_height:
                continue
            factorization, gaps = legal_divisor_gaps(
                difference, prime, factor_cache
            )
            edges.append(
                {
                    "edge_id": f"label:q={q}:{current_label}:{other_label}",
                    "kind": "label_difference",
                    "q": q,
                    "current_label": current_label,
                    "other_label": other_label,
                    "difference": difference,
                    "q_valuation": q_height,
                    "difference_factorization": [
                        list(item) for item in factorization
                    ],
                    "candidate_gaps": gaps,
                }
            )

    for other_R in sorted(states_by_R):
        if other_R == original_R:
            continue
        difference = abs(original_R - other_R)
        q_height = valuation(difference, q)
        if not q_height:
            continue
        factorization, gaps = legal_divisor_gaps(difference, prime, factor_cache)
        edges.append(
            {
                "edge_id": f"modulus:q={q}:{original_R}:{other_R}",
                "kind": "modulus_difference",
                "q": q,
                "current_R": original_R,
                "other_R": other_R,
                "difference": difference,
                "q_valuation": q_height,
                "difference_factorization": [list(item) for item in factorization],
                "candidate_gaps": gaps,
            }
        )

    edges.sort(key=lambda row: str(row["edge_id"]))
    candidate_gaps = sorted(
        {
            int(gap)
            for edge in edges
            for gap in edge["candidate_gaps"]
        }
    )
    hit_profiles: list[dict[str, object]] = []
    for gap in candidate_gaps:
        cache_key = (prime, gap)
        if cache_key not in type_ii_cache:
            certificates = shared_gap.type_ii_certificates(prime, gap)
            shared_gap.verify_complete_type_ii_check(prime, gap, certificates)
            type_ii_cache[cache_key] = certificates
        certificates = type_ii_cache[cache_key]
        if not certificates:
            continue
        hit_profiles.append(
            {
                "gap": gap,
                "generating_edge_ids": [
                    str(edge["edge_id"])
                    for edge in edges
                    if gap in edge["candidate_gaps"]
                ],
                "type_ii_certificate_count": len(certificates),
                "type_ii_certificates": certificates,
            }
        )

    return {
        "q": q,
        "candidate_semantics": (
            "q divides the label or modulus difference. This is a necessary "
            "congruence candidate, not a constructed carrier migration edge."
        ),
        "candidate_edge_count": len(edges),
        "label_difference_edge_count": sum(
            int(edge["kind"] == "label_difference") for edge in edges
        ),
        "modulus_difference_edge_count": sum(
            int(edge["kind"] == "modulus_difference") for edge in edges
        ),
        "candidate_edges": edges,
        "candidate_gap_count": len(candidate_gaps),
        "candidate_gaps": candidate_gaps,
        "type_ii_hit_gap_count": len(hit_profiles),
        "type_ii_hit_gaps": [int(row["gap"]) for row in hit_profiles],
        "type_ii_hit_profiles": hit_profiles,
    }


def state_key(row: dict[str, object]) -> tuple[int, int]:
    return int(row["prime"]), int(row["lower_modulus"])


def full_state_key(
    row: dict[str, object],
) -> tuple[int, str, int, int, int]:
    return (
        int(row["prime"]),
        str(row["orientation"]),
        int(row["original_R"]),
        int(row["gap"]),
        int(row["lower_modulus"]),
    )


def run() -> dict[str, object]:
    for path, expected_hash in EXPECTED_HASHES.items():
        if sha256(path) != expected_hash:
            raise AssertionError(f"frozen input changed: {path.name}")

    payload = json.loads(HARD_CORE_INPUT.read_text(encoding="utf-8"))
    carrier_payload = json.loads(CARRIER_INPUT.read_text(encoding="utf-8"))
    remaining_keys = {state_key(row) for row in payload["remaining_states"]}
    if remaining_keys != set(EXPECTED):
        raise AssertionError("the frozen residual state set changed")

    records_by_key = {state_key(row): row for row in payload["records"]}
    avoidance_by_key = {
        state_key(row): row for row in payload["exact_constrained_avoidance_profiles"]
    }
    carrier_by_key = {
        full_state_key(row): row for row in carrier_payload["records"]
    }
    if set(avoidance_by_key) != set(EXPECTED):
        raise AssertionError("the frozen constrained avoidance profile set changed")

    shared_gap.prime_certificates.clear()
    type_ii_cache: dict[tuple[int, int], list[dict[str, int]]] = {}
    source_cache: dict[int, tuple[int, dict[int, list[tuple[int, int]]]]] = {}
    difference_factor_cache: dict[int, tuple[tuple[int, int], ...]] = {}
    records: list[dict[str, object]] = []

    for key in sorted(EXPECTED):
        expected = EXPECTED[key]
        source_row = records_by_key[key]
        frozen_avoidance = avoidance_by_key[key]
        prime, modulus = key
        orientation = str(source_row["orientation"])
        original_R = int(source_row["original_R"])
        gap = int(source_row["gap"])
        if (
            orientation != expected["orientation"]
            or original_R != expected["original_R"]
            or gap != expected["gap"]
            or bool(source_row["resolved_by_collision_selector"])
        ):
            raise AssertionError("a frozen residual state descriptor changed")
        if int(source_row["omega"]) != expected["unconstrained_omega"]:
            raise AssertionError("the frozen unconstrained omega changed")

        carrier_key = (prime, orientation, original_R, gap, modulus)
        if carrier_key not in carrier_by_key:
            raise AssertionError("the residual state lost its frozen carrier profile")
        carrier_row = carrier_by_key[carrier_key]

        factorization = tuple(
            (int(q), int(exponent)) for q, exponent in source_row["factorization"]
        )
        factors = tuple(q for q, _exponent in factorization)
        bounds = tuple(exponent for _q, exponent in factorization)
        K = math.prod(q**exponent for q, exponent in factorization)
        if 4 * K != prime * original_R + 1 or original_R != gap * modulus:
            raise AssertionError("the frozen factorization did not reconstruct its state")

        if prime not in source_cache:
            source_cache[prime] = source.enumerate_linear_source_states(prime)
        source_bound, states_by_R = source_cache[prime]
        if original_R not in states_by_R:
            raise AssertionError("the current state disappeared from the source spectrum")
        channel_heights = reconstructed_channel_heights(
            factorization,
            original_R,
            states_by_R,
            carrier_row["coordinate_heights"],
        )

        forbidden_q = int(expected["forbidden_q"])
        if source_row["mandatory_separators"] != [forbidden_q]:
            raise AssertionError("the isolated heavy coordinate changed")
        forbidden_index = factors.index(forbidden_q)
        complete_heavy_q_blocks = complete_source_q_blocks(states_by_R, forbidden_q)
        if (
            len(complete_heavy_q_blocks) != 1
            or (
                int(complete_heavy_q_blocks[0]["label"]),
                int(complete_heavy_q_blocks[0]["R"]),
                int(complete_heavy_q_blocks[0]["block"]),
            )
            != expected["unique_heavy_q_block"]
            or int(complete_heavy_q_blocks[0]["q_valuation"]) != 1
        ):
            raise AssertionError("the complete source spectrum lost its unique heavy-q block")
        local_pool = next(
            row
            for row in source_row["local_pool_profiles"]
            if int(row["q"]) == forbidden_q
        )
        isolation_evidence = {
            "q": forbidden_q,
            "block_height_sum": int(local_pool["block"]["height_sum"]),
            "label_difference_height_sum": int(
                local_pool["label_difference"]["height_sum"]
            ),
            "modulus_difference_height_sum": int(
                local_pool["modulus_difference"]["height_sum"]
            ),
            "reduced_endpoint_height": int(local_pool["reduced_endpoint_height"]),
        }
        if isolation_evidence != {
            "q": forbidden_q,
            "block_height_sum": 1,
            "label_difference_height_sum": 0,
            "modulus_difference_height_sum": 0,
            "reduced_endpoint_height": 0,
        }:
            raise AssertionError("the forbidden coordinate is no longer locally isolated")

        zero_capacity_upper_bound = int(
            frozen_avoidance["exact_constrained_overflow_price"]
        )
        if zero_capacity_upper_bound != expected["zero_capacity_omega"]:
            raise AssertionError("the frozen zero-capacity upper bound changed")
        (
            zero_capacity_cost,
            zero_capacity_vectors,
            zero_capacity_shell_audit,
        ) = complete_constrained_minimum_face(
            factors,
            bounds,
            modulus,
            forbidden_index,
            0,
            zero_capacity_upper_bound,
        )
        zero_capacity_mitm_audit = independent_mitm_audit(
            factors,
            bounds,
            modulus,
            forbidden_index,
            0,
            zero_capacity_cost,
            zero_capacity_vectors,
        )
        zero_capacity_menu_audit = finite_face_menu_audit(
            prime, factors, zero_capacity_vectors, type_ii_cache
        )
        if (
            len(zero_capacity_vectors)
            != expected["zero_capacity_minimum_vector_count"]
            or int(zero_capacity_menu_audit["minimum_inverse_pair_count"])
            != expected["zero_capacity_inverse_pair_count"]
            or tuple(
                int(row["coprime_pair_count"])
                for row in zero_capacity_menu_audit["subfactor_menu_profiles"]
            )
            != expected["zero_capacity_menu_counts"]
            or tuple(zero_capacity_menu_audit["shared_gap_candidate_gaps"])
            != expected["zero_capacity_shared_candidate_gaps"]
            or zero_capacity_menu_audit["shared_gap_type_ii_hit_gaps"]
            or int(
                zero_capacity_menu_audit[
                    "direct_subfactor_type_ii_candidate_count"
                ]
            )
        ):
            raise AssertionError("the exact zero-capacity boundary face changed")

        capacity_one_upper_bound = int(expected["capacity_one_omega"])
        minimum_cost, minimum_vectors, shell_audit = (
            complete_constrained_minimum_face(
                factors,
                bounds,
                modulus,
                forbidden_index,
                1,
                capacity_one_upper_bound,
            )
        )
        mitm_audit = independent_mitm_audit(
            factors,
            bounds,
            modulus,
            forbidden_index,
            1,
            minimum_cost,
            minimum_vectors,
        )

        capacity_curve: list[dict[str, object]] = []
        for capacity, expected_cost, expected_count in expected["capacity_curve"]:
            if capacity == 0:
                curve_cost = zero_capacity_cost
                curve_vectors = zero_capacity_vectors
                curve_audit = zero_capacity_shell_audit
            elif capacity == 1:
                curve_cost = minimum_cost
                curve_vectors = minimum_vectors
                curve_audit = shell_audit
            else:
                curve_cost, curve_vectors, curve_audit = (
                    complete_constrained_minimum_face(
                        factors,
                        bounds,
                        modulus,
                        forbidden_index,
                        capacity,
                        expected_cost,
                    )
                )
            if curve_cost != expected_cost or len(curve_vectors) != expected_count:
                raise AssertionError("the exact heavy-coordinate capacity curve changed")
            capacity_curve.append(
                {
                    "heavy_coordinate_overflow_capacity": capacity,
                    "omega": curve_cost,
                    "minimum_face_vector_count": len(curve_vectors),
                    "minimum_face_vectors_sha256": vector_set_sha256(curve_vectors),
                    "direct_shell_and_generating_function_audit": curve_audit,
                }
            )
        if (
            int(capacity_curve[-1]["omega"]) != int(source_row["omega"])
            or any(
                int(row["omega"]) == int(source_row["omega"])
                for row in capacity_curve[:-1]
            )
        ):
            raise AssertionError("the capacity curve did not stop at the first original omega")

        pairs = inversion_pairs(minimum_vectors)
        if (
            len(minimum_vectors) != expected["minimum_vector_count"]
            or len(pairs) != expected["inverse_pair_count"]
        ):
            raise AssertionError("a constrained minimum-face size changed")
        shared_profiles = shared_gap_profiles(
            prime, factors, pairs, type_ii_cache
        )
        all_shared_gaps = tuple(
            sorted(
                {
                    int(candidate_gap)
                    for profile in shared_profiles
                    for candidate_gap in profile["candidate_gaps"]
                }
            )
        )
        if all_shared_gaps != expected["shared_candidate_gaps"]:
            raise AssertionError("the constrained shared-gap menu changed")
        if any(profile["type_ii_hit_gap_count"] for profile in shared_profiles):
            raise AssertionError("a constrained shared-gap Type II hit appeared")

        menus = subfactor_menus(factors, minimum_vectors)
        menu_profiles: list[dict[str, object]] = []
        for name, pairs_menu in menus.items():
            candidates = direct_normal_form_candidates(prime, pairs_menu)
            menu_profiles.append(
                {
                    "menu": name,
                    "finite_definition": {
                        "oriented_subfactors": (
                            "choose arbitrary prime-power subfactors from the positive "
                            "and negative sides of a minimum vector"
                        ),
                        "all_coordinate_repartitions": (
                            "for each active coordinate choose one side and any power no "
                            "larger than its absolute minimum-vector exponent, or omit it"
                        ),
                        "pure_two_coordinate_pairs": (
                            "choose two active coordinates and one positive power from "
                            "each within its minimum-vector exponent budget"
                        ),
                    }[name],
                    "coprime_pair_count": len(pairs_menu),
                    "pair_set_sha256": pair_set_sha256(pairs_menu),
                    "direct_type_ii_normal_form_candidate_count": len(candidates),
                    "direct_type_ii_normal_form_candidates": candidates,
                }
            )
        if tuple(
            int(row["coprime_pair_count"]) for row in menu_profiles
        ) != expected["menu_counts"]:
            raise AssertionError("a constrained subfactor menu size changed")
        if any(
            row["direct_type_ii_normal_form_candidate_count"]
            for row in menu_profiles
        ):
            raise AssertionError("a constrained direct Type II candidate appeared")

        patterns = Counter(
            overflow_vector(vector, bounds) for vector in minimum_vectors
        )
        heights_by_q = {int(row["q"]): row for row in channel_heights}
        difference_menus_by_q: dict[int, dict[str, object]] = {}
        pattern_profiles: list[dict[str, object]] = []
        observed_pattern_hits: dict[tuple[int, ...], tuple[int, ...]] = {}
        for pattern, count in sorted(patterns.items()):
            overloaded_coordinates = []
            for index, (q, demand) in enumerate(zip(factors, pattern)):
                capacity = int(heights_by_q[q]["three_channel_sum"])
                if demand <= capacity:
                    continue
                overloaded_coordinates.append(
                    {
                        "coordinate_index": index,
                        "q": q,
                        "demand": demand,
                        "three_channel_sum": capacity,
                        "overload": demand - capacity,
                    }
                )
                if q not in difference_menus_by_q:
                    difference_menus_by_q[q] = q_divisible_difference_menu(
                        prime,
                        original_R,
                        q,
                        states_by_R,
                        difference_factor_cache,
                        type_ii_cache,
                    )
            if not overloaded_coordinates:
                raise AssertionError("a residual constrained pattern is not overloaded")

            pattern_candidate_gaps = sorted(
                {
                    int(candidate_gap)
                    for coordinate in overloaded_coordinates
                    for candidate_gap in difference_menus_by_q[int(coordinate["q"])][
                        "candidate_gaps"
                    ]
                }
            )
            pattern_hit_gaps = tuple(
                sorted(
                    {
                        int(hit_gap)
                        for coordinate in overloaded_coordinates
                        for hit_gap in difference_menus_by_q[int(coordinate["q"])][
                            "type_ii_hit_gaps"
                        ]
                    }
                )
            )
            if not pattern_hit_gaps:
                raise AssertionError(
                    "an overloaded constrained pattern lacks a difference-menu certificate"
                )
            observed_pattern_hits[pattern] = pattern_hit_gaps
            pattern_profiles.append(
                {
                    "overflow_vector": list(pattern),
                    "support_indices": [
                        index for index, value in enumerate(pattern) if value
                    ],
                    "support_primes": [
                        factors[index]
                        for index, value in enumerate(pattern)
                        if value
                    ],
                    "exponent_vector_count": count,
                    "overloaded_coordinates": overloaded_coordinates,
                    "difference_menu_candidate_gap_count": len(
                        pattern_candidate_gaps
                    ),
                    "difference_menu_candidate_gaps": pattern_candidate_gaps,
                    "difference_menu_type_ii_hit_gap_count": len(pattern_hit_gaps),
                    "difference_menu_type_ii_hit_gaps": list(pattern_hit_gaps),
                    "resolved_by_overloaded_q_difference_menu": True,
                }
            )
        if observed_pattern_hits != expected["pattern_collision_hit_gaps"]:
            raise AssertionError("the pattern-scoped difference-menu hit map changed")

        dual_normal_form = same_gap_dual_normal_form_certificate(prime)
        exit_gap = int(dual_normal_form["gap"])
        state_difference_hit_gaps = {
            int(hit_gap)
            for menu in difference_menus_by_q.values()
            for hit_gap in menu["type_ii_hit_gaps"]
        }
        if exit_gap not in state_difference_hit_gaps:
            raise AssertionError("the dual-normal-form exit gap left the difference menu")
        expected_type_ii = EXPECTED_DUAL_NORMAL_FORMS[prime]["type_II"]
        if not any(
            (
                int(certificate["A"]),
                int(certificate["B"]),
                int(certificate["C"]),
            )
            == expected_type_ii
            for certificate in type_ii_cache[(prime, exit_gap)]
        ):
            raise AssertionError("the complete Type II check lost the dual normal form")

        zero_capacity_patterns = Counter(
            overflow_vector(vector, bounds) for vector in zero_capacity_vectors
        )

        records.append(
            {
                "prime": prime,
                "orientation": orientation,
                "original_R": original_R,
                "gap": gap,
                "lower_modulus": modulus,
                "K": K,
                "factorization": [list(item) for item in factorization],
                "capacity_aware_constraint": {
                    "heavy_q": forbidden_q,
                    "heavy_coordinate_index": forbidden_index,
                    "heavy_coordinate_overflow_capacity": 1,
                    "condition": (
                        f"overflow_{forbidden_index}(z) <= 1, equivalently "
                        f"abs(z_{forbidden_index}) <= "
                        f"{bounds[forbidden_index] + 1}"
                    ),
                    "unit_cost": (
                        "sum_i max(abs(z_i)-nu_i,0), subject to at most one "
                        "overflow layer on the heavy coordinate"
                    ),
                    "frozen_local_isolation_evidence": isolation_evidence,
                    "complete_source_q_block_count": len(complete_heavy_q_blocks),
                    "complete_source_q_blocks": complete_heavy_q_blocks,
                },
                "unconstrained_omega": int(source_row["omega"]),
                "capacity_aware_omega": minimum_cost,
                "capacity_aware_price_increase_over_unconstrained_omega": (
                    minimum_cost - int(source_row["omega"])
                ),
                "heavy_coordinate_capacity_curve_to_first_unconstrained_omega": (
                    capacity_curve
                ),
                "zero_capacity_boundary": {
                    "heavy_coordinate_overflow_capacity": 0,
                    "condition": (
                        f"overflow_{forbidden_index}(z) = 0, equivalently "
                        f"abs(z_{forbidden_index}) <= {bounds[forbidden_index]}"
                    ),
                    "omega": zero_capacity_cost,
                    "minimum_face_vector_count": len(zero_capacity_vectors),
                    "minimum_inverse_pair_count": int(
                        zero_capacity_menu_audit["minimum_inverse_pair_count"]
                    ),
                    "minimum_overflow_pattern_count": len(zero_capacity_patterns),
                    "minimum_face_vectors": [
                        list(vector) for vector in zero_capacity_vectors
                    ],
                    "minimum_face_vectors_sha256": vector_set_sha256(
                        zero_capacity_vectors
                    ),
                    "minimum_overflow_patterns": [
                        {
                            "overflow_vector": list(pattern),
                            "exponent_vector_count": count,
                        }
                        for pattern, count in sorted(zero_capacity_patterns.items())
                    ],
                    "direct_shell_and_generating_function_audit": (
                        zero_capacity_shell_audit
                    ),
                    "independent_mitm_audit": zero_capacity_mitm_audit,
                    "finite_shared_gap_and_direct_menu_audit": (
                        zero_capacity_menu_audit
                    ),
                    "scope_note": (
                        "Exact boundary for the older no-heavy-overflow model; it "
                        "is not the block-height-compatible one-layer surrogate."
                    ),
                },
                "minimum_face_vector_count": len(minimum_vectors),
                "minimum_inverse_pair_count": len(pairs),
                "minimum_overflow_pattern_count": len(patterns),
                "minimum_face_vectors": [list(vector) for vector in minimum_vectors],
                "minimum_face_vectors_sha256": vector_set_sha256(minimum_vectors),
                "minimum_overflow_patterns": pattern_profiles,
                "direct_shell_and_generating_function_audit": shell_audit,
                "independent_mitm_audit": mitm_audit,
                "shared_gap_inverse_pair_profiles": shared_profiles,
                "shared_gap_candidate_count": len(all_shared_gaps),
                "shared_gap_candidate_gaps": list(all_shared_gaps),
                "shared_gap_type_ii_hit_gap_count": 0,
                "subfactor_menu_profiles": menu_profiles,
                "complete_linear_source_spectrum": {
                    "least_coordinate_bound": source_bound,
                    "source_modulus_count": len(states_by_R),
                    "directed_source_state_count": sum(
                        len(states) for states in states_by_R.values()
                    ),
                    "source_label_count": len(
                        {
                            label
                            for states in states_by_R.values()
                            for pair in states
                            for label in pair
                        }
                    ),
                },
                "reconstructed_three_channel_heights": channel_heights,
                "overloaded_q_difference_menus": [
                    difference_menus_by_q[q] for q in sorted(difference_menus_by_q)
                ],
                "pattern_count_resolved_by_overloaded_q_difference_menu": len(
                    pattern_profiles
                ),
                "same_gap_dual_normal_form_exit": dual_normal_form,
                "resolved_by_independent_short_certificate": True,
            }
        )

    menu_names = [
        str(row["menu"]) for row in records[0]["subfactor_menu_profiles"]
    ]
    total_menu_counts = {
        name: sum(
            int(menu["coprime_pair_count"])
            for record in records
            for menu in record["subfactor_menu_profiles"]
            if menu["menu"] == name
        )
        for name in menu_names
    }
    return {
        "arithmetic": (
            "For exactly the two residual frozen carrier states, separate the old zero-"
            "heavy-capacity boundary from the block-height-compatible unique-block "
            "capacity-one surrogate; "
            "exhaust both minimum faces, check shell counts by generating functions and "
            "the h=0/h=1 target fibers by independent MITM, exhaust shared-gap and three "
            "direct subfactor Type II menus, then factor every overloaded-q-divisible "
            "label/modulus difference and verify two same-gap Type I/II exits."
        ),
        "scope_note": (
            "Completeness is limited to the two stated faces, complete linear-source "
            "spectra for these primes, and explicitly defined finite menus. q-divisibility "
            "of a label/modulus difference is only a congruence candidate and does not "
            "construct a carrier migration edge or prove a general overflow-to-carrier "
            "injection. The two independently verified dual "
            "normal-form exits solve these instances but do not imply a general theorem."
        ),
        "inputs": [
            {"file": path.name, "sha256": sha256(path)}
            for path in EXPECTED_HASHES
        ],
        "residual_state_count": len(records),
        "zero_capacity_omega_by_prime": {
            str(record["prime"]): record["zero_capacity_boundary"]["omega"]
            for record in records
        },
        "capacity_aware_omega_by_prime": {
            str(record["prime"]): record["capacity_aware_omega"]
            for record in records
        },
        "complete_source_heavy_q_block_count": sum(
            int(record["capacity_aware_constraint"]["complete_source_q_block_count"])
            for record in records
        ),
        "minimum_face_vector_count": sum(
            int(record["minimum_face_vector_count"]) for record in records
        ),
        "minimum_inverse_pair_count": sum(
            int(record["minimum_inverse_pair_count"]) for record in records
        ),
        "shared_gap_inverse_pair_check_count": sum(
            len(record["shared_gap_inverse_pair_profiles"]) for record in records
        ),
        "distinct_state_scoped_shared_gap_check_count": sum(
            int(record["shared_gap_candidate_count"]) for record in records
        ),
        "shared_gap_type_ii_hit_gap_count": 0,
        "direct_subfactor_pair_counts": total_menu_counts,
        "direct_subfactor_type_ii_candidate_count": 0,
        "capacity_aware_pattern_count": sum(
            int(record["minimum_overflow_pattern_count"]) for record in records
        ),
        "pattern_count_resolved_by_overloaded_q_difference_menu": sum(
            int(record["pattern_count_resolved_by_overloaded_q_difference_menu"])
            for record in records
        ),
        "overloaded_q_difference_menu_count": sum(
            len(record["overloaded_q_difference_menus"]) for record in records
        ),
        "overloaded_q_difference_candidate_edge_count": sum(
            int(menu["candidate_edge_count"])
            for record in records
            for menu in record["overloaded_q_difference_menus"]
        ),
        "distinct_state_scoped_difference_candidate_gap_check_count": sum(
            len(
                {
                    int(gap)
                    for menu in record["overloaded_q_difference_menus"]
                    for gap in menu["candidate_gaps"]
                }
            )
            for record in records
        ),
        "distinct_state_scoped_difference_type_ii_hit_gap_count": sum(
            len(
                {
                    int(gap)
                    for menu in record["overloaded_q_difference_menus"]
                    for gap in menu["type_ii_hit_gaps"]
                }
            )
            for record in records
        ),
        "same_gap_dual_normal_form_exit_count": sum(
            int(record["resolved_by_independent_short_certificate"])
            for record in records
        ),
        "recursive_prime_certificate_count": len(shared_gap.prime_certificates),
        "records": records,
    }


def main() -> int:
    result = run()
    OUTPUT.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "residual_state_count",
                    "zero_capacity_omega_by_prime",
                    "capacity_aware_omega_by_prime",
                    "complete_source_heavy_q_block_count",
                    "minimum_face_vector_count",
                    "minimum_inverse_pair_count",
                    "shared_gap_inverse_pair_check_count",
                    "distinct_state_scoped_shared_gap_check_count",
                    "shared_gap_type_ii_hit_gap_count",
                    "direct_subfactor_pair_counts",
                    "direct_subfactor_type_ii_candidate_count",
                    "capacity_aware_pattern_count",
                    "pattern_count_resolved_by_overloaded_q_difference_menu",
                    "overloaded_q_difference_candidate_edge_count",
                    "distinct_state_scoped_difference_candidate_gap_check_count",
                    "distinct_state_scoped_difference_type_ii_hit_gap_count",
                    "same_gap_dual_normal_form_exit_count",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
