#!/usr/bin/env python3
"""Audit the complete a=1 slice of linear general-B sources on 1,964 points."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
LINEAR_SCRIPT = ROOT / "reproductions" / "type_i_linear_source_general_b_completion_profile_600m.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-linear-a1-source-boundary-profile-600m-results.json"

EXPECTED_TOTALS = {
    "input_prime_count": 1_964,
    "a_eq_1_source_state_count": 15_012,
    "target_R_audits_until_first_hit_or_exhaustion": 5_548,
    "captured_count": 1_463,
    "miss_count": 501,
}
EXPECTED_MISS_PREFIX = [
    214_729,
    297_049,
    629_689,
    878_089,
    1_447_609,
    1_511_449,
    2_754_889,
    3_942_409,
]
EXPECTED_SELECTED_R_COUNTS = {
    7: 911,
    23: 368,
    15: 51,
    47: 30,
    71: 15,
}


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


linear = load_module("a1_source_linear_completion", LINEAR_SCRIPT)


def enumerate_a_eq_1_sources(prime: int) -> list[tuple[int, int]]:
    """Return every linear source p=1+s+sR, in increasing (R,s) order."""
    states = []
    for s in linear.divisors_from_factorization(linear.exact_factorization(prime - 1)):
        if s % 2 != 1:
            continue
        R = (prime - 1) // s - 1
        if R < 3 or R % 4 != 3:
            continue
        if prime != 1 + s + s * R:
            raise AssertionError("a=1 source divisor recovery failed")
        states.append((R, s))
    canonical = sorted(set(states))
    if len(canonical) != len(states):
        raise AssertionError("distinct a=1 divisors recovered the same source")
    return canonical


def compact_witness(witness: dict[str, object]) -> dict[str, object]:
    """Store the replay-relevant certificate, not its bulky search internals."""
    fields = (
        "a",
        "s",
        "R",
        "E",
        "source_denominator",
        "K",
        "matched_square_divisor",
        "A",
        "B",
        "C",
        "H",
        "gap",
        "target_solution",
        "source_solution",
    )
    return {field: witness[field] for field in fields}


def audit_prime(prime: int) -> tuple[dict[str, object], Counter[str]]:
    """Decide the a=1 family, stopping only after a valid target hit is found."""
    states = enumerate_a_eq_1_sources(prime)
    if not states:
        raise AssertionError("the universal a=1, s=(p-1)/8 state disappeared")
    local: Counter[str] = Counter()
    for R, s in states:
        local["target_R_audits_until_first_hit_or_exhaustion"] += 1
        audit = linear.audit_target_R(prime, R)
        local["square_divisor_candidate_space"] += int(
            audit["square_divisor_candidate_space"]
        )
        if not bool(audit["target_residue_reachable"]):
            continue
        witness = linear.build_witness(prime, 1, s, R, audit)
        if not all(witness["conditions"].values()):
            raise AssertionError("a=1 witness did not pass the complete replay")
        return (
            {
                "prime": prime,
                "a_eq_1_source_count": len(states),
                "selected_witness": compact_witness(witness),
            },
            local,
        )
    return (
        {
            "prime": prime,
            "a_eq_1_source_count": len(states),
            "selected_witness": None,
        },
        local,
    )


def run_audit() -> dict[str, object]:
    _, _, first_primes, second_primes = linear.load_authoritative_primes()
    primes = [*first_primes, *second_primes]
    records = []
    totals: Counter[str] = Counter()
    for prime in primes:
        record, local = audit_prime(prime)
        records.append(record)
        totals.update(local)
    captured = [record for record in records if record["selected_witness"] is not None]
    misses = [int(record["prime"]) for record in records if record["selected_witness"] is None]
    selected_R_counts = Counter(
        int(record["selected_witness"]["R"])
        for record in captured
        if isinstance(record["selected_witness"], dict)
    )
    observed = {
        "input_prime_count": len(primes),
        "a_eq_1_source_state_count": sum(
            int(record["a_eq_1_source_count"]) for record in records
        ),
        "target_R_audits_until_first_hit_or_exhaustion": totals[
            "target_R_audits_until_first_hit_or_exhaustion"
        ],
        "captured_count": len(captured),
        "miss_count": len(misses),
    }
    if observed != EXPECTED_TOTALS or misses[: len(EXPECTED_MISS_PREFIX)] != EXPECTED_MISS_PREFIX:
        raise AssertionError("the frozen a=1 boundary profile changed")
    for R, expected_count in EXPECTED_SELECTED_R_COUNTS.items():
        if selected_R_counts[R] != expected_count:
            raise AssertionError("the dominant selected a=1 target ray changed")
    return {
        "arithmetic": (
            "enumerate every odd divisor s of p-1, set R=(p-1)/s-1, and retain exactly the states "
            "p=1+s+sR with R=3 (mod 4); at each state decide every d|K^2 by balanced MITM until "
            "the first target hit, or exhaust the state list"
        ),
        "scope_note": (
            "This completely decides only the a=1 slice of the linear-source general-B selector on the "
            "frozen 1,964-point pressure set. Its misses can still have a>1 linear bridges, non-linear "
            "source-square bridges, or Type II certificates."
        ),
        "input_prime_count": observed["input_prime_count"],
        "a_eq_1_source_state_count": observed["a_eq_1_source_state_count"],
        "target_R_audits_until_first_hit_or_exhaustion": observed[
            "target_R_audits_until_first_hit_or_exhaustion"
        ],
        "square_divisor_candidate_space_until_first_hit_or_exhaustion": totals[
            "square_divisor_candidate_space"
        ],
        "captured_count": observed["captured_count"],
        "miss_count": observed["miss_count"],
        "misses": misses,
        "dominant_selected_R_counts": {
            str(R): int(selected_R_counts[R])
            for R in sorted(EXPECTED_SELECTED_R_COUNTS)
        },
        "captured_records": captured,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                key: value
                for key, value in payload.items()
                if key not in {"captured_records", "misses"}
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
