#!/usr/bin/env python3
"""Non-circular persistent-state admission kernel for the T6 selector.

The extractor in this module deliberately stops before family recognition.
It validates a small, content-addressed projection of a serializer output and
can therefore return a header for which no family predicate succeeds.  Owner
selection and queue admission are later operations.  This ordering is the
point of the contract: an unclassified E3 target is observable and rejected,
not removed from the domain by the definition of ``legal state``.

The module proves no constructor inventory theorem.  Callers must supply the
active producer registry reconstructed from source.  Likewise, replaying a
finite trace checks an implementation instance; the universal trace-induction
lemma is the mathematical statement documented in
``concepts/t6-persistent-selector-state-v1.md``.
"""

from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass
from enum import Enum
from math import gcd
from types import MappingProxyType
from typing import Any, Callable, Iterable, Mapping, Sequence


CONTRACT_ID = "t6_persistent_selector_state_v1"
STATE_SCHEMA_ID = "persistent_selector_state_v1"
STATE_SCHEMA_VERSION = 1
MARK_SCHEMA_ID = "selector_mark_receipt_v1"
TERMINAL_FIRST_SCHEMA_ID = "terminal_first_receipt_v1"
INITIALIZER_RECEIPT_SCHEMA_ID = "t6_initializer_nonterminal_receipt_v1"
SUCCESSOR_RECEIPT_SCHEMA_ID = "t6_admitted_successor_receipt_v1"

ROOT_INITIALIZER_OUTPUT = "ROOT_INITIALIZER_OUTPUT"
ADMITTED_SUCCESSOR = "ADMITTED_SUCCESSOR"
QUEUE_GATES = frozenset({ROOT_INITIALIZER_OUTPUT, ADMITTED_SUCCESSOR})

T5_TICKETS = frozenset({"OUTER_RANK_DROP", "PHASE_DROP", "LOCAL_DROP"})

ROOT_SOL = "ROOT_SOL"
NONTRIVIAL_MARK = "NONTRIVIAL_MARK"

PHASES = frozenset(
    {"TYPEII_REL", "TYPEII_G_HANDOFF", "TYPEI", "GENERIC_MARKED"}
)
TYPE_I_PROTOCOLS = frozenset({"CHARGED", "PRE", "ABSORB", "RESET"})
ENDPOINT_FIBERS = frozenset({"NONE", "F", "G"})
PROVENANCE_KINDS = frozenset(
    {
        "ORDINARY_ENDPOINT",
        "FULL_CARRIER_POST_G",
        "OVERFLOW",
        "PROPER_ROOT",
        "C8_PARENT",
        "H4_RESIDUAL",
        "C2_19_MACRO",
        "ATOMIC_PENDING",
        "MARKED_ABSORB",
        "GENERIC_MARKED",
    }
)
ATOMIC_ARMS = frozenset({"NONE", "H4_A1", "C8_DOUBLE_LOW"})
DISPATCH_STATUSES = frozenset({"NONE", "PENDING"})


class RejectCode(str, Enum):
    """Stable fail-closed reason codes for the v1 queue boundary."""

    ACCEPT = "ACCEPT"
    INPUT_NOT_MAPPING = "INPUT_NOT_MAPPING"
    UNKNOWN_SCHEMA = "UNKNOWN_SCHEMA"
    UNKNOWN_VERSION = "UNKNOWN_VERSION"
    UNKNOWN_TOP_LEVEL_FIELD = "UNKNOWN_TOP_LEVEL_FIELD"
    MISSING_TOP_LEVEL_FIELD = "MISSING_TOP_LEVEL_FIELD"
    CIRCULAR_CACHE_FIELD = "CIRCULAR_CACHE_FIELD"
    INVALID_ARTIFACT_CLASS = "INVALID_ARTIFACT_CLASS"
    INVALID_CONSUMER = "INVALID_CONSUMER"
    UNKNOWN_QUEUE_GATE = "UNKNOWN_QUEUE_GATE"
    UNKNOWN_PRODUCER = "UNKNOWN_PRODUCER"
    PRODUCER_GATE_MISMATCH = "PRODUCER_GATE_MISMATCH"
    PRODUCER_BRANCH_MISMATCH = "PRODUCER_BRANCH_MISMATCH"
    MALFORMED_MARK_RECEIPT = "MALFORMED_MARK_RECEIPT"
    MALFORMED_TERMINAL_FIRST_RECEIPT = "MALFORMED_TERMINAL_FIRST_RECEIPT"
    TERMINAL_OUTPUT_NOT_PERSISTENT = "TERMINAL_OUTPUT_NOT_PERSISTENT"
    MALFORMED_SOURCE_RECEIPT = "MALFORMED_SOURCE_RECEIPT"
    RECEIPT_DIGEST_MISMATCH = "RECEIPT_DIGEST_MISMATCH"
    RECEIPT_STATE_MISMATCH = "RECEIPT_STATE_MISMATCH"
    MALFORMED_SELECTOR_FACTS = "MALFORMED_SELECTOR_FACTS"
    UNKNOWN_HEADER_VALUE = "UNKNOWN_HEADER_VALUE"
    INVALID_CORE_CONTEXT = "INVALID_CORE_CONTEXT"
    INVALID_CHART_FACTS = "INVALID_CHART_FACTS"
    INVALID_ADMISSION_TICKET = "INVALID_ADMISSION_TICKET"
    PENDING_OUTPUT_NOT_PERSISTENT = "PENDING_OUTPUT_NOT_PERSISTENT"
    STATE_ID_MISMATCH = "STATE_ID_MISMATCH"
    FAMILY_NO_MATCH = "FAMILY_NO_MATCH"
    FAMILY_ILLEGAL_OVERLAP = "FAMILY_ILLEGAL_OVERLAP"
    PRODUCER_SOURCE_OWNER_NOT_DECLARED = "PRODUCER_SOURCE_OWNER_NOT_DECLARED"
    PRODUCER_TARGET_OWNER_NOT_DECLARED = "PRODUCER_TARGET_OWNER_NOT_DECLARED"
    OWNER_DIGEST_MISMATCH = "OWNER_DIGEST_MISMATCH"
    TRACE_ROOT_ORDER = "TRACE_ROOT_ORDER"
    DUPLICATE_STATE_ID = "DUPLICATE_STATE_ID"
    PARENT_NOT_REACHABLE = "PARENT_NOT_REACHABLE"


class StateContractError(ValueError):
    """An admission failure carrying a stable machine-readable code."""

    def __init__(self, code: RejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


@dataclass(frozen=True)
class ProducerRuleV1:
    """Source-derived queue rights for one constructor/serializer branch."""

    producer_id: str
    queue_gate: str
    branch_ids: frozenset[str]
    source_owners: frozenset[str]
    target_owners: frozenset[str]

    def __post_init__(self) -> None:
        if not self.producer_id:
            raise ValueError("producer_id must be nonempty")
        if self.queue_gate not in QUEUE_GATES:
            raise ValueError(f"unknown queue gate: {self.queue_gate}")
        if not self.branch_ids:
            raise ValueError("a producer rule needs at least one branch")
        if not self.target_owners:
            raise ValueError("a producer rule needs at least one target owner")
        if self.queue_gate == ROOT_INITIALIZER_OUTPUT and self.source_owners:
            raise ValueError("an initializer output has no persistent source owner")
        if self.queue_gate == ADMITTED_SUCCESSOR and not self.source_owners:
            raise ValueError("a successor rule must declare source owners")


@dataclass(frozen=True)
class VerifiedSelectorHeaderV1:
    """Typed projection produced before normalizer or owner computation."""

    state_id: str
    queue_gate: str
    producer_id: str
    branch_id: str
    parent_state_id: str | None
    root_context: int
    equation_rank: int
    mark_kind: str
    mark_receipt_digest: str
    terminal_first_digest: str
    source_receipt_digest: str
    facts_digest: str
    facts: Mapping[str, Any]


@dataclass(frozen=True)
class OwnerClassificationV1:
    owner: str
    matched_families: tuple[str, ...]
    precedence_index: int
    owner_digest: str


@dataclass(frozen=True)
class QueueAdmissionDecisionV1:
    accepted: bool
    reason_code: RejectCode
    detail: str
    state_id: str | None = None
    owner: str | None = None
    matched_families: tuple[str, ...] = ()
    owner_digest: str | None = None


@dataclass(frozen=True)
class TraceInductionReceiptV1:
    root_context: int
    admitted_state_ids: tuple[str, ...]
    owners: tuple[str, ...]
    base_steps: int
    successor_steps: int
    statement_scope: str = "finite_replay_instance_not_universal_constructor_proof"


Predicate = Callable[[VerifiedSelectorHeaderV1], bool]


@dataclass(frozen=True)
class FamilyPredicateV1:
    family_id: str
    predicate: Predicate


TOP_LEVEL_FIELDS = frozenset(
    {
        "schema_id",
        "schema_version",
        "state_id",
        "artifact_class",
        "consumer",
        "queue_gate",
        "producer_id",
        "branch_id",
        "parent_state_id",
        "root_context",
        "equation_rank",
        "mark",
        "terminal_first",
        "source_receipt",
        "facts",
    }
)

FACT_FIELDS = frozenset(
    {
        "major_phase",
        "type_i_protocol",
        "t5_eta_p",
        "pre_a",
        "absorb_m",
        "absorb_r_epsilon",
        "reset_carrier",
        "endpoint_fiber",
        "relation_q",
        "provenance_kind",
        "full_carrier_scope",
        "atomic_arm",
        "dispatch_status",
        "proper_root_k",
        "proper_root_height_class",
        "proper_root_height",
        "proper_root_r",
        "is_overflow",
        "support_A",
        "carrier_M",
        "overflow_d",
        "chart_R",
        "chart_K",
        "sink_scc_receipt",
        "same_chart_promotion_receipt",
    }
)

CIRCULAR_KEYS = frozenset(
    {
        "owner",
        "owner_digest",
        "selector_family_id",
        "family_id",
        "normal_form",
        "normalized_state",
        "normalizer_result",
    }
)


def canonical_digest_v1(payload: Any) -> str:
    """Return the content digest used by all v1 receipts."""

    try:
        encoded = json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
            allow_nan=False,
        ).encode("ascii")
    except (TypeError, ValueError) as exc:
        raise StateContractError(
            RejectCode.MALFORMED_SOURCE_RECEIPT,
            f"payload is not canonical JSON: {exc}",
        ) from exc
    return hashlib.sha256(encoded).hexdigest()


def seal_receipt_v1(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Copy and content-address a receipt fixture or serializer output."""

    result = copy.deepcopy(dict(payload))
    result.pop("digest", None)
    result["digest"] = canonical_digest_v1(result)
    return result


def build_state_id_v1(raw_state: Mapping[str, Any]) -> str:
    """Compute a state ID without consuming a cached owner or family."""

    payload = copy.deepcopy(dict(raw_state))
    payload.pop("state_id", None)
    return "state:" + canonical_digest_v1(payload)


def _is_plain_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _nonnegative_plain_int(value: Any) -> bool:
    return _is_plain_int(value) and value >= 0


def _expect_mapping(value: Any, code: RejectCode, name: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise StateContractError(code, f"{name} must be a mapping")
    return value


def _expect_string(value: Any, code: RejectCode, name: str) -> str:
    if not isinstance(value, str) or not value:
        raise StateContractError(code, f"{name} must be a nonempty string")
    return value


def _reject_circular_keys(value: Any, path: str = "state") -> None:
    if isinstance(value, Mapping):
        for key, child in value.items():
            if key in CIRCULAR_KEYS:
                raise StateContractError(
                    RejectCode.CIRCULAR_CACHE_FIELD,
                    f"{path}.{key} is a classifier/normalizer conclusion",
                )
            _reject_circular_keys(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _reject_circular_keys(child, f"{path}[{index}]")


def _validate_exact_fields(
    value: Mapping[str, Any],
    expected: frozenset[str],
    malformed_code: RejectCode,
    name: str,
) -> None:
    fields = set(value)
    missing = expected - fields
    extra = fields - expected
    if missing:
        raise StateContractError(malformed_code, f"{name} missing {sorted(missing)}")
    if extra:
        raise StateContractError(malformed_code, f"{name} has unknown {sorted(extra)}")


def _validate_sealed_receipt(
    receipt: Mapping[str, Any], expected_schema: str, code: RejectCode, name: str
) -> str:
    if receipt.get("schema_id") != expected_schema:
        raise StateContractError(code, f"{name}.schema_id is not {expected_schema}")
    if receipt.get("schema_version") != 1:
        raise StateContractError(code, f"{name}.schema_version is not 1")
    digest = receipt.get("digest")
    if not isinstance(digest, str) or len(digest) != 64:
        raise StateContractError(code, f"{name}.digest is malformed")
    payload = dict(receipt)
    payload.pop("digest")
    if canonical_digest_v1(payload) != digest:
        raise StateContractError(
            RejectCode.RECEIPT_DIGEST_MISMATCH, f"{name}.digest does not replay"
        )
    return digest


def _validate_mark(
    mark: Any, root_context: int, equation_rank: int
) -> tuple[str, str]:
    receipt = _expect_mapping(mark, RejectCode.MALFORMED_MARK_RECEIPT, "mark")
    expected = frozenset(
        {
            "schema_id",
            "schema_version",
            "receipt_id",
            "kind",
            "root_context",
            "equation_rank",
            "digest",
        }
    )
    _validate_exact_fields(
        receipt, expected, RejectCode.MALFORMED_MARK_RECEIPT, "mark"
    )
    digest = _validate_sealed_receipt(
        receipt, MARK_SCHEMA_ID, RejectCode.MALFORMED_MARK_RECEIPT, "mark"
    )
    _expect_string(
        receipt["receipt_id"], RejectCode.MALFORMED_MARK_RECEIPT, "mark.receipt_id"
    )
    if receipt["root_context"] != root_context or receipt["equation_rank"] != equation_rank:
        raise StateContractError(
            RejectCode.RECEIPT_STATE_MISMATCH,
            "mark root/equation coordinates differ from the state",
        )
    kind = receipt["kind"]
    if kind not in {ROOT_SOL, NONTRIVIAL_MARK}:
        raise StateContractError(
            RejectCode.MALFORMED_MARK_RECEIPT, f"unknown mark kind {kind!r}"
        )
    if kind == ROOT_SOL and equation_rank != root_context:
        raise StateContractError(
            RejectCode.MALFORMED_MARK_RECEIPT,
            "ROOT_SOL requires equation_rank == root_context",
        )
    if kind == NONTRIVIAL_MARK and equation_rank >= root_context:
        raise StateContractError(
            RejectCode.MALFORMED_MARK_RECEIPT,
            "NONTRIVIAL_MARK requires a strictly smaller positive equation rank",
        )
    return kind, digest


def _validate_terminal_first(receipt_value: Any) -> str:
    receipt = _expect_mapping(
        receipt_value,
        RejectCode.MALFORMED_TERMINAL_FIRST_RECEIPT,
        "terminal_first",
    )
    expected = frozenset(
        {
            "schema_id",
            "schema_version",
            "receipt_id",
            "scope",
            "outcome",
            "digest",
        }
    )
    _validate_exact_fields(
        receipt,
        expected,
        RejectCode.MALFORMED_TERMINAL_FIRST_RECEIPT,
        "terminal_first",
    )
    digest = _validate_sealed_receipt(
        receipt,
        TERMINAL_FIRST_SCHEMA_ID,
        RejectCode.MALFORMED_TERMINAL_FIRST_RECEIPT,
        "terminal_first",
    )
    _expect_string(
        receipt["receipt_id"],
        RejectCode.MALFORMED_TERMINAL_FIRST_RECEIPT,
        "terminal_first.receipt_id",
    )
    _expect_string(
        receipt["scope"],
        RejectCode.MALFORMED_TERMINAL_FIRST_RECEIPT,
        "terminal_first.scope",
    )
    if receipt["outcome"] == "HIT":
        raise StateContractError(
            RejectCode.TERMINAL_OUTPUT_NOT_PERSISTENT,
            "a terminal-first hit is a leaf, not a queue item",
        )
    if receipt["outcome"] != "MISS":
        raise StateContractError(
            RejectCode.MALFORMED_TERMINAL_FIRST_RECEIPT,
            f"unknown terminal-first outcome {receipt['outcome']!r}",
        )
    return digest


def _validate_facts(value: Any, root_context: int, mark_kind: str) -> Mapping[str, Any]:
    facts = _expect_mapping(value, RejectCode.MALFORMED_SELECTOR_FACTS, "facts")
    _validate_exact_fields(
        facts, FACT_FIELDS, RejectCode.MALFORMED_SELECTOR_FACTS, "facts"
    )
    phase = facts["major_phase"]
    type_i_protocol = facts["type_i_protocol"]
    endpoint = facts["endpoint_fiber"]
    provenance = facts["provenance_kind"]
    atomic_arm = facts["atomic_arm"]
    dispatch = facts["dispatch_status"]
    if phase not in PHASES:
        raise StateContractError(
            RejectCode.UNKNOWN_HEADER_VALUE, f"unknown major_phase {phase!r}"
        )
    if type_i_protocol is not None and type_i_protocol not in TYPE_I_PROTOCOLS:
        raise StateContractError(
            RejectCode.UNKNOWN_HEADER_VALUE,
            f"unknown type_i_protocol {type_i_protocol!r}",
        )
    if endpoint not in ENDPOINT_FIBERS:
        raise StateContractError(
            RejectCode.UNKNOWN_HEADER_VALUE, f"unknown endpoint_fiber {endpoint!r}"
        )
    if provenance not in PROVENANCE_KINDS:
        raise StateContractError(
            RejectCode.UNKNOWN_HEADER_VALUE, f"unknown provenance_kind {provenance!r}"
        )
    if atomic_arm not in ATOMIC_ARMS or dispatch not in DISPATCH_STATUSES:
        raise StateContractError(
            RejectCode.UNKNOWN_HEADER_VALUE,
            "unknown atomic_arm or dispatch_status",
        )
    for name in (
        "full_carrier_scope",
        "is_overflow",
        "sink_scc_receipt",
        "same_chart_promotion_receipt",
    ):
        if not isinstance(facts[name], bool):
            raise StateContractError(
                RejectCode.MALFORMED_SELECTOR_FACTS, f"facts.{name} must be boolean"
            )
    for name in (
        "relation_q",
        "proper_root_k",
        "support_A",
        "carrier_M",
        "overflow_d",
        "chart_R",
        "chart_K",
        "pre_a",
        "absorb_m",
        "reset_carrier",
        "proper_root_height",
        "proper_root_r",
    ):
        if facts[name] is not None and (
            not _is_plain_int(facts[name]) or facts[name] <= 0
        ):
            raise StateContractError(
                RejectCode.MALFORMED_SELECTOR_FACTS,
                f"facts.{name} must be null or a positive integer",
            )
    for name in ("t5_eta_p", "absorb_r_epsilon"):
        if not _nonnegative_plain_int(facts[name]):
            raise StateContractError(
                RejectCode.MALFORMED_SELECTOR_FACTS,
                f"facts.{name} must be a nonnegative integer",
            )

    height_class = facts["proper_root_height_class"]
    if height_class not in {"NONE", "LOW", "HIGH"}:
        raise StateContractError(
            RejectCode.UNKNOWN_HEADER_VALUE,
            f"unknown proper_root_height_class {height_class!r}",
        )

    if mark_kind == ROOT_SOL and phase == "GENERIC_MARKED":
        raise StateContractError(
            RejectCode.UNKNOWN_HEADER_VALUE,
            "a ROOT_SOL state cannot claim GENERIC_MARKED phase",
        )
    if mark_kind == NONTRIVIAL_MARK and not (
        phase == "GENERIC_MARKED" and provenance == "GENERIC_MARKED"
    ):
        raise StateContractError(
            RejectCode.UNKNOWN_HEADER_VALUE,
            "a nontrivial mark must use the generic-marked phase/provenance",
        )

    relation_q = facts["relation_q"]
    if phase == "TYPEII_REL":
        if not (
            endpoint == "F"
            and provenance == "ORDINARY_ENDPOINT"
            and _is_plain_int(relation_q)
            and relation_q > 1
        ):
            raise StateContractError(
                RejectCode.UNKNOWN_HEADER_VALUE,
                "TYPEII_REL requires an ordinary F endpoint with q>1",
            )
    elif phase == "TYPEII_G_HANDOFF":
        if not (
            endpoint == "G"
            and provenance == "ORDINARY_ENDPOINT"
            and _is_plain_int(relation_q)
            and relation_q >= 1
        ):
            raise StateContractError(
                RejectCode.UNKNOWN_HEADER_VALUE,
                "TYPEII_G_HANDOFF requires an ordinary G endpoint with q>=1",
            )
    elif relation_q is not None or endpoint != "NONE":
        raise StateContractError(
            RejectCode.UNKNOWN_HEADER_VALUE,
            "non-Type-II states cannot carry relation_q or an endpoint fiber",
        )

    if phase == "TYPEI":
        chart_r, chart_k, support_a = (
            facts["chart_R"],
            facts["chart_K"],
            facts["support_A"],
        )
        if not all(_is_plain_int(item) and item > 0 for item in (chart_r, chart_k, support_a)):
            raise StateContractError(
                RejectCode.INVALID_CHART_FACTS,
                "TYPEI requires positive R, K and support A",
            )
        if 4 * chart_k != root_context * chart_r + 1 or chart_k % support_a:
            raise StateContractError(
                RejectCode.INVALID_CHART_FACTS,
                "TYPEI base chart must satisfy 4K=pR+1 and A divides K",
            )
        if type_i_protocol not in TYPE_I_PROTOCOLS:
            raise StateContractError(
                RejectCode.UNKNOWN_HEADER_VALUE,
                "TYPEI requires an explicit frozen protocol",
            )
    elif type_i_protocol is not None or any(
        facts[name] is not None
        for name in (
            "support_A",
            "carrier_M",
            "overflow_d",
            "chart_R",
            "chart_K",
            "proper_root_k",
            "proper_root_height",
            "proper_root_r",
            "pre_a",
            "absorb_m",
            "reset_carrier",
        )
    ):
        raise StateContractError(
            RejectCode.INVALID_CHART_FACTS,
            "non-Type-I states cannot carry Type-I protocol/chart coordinates",
        )

    if phase == "TYPEI":
        protocol_payloads = {
            "CHARGED": (
                facts["pre_a"] is None
                and facts["absorb_m"] is None
                and facts["absorb_r_epsilon"] == 0
                and facts["reset_carrier"] is None
            ),
            "PRE": (
                _is_plain_int(facts["pre_a"])
                and facts["pre_a"] > 0
                and facts["t5_eta_p"] == 0
                and facts["absorb_m"] is None
                and facts["absorb_r_epsilon"] == 0
                and facts["reset_carrier"] is None
            ),
            "ABSORB": (
                facts["pre_a"] is None
                and facts["t5_eta_p"] == 0
                and _is_plain_int(facts["absorb_m"])
                and facts["absorb_m"] > 0
                and facts["reset_carrier"] is None
            ),
            "RESET": (
                facts["pre_a"] is None
                and facts["t5_eta_p"] == 0
                and facts["absorb_m"] is None
                and facts["absorb_r_epsilon"] == 0
                and _is_plain_int(facts["reset_carrier"])
                and facts["reset_carrier"] > 0
            ),
        }
        if not protocol_payloads[type_i_protocol]:
            raise StateContractError(
                RejectCode.MALFORMED_SELECTOR_FACTS,
                f"facts do not match TYPEI/{type_i_protocol} rank schema",
            )

    if phase == "TYPEI" and type_i_protocol == "CHARGED":
        chart_is_overflow = facts["chart_R"] > root_context
        if facts["is_overflow"] != chart_is_overflow:
            raise StateContractError(
                RejectCode.INVALID_CHART_FACTS,
                "TYPEI/CHARGED must classify overflow exactly by R>p",
            )
    if facts["is_overflow"]:
        if phase != "TYPEI" or type_i_protocol != "CHARGED":
            raise StateContractError(
                RejectCode.UNKNOWN_HEADER_VALUE,
                "overflow facts require TYPEI/CHARGED",
            )
    elif provenance == "OVERFLOW":
        raise StateContractError(
            RejectCode.UNKNOWN_HEADER_VALUE,
            "OVERFLOW provenance requires is_overflow=true",
        )

    if provenance == "MARKED_ABSORB":
        if not (
            phase == "TYPEI"
            and type_i_protocol == "ABSORB"
            and not facts["is_overflow"]
            and facts["chart_R"] < root_context
        ):
            raise StateContractError(
                RejectCode.UNKNOWN_HEADER_VALUE,
                "MARKED_ABSORB requires TYPEI/ABSORB, R<p and non-overflow",
            )
    elif type_i_protocol == "ABSORB":
        raise StateContractError(
            RejectCode.UNKNOWN_HEADER_VALUE,
            "ordinary ABSORB targets require MARKED_ABSORB provenance",
        )

    if provenance == "PROPER_ROOT":
        height = facts["proper_root_height"]
        root_parameter = facts["proper_root_r"]
        if not (
            type_i_protocol == "CHARGED"
            and _is_plain_int(height)
            and _is_plain_int(root_parameter)
            and root_parameter >= 1
        ):
            raise StateContractError(
                RejectCode.MALFORMED_SELECTOR_FACTS,
                "PROPER_ROOT requires CHARGED, root r>=1 and a positive root height",
            )
        root_modulus = (root_context * root_context + root_context + 1) // 3
        u_value = gcd(2 * root_parameter + 1, root_modulus)
        if not (
            0 < u_value < root_modulus
            and height == 3 * u_value
        ):
            raise StateContractError(
                RejectCode.MALFORMED_SELECTOR_FACTS,
                "proper-root height does not replay from r and the cyclotomic modulus",
            )
        root_half = (root_context + 1) // 2
        root_support = root_half * (root_context * root_context * root_parameter - root_half)
        root_carrier = root_support * (root_context - 1)
        root_residual = (
            2 * root_context**3 * root_parameter
            - root_context * root_context
            - 2 * root_context * root_parameter
            - root_context
            + 1
        )
        if (
            facts["support_A"],
            facts["chart_K"],
            facts["chart_R"],
        ) != (root_support, root_carrier, root_residual):
            raise StateContractError(
                RejectCode.INVALID_CHART_FACTS,
                "PROPER_ROOT chart must replay from p and r",
            )
        if not facts["is_overflow"]:
            raise StateContractError(
                RejectCode.INVALID_CHART_FACTS,
                "PROPER_ROOT chart is a TYPEI/CHARGED overflow",
            )
        if height_class == "LOW":
            if not (
                2 <= height < root_context
                and _is_plain_int(facts["proper_root_k"])
                and facts["proper_root_k"] > 0
            ):
                raise StateContractError(
                    RejectCode.MALFORMED_SELECTOR_FACTS,
                    "LOW proper root requires 2<=h<p and positive k",
                )
        elif height_class == "HIGH":
            if not (height > root_context and facts["proper_root_k"] is None):
                raise StateContractError(
                    RejectCode.MALFORMED_SELECTOR_FACTS,
                    "HIGH proper root requires h>p and no low-height k",
                )
        else:
            raise StateContractError(
                RejectCode.MALFORMED_SELECTOR_FACTS,
                "PROPER_ROOT requires LOW or HIGH height class",
            )
    elif not (
        facts["proper_root_k"] is None
        and facts["proper_root_height"] is None
        and facts["proper_root_r"] is None
        and height_class == "NONE"
    ):
        raise StateContractError(
            RejectCode.MALFORMED_SELECTOR_FACTS,
            "proper-root fields are reserved for PROPER_ROOT provenance",
        )
    if provenance == "C8_PARENT" and not (
        phase == "TYPEI"
        and type_i_protocol == "CHARGED"
        and facts["is_overflow"]
        and facts["support_A"] > 1
    ):
        raise StateContractError(
            RejectCode.INVALID_CHART_FACTS,
            "C8_PARENT is a high-support TYPEI/CHARGED overflow lineage",
        )
    if provenance == "ATOMIC_PENDING" or dispatch == "PENDING":
        raise StateContractError(
            RejectCode.PENDING_OUTPUT_NOT_PERSISTENT,
            "atomic pending output is a macro checkpoint, not a queue state",
        )
    if atomic_arm != "NONE" or dispatch != "NONE":
        raise StateContractError(
            RejectCode.MALFORMED_SELECTOR_FACTS,
            "atomic arm fields belong in edge receipts, not persistent states",
        )
    return MappingProxyType(copy.deepcopy(dict(facts)))


def _validate_source_receipt(
    receipt_value: Any,
    raw: Mapping[str, Any],
    facts_digest: str,
    terminal_digest: str,
) -> str:
    receipt = _expect_mapping(
        receipt_value, RejectCode.MALFORMED_SOURCE_RECEIPT, "source_receipt"
    )
    common = {
        "schema_id",
        "schema_version",
        "receipt_id",
        "producer_id",
        "branch_id",
        "root_context",
        "equation_rank",
        "target_facts_digest",
        "terminal_first_digest",
        "status",
        "digest",
    }
    if raw["queue_gate"] == ROOT_INITIALIZER_OUTPUT:
        expected = frozenset(common)
        schema = INITIALIZER_RECEIPT_SCHEMA_ID
        status = "NONTERMINAL_INITIALIZER_OUTPUT"
    else:
        expected = frozenset(
            common
            | {
                "parent_state_id",
                "E1",
                "E2",
                "E3",
                "E4",
                "E5",
                "T5_ticket",
            }
        )
        schema = SUCCESSOR_RECEIPT_SCHEMA_ID
        status = "VERIFIED_EDGE"
    _validate_exact_fields(
        receipt, expected, RejectCode.MALFORMED_SOURCE_RECEIPT, "source_receipt"
    )
    digest = _validate_sealed_receipt(
        receipt, schema, RejectCode.MALFORMED_SOURCE_RECEIPT, "source_receipt"
    )
    _expect_string(
        receipt["receipt_id"],
        RejectCode.MALFORMED_SOURCE_RECEIPT,
        "source_receipt.receipt_id",
    )
    expected_values = {
        "producer_id": raw["producer_id"],
        "branch_id": raw["branch_id"],
        "root_context": raw["root_context"],
        "equation_rank": raw["equation_rank"],
        "target_facts_digest": facts_digest,
        "terminal_first_digest": terminal_digest,
        "status": status,
    }
    for key, expected_value in expected_values.items():
        if receipt[key] != expected_value:
            raise StateContractError(
                RejectCode.RECEIPT_STATE_MISMATCH,
                f"source_receipt.{key} does not match state header",
            )
    if raw["queue_gate"] == ROOT_INITIALIZER_OUTPUT:
        if raw["parent_state_id"] is not None:
            raise StateContractError(
                RejectCode.RECEIPT_STATE_MISMATCH,
                "an initializer output cannot have a persistent parent",
            )
    else:
        if receipt["parent_state_id"] != raw["parent_state_id"]:
            raise StateContractError(
                RejectCode.RECEIPT_STATE_MISMATCH,
                "successor parent_state_id does not match its receipt",
            )
        if not isinstance(raw["parent_state_id"], str) or not raw["parent_state_id"]:
            raise StateContractError(
                RejectCode.MALFORMED_SOURCE_RECEIPT,
                "a successor requires a nonempty parent_state_id",
            )
        if not all(receipt[name] is True for name in ("E1", "E2", "E3", "E4", "E5")):
            raise StateContractError(
                RejectCode.MALFORMED_SOURCE_RECEIPT,
                "a successor receipt must explicitly carry E1--E5=true",
            )
        if receipt["T5_ticket"] not in T5_TICKETS:
            raise StateContractError(
                RejectCode.INVALID_ADMISSION_TICKET,
                f"unknown T5 ticket {receipt['T5_ticket']!r}",
            )
    return digest


def extract_verified_selector_header_v1(
    raw_state: Mapping[str, Any],
    registered_producers: Mapping[str, ProducerRuleV1],
) -> VerifiedSelectorHeaderV1:
    """Extract a verified header without calling any family predicate.

    Success means only that the independent state projection and its receipts
    replay.  In particular it does *not* mean that a family owner exists.
    """

    raw = _expect_mapping(raw_state, RejectCode.INPUT_NOT_MAPPING, "state")
    _reject_circular_keys(raw)
    fields = set(raw)
    missing = TOP_LEVEL_FIELDS - fields
    extra = fields - TOP_LEVEL_FIELDS
    if missing:
        raise StateContractError(
            RejectCode.MISSING_TOP_LEVEL_FIELD, f"state missing {sorted(missing)}"
        )
    if extra:
        raise StateContractError(
            RejectCode.UNKNOWN_TOP_LEVEL_FIELD, f"state has unknown {sorted(extra)}"
        )
    if raw["schema_id"] != STATE_SCHEMA_ID:
        raise StateContractError(
            RejectCode.UNKNOWN_SCHEMA, f"unknown state schema {raw['schema_id']!r}"
        )
    if raw["schema_version"] != STATE_SCHEMA_VERSION:
        raise StateContractError(
            RejectCode.UNKNOWN_VERSION, f"unknown state version {raw['schema_version']!r}"
        )
    if raw["artifact_class"] != "persistent_state":
        raise StateContractError(
            RejectCode.INVALID_ARTIFACT_CLASS,
            f"artifact_class={raw['artifact_class']!r}",
        )
    if raw["consumer"] != "t6_selector":
        raise StateContractError(
            RejectCode.INVALID_CONSUMER, f"consumer={raw['consumer']!r}"
        )
    if raw["queue_gate"] not in QUEUE_GATES:
        raise StateContractError(
            RejectCode.UNKNOWN_QUEUE_GATE, f"queue_gate={raw['queue_gate']!r}"
        )
    producer_id = _expect_string(
        raw["producer_id"], RejectCode.UNKNOWN_PRODUCER, "producer_id"
    )
    branch_id = _expect_string(
        raw["branch_id"], RejectCode.PRODUCER_BRANCH_MISMATCH, "branch_id"
    )
    rule = registered_producers.get(producer_id)
    if rule is None:
        raise StateContractError(
            RejectCode.UNKNOWN_PRODUCER, f"producer {producer_id!r} is not registered"
        )
    if rule.producer_id != producer_id:
        raise StateContractError(
            RejectCode.UNKNOWN_PRODUCER, "producer registry key/id mismatch"
        )
    if rule.queue_gate != raw["queue_gate"]:
        raise StateContractError(
            RejectCode.PRODUCER_GATE_MISMATCH,
            f"producer {producer_id!r} cannot use {raw['queue_gate']!r}",
        )
    if branch_id not in rule.branch_ids:
        raise StateContractError(
            RejectCode.PRODUCER_BRANCH_MISMATCH,
            f"branch {branch_id!r} is not registered for {producer_id!r}",
        )
    root_context, equation_rank = raw["root_context"], raw["equation_rank"]
    if not (
        _is_plain_int(root_context)
        and root_context > 1
        and root_context % 24 == 1
        and _is_plain_int(equation_rank)
        and 0 < equation_rank <= root_context
    ):
        raise StateContractError(
            RejectCode.INVALID_CORE_CONTEXT,
            "root must be 1 mod 24 and equation rank must lie in [1,p]",
        )
    mark_kind, mark_digest = _validate_mark(
        raw["mark"], root_context, equation_rank
    )
    terminal_digest = _validate_terminal_first(raw["terminal_first"])
    facts = _validate_facts(raw["facts"], root_context, mark_kind)
    facts_digest = canonical_digest_v1(dict(facts))
    source_digest = _validate_source_receipt(
        raw["source_receipt"], raw, facts_digest, terminal_digest
    )
    state_id = _expect_string(
        raw["state_id"], RejectCode.STATE_ID_MISMATCH, "state_id"
    )
    expected_state_id = build_state_id_v1(raw)
    if state_id != expected_state_id:
        raise StateContractError(
            RejectCode.STATE_ID_MISMATCH,
            f"state_id does not replay; expected {expected_state_id}",
        )
    return VerifiedSelectorHeaderV1(
        state_id=state_id,
        queue_gate=raw["queue_gate"],
        producer_id=producer_id,
        branch_id=branch_id,
        parent_state_id=raw["parent_state_id"],
        root_context=root_context,
        equation_rank=equation_rank,
        mark_kind=mark_kind,
        mark_receipt_digest=mark_digest,
        terminal_first_digest=terminal_digest,
        source_receipt_digest=source_digest,
        facts_digest=facts_digest,
        facts=facts,
    )


def _ordinary(header: VerifiedSelectorHeaderV1) -> bool:
    return header.mark_kind == ROOT_SOL


def _family_predicates_v1() -> tuple[FamilyPredicateV1, ...]:
    """Return the frozen persistent-owner precedence.

    ``initial_core_root`` is an initializer input and ``direct_terminal_leaf``
    is removed by terminal-first.  They are boundary dispositions, not
    persistent queue owners.  The frozen frontier owners plus the two wave1
    protocol/height refinements appear below in a stable order.
    """

    def fact(name: str) -> Callable[[VerifiedSelectorHeaderV1], Any]:
        # Direct shape-controls may construct a header without first passing
        # the extractor. Missing v1 grammar fields must fail predicates rather
        # than raising KeyError or becoming an implicit default.
        return lambda header: header.facts.get(name)

    phase = fact("major_phase")
    protocol = fact("type_i_protocol")
    provenance = fact("provenance_kind")
    support = fact("support_A")
    root_k = fact("proper_root_k")

    return (
        FamilyPredicateV1(
            "generic_nontrivial_marked_state",
            lambda h: h.mark_kind == NONTRIVIAL_MARK
            and phase(h) == "GENERIC_MARKED"
            and provenance(h) == "GENERIC_MARKED",
        ),
        FamilyPredicateV1(
            "type_ii_relation_f_endpoint",
            lambda h: _ordinary(h)
            and phase(h) == "TYPEII_REL"
            and h.facts["endpoint_fiber"] == "F",
        ),
        FamilyPredicateV1(
            "type_ii_relation_g_endpoint",
            lambda h: _ordinary(h)
            and phase(h) == "TYPEII_G_HANDOFF"
            and h.facts["endpoint_fiber"] == "G",
        ),
        FamilyPredicateV1(
            "h4_non_v1_branch_or_descendant",
            lambda h: _ordinary(h)
            and phase(h) == "TYPEI"
            and protocol(h) == "CHARGED"
            and provenance(h) == "H4_RESIDUAL",
        ),
        FamilyPredicateV1(
            "c8_terminal_first_surviving_parent",
            lambda h: _ordinary(h)
            and phase(h) == "TYPEI"
            and protocol(h) == "CHARGED"
            and provenance(h) == "C8_PARENT",
        ),
        FamilyPredicateV1(
            "type_i_c2_19_macro_target",
            lambda h: _ordinary(h)
            and phase(h) == "TYPEI"
            and protocol(h) == "CHARGED"
            and provenance(h) == "C2_19_MACRO",
        ),
        FamilyPredicateV1(
            "proper_root_high_endpoint",
            lambda h: _ordinary(h)
            and phase(h) == "TYPEI"
            and protocol(h) == "CHARGED"
            and provenance(h) == "PROPER_ROOT"
            and h.facts["proper_root_height_class"] == "HIGH",
        ),
        FamilyPredicateV1(
            "proper_root_stutter_k_one",
            lambda h: _ordinary(h)
            and phase(h) == "TYPEI"
            and protocol(h) == "CHARGED"
            and provenance(h) == "PROPER_ROOT"
            and h.facts["proper_root_height_class"] == "LOW"
            and root_k(h) == 1,
        ),
        FamilyPredicateV1(
            "proper_root_stutter_k_gt_one",
            lambda h: _ordinary(h)
            and phase(h) == "TYPEI"
            and protocol(h) == "CHARGED"
            and provenance(h) == "PROPER_ROOT"
            and h.facts["proper_root_height_class"] == "LOW"
            and _is_plain_int(root_k(h))
            and root_k(h) > 1,
        ),
        FamilyPredicateV1(
            "type_i_absorb_marked_residual",
            lambda h: _ordinary(h)
            and phase(h) == "TYPEI"
            and protocol(h) == "ABSORB"
            and provenance(h) == "MARKED_ABSORB"
            and not h.facts["is_overflow"]
            and h.facts["chart_R"] < h.root_context,
        ),
        FamilyPredicateV1(
            "type_i_a_one_overflow",
            lambda h: _ordinary(h)
            and phase(h) == "TYPEI"
            and protocol(h) == "CHARGED"
            and h.facts["is_overflow"]
            and support(h) == 1
            and _is_plain_int(h.facts["overflow_d"])
            and 1 <= h.facts["overflow_d"] < h.root_context,
        ),
        FamilyPredicateV1(
            "type_i_high_support_sink",
            lambda h: _ordinary(h)
            and phase(h) == "TYPEI"
            and protocol(h) == "CHARGED"
            and h.facts["is_overflow"]
            and _is_plain_int(support(h))
            and support(h) > (h.root_context - 1) ** 2 // 4
            and h.facts["sink_scc_receipt"],
        ),
        FamilyPredicateV1(
            "type_i_low_support_persistent_overflow",
            lambda h: _ordinary(h)
            and phase(h) == "TYPEI"
            and protocol(h) == "CHARGED"
            and h.facts["is_overflow"]
            and h.facts["same_chart_promotion_receipt"]
            and _is_plain_int(support(h))
            and _is_plain_int(h.facts["carrier_M"])
            and h.facts["carrier_M"] % support(h) == 0
            and h.facts["carrier_M"] // support(h) >= 2,
        ),
        FamilyPredicateV1(
            "type_i_a_gt_one_overflow_residual",
            lambda h: _ordinary(h)
            and phase(h) == "TYPEI"
            and protocol(h) == "CHARGED"
            and h.facts["is_overflow"]
            and _is_plain_int(support(h))
            and support(h) > 1,
        ),
        FamilyPredicateV1(
            "type_i_full_carrier_post_g",
            lambda h: _ordinary(h)
            and phase(h) == "TYPEI"
            and protocol(h) == "CHARGED"
            and provenance(h) == "FULL_CARRIER_POST_G"
            and h.facts["full_carrier_scope"],
        ),
    )


FAMILY_PREDICATES_V1 = _family_predicates_v1()
FAMILY_PRECEDENCE_V1 = tuple(item.family_id for item in FAMILY_PREDICATES_V1)

_OVERFLOW_SPECIALIZATIONS = frozenset(
    {
        "type_i_a_one_overflow",
        "type_i_high_support_sink",
        "type_i_low_support_persistent_overflow",
        "type_i_a_gt_one_overflow_residual",
    }
)

_LINEAGE_OVERFLOW_REFINEMENTS = {
    "c8_terminal_first_surviving_parent": _OVERFLOW_SPECIALIZATIONS,
    "proper_root_high_endpoint": frozenset(
        {"type_i_high_support_sink", "type_i_a_gt_one_overflow_residual"}
    ),
    "proper_root_stutter_k_one": frozenset(
        {"type_i_high_support_sink", "type_i_a_gt_one_overflow_residual"}
    ),
    "proper_root_stutter_k_gt_one": frozenset(
        {"type_i_high_support_sink", "type_i_a_gt_one_overflow_residual"}
    ),
}


def _pair(left: str, right: str) -> frozenset[str]:
    return frozenset({left, right})


ALLOWED_FAMILY_OVERLAPS_V1 = frozenset(
    {
        _pair(left, right)
        for left in _OVERFLOW_SPECIALIZATIONS
        for right in _OVERFLOW_SPECIALIZATIONS
        if left != right
    }
    | {
        _pair(lineage, overflow)
        for lineage, allowed_overflows in _LINEAGE_OVERFLOW_REFINEMENTS.items()
        for overflow in allowed_overflows
    }
)


def _all_pairs(values: Sequence[str]) -> Iterable[frozenset[str]]:
    for left_index, left in enumerate(values):
        for right in values[left_index + 1 :]:
            yield _pair(left, right)


def owner_digest_v1(
    header: VerifiedSelectorHeaderV1,
    owner: str,
    matched_families: Sequence[str],
    precedence_index: int,
) -> str:
    payload = {
        "contract_id": CONTRACT_ID,
        "schema_version": STATE_SCHEMA_VERSION,
        "state_id": header.state_id,
        "facts_digest": header.facts_digest,
        "owner": owner,
        "matched_families": list(matched_families),
        "precedence_index": precedence_index,
    }
    return "owner:" + canonical_digest_v1(payload)


def classify_selector_owner_v1(
    header: VerifiedSelectorHeaderV1,
    predicates: Sequence[FamilyPredicateV1] = FAMILY_PREDICATES_V1,
    allowed_overlaps: frozenset[frozenset[str]] = ALLOWED_FAMILY_OVERLAPS_V1,
) -> OwnerClassificationV1:
    """Classify a previously extracted header using fail-closed precedence."""

    ids = tuple(item.family_id for item in predicates)
    if len(ids) != len(set(ids)):
        raise StateContractError(
            RejectCode.FAMILY_ILLEGAL_OVERLAP, "family registry has duplicate IDs"
        )
    matches = tuple(item.family_id for item in predicates if item.predicate(header))
    if not matches:
        raise StateContractError(
            RejectCode.FAMILY_NO_MATCH,
            "verified header matches no persistent family predicate",
        )
    illegal = [pair for pair in _all_pairs(matches) if pair not in allowed_overlaps]
    if illegal:
        readable = sorted(sorted(pair) for pair in illegal)
        raise StateContractError(
            RejectCode.FAMILY_ILLEGAL_OVERLAP,
            f"unexpected predicate overlap {readable}",
        )
    index_by_id = {family_id: index for index, family_id in enumerate(ids)}
    owner = min(matches, key=index_by_id.__getitem__)
    index = index_by_id[owner]
    return OwnerClassificationV1(
        owner=owner,
        matched_families=matches,
        precedence_index=index,
        owner_digest=owner_digest_v1(header, owner, matches, index),
    )


def verify_owner_digest_v1(
    header: VerifiedSelectorHeaderV1,
    classification: OwnerClassificationV1,
    claimed_digest: str,
) -> None:
    expected = owner_digest_v1(
        header,
        classification.owner,
        classification.matched_families,
        classification.precedence_index,
    )
    if claimed_digest != expected:
        raise StateContractError(
            RejectCode.OWNER_DIGEST_MISMATCH, "owner digest does not replay"
        )


def _admit_or_raise(
    raw_state: Mapping[str, Any],
    registered_producers: Mapping[str, ProducerRuleV1],
) -> tuple[VerifiedSelectorHeaderV1, OwnerClassificationV1]:
    header = extract_verified_selector_header_v1(raw_state, registered_producers)
    classification = classify_selector_owner_v1(header)
    rule = registered_producers[header.producer_id]
    if classification.owner not in rule.target_owners:
        raise StateContractError(
            RejectCode.PRODUCER_TARGET_OWNER_NOT_DECLARED,
            f"{header.producer_id!r} does not declare target owner {classification.owner!r}",
        )
    return header, classification


def reject_before_persistent_queue_v1(
    raw_state: Mapping[str, Any],
    registered_producers: Mapping[str, ProducerRuleV1],
) -> QueueAdmissionDecisionV1:
    """The sole v1 queue boundary: accept or return one stable reject code."""

    try:
        header, classification = _admit_or_raise(raw_state, registered_producers)
    except StateContractError as exc:
        state_id = raw_state.get("state_id") if isinstance(raw_state, Mapping) else None
        return QueueAdmissionDecisionV1(
            accepted=False,
            reason_code=exc.code,
            detail=exc.detail,
            state_id=state_id if isinstance(state_id, str) else None,
        )
    return QueueAdmissionDecisionV1(
        accepted=True,
        reason_code=RejectCode.ACCEPT,
        detail="header, owner, producer target declaration and receipts replayed",
        state_id=header.state_id,
        owner=classification.owner,
        matched_families=classification.matched_families,
        owner_digest=classification.owner_digest,
    )


def verify_persistent_trace_v1(
    raw_states: Sequence[Mapping[str, Any]],
    registered_producers: Mapping[str, ProducerRuleV1],
) -> TraceInductionReceiptV1:
    """Replay one finite initializer/successor trace in topological order."""

    if not raw_states:
        raise StateContractError(RejectCode.TRACE_ROOT_ORDER, "trace is empty")
    admitted: dict[str, OwnerClassificationV1] = {}
    root_context: int | None = None
    owners: list[str] = []
    base_steps = 0
    successor_steps = 0
    for index, raw in enumerate(raw_states):
        header, classification = _admit_or_raise(raw, registered_producers)
        if header.state_id in admitted:
            raise StateContractError(
                RejectCode.DUPLICATE_STATE_ID, f"duplicate {header.state_id}"
            )
        if root_context is None:
            root_context = header.root_context
        elif header.root_context != root_context:
            raise StateContractError(
                RejectCode.TRACE_ROOT_ORDER, "one trace cannot mix root contexts"
            )
        rule = registered_producers[header.producer_id]
        if header.queue_gate == ROOT_INITIALIZER_OUTPUT:
            if index != 0 or base_steps:
                raise StateContractError(
                    RejectCode.TRACE_ROOT_ORDER,
                    "the unique initializer output must be the first trace item",
                )
            base_steps += 1
        else:
            parent_id = header.parent_state_id
            if parent_id not in admitted:
                raise StateContractError(
                    RejectCode.PARENT_NOT_REACHABLE,
                    f"parent {parent_id!r} was not admitted earlier",
                )
            parent_owner = admitted[parent_id].owner
            if parent_owner not in rule.source_owners:
                raise StateContractError(
                    RejectCode.PRODUCER_SOURCE_OWNER_NOT_DECLARED,
                    f"{header.producer_id!r} does not declare source owner {parent_owner!r}",
                )
            successor_steps += 1
        admitted[header.state_id] = classification
        owners.append(classification.owner)
    assert root_context is not None
    return TraceInductionReceiptV1(
        root_context=root_context,
        admitted_state_ids=tuple(admitted),
        owners=tuple(owners),
        base_steps=base_steps,
        successor_steps=successor_steps,
    )


__all__ = [
    "ADMITTED_SUCCESSOR",
    "ALLOWED_FAMILY_OVERLAPS_V1",
    "CONTRACT_ID",
    "FAMILY_PREDICATES_V1",
    "FAMILY_PRECEDENCE_V1",
    "FamilyPredicateV1",
    "INITIALIZER_RECEIPT_SCHEMA_ID",
    "MARK_SCHEMA_ID",
    "NONTRIVIAL_MARK",
    "ProducerRuleV1",
    "QUEUE_GATES",
    "ROOT_INITIALIZER_OUTPUT",
    "ROOT_SOL",
    "RejectCode",
    "STATE_SCHEMA_ID",
    "STATE_SCHEMA_VERSION",
    "SUCCESSOR_RECEIPT_SCHEMA_ID",
    "StateContractError",
    "TERMINAL_FIRST_SCHEMA_ID",
    "T5_TICKETS",
    "TraceInductionReceiptV1",
    "VerifiedSelectorHeaderV1",
    "build_state_id_v1",
    "canonical_digest_v1",
    "classify_selector_owner_v1",
    "extract_verified_selector_header_v1",
    "owner_digest_v1",
    "reject_before_persistent_queue_v1",
    "seal_receipt_v1",
    "verify_owner_digest_v1",
    "verify_persistent_trace_v1",
]
