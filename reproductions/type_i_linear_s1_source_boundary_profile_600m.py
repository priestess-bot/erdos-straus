#!/usr/bin/env python3
"""Audit the complete s=1 slice of linear general-B sources on 1,964 points."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
LINEAR_SCRIPT = ROOT / "reproductions" / "type_i_linear_source_general_b_completion_profile_600m.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-linear-s1-source-boundary-profile-600m-results.json"

EXPECTED_TOTALS = {
    "input_prime_count": 1_964,
    "s_eq_1_source_state_count": 31_046,
    "target_R_audits_until_first_hit_or_exhaustion": 5_701,
    "captured_count": 1_827,
    "miss_count": 137,
}
EXPECTED_MISS_PREFIX = [
    214_729,
    297_049,
    878_089,
    1_511_449,
    3_942_409,
    5_478_169,
    6_294_649,
    10_170_169,
]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


linear = load_module("s1_source_linear_completion", LINEAR_SCRIPT)


def enumerate_s_eq_1_sources(prime: int) -> list[tuple[int, int]]:
    """Return every source p=a+1+aR, in increasing (R,a) order."""
    states = []
    for a in linear.divisors_from_factorization(linear.exact_factorization(prime - 1)):
        R = (prime - 1) // a - 1
        if R < 3 or R % 4 != 3:
            continue
        if prime != a + 1 + a * R:
            raise AssertionError("s=1 source divisor recovery failed")
        states.append((R, a))
    canonical = sorted(set(states))
    if len(canonical) != len(states):
        raise AssertionError("distinct s=1 divisors recovered the same source")
    return canonical


def a_eq_1_moduli(prime: int) -> set[int]:
    """Recover the target moduli of the a=1 slice for the symmetry check."""
    return {
        (prime - 1) // s - 1
        for s in linear.divisors_from_factorization(linear.exact_factorization(prime - 1))
        if s % 2 == 1 and (prime - 1) // s - 1 >= 3 and (prime - 1) // s % 4 == 0
    }


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
    """Decide the s=1 family, stopping only after a valid target hit is found."""
    states = enumerate_s_eq_1_sources(prime)
    if not states:
        raise AssertionError("the universal s=1, R=3 state disappeared")
    if not a_eq_1_moduli(prime) <= {R for R, _ in states}:
        raise AssertionError("a=1 target moduli escaped their s=1 symmetric partners")
    local: Counter[str] = Counter()
    for R, a in states:
        local["target_R_audits_until_first_hit_or_exhaustion"] += 1
        audit = linear.audit_target_R(prime, R)
        local["square_divisor_candidate_space"] += int(
            audit["square_divisor_candidate_space"]
        )
        if not bool(audit["target_residue_reachable"]):
            continue
        witness = linear.build_witness(prime, a, 1, R, audit)
        if not all(witness["conditions"].values()):
            raise AssertionError("s=1 witness did not pass the complete replay")
        return (
            {
                "prime": prime,
                "s_eq_1_source_count": len(states),
                "selected_witness": compact_witness(witness),
            },
            local,
        )
    return (
        {
            "prime": prime,
            "s_eq_1_source_count": len(states),
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
    observed = {
        "input_prime_count": len(primes),
        "s_eq_1_source_state_count": sum(
            int(record["s_eq_1_source_count"]) for record in records
        ),
        "target_R_audits_until_first_hit_or_exhaustion": totals[
            "target_R_audits_until_first_hit_or_exhaustion"
        ],
        "captured_count": len(captured),
        "miss_count": len(misses),
    }
    if observed != EXPECTED_TOTALS or misses[: len(EXPECTED_MISS_PREFIX)] != EXPECTED_MISS_PREFIX:
        raise AssertionError("the frozen s=1 boundary profile changed")
    return {
        "arithmetic": (
            "enumerate every divisor a of p-1, set R=(p-1)/a-1, and retain exactly the states "
            "p=a+1+aR with R=3 (mod 4); at each state decide every d|K^2 by balanced MITM until "
            "the first target hit, or exhaust the state list"
        ),
        "scope_note": (
            "This completely decides only the s=1 slice of the linear-source general-B selector on the "
            "frozen 1,964-point pressure set. Its misses can still have a,s>1 linear bridges, non-linear "
            "source-square bridges, or Type II certificates."
        ),
        "input_prime_count": observed["input_prime_count"],
        "s_eq_1_source_state_count": observed["s_eq_1_source_state_count"],
        "target_R_audits_until_first_hit_or_exhaustion": observed[
            "target_R_audits_until_first_hit_or_exhaustion"
        ],
        "square_divisor_candidate_space_until_first_hit_or_exhaustion": totals[
            "square_divisor_candidate_space"
        ],
        "captured_count": observed["captured_count"],
        "miss_count": observed["miss_count"],
        "misses": misses,
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
