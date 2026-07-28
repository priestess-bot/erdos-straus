#!/usr/bin/env python3
"""Extend the quadratic G-state compatibility audit to seven single-hit points.

The input is the complete-spectrum artifact on the stratified B>1 pressure
layer.  This module selects the seven primes having exactly one target-spectrum
hit, recovers the minimal quadratic separator for every quadratic G state, and
checks the cross-modulus shared-prime compatibility law.  Higher-order-only G
states are recorded separately rather than forced into the quadratic argument.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-full-spectrum-bgt1-200-results.json"
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-linear-single-hit-quadratic-compatibility-7-results.json"
)
EXPECTED_INPUT_SHA256 = "5f60c11b255aac289b45d2a4721b233534b7bc29476b76bb5f41efc0917a0196"
SINGLE_HIT_PRIMES = (
    67_369,
    878_089,
    13_782_409,
    26_034_649,
    57_399_241,
    152_498_329,
    283_319_689,
)


def load_module(name: str, path: Path):
    """Load a repository arithmetic module under an isolated name."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sources = load_module("single_hit_quadratic_sources", SOURCE_SCRIPT)


def file_sha256(path: Path) -> str:
    """Hash the complete-spectrum input before selecting records."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stable_sha256(rows: list[tuple[int, ...]]) -> str:
    """Hash integer rows in a deterministic order."""
    data = "\n".join(",".join(str(value) for value in row) for row in rows)
    return hashlib.sha256(data.encode("ascii")).hexdigest()


def load_single_hit_profiles(input_path: Path = INPUT) -> list[dict[str, object]]:
    """Load exactly the seven complete spectra with one target hit."""
    if file_sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the complete-spectrum input artifact changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    profiles = payload.get("records")
    if not isinstance(profiles, list):
        raise AssertionError("complete-spectrum input lacks records")
    selected = [
        dict(profile)
        for profile in profiles
        if int(profile["classification_counts"]["hit"]) == 1
    ]
    if tuple(int(profile["prime"]) for profile in selected) != SINGLE_HIT_PRIMES:
        raise AssertionError("the seven single-hit pressure points changed")
    return selected


def quadratic_separator(
    prime: int, stored: dict[str, object]
) -> dict[str, int] | None:
    """Recover a minimal quadratic separator, omitting higher-order G states."""
    R = int(stored["R"])
    K = (prime * R + 1) // 4
    certificate = sources.unit_group_subgroup_certificate(
        sources.exact_factorization(K), R
    )
    if bool(certificate["target_in_generated_subgroup"]):
        raise AssertionError("a stored G state contains -1 in its support subgroup")
    depth = sources.two_power_character_depth(certificate)
    if int(depth["minimal_separating_two_power_character_order"]) != 2:
        return None
    support = sources.quadratic_character_local_support(certificate)
    conductor = int(support["minimal_quadratic_conductor"])
    if conductor <= 1 or conductor % 4 != 3 or R % conductor:
        raise AssertionError("quadratic separator is not a valid odd conductor divisor")
    return {"R": R, "K": K, "conductor": conductor}


def audit_prime(profile: dict[str, object]) -> dict[str, object]:
    """Check all shared odd K-primes between quadratic G states."""
    prime = int(profile["prime"])
    states: list[dict[str, int]] = []
    higher_order_count = 0
    for stored in profile["records"]:
        if stored["classification"] != "subgroup_character":
            continue
        state = quadratic_separator(prime, stored)
        if state is None:
            higher_order_count += 1
        else:
            states.append(state)
    states.sort(key=lambda state: state["R"])
    relations: list[dict[str, int]] = []
    pair_with_shared_odd_prime = 0
    all_pairs = len(states) * (len(states) - 1) // 2
    for index, left in enumerate(states):
        for right in states[index + 1 :]:
            R, K, m = left["R"], left["K"], left["conductor"]
            U, L, n = right["R"], right["K"], right["conductor"]
            difference, remainder = divmod(abs(R - U), 4)
            if remainder or difference <= 0:
                raise AssertionError("distinct source moduli did not have a fourfold difference")
            shared = math.gcd(K, L)
            odd_relations = 0
            for q, _ in sources.exact_factorization(shared):
                if q == 2:
                    continue
                odd_relations += 1
                if (
                    difference % q
                    or math.gcd(q, m * n) != 1
                    or int(sympy.jacobi_symbol(m * n, q)) != 1
                ):
                    raise AssertionError("quadratic shared-prime compatibility failed")
                relations.append(
                    {
                        "left_R": R,
                        "right_R": U,
                        "shared_odd_prime": q,
                        "left_conductor": m,
                        "right_conductor": n,
                    }
                )
            if odd_relations:
                pair_with_shared_odd_prime += 1
    digest_rows = [
        (
            row["left_R"],
            row["right_R"],
            row["shared_odd_prime"],
            row["left_conductor"],
            row["right_conductor"],
        )
        for row in relations
    ]
    return {
        "prime": prime,
        "quadratic_subgroup_character_R_count": len(states),
        "higher_order_subgroup_character_R_count": higher_order_count,
        "quadratic_state_pair_count": all_pairs,
        "pair_with_shared_odd_prime_count": pair_with_shared_odd_prime,
        "shared_odd_prime_relation_count": len(relations),
        "relation_sha256": stable_sha256(digest_rows),
        "relations": relations,
    }


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    """Run the seven-point cross-state compatibility audit."""
    profiles = [audit_prime(profile) for profile in load_single_hit_profiles(input_path)]
    return {
        "arithmetic": (
            "select the seven complete linear spectra with exactly one target hit; for every quadratic "
            "G state recover its minimal odd conductor m, then for every pair factor gcd(K_R,K_R') "
            "and verify q divides |R-R'|/4 and (m*m'/q)=1 for every shared odd q"
        ),
        "scope_note": (
            "This is a finite compatibility audit, not a proof that quadratic G states are globally "
            "incompatible. Higher-order-only G states are reported separately, and F states are outside "
            "the quadratic law."
        ),
        "input": input_path.name,
        "input_sha256": file_sha256(input_path),
        "primes": list(SINGLE_HIT_PRIMES),
        "quadratic_subgroup_character_R_count": sum(
            int(profile["quadratic_subgroup_character_R_count"]) for profile in profiles
        ),
        "higher_order_subgroup_character_R_count": sum(
            int(profile["higher_order_subgroup_character_R_count"]) for profile in profiles
        ),
        "shared_odd_prime_relation_count": sum(
            int(profile["shared_odd_prime_relation_count"]) for profile in profiles
        ),
        "pair_with_shared_odd_prime_count": sum(
            int(profile["pair_with_shared_odd_prime_count"]) for profile in profiles
        ),
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
            {key: value for key, value in payload.items() if key != "profiles"},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
