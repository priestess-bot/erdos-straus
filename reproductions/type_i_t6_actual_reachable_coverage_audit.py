#!/usr/bin/env python3
"""Audit the current T6 reachable surface without inventing new edges.

This is deliberately a coverage audit, not a T6 totality verifier.  It checks
three narrow facts that are easy to blur in prose:

* every *named current* persistent edge family preserves the ordinary
  ``Sol(p)`` marking; the generic marked contract is not an edge generator;
* the named atomic transition surface is exactly the two T2-v1 arms; and
* the first c=8/q*=103 arithmetic residual allowed by the frozen necessary
  predicates is terminal-preempted, so it is not an actual dead-end fixture.

The remaining c=8 gap is quantified: produce a terminal or a strict receipt
for every terminal-first-surviving parent.  A finite control cannot prove it.
"""

from __future__ import annotations

import argparse
import json
import math
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TAXONOMY = ROOT / "data" / "t5-full-transition-taxonomy-v2.json"


# Every concrete family below either states W_S=W_T=Sol(p) explicitly or
# invokes a receipt whose E4 is that identity lift.  The final generic row is
# only an admission class in the state contract and has no construction.
ORDINARY_EDGE_E4_ANCHORS: dict[str, tuple[str, ...]] = {
    "type-II-relation-reach-proper-endpoint-descent": ("Sol(p)", "恒等"),
    "type-II-relation-reach-gcd-shadow-endpoint-descent": ("Sol(p)", "恒等"),
    "type-II-q-one-full-carrier-phase-root-entry": ("Sol(p)", "恒等"),
    "type-II-positive-q-G-full-carrier-phase-root-entry": ("Sol(p)", "恒等映射"),
    "type-II-q-one-c3-source-lineage-phase-root-entry": ("Sol(p)", "恒等"),
    "type-I-overflow-unbounded-same-chart-promotion-persistence-boundary": (
        "Sol}(4,p)",
        "恒等",
    ),
    "type-I-overflow-outer-rank-reset": ("Sol}(p)", "恒等"),
    "type-I-overflow-a-one-dual-outer-rank-reset": ("Sol}(p)", "恒等"),
    "type-I-overflow-high-carrier-fixed-n-R-descent": ("Sol}(p)", "恒等"),
    "type-I-high-support-rank-aware-sink-bundle-selector": (
        "恒等解提升",
        "path-anchored complete-excess receipt",
    ),
    "type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay": (
        "Sol}(p)",
        "恒等",
    ),
    "type-II-q-one-c-two-19-phase-three-anchor-persistent-macro": (
        "Sol}(p)",
        "identity",
    ),
    "type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-atomic-macro-checkpoint-contraction": (
        "Sol}(p)",
        "Phi_{T\\to P}(u)=u",
    ),
    "type-I-q-one-full-carrier-d-one-c-eight-double-low-parent-anchored-atomic-macro": (
        "Sol}(p)",
        "恒等 lift",
    ),
}

# "Concrete" here means that the referenced claim gives a deterministic
# target/receipt once its written guard is supplied.  It does *not* mean that
# the guard holds for every reachable state.  Keeping this distinction in the
# machine output prevents a guarded constructor from being counted as a T6
# totality row.
EDGE_GENERATOR_CLASS: dict[str, str] = {
    "type-II-relation-reach-proper-endpoint-descent": "guarded_constructor",
    "type-II-relation-reach-gcd-shadow-endpoint-descent": "total_on_declared_q_gt_one_source",
    "type-II-q-one-full-carrier-phase-root-entry": "total_on_declared_ordinary_q_one_G_source",
    "type-II-positive-q-G-full-carrier-phase-root-entry": "total_on_declared_actual_ordinary_positive_q_G_source",
    "type-II-q-one-c3-source-lineage-phase-root-entry": "guarded_constructor",
    "type-I-overflow-unbounded-same-chart-promotion-persistence-boundary": "total_on_declared_persistent_overflow_source",
    "type-I-overflow-outer-rank-reset": "guarded_constructor",
    "type-I-overflow-a-one-dual-outer-rank-reset": "total_on_declared_A_one_overflow_source",
    "type-I-overflow-high-carrier-fixed-n-R-descent": "guarded_constructor",
    "type-I-high-support-rank-aware-sink-bundle-selector": "guarded_constructor",
    "type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay": "total_on_declared_immediate_receiver",
    "type-II-q-one-c-two-19-phase-three-anchor-persistent-macro": "guarded_constructor",
    "type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-atomic-macro-checkpoint-contraction": "guarded_constructor",
    "type-I-q-one-full-carrier-d-one-c-eight-double-low-parent-anchored-atomic-macro": "guarded_constructor",
}

GENERIC_MARKED_CONTRACT = "denominator-escape-state-contract"
ATOMIC_FAMILY_REFERENCES = {
    "type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-atomic-macro-checkpoint-contraction",
    "type-I-q-one-full-carrier-d-one-c-eight-double-low-parent-anchored-atomic-macro",
}
ATOMIC_V1_ARMS = {
    "h4_a1_clean_q_atomic_v1",
    "c8_double_low_parent_atomic_v1",
}


def claim_path(claim_id: str) -> Path:
    path = ROOT / "claims" / f"{claim_id}.md"
    if not path.is_file():
        raise AssertionError(f"missing claim for current edge family: {claim_id}")
    return path


def claim_header(text: str) -> dict[str, str]:
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise AssertionError("claim lost its YAML-like header")
    header = text.split("\n---\n", 1)[0][4:]
    result: dict[str, str] = {}
    for key in ("kind", "claim_id", "claim_status", "proof_provenance", "review_status"):
        match = re.search(rf"^{key}:\s*([^\n]+)$", header, flags=re.MULTILINE)
        if match:
            result[key] = match.group(1).strip(" '\"")
    return result


def audit_current_edge_marks() -> list[dict[str, str]]:
    taxonomy = json.loads(TAXONOMY.read_text())
    rows = taxonomy["current_verified_edge_families"]
    references = {row["reference"] for row in rows}
    expected = set(ORDINARY_EDGE_E4_ANCHORS) | {GENERIC_MARKED_CONTRACT}
    if references != expected:
        raise AssertionError(
            "current edge taxonomy changed; mark-closure audit must be updated: "
            f"missing={sorted(expected - references)}, extra={sorted(references - expected)}"
        )

    audited: list[dict[str, str]] = []
    for row in rows:
        reference = row["reference"]
        if reference == GENERIC_MARKED_CONTRACT:
            audited.append(
                {
                    "family": row["family"],
                    "reference": reference,
                    "generator_class": "contract_schema_not_a_generator",
                    "mark_policy": "contract_only_no_concrete_edge_generator",
                }
            )
            continue
        text = claim_path(reference).read_text()
        header = claim_header(text)
        if header.get("kind") != "claim" or header.get("claim_id") != reference:
            raise AssertionError(f"{reference} is not a content-addressed claim card")
        if header.get("claim_status") not in {"established", "computationally_reproduced"}:
            raise AssertionError(f"{reference} is not an accepted guarded constructor")
        for anchor in ORDINARY_EDGE_E4_ANCHORS[reference]:
            if anchor not in text:
                raise AssertionError(f"{reference} lost E4 audit anchor {anchor!r}")
        audited.append(
            {
                "family": row["family"],
                "reference": reference,
                "generator_class": EDGE_GENERATOR_CLASS[reference],
                "mark_policy": "ordinary_Sol(p)_identity",
            }
        )
    return audited


def audit_atomic_surface() -> dict[str, object]:
    taxonomy = json.loads(TAXONOMY.read_text())
    named = {
        row["reference"]
        for row in taxonomy["current_verified_edge_families"]
        if row["family"].startswith("T2 ")
    }
    if named != ATOMIC_FAMILY_REFERENCES:
        raise AssertionError("named current atomic family surface changed")

    contract = (
        ROOT / "reproductions" / "type_i_atomic_admission_v1_contract.py"
    ).read_text()
    match = re.search(r"^ARMS\s*=\s*\{([^}]*)\}", contract, flags=re.MULTILINE)
    if match is None:
        raise AssertionError("cannot locate the T2-v1 arm registry")
    arms = set(re.findall(r'"([^"]+)"', match.group(1)))
    if arms != ATOMIC_V1_ARMS:
        raise AssertionError("T2-v1 arm registry changed")

    nonrecursive = set(taxonomy["nonrecursive_surfaces"])
    for required in ("raw macro checkpoint", "standalone atomic stutter"):
        if required not in nonrecursive:
            raise AssertionError(f"atomic nonrecursive boundary disappeared: {required}")

    return {
        "named_atomic_family_references": sorted(named),
        "t2_v1_arms": sorted(arms),
        "generic_raw_schema_is_a_named_edge_family": False,
    }


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, math.isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def factorint(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def primes_below(limit: int) -> list[int]:
    return [value for value in range(2, limit) if is_prime(value)]


SMALL_EXCESS_PRIMES = tuple(prime for prime in primes_below(103) if prime >= 7)


def exact_qstar_103_rough(s: int) -> bool:
    value = 6 * s - 1
    return bool(
        value % 103 == 0
        and value % 25 != 0
        and all(value % prime for prime in SMALL_EXCESS_PRIMES)
    )


def ordinary_q_one_g_arithmetic(s: int) -> bool:
    # In the frozen zero-k phase, X=12s+1 must have only 1 mod 3 primes.
    return all(prime % 3 == 1 for prime in factorint(12 * s + 1))


def c8_phase_candidate(u: int) -> dict[str, object] | None:
    # s=86+103u is the c=8, j=11, g=1 zero-k ray.  After the named
    # gap-7 terminal sieve and q*=103 roughness, only u=1,6 mod 7 remains.
    if u < 0 or u % 7 not in {1, 6}:
        return None
    s = 86 + 103 * u
    p = 48 * s + 1
    if not exact_qstar_103_rough(s):
        return None
    if not is_prime(p):
        return None
    if not ordinary_q_one_g_arithmetic(s):
        return None
    if math.gcd(24 * s + 1, 66 * s + 1) != 1:
        return None
    if (11 * p + 4) % (3 * 103):
        return None
    # The frozen zero-k equation is c*j+8*g=12*c with (c,j,g)=(8,11,1).
    if 8 * 11 + 8 != 12 * 8:
        raise AssertionError("c=8 zero-k phase identity changed")
    return {
        "u": u,
        "s": s,
        "p": p,
        "six_s_minus_one_factors": factorint(6 * s - 1),
        "twelve_s_plus_one_factors": factorint(12 * s + 1),
    }


def verify_type_i_terminal_241441() -> dict[str, object]:
    # Fixed B=1, E=12 p-1 Type-I receipt already present in the 1m profile.
    p, E, B, C, H = 241_441, 12, 1, 129, 5_147
    R = E - 1
    K = (p * R + 1) // 4
    A = (H + B) // R
    gap = (4 * B * B * C + 1) // R
    if not (
        4 * K == p * R + 1
        and K == B * C * H
        and H == A * R - B
        and p == 4 * A * B * C - gap
    ):
        raise AssertionError("p=241441 Type-I normal form changed")
    x = A * B * C
    y = A * C * H
    z = p * K
    if Fraction(1, x) + Fraction(1, y) + Fraction(1, z) != Fraction(4, p):
        raise AssertionError("p=241441 terminal identity failed")
    return {
        "prime": p,
        "certificate_type": "registered_direct_root_terminal",
        "normal_form": {"A": A, "B": B, "C": C, "H": H, "gap": gap},
        "denominators": [x, y, z],
    }


def verify_terminal_preempted_controls() -> dict[str, object]:
    candidates = [candidate for u in range(49) if (candidate := c8_phase_candidate(u))]
    if candidates != [
        {
            "u": 48,
            "s": 5_030,
            "p": 241_441,
            "six_s_minus_one_factors": {103: 1, 293: 1},
            "twelve_s_plus_one_factors": {7: 1, 8_623: 1},
        }
    ]:
        raise AssertionError(f"minimal c=8 residual scan changed: {candidates}")

    terminal = verify_type_i_terminal_241441()

    # The repository's original arithmetic c=8 control is preempted too.
    p = 157_393
    denominators = (39_375, 57_920_624, 2_280_624_570_000)
    if Fraction(1, denominators[0]) + Fraction(1, denominators[1]) + Fraction(
        1, denominators[2]
    ) != Fraction(4, p):
        raise AssertionError("p=157393 terminal control changed")

    return {
        "first_frozen_necessary_predicate_candidate": candidates[0],
        "candidate_terminal": terminal,
        "original_c8_control": {
            "prime": p,
            "terminal_denominators": list(denominators),
        },
        "actual_persistent_c8_dead_end_fixture": None,
    }


def audit_c8_branches() -> list[dict[str, str]]:
    return [
        {
            "branch": "terminal-first hit",
            "disposition": "root_terminal_leaf",
        },
        {
            "branch": "actual high-q with c_a<8 and c_Sigma<8",
            "disposition": "T2-v1 parent-anchored strict macro (marker included)",
        },
        {
            "branch": "second full-excess carry",
            "disposition": "rejected: target capacity is >8",
        },
        {
            "branch": "two named structured m=1 nodes",
            "disposition": "rejected: forced carry is >8; E1 source also absent",
        },
        {
            "branch": "only an unspecified non-p V-side raw prime is known",
            "disposition": "OPEN: no theorem selects a high-q double-low receipt",
        },
        {
            "branch": "high-q but c_a>=8 or c_Sigma>=8",
            "disposition": "OPEN: no current T5 ticket",
        },
    ]


def run_audit() -> dict[str, object]:
    edge_rows = audit_current_edge_marks()
    if sum(row["mark_policy"] == "ordinary_Sol(p)_identity" for row in edge_rows) != 14:
        raise AssertionError("ordinary edge-family count changed")
    return {
        "audit_id": "t6_actual_reachable_coverage_v1",
        "current_edge_mark_rows": edge_rows,
        "ordinary_mark_closure": {
            "root_mark": "Sol(p)",
            "concrete_current_edge_generators_preserve_root_mark": True,
            "nontrivial_mark_seed_in_current_taxonomy": False,
            "scope": "current named edge generators only",
        },
        "atomic_surface": audit_atomic_surface(),
        "c8_branch_surface": audit_c8_branches(),
        "terminal_preempted_controls": verify_terminal_preempted_controls(),
        "t6_totality": "OPEN",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = run_audit()
    if args.verify:
        print("T6 actual reachable coverage audit passed")
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
