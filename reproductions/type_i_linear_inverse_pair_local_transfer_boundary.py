#!/usr/bin/env python3
"""Audit known local source transfers at the two inverse-pair F states."""

from __future__ import annotations

from collections import defaultdict, deque
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
PULLBACK_INPUT = ROOT / "reproductions" / "type-i-linear-f-cross-source-pullback-profile-600m-results.json"
MIXTURE_INPUT = ROOT / "reproductions" / "type-i-linear-general-b-obstruction-mixture-profile-600m-results.json"
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
INVERSE_SCRIPT = ROOT / "reproductions" / "type_i_linear_inverse_pair_log_box_criterion.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-linear-inverse-pair-local-transfer-boundary-results.json"

EXPECTED_PULLBACK_SHA256 = (
    "60a95000d81cdfee41f6b07b54b0f9e088bc56f71772ef296dec49b7c3020d05"
)
EXPECTED_MIXTURE_SHA256 = (
    "dce587d6e6703e5cdcb81b6cd05c16989394a7321d2d14515ea2eda6c2aec44d"
)
EXPECTED_CASES = {
    (64_214_329, 359): (7154, 25),
    (105_295_129, 839): (2, 62_713),
}


def load_module(name: str, path: Path):
    """Load an established enumerator without duplicating its arithmetic."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sources = load_module("inverse_pair_local_sources", SOURCE_SCRIPT)
inverse_pair = load_module("inverse_pair_local_log_box", INVERSE_SCRIPT)


def file_sha256(path: Path) -> str:
    """Return the SHA-256 digest of exact input bytes."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def state_valid(prime: int, state: tuple[int, int, int]) -> None:
    """Check the strict linear-source identities for one state."""
    a, s, R = state
    if (
        a < 1
        or s < 1
        or s % 2 != 1
        or R < 3
        or R % 4 != 3
        or prime != a + s + a * s * R
        or prime - s != a * (s * R + 1)
    ):
        raise AssertionError(f"invalid linear source state {prime}, {state}")
    if (prime * R + 1) % 4:
        raise AssertionError("K is not integral")


def divisors(value: int) -> list[int]:
    """Enumerate all positive divisors using the authoritative factorizer."""
    return sources.divisors_from_factorization(sources.exact_factorization(value))


def fixed_s_transfer(
    prime: int, state: tuple[int, int, int], factor: int
) -> tuple[int, int, int] | None:
    """Apply the known q|a, q=1 (mod s) transfer when its R gate passes."""
    a, s, R = state
    if factor <= 1 or a % factor or (factor - 1) % s:
        return None
    R_next = factor * R + (factor - 1) // s
    if R_next % 4 != 3:
        return None
    target = (a // factor, s, R_next)
    state_valid(prime, target)
    if ((prime * R_next + 1) // 4) % factor:
        raise AssertionError("fixed-s transfer lost q|K' divisibility")
    return target


def shift_transfer(
    prime: int, state: tuple[int, int, int], factor: int
) -> tuple[int, int, int] | None:
    """Apply the known q|s, q=1 (mod a) transfer when its R gate passes."""
    a, s, R = state
    if factor <= 1 or s % factor or (factor - 1) % a:
        return None
    R_next = factor * R + (factor - 1) // a
    if R_next % 4 != 3:
        return None
    target = (a, s // factor, R_next)
    state_valid(prime, target)
    if ((prime * R_next + 1) // 4) % factor:
        raise AssertionError("shift transfer lost q|K' divisibility")
    return target


def complete_states(prime: int) -> set[tuple[int, int, int]]:
    """Recover the complete directed source state set from the frozen enumerator."""
    _, by_R = sources.enumerate_linear_source_states(prime)
    states = {
        (int(a), int(s), int(R))
        for R, pairs in by_R.items()
        for a, s in pairs
    }
    if not states:
        raise AssertionError("source state set is empty")
    for state in states:
        state_valid(prime, state)
    return states


def local_edges(
    prime: int, states: set[tuple[int, int, int]]
) -> dict[tuple[int, int, int], list[dict[str, object]]]:
    """Enumerate all forward fixed-s, shift, and legal coordinate-swap edges."""
    edges: dict[tuple[int, int, int], list[dict[str, object]]] = defaultdict(list)
    for state in sorted(states):
        a, s, R = state
        for factor in divisors(a):
            target = fixed_s_transfer(prime, state, factor)
            if target is None:
                continue
            if target not in states:
                raise AssertionError("complete source enumerator missed a fixed-s transfer")
            edges[state].append(
                {"kind": "fixed_s", "factor": int(factor), "to": list(target)}
            )
        for factor in divisors(s):
            target = shift_transfer(prime, state, factor)
            if target is None:
                continue
            if target not in states:
                raise AssertionError("complete source enumerator missed a shift-s transfer")
            edges[state].append(
                {"kind": "shift_s", "factor": int(factor), "to": list(target)}
            )
        if a % 2 == 1 and s % 2 == 1 and a != s:
            target = (s, a, R)
            if target not in states:
                raise AssertionError("coordinate swap left the complete state set")
            edges[state].append({"kind": "swap", "factor": 1, "to": list(target)})
    for state in edges:
        edges[state].sort(key=lambda row: (str(row["kind"]), int(row["factor"]), row["to"]))
    return edges


def target_hits() -> dict[int, set[int]]:
    """Load the frozen B=1 target-modulus rows used by the source profile."""
    if file_sha256(MIXTURE_INPUT) != EXPECTED_MIXTURE_SHA256:
        raise AssertionError("target profile changed")
    payload = json.loads(MIXTURE_INPUT.read_text(encoding="utf-8"))
    return {
        int(record["prime"]): {int(value) for value in record["hit_R"]}
        for record in payload["profiles"]
    }


def affine_transfer_tests(
    state: tuple[int, int, int]
) -> tuple[list[dict[str, object]], dict[str, int]]:
    """Test every divisor of L=aR+1 against both known source-transfer predicates."""
    a, s, R = state
    L = a * R + 1
    rows = []
    for factor in divisors(L):
        if factor == 1:
            continue
        rows.append(
            {
                "factor": int(factor),
                "divides_a": a % factor == 0,
                "divides_s": s % factor == 0,
                "fixed_s_congruence": (factor - 1) % s == 0,
                "shift_s_congruence": (factor - 1) % a == 0,
                "fixed_s_admissible": a % factor == 0 and (factor - 1) % s == 0,
                "shift_s_admissible": s % factor == 0 and (factor - 1) % a == 0,
            }
        )
    counts = {
        "nontrivial_divisor_count": len(rows),
        "fixed_s_admissible_count": sum(int(row["fixed_s_admissible"]) for row in rows),
        "shift_s_admissible_count": sum(int(row["shift_s_admissible"]) for row in rows),
    }
    return rows, counts


def profile_case(
    candidate: dict[str, int], hits_by_prime: dict[int, set[int]]
) -> dict[str, object]:
    """Profile one inverse-pair F state and its exact local-transfer closure."""
    prime = int(candidate["prime"])
    R = int(candidate["R"])
    root = (int(candidate["a"]), int(candidate["s"]), R)
    if EXPECTED_CASES.get((prime, R)) != root[:2]:
        raise AssertionError(f"unexpected inverse-pair source state {prime}, {R}")
    states = complete_states(prime)
    if root not in states:
        raise AssertionError("inverse-pair source state is missing")
    edges = local_edges(prime, states)
    affine_rows, affine_counts = affine_transfer_tests(root)

    reachable = {root}
    pending = deque([root])
    while pending:
        state = pending.popleft()
        for edge in edges.get(state, []):
            target = tuple(int(value) for value in edge["to"])
            if target not in reachable:
                reachable.add(target)
                pending.append(target)
    hit_R = hits_by_prime[prime]
    hit_reachable = sorted({state[2] for state in reachable if state[2] in hit_R})

    incoming = defaultdict(int)
    edge_count = 0
    closure_edges = []
    for source, rows in edges.items():
        for row in rows:
            edge_count += 1
            target = tuple(int(value) for value in row["to"])
            incoming[target] += 1
            if source in reachable:
                closure_edges.append(
                    {"from": list(source), **row}
                )
    closure_edges.sort(key=lambda row: (row["from"], str(row["kind"]), int(row["factor"]), row["to"]))

    L = root[0] * root[2] + 1
    E = root[1] * root[2] + 1
    if math.gcd(root[0], L) != 1:
        raise AssertionError("gcd(a,aR+1) should be one")
    if affine_counts["fixed_s_admissible_count"] or affine_counts["shift_s_admissible_count"]:
        raise AssertionError("an affine-block divisor unexpectedly satisfies a local transfer")
    return {
        "prime": prime,
        "R": R,
        "root_state": list(root),
        "hit_R": sorted(hit_R),
        "complete_source_state_count": len(states),
        "complete_local_edge_count": edge_count,
        "root_outgoing_edges": edges.get(root, []),
        "root_incoming_edge_count": int(incoming[root]),
        "affine_block_L": L,
        "affine_block_factorization": [
            {"prime": int(prime_factor), "exponent": int(exponent)}
            for prime_factor, exponent in sources.exact_factorization(L)
        ],
        "shift_block_E": E,
        "shift_block_factorization": [
            {"prime": int(prime_factor), "exponent": int(exponent)}
            for prime_factor, exponent in sources.exact_factorization(E)
        ],
        "gcd_a_L": math.gcd(root[0], L),
        "gcd_s_L": math.gcd(root[1], L),
        "affine_divisor_tests": affine_rows,
        "affine_divisor_counts": affine_counts,
        "forward_local_closure_state_count": len(reachable),
        "forward_local_closure_states": [list(state) for state in sorted(reachable)],
        "forward_local_closure_edge_count": len(closure_edges),
        "forward_local_closure_edges": closure_edges,
        "forward_local_closure_hit_R": hit_reachable,
        "forward_local_closure_hit_state_count": sum(
            int(state[2] in hit_R) for state in reachable
        ),
    }


def run_audit() -> dict[str, object]:
    """Run the exact two-case inverse-pair local-transfer audit."""
    if file_sha256(PULLBACK_INPUT) != EXPECTED_PULLBACK_SHA256:
        raise AssertionError("inverse-pair input artifact changed")
    candidates = inverse_pair.inverse_pair_candidates()
    candidate_keys = {(int(row["prime"]), int(row["R"])) for row in candidates}
    if candidate_keys != set(EXPECTED_CASES) or len(candidates) != len(EXPECTED_CASES):
        raise AssertionError("inverse-pair candidate census changed")
    hits = target_hits()
    profiles = [profile_case(candidate, hits) for candidate in candidates]
    if any(profile["forward_local_closure_hit_R"] for profile in profiles):
        raise AssertionError("a local inverse-pair closure unexpectedly reached a target")
    return {
        "arithmetic": (
            "test every divisor of L=aR+1 against the established fixed-s and shift-s transfer "
            "conditions, then exhaust the complete forward source-state closure"
        ),
        "scope_note": (
            "This is an exact finite boundary for the two inverse-pair F directions in the frozen "
            "seven-spectrum profile. It does not refute the mixed selector and does not enumerate "
            "new source constructions outside the audited transfer operations."
        ),
        "input_artifacts": {
            "pullback": PULLBACK_INPUT.name,
            "pullback_sha256": file_sha256(PULLBACK_INPUT),
            "target_profile": MIXTURE_INPUT.name,
            "target_profile_sha256": file_sha256(MIXTURE_INPUT),
        },
        "inverse_pair_candidate_count": len(candidates),
        "profiles": profiles,
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit()
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
