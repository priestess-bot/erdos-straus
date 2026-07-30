#!/usr/bin/env python3
"""Reconstruct relation-lattice certificates for lower-modulus F-box misses."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-f-overflow-r-modulus-repair-results.json"
SOURCE_INPUT = ROOT / "reproductions" / "type-i-f-overflow-support-boundary-results.json"
LATTICE_SCRIPT = ROOT / "reproductions" / "type_i_f_relation_lattice_certificate.py"
OUTPUT = ROOT / "reproductions" / "type-i-f-overflow-lower-modulus-relation-lattice-results.json"
EXPECTED_INPUT_SHA256 = "c656c91ebb02a33e8d1f5c78db70ce14ac5fbc2decc0db99e05bcbcc1fbee22f"
EXPECTED_SOURCE_SHA256 = "93c571a0fdfe12d18028c21d10c1f8445b1e34ae979489c852478d0bce8ad9b1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_lattice_module():
    spec = importlib.util.spec_from_file_location("lower_modulus_lattice", LATTICE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {LATTICE_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


lattice = load_lattice_module()


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the lower-modulus split input changed")
    if sha256(SOURCE_INPUT) != EXPECTED_SOURCE_SHA256:
        raise AssertionError("the frozen factorization input changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    source_payload = json.loads(SOURCE_INPUT.read_text(encoding="utf-8"))
    source_rows = {
        (int(row["prime"]), int(row["R"]), tuple(row["witness_exponents"])): dict(row)
        for row in source_payload["records"]
        if row.get("within_radius_cap")
    }

    profiles: list[dict[str, object]] = []
    total_box_points = 0
    for row in payload["records"]:
        key = (int(row["prime"]), int(row["R"]), tuple(row["witness_exponents"]))
        if key not in source_rows:
            raise AssertionError("a split row is missing its frozen factorization")
        source_row = source_rows[key]
        for candidate in row["candidates"]:
            if candidate["lower_modulus_classification"] != "F_box_miss":
                continue
            prime = int(row["prime"])
            original_R = int(row["R"])
            modulus = int(candidate["balanced_t"])
            if modulus <= 1 or modulus % 4 != 1:
                raise AssertionError("the lower modulus lost its 1 mod 4 parity")
            factors = [(int(q), int(nu)) for q, nu in source_row["factorization"]]
            certificate = lattice.pair.source.unit_group_subgroup_certificate(factors, modulus)
            if not bool(certificate["target_in_generated_subgroup"]):
                raise AssertionError("an F-box miss is not in the lower-modulus support subgroup")
            relation_basis, z0, orders = lattice.solve_relation_lattice(factors, certificate)
            target = [order // 2 for order in orders]
            checked, target_in_box = lattice.box_audit(
                certificate["generator_log_vectors"],
                orders,
                target,
                factors,
            )
            box_size = math.prod(2 * nu + 1 for _prime, nu in factors)
            if checked != box_size or target_in_box:
                raise AssertionError("the lower-modulus F-box miss was not exhaustive")
            relation_index = abs(int(relation_basis.det()))
            if relation_index != int(candidate["lower_modulus_subgroup_order"]):
                raise AssertionError("relation index disagrees with subgroup closure")
            ambient_basis = lattice.pair.source.component_lattice_hnf(
                certificate["generator_log_vectors"], orders
            )
            ambient_index = abs(int(ambient_basis.det()))
            image_order = math.prod(orders)
            if ambient_index == 0 or image_order % ambient_index:
                raise AssertionError("invalid lower-modulus ambient subgroup index")
            image_order //= ambient_index
            if relation_index != image_order:
                raise AssertionError("relation index disagrees with image order")
            total_box_points += box_size
            profiles.append(
                {
                    "prime": prime,
                    "orientation": row["orientation"],
                    "original_R": original_R,
                    "gap": int(candidate["gap"]),
                    "lower_modulus": modulus,
                    "balanced_pair_gcd": int(candidate["balanced_pair_gcd"]),
                    "factorization": [[int(q), int(e)] for q, e in factors],
                    "component_orders": orders,
                    "relation_basis_columns": [
                        [int(relation_basis[index, column]) for index in range(relation_basis.rows)]
                        for column in range(relation_basis.cols)
                    ],
                    "relation_index": relation_index,
                    "image_order": image_order,
                    "target_preimage": z0,
                    "box_size": box_size,
                    "box_points_checked": checked,
                    "target_in_generated_subgroup": True,
                    "target_in_box": False,
                    "order_two_to_minus_one": candidate["lower_modulus_order_two_to_minus_one"],
                    "dyadic_budget": candidate["lower_modulus_dyadic_budget"],
                    "dyadic_budget_gap": candidate["lower_modulus_dyadic_budget_gap"],
                }
            )

    by_orientation = {
        orientation: [profile for profile in profiles if profile["orientation"] == orientation]
        for orientation in ("forward", "reverse")
    }
    if len(profiles) != 42:
        raise AssertionError(f"unexpected lower-modulus F-box miss count: {len(profiles)}")
    return {
        "arithmetic": (
            "For every strict balanced endpoint descent classified as a lower-modulus "
            "F-box miss, Smith/Hermite transforms reconstruct the support relation lattice "
            "and an exhaustive affine-box miss at t=R/m."
        ),
        "scope_note": (
            "This is a finite relation-lattice certificate on the frozen 48 strict descents. "
            "The reduced modulus is t=1 mod 4, so the certificate is a quotient F interface, "
            "not itself a legal Type-I gap or a global descent theorem."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "factorization_input": SOURCE_INPUT.name,
        "factorization_input_sha256": sha256(SOURCE_INPUT),
        "state_count": len(profiles),
        "total_box_points_checked": total_box_points,
        "maximum_box_size": max(int(profile["box_size"]) for profile in profiles),
        "minimum_relation_index": min(int(profile["relation_index"]) for profile in profiles),
        "maximum_relation_index": max(int(profile["relation_index"]) for profile in profiles),
        "order_two_target_count": sum(
            profile["order_two_to_minus_one"] is not None for profile in profiles
        ),
        "profiles_by_orientation": {
            orientation: {
                "state_count": len(rows),
                "total_box_points_checked": sum(int(row["box_size"]) for row in rows),
                "order_two_target_count": sum(
                    row["order_two_to_minus_one"] is not None for row in rows
                ),
            }
            for orientation, rows in by_orientation.items()
        },
        "profiles": profiles,
    }


def main() -> int:
    result = run()
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "state_count",
                    "total_box_points_checked",
                    "maximum_box_size",
                    "minimum_relation_index",
                    "maximum_relation_index",
                    "order_two_target_count",
                    "profiles_by_orientation",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
