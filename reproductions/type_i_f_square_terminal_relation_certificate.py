#!/usr/bin/env python3
"""Reconstruct exact relation-lattice F certificates for square-terminal states."""

from __future__ import annotations

from collections import Counter
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SQUARE_INPUT = ROOT / "reproductions" / "type-i-f-overflow-square-terminal-lift-results.json"
PROFILE_INPUT = ROOT / "reproductions" / "type-i-f-square-half-block-kneser-profile-results.json"
LATTICE_SCRIPT = ROOT / "reproductions" / "type_i_f_relation_lattice_certificate.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-square-terminal-relation-certificate-results.json"

EXPECTED_SQUARE_SHA256 = "ca3d74768cf90586834dfa7f8a127c760871cf5b5d27cc98be8ec96ec58dc9a1"
EXPECTED_PROFILE_SHA256 = "680d290b79ab9ca4cc6a4d8940c3aa5ad4ef7884a115153c82bb85bba36042c3"
EXPECTED_STATE_COUNT = 253


def load_lattice_module():
    spec = importlib.util.spec_from_file_location("square_terminal_lattice", LATTICE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {LATTICE_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


lattice = load_lattice_module()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_inputs() -> tuple[list[dict[str, object]], dict[tuple[int, int], dict[str, object]]]:
    if sha256(SQUARE_INPUT) != EXPECTED_SQUARE_SHA256:
        raise AssertionError("the frozen square-terminal input changed")
    if sha256(PROFILE_INPUT) != EXPECTED_PROFILE_SHA256:
        raise AssertionError("the frozen half-block profile input changed")
    square_payload = json.loads(SQUARE_INPUT.read_text(encoding="utf-8"))
    profile_payload = json.loads(PROFILE_INPUT.read_text(encoding="utf-8"))
    candidates = [dict(row) for row in square_payload.get("candidates", [])]
    profiles = {
        (int(row["prime"]), int(row["R"])): dict(row)
        for row in profile_payload.get("records", [])
    }
    if len(candidates) != EXPECTED_STATE_COUNT or len(profiles) != EXPECTED_STATE_COUNT:
        raise AssertionError("the frozen square-terminal profile is incomplete")
    return candidates, profiles


def reconstruct_row(
    row: dict[str, object], profile: dict[str, object]
) -> tuple[dict[str, object], int]:
    prime = int(row["prime"])
    R = int(row["R"])
    K = (prime * R + 1) // 4
    factors = lattice.pair.source.exact_factorization(K)
    certificate = lattice.pair.source.unit_group_subgroup_certificate(factors, R)
    if not bool(certificate["target_in_generated_subgroup"]):
        raise AssertionError("square-terminal row is not in the generated subgroup")
    relation_basis, target_preimage, orders = lattice.solve_relation_lattice(factors, certificate)
    target = [order // 2 for order in orders]
    checked, target_in_box = lattice.box_audit(
        certificate["generator_log_vectors"], orders, target, factors
    )
    box_size = math.prod(2 * exponent + 1 for _prime, exponent in factors)
    if checked != box_size or target_in_box:
        raise AssertionError("the relation-lattice box miss did not reproduce")
    relation_index = abs(int(relation_basis.det()))
    ambient_basis = lattice.pair.source.component_lattice_hnf(
        certificate["generator_log_vectors"], orders
    )
    ambient_index = abs(int(ambient_basis.det()))
    image_order = math.prod(orders) // ambient_index
    if relation_index != image_order:
        raise AssertionError("relation-lattice index disagrees with support subgroup order")
    record = {
        "prime": prime,
        "R": R,
        "source": int(row["source"]),
        "E": int(row["E"]),
        "a": int(row["a"]),
        "s": int(row["s"]),
        "K": K,
        "factorization": [[int(q), int(e)] for q, e in factors],
        "component_orders": [int(order) for order in orders],
        "relation_basis_columns": [
            [int(relation_basis[index, column]) for index in range(relation_basis.rows)]
            for column in range(relation_basis.cols)
        ],
        "relation_index": relation_index,
        "image_order": image_order,
        "target_preimage": [int(value) for value in target_preimage],
        "box_size": box_size,
        "box_points_checked": checked,
        "target_in_generated_subgroup": True,
        "target_in_box": False,
        "full_support_rank_with_two": int(profile["full_support_rank_with_two"]),
        "full_support_primes": [int(value) for value in profile["full_support_primes"]],
    }
    return record, box_size


def run() -> dict[str, object]:
    candidates, profiles = load_inputs()
    records: list[dict[str, object]] = []
    rank_counts: Counter[int] = Counter()
    box_sizes: list[int] = []
    for row in sorted(
        candidates,
        key=lambda item: (
            int(item["prime"]),
            int(item["R"]),
            int(item["source"]),
            int(item["E"]),
        ),
    ):
        key = (int(row["prime"]), int(row["R"]))
        if key not in profiles:
            raise AssertionError("square-terminal row is missing from the half-block profile")
        record, box_size = reconstruct_row(row, profiles[key])
        records.append(record)
        rank_counts[int(record["full_support_rank_with_two"])] += 1
        box_sizes.append(box_size)
    if len(records) != EXPECTED_STATE_COUNT:
        raise AssertionError("unexpected square-terminal certificate count")
    return {
        "arithmetic": (
            "For every frozen square-terminal F state, reconstruct the Smith/Hermite relation "
            "lattice, a target affine preimage of -1, and an exhaustive finite exponent-box miss."
        ),
        "scope_note": (
            "Finite certificate reconstruction only. It covers the 253 square-terminal states "
            "from the frozen overflow audit and does not prove a certificate for all core primes "
            "or all reachable states."
        ),
        "square_input": SQUARE_INPUT.name,
        "square_input_sha256": sha256(SQUARE_INPUT),
        "profile_input": PROFILE_INPUT.name,
        "profile_input_sha256": sha256(PROFILE_INPUT),
        "state_count": len(records),
        "total_box_points_checked": sum(box_sizes),
        "maximum_box_size": max(box_sizes),
        "all_target_in_generated_subgroup": all(bool(row["target_in_generated_subgroup"]) for row in records),
        "all_target_outside_box": all(not bool(row["target_in_box"]) for row in records),
        "full_support_rank_with_two_histogram": {
            str(rank): int(count) for rank, count in sorted(rank_counts.items())
        },
        "records": records,
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "state_count",
                    "total_box_points_checked",
                    "maximum_box_size",
                    "full_support_rank_with_two_histogram",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
