#!/usr/bin/env python3
"""Census higher-order G separators across 200 complete B>1 linear spectra."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json"
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-b-gt-one-high-order-separator-census-600m-results.json"
)
EXPECTED_INPUT_SHA256 = "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f"
EXPECTED_SUBGROUP_CHARACTER_R_COUNT = 6_522
EXPECTED_SEPARATOR_ORDER_COUNTS = {2: 6_461, 4: 49, 8: 12}
EXPECTED_HIGHER_ORDER_SEPARATOR_PRIME_COUNT = 57
EXPECTED_HIGHER_ORDER_COLLISION_RELATION_COUNT = 387
EXPECTED_HIGHER_ORDER_COLLISION_R_PAIR_COUNT = 342
EXPECTED_HIGHER_TO_HIGHER_RELATION_COUNT = 2
EXPECTED_HIGHER_TO_HIGHER_R_PAIR_COUNT = 2


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sources = load_module("b_gt_one_high_order_separator_sources", SOURCE_SCRIPT)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stable_sha256(rows: list[tuple[int, ...]]) -> str:
    return hashlib.sha256(
        "\n".join(",".join(str(value) for value in row) for row in rows).encode("ascii")
    ).hexdigest()


def load_subgroup_records(input_path: Path = INPUT) -> dict[int, list[dict[str, object]]]:
    """Read exactly the G states from the hash-frozen 200-prime full-spectrum audit."""
    if file_sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the full B>1-spectrum input changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    profiles = payload.get("profiles")
    if not isinstance(profiles, list) or len(profiles) != 200:
        raise AssertionError("full B>1-spectrum input lacks its 200 profiles")
    records_by_prime: dict[int, list[dict[str, object]]] = {}
    for profile in profiles:
        prime = int(profile["prime"])
        records = [
            dict(record)
            for record in profile["records"]
            if record["classification"] == "subgroup_character"
        ]
        records.sort(key=lambda record: int(record["R"]))
        records_by_prime[prime] = records
    if sum(len(records) for records in records_by_prime.values()) != EXPECTED_SUBGROUP_CHARACTER_R_COUNT:
        raise AssertionError("frozen subgroup-character count changed")
    return records_by_prime


def halfblock_two_injection_count(
    prime: int, R: int, states: list[tuple[int, int]]
) -> int:
    """Count directed endpoints t=3 (mod 4), verifying each half-block witness."""
    K = (prime * R + 1) // 4
    count = 0
    for a, s in states:
        for t, u in ((a, s), (s, a)):
            if t % 4 != 3:
                continue
            left = (t * R + 1) // 2
            right = (u * R + 1) // 2
            if (
                prime != a + s + a * s * R
                or u % 2 != 1
                or (t * R + 1) % 2
                or (u * R + 1) % 2
                or left * right != K
                or left % R != pow(2, -1, R)
            ):
                raise AssertionError("purported half-block two injection is invalid")
            count += 1
    return count


def classify_record(
    prime: int, stored: dict[str, object], states: list[tuple[int, int]]
) -> dict[str, object]:
    """Recover the separator order and two-residue data for one exact G state."""
    R = int(stored["R"])
    K = int(stored["K"])
    factors = sources.exact_factorization(K)
    certificate = sources.unit_group_subgroup_certificate(factors, R)
    if bool(certificate["target_in_generated_subgroup"]):
        raise AssertionError("stored G state contains its target in the support subgroup")
    depth = sources.two_power_character_depth(certificate)
    minimal_order = int(depth["minimal_separating_two_power_character_order"])
    injection_count = halfblock_two_injection_count(prime, R, states)
    two_order = int(sympy.n_order(2, R))
    minus_one_in_two_subgroup = bool(
        two_order % 2 == 0 and pow(2, two_order // 2, R) == R - 1
    )
    if injection_count and minus_one_in_two_subgroup:
        raise AssertionError("a G state contradicts the half-block two-residue escape")
    return {
        "R": R,
        "K": K,
        "K_factorization": [
            {"prime": int(factor), "exponent": int(exponent)}
            for factor, exponent in factors
        ],
        "source_state_count": int(stored["source_state_count"]),
        "two_injecting_endpoint_count": injection_count,
        "two_multiplicative_order": two_order,
        "minus_one_in_two_subgroup": minus_one_in_two_subgroup,
        "minimal_separating_two_power_character_order": minimal_order,
    }


def shared_odd_prime_relations(
    prime: int, records: list[dict[str, object]]
) -> list[dict[str, int]]:
    """List same-prime G-state collisions involving at least one higher-order separator."""
    relations: list[dict[str, int]] = []
    for index, left in enumerate(records):
        for right in records[index + 1 :]:
            left_order = int(left["minimal_separating_two_power_character_order"])
            right_order = int(right["minimal_separating_two_power_character_order"])
            if left_order <= 2 and right_order <= 2:
                continue
            shared = math.gcd(int(left["K"]), int(right["K"]))
            for factor, _ in sources.exact_factorization(shared):
                if factor == 2:
                    continue
                if left_order > 2:
                    high, other = left, right
                    high_order, other_order = left_order, right_order
                else:
                    high, other = right, left
                    high_order, other_order = right_order, left_order
                relations.append(
                    {
                        "prime": prime,
                        "higher_order_R": int(high["R"]),
                        "higher_order_separator_order": high_order,
                        "other_R": int(other["R"]),
                        "other_separator_order": other_order,
                        "shared_odd_prime": int(factor),
                    }
                )
    relations.sort(
        key=lambda row: (
            row["prime"],
            row["higher_order_R"],
            row["other_R"],
            row["shared_odd_prime"],
        )
    )
    return relations


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    """Audit separator orders and collision opportunities in all 200 complete spectra."""
    stored_by_prime = load_subgroup_records(input_path)
    profiles = []
    all_records: list[dict[str, object]] = []
    all_relations: list[dict[str, int]] = []
    for prime, stored_records in sorted(stored_by_prime.items()):
        states_by_R = sources.enumerate_linear_source_states(prime)[1]
        records = [
            classify_record(prime, stored, states_by_R[int(stored["R"])])
            for stored in stored_records
        ]
        records.sort(key=lambda record: int(record["R"]))
        relations = shared_odd_prime_relations(prime, records)
        order_counts = Counter(
            int(record["minimal_separating_two_power_character_order"])
            for record in records
        )
        digest_rows = [
            (
                int(record["R"]),
                int(record["K"]),
                int(record["two_injecting_endpoint_count"]),
                int(record["two_multiplicative_order"]),
                int(bool(record["minus_one_in_two_subgroup"])),
                int(record["minimal_separating_two_power_character_order"]),
            )
            for record in records
        ]
        profiles.append(
            {
                "prime": prime,
                "subgroup_character_R_count": len(records),
                "separator_order_counts": {
                    str(order): count for order, count in sorted(order_counts.items())
                },
                "higher_order_separator_R_count": sum(
                    count for order, count in order_counts.items() if order > 2
                ),
                "higher_order_collision_relation_count": len(relations),
                "record_sha256": stable_sha256(digest_rows),
                "records": records,
            }
        )
        all_records.extend(records)
        all_relations.extend(relations)

    order_counts = Counter(
        int(record["minimal_separating_two_power_character_order"])
        for record in all_records
    )
    high_records = [
        {"prime": profile["prime"], **record}
        for profile in profiles
        for record in profile["records"]
        if int(record["minimal_separating_two_power_character_order"]) > 2
    ]
    high_records.sort(key=lambda record: (int(record["prime"]), int(record["R"])))
    high_high_relations = [
        relation
        for relation in all_relations
        if int(relation["other_separator_order"]) > 2
    ]
    if (
        len(all_records) != EXPECTED_SUBGROUP_CHARACTER_R_COUNT
        or dict(order_counts) != EXPECTED_SEPARATOR_ORDER_COUNTS
        or len(high_records) != sum(
            count for order, count in EXPECTED_SEPARATOR_ORDER_COUNTS.items() if order > 2
        )
        or len({int(record["prime"]) for record in high_records})
        != EXPECTED_HIGHER_ORDER_SEPARATOR_PRIME_COUNT
        or len(all_relations) != EXPECTED_HIGHER_ORDER_COLLISION_RELATION_COUNT
        or len(
            {
                (relation["prime"], relation["higher_order_R"], relation["other_R"])
                for relation in all_relations
            }
        )
        != EXPECTED_HIGHER_ORDER_COLLISION_R_PAIR_COUNT
        or len(high_high_relations) != EXPECTED_HIGHER_TO_HIGHER_RELATION_COUNT
        or len(
            {
                (relation["prime"], relation["higher_order_R"], relation["other_R"])
                for relation in high_high_relations
            }
        )
        != EXPECTED_HIGHER_TO_HIGHER_R_PAIR_COUNT
    ):
        raise AssertionError("higher-order separator census changed")
    return {
        "arithmetic": (
            "for every subgroup-character state in the hash-frozen complete spectra behind 200 "
            "first-selected B>1 certificates, factor K, certify the support subgroup, recover the "
            "minimal separating 2-power character order, and enumerate same-prime shared odd K-primes "
            "whenever at least one endpoint has higher-order separation"
        ),
        "scope_note": (
            "The census detects where a cross-source higher-reciprocity comparison could be attempted. "
            "A shared prime or higher-order character is only a necessary input, not a target-hit proof."
        ),
        "input": input_path.name,
        "input_sha256": file_sha256(input_path),
        "subgroup_character_R_count": len(all_records),
        "separator_order_counts": {
            str(order): count for order, count in sorted(order_counts.items())
        },
        "higher_order_separator_R_count": len(high_records),
        "higher_order_separator_prime_count": len(
            {int(record["prime"]) for record in high_records}
        ),
        "two_injecting_R_count": sum(
            int(record["two_injecting_endpoint_count"]) > 0 for record in all_records
        ),
        "minus_one_in_two_subgroup_R_count": sum(
            bool(record["minus_one_in_two_subgroup"]) for record in all_records
        ),
        "higher_order_collision_relation_count": len(all_relations),
        "higher_order_collision_R_pair_count": len(
            {
                (relation["prime"], relation["higher_order_R"], relation["other_R"])
                for relation in all_relations
            }
        ),
        "higher_order_to_higher_order_relation_count": len(high_high_relations),
        "higher_order_to_higher_order_R_pair_count": len(
            {
                (relation["prime"], relation["higher_order_R"], relation["other_R"])
                for relation in high_high_relations
            }
        ),
        "higher_order_records": high_records,
        "higher_order_collision_relations": all_relations,
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                key: value
                for key, value in payload.items()
                if key
                not in {
                    "higher_order_records",
                    "higher_order_collision_relations",
                    "profiles",
                }
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
