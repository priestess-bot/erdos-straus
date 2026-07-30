#!/usr/bin/env python3
"""Count exact active prime directions in the four adversarial F cores."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from itertools import combinations
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json"
SOURCE = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-linear-adversarial-core-f-active-direction-profile-600m-results.json"
EXPECTED_INPUT_SHA256 = "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f"
ADVERSARIAL_PRIMES = (878_089, 26_034_649, 57_399_241, 283_319_689)
EXPECTED_COUNTS = {3: 3, 4: 9, 5: 13, 6: 12, 7: 8}
EXPECTED_PROFILE_SHARED_PAIRS = {
    878_089: (1, 1),
    26_034_649: (5, 15),
    57_399_241: (206, 276),
    283_319_689: (45, 78),
}
EXPECTED_TOTAL_SHARED_PAIRS = (599, 990)


def load_source():
    spec = importlib.util.spec_from_file_location("active_direction_source", SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOURCE.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sources = load_source()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_f_states(path: Path = INPUT) -> dict[int, list[dict[str, object]]]:
    if sha256(path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen full-spectrum input changed")
    payload = json.loads(path.read_text(encoding="utf-8"))
    selected: dict[int, list[dict[str, object]]] = {}
    for profile in payload["profiles"]:
        prime = int(profile["prime"])
        if prime not in ADVERSARIAL_PRIMES:
            continue
        rows = [
            dict(row)
            for row in profile["records"]
            if row["classification"] == "finite_exponent"
        ]
        selected[prime] = sorted(rows, key=lambda row: int(row["R"]))
    if tuple(sorted(selected)) != ADVERSARIAL_PRIMES:
        raise AssertionError("the four adversarial profiles are incomplete")
    if sum(len(rows) for rows in selected.values()) != 45:
        raise AssertionError("the frozen F-state count changed")
    return selected


def active_direction_record(prime: int, stored: dict[str, object]) -> dict[str, object]:
    R = int(stored["R"])
    K = int(stored["K"])
    factors = sources.exact_factorization(K)
    divisor_residues = {
        int(divisor) % R
        for divisor in sources.divisors_from_factorization(factors)
    }
    certificate = sources.unit_group_subgroup_certificate(factors, R)
    if not bool(stored["target_in_generated_subgroup"]) or not bool(
        certificate["target_in_generated_subgroup"]
    ):
        raise AssertionError("the selected state is not an exact F state")
    target = (R - 1) % R
    if target in {
        left * pow(right, -1, R) % R
        for left in divisor_residues
        for right in divisor_residues
    }:
        raise AssertionError("the selected F state contains the target")
    active_primes = [
        int(prime_factor)
        for prime_factor, _ in factors
        if {
            int(prime_factor) * residue % R for residue in divisor_residues
        }
        != divisor_residues
    ]
    return {
        "prime": prime,
        "R": R,
        "K": K,
        "divisor_residue_count": len(divisor_residues),
        "prime_support_count": len(factors),
        "active_direction_count": len(active_primes),
        "active_primes": active_primes,
    }


def run_audit(path: Path = INPUT) -> dict[str, object]:
    selected = load_f_states(path)
    profiles = []
    all_records = []
    for prime in ADVERSARIAL_PRIMES:
        records = [active_direction_record(prime, row) for row in selected[prime]]
        counts = Counter(int(row["active_direction_count"]) for row in records)
        active_prime_occurrences = Counter(
            prime_factor
            for row in records
            for prime_factor in row["active_primes"]
        )
        shared_pairs = sum(
            bool(set(left["active_primes"]) & set(right["active_primes"]))
            for left, right in combinations(records, 2)
        )
        total_pairs = len(records) * (len(records) - 1) // 2
        if (shared_pairs, total_pairs) != EXPECTED_PROFILE_SHARED_PAIRS[prime]:
            raise AssertionError(
                f"shared active-pair profile changed for {prime}: "
                f"{(shared_pairs, total_pairs)}"
            )
        profiles.append(
            {
                "prime": prime,
                "finite_exponent_R_count": len(records),
                "active_direction_counts": {
                    str(count): int(counts[count]) for count in sorted(counts)
                },
                "active_prime_occurrences": {
                    str(prime_factor): int(count)
                    for prime_factor, count in sorted(active_prime_occurrences.items())
                },
                "shared_active_pair_count": shared_pairs,
                "total_pair_count": total_pairs,
                "records": records,
            }
        )
        all_records.extend(records)
    total_counts = Counter(int(row["active_direction_count"]) for row in all_records)
    distribution = {
        str(count): int(total_counts[count]) for count in sorted(total_counts)
    }
    expected_distribution = {
        str(key): value for key, value in EXPECTED_COUNTS.items()
    }
    if distribution != expected_distribution:
        raise AssertionError(f"active-direction distribution changed: {distribution}")
    if any(int(row["active_direction_count"]) < 3 for row in all_records):
        raise AssertionError("an adversarial F state has fewer than three active directions")
    total_shared_pairs = sum(
        bool(set(left["active_primes"]) & set(right["active_primes"]))
        for left, right in combinations(all_records, 2)
    )
    total_pairs = len(all_records) * (len(all_records) - 1) // 2
    if (total_shared_pairs, total_pairs) != EXPECTED_TOTAL_SHARED_PAIRS:
        raise AssertionError(
            f"total shared active-pair profile changed: "
            f"{(total_shared_pairs, total_pairs)}"
        )
    active_prime_occurrences = Counter(
        prime_factor
        for row in all_records
        for prime_factor in row["active_primes"]
    )
    return {
        "arithmetic": (
            "for the 45 finite-exponent states in the four adversarial cores, compute "
            "A_R(K) from every divisor of K, test each support prime q by q*A_R(K)=A_R(K), "
            "and count the prime directions surviving the exact stabilizer"
        ),
        "scope_note": (
            "This is a finite profile of four adversarial cores. It rules out the single-active "
            "model on this input, but says nothing about all core primes or multi-active closure."
        ),
        "input": path.name,
        "input_sha256": sha256(path),
        "prime_count": len(ADVERSARIAL_PRIMES),
        "finite_exponent_R_count": len(all_records),
        "active_direction_distribution": distribution,
        "active_direction_occurrence_total": sum(active_prime_occurrences.values()),
        "active_prime_count": len(active_prime_occurrences),
        "shared_active_pair_count": total_shared_pairs,
        "total_pair_count": total_pairs,
        "top_active_primes": [
            [int(prime_factor), int(count)]
            for prime_factor, count in active_prime_occurrences.most_common(20)
        ],
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.input)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {key: value for key, value in payload.items() if key != "profiles"},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
