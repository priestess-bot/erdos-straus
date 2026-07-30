#!/usr/bin/env python3
"""Audit paired active-prime carrier capacity on the frozen 45-state profile."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json"
SOURCE = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-linear-multi-active-pair-divisor-capacity-results.json"
EXPECTED_INPUT_SHA256 = "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f"
ADVERSARIAL_PRIMES = (878_089, 26_034_649, 57_399_241, 283_319_689)
EXPECTED_TOTALS = {"state_count": 45, "pair_group_count": 40, "demand": 45, "capacity": 70}
EXPECTED_JOINT_HEIGHT_TOTALS = {
    "demand": 99,
    "capacity": 136,
    "by_prime": {
        "878089": {"demand": 4, "capacity": 4},
        "26034649": {"demand": 14, "capacity": 14},
        "57399241": {"demand": 56, "capacity": 93},
        "283319689": {"demand": 25, "capacity": 25},
    },
}


def load_source():
    spec = importlib.util.spec_from_file_location("linear_source", SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOURCE.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


source = load_source()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def recover_state(prime: int, R: int, K: int) -> tuple[int, int, list[int]]:
    candidates = []
    for s in range(1, (prime - 1) // (R + 1) + 1, 2):
        denominator = 1 + s * R
        numerator = prime - s
        if numerator > 0 and numerator % denominator == 0:
            a = numerator // denominator
            if a > 0:
                candidates.append((a, s))
    if not candidates:
        raise AssertionError(f"could not recover linear state ({prime}, {R})")
    a, s = max(candidates)
    factors = source.exact_factorization(K)
    divisor_residues = {
        divisor % R
        for divisor in source.divisors_from_factorization(factors)
    }
    active = [
        int(q)
        for q, _ in factors
        if {q * residue % R for residue in divisor_residues} != divisor_residues
    ]
    return a, s, active


def load_rows(path: Path) -> list[tuple[int, int, int, int, int, list[int]]]:
    if sha256(path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen full-spectrum input changed")
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = []
    for profile in payload["profiles"]:
        prime = int(profile["prime"])
        if prime not in ADVERSARIAL_PRIMES:
            continue
        for record in profile["records"]:
            if record["classification"] != "finite_exponent":
                continue
            R = int(record["R"])
            K = int(record["K"])
            a, s, active = recover_state(prime, R, K)
            if len(active) < 3:
                raise AssertionError(
                    "a frozen adversarial state has fewer than three "
                    "available stabilizer directions"
                )
            rows.append((prime, R, a, s, K, active))
    if len(rows) != EXPECTED_TOTALS["state_count"]:
        raise AssertionError(f"unexpected frozen state count: {len(rows)}")
    return rows


def divisors(value: int) -> list[int]:
    return [int(d) for d in sympy.divisors(value)]


def pair_capacity(prime: int, t: int, q1: int, q2: int, lo: int, hi: int) -> int:
    product = q1 * q2
    if (prime - t) % product:
        return 0
    count = 0
    for d in divisors((prime - t) // product):
        if (product * d - 1) % t:
            continue
        R = (product * d - 1) // t
        if lo <= R <= hi:
            count += 1
    return count


def valuation_limit(value: int, prime: int) -> int:
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def joint_height_capacity(
    prime: int, t: int, q1: int, q2: int, lo: int, hi: int
) -> int:
    total = 0
    for k in range(1, valuation_limit(prime - t, q1) + 1):
        if (prime - t) % q1**k:
            continue
        for ell in range(1, valuation_limit(prime - t, q2) + 1):
            product = q1**k * q2**ell
            if (prime - t) % product:
                continue
            for d1 in divisors((prime - t) // q1**k):
                if (q1**k * d1 - 1) % t:
                    continue
                R = (q1**k * d1 - 1) // t
                if lo <= R <= hi and (t * R + 1) % q2**ell == 0:
                    total += 1
    return total


def run(path: Path) -> dict[str, object]:
    rows = load_rows(path)
    groups: dict[tuple[int, int, int, int], list[tuple[int, int, int]]] = {}
    selected = []
    for prime, R, a, s, K, active in rows:
        pair = None
        chosen_t = None
        for t in (s, a):
            carriers = sorted(q for q in active if (t * R + 1) % q == 0)
            if len(carriers) >= 2:
                chosen_t = t
                pair = (carriers[0], carriers[1])
                break
        if pair is None or chosen_t is None:
            raise AssertionError(f"no paired carrier for ({prime}, {R})")
        key = (prime, chosen_t, pair[0], pair[1])
        heights = []
        block = chosen_t * R + 1
        for q in pair:
            height = 0
            while block % q == 0:
                block //= q
                height += 1
            heights.append(height)
        groups.setdefault(key, []).append((R, heights[0], heights[1]))
        selected.append(
            {
                "prime": prime,
                "R": R,
                "t": chosen_t,
                "pair": list(pair),
                "heights": heights,
            }
        )

    capacities = {}
    joint_height_demand = 0
    joint_height_capacity_total = 0
    joint_by_prime = {}
    for key, values in groups.items():
        prime, t, q1, q2 = key
        lo = min(value[0] for value in values)
        hi = max(value[0] for value in values)
        joint_height_demand += sum(value[1] * value[2] for value in values)
        joint_height_capacity_for_group = (
            joint_height_capacity(prime, t, q1, q2, lo, hi)
        )
        joint_height_capacity_total += joint_height_capacity_for_group
        capacities["%d:%d:%d:%d" % key] = {
            "demand": len(values),
            "capacity": pair_capacity(prime, t, q1, q2, lo, hi),
            "joint_height_demand": sum(value[1] * value[2] for value in values),
            "joint_height_capacity": joint_height_capacity_for_group,
            "R_min": lo,
            "R_max": hi,
        }

    demand = len(selected)
    capacity = sum(int(item["capacity"]) for item in capacities.values())
    by_prime = {}
    for prime in ADVERSARIAL_PRIMES:
        by_prime[str(prime)] = {
            "demand": sum(item["demand"] for key, item in capacities.items() if key.startswith(f"{prime}:")),
            "capacity": sum(item["capacity"] for key, item in capacities.items() if key.startswith(f"{prime}:")),
        }
    totals = {
        "state_count": len(rows),
        "pair_group_count": len(groups),
        "demand": demand,
        "capacity": capacity,
    }
    if totals != EXPECTED_TOTALS:
        raise AssertionError(f"frozen pair-capacity totals changed: {totals}")
    for prime in ADVERSARIAL_PRIMES:
        joint_by_prime[str(prime)] = {
            "demand": sum(
                int(item["joint_height_demand"])
                for key, item in capacities.items()
                if key.startswith(f"{prime}:")
            ),
            "capacity": sum(
                int(item["joint_height_capacity"])
                for key, item in capacities.items()
                if key.startswith(f"{prime}:")
            ),
        }
    joint_totals = {
        "demand": joint_height_demand,
        "capacity": joint_height_capacity_total,
        "by_prime": joint_by_prime,
    }
    if joint_totals != EXPECTED_JOINT_HEIGHT_TOTALS:
        raise AssertionError(f"frozen joint-height totals changed: {joint_totals}")
    return {
        "arithmetic": "For every frozen F state with at least three available stabilizer directions, choose the first block carrying two such primes; count exact divisor-residue windows for the resulting prime pair.",
        "scope_note": "Finite audit only. The paired carrier lemma is general for a selected direction set, but the stabilizer-direction profile does not prove that a chosen Fourier character has the same support; the 45-state capacity total is not universal.",
        "input": path.name,
        "input_sha256": sha256(path),
        "totals": totals,
        "joint_height_totals": joint_totals,
        "by_prime": by_prime,
        "groups": capacities,
        "selected": selected,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run(args.input)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "totals": payload["totals"],
                "joint_height_totals": payload["joint_height_totals"],
                "by_prime": payload["by_prime"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
