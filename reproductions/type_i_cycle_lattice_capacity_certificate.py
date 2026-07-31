#!/usr/bin/env python3
"""Build replayable cycle-lattice capacity certificates for the R=47 cycle."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path

import sympy
from sympy.ntheory.modular import crt
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-cycle-lattice-capacity-certificate-results.json"
)

MODULUS = 47
CYCLE = [2, 15, 16, 8, 4]
SELECTED = [45, 32, 16, 8, 4]
EDGE_LABELS = [3, 2, 2, 2, 2]
SUPPORT = [2, 3, 5, 13, 31, 43]

MISS_EXTERNAL = "MISS_EXTERNAL"
MISS_CAPACITY = "MISS_CAPACITY"
HIT = "HIT"


@dataclass(frozen=True)
class SmithReplay:
    """One exact, replayable Smith decomposition D = U A V."""

    source: sympy.Matrix
    diagonal: sympy.Matrix
    left: sympy.Matrix
    right: sympy.Matrix
    rank: int


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def vector_payload(vector: sympy.Matrix) -> list[int]:
    if vector.cols != 1:
        raise AssertionError("expected a column vector")
    return [int(vector[row]) for row in range(vector.rows)]


def matrix_payload(matrix: sympy.Matrix) -> dict[str, object]:
    return {
        "shape": [matrix.rows, matrix.cols],
        "rows": [
            [int(matrix[row, column]) for column in range(matrix.cols)]
            for row in range(matrix.rows)
        ],
    }


def select_rows(matrix: sympy.Matrix, indices: list[int]) -> sympy.Matrix:
    if not indices:
        return sympy.zeros(0, matrix.cols)
    return matrix.extract(indices, list(range(matrix.cols)))


def exponent_vector(numerator: int, denominator: int) -> sympy.Matrix:
    if math.gcd(numerator, denominator) != 1:
        raise AssertionError("cycle coordinates were not coprime")
    return sympy.Matrix(
        [
            valuation(numerator, prime) - valuation(denominator, prime)
            for prime in SUPPORT
        ]
    )


def cycle_matrices() -> tuple[list[sympy.Matrix], sympy.Matrix]:
    vectors = [
        exponent_vector(coordinate, MODULUS - coordinate)
        for coordinate in SELECTED
    ]
    z0 = vectors[0]
    relation_matrix = sympy.Matrix.hstack(
        *(vector - z0 for vector in vectors[1:]),
        2 * z0,
    )
    return vectors, relation_matrix


def validate_cycle(vectors: list[sympy.Matrix], relation_matrix: sympy.Matrix) -> None:
    if not (
        len(CYCLE) == len(SELECTED) == len(EDGE_LABELS) == len(vectors)
    ):
        raise AssertionError("cycle fixture lengths disagreed")
    if relation_matrix.shape != (len(SUPPORT), len(CYCLE)):
        raise AssertionError("cycle relation matrix had the wrong shape")
    observed_support = sorted(
        set().union(
            *(
                set(map(int, sympy.factorint(coordinate)))
                | set(map(int, sympy.factorint(MODULUS - coordinate)))
                for coordinate in SELECTED
            )
        )
    )
    if observed_support != SUPPORT:
        raise AssertionError("declared cycle support was incomplete")

    for index, (node, coordinate, label, vector) in enumerate(
        zip(CYCLE, SELECTED, EDGE_LABELS, vectors)
    ):
        complement = MODULUS - coordinate
        if node != min(coordinate, complement):
            raise AssertionError("selected coordinate was not in its cycle node")
        if math.gcd(coordinate, complement) != 1:
            raise AssertionError("cycle node coordinates were not coprime")
        if coordinate % (label * label):
            raise AssertionError("cycle edge lacked label-square divisibility")
        destination = min(coordinate // label, MODULUS - coordinate // label)
        if destination != CYCLE[(index + 1) % len(CYCLE)]:
            raise AssertionError("cycle edge had the wrong destination")
        residue = math.prod(
            pow(prime, int(vector[row]), MODULUS)
            if int(vector[row]) >= 0
            else pow(pow(prime, -1, MODULUS), -int(vector[row]), MODULUS)
            for row, prime in enumerate(SUPPORT)
        ) % MODULUS
        if residue != MODULUS - 1:
            raise AssertionError("cycle vector did not represent -1")

    z0 = vectors[0]
    expected = sympy.Matrix.hstack(
        *(vector - z0 for vector in vectors[1:]),
        2 * z0,
    )
    if relation_matrix != expected:
        raise AssertionError("relation matrix did not use the declared generators")


def smith_replay(matrix: sympy.Matrix) -> SmithReplay:
    domain_matrix = DomainMatrix.from_Matrix(matrix, fmt="dense").convert_to(
        sympy.ZZ
    )
    diagonal_dm, left_dm, right_dm = smith_normal_decomp(domain_matrix)
    diagonal = diagonal_dm.to_Matrix()
    left = left_dm.to_Matrix()
    right = right_dm.to_Matrix()

    for index in range(min(diagonal.shape)):
        if int(diagonal[index, index]) < 0:
            diagonal.row_op(index, lambda value, _column: -value)
            left.row_op(index, lambda value, _column: -value)

    if left.shape != (matrix.rows, matrix.rows):
        raise AssertionError("Smith left transform had the wrong shape")
    if right.shape != (matrix.cols, matrix.cols):
        raise AssertionError("Smith right transform had the wrong shape")
    if diagonal != left * matrix * right:
        raise AssertionError("Smith identity D = U A V failed")
    if abs(int(left.det())) != 1 or abs(int(right.det())) != 1:
        raise AssertionError("Smith transforms were not unimodular")

    rank = 0
    zero_seen = False
    previous = 0
    for index in range(min(diagonal.shape)):
        entry = int(diagonal[index, index])
        if entry == 0:
            zero_seen = True
            continue
        if zero_seen:
            raise AssertionError("Smith diagonal had a nonzero entry after a zero")
        if previous and entry % previous:
            raise AssertionError("Smith invariant factors did not form a divisibility chain")
        previous = entry
        rank += 1

    for row in range(diagonal.rows):
        for column in range(diagonal.cols):
            if row != column and diagonal[row, column] != 0:
                raise AssertionError("Smith output was not diagonal")
    for row in range(rank, diagonal.rows):
        if any(diagonal[row, column] != 0 for column in range(diagonal.cols)):
            raise AssertionError("Smith zero row was not zero")
    for column in range(rank, diagonal.cols):
        if any(diagonal[row, column] != 0 for row in range(diagonal.rows)):
            raise AssertionError("Smith zero column was not zero")

    return SmithReplay(matrix, diagonal, left, right, rank)


def smith_payload(replay: SmithReplay) -> dict[str, object]:
    return {
        "identity": "D = U A V",
        "A": matrix_payload(replay.source),
        "D": matrix_payload(replay.diagonal),
        "U": matrix_payload(replay.left),
        "V": matrix_payload(replay.right),
        "rank": replay.rank,
        "U_unimodular": True,
        "V_unimodular": True,
        "D_zero_rows": list(range(replay.rank, replay.diagonal.rows)),
        "D_zero_columns": list(range(replay.rank, replay.diagonal.cols)),
    }


def solve_external(
    matrix: sympy.Matrix, rhs: sympy.Matrix
) -> tuple[dict[str, object], sympy.Matrix | None, sympy.Matrix | None]:
    replay = smith_replay(matrix)
    transformed_rhs = replay.left * rhs
    failures: list[dict[str, object]] = []
    for row in range(replay.rank):
        divisor = int(replay.diagonal[row, row])
        value = int(transformed_rhs[row])
        if value % divisor:
            failures.append(
                {
                    "kind": "diagonal_divisibility",
                    "row": row,
                    "transformed_rhs": value,
                    "required_divisor": divisor,
                }
            )
    for row in range(replay.rank, matrix.rows):
        value = int(transformed_rhs[row])
        if value:
            failures.append(
                {
                    "kind": "zero_row",
                    "row": row,
                    "transformed_rhs": value,
                    "required_value": 0,
                }
            )

    payload: dict[str, object] = {
        "equation": "A_external * t = -z0_external",
        "rhs": vector_payload(rhs),
        "smith": smith_payload(replay),
        "transformed_rhs_Ub": vector_payload(transformed_rhs),
        "solvability_failures": failures,
        "solution_exists": not failures,
    }
    if failures:
        return payload, None, None

    smith_coordinates = sympy.zeros(matrix.cols, 1)
    for row in range(replay.rank):
        smith_coordinates[row] = (
            transformed_rhs[row] / replay.diagonal[row, row]
        )
    t0 = replay.right * smith_coordinates
    kernel = replay.right[:, replay.rank :]
    if matrix * t0 != rhs:
        raise AssertionError("external particular solution failed")
    if matrix * kernel != sympy.zeros(matrix.rows, kernel.cols):
        raise AssertionError("external kernel basis failed")
    if abs(int(replay.right.det())) != 1:
        raise AssertionError("kernel ambient completion was not unimodular")

    payload.update(
        {
            "smith_particular_coordinates": vector_payload(smith_coordinates),
            "particular_solution_t0": vector_payload(t0),
            "saturated_kernel_N": matrix_payload(kernel),
            "kernel_is_saturated": True,
            "saturation_witness": (
                "N consists of columns V[:, rank:] in the unimodular ambient "
                "basis V."
            ),
        }
    )
    return payload, t0, kernel


def quotient_signature(replay: SmithReplay, vector: sympy.Matrix) -> tuple[int, ...]:
    transformed = replay.left * vector
    return tuple(
        int(transformed[row]) % int(replay.diagonal[row, row])
        if row < replay.rank
        else int(transformed[row])
        for row in range(vector.rows)
    )


def signature_components(replay: SmithReplay) -> list[dict[str, object]]:
    return [
        {"kind": "residue", "modulus": int(replay.diagonal[row, row])}
        if row < replay.rank
        else {"kind": "exact_integer"}
        for row in range(replay.source.rows)
    ]


def solve_from_replay(replay: SmithReplay, rhs: sympy.Matrix) -> sympy.Matrix:
    transformed_rhs = replay.left * rhs
    smith_coordinates = sympy.zeros(replay.source.cols, 1)
    for row in range(replay.rank):
        divisor = int(replay.diagonal[row, row])
        value = int(transformed_rhs[row])
        if value % divisor:
            raise AssertionError("internal target failed a Smith divisibility condition")
        smith_coordinates[row] = value // divisor
    if any(
        transformed_rhs[row] != 0
        for row in range(replay.rank, replay.source.rows)
    ):
        raise AssertionError("internal target failed a Smith zero-row condition")
    solution = replay.right * smith_coordinates
    if replay.source * solution != rhs:
        raise AssertionError("recovered internal solution failed")
    return solution


def ratio_from_vector(vector: sympy.Matrix) -> tuple[int, int]:
    numerator = 1
    denominator = 1
    for row, prime in enumerate(SUPPORT):
        exponent = int(vector[row])
        if exponent > 0:
            numerator *= prime**exponent
        elif exponent < 0:
            denominator *= prime ** (-exponent)
    if math.gcd(numerator, denominator) != 1:
        raise AssertionError("exponent vector did not yield a reduced ratio")
    if numerator * pow(denominator, -1, MODULUS) % MODULUS != MODULUS - 1:
        raise AssertionError("recovered ratio did not represent -1")
    return numerator, denominator


def recover_hit(
    box_vector: tuple[int, ...],
    internal_indices: list[int],
    internal_base: sympy.Matrix,
    internal_replay: SmithReplay,
    t0: sympy.Matrix,
    kernel: sympy.Matrix,
    vectors: list[sympy.Matrix],
    relation_matrix: sympy.Matrix,
    capacities: dict[int, int],
    prime: int | None,
    k_value: int | None,
) -> dict[str, object]:
    target = sympy.Matrix(box_vector)
    internal_parameter = solve_from_replay(
        internal_replay,
        target - internal_base,
    )
    relation_parameter = t0 + kernel * internal_parameter
    full_vector = vectors[0] + relation_matrix * relation_parameter
    if select_rows(full_vector, internal_indices) != target:
        raise AssertionError("hit did not recover its internal box vector")
    external_indices = [
        index for index in range(len(SUPPORT)) if index not in internal_indices
    ]
    if any(select_rows(full_vector, external_indices)):
        raise AssertionError("hit retained an external exponent")
    if any(
        abs(int(full_vector[index])) > capacities.get(SUPPORT[index], 0)
        for index in range(len(SUPPORT))
    ):
        raise AssertionError("hit left the capacity box")

    differences = [int(value) for value in relation_parameter[:-1, :]]
    parity_parameter = int(relation_parameter[-1])
    node_coefficients = [
        1 - sum(differences) + 2 * parity_parameter,
        *differences,
    ]
    if sum(node_coefficients) != 1 + 2 * parity_parameter:
        raise AssertionError("node coefficient parity reconstruction failed")
    if sum(node_coefficients) % 2 != 1:
        raise AssertionError("recovered node coefficients were not odd-sum")
    reconstructed = sum(
        (coefficient * vector for coefficient, vector in zip(node_coefficients, vectors)),
        sympy.zeros(len(SUPPORT), 1),
    )
    if reconstructed != full_vector:
        raise AssertionError("node coefficients did not reconstruct the hit")

    oriented_numerator, oriented_denominator = ratio_from_vector(full_vector)
    normalization_sign = 1 if oriented_numerator < oriented_denominator else -1
    if oriented_numerator == oriented_denominator:
        raise AssertionError("a nontrivial -1 ratio had equal tails")
    normalized_vector = normalization_sign * full_vector
    normalized_coefficients = [
        normalization_sign * coefficient for coefficient in node_coefficients
    ]
    numerator, denominator = ratio_from_vector(normalized_vector)
    if not numerator < denominator:
        raise AssertionError("ratio normalization did not put the smaller tail first")

    hit: dict[str, object] = {
        "box_vector": list(box_vector),
        "internal_solution_u": vector_payload(internal_parameter),
        "relation_parameter_t": vector_payload(relation_parameter),
        "node_coefficients": node_coefficients,
        "node_coefficient_sum": sum(node_coefficients),
        "full_exponent_vector": vector_payload(full_vector),
        "oriented_ratio": {
            "numerator": oriented_numerator,
            "denominator": oriented_denominator,
        },
        "normalization_sign": normalization_sign,
        "normalized_node_coefficients": normalized_coefficients,
        "normalized_exponent_vector": vector_payload(normalized_vector),
        "tail_pair": {"a": numerator, "b": denominator},
        "used_primes": [
            SUPPORT[index]
            for index in range(len(SUPPORT))
            if normalized_vector[index] != 0
        ],
    }

    if (prime is None) != (k_value is None):
        raise AssertionError("prime and K must be supplied together")
    if prime is None or k_value is None:
        return hit
    if k_value % (numerator * denominator):
        raise AssertionError("recovered tails did not divide K")
    normal_c = k_value // (numerator * denominator)
    if (numerator + denominator) % MODULUS:
        raise AssertionError("recovered tails did not sum to a multiple of R")
    normal_a = (numerator + denominator) // MODULUS
    gap_numerator = 4 * numerator * numerator * normal_c + 1
    if gap_numerator % MODULUS:
        raise AssertionError("Type I gap was not integral")
    gap = gap_numerator // MODULUS
    center_divisor = numerator * numerator * normal_c
    if not center_divisor < k_value:
        raise AssertionError("Type I center divisor was not strict")
    if k_value != numerator * normal_c * denominator:
        raise AssertionError("Type I normal form did not reconstruct K")
    if prime != 4 * normal_a * numerator * normal_c - gap:
        raise AssertionError("Type I normal form did not reconstruct p")
    if math.gcd(normal_a, numerator) != 1:
        raise AssertionError("Type I normal form lost coprimality")
    if numerator * prime + normal_a != denominator * gap:
        raise AssertionError("Type I divisibility identity failed")

    denominators = [
        normal_a * numerator * normal_c,
        normal_a * normal_c * denominator,
        prime * k_value,
    ]
    if sum((Fraction(1, value) for value in denominators), Fraction()) != Fraction(
        4, prime
    ):
        raise AssertionError("Type I unit-fraction identity failed")
    hit["type_I_certificate"] = {
        "A": normal_a,
        "B": numerator,
        "C": normal_c,
        "H": denominator,
        "h": gap,
        "center_divisor": center_divisor,
        "unit_fraction": {
            "left": [4, prime],
            "denominators": denominators,
            "verified": True,
        },
    }
    return hit


def certify_capacity(
    capacities: dict[int, int],
    vectors: list[sympy.Matrix],
    relation_matrix: sympy.Matrix,
    *,
    prime: int | None = None,
    k_value: int | None = None,
    collect_all_hits: bool = False,
) -> dict[str, object]:
    if not capacities or any(
        support_prime not in SUPPORT or capacity <= 0
        for support_prime, capacity in capacities.items()
    ):
        raise ValueError("capacities must be positive and lie in cycle support")
    internal_indices = [
        index for index, support_prime in enumerate(SUPPORT) if support_prime in capacities
    ]
    external_indices = [
        index
        for index, support_prime in enumerate(SUPPORT)
        if support_prime not in capacities
    ]
    external_matrix = select_rows(relation_matrix, external_indices)
    external_rhs = -select_rows(vectors[0], external_indices)
    external_payload, t0, kernel = solve_external(external_matrix, external_rhs)

    result: dict[str, object] = {
        "capacity": [[support_prime, capacities[support_prime]] for support_prime in capacities],
        "internal_primes": [SUPPORT[index] for index in internal_indices],
        "external_primes": [SUPPORT[index] for index in external_indices],
        "external_stage": external_payload,
    }
    if t0 is None or kernel is None:
        result["status"] = MISS_EXTERNAL
        return result

    internal_base = select_rows(vectors[0], internal_indices) + select_rows(
        relation_matrix, internal_indices
    ) * t0
    internal_matrix = select_rows(relation_matrix, internal_indices) * kernel
    internal_replay = smith_replay(internal_matrix)
    target_signature = quotient_signature(internal_replay, internal_base)
    box_ranges = [
        range(-capacities[SUPPORT[index]], capacities[SUPPORT[index]] + 1)
        for index in internal_indices
    ]
    box_size = math.prod(len(values) for values in box_ranges)
    reachable_signatures: set[tuple[int, ...]] = set()
    first_hit: tuple[int, ...] | None = None
    hit_vectors: list[tuple[int, ...]] = []
    points_checked = 0
    for box_vector in itertools.product(*box_ranges):
        points_checked += 1
        signature = quotient_signature(internal_replay, sympy.Matrix(box_vector))
        reachable_signatures.add(signature)
        if signature == target_signature:
            hit_vector = tuple(int(value) for value in box_vector)
            hit_vectors.append(hit_vector)
            if first_hit is None:
                first_hit = hit_vector
    if points_checked != box_size:
        raise AssertionError("capacity box enumeration was incomplete")

    internal_payload: dict[str, object] = {
        "affine_lattice": "x_internal = c + A_internal * u",
        "c": vector_payload(internal_base),
        "A_internal": matrix_payload(internal_matrix),
        "smith": smith_payload(internal_replay),
        "signature_components": signature_components(internal_replay),
        "target_signature_sigma_c": list(target_signature),
        "box_size": box_size,
        "box_points_checked": points_checked,
        "reachable_signature_count": len(reachable_signatures),
        "hit_vector_count": len(hit_vectors),
    }
    result["internal_stage"] = internal_payload
    if first_hit is None:
        sorted_signatures = sorted(reachable_signatures)
        if target_signature in reachable_signatures:
            raise AssertionError("capacity miss retained the target signature")
        internal_payload.update(
            {
                "reachable_signatures": [list(value) for value in sorted_signatures],
                "target_signature_absent": True,
            }
        )
        result["status"] = MISS_CAPACITY
        return result

    hit = recover_hit(
        first_hit,
        internal_indices,
        internal_base,
        internal_replay,
        t0,
        kernel,
        vectors,
        relation_matrix,
        capacities,
        prime,
        k_value,
    )
    internal_payload["target_signature_absent"] = False
    result["status"] = HIT
    result["hit"] = hit
    if collect_all_hits:
        result["all_hits"] = [
            recover_hit(
                hit_vector,
                internal_indices,
                internal_base,
                internal_replay,
                t0,
                kernel,
                vectors,
                relation_matrix,
                capacities,
                prime,
                k_value,
            )
            for hit_vector in hit_vectors
        ]
    return result


def fixture_certificate(
    prime: int,
    expected_status: str,
    vectors: list[sympy.Matrix],
    relation_matrix: sympy.Matrix,
) -> dict[str, object]:
    if not sympy.isprime(prime) or prime % 24 != 1:
        raise AssertionError("fixture prime was not a core prime")
    numerator = prime * MODULUS + 1
    if numerator % 4:
        raise AssertionError("fixture did not define an integral K")
    k_value = numerator // 4
    factors = {int(q): int(e) for q, e in sympy.factorint(k_value).items()}
    if factors.get(2) != 1 or factors.get(3) != 1:
        raise AssertionError("fixture lost the exact core edge capacities")
    for coordinate, label in zip(SELECTED, EDGE_LABELS):
        if valuation(coordinate, label) <= factors.get(label, 0):
            raise AssertionError("fixture cycle edge was not strictly overhigh")
    capacities = {
        support_prime: factors[support_prime]
        for support_prime in SUPPORT
        if support_prime in factors
    }
    certificate = certify_capacity(
        capacities,
        vectors,
        relation_matrix,
        prime=prime,
        k_value=k_value,
    )
    if certificate["status"] != expected_status:
        raise AssertionError(
            f"fixture p={prime} changed status: {certificate['status']}"
        )
    certificate.update(
        {
            "p": prime,
            "R": MODULUS,
            "K": k_value,
            "K_factorization": [[q, e] for q, e in sorted(factors.items())],
            "inactive_K_factors": [
                [q, e] for q, e in sorted(factors.items()) if q not in SUPPORT
            ],
        }
    )
    return certificate


def primitive_mask_progression(
    selected_optional: tuple[int, ...],
) -> dict[str, object]:
    """Return one primitive CRT class realizing an exact squarefree mask."""

    optional = [5, 13, 31, 43]
    selected = set(selected_optional)
    moduli = [16, 9]
    residues = [9, 1]
    local_conditions: list[dict[str, object]] = [
        {
            "prime": 2,
            "included": True,
            "modulus": 16,
            "residue": 9,
            "guarantee": "v_2(K) = 1",
        },
        {
            "prime": 3,
            "included": True,
            "modulus": 9,
            "residue": 1,
            "guarantee": "v_3(K) = 1",
        },
    ]
    for prime in optional:
        if prime in selected:
            root_mod_prime = (-pow(MODULUS, -1, prime)) % prime
            residue = next(
                root_mod_prime + lift * prime
                for lift in range(prime)
                if (MODULUS * (root_mod_prime + lift * prime) + 1)
                % (prime * prime)
            )
            modulus = prime * prime
            guarantee = f"v_{prime}(K) = 1"
        else:
            residue = 1
            modulus = prime
            guarantee = f"v_{prime}(K) = 0"
        moduli.append(modulus)
        residues.append(residue)
        local_conditions.append(
            {
                "prime": prime,
                "included": prime in selected,
                "modulus": modulus,
                "residue": residue,
                "guarantee": guarantee,
            }
        )

    crt_result = crt(moduli, residues, check=True)
    if crt_result is None:
        raise AssertionError("mask congruences unexpectedly failed CRT")
    combined_residue, combined_modulus = map(int, crt_result)
    if math.gcd(combined_residue, combined_modulus) != 1:
        raise AssertionError("combined mask class was not primitive")
    if combined_residue % 24 != 1:
        raise AssertionError("combined mask class was not a core class")
    if (MODULUS * combined_residue + 1) % 4:
        raise AssertionError("combined mask class did not define integral K")
    representative_k = (MODULUS * combined_residue + 1) // 4
    if valuation(representative_k, 2) != 1 or valuation(representative_k, 3) != 1:
        raise AssertionError("combined class lost an exact fixed valuation")
    observed_optional = {
        prime for prime in optional if valuation(representative_k, prime) == 1
    }
    if observed_optional != selected:
        raise AssertionError("combined class did not realize the declared mask")

    return {
        "residue": combined_residue,
        "modulus": combined_modulus,
        "primitive": True,
        "core_congruence": "p = 1 (mod 24)",
        "local_conditions": local_conditions,
    }


def mask_phase(
    vectors: list[sympy.Matrix], relation_matrix: sympy.Matrix
) -> dict[str, object]:
    fixed = [2, 3]
    optional = [5, 13, 31, 43]
    rows: list[dict[str, object]] = []
    full_results: dict[tuple[int, ...], dict[str, object]] = {}
    counts = {MISS_EXTERNAL: 0, MISS_CAPACITY: 0, HIT: 0}
    for mask in range(1 << len(optional)):
        selected_optional = tuple(
            prime for index, prime in enumerate(optional) if mask & (1 << index)
        )
        capacities = {prime: 1 for prime in [*fixed, *selected_optional]}
        result = certify_capacity(capacities, vectors, relation_matrix)
        status = str(result["status"])
        expected = (
            MISS_EXTERNAL
            if not selected_optional
            else HIT
            if 31 in selected_optional or {5, 13, 43} <= set(selected_optional)
            else MISS_CAPACITY
        )
        if status != expected:
            raise AssertionError(
                f"mask {selected_optional} changed status: {status} != {expected}"
            )
        counts[status] += 1
        full_results[selected_optional] = result
        rows.append(
            {
                "mask": mask,
                "optional_support": list(selected_optional),
                "status": status,
                "prime_progression": primitive_mask_progression(selected_optional),
            }
        )

    expected_counts = {MISS_EXTERNAL: 1, MISS_CAPACITY: 6, HIT: 9}
    if counts != expected_counts:
        raise AssertionError(f"mask status counts changed: {counts}")
    minimal_masks = [
        support
        for support, result in full_results.items()
        if result["status"] == HIT
        and not any(
            full_results[candidate]["status"] == HIT
            for candidate in full_results
            if set(candidate) < set(support)
        )
    ]
    if minimal_masks != [(31,), (5, 13, 43)]:
        raise AssertionError(f"minimal hit carriers changed: {minimal_masks}")
    minimal_carriers = []
    for support in minimal_masks:
        hit = full_results[support]["hit"]
        minimal_carriers.append(
            {
                "optional_support": list(support),
                "box_vector": hit["box_vector"],
                "normalized_exponent_vector": hit["normalized_exponent_vector"],
                "normalized_node_coefficients": hit[
                    "normalized_node_coefficients"
                ],
                "tail_pair": hit["tail_pair"],
                "used_primes": hit["used_primes"],
            }
        )

    return {
        "fixed_primes": fixed,
        "optional_primes": optional,
        "capacity_per_present_prime": 1,
        "mask_count": len(rows),
        "status_counts": counts,
        "classification": {
            "MISS_EXTERNAL": "the optional support is empty",
            "HIT": "31 is present, or 5, 13, and 43 are all present",
            "MISS_CAPACITY": "all other nonempty optional supports",
        },
        "rows": rows,
        "minimal_hit_carriers": minimal_carriers,
    }


def full_unit_box_phase(
    vectors: list[sympy.Matrix], relation_matrix: sympy.Matrix
) -> dict[str, object]:
    capacities = {prime: 1 for prime in SUPPORT}
    result = certify_capacity(
        capacities,
        vectors,
        relation_matrix,
        collect_all_hits=True,
    )
    if result["status"] != HIT:
        raise AssertionError("the full unit box unexpectedly missed")
    all_hits = result.pop("all_hits")
    ratios: dict[tuple[int, int], dict[str, object]] = {}
    for hit in all_hits:
        tail_pair = hit["tail_pair"]
        pair = (int(tail_pair["a"]), int(tail_pair["b"]))
        ratios.setdefault(pair, hit)

    expected_pairs = [
        (1, 93),
        (5, 559),
        (13, 645),
        (30, 1333),
        (62, 1677),
        (13, 2666),
    ]
    if set(ratios) != set(expected_pairs):
        raise AssertionError(f"full-unit-box ratios changed: {sorted(ratios)}")
    rows = []
    for pair in expected_pairs:
        hit = ratios[pair]
        if (pair[0] + pair[1]) % MODULUS:
            raise AssertionError("full-box ratio tails did not sum to a multiple of R")
        rows.append(
            {
                "tail_pair": {"a": pair[0], "b": pair[1]},
                "sum_multiple_of_R": (pair[0] + pair[1]) // MODULUS,
                "support": hit["used_primes"],
                "box_vector": hit["box_vector"],
                "relation_parameter_t": hit["relation_parameter_t"],
                "normalized_exponent_vector": hit[
                    "normalized_exponent_vector"
                ],
                "normalized_node_coefficients": hit[
                    "normalized_node_coefficients"
                ],
            }
        )

    support_sets = {tuple(row["support"]) for row in rows}
    minimal_supports = sorted(
        support
        for support in support_sets
        if not any(set(candidate) < set(support) for candidate in support_sets)
    )
    expected_minimal = [(2, 13, 31, 43), (3, 31), (5, 13, 43)]
    if minimal_supports != expected_minimal:
        raise AssertionError(
            f"full-unit-box minimal supports changed: {minimal_supports}"
        )

    internal_stage = result["internal_stage"]
    return {
        "capacity_per_support_prime": 1,
        "box_size": internal_stage["box_size"],
        "box_points_checked": internal_stage["box_points_checked"],
        "oriented_hit_vector_count": len(all_hits),
        "normalized_ratio_count": len(rows),
        "ratios_up_to_inversion": rows,
        "support_minimal_elements": [list(support) for support in minimal_supports],
    }


def run() -> dict[str, object]:
    vectors, relation_matrix = cycle_matrices()
    validate_cycle(vectors, relation_matrix)
    fixtures = [
        fixture_certificate(313, MISS_EXTERNAL, vectors, relation_matrix),
        fixture_certificate(73, MISS_CAPACITY, vectors, relation_matrix),
        fixture_certificate(5_113, HIT, vectors, relation_matrix),
        fixture_certificate(6_415_417, HIT, vectors, relation_matrix),
    ]
    fixture_by_prime = {int(row["p"]): row for row in fixtures}
    external_failures = fixture_by_prime[313]["external_stage"][
        "solvability_failures"
    ]
    if not any(
        failure["kind"] == "diagonal_divisibility"
        for failure in external_failures
    ):
        raise AssertionError("p=313 lost its replayable external obstruction")
    miss_internal = fixture_by_prime[73]["internal_stage"]
    if (
        miss_internal["box_size"] != 27
        or miss_internal["box_points_checked"] != 27
        or not miss_internal["target_signature_absent"]
        or len(miss_internal["reachable_signatures"])
        != miss_internal["reachable_signature_count"]
    ):
        raise AssertionError("p=73 lost its complete capacity-miss certificate")
    hit_5113 = fixture_by_prime[5_113]["hit"]
    if hit_5113["tail_pair"] != {"a": 1, "b": 93}:
        raise AssertionError("p=5113 lost the expected 1/93 witness")
    if not hit_5113["type_I_certificate"]["unit_fraction"]["verified"]:
        raise AssertionError("p=5113 lost its unit-fraction verification")

    return {
        "schema_version": "cycle-lattice-capacity/v1",
        "arithmetic": (
            "For the R=47 five-cycle, solve external exponent cancellation "
            "with replayable Smith data, enumerate the exact internal capacity "
            "box by quotient signatures, and recover every stored hit as an "
            "odd cycle combination and a Type I unit-fraction certificate."
        ),
        "scope_note": (
            "This is an exact certificate for the declared cycle, fixtures, "
            "and 16 squarefree support masks. It is not a proof that every "
            "formal cycle or every core prime has a capacity hit."
        ),
        "cycle": {
            "R": MODULUS,
            "nodes": CYCLE,
            "node_pairs": [[node, MODULUS - node] for node in CYCLE],
            "selected_coordinates": SELECTED,
            "edge_labels": EDGE_LABELS,
            "support_primes": SUPPORT,
            "oriented_node_vectors": [vector_payload(vector) for vector in vectors],
            "relation_generators": [
                "z1-z0",
                "z2-z0",
                "z3-z0",
                "z4-z0",
                "2*z0",
            ],
            "relation_matrix_M": matrix_payload(relation_matrix),
        },
        "fixtures": fixtures,
        "full_unit_box_phase": full_unit_box_phase(vectors, relation_matrix),
        "core_squarefree_mask_phase": mask_phase(vectors, relation_matrix),
        "script_sha256": sha256(Path(__file__)),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--verify",
        nargs="?",
        const=DEFAULT_OUTPUT,
        type=Path,
        help="recompute and compare with PATH (default: the standard result JSON)",
    )
    args = parser.parse_args()
    payload = run()
    if args.verify is not None:
        stored = json.loads(args.verify.read_text(encoding="utf-8"))
        if stored != payload:
            raise AssertionError(f"stored certificate differs from replay: {args.verify}")
        action = "verified"
        path = args.verify
    else:
        args.output.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        action = "wrote"
        path = args.output
    print(
        json.dumps(
            {
                "action": action,
                "path": str(path),
                "fixture_statuses": {
                    str(row["p"]): row["status"] for row in payload["fixtures"]
                },
                "mask_status_counts": payload["core_squarefree_mask_phase"][
                    "status_counts"
                ],
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
