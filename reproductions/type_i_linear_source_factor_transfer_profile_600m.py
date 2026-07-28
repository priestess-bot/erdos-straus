#!/usr/bin/env python3
"""Audit the exact factor-transfer graph in seven complete linear source spectra."""

from __future__ import annotations

import argparse
from collections import Counter
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
SOURCE_SCRIPT = (
    ROOT
    / "reproductions"
    / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-source-factor-transfer-profile-600m-results.json"
)

EXPECTED_INPUT_SHA256 = (
    "dce587d6e6703e5cdcb81b6cd05c16989394a7321d2d14515ea2eda6c2aec44d"
)
EXPECTED_PER_PRIME = {
    214_729: {
        "source_state_count": 43,
        "target_hit_state_count": 4,
        "source_s_count": 20,
        "target_hit_s_count": 4,
        "failed_state_same_s_as_target_hit_count": 6,
        "failed_state_s_isolated_from_target_hit_count": 33,
        "forward_factor_transfer_count": 70,
    },
    878_089: {
        "source_state_count": 54,
        "target_hit_state_count": 1,
        "source_s_count": 32,
        "target_hit_s_count": 1,
        "failed_state_same_s_as_target_hit_count": 0,
        "failed_state_s_isolated_from_target_hit_count": 53,
        "forward_factor_transfer_count": 45,
    },
    2_210_569: {
        "source_state_count": 38,
        "target_hit_state_count": 4,
        "source_s_count": 21,
        "target_hit_s_count": 3,
        "failed_state_same_s_as_target_hit_count": 13,
        "failed_state_s_isolated_from_target_hit_count": 21,
        "forward_factor_transfer_count": 26,
    },
    13_782_409: {
        "source_state_count": 78,
        "target_hit_state_count": 1,
        "source_s_count": 44,
        "target_hit_s_count": 1,
        "failed_state_same_s_as_target_hit_count": 11,
        "failed_state_s_isolated_from_target_hit_count": 66,
        "forward_factor_transfer_count": 90,
    },
    64_214_329: {
        "source_state_count": 80,
        "target_hit_state_count": 5,
        "source_s_count": 50,
        "target_hit_s_count": 5,
        "failed_state_same_s_as_target_hit_count": 8,
        "failed_state_s_isolated_from_target_hit_count": 67,
        "forward_factor_transfer_count": 77,
    },
    105_295_129: {
        "source_state_count": 95,
        "target_hit_state_count": 6,
        "source_s_count": 64,
        "target_hit_s_count": 6,
        "failed_state_same_s_as_target_hit_count": 0,
        "failed_state_s_isolated_from_target_hit_count": 89,
        "forward_factor_transfer_count": 83,
    },
    536_944_489: {
        "source_state_count": 102,
        "target_hit_state_count": 9,
        "source_s_count": 74,
        "target_hit_s_count": 9,
        "failed_state_same_s_as_target_hit_count": 16,
        "failed_state_s_isolated_from_target_hit_count": 77,
        "forward_factor_transfer_count": 72,
    },
}
EXPECTED_TOTALS = {
    "source_state_count": 490,
    "target_hit_state_count": 30,
    "failed_state_count": 460,
    "failed_state_same_s_as_target_hit_count": 54,
    "failed_state_s_isolated_from_target_hit_count": 406,
    "forward_factor_transfer_count": 463,
}


def load_module(name: str, path: Path):
    """Load the authoritative complete linear source enumerator."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sources = load_module("linear_source_factor_transfer_sources", SOURCE_SCRIPT)


def file_sha256(path: Path) -> str:
    """Return the SHA-256 digest of exact input bytes."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def transfer_factor(
    prime: int, state: tuple[int, int, int], factor: int
) -> tuple[int, int, int]:
    """Move one admissible factor from a to E=sR+1, checking every identity."""
    a, s, R = state
    if (
        factor <= 1
        or a % factor
        or (factor - 1) % s
        or prime != a + s + a * s * R
        or s % 2 != 1
        or R < 3
        or R % 4 != 3
    ):
        raise ValueError("factor is not transferable from this linear source state")
    a_next = a // factor
    increment = (factor - 1) // s
    R_next = factor * R + increment
    E = s * R + 1
    E_next = s * R_next + 1
    K = (prime * R + 1) // 4
    K_next = (prime * R_next + 1) // 4
    if (
        a_next < 1
        or R_next <= R
        or R_next % 4 != 3
        or E_next != factor * E
        or prime != a_next + s + a_next * s * R_next
        or prime - s != a_next * E_next
        or 4 * K != prime * R + 1
        or 4 * K_next != prime * R_next + 1
        or K_next % factor
    ):
        raise AssertionError("factor transfer did not preserve its exact identities")
    return (a_next, s, R_next)


def checked_states(prime: int) -> set[tuple[int, int, int]]:
    """Recover every directed source state, with no extra search restriction."""
    _, by_R = sources.enumerate_linear_source_states(prime)
    states = {
        (int(a), int(s), int(R))
        for R, pairs in by_R.items()
        for a, s in pairs
    }
    if not states:
        raise AssertionError("linear source state set is empty")
    return states


def factor_transfers(
    prime: int, states: set[tuple[int, int, int]]
) -> list[dict[str, int | list[int]]]:
    """Exhaust every forward admissible factor transfer in one source spectrum."""
    transitions = []
    for state in sorted(states):
        a, s, _ = state
        for factor in sources.divisors_from_factorization(
            sources.exact_factorization(a)
        ):
            if factor <= 1 or (factor - 1) % s:
                continue
            target = transfer_factor(prime, state, factor)
            if target not in states:
                raise AssertionError("complete source enumerator missed a factor transfer")
            transitions.append(
                {
                    "from": list(state),
                    "factor": int(factor),
                    "to": list(target),
                }
            )
    if len({(tuple(row["from"]), int(row["factor"])) for row in transitions}) != len(
        transitions
    ):
        raise AssertionError("factor transfer enumeration duplicated an edge")
    return transitions


def profile_prime(
    source_profile: dict[str, object],
) -> tuple[dict[str, object], Counter[str]]:
    """Profile transfer invariants and target-hit fibers at one frozen prime."""
    prime = int(source_profile["prime"])
    hit_R = {int(value) for value in source_profile["hit_R"]}
    states = checked_states(prime)
    hit_states = {state for state in states if state[2] in hit_R}
    failed_states = states - hit_states
    hit_s = {state[1] for state in hit_states}
    same_s_failures = {state for state in failed_states if state[1] in hit_s}
    isolated_failures = failed_states - same_s_failures
    transitions = factor_transfers(prime, states)
    counts = {
        "source_state_count": len(states),
        "target_hit_state_count": len(hit_states),
        "source_s_count": len({state[1] for state in states}),
        "target_hit_s_count": len(hit_s),
        "failed_state_same_s_as_target_hit_count": len(same_s_failures),
        "failed_state_s_isolated_from_target_hit_count": len(isolated_failures),
        "forward_factor_transfer_count": len(transitions),
    }
    if counts != EXPECTED_PER_PRIME[prime]:
        raise AssertionError("frozen factor-transfer profile changed")
    if len(failed_states) != (
        counts["failed_state_same_s_as_target_hit_count"]
        + counts["failed_state_s_isolated_from_target_hit_count"]
    ):
        raise AssertionError("failed states did not partition by their s fiber")
    example = min(transitions, key=lambda row: (row["from"], row["factor"], row["to"]))
    isolated_example = min(
        isolated_failures, key=lambda state: (state[1], state[2], state[0])
    )
    return (
        {
            "prime": prime,
            **counts,
            "factor_transfer_example": example,
            "s_isolated_failed_state_example": list(isolated_example),
        },
        Counter(
            {
                "source_state_count": len(states),
                "target_hit_state_count": len(hit_states),
                "failed_state_count": len(failed_states),
                "failed_state_same_s_as_target_hit_count": len(same_s_failures),
                "failed_state_s_isolated_from_target_hit_count": len(isolated_failures),
                "forward_factor_transfer_count": len(transitions),
            }
        ),
    )


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    """Run the exact seven-spectrum factor-transfer audit."""
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
        raise AssertionError("aggregate factor-transfer profile changed")
    return {
        "arithmetic": (
            "for p=a+s+asR and every q>1 with q|a and q=1 (mod s), "
            "verify the exact transfer (a,s,R) -> (a/q,s,qR+(q-1)/s) and "
            "the induced divisibility q|K' at the destination"
        ),
        "scope_note": (
            "The transfer preserves s, so this finite audit can bound only "
            "fixed-s reselection. It neither disproves the existence of a "
            "good source state nor proves a universal selector."
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
