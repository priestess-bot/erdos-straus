#!/usr/bin/env python3
"""Generic verifier for the corrected H4 clean-q E1--E5 relative macro.

This verifier does *not* reconstruct the upstream 19-phase H4 provenance.
It accepts that provenance, and the earlier versioned priority-prefix miss,
as explicit premises/receipt references.  It then recomputes every integer
quantity used by the H4 clean-q macro, constructs a canonical target state,
and verifies the local E1--E5 obligations.

The target is serialized as ``pending_dispatch``: no F/G/hit label is inherited.
Any subsequent selector action must recompute its own type/fiber data from the
canonical target integers.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ADAPTER_VERSION = "h4_clean_q_e1_e5_relative_macro_v1"
INPUT_SCHEMA = "h4-clean-q-macro-input/v1"
OUTPUT_SCHEMA = "h4-clean-q-macro-receipt/v1"
EXPECTED_UPSTREAM_CLAIM = (
    "type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff"
)
STUTTER_CLOSURE_CLAIM = (
    "type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-"
    "universal-stutter-source-d-gate-closure"
)
CORRECTED_CLOSURE_CLAIM = (
    "type-II-q-one-c-two-19-phase-h4-clean-q-e1-e5-relative-macro-closure"
)


class VerificationError(ValueError):
    pass


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise VerificationError(msg)


def canonical_json(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(prefix: str, obj: Any) -> str:
    h = hashlib.sha256(canonical_json(obj).encode("utf-8")).hexdigest()
    return f"{prefix}:{h}"


def factorint(n: int) -> dict[int, int]:
    require(n > 0, "factorint expects a positive integer")
    out: dict[int, int] = {}
    while n % 2 == 0:
        out[2] = out.get(2, 0) + 1
        n //= 2
    d = 3
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def valuation(n: int, ell: int) -> int:
    require(ell > 1, "valuation base must exceed 1")
    a = 0
    while n % ell == 0:
        a += 1
        n //= ell
    return a


def complete_excess(value: int, carrier: int) -> int:
    """Canonical maximal complete-excess block Q_carrier(value).

    A prime power ell^v in ``value`` is kept iff v > v_ell(carrier), and when
    kept its *full* exponent v is retained.  The bit-length power formula is
    equivalent and avoids an explicit factorization of ``value``.
    """
    require(value > 0 and carrier > 0, "complete_excess expects positive integers")
    g = math.gcd(value, carrier)
    return math.gcd(value, pow(value // g, value.bit_length(), value))


def canonical_raw_q_word(z: int, q: int, carrier: int) -> tuple[list[dict[str, int]], int]:
    """Replay the canonical prime-factor q-word on the y-coordinate."""
    current = z
    steps: list[dict[str, int]] = []
    for ell, exp in sorted(factorint(q).items()):
        for _ in range(exp):
            require(current % ell == 0, f"q-word cannot divide current y by {ell}")
            require(
                valuation(current, ell) > valuation(carrier, ell),
                f"raw q-edge at ell={ell} is not complete-excess",
            )
            before = current
            current //= ell
            steps.append({"ell": ell, "before_y": before, "after_y": current})
    require(current * q == z, "q-word does not remove exactly q")
    return steps, current


def audit_proper_prefixes(r4: int, z: int, q: int, k4: int) -> list[dict[str, int]]:
    """Verify every proper q-word prefix retains a factor outside K4.

    Hence no proper prefix is a full-excess sink x*y | K4.
    """
    current = z
    removed = 1
    proof: list[dict[str, int]] = []
    q_factors: list[int] = []
    for ell, exp in sorted(factorint(q).items()):
        q_factors.extend([ell] * exp)
    for ell in q_factors:
        # Before each removal, ``removed<q``; this includes the empty prefix
        # e=1 and every nonempty proper prefix.  The next q-prime is still
        # present in y and is absent from K4, so x*y cannot divide K4.
        next_ell = ell
        require(current % next_ell == 0, "proper prefix lost remaining q-factor")
        require(k4 % next_ell != 0, "remaining q-factor unexpectedly lies in K4")
        x = r4 - current
        require(k4 % (x * current) != 0,
                "proper prefix unexpectedly became a full-excess sink")
        proof.append({
            "removed": removed,
            "y": current,
            "remaining_clean_prime": next_ell,
        })
        current //= ell
        removed *= ell
    return proof


@dataclass(frozen=True)
class H4Input:
    p: int
    r4: int
    k4: int
    m4: int
    c4: int
    persistent_parent: dict[str, Any]
    priority_prefix: dict[str, Any]
    upstream_h4: dict[str, Any]
    schema_version: str = INPUT_SCHEMA

    @classmethod
    def from_dict(cls, obj: dict[str, Any]) -> "H4Input":
        return cls(
            p=int(obj["p"]),
            r4=int(obj["R4"]),
            k4=int(obj["K4"]),
            m4=int(obj["M4"]),
            c4=int(obj["c4"]),
            persistent_parent=dict(obj["persistent_parent"]),
            priority_prefix=dict(obj["priority_prefix"]),
            upstream_h4=dict(obj["upstream_h4"]),
            schema_version=str(obj.get("schema_version", "")),
        )


def corrected_target_support(m4: int, q_x: int, q_y: int) -> int:
    """The corrected formula, valid for both single-side and atomic endpoints."""
    return math.lcm(m4, q_x, q_y)


def verify_h4_macro(inp: H4Input) -> dict[str, Any]:
    p, r4, k4, m4, c4 = inp.p, inp.r4, inp.k4, inp.m4, inp.c4

    # ------------------------------------------------------------------
    # Relative premises: upstream actual H4 receipt and priority miss.
    # ------------------------------------------------------------------
    require(inp.schema_version == INPUT_SCHEMA, "wrong input schema")
    parent_id = str(inp.persistent_parent.get("state_id", ""))
    require(parent_id, "persistent parent state_id is required")
    require(inp.persistent_parent.get("source_tree_scope") == "charged_history_only",
            "H4 macro requires charged_history_only source-tree scope")
    require(inp.persistent_parent.get("rank") == [0, p - 1],
            "persistent parent rank must be [0,p-1]")

    require(inp.priority_prefix.get("status") == "miss",
            "H4 macro is entered only after the versioned priority prefix misses")
    require(inp.priority_prefix.get("source_state_id") == parent_id,
            "priority-prefix receipt refers to a different source state")
    require(bool(inp.priority_prefix.get("policy_version")), "priority policy version is required")
    require(bool(inp.priority_prefix.get("receipt_id")), "priority-prefix receipt_id is required")

    require(bool(inp.upstream_h4.get("receipt_id")), "upstream H4 receipt_id is required")
    upstream_claim = str(inp.upstream_h4.get("claim_id", ""))
    require(upstream_claim, "upstream H4 claim_id is required")

    # ------------------------------------------------------------------
    # E1: recompute the H4 arithmetic checkpoint and clean q-word.
    # ------------------------------------------------------------------
    require(is_prime(p), "p must be prime")
    require(p % 24 == 1, "p must be a core prime 1 mod 24")
    require(r4 > 0 and k4 > 0 and m4 > 0, "H4 chart integers must be positive")
    require(r4 % p == 1, "H4 checkpoint requires R4 == 1 mod p")
    require(r4 % 4 == 3, "R4 must be 3 mod 4")
    require(p * r4 + 1 == 4 * k4, "H4 chart equation p*R4+1=4*K4 failed")
    require(k4 == m4 * c4, "K4=M4*c4 failed")
    require(m4 > ((p - 1) ** 2) // 4, "H4 support must be in the high-support region")
    require(1 <= c4 <= p - 2, "H4 checkpoint capacity must already be strict")
    require(2 * r4 > p**3, "H4 high-R premise failed")

    h = math.gcd(r4 - 1, k4)
    z = r4 - h
    require(1 < h < r4, "proper-overlap H4 requires 1<h<R4")
    require(math.gcd(z, r4) == 1, "H4 endpoint precursor must be primitive")

    w = (p + 1) // 2
    d = math.gcd(w, m4)
    q = w // d
    require(q > 1, "clean q-bridge requires q>1")
    require(h == 2 * d, "actual carry identity h=2d failed")
    require(h * q == p + 1, "actual carry identity hq=p+1 failed")

    q_block = complete_excess(z, k4)
    require(q_block % q == 0, "q is not contained in the complete-excess block of z")
    require(math.gcd(q, k4) == 1, "clean-carrier condition gcd(q,K4)=1 failed")
    require(q_block % p != 0, "q-block must be p-free")

    m_alt = math.lcm(m4, q_block)
    require(math.gcd(m_alt, p) == 1, "alternate support must be p-free")
    c_alt = pow((4 * m_alt) % p, -1, p)
    require(c_alt == p - 1, "H4 top-capacity premise c_alt=p-1 failed")
    # The H4 a_alt gate is defined on the associated d=1 alternate source
    # n_alt=(4*M_alt+1)/p.  Do not confuse it with the canonical linear-chart
    # target R=(4*M*c-1)/p used later for E2.
    require((4 * m_alt + 1) % p == 0, "top-capacity alternate source is not integral")
    n_alt = (4 * m_alt + 1) // p
    require((n_alt + 1) % 2 == 0, "alternate source half-coordinate is not integral")
    a_alt = w // math.gcd(w, (n_alt + 1) // 2)
    require(a_alt == 1, "H4 a_alt=1 premise failed")

    raw_steps, y_q = canonical_raw_q_word(z, q, k4)
    prefix_receipts = audit_proper_prefixes(r4, z, q, k4)
    x_q = r4 - y_q
    require(x_q > 0 and y_q > 0, "q-endpoint coordinates must be positive")
    require(math.gcd(x_q, y_q) == 1, "q-endpoint must remain primitive")

    q_x = complete_excess(x_q, k4)
    q_y = complete_excess(y_q, k4)
    beta_x = x_q // q_x
    beta_y = y_q // q_y
    require(q_y == q_block // q, "y-side complete-excess block is not Q/q")
    require(q_y > 1, "actual H4 endpoint theorem requires Q_y>1")
    require(math.gcd(q_x, beta_x) == 1, "x complete-excess decomposition is not primitive")
    require(math.gcd(q_y, beta_y) == 1, "y complete-excess decomposition is not primitive")
    require(math.gcd(q_x, q_y) == 1, "endpoint complete-excess blocks must be coprime")
    require(k4 % (beta_x * beta_y) == 0, "beta_x*beta_y must divide K4")
    require((q_x * q_y) % p != 0, "endpoint complete-excess blocks must be p-free")

    branch = "single_side" if q_x == 1 else "atomic_split"
    require(branch == "single_side" or (q_x > 1 and q_y > 1),
            "endpoint is neither actual single-side nor atomic-split")
    if branch == "single_side":
        require(k4 % (x_q * beta_y) == 0,
                "single-side residual divisibility x_q*beta_y | K4 failed")

    # ------------------------------------------------------------------
    # E2: corrected canonical support and target chart.
    # ------------------------------------------------------------------
    m_target = corrected_target_support(m4, q_x, q_y)
    require(m_target % m4 == 0, "target support must extend M4")
    require(m_target > m4, "actual Q_y>1 must produce a strict support enlargement")
    require(m_target % p != 0, "target support must remain p-free")

    l0 = m_alt // m4
    l_target = m_target // m4
    e_x = q_x // math.gcd(m4, q_x)
    e_y = q_y // math.gcd(m4, q_y)
    require(l0 % q == 0, "L0/q is not integral")
    require(e_y == l0 // q, "y-side multiplier identity E_y=L0/q failed")
    require(l_target == e_x * e_y, "corrected multiplier identity L=E_x*E_y failed")

    c_target = pow((4 * m_target) % p, -1, p)
    require(c_target == (c4 * pow(l_target % p, -1, p)) % p,
            "capacity transport c_target=c4*L^-1 mod p failed")
    require(c_target == (-q * pow(e_x % p, -1, p)) % p,
            "stutter-reduction identity c_target=-q*E_x^-1 mod p failed")

    # The universal stutter theorem is an upstream proof dependency.  The
    # verifier also checks the concrete receipt is not a forbidden stutter.
    require(c_target != p - 1,
            f"forbidden first stutter: contradicts {STUTTER_CLOSURE_CLAIM}")
    require(1 <= c_target <= p - 2, "target capacity is not strict")
    if branch == "single_side":
        require(e_x == 1, "single-side must have E_x=1")
        require(c_target == p - q, "single-side capacity formula c=p-q failed")

    k_target = m_target * c_target
    require((4 * k_target - 1) % p == 0, "target R is not integral")
    r_target = (4 * k_target - 1) // p
    require(r_target > 0 and r_target % 4 == 3, "target R must be positive and 3 mod 4")
    require(p * r_target + 1 == 4 * k_target, "target chart equation failed")

    # ------------------------------------------------------------------
    # E3: canonical serialization; dispatch labels are *not* inherited.
    # ------------------------------------------------------------------
    source_state = {
        "state_id": parent_id,
        "p": p,
        "marked_solution_set": "Sol(p)",
        "source_tree_scope": "charged_history_only",
        "rank": [0, p - 1],
    }
    target_core = {
        "p": p,
        "R": r_target,
        "K": k_target,
        "absorbed_support": m_target,
        "capacity": c_target,
        "marked_solution_set": "Sol(p)",
        "source_tree_scope": "charged_history_only",
        "dispatch_status": "pending_dispatch",
        "inherited_type_label": False,
        "rank": [0, c_target],
    }
    target_state_id = digest("state", target_core)
    target_state = {"state_id": target_state_id, **target_core}

    occurrence_core = {
        "adapter_version": ADAPTER_VERSION,
        "source_state_id": parent_id,
        "upstream_h4_receipt_id": inp.upstream_h4["receipt_id"],
        "q": q,
        "raw_path": [s["ell"] for s in raw_steps],
        "endpoint": [x_q, y_q],
        "blocks": [q_x, q_y],
    }
    occurrence_id = digest("h4occ", occurrence_core)
    if branch == "atomic_split":
        owner = {
            "owner_id": digest("owner", occurrence_core),
            "owner_rule": "canonical_raw_q_path_plus_maximal_complete_excess",
            "physical_occurrence_id": occurrence_id,
        }
    else:
        owner = {
            "bundle_id": digest("bundle", occurrence_core),
            "owner_rule": "single_nontrivial_y_block",
            "physical_occurrence_id": occurrence_id,
        }

    # ------------------------------------------------------------------
    # E4: chart-independent marked set, so the lift is literally identity.
    # ------------------------------------------------------------------
    lift = {
        "kind": "identity_on_Sol(p)",
        "domain": "Sol(p)",
        "codomain": "Sol(p)",
        "total": True,
    }

    # ------------------------------------------------------------------
    # E5: compare the original persistent parent to the final target.
    # ------------------------------------------------------------------
    source_rank = (0, p - 1)
    target_rank = (0, c_target)
    require(target_rank < source_rank, "global H4 macro rank does not strictly decrease")

    edge_core = {
        "adapter_version": ADAPTER_VERSION,
        "source_state_id": parent_id,
        "target_state_id": target_state_id,
        "occurrence_id": occurrence_id,
        "priority_prefix_receipt_id": inp.priority_prefix["receipt_id"],
    }
    edge_id = digest("edge", edge_core)

    return {
        "schema_version": OUTPUT_SCHEMA,
        "claim_id": CORRECTED_CLOSURE_CLAIM,
        "adapter_version": ADAPTER_VERSION,
        "proof_boundary": "relative_to_validated_actual_h4_receipt_and_priority_prefix_miss",
        "proof_dependencies": [
            upstream_claim,
            STUTTER_CLOSURE_CLAIM,
            "type-I-path-anchored-atomic-split-complete-excess-admission",
            "denominator-escape-state-contract",
        ],
        "source": source_state,
        "upstream_h4": inp.upstream_h4,
        "priority_prefix": inp.priority_prefix,
        "h4": {
            "R4": r4,
            "K4": k4,
            "M4": m4,
            "c4": c4,
            "h": h,
            "z": z,
            "w": w,
            "d": d,
            "q": q,
            "q_block": q_block,
            "alternate_support": m_alt,
            "alternate_capacity": c_alt,
            "a_alt": a_alt,
        },
        "raw_q_word": {
            "steps": raw_steps,
            "proper_prefix_nonterminal_receipts": prefix_receipts,
        },
        "endpoint": {
            "x": x_q,
            "y": y_q,
            "Q_x": q_x,
            "Q_y": q_y,
            "beta_x": beta_x,
            "beta_y": beta_y,
            "branch": branch,
            "p_free": True,
        },
        "corrected_support": {
            "formula": "lcm(M4,Q_x,Q_y)",
            "M_target": m_target,
            "L0": l0,
            "E_x": e_x,
            "E_y": e_y,
            "L_target": l_target,
            "capacity": c_target,
            "stutter": False,
        },
        "owner": owner,
        "target": target_state,
        "typed_reclassification": {
            "status": "required_before_next_type_specific_selector_action",
            "inherited_label": False,
            "note": (
                "This macro validates the canonical integer target and serializes it as "
                "pending_dispatch. Any F/G/hit classifier must recompute from target integers."
            ),
        },
        "lift": lift,
        "rank_check": {
            "source_rank": list(source_rank),
            "target_rank": list(target_rank),
            "strict": True,
        },
        "e1_e5": {"E1": True, "E2": True, "E3": True, "E4": True, "E5": True},
        "selector_status": "verified_edge",
        "recursive_edge_eligible": True,
        "edge_id": edge_id,
    }


CONTROL_FIXTURES = [
    # Local arithmetic controls inherited from the existing clean-q reproduction.
    {"name": "p73", "p": 73, "peeled_part": 3366},
    {"name": "p241", "p": 241, "peeled_part": 29886},
]


def make_control_input(p: int, peeled_part: int, name: str) -> H4Input:
    r4 = 1 + p * peeled_part
    k4 = (p * r4 + 1) // 4
    m4 = k4
    c4 = 1
    parent_id = f"control-parent:{name}"
    return H4Input(
        p=p,
        r4=r4,
        k4=k4,
        m4=m4,
        c4=c4,
        persistent_parent={
            "state_id": parent_id,
            "source_tree_scope": "charged_history_only",
            "rank": [0, p - 1],
        },
        priority_prefix={
            "status": "miss",
            "policy_version": "control-priority-v1",
            "source_state_id": parent_id,
            "receipt_id": f"control-priority-receipt:{name}",
        },
        upstream_h4={
            "claim_id": EXPECTED_UPSTREAM_CLAIM,
            "receipt_id": f"local-arithmetic-control:{name}",
            "evidence_scope": "local_arithmetic_control_not_upstream_proof",
        },
    )


def verify_controls() -> list[dict[str, Any]]:
    out = []
    for f in CONTROL_FIXTURES:
        receipt = verify_h4_macro(make_control_input(**f))
        out.append({
            "name": f["name"],
            "branch": receipt["endpoint"]["branch"],
            "q": receipt["h4"]["q"],
            "M_target": receipt["corrected_support"]["M_target"],
            "capacity": receipt["corrected_support"]["capacity"],
            "e1_e5": receipt["e1_e5"],
            "edge_id": receipt["edge_id"],
        })
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--input", type=Path, help="JSON H4 macro input")
    group.add_argument("--verify-controls", action="store_true")
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    if args.verify_controls:
        result: Any = {
            "controls_only": True,
            "note": "These fixtures test arithmetic/serialization; they do not prove upstream H4 provenance.",
            "results": verify_controls(),
        }
    else:
        obj = json.loads(args.input.read_text(encoding="utf-8"))
        result = verify_h4_macro(H4Input.from_dict(obj))

    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
