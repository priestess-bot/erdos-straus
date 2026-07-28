#!/usr/bin/env python3
"""Audit quadratic compatibility of shared K-primes across four adversarial spectra."""

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
INPUT = ROOT / "reproductions" / "type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json"
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-linear-cross-state-quadratic-separator-compatibility-profile-600m-results.json"
)
EXPECTED_INPUT_SHA256 = "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f"
ADVERSARIAL_PRIMES = (878_089, 26_034_649, 57_399_241, 283_319_689)
EXPECTED_QUADRATIC_G_COUNTS = {
    878_089: 21,
    26_034_649: 20,
    57_399_241: 29,
    283_319_689: 46,
}


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sources = load_module("cross_state_quadratic_separator_sources", SOURCE_SCRIPT)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stable_sha256(rows: list[tuple[int, ...]]) -> str:
    return hashlib.sha256(
        "\n".join(",".join(str(value) for value in row) for row in rows).encode("ascii")
    ).hexdigest()


def load_adversarial_profiles(input_path: Path = INPUT) -> list[dict[str, object]]:
    """Load the four unique-general-B-hit, full-B=1-failure core spectra."""
    if file_sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the full B>1-spectrum input changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    profiles = payload.get("profiles")
    if not isinstance(profiles, list):
        raise AssertionError("full B>1-spectrum input lacks profiles")
    selected = [
        dict(profile)
        for profile in profiles
        if int(profile["prime"]) in ADVERSARIAL_PRIMES
    ]
    if (
        tuple(int(profile["prime"]) for profile in selected) != ADVERSARIAL_PRIMES
        or any(profile["B_eq_1_hit_R"] for profile in selected)
        or any(int(profile["classification_counts"]["hit"]) != 1 for profile in selected)
    ):
        raise AssertionError("adversarial core selection changed")
    return selected


def quadratic_separator_state(
    stored: dict[str, object]
) -> dict[str, int] | None:
    """Recover one explicit quadratic separator, omitting genuine higher-order cases."""
    R = int(stored["R"])
    K = int(stored["K"])
    certificate = sources.unit_group_subgroup_certificate(
        sources.exact_factorization(K), R
    )
    depth = sources.two_power_character_depth(certificate)
    if int(depth["minimal_separating_two_power_character_order"]) != 2:
        return None
    support = sources.quadratic_character_local_support(certificate)
    conductor = int(support["minimal_quadratic_conductor"])
    if conductor % 4 != 3:
        raise AssertionError("quadratic separator is not odd at minus one")
    return {"R": R, "K": K, "conductor": conductor}


def audit_prime(profile: dict[str, object]) -> dict[str, object]:
    """Check every shared odd K-prime between quadratic G states of one core prime."""
    prime = int(profile["prime"])
    states = [
        quadratic_separator_state(record)
        for record in profile["records"]
        if record["classification"] == "subgroup_character"
    ]
    quadratic_states = [state for state in states if state is not None]
    if len(quadratic_states) != EXPECTED_QUADRATIC_G_COUNTS[prime]:
        raise AssertionError("quadratic G-state count changed")
    relations: list[dict[str, int]] = []
    for index, left in enumerate(quadratic_states):
        for right in quadratic_states[index + 1 :]:
            R, K, m = left["R"], left["K"], left["conductor"]
            U, L, n = right["R"], right["K"], right["conductor"]
            modulus_difference, remainder = divmod(abs(R - U), 4)
            if remainder:
                raise AssertionError("two source moduli did not have a fourfold difference")
            shared = math.gcd(K, L)
            if shared != math.gcd(K, modulus_difference):
                raise AssertionError("cross-modulus gcd rigidity failed")
            for q, _ in sources.exact_factorization(shared):
                if q == 2:
                    continue
                if (
                    modulus_difference % q
                    or math.gcd(q, m * n) != 1
                    or int(sympy.jacobi_symbol(m * n, q)) != 1
                ):
                    raise AssertionError("shared quadratic-separator compatibility failed")
                relations.append(
                    {
                        "left_R": R,
                        "right_R": U,
                        "shared_odd_prime": q,
                        "left_conductor": m,
                        "right_conductor": n,
                    }
                )
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
        "quadratic_subgroup_character_R_count": len(quadratic_states),
        "higher_order_subgroup_character_R_count": len(states) - len(quadratic_states),
        "shared_odd_prime_relation_count": len(relations),
        "distinct_R_pair_with_shared_odd_prime_count": len(
            {(row["left_R"], row["right_R"]) for row in relations}
        ),
        "relation_sha256": stable_sha256(digest_rows),
        "relations": relations,
    }


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    """Audit the exact compatibility law on the four adversarial core spectra."""
    profiles = [audit_prime(profile) for profile in load_adversarial_profiles(input_path)]
    return {
        "arithmetic": (
            "when two quadratic G-state K-values share an odd prime q, recover their explicit "
            "minimal quadratic conductors m,m'; verify q divides the corresponding source-modulus "
            "difference and (mm'/q)=1"
        ),
        "scope_note": (
            "This is a local compatibility condition for shared primes of quadratic G states. It does not "
            "force a target hit and deliberately excludes higher-order-only G states."
        ),
        "input": input_path.name,
        "input_sha256": file_sha256(input_path),
        "primes": list(ADVERSARIAL_PRIMES),
        "quadratic_subgroup_character_R_count": sum(
            int(profile["quadratic_subgroup_character_R_count"]) for profile in profiles
        ),
        "higher_order_subgroup_character_R_count": sum(
            int(profile["higher_order_subgroup_character_R_count"]) for profile in profiles
        ),
        "shared_odd_prime_relation_count": sum(
            int(profile["shared_odd_prime_relation_count"]) for profile in profiles
        ),
        "distinct_R_pair_with_shared_odd_prime_count": sum(
            int(profile["distinct_R_pair_with_shared_odd_prime_count"])
            for profile in profiles
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
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "profiles"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
