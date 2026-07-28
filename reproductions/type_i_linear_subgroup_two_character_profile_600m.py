#!/usr/bin/env python3
"""Profile two-residue coverage and separator orders at every frozen G-type state."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
INPUT = ROOT / "reproductions" / "type-i-linear-general-b-obstruction-mixture-profile-600m-results.json"
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-linear-subgroup-two-character-profile-600m-results.json"
)
EXPECTED_INPUT_SHA256 = "dce587d6e6703e5cdcb81b6cd05c16989394a7321d2d14515ea2eda6c2aec44d"
EXPECTED_PER_PRIME_G_COUNTS = {
    214_729: 19,
    878_089: 21,
    2_210_569: 21,
    13_782_409: 31,
    64_214_329: 25,
    105_295_129: 41,
    536_944_489: 32,
}


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sources = load_module("subgroup_two_character_sources", SOURCE_SCRIPT)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stable_sha256(rows: list[tuple[int, ...]]) -> str:
    return hashlib.sha256(
        "\n".join(",".join(str(value) for value in row) for row in rows).encode("ascii")
    ).hexdigest()


def load_subgroup_records(input_path: Path = INPUT) -> list[tuple[int, dict[str, object]]]:
    """Read exactly the 190 G-type states from a hash-frozen full-spectrum audit."""
    if file_sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen obstruction-mixture input changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    profiles = payload.get("profiles")
    if not isinstance(profiles, list):
        raise AssertionError("obstruction-mixture input lacks profiles")
    result = []
    for profile in profiles:
        prime = int(profile["prime"])
        subgroup_records = [
            dict(record)
            for record in profile["records"]
            if record["classification"] == "subgroup_character"
        ]
        if len(subgroup_records) != EXPECTED_PER_PRIME_G_COUNTS[prime]:
            raise AssertionError("frozen subgroup-character count changed")
        result.extend((prime, record) for record in subgroup_records)
    if len(result) != sum(EXPECTED_PER_PRIME_G_COUNTS.values()):
        raise AssertionError("frozen subgroup-character total changed")
    return result


def endpoint_count_with_halfblock_two_injection(
    prime: int, R: int, states: list[tuple[int, int]]
) -> int:
    """Count directed endpoints t=3 (mod 4), each of which injects 2 into H_R(K)."""
    count = 0
    for a, s in states:
        for t, u in ((a, s), (s, a)):
            if t % 4 != 3:
                continue
            K = (prime * R + 1) // 4
            if (
                prime != a + s + a * s * R
                or prime % 4 != 1
                or R % 4 != 3
                or u % 2 != 1
                or (t * R + 1) % 2
                or (u * R + 1) % 2
                or ((t * R + 1) // 2) * ((u * R + 1) // 2) != K
                or (t * R + 1) // 2 % R != pow(2, -1, R)
            ):
                raise AssertionError("purported two-residue half-block is invalid")
            count += 1
    return count


def audit_record(
    prime: int, stored: dict[str, object], states: list[tuple[int, int]]
) -> dict[str, int | bool]:
    """Measure the surviving two-mechanism and minimal character-order boundary."""
    R = int(stored["R"])
    K = (prime * R + 1) // 4
    factors = sources.exact_factorization(K)
    certificate = sources.unit_group_subgroup_certificate(factors, R)
    minimal_order = int(
        sources.two_power_character_depth(certificate)[
            "minimal_separating_two_power_character_order"
        ]
    )
    endpoint_count = endpoint_count_with_halfblock_two_injection(prime, R, states)
    two_order = int(sympy.n_order(2, R))
    minus_one_in_two_subgroup = bool(
        two_order % 2 == 0 and pow(2, two_order // 2, R) == R - 1
    )
    if (
        stored["classification"] != "subgroup_character"
        or bool(stored["target_in_generated_subgroup"])
        or bool(certificate["target_in_generated_subgroup"])
        or (endpoint_count > 0 and minus_one_in_two_subgroup)
    ):
        raise AssertionError("subgroup obstacle contradicted its two-residue boundary")
    return {
        "R": R,
        "K": K,
        "source_state_count": int(stored["source_state_count"]),
        "two_injecting_endpoint_count": endpoint_count,
        "two_injecting_state_exists": endpoint_count > 0,
        "two_multiplicative_order": two_order,
        "minus_one_in_two_subgroup": minus_one_in_two_subgroup,
        "minimal_separating_two_power_character_order": minimal_order,
    }


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    """Audit all exact G states of the seven complete pressure spectra."""
    source_records = load_subgroup_records(input_path)
    source_spectra = {
        prime: sources.enumerate_linear_source_states(prime)[1]
        for prime in EXPECTED_PER_PRIME_G_COUNTS
    }
    records_by_prime: dict[int, list[dict[str, int | bool]]] = {
        prime: [] for prime in EXPECTED_PER_PRIME_G_COUNTS
    }
    for prime, stored in source_records:
        R = int(stored["R"])
        records_by_prime[prime].append(
            audit_record(prime, stored, source_spectra[prime][R])
        )

    profiles = []
    for prime, records in records_by_prime.items():
        records.sort(key=lambda record: int(record["R"]))
        if len(records) != EXPECTED_PER_PRIME_G_COUNTS[prime]:
            raise AssertionError("subgroup-character profile lost a frozen record")
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
                "two_injecting_R_count": sum(
                    bool(record["two_injecting_state_exists"]) for record in records
                ),
                "quadratic_separator_R_count": sum(
                    int(record["minimal_separating_two_power_character_order"]) == 2
                    for record in records
                ),
                "higher_order_separator_R_count": sum(
                    int(record["minimal_separating_two_power_character_order"]) > 2
                    for record in records
                ),
                "record_sha256": stable_sha256(digest_rows),
                "records": records,
            }
        )

    all_records = [record for profile in profiles for record in profile["records"]]
    separator_counts = Counter(
        str(record["minimal_separating_two_power_character_order"])
        for record in all_records
    )
    return {
        "arithmetic": (
            "for every frozen subgroup-character state, certify whether a half-block t=3 (mod 4) "
            "injects 2 into the support subgroup, decide whether -1 is a power of 2 modulo R, "
            "and recover the exact minimal separating 2-power character order"
        ),
        "scope_note": (
            "A G-state cannot simultaneously have a half-block two injection and -1 in <2>. This profile "
            "records the surviving cases; it does not compare separators across different R."
        ),
        "input": input_path.name,
        "input_sha256": file_sha256(input_path),
        "subgroup_character_R_count": len(all_records),
        "two_injecting_R_count": sum(
            bool(record["two_injecting_state_exists"]) for record in all_records
        ),
        "minus_one_in_two_subgroup_R_count": sum(
            bool(record["minus_one_in_two_subgroup"]) for record in all_records
        ),
        "quadratic_separator_R_count": sum(
            int(record["minimal_separating_two_power_character_order"]) == 2
            for record in all_records
        ),
        "higher_order_separator_order_counts": {
            order: count
            for order, count in sorted(separator_counts.items(), key=lambda item: int(item[0]))
            if int(order) > 2
        },
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "profiles"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
