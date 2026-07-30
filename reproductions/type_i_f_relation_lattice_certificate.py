#!/usr/bin/env python3
"""Reconstruct exact relation-lattice F certificates on the frozen 45-state profile."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
from pathlib import Path
import sys

import sympy
from sympy.matrices.normalforms import hermite_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp


ROOT = Path(__file__).resolve().parents[1]
PAIR_SCRIPT = ROOT / "reproductions" / "type_i_linear_multi_active_pair_divisor_capacity.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-relation-lattice-certificate-results.json"
EXPECTED_INPUT_SHA256 = "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f"
EXPECTED_STATE_COUNT = 45


def load_pair_module():
    spec = importlib.util.spec_from_file_location("pair_capacity_for_lattice", PAIR_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {PAIR_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


pair = load_pair_module()


def solve_relation_lattice(
    factors: list[tuple[int, int]], certificate: dict[str, object]
) -> tuple[sympy.Matrix, list[int], list[int]]:
    orders = [int(component["order"]) for component in certificate["components"]]
    generator_logs = sympy.Matrix(certificate["generator_log_vectors"]).T
    diagonal = sympy.diag(*orders)
    congruence_matrix = generator_logs.row_join(-diagonal)
    domain_matrix = DomainMatrix.from_Matrix(
        congruence_matrix, fmt="dense"
    ).convert_to(sympy.ZZ)
    smith, left, right = smith_normal_decomp(domain_matrix)
    smith_matrix = smith.to_Matrix()
    left_matrix = left.to_Matrix()
    right_matrix = right.to_Matrix()
    dimension = len(factors)
    component_count = len(orders)
    if right_matrix.shape != (dimension + component_count, dimension + component_count):
        raise AssertionError("unexpected Smith transform shape")
    if left_matrix * congruence_matrix * right_matrix != smith_matrix:
        raise AssertionError("Smith decomposition reconstruction failed")

    relation_projection = right_matrix[:dimension, component_count:]
    relation_basis = hermite_normal_form(relation_projection)
    if relation_basis.det() == 0:
        raise AssertionError("relation lattice is not full rank")

    target = sympy.Matrix([order // 2 for order in orders])
    transformed_target = left_matrix * target
    coordinates = sympy.zeros(dimension + component_count, 1)
    for row in range(component_count):
        diagonal_entry = int(smith_matrix[row, row])
        if diagonal_entry == 0 or int(transformed_target[row]) % diagonal_entry:
            raise AssertionError("target is not in the generated subgroup")
        coordinates[row] = transformed_target[row] // diagonal_entry
    preimage = right_matrix * coordinates
    z0 = [int(value) for value in preimage[:dimension]]

    for row, order in enumerate(orders):
        residue = sum(
            int(generator_logs[row, column]) * z0[column]
            for column in range(dimension)
        )
        if (residue - int(target[row])) % order:
            raise AssertionError("target preimage does not reconstruct -1")

    for column in range(dimension):
        for row, order in enumerate(orders):
            if int(generator_logs[row, :].dot(relation_basis[:, column])) % order:
                raise AssertionError("relation basis does not lie in the kernel")
    return relation_basis, z0, orders


def box_audit(
    generator_logs: list[list[int]],
    orders: list[int],
    target: list[int],
    exponents: list[tuple[int, int]],
) -> tuple[int, bool]:
    checked = 0
    for vector in itertools.product(
        *[range(-exponent, exponent + 1) for _prime, exponent in exponents]
    ):
        checked += 1
        residues = tuple(
            sum(
                int(generator_logs[column][row]) * vector[column]
                for column in range(len(vector))
            )
            % orders[row]
            for row in range(len(orders))
        )
        if residues == tuple(target):
            return checked, True
    return checked, False


def reconstruct(input_path: Path) -> dict[str, object]:
    if pair.sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen full-spectrum input changed")
    rows = pair.load_rows(input_path)
    profiles = []
    total_box_points = 0
    for prime, R, _a, _s, K, _active in rows:
        factors = pair.source.exact_factorization(K)
        certificate = pair.source.unit_group_subgroup_certificate(factors, R)
        if not bool(certificate["target_in_generated_subgroup"]):
            raise AssertionError("a selected row is not F type")
        relation_basis, z0, orders = solve_relation_lattice(factors, certificate)
        target = [order // 2 for order in orders]
        checked, target_in_box = box_audit(
            certificate["generator_log_vectors"],
            orders,
            target,
            factors,
        )
        box_size = 1
        for _prime, exponent in factors:
            box_size *= 2 * exponent + 1
        if checked != box_size or target_in_box:
            raise AssertionError("the F box audit did not reproduce target absence")
        relation_index = abs(int(relation_basis.det()))
        if relation_index <= 0:
            raise AssertionError("invalid relation index")
        ambient_basis = pair.source.component_lattice_hnf(
            certificate["generator_log_vectors"], orders
        )
        ambient_index = abs(int(ambient_basis.det()))
        image_order = 1
        for order in orders:
            image_order *= order
        if ambient_index == 0 or image_order % ambient_index:
            raise AssertionError("invalid ambient subgroup index")
        image_order //= ambient_index
        if relation_index != image_order:
            raise AssertionError(
                f"relation index disagrees with image order: {relation_index} != {image_order}"
            )
        total_box_points += box_size
        profiles.append(
            {
                "prime": prime,
                "R": R,
                "K": K,
                "factorization": [[int(q), int(e)] for q, e in factors],
                "component_orders": orders,
                "relation_basis_columns": [
                    [int(relation_basis[row, column]) for row in range(relation_basis.rows)]
                    for column in range(relation_basis.cols)
                ],
                "relation_index": relation_index,
                "image_order": image_order,
                "target_preimage": z0,
                "box_size": box_size,
                "box_points_checked": checked,
                "target_in_generated_subgroup": True,
                "target_in_box": False,
            }
        )

    if len(profiles) != EXPECTED_STATE_COUNT:
        raise AssertionError(f"unexpected F-state count: {len(profiles)}")
    return {
        "arithmetic": "For every frozen finite-exponent F state, reconstruct a Smith/Hermite relation lattice, an affine preimage of -1, and an exhaustive integer-box miss certificate.",
        "scope_note": "Finite certificate reconstruction only. It verifies the 45 frozen F states and does not prove a certificate for all core primes or all possible states.",
        "input": input_path.name,
        "input_sha256": pair.sha256(input_path),
        "state_count": len(profiles),
        "total_box_points_checked": total_box_points,
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=pair.INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = reconstruct(args.input)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "state_count": payload["state_count"],
                "total_box_points_checked": payload["total_box_points_checked"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
