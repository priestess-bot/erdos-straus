#!/usr/bin/env python3
"""Profile s-changing linear source factor transfers and their combined closure."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict, deque
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
INPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-general-b-obstruction-mixture-profile-600m-results.json"
)
FIXED_SCRIPT = (
    ROOT / "reproductions" / "type_i_linear_source_factor_transfer_profile_600m.py"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-source-shift-transfer-closure-profile-600m-results.json"
)

EXPECTED_INPUT_SHA256 = (
    "dce587d6e6703e5cdcb81b6cd05c16989394a7321d2d14515ea2eda6c2aec44d"
)
EXPECTED_PER_PRIME = {
    214_729: {
        "source_state_count": 43,
        "target_hit_state_count": 4,
        "raw_shift_factor_candidate_count": 30,
        "admissible_shift_factor_transfer_count": 24,
        "fixed_factor_transfer_count": 70,
        "combined_reachable_target_state_count": 4,
        "failed_state_reaching_target_count": 0,
        "s_isolated_failed_state_reaching_target_count": 0,
    },
    878_089: {
        "source_state_count": 54,
        "target_hit_state_count": 1,
        "raw_shift_factor_candidate_count": 42,
        "admissible_shift_factor_transfer_count": 13,
        "fixed_factor_transfer_count": 45,
        "combined_reachable_target_state_count": 1,
        "failed_state_reaching_target_count": 0,
        "s_isolated_failed_state_reaching_target_count": 0,
    },
    2_210_569: {
        "source_state_count": 38,
        "target_hit_state_count": 4,
        "raw_shift_factor_candidate_count": 16,
        "admissible_shift_factor_transfer_count": 6,
        "fixed_factor_transfer_count": 26,
        "combined_reachable_target_state_count": 9,
        "failed_state_reaching_target_count": 5,
        "s_isolated_failed_state_reaching_target_count": 1,
    },
    13_782_409: {
        "source_state_count": 78,
        "target_hit_state_count": 1,
        "raw_shift_factor_candidate_count": 54,
        "admissible_shift_factor_transfer_count": 31,
        "fixed_factor_transfer_count": 90,
        "combined_reachable_target_state_count": 1,
        "failed_state_reaching_target_count": 0,
        "s_isolated_failed_state_reaching_target_count": 0,
    },
    64_214_329: {
        "source_state_count": 80,
        "target_hit_state_count": 5,
        "raw_shift_factor_candidate_count": 35,
        "admissible_shift_factor_transfer_count": 23,
        "fixed_factor_transfer_count": 77,
        "combined_reachable_target_state_count": 5,
        "failed_state_reaching_target_count": 0,
        "s_isolated_failed_state_reaching_target_count": 0,
    },
    105_295_129: {
        "source_state_count": 95,
        "target_hit_state_count": 6,
        "raw_shift_factor_candidate_count": 255,
        "admissible_shift_factor_transfer_count": 128,
        "fixed_factor_transfer_count": 83,
        "combined_reachable_target_state_count": 6,
        "failed_state_reaching_target_count": 0,
        "s_isolated_failed_state_reaching_target_count": 0,
    },
    536_944_489: {
        "source_state_count": 102,
        "target_hit_state_count": 9,
        "raw_shift_factor_candidate_count": 64,
        "admissible_shift_factor_transfer_count": 31,
        "fixed_factor_transfer_count": 72,
        "combined_reachable_target_state_count": 13,
        "failed_state_reaching_target_count": 4,
        "s_isolated_failed_state_reaching_target_count": 1,
    },
}
EXPECTED_TOTALS = {
    "source_state_count": 490,
    "target_hit_state_count": 30,
    "raw_shift_factor_candidate_count": 496,
    "admissible_shift_factor_transfer_count": 256,
    "fixed_factor_transfer_count": 463,
    "combined_reachable_target_state_count": 39,
    "failed_state_reaching_target_count": 9,
    "s_isolated_failed_state_reaching_target_count": 2,
    "failed_state_not_reaching_target_count": 451,
}


def load_module(name: str, path: Path):
    """Load the established fixed-s transfer implementation and source enumerator."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


fixed = load_module("linear_source_fixed_transfer", FIXED_SCRIPT)
sources = fixed.sources


def file_sha256(path: Path) -> str:
    """Return the SHA-256 digest of exact input bytes."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def shift_transfer(
    prime: int, state: tuple[int, int, int], factor: int
) -> tuple[int, int, int] | None:
    """Move an a-congruent factor from s to aR+1 when R' stays admissible."""
    a, s, R = state
    if (
        factor <= 1
        or s % factor
        or (factor - 1) % a
        or prime != a + s + a * s * R
        or s % 2 != 1
        or R < 3
        or R % 4 != 3
    ):
        raise ValueError("factor is not transferable from the shift coordinate")
    s_next = s // factor
    increment = (factor - 1) // a
    R_next = factor * R + increment
    if R_next % 4 != 3:
        return None
    F = a * R + 1
    F_next = a * R_next + 1
    K_next = (prime * R_next + 1) // 4
    if (
        s_next < 1
        or s_next >= s
        or F_next != factor * F
        or prime != a + s_next + a * s_next * R_next
        or prime - s_next != a * (s_next * R_next + 1)
        or 4 * K_next != prime * R_next + 1
        or K_next % factor
    ):
        raise AssertionError("shift transfer did not preserve its exact identities")
    return (a, s_next, R_next)


def raw_shift_candidates(
    state: tuple[int, int, int]
) -> list[int]:
    """List all algebraic shift-factor candidates before the R mod 4 gate."""
    a, s, _ = state
    return [
        int(factor)
        for factor in sources.divisors_from_factorization(
            sources.exact_factorization(s)
        )
        if factor > 1 and (factor - 1) % a == 0
    ]


def shift_transfers(
    prime: int, states: set[tuple[int, int, int]]
) -> tuple[int, list[tuple[tuple[int, int, int], tuple[int, int, int]]]]:
    """Exhaust all raw candidates and retain exactly the R=3 mod 4 transfers."""
    raw_count = 0
    transitions = []
    for state in sorted(states):
        for factor in raw_shift_candidates(state):
            raw_count += 1
            target = shift_transfer(prime, state, factor)
            if target is None:
                continue
            if target not in states:
                raise AssertionError("complete source enumerator missed a shift transfer")
            transitions.append((state, target))
    if len(set(transitions)) != len(transitions):
        raise AssertionError("shift transfer enumeration duplicated an edge")
    return raw_count, transitions


def reverse_reachable(
    states: set[tuple[int, int, int]],
    target_states: set[tuple[int, int, int]],
    transitions: list[tuple[tuple[int, int, int], tuple[int, int, int]]],
) -> set[tuple[int, int, int]]:
    """Return all states with a directed path to a target state."""
    reverse: dict[tuple[int, int, int], set[tuple[int, int, int]]] = defaultdict(set)
    for source, target in transitions:
        if source not in states or target not in states:
            raise AssertionError("transition left the complete source state set")
        reverse[target].add(source)
    reachable = set(target_states)
    pending = deque(target_states)
    while pending:
        target = pending.popleft()
        for source in reverse[target]:
            if source not in reachable:
                reachable.add(source)
                pending.append(source)
    return reachable


def profile_prime(source_profile: dict[str, object]) -> tuple[dict[str, object], Counter[str]]:
    """Compute the exact combined fixed-s and shift-transfer closure at one prime."""
    prime = int(source_profile["prime"])
    hit_R = {int(value) for value in source_profile["hit_R"]}
    states = fixed.checked_states(prime)
    hit_states = {state for state in states if state[2] in hit_R}
    fixed_transitions = [
        (tuple(row["from"]), tuple(row["to"]))
        for row in fixed.factor_transfers(prime, states)
    ]
    raw_shift_count, shift_transitions = shift_transfers(prime, states)
    reachable = reverse_reachable(
        states, hit_states, [*fixed_transitions, *shift_transitions]
    )
    failed_states = states - hit_states
    hit_s = {state[1] for state in hit_states}
    isolated_failures = {
        state for state in failed_states if state[1] not in hit_s
    }
    counts = {
        "source_state_count": len(states),
        "target_hit_state_count": len(hit_states),
        "raw_shift_factor_candidate_count": raw_shift_count,
        "admissible_shift_factor_transfer_count": len(shift_transitions),
        "fixed_factor_transfer_count": len(fixed_transitions),
        "combined_reachable_target_state_count": len(reachable),
        "failed_state_reaching_target_count": len(reachable - hit_states),
        "s_isolated_failed_state_reaching_target_count": len(
            reachable & isolated_failures
        ),
    }
    if counts != EXPECTED_PER_PRIME[prime]:
        raise AssertionError("frozen combined transfer closure changed")
    direct_to_hit = [
        (source, target)
        for source, target in shift_transitions
        if target in hit_states and source not in hit_states
    ]
    return (
        {
            "prime": prime,
            **counts,
            "failed_state_not_reaching_target_count": len(failed_states - reachable),
            "shift_transfer_to_target_examples": [
                {"from": list(source), "to": list(target)}
                for source, target in sorted(direct_to_hit)
            ],
        },
        Counter(
            {
                "source_state_count": len(states),
                "target_hit_state_count": len(hit_states),
                "raw_shift_factor_candidate_count": raw_shift_count,
                "admissible_shift_factor_transfer_count": len(shift_transitions),
                "fixed_factor_transfer_count": len(fixed_transitions),
                "combined_reachable_target_state_count": len(reachable),
                "failed_state_reaching_target_count": len(reachable - hit_states),
                "s_isolated_failed_state_reaching_target_count": len(
                    reachable & isolated_failures
                ),
                "failed_state_not_reaching_target_count": len(failed_states - reachable),
            }
        ),
    )


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    """Run the exact combined-transfer closure profile on seven frozen spectra."""
    if file_sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen obstruction-mixture input changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    input_profiles = payload.get("profiles")
    if not isinstance(input_profiles, list):
        raise AssertionError("input does not contain source profiles")
    records = []
    totals: Counter[str] = Counter()
    for source_profile in input_profiles:
        record, local_totals = profile_prime(source_profile)
        records.append(record)
        totals.update(local_totals)
    actual_totals = {key: int(totals[key]) for key in EXPECTED_TOTALS}
    if actual_totals != EXPECTED_TOTALS:
        raise AssertionError("aggregate combined transfer closure changed")
    return {
        "arithmetic": (
            "combine every fixed-s transfer q|a, q=1 (mod s), with every "
            "admissible shift transfer q|s, q=1 (mod a), R'=qR+(q-1)/a=3 (mod 4), "
            "then compute reverse reachability from exact target-spectrum hits"
        ),
        "scope_note": (
            "This is a finite profile of two explicit forward local source-state "
            "transfers. It neither disproves a different source selector nor "
            "proves a universal certificate or strict descent."
        ),
        "input_artifact": input_path.name,
        "input_sha256": file_sha256(input_path),
        "totals": actual_totals,
        "profiles": records,
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
