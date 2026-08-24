#!/usr/bin/env python3
"""Track-local AtomicPendingTargetV1 proposal and exact target disposition.

This module is intentionally below the shared selector grammar.  It turns a
parent-bound H4/c8 atomic payload into one of terminal, recomputed F,
recomputed G, or rejection.  The pending object is an internal artifact and
must never be enqueued.  Exact fiber computation is finite for a supplied
factorization; a caller still has to provide the parent/path and final owner
evidence before a successor can be admitted.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from dataclasses import dataclass
from enum import Enum
from math import gcd
from typing import Any, Sequence


SCHEMA_ID = "atomic_pending_target_v1"
SCHEMA_VERSION = 1
ARMS = frozenset({"H4_A1", "C8_DOUBLE_LOW"})
FORBIDDEN_MARKERS = frozenset(
    {"pending_suffix", "pending_dispatch", "later_selector", "inherited_F_G_hit_label"}
)


class AtomicProtocolError(ValueError):
    """A stable local error for an incomplete or unsafe atomic transition."""

    def __init__(self, code: str, detail: str):
        super().__init__(f"{code}: {detail}")
        self.code = code
        self.detail = detail


class FiberKind(str, Enum):
    HIT = "HIT"
    F = "F"
    G = "G"


class Disposition(str, Enum):
    TERMINAL = "TERMINAL"
    F_SUCCESSOR = "RECOMPUTED_F_SUCCESSOR"
    G_SUCCESSOR = "RECOMPUTED_G_SUCCESSOR"
    REJECT = "REJECT_BEFORE_QUEUE"


def digest(payload: Any) -> str:
    try:
        encoded = json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
            allow_nan=False,
        ).encode("ascii")
    except (TypeError, ValueError) as exc:
        raise AtomicProtocolError("NON_CANONICAL_PAYLOAD", str(exc)) from exc
    return hashlib.sha256(encoded).hexdigest()


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def _positive_int(value: Any, name: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
        raise AtomicProtocolError("INVALID_CHART", f"{name} must be positive")
    return value


@dataclass(frozen=True)
class ChartFacts:
    prime: int
    residual: int
    carrier: int
    support: int
    capacity: int
    carrier_factors: tuple[tuple[int, int], ...]

    def __post_init__(self) -> None:
        p = _positive_int(self.prime, "prime")
        r = _positive_int(self.residual, "residual")
        k = _positive_int(self.carrier, "carrier")
        a = _positive_int(self.support, "support")
        c = _positive_int(self.capacity, "capacity")
        if p % 24 != 1 or r <= 1:
            raise AtomicProtocolError("INVALID_CHART", "prime/residual domain mismatch")
        if 4 * k != p * r + 1 or k != a * c:
            raise AtomicProtocolError("INVALID_CHART", "chart determinant or K=A*C mismatch")
        if gcd(p, a * r) != 1:
            raise AtomicProtocolError("INVALID_CHART", "chart support is not p/residual-free")
        if not self.carrier_factors:
            raise AtomicProtocolError("INVALID_CARRIER_FACTORIZATION", "empty carrier factorization")
        product = 1
        previous = 1
        for factor, exponent in self.carrier_factors:
            if not _is_prime(factor) or not isinstance(exponent, int) or exponent <= 0:
                raise AtomicProtocolError("INVALID_CARRIER_FACTORIZATION", "factor/exponent malformed")
            if factor <= previous:
                raise AtomicProtocolError("INVALID_CARRIER_FACTORIZATION", "factors are not canonical")
            if gcd(factor, p * r) != 1:
                raise AtomicProtocolError("INVALID_CARRIER_FACTORIZATION", "factor is not a unit")
            product *= factor**exponent
            previous = factor
        if product != k:
            raise AtomicProtocolError("INVALID_CARRIER_FACTORIZATION", "factors do not multiply to carrier")

    def payload(self) -> dict[str, Any]:
        return {
            "prime": self.prime,
            "residual": self.residual,
            "carrier": self.carrier,
            "support": self.support,
            "capacity": self.capacity,
            "carrier_factors": [list(item) for item in self.carrier_factors],
        }

    @property
    def chart_digest(self) -> str:
        return "chart:" + digest(self.payload())


@dataclass(frozen=True)
class FiberCertificate:
    chart_digest: str
    hit_vectors: tuple[tuple[int, ...], ...]
    minus_one_in_subgroup: bool
    recomputed: bool
    inherited_label: bool
    subgroup_size: int | None
    unbounded_f_witness: tuple[int, ...] | None

    @property
    def kind(self) -> FiberKind:
        if self.hit_vectors:
            return FiberKind.HIT
        return FiberKind.F if self.minus_one_in_subgroup else FiberKind.G

    @property
    def evidence_digest(self) -> str:
        evidence = {
            "chart_digest": self.chart_digest,
            "hit_vectors": [list(vector) for vector in self.hit_vectors],
            "minus_one_in_subgroup": self.minus_one_in_subgroup,
            "subgroup_size": self.subgroup_size,
            "unbounded_f_witness": (
                list(self.unbounded_f_witness)
                if self.unbounded_f_witness is not None
                else None
            ),
            "recomputed": self.recomputed,
            "inherited_label": self.inherited_label,
        }
        return "fiber:" + digest(evidence)


@dataclass(frozen=True)
class AtomicPendingTargetV1:
    source_parent_id: str
    source_macro_id: str
    source_path_digest: str
    terminal_first_digest: str
    atomic_grammar_arm: str
    canonical_payload: tuple[int, ...]
    chart: ChartFacts
    source_tree_scope: str
    parent_n7_potential: tuple[int, ...]
    t5_ticket_candidate: str
    content_digest: str

    def payload_without_digest(self) -> dict[str, Any]:
        return {
            "schema_id": SCHEMA_ID,
            "schema_version": SCHEMA_VERSION,
            "source_parent_id": self.source_parent_id,
            "source_macro_id": self.source_macro_id,
            "source_path_digest": self.source_path_digest,
            "terminal_first_digest": self.terminal_first_digest,
            "atomic_grammar_arm": self.atomic_grammar_arm,
            "canonical_payload": list(self.canonical_payload),
            "canonical_target_chart_facts": self.chart.payload(),
            "source_tree_scope": self.source_tree_scope,
            "parent_n7_potential": list(self.parent_n7_potential),
            "t5_ticket_candidate": self.t5_ticket_candidate,
        }

    def payload(self) -> dict[str, Any]:
        result = self.payload_without_digest()
        result["content_digest"] = self.content_digest
        return result


@dataclass(frozen=True)
class AtomicDisposition:
    disposition: Disposition
    fiber_kind: FiberKind | None
    reason: str
    source_parent_id: str
    chart_digest: str


def canonical_charged_n7(chart: ChartFacts) -> tuple[int, ...]:
    """Return the frozen T5 N7 potential for this final TYPEI/CHARGED chart."""
    boundary = (chart.prime - 1) ** 2 // 4
    return (
        chart.prime,
        2,
        4,
        boundary // chart.support,
        chart.capacity,
        0,
        0,
    )


def _require_token(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value:
        raise AtomicProtocolError("MISSING_PARENT_PATH", f"{name} is empty")
    if any(marker in value for marker in FORBIDDEN_MARKERS):
        raise AtomicProtocolError("FORBIDDEN_PENDING_MARKER", f"{name} contains a pending marker")
    return value


def make_pending(
    *,
    source_parent_id: str,
    source_macro_id: str,
    source_path_digest: str,
    terminal_first_digest: str,
    atomic_grammar_arm: str,
    canonical_payload: Sequence[int],
    chart: ChartFacts,
    source_tree_scope: str,
    parent_n7_potential: Sequence[int],
    t5_ticket_candidate: str,
) -> AtomicPendingTargetV1:
    if atomic_grammar_arm not in ARMS:
        raise AtomicProtocolError("UNSUPPORTED_ATOMIC_ARM", atomic_grammar_arm)
    tokens = {
        "source_parent_id": source_parent_id,
        "source_macro_id": source_macro_id,
        "source_path_digest": source_path_digest,
        "terminal_first_digest": terminal_first_digest,
        "source_tree_scope": source_tree_scope,
        "t5_ticket_candidate": t5_ticket_candidate,
    }
    for name, value in tokens.items():
        _require_token(value, name)
    payload = tuple(canonical_payload)
    if not payload or any(not isinstance(value, int) or isinstance(value, bool) for value in payload):
        raise AtomicProtocolError("INVALID_ATOMIC_PAYLOAD", "payload must be nonempty integer tuple")
    potential = tuple(parent_n7_potential)
    if (
        len(potential) != 7
        or any(not isinstance(value, int) or value < 0 for value in potential)
        or potential[:3] != (chart.prime, 2, 4)
    ):
        raise AtomicProtocolError("INVALID_N7_POTENTIAL", "parent potential must be N^7")
    if t5_ticket_candidate != "LOCAL_DROP":
        raise AtomicProtocolError(
            "INVALID_T5_TICKET", "H4/c8 atomic final targets require LOCAL_DROP"
        )
    bare = {
        "schema_id": SCHEMA_ID,
        "schema_version": SCHEMA_VERSION,
        "source_parent_id": source_parent_id,
        "source_macro_id": source_macro_id,
        "source_path_digest": source_path_digest,
        "terminal_first_digest": terminal_first_digest,
        "atomic_grammar_arm": atomic_grammar_arm,
        "canonical_payload": list(payload),
        "canonical_target_chart_facts": chart.payload(),
        "source_tree_scope": source_tree_scope,
        "parent_n7_potential": list(potential),
        "t5_ticket_candidate": t5_ticket_candidate,
    }
    return AtomicPendingTargetV1(
        source_parent_id=source_parent_id,
        source_macro_id=source_macro_id,
        source_path_digest=source_path_digest,
        terminal_first_digest=terminal_first_digest,
        atomic_grammar_arm=atomic_grammar_arm,
        canonical_payload=payload,
        chart=chart,
        source_tree_scope=source_tree_scope,
        parent_n7_potential=potential,
        t5_ticket_candidate=t5_ticket_candidate,
        content_digest="atomic:" + digest(bare),
    )


def _mod_pow(base: int, exponent: int, modulus: int) -> int:
    if exponent >= 0:
        return pow(base, exponent, modulus)
    return pow(pow(base, -exponent, modulus), -1, modulus)


def exact_fiber_certificate(
    chart: ChartFacts,
    *,
    unbounded_f_witness: Sequence[int] | None = None,
    max_nodes: int | None = None,
) -> FiberCertificate:
    """Compute hit and subgroup membership independently from target integers.

    The production default has no artificial cutoff: both finite sets are
    mathematically bounded by the supplied factorization and residual.  Tests
    or callers may request a fail-closed resource limit explicitly, but such a
    limited call is not a total classifier receipt.
    """
    factors = chart.carrier_factors
    box_size = 1
    for _, exponent in factors:
        box_size *= 2 * exponent + 1
    if max_nodes is not None and box_size > max_nodes:
        raise AtomicProtocolError("FIBER_WORK_LIMIT", f"bounded hit box has {box_size} points")
    hit_vectors: list[tuple[int, ...]] = []
    for vector in itertools.product(*[range(-e, e + 1) for _, e in factors]):
        residue = 1
        for (factor, _), exponent in zip(factors, vector, strict=True):
            residue = residue * _mod_pow(factor, exponent, chart.residual) % chart.residual
        if residue == chart.residual - 1:
            hit_vectors.append(tuple(vector))

    witness: tuple[int, ...] | None = None
    if hit_vectors:
        minus_one_in_subgroup = True
        subgroup_size = None
    elif unbounded_f_witness is not None:
        witness = tuple(unbounded_f_witness)
        if len(witness) != len(factors) or any(
            not isinstance(value, int) or isinstance(value, bool) for value in witness
        ):
            raise AtomicProtocolError("INVALID_F_WITNESS", "witness dimension/type mismatch")
        value = 1
        for (factor, _), exponent in zip(factors, witness, strict=True):
            value = value * _mod_pow(factor, exponent, chart.residual) % chart.residual
        if value != chart.residual - 1:
            raise AtomicProtocolError("INVALID_F_WITNESS", "witness does not evaluate to -1")
        minus_one_in_subgroup = True
        subgroup_size: int | None = None
    else:
        subgroup = {1}
        frontier = [1]
        nodes = 1
        while frontier:
            current = frontier.pop()
            for factor, _ in factors:
                for step in (factor % chart.residual, pow(factor, -1, chart.residual)):
                    successor = current * step % chart.residual
                    if successor not in subgroup:
                        subgroup.add(successor)
                        frontier.append(successor)
                        nodes += 1
                        if max_nodes is not None and nodes > max_nodes:
                            raise AtomicProtocolError("FIBER_WORK_LIMIT", "subgroup closure exceeds limit")
        minus_one_in_subgroup = chart.residual - 1 in subgroup
        subgroup_size = len(subgroup)
    return FiberCertificate(
        chart_digest=chart.chart_digest,
        hit_vectors=tuple(sorted(hit_vectors)),
        minus_one_in_subgroup=minus_one_in_subgroup,
        recomputed=True,
        inherited_label=False,
        subgroup_size=subgroup_size,
        unbounded_f_witness=witness,
    )


def verify_fiber_certificate(
    chart: ChartFacts, certificate: FiberCertificate
) -> None:
    """Replay a supplied certificate instead of trusting its status fields."""
    expected = exact_fiber_certificate(
        chart, unbounded_f_witness=certificate.unbounded_f_witness
    )
    if certificate != expected:
        raise AtomicProtocolError(
            "FIBER_CERTIFICATE_MISMATCH",
            "hit set, subgroup decision or witness does not replay",
        )


def resolve_pending(
    pending: AtomicPendingTargetV1,
    *,
    terminal_first_miss: bool,
    fiber: FiberCertificate | None,
) -> AtomicDisposition:
    """Close the pending marker into terminal/F/G or reject before queue."""
    if not terminal_first_miss:
        return AtomicDisposition(
            Disposition.TERMINAL,
            None,
            "TERMINAL_FIRST",
            pending.source_parent_id,
            pending.chart.chart_digest,
        )
    if fiber is None:
        return AtomicDisposition(
            Disposition.REJECT,
            None,
            "MISSING_RECOMPUTED_FIBER_CERTIFICATE",
            pending.source_parent_id,
            pending.chart.chart_digest,
        )
    if fiber.chart_digest != pending.chart.chart_digest:
        return AtomicDisposition(
            Disposition.REJECT,
            None,
            "TARGET_CHART_DIGEST_MISMATCH",
            pending.source_parent_id,
            pending.chart.chart_digest,
        )
    if not fiber.recomputed or fiber.inherited_label:
        return AtomicDisposition(
            Disposition.REJECT,
            None,
            "TARGET_FIBER_NOT_RECOMPUTED",
            pending.source_parent_id,
            pending.chart.chart_digest,
        )
    try:
        verify_fiber_certificate(pending.chart, fiber)
    except AtomicProtocolError as exc:
        return AtomicDisposition(
            Disposition.REJECT,
            None,
            exc.code,
            pending.source_parent_id,
            pending.chart.chart_digest,
        )
    if fiber.kind is FiberKind.HIT:
        return AtomicDisposition(
            Disposition.TERMINAL,
            FiberKind.HIT,
            "TARGET_CENTERED_HIT",
            pending.source_parent_id,
            pending.chart.chart_digest,
        )
    disposition = (
        Disposition.F_SUCCESSOR if fiber.kind is FiberKind.F else Disposition.G_SUCCESSOR
    )
    return AtomicDisposition(
        disposition,
        fiber.kind,
        "TARGET_FIBER_RECOMPUTED",
        pending.source_parent_id,
        pending.chart.chart_digest,
    )


def finalize_successor(
    pending: AtomicPendingTargetV1,
    disposition: AtomicDisposition,
    *,
    target_state_id: str,
    target_owner: str,
    target_n7_potential: Sequence[int],
    e4_lift_digest: str,
) -> dict[str, Any]:
    """Return a non-active final candidate; shared admission remains external."""
    if disposition.disposition not in {Disposition.F_SUCCESSOR, Disposition.G_SUCCESSOR}:
        raise AtomicProtocolError("NOT_A_NONTERMINAL_DISPOSITION", disposition.disposition.value)
    _require_token(target_state_id, "target_state_id")
    _require_token(target_owner, "target_owner")
    _require_token(e4_lift_digest, "e4_lift_digest")
    target_rank = tuple(target_n7_potential)
    if len(target_rank) != 7 or any(not isinstance(value, int) or value < 0 for value in target_rank):
        raise AtomicProtocolError("INVALID_N7_POTENTIAL", "target potential must be N^7")
    expected_target_rank = canonical_charged_n7(pending.chart)
    if target_rank != expected_target_rank:
        raise AtomicProtocolError(
            "N7_TARGET_MISMATCH", "target potential does not replay from its chart"
        )
    if not target_rank < pending.parent_n7_potential:
        raise AtomicProtocolError("N7_NOT_STRICT", "parent-to-final target is not strict")
    fiber_name = disposition.fiber_kind.value if disposition.fiber_kind else "UNKNOWN"
    result = {
        "schema_id": "atomic_final_candidate_v1",
        "schema_version": 1,
        "status": "FINAL_CANDIDATE_NOT_ACTIVE_SHARED_ADMISSION_REQUIRED",
        "source_parent_id": pending.source_parent_id,
        "source_macro_id": pending.source_macro_id,
        "source_path_digest": pending.source_path_digest,
        "atomic_grammar_arm": pending.atomic_grammar_arm,
        "target_state_id": target_state_id,
        "target_owner": target_owner,
        "target_fiber": fiber_name,
        "target_n7_potential": list(target_rank),
        "parent_n7_potential": list(pending.parent_n7_potential),
        "t5_ticket": pending.t5_ticket_candidate,
        "e4_lift_digest": e4_lift_digest,
        "requires_shared_reentry_receipt": True,
    }
    if any(marker in json.dumps(result) for marker in FORBIDDEN_MARKERS):
        raise AtomicProtocolError("FORBIDDEN_PENDING_MARKER", "final receipt retains pending marker")
    result["receipt_digest"] = "candidate:" + digest(result)
    return result


__all__ = [
    "ARMS",
    "AtomicDisposition",
    "AtomicPendingTargetV1",
    "AtomicProtocolError",
    "ChartFacts",
    "Disposition",
    "FiberCertificate",
    "FiberKind",
    "SCHEMA_ID",
    "SCHEMA_VERSION",
    "exact_fiber_certificate",
    "finalize_successor",
    "make_pending",
    "canonical_charged_n7",
    "resolve_pending",
    "verify_fiber_certificate",
]
