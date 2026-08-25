#!/usr/bin/env python3
"""Exclusive producer, projection, admission and queue runtime for T6 v1.

This module freezes the shared protocol used by the F2/F3 wave.  It does not
claim that any mathematical producer is total.  A branch becomes executable
only after the coordinator registers its implementation, projector, terminal
schedule and proof evidence.  Producer output never carries owner, family or
recursive authority; those are recomputed by the existing non-circular state
contract before the sole queue mutation point is reached.
"""

from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import sys
from types import MappingProxyType
from typing import Any, Callable, Mapping, Sequence


SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import t6_persistent_selector_state_v1 as state_contract  # noqa: E402


RUNTIME_ID = "t6_persistent_selector_runtime_v1"
RUNTIME_VERSION = 1

PHASE_RANKS = MappingProxyType(
    {
        "TYPEII_REL": 4,
        "TYPEII_G_HANDOFF": 3,
        "TYPEI": 2,
        "GENERIC_MARKED": 1,
    }
)
PROTOCOL_RANKS = MappingProxyType(
    {"CHARGED": 4, "PRE": 3, "ABSORB": 2, "RESET": 1}
)

IDENTITY_MARK = "IDENTITY_MARK"
LOWER_EQUATION_MARK = "LOWER_EQUATION_MARK"
MARK_BEHAVIORS = frozenset({IDENTITY_MARK, LOWER_EQUATION_MARK})

FORBIDDEN_CANDIDATE_KEYS = frozenset(
    {
        "owner",
        "owner_digest",
        "family",
        "family_id",
        "selector_family_id",
        "normal_form",
        "normalized_state",
        "normalizer_result",
        "recursive_edge_eligible",
        "persistent_queue",
        "selector_status",
    }
)


class RuntimeRejectCode(str, Enum):
    ACCEPT = "ACCEPT"
    UNKNOWN_PRODUCER = "UNKNOWN_PRODUCER"
    UNKNOWN_BRANCH = "UNKNOWN_BRANCH"
    SOURCE_NOT_ADMITTED = "SOURCE_NOT_ADMITTED"
    SOURCE_OWNER_NOT_ALLOWED = "SOURCE_OWNER_NOT_ALLOWED"
    PRODUCER_RESULT_INVALID = "PRODUCER_RESULT_INVALID"
    BRANCH_GUARD_MISS = "BRANCH_GUARD_MISS"
    CANDIDATE_AUTHORITY_FIELD = "CANDIDATE_AUTHORITY_FIELD"
    TERMINAL_ONLY_CANDIDATE = "TERMINAL_ONLY_CANDIDATE"
    PROJECTOR_MISSING = "PROJECTOR_MISSING"
    PROJECTOR_OUTPUT_INVALID = "PROJECTOR_OUTPUT_INVALID"
    TERMINAL_SCHEDULE_MISSING = "TERMINAL_SCHEDULE_MISSING"
    TERMINAL_RESULT_INVALID = "TERMINAL_RESULT_INVALID"
    TERMINAL_VERIFIER_MISSING = "TERMINAL_VERIFIER_MISSING"
    TERMINAL_VERIFICATION_FAILED = "TERMINAL_VERIFICATION_FAILED"
    MARK_BEHAVIOR_INVALID = "MARK_BEHAVIOR_INVALID"
    T5_DESCRIPTOR_INVALID = "T5_DESCRIPTOR_INVALID"
    T5_TICKET_INVALID = "T5_TICKET_INVALID"
    TARGET_ADMISSION_REJECTED = "TARGET_ADMISSION_REJECTED"
    DUPLICATE_STATE = "DUPLICATE_STATE"
    DEAD_END = "DEAD_END"


class RuntimeContractError(ValueError):
    def __init__(self, code: RuntimeRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


@dataclass(frozen=True)
class T5StateDescriptorV1:
    induction_rank: int
    major_phase: str
    type_i_protocol: str | None = None
    eta_p: int = 0
    pre_a: int | None = None
    absorb_m: int | None = None
    absorb_r_epsilon: int | None = None
    reset_carrier: int | None = None


@dataclass(frozen=True)
class TargetProjectionV1:
    root_context: int
    equation_rank: int
    facts: Mapping[str, Any]
    t5: T5StateDescriptorV1
    mark_behavior: str


@dataclass(frozen=True)
class TransitionValidationV1:
    """Independent branch validation before common E3 admission.

    The producer cannot construct this receipt itself.  A separately
    registered validator must bind the source, branch and canonical
    projection and replay the mathematical E1--E4 obligations.
    """

    source_state_id: str
    producer_id: str
    branch_id: str
    projection_digest: str
    E1: bool
    E2: bool
    E3_pre_admission: bool
    E4: bool
    evidence_ids: tuple[str, ...]


@dataclass(frozen=True)
class CandidateTransitionV1:
    producer_id: str
    branch_id: str
    witness_payload: Mapping[str, Any]
    ticket_type: str


@dataclass(frozen=True)
class DispatchEntryV1:
    producer_id: str
    branch_id: str


@dataclass(frozen=True)
class TerminalDispatchEntryV1:
    producer_id: str
    branch_id: str


@dataclass(frozen=True)
class ProducedCandidateV1:
    candidate: CandidateTransitionV1
    execution_id: str
    dispatch_receipt: Mapping[str, Any]


@dataclass(frozen=True)
class GuardMissV1:
    reason_code: str
    detail: str


@dataclass(frozen=True)
class TerminalDraftV1:
    verifier_id: str
    certificate_payload: Mapping[str, Any]
    lift_evidence_id: str


ProducerOutputV1 = CandidateTransitionV1 | GuardMissV1 | TerminalDraftV1


@dataclass(frozen=True)
class TerminalMissV1:
    schedule_id: str
    scope: str
    evidence_id: str


@dataclass(frozen=True)
class VerifiedTerminalV1:
    source_state_id: str
    producer_id: str
    branch_id: str
    verifier_id: str
    certificate_id: str
    lift_evidence_id: str
    certificate_payload: Mapping[str, Any]
    dispatch_receipt: Mapping[str, Any] | None = None


TargetTerminalOutputV1 = TerminalMissV1 | TerminalDraftV1


@dataclass(frozen=True)
class BranchRegistrationV1:
    branch_id: str
    source_owners: frozenset[str]
    target_owners: frozenset[str]
    evidence_refs: tuple[str, ...]
    allowed_tickets: frozenset[str]
    projector_id: str
    transition_validator_id: str
    source_terminal_schedule_id: str
    target_terminal_schedule_id: str
    terminal_verifier_ids: frozenset[str] = frozenset()

    def __post_init__(self) -> None:
        if not self.branch_id:
            raise ValueError("branch_id must be nonempty")
        if not self.source_owners or not self.target_owners:
            raise ValueError("successor branch requires source and target owners")
        if not self.evidence_refs or any(not item for item in self.evidence_refs):
            raise ValueError("branch requires nonempty proof evidence references")
        if not self.allowed_tickets or not self.allowed_tickets <= state_contract.T5_TICKETS:
            raise ValueError("branch has invalid T5 ticket allowlist")
        if not (
            self.projector_id
            and self.transition_validator_id
            and self.source_terminal_schedule_id
            and self.target_terminal_schedule_id
        ):
            raise ValueError(
                "branch requires projector, transition validator and both terminal schedules"
            )


@dataclass(frozen=True)
class TerminalOnlyBranchRegistrationV1:
    """A source branch that can only return a verified terminal or a miss."""

    branch_id: str
    source_owners: frozenset[str]
    evidence_refs: tuple[str, ...]
    source_terminal_schedule_id: str
    terminal_verifier_ids: frozenset[str]

    def __post_init__(self) -> None:
        if not self.branch_id or not self.source_owners:
            raise ValueError("terminal-only branch needs an ID and source owners")
        if not self.evidence_refs or any(not item for item in self.evidence_refs):
            raise ValueError("terminal-only branch needs proof evidence")
        if not self.source_terminal_schedule_id:
            raise ValueError("terminal-only branch needs a source schedule")
        if not self.terminal_verifier_ids:
            raise ValueError("terminal-only branch needs terminal verifiers")


@dataclass(frozen=True)
class TerminalOnlyProducerRegistrationV1:
    """Registration metadata deliberately excluded from persistent rules."""

    producer_id: str
    implementation_ref: str
    branches: tuple[TerminalOnlyBranchRegistrationV1, ...]

    def __post_init__(self) -> None:
        if not self.producer_id or not self.implementation_ref or not self.branches:
            raise ValueError("terminal-only producer registration is incomplete")
        branch_ids = tuple(branch.branch_id for branch in self.branches)
        if len(branch_ids) != len(set(branch_ids)):
            raise ValueError("terminal-only producer has duplicate branch IDs")

    def branch(self, branch_id: str) -> TerminalOnlyBranchRegistrationV1:
        for branch in self.branches:
            if branch.branch_id == branch_id:
                return branch
        raise RuntimeContractError(
            RuntimeRejectCode.UNKNOWN_BRANCH,
            f"{self.producer_id!r} has no terminal-only branch {branch_id!r}",
        )


@dataclass(frozen=True)
class ProducerRegistrationV1:
    producer_id: str
    implementation_ref: str
    branches: tuple[BranchRegistrationV1, ...]
    queue_gate: str = state_contract.ADMITTED_SUCCESSOR

    def __post_init__(self) -> None:
        if not self.producer_id or not self.implementation_ref or not self.branches:
            raise ValueError("producer registration is incomplete")
        ids = tuple(branch.branch_id for branch in self.branches)
        if len(ids) != len(set(ids)):
            raise ValueError("producer has duplicate branch IDs")
        if self.queue_gate != state_contract.ADMITTED_SUCCESSOR:
            raise ValueError("runtime producer must use ADMITTED_SUCCESSOR")

    def branch(self, branch_id: str) -> BranchRegistrationV1:
        for branch in self.branches:
            if branch.branch_id == branch_id:
                return branch
        raise RuntimeContractError(
            RuntimeRejectCode.UNKNOWN_BRANCH,
            f"{self.producer_id!r} has no branch {branch_id!r}",
        )


@dataclass(frozen=True)
class InitializerRegistrationV1:
    producer_id: str
    branch_ids: frozenset[str]
    target_owners: frozenset[str]


@dataclass(frozen=True)
class SourceExecutionContextV1:
    state_id: str
    owner: str
    owner_digest: str
    header: state_contract.VerifiedSelectorHeaderV1
    potential: tuple[int, int, int, int, int, int, int]
    raw_state: Mapping[str, Any]


@dataclass(frozen=True)
class RuntimeQueueItemV1:
    raw_state: Mapping[str, Any]
    owner: str
    owner_digest: str
    t5_descriptor: T5StateDescriptorV1
    potential_receipt: Mapping[str, Any]
    transition_receipt: Mapping[str, Any] | None

    @property
    def state_id(self) -> str:
        return str(self.raw_state["state_id"])


@dataclass(frozen=True)
class VerifiedSuccessorV1:
    source_state_id: str
    target_state_id: str
    producer_id: str
    branch_id: str
    target_owner: str
    owner_digest: str
    t5_ticket_receipt: Mapping[str, Any]
    transition_receipt: Mapping[str, Any]


@dataclass(frozen=True)
class RuntimeDecisionV1:
    accepted: bool
    reason_code: RuntimeRejectCode
    detail: str
    successor: VerifiedSuccessorV1 | None = None
    terminal: VerifiedTerminalV1 | None = None


ProducerExecutorV1 = Callable[[SourceExecutionContextV1, str], ProducerOutputV1]
ProjectorV1 = Callable[
    [SourceExecutionContextV1, CandidateTransitionV1], TargetProjectionV1
]
TransitionValidatorV1 = Callable[
    [SourceExecutionContextV1, CandidateTransitionV1, TargetProjectionV1],
    TransitionValidationV1,
]
SourceTerminalSchedulerV1 = Callable[
    [SourceExecutionContextV1], TargetTerminalOutputV1
]
TargetTerminalSchedulerV1 = Callable[
    [TargetProjectionV1, Mapping[str, Any]], TargetTerminalOutputV1
]
TerminalVerifierV1 = Callable[
    [SourceExecutionContextV1, Mapping[str, Any], str], bool
]


def canonical_digest_v1(payload: Any) -> str:
    try:
        encoded = json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
            allow_nan=False,
        ).encode("ascii")
    except (TypeError, ValueError) as exc:
        raise RuntimeContractError(
            RuntimeRejectCode.PRODUCER_RESULT_INVALID,
            f"payload is not canonical JSON: {exc}",
        ) from exc
    return hashlib.sha256(encoded).hexdigest()


def seal_v1(payload: Mapping[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(dict(payload))
    result.pop("digest", None)
    result["digest"] = canonical_digest_v1(result)
    return result


def _positive_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def _nonnegative_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def _reject_candidate_authority(value: Any, path: str = "candidate") -> None:
    if isinstance(value, Mapping):
        for key, child in value.items():
            if key in FORBIDDEN_CANDIDATE_KEYS:
                raise RuntimeContractError(
                    RuntimeRejectCode.CANDIDATE_AUTHORITY_FIELD,
                    f"{path}.{key} cannot grant persistence",
                )
            _reject_candidate_authority(child, f"{path}.{key}")
    elif isinstance(value, (list, tuple)):
        for index, child in enumerate(value):
            _reject_candidate_authority(child, f"{path}[{index}]")


def compute_t5_potential_v1(
    *,
    descriptor: T5StateDescriptorV1,
    facts: Mapping[str, Any],
    root_context: int,
    equation_rank: int,
) -> tuple[int, int, int, int, int, int, int]:
    """Recompute the frozen T5 N^7 potential from semantic fields."""

    if not (
        _positive_int(descriptor.induction_rank)
        and descriptor.induction_rank == equation_rank
        and descriptor.major_phase in PHASE_RANKS
        and facts.get("major_phase") == descriptor.major_phase
        and facts.get("type_i_protocol") == descriptor.type_i_protocol
    ):
        raise RuntimeContractError(
            RuntimeRejectCode.T5_DESCRIPTOR_INVALID,
            "induction rank or major phase does not match the target projection",
        )

    phase_rank = PHASE_RANKS[descriptor.major_phase]
    protocol_rank = 0
    local: tuple[int, int, int, int]
    if descriptor.major_phase == "TYPEII_REL":
        q_value = facts.get("relation_q")
        if not _positive_int(q_value) or descriptor.type_i_protocol is not None:
            raise RuntimeContractError(
                RuntimeRejectCode.T5_DESCRIPTOR_INVALID,
                "TYPEII_REL requires q and no Type-I protocol",
            )
        local = (q_value, 0, 0, 0)
    elif descriptor.major_phase in {"TYPEII_G_HANDOFF", "GENERIC_MARKED"}:
        if descriptor.type_i_protocol is not None:
            raise RuntimeContractError(
                RuntimeRejectCode.T5_DESCRIPTOR_INVALID,
                "non-Type-I phase cannot carry a Type-I protocol",
            )
        local = (0, 0, 0, 0)
    else:
        protocol = descriptor.type_i_protocol
        if protocol not in PROTOCOL_RANKS:
            raise RuntimeContractError(
                RuntimeRejectCode.T5_DESCRIPTOR_INVALID,
                "TYPEI requires a frozen protocol",
            )
        protocol_rank = PROTOCOL_RANKS[protocol]
        if protocol == "CHARGED":
            support = facts.get("support_A")
            chart_k = facts.get("chart_K")
            if not (
                _positive_int(support)
                and _positive_int(chart_k)
                and chart_k % support == 0
                and _nonnegative_int(descriptor.eta_p)
                and facts.get("t5_eta_p") == descriptor.eta_p
            ):
                raise RuntimeContractError(
                    RuntimeRejectCode.T5_DESCRIPTOR_INVALID,
                    "CHARGED requires A|K and nonnegative eta_p",
                )
            b_p = (root_context - 1) ** 2 // 4
            local = (
                b_p // support,
                chart_k // support,
                descriptor.eta_p,
                0,
            )
        elif protocol == "PRE":
            if not (
                _positive_int(descriptor.pre_a)
                and facts.get("pre_a") == descriptor.pre_a
            ):
                raise RuntimeContractError(
                    RuntimeRejectCode.T5_DESCRIPTOR_INVALID,
                    "PRE requires positive a",
                )
            local = (descriptor.pre_a, 0, 0, 0)
        elif protocol == "ABSORB":
            chart_r = facts.get("chart_R")
            if not (
                _positive_int(chart_r)
                and _positive_int(descriptor.absorb_m)
                and _nonnegative_int(descriptor.absorb_r_epsilon)
                and facts.get("absorb_m") == descriptor.absorb_m
                and facts.get("absorb_r_epsilon")
                == descriptor.absorb_r_epsilon
            ):
                raise RuntimeContractError(
                    RuntimeRejectCode.T5_DESCRIPTOR_INVALID,
                    "ABSORB requires R,m,r_epsilon",
                )
            local = (
                chart_r,
                descriptor.absorb_m,
                descriptor.absorb_r_epsilon,
                0,
            )
        else:
            if not (
                _positive_int(descriptor.reset_carrier)
                and facts.get("reset_carrier") == descriptor.reset_carrier
            ):
                raise RuntimeContractError(
                    RuntimeRejectCode.T5_DESCRIPTOR_INVALID,
                    "RESET requires a positive carrier",
                )
            local = (descriptor.reset_carrier, 0, 0, 0)
    return (
        descriptor.induction_rank,
        phase_rank,
        protocol_rank,
        *local,
    )


def make_potential_receipt_v1(
    state_id: str,
    potential: Sequence[int],
) -> dict[str, Any]:
    if len(potential) != 7 or any(not _nonnegative_int(item) for item in potential):
        raise RuntimeContractError(
            RuntimeRejectCode.T5_DESCRIPTOR_INVALID,
            "potential must be an N^7 tuple",
        )
    return seal_v1(
        {
            "schema_id": "t5_n7_potential_receipt_v1",
            "schema_version": 1,
            "state_id": state_id,
            "coordinates": list(potential),
        }
    )


def verify_potential_receipt_v1(
    receipt: Mapping[str, Any], state_id: str, potential: Sequence[int]
) -> None:
    expected = make_potential_receipt_v1(state_id, potential)
    if dict(receipt) != expected:
        raise RuntimeContractError(
            RuntimeRejectCode.T5_DESCRIPTOR_INVALID,
            "potential receipt does not replay",
        )


def verify_t5_ticket_v1(
    ticket_type: str,
    source: Sequence[int],
    target: Sequence[int],
) -> None:
    if (
        ticket_type not in state_contract.T5_TICKETS
        or len(source) != 7
        or len(target) != 7
        or any(not _nonnegative_int(item) for item in (*source, *target))
    ):
        raise RuntimeContractError(
            RuntimeRejectCode.T5_TICKET_INVALID,
            "ticket type or potential shape is invalid",
        )
    source_tuple = tuple(source)
    target_tuple = tuple(target)
    if not source_tuple > target_tuple:
        raise RuntimeContractError(
            RuntimeRejectCode.T5_TICKET_INVALID,
            "target does not strictly decrease the N^7 potential",
        )
    if ticket_type == "OUTER_RANK_DROP":
        valid = target_tuple[0] < source_tuple[0]
    elif ticket_type == "PHASE_DROP":
        valid = (
            target_tuple[0] == source_tuple[0]
            and target_tuple[1:3] < source_tuple[1:3]
        )
    else:
        valid = (
            target_tuple[:3] == source_tuple[:3]
            and target_tuple[3:] < source_tuple[3:]
        )
    if not valid:
        raise RuntimeContractError(
            RuntimeRejectCode.T5_TICKET_INVALID,
            f"{ticket_type} does not match the first decreasing coordinate",
        )


def make_t5_ticket_receipt_v1(
    *,
    source_state_id: str,
    target_state_id: str,
    ticket_type: str,
    source: Sequence[int],
    target: Sequence[int],
) -> dict[str, Any]:
    verify_t5_ticket_v1(ticket_type, source, target)
    return seal_v1(
        {
            "schema_id": "t5_n7_ticket_receipt_v1",
            "schema_version": 1,
            "source_state_id": source_state_id,
            "target_state_id": target_state_id,
            "ticket_type": ticket_type,
            "source": list(source),
            "target": list(target),
        }
    )


class PersistentSelectorRuntimeV1:
    """One authoritative path from admitted source to queue mutation."""

    def __init__(
        self,
        *,
        initializer: InitializerRegistrationV1,
        producers: Sequence[ProducerRegistrationV1],
        executors: Mapping[str, ProducerExecutorV1],
        projectors: Mapping[str, ProjectorV1],
        transition_validators: Mapping[str, TransitionValidatorV1],
        source_terminal_schedulers: Mapping[str, SourceTerminalSchedulerV1],
        target_terminal_schedulers: Mapping[str, TargetTerminalSchedulerV1],
        terminal_verifiers: Mapping[str, TerminalVerifierV1],
        dispatch_precedence: Mapping[str, Sequence[DispatchEntryV1]],
        terminal_producers: Sequence[TerminalOnlyProducerRegistrationV1] = (),
        terminal_executors: Mapping[str, ProducerExecutorV1] | None = None,
        terminal_dispatch_precedence: Mapping[
            str, Sequence[TerminalDispatchEntryV1]
        ]
        | None = None,
    ) -> None:
        if len({item.producer_id for item in producers}) != len(producers):
            raise ValueError("duplicate producer registration")
        if len({item.producer_id for item in terminal_producers}) != len(
            terminal_producers
        ):
            raise ValueError("duplicate terminal-only producer registration")
        successor_ids = {item.producer_id for item in producers}
        terminal_ids = {item.producer_id for item in terminal_producers}
        if successor_ids & terminal_ids:
            raise ValueError("a producer ID cannot mix successor and terminal-only branches")
        self.initializer = initializer
        self.producers = MappingProxyType(
            {item.producer_id: item for item in producers}
        )
        self.executors = MappingProxyType(dict(executors))
        self.projectors = MappingProxyType(dict(projectors))
        self.transition_validators = MappingProxyType(
            dict(transition_validators)
        )
        self.source_terminal_schedulers = MappingProxyType(
            dict(source_terminal_schedulers)
        )
        self.target_terminal_schedulers = MappingProxyType(
            dict(target_terminal_schedulers)
        )
        self.terminal_verifiers = MappingProxyType(dict(terminal_verifiers))
        self.terminal_producers = MappingProxyType(
            {item.producer_id: item for item in terminal_producers}
        )
        self.terminal_executors = MappingProxyType(
            dict(terminal_executors or {})
        )
        missing_terminal_executors = terminal_ids - set(self.terminal_executors)
        if missing_terminal_executors:
            raise ValueError(
                "terminal-only producers lack executors: "
                + repr(sorted(missing_terminal_executors))
            )
        normalized_dispatch: dict[str, tuple[DispatchEntryV1, ...]] = {}
        expected_routes: set[tuple[str, str, str]] = set()
        for producer in producers:
            for branch in producer.branches:
                for owner in branch.source_owners:
                    expected_routes.add((owner, producer.producer_id, branch.branch_id))
        observed_routes: set[tuple[str, str, str]] = set()
        for owner, entries_value in dispatch_precedence.items():
            entries = tuple(entries_value)
            if not entries:
                raise ValueError(f"dispatch owner {owner!r} has no routes")
            if len(entries) != len(set(entries)):
                raise ValueError(f"dispatch owner {owner!r} has duplicate routes")
            source_schedules: set[str] = set()
            for entry in entries:
                producer = self.producers.get(entry.producer_id)
                if producer is None:
                    raise ValueError(f"unknown dispatch producer {entry.producer_id!r}")
                branch = producer.branch(entry.branch_id)
                if owner not in branch.source_owners:
                    raise ValueError(
                        f"dispatch route {entry} cannot consume owner {owner!r}"
                    )
                observed_routes.add((owner, entry.producer_id, entry.branch_id))
                source_schedules.add(branch.source_terminal_schedule_id)
            if len(source_schedules) != 1:
                raise ValueError(
                    f"all routes for owner {owner!r} must share one source terminal schedule"
                )
            normalized_dispatch[owner] = entries
        if observed_routes != expected_routes:
            missing = sorted(expected_routes - observed_routes)
            extra = sorted(observed_routes - expected_routes)
            raise ValueError(f"dispatch registry mismatch: missing={missing}, extra={extra}")
        self.dispatch_precedence = MappingProxyType(normalized_dispatch)
        terminal_dispatch = terminal_dispatch_precedence or {}
        expected_terminal_routes: set[tuple[str, str, str]] = set()
        for producer in terminal_producers:
            for branch in producer.branches:
                for owner in branch.source_owners:
                    expected_terminal_routes.add(
                        (owner, producer.producer_id, branch.branch_id)
                    )
        observed_terminal_routes: set[tuple[str, str, str]] = set()
        normalized_terminal_dispatch: dict[
            str, tuple[TerminalDispatchEntryV1, ...]
        ] = {}
        for owner, entries_value in terminal_dispatch.items():
            entries = tuple(entries_value)
            if not entries:
                raise ValueError(f"terminal dispatch owner {owner!r} has no routes")
            if len(entries) != len(set(entries)):
                raise ValueError(
                    f"terminal dispatch owner {owner!r} has duplicate routes"
                )
            schedules: set[str] = set()
            for entry in entries:
                producer = self.terminal_producers.get(entry.producer_id)
                if producer is None:
                    raise ValueError(
                        f"unknown terminal-only producer {entry.producer_id!r}"
                    )
                branch = producer.branch(entry.branch_id)
                if owner not in branch.source_owners:
                    raise ValueError(
                        f"terminal route {entry} cannot consume owner {owner!r}"
                    )
                observed_terminal_routes.add(
                    (owner, entry.producer_id, entry.branch_id)
                )
                schedules.add(branch.source_terminal_schedule_id)
            if len(schedules) != 1:
                raise ValueError(
                    f"all terminal routes for owner {owner!r} must share one source schedule"
                )
            normalized_terminal_dispatch[owner] = entries
        if observed_terminal_routes != expected_terminal_routes:
            missing = sorted(expected_terminal_routes - observed_terminal_routes)
            extra = sorted(observed_terminal_routes - expected_terminal_routes)
            raise ValueError(
                f"terminal dispatch registry mismatch: missing={missing}, extra={extra}"
            )
        self.terminal_dispatch_precedence = MappingProxyType(
            normalized_terminal_dispatch
        )
        self._queue: list[RuntimeQueueItemV1] = []
        self._known_items: dict[str, RuntimeQueueItemV1] = {}
        self._issued_candidates: dict[str, tuple[str, str]] = {}

    def producer_rules_v1(self) -> Mapping[str, state_contract.ProducerRuleV1]:
        rules: dict[str, state_contract.ProducerRuleV1] = {
            self.initializer.producer_id: state_contract.ProducerRuleV1(
                producer_id=self.initializer.producer_id,
                queue_gate=state_contract.ROOT_INITIALIZER_OUTPUT,
                branch_ids=self.initializer.branch_ids,
                source_owners=frozenset(),
                target_owners=self.initializer.target_owners,
            )
        }
        for producer in self.producers.values():
            rules[producer.producer_id] = state_contract.ProducerRuleV1(
                producer_id=producer.producer_id,
                queue_gate=state_contract.ADMITTED_SUCCESSOR,
                branch_ids=frozenset(
                    branch.branch_id for branch in producer.branches
                ),
                source_owners=frozenset().union(
                    *(branch.source_owners for branch in producer.branches)
                ),
                target_owners=frozenset().union(
                    *(branch.target_owners for branch in producer.branches)
                ),
            )
        return MappingProxyType(rules)

    def queue_snapshot_v1(self) -> tuple[RuntimeQueueItemV1, ...]:
        return tuple(self._queue)

    def _enqueue_admitted_target_v1(self, item: RuntimeQueueItemV1) -> None:
        if item.state_id in self._known_items:
            raise RuntimeContractError(
                RuntimeRejectCode.DUPLICATE_STATE,
                f"state {item.state_id} was already enqueued",
            )
        self._known_items[item.state_id] = item
        self._queue.append(item)

    def bootstrap_nonterminal_v1(
        self,
        raw_state: Mapping[str, Any],
        t5_descriptor: T5StateDescriptorV1,
    ) -> RuntimeQueueItemV1:
        rules = self.producer_rules_v1()
        decision = state_contract.reject_before_persistent_queue_v1(
            raw_state, rules
        )
        if not decision.accepted or decision.owner is None or decision.owner_digest is None:
            raise RuntimeContractError(
                RuntimeRejectCode.TARGET_ADMISSION_REJECTED,
                f"initializer target rejected: {decision.reason_code.value}",
            )
        header = state_contract.extract_verified_selector_header_v1(raw_state, rules)
        potential = compute_t5_potential_v1(
            descriptor=t5_descriptor,
            facts=header.facts,
            root_context=header.root_context,
            equation_rank=header.equation_rank,
        )
        receipt = make_potential_receipt_v1(header.state_id, potential)
        item = RuntimeQueueItemV1(
            raw_state=MappingProxyType(copy.deepcopy(dict(raw_state))),
            owner=decision.owner,
            owner_digest=decision.owner_digest,
            t5_descriptor=t5_descriptor,
            potential_receipt=MappingProxyType(receipt),
            transition_receipt=None,
        )
        self._enqueue_admitted_target_v1(item)
        return item

    def verify_source_state_v1(
        self, item: RuntimeQueueItemV1
    ) -> SourceExecutionContextV1:
        stored = self._known_items.get(item.state_id)
        if stored is None:
            raise RuntimeContractError(
                RuntimeRejectCode.SOURCE_NOT_ADMITTED,
                "source is not in the runtime admitted-state set",
            )
        if item != stored:
            raise RuntimeContractError(
                RuntimeRejectCode.SOURCE_NOT_ADMITTED,
                "source queue item differs from the runtime-enqueued record",
            )
        rules = self.producer_rules_v1()
        header = state_contract.extract_verified_selector_header_v1(
            item.raw_state, rules
        )
        classification = state_contract.classify_selector_owner_v1(header)
        state_contract.verify_owner_digest_v1(
            header, classification, item.owner_digest
        )
        if classification.owner != item.owner:
            raise RuntimeContractError(
                RuntimeRejectCode.SOURCE_NOT_ADMITTED,
                "cached source owner differs from recomputed owner",
            )
        potential = compute_t5_potential_v1(
            descriptor=item.t5_descriptor,
            facts=header.facts,
            root_context=header.root_context,
            equation_rank=header.equation_rank,
        )
        verify_potential_receipt_v1(
            item.potential_receipt, item.state_id, potential
        )
        return SourceExecutionContextV1(
            state_id=item.state_id,
            owner=item.owner,
            owner_digest=item.owner_digest,
            header=header,
            potential=potential,
            raw_state=item.raw_state,
        )

    def _verified_terminal_v1(
        self,
        *,
        source: SourceExecutionContextV1,
        producer_id: str,
        branch: BranchRegistrationV1,
        draft: TerminalDraftV1,
        dispatch_receipt: Mapping[str, Any] | None = None,
    ) -> VerifiedTerminalV1:
        if draft.verifier_id not in branch.terminal_verifier_ids:
            raise RuntimeContractError(
                RuntimeRejectCode.TERMINAL_RESULT_INVALID,
                "branch did not declare this terminal verifier",
            )
        verifier = self.terminal_verifiers.get(draft.verifier_id)
        if verifier is None:
            raise RuntimeContractError(
                RuntimeRejectCode.TERMINAL_VERIFIER_MISSING,
                f"no verifier for {draft.verifier_id!r}",
            )
        payload = copy.deepcopy(dict(draft.certificate_payload))
        if not draft.lift_evidence_id or not verifier(
            source, payload, draft.lift_evidence_id
        ):
            raise RuntimeContractError(
                RuntimeRejectCode.TERMINAL_VERIFICATION_FAILED,
                f"terminal verifier {draft.verifier_id!r} rejected payload",
            )
        certificate_id = "terminal:" + canonical_digest_v1(
            {
                "verifier_id": draft.verifier_id,
                "payload": payload,
                "lift_evidence_id": draft.lift_evidence_id,
            }
        )
        return VerifiedTerminalV1(
            source_state_id=source.state_id,
            producer_id=producer_id,
            branch_id=branch.branch_id,
            verifier_id=draft.verifier_id,
            certificate_id=certificate_id,
            lift_evidence_id=draft.lift_evidence_id,
            certificate_payload=MappingProxyType(payload),
            dispatch_receipt=(
                MappingProxyType(copy.deepcopy(dict(dispatch_receipt)))
                if dispatch_receipt is not None
                else None
            ),
        )

    def _verified_terminal_only_v1(
        self,
        *,
        source: SourceExecutionContextV1,
        producer_id: str,
        branch: TerminalOnlyBranchRegistrationV1,
        draft: TerminalDraftV1,
        dispatch_receipt: Mapping[str, Any] | None = None,
    ) -> VerifiedTerminalV1:
        if draft.verifier_id not in branch.terminal_verifier_ids:
            raise RuntimeContractError(
                RuntimeRejectCode.TERMINAL_RESULT_INVALID,
                "terminal-only branch did not declare this verifier",
            )
        verifier = self.terminal_verifiers.get(draft.verifier_id)
        if verifier is None:
            raise RuntimeContractError(
                RuntimeRejectCode.TERMINAL_VERIFIER_MISSING,
                f"no verifier for {draft.verifier_id!r}",
            )
        payload = copy.deepcopy(dict(draft.certificate_payload))
        if not draft.lift_evidence_id or not verifier(
            source, payload, draft.lift_evidence_id
        ):
            raise RuntimeContractError(
                RuntimeRejectCode.TERMINAL_VERIFICATION_FAILED,
                f"terminal verifier {draft.verifier_id!r} rejected payload",
            )
        certificate_id = "terminal:" + canonical_digest_v1(
            {
                "verifier_id": draft.verifier_id,
                "payload": payload,
                "lift_evidence_id": draft.lift_evidence_id,
            }
        )
        return VerifiedTerminalV1(
            source_state_id=source.state_id,
            producer_id=producer_id,
            branch_id=branch.branch_id,
            verifier_id=draft.verifier_id,
            certificate_id=certificate_id,
            lift_evidence_id=draft.lift_evidence_id,
            certificate_payload=MappingProxyType(payload),
            dispatch_receipt=(
                MappingProxyType(copy.deepcopy(dict(dispatch_receipt)))
                if dispatch_receipt is not None
                else None
            ),
        )

    def _project_candidate_v1(
        self,
        source: SourceExecutionContextV1,
        registration: ProducerRegistrationV1,
        branch: BranchRegistrationV1,
        candidate: CandidateTransitionV1,
    ) -> TargetProjectionV1:
        if (
            candidate.producer_id != registration.producer_id
            or candidate.branch_id != branch.branch_id
        ):
            raise RuntimeContractError(
                RuntimeRejectCode.PRODUCER_RESULT_INVALID,
                "candidate producer/branch does not match invocation",
            )
        _reject_candidate_authority(candidate.witness_payload)
        if candidate.ticket_type not in branch.allowed_tickets:
            raise RuntimeContractError(
                RuntimeRejectCode.T5_TICKET_INVALID,
                "candidate ticket is not allowed by its branch registration",
            )
        projector = self.projectors.get(branch.projector_id)
        if projector is None:
            raise RuntimeContractError(
                RuntimeRejectCode.PROJECTOR_MISSING,
                f"no target projector {branch.projector_id!r}",
            )
        projection = projector(source, candidate)
        if not isinstance(projection, TargetProjectionV1):
            raise RuntimeContractError(
                RuntimeRejectCode.PROJECTOR_OUTPUT_INVALID,
                "projector did not return TargetProjectionV1",
            )
        _reject_candidate_authority(projection.facts, "projection.facts")
        if projection.mark_behavior not in MARK_BEHAVIORS:
            raise RuntimeContractError(
                RuntimeRejectCode.MARK_BEHAVIOR_INVALID,
                f"unknown mark behavior {projection.mark_behavior!r}",
            )
        return projection

    def _target_mark_receipt_v1(
        self,
        source: SourceExecutionContextV1,
        projection: TargetProjectionV1,
        transition_id: str,
    ) -> dict[str, Any]:
        if projection.root_context != source.header.root_context:
            raise RuntimeContractError(
                RuntimeRejectCode.MARK_BEHAVIOR_INVALID,
                "runtime v1 cannot change the root context",
            )
        if projection.mark_behavior == IDENTITY_MARK:
            if projection.equation_rank != source.header.equation_rank:
                raise RuntimeContractError(
                    RuntimeRejectCode.MARK_BEHAVIOR_INVALID,
                    "identity mark requires the same equation rank",
                )
            kind = source.header.mark_kind
        else:
            if not (0 < projection.equation_rank < source.header.equation_rank):
                raise RuntimeContractError(
                    RuntimeRejectCode.MARK_BEHAVIOR_INVALID,
                    "lower-equation mark requires a strict positive rank drop",
                )
            kind = state_contract.NONTRIVIAL_MARK
        return state_contract.seal_receipt_v1(
            {
                "schema_id": state_contract.MARK_SCHEMA_ID,
                "schema_version": 1,
                "receipt_id": f"runtime-mark:{transition_id}",
                "kind": kind,
                "root_context": projection.root_context,
                "equation_rank": projection.equation_rank,
            }
        )

    def _target_terminal_miss_receipt_v1(
        self,
        branch: BranchRegistrationV1,
        projection: TargetProjectionV1,
        witness_payload: Mapping[str, Any],
    ) -> TerminalMissV1 | TerminalDraftV1:
        scheduler = self.target_terminal_schedulers.get(
            branch.target_terminal_schedule_id
        )
        if scheduler is None:
            raise RuntimeContractError(
                RuntimeRejectCode.TERMINAL_SCHEDULE_MISSING,
                f"no schedule {branch.target_terminal_schedule_id!r}",
            )
        result = scheduler(projection, witness_payload)
        if not isinstance(result, (TerminalMissV1, TerminalDraftV1)):
            raise RuntimeContractError(
                RuntimeRejectCode.TERMINAL_RESULT_INVALID,
                "target terminal scheduler returned an invalid object",
            )
        if isinstance(result, TerminalMissV1) and result.schedule_id != branch.target_terminal_schedule_id:
            raise RuntimeContractError(
                RuntimeRejectCode.TERMINAL_RESULT_INVALID,
                "terminal miss schedule does not match branch registration",
            )
        return result

    def _source_terminal_first_v1(
        self,
        *,
        source: SourceExecutionContextV1,
        producer_id: str,
        branch: BranchRegistrationV1,
    ) -> TerminalMissV1 | VerifiedTerminalV1:
        scheduler = self.source_terminal_schedulers.get(
            branch.source_terminal_schedule_id
        )
        if scheduler is None:
            raise RuntimeContractError(
                RuntimeRejectCode.TERMINAL_SCHEDULE_MISSING,
                f"no source schedule {branch.source_terminal_schedule_id!r}",
            )
        result = scheduler(source)
        if isinstance(result, TerminalDraftV1):
            return self._verified_terminal_v1(
                source=source,
                producer_id=producer_id,
                branch=branch,
                draft=result,
            )
        if not isinstance(result, TerminalMissV1):
            raise RuntimeContractError(
                RuntimeRejectCode.TERMINAL_RESULT_INVALID,
                "source terminal scheduler returned an invalid object",
            )
        if result.schedule_id != branch.source_terminal_schedule_id:
            raise RuntimeContractError(
                RuntimeRejectCode.TERMINAL_RESULT_INVALID,
                "source terminal miss schedule does not match registration",
            )
        return result

    def _source_terminal_only_first_v1(
        self,
        *,
        source: SourceExecutionContextV1,
        producer_id: str,
        branch: TerminalOnlyBranchRegistrationV1,
    ) -> TerminalMissV1 | VerifiedTerminalV1:
        scheduler = self.source_terminal_schedulers.get(
            branch.source_terminal_schedule_id
        )
        if scheduler is None:
            raise RuntimeContractError(
                RuntimeRejectCode.TERMINAL_SCHEDULE_MISSING,
                f"no terminal-only source schedule {branch.source_terminal_schedule_id!r}",
            )
        result = scheduler(source)
        if isinstance(result, TerminalDraftV1):
            return self._verified_terminal_only_v1(
                source=source,
                producer_id=producer_id,
                branch=branch,
                draft=result,
            )
        if not isinstance(result, TerminalMissV1):
            raise RuntimeContractError(
                RuntimeRejectCode.TERMINAL_RESULT_INVALID,
                "terminal-only source scheduler returned an invalid object",
            )
        if result.schedule_id != branch.source_terminal_schedule_id:
            raise RuntimeContractError(
                RuntimeRejectCode.TERMINAL_RESULT_INVALID,
                "terminal-only source miss schedule does not match registration",
            )
        return result

    @staticmethod
    def _projection_digest_v1(projection: TargetProjectionV1) -> str:
        return canonical_digest_v1(
            {
                "root_context": projection.root_context,
                "equation_rank": projection.equation_rank,
                "facts": dict(projection.facts),
                "t5": {
                    "induction_rank": projection.t5.induction_rank,
                    "major_phase": projection.t5.major_phase,
                    "type_i_protocol": projection.t5.type_i_protocol,
                    "eta_p": projection.t5.eta_p,
                    "pre_a": projection.t5.pre_a,
                    "absorb_m": projection.t5.absorb_m,
                    "absorb_r_epsilon": projection.t5.absorb_r_epsilon,
                    "reset_carrier": projection.t5.reset_carrier,
                },
                "mark_behavior": projection.mark_behavior,
            }
        )

    def _validate_transition_v1(
        self,
        *,
        source: SourceExecutionContextV1,
        branch: BranchRegistrationV1,
        candidate: CandidateTransitionV1,
        projection: TargetProjectionV1,
        projection_digest: str,
    ) -> TransitionValidationV1:
        validator = self.transition_validators.get(
            branch.transition_validator_id
        )
        if validator is None:
            raise RuntimeContractError(
                RuntimeRejectCode.PRODUCER_RESULT_INVALID,
                f"no transition validator {branch.transition_validator_id!r}",
            )
        validation = validator(source, candidate, projection)
        if not isinstance(validation, TransitionValidationV1):
            raise RuntimeContractError(
                RuntimeRejectCode.PRODUCER_RESULT_INVALID,
                "transition validator returned an invalid object",
            )
        if (
            validation.source_state_id != source.state_id
            or validation.producer_id != candidate.producer_id
            or validation.branch_id != candidate.branch_id
            or validation.projection_digest != projection_digest
            or not all(
                (
                    validation.E1,
                    validation.E2,
                    validation.E3_pre_admission,
                    validation.E4,
                )
            )
            or not validation.evidence_ids
            or any(not item for item in validation.evidence_ids)
            or not set(branch.evidence_refs) <= set(validation.evidence_ids)
        ):
            raise RuntimeContractError(
                RuntimeRejectCode.PRODUCER_RESULT_INVALID,
                "transition validator did not bind and prove E1--E4",
            )
        return validation

    def _admit_candidate_transition_v1(
        self,
        source_item: RuntimeQueueItemV1,
        produced: ProducedCandidateV1,
        *,
        _verified_source: SourceExecutionContextV1 | None = None,
        _source_terminal: TerminalMissV1 | None = None,
    ) -> RuntimeDecisionV1:
        try:
            if not isinstance(produced, ProducedCandidateV1):
                raise RuntimeContractError(
                    RuntimeRejectCode.PRODUCER_RESULT_INVALID,
                    "candidate admission requires a runtime-issued envelope",
                )
            candidate = produced.candidate
            source = (
                _verified_source
                if _verified_source is not None
                else self.verify_source_state_v1(source_item)
            )
            issued = self._issued_candidates.get(produced.execution_id)
            expected_candidate_digest = canonical_digest_v1(
                {
                    "producer_id": candidate.producer_id,
                    "branch_id": candidate.branch_id,
                    "witness_payload": dict(candidate.witness_payload),
                    "ticket_type": candidate.ticket_type,
                }
            )
            if issued != (source.state_id, expected_candidate_digest):
                raise RuntimeContractError(
                    RuntimeRejectCode.PRODUCER_RESULT_INVALID,
                    "candidate was not issued once by this runtime executor",
                )
            del self._issued_candidates[produced.execution_id]
            dispatch_payload = dict(produced.dispatch_receipt)
            dispatch_digest = dispatch_payload.pop("digest", None)
            if (
                not isinstance(dispatch_digest, str)
                or canonical_digest_v1(dispatch_payload) != dispatch_digest
                or dispatch_payload.get("source_state_id") != source.state_id
                or dispatch_payload.get("selected_producer_id") != candidate.producer_id
                or dispatch_payload.get("selected_branch_id") != candidate.branch_id
            ):
                raise RuntimeContractError(
                    RuntimeRejectCode.PRODUCER_RESULT_INVALID,
                    "dispatch precedence receipt does not replay",
                )
            registration = self.producers.get(candidate.producer_id)
            if registration is None:
                raise RuntimeContractError(
                    RuntimeRejectCode.UNKNOWN_PRODUCER,
                    f"producer {candidate.producer_id!r} is not registered",
                )
            branch = registration.branch(candidate.branch_id)
            if source.owner not in branch.source_owners:
                raise RuntimeContractError(
                    RuntimeRejectCode.SOURCE_OWNER_NOT_ALLOWED,
                    f"branch cannot consume {source.owner!r}",
                )
            source_terminal = _source_terminal
            if source_terminal is None:
                source_terminal = self._source_terminal_first_v1(
                    source=source,
                    producer_id=registration.producer_id,
                    branch=branch,
                )
            if isinstance(source_terminal, VerifiedTerminalV1):
                return RuntimeDecisionV1(
                    accepted=True,
                    reason_code=RuntimeRejectCode.ACCEPT,
                    detail="source terminal preempted producer execution",
                    terminal=source_terminal,
                )
            projection = self._project_candidate_v1(
                source, registration, branch, candidate
            )
            terminal = self._target_terminal_miss_receipt_v1(
                branch, projection, candidate.witness_payload
            )
            if isinstance(terminal, TerminalDraftV1):
                verified = self._verified_terminal_v1(
                    source=source,
                    producer_id=registration.producer_id,
                    branch=branch,
                    draft=terminal,
                    dispatch_receipt=produced.dispatch_receipt,
                )
                return RuntimeDecisionV1(
                    accepted=True,
                    reason_code=RuntimeRejectCode.ACCEPT,
                    detail="target terminal preempted persistent admission",
                    terminal=verified,
                )

            target_potential = compute_t5_potential_v1(
                descriptor=projection.t5,
                facts=projection.facts,
                root_context=projection.root_context,
                equation_rank=projection.equation_rank,
            )
            verify_t5_ticket_v1(
                candidate.ticket_type, source.potential, target_potential
            )
            projection_digest = self._projection_digest_v1(projection)
            validation = self._validate_transition_v1(
                source=source,
                branch=branch,
                candidate=candidate,
                projection=projection,
                projection_digest=projection_digest,
            )
            transition_id = "transition:" + canonical_digest_v1(
                {
                    "runtime_id": RUNTIME_ID,
                    "source_state_id": source.state_id,
                    "producer_id": registration.producer_id,
                    "branch_id": branch.branch_id,
                    "projection_digest": projection_digest,
                    "witness_digest": canonical_digest_v1(
                        dict(candidate.witness_payload)
                    ),
                    "evidence_refs": list(branch.evidence_refs),
                    "validator_id": branch.transition_validator_id,
                    "validation_evidence_ids": list(validation.evidence_ids),
                    "source_terminal_miss": source_terminal.evidence_id,
                    "dispatch_precedence_digest": dispatch_digest,
                    "ticket_type": candidate.ticket_type,
                    "source_potential": list(source.potential),
                    "target_potential": list(target_potential),
                }
            )
            terminal_receipt = state_contract.seal_receipt_v1(
                {
                    "schema_id": state_contract.TERMINAL_FIRST_SCHEMA_ID,
                    "schema_version": 1,
                    "receipt_id": terminal.evidence_id,
                    "scope": terminal.scope,
                    "outcome": "MISS",
                }
            )
            mark_receipt = self._target_mark_receipt_v1(
                source, projection, transition_id
            )
            facts = copy.deepcopy(dict(projection.facts))
            facts_digest = state_contract.canonical_digest_v1(facts)
            source_receipt = state_contract.seal_receipt_v1(
                {
                    "schema_id": state_contract.SUCCESSOR_RECEIPT_SCHEMA_ID,
                    "schema_version": 1,
                    "receipt_id": transition_id,
                    "producer_id": registration.producer_id,
                    "branch_id": branch.branch_id,
                    "root_context": projection.root_context,
                    "equation_rank": projection.equation_rank,
                    "target_facts_digest": facts_digest,
                    "terminal_first_digest": terminal_receipt["digest"],
                    "status": "VERIFIED_EDGE",
                    "parent_state_id": source.state_id,
                    "E1": True,
                    "E2": True,
                    "E3": True,
                    "E4": True,
                    "E5": True,
                    "T5_ticket": candidate.ticket_type,
                }
            )
            raw_target: dict[str, Any] = {
                "schema_id": state_contract.STATE_SCHEMA_ID,
                "schema_version": state_contract.STATE_SCHEMA_VERSION,
                "state_id": "",
                "artifact_class": "persistent_state",
                "consumer": "t6_selector",
                "queue_gate": state_contract.ADMITTED_SUCCESSOR,
                "producer_id": registration.producer_id,
                "branch_id": branch.branch_id,
                "parent_state_id": source.state_id,
                "root_context": projection.root_context,
                "equation_rank": projection.equation_rank,
                "mark": mark_receipt,
                "terminal_first": terminal_receipt,
                "source_receipt": source_receipt,
                "facts": facts,
            }
            raw_target["state_id"] = state_contract.build_state_id_v1(raw_target)
            rules = self.producer_rules_v1()
            admission = state_contract.reject_before_persistent_queue_v1(
                raw_target, rules
            )
            if not admission.accepted or admission.owner is None or admission.owner_digest is None:
                raise RuntimeContractError(
                    RuntimeRejectCode.TARGET_ADMISSION_REJECTED,
                    f"{admission.reason_code.value}: {admission.detail}",
                )
            if admission.owner not in branch.target_owners:
                raise RuntimeContractError(
                    RuntimeRejectCode.TARGET_ADMISSION_REJECTED,
                    "recomputed owner is outside the branch target set",
                )
            target_id = str(raw_target["state_id"])
            ticket_receipt = make_t5_ticket_receipt_v1(
                source_state_id=source.state_id,
                target_state_id=target_id,
                ticket_type=candidate.ticket_type,
                source=source.potential,
                target=target_potential,
            )
            transition_receipt = seal_v1(
                {
                    "schema_id": "verified_successor_runtime_receipt_v1",
                    "schema_version": 1,
                    "transition_id": transition_id,
                    "source_state_id": source.state_id,
                    "target_state_id": target_id,
                    "producer_id": registration.producer_id,
                    "branch_id": branch.branch_id,
                    "evidence_refs": list(branch.evidence_refs),
                    "validator_id": branch.transition_validator_id,
                    "validation_evidence_ids": list(validation.evidence_ids),
                    "source_terminal_miss": source_terminal.evidence_id,
                    "dispatch_precedence_digest": dispatch_digest,
                    "projection_digest": projection_digest,
                    "owner": admission.owner,
                    "owner_digest": admission.owner_digest,
                    "t5_ticket_digest": ticket_receipt["digest"],
                }
            )
            target_item = RuntimeQueueItemV1(
                raw_state=MappingProxyType(raw_target),
                owner=admission.owner,
                owner_digest=admission.owner_digest,
                t5_descriptor=projection.t5,
                potential_receipt=MappingProxyType(
                    make_potential_receipt_v1(target_id, target_potential)
                ),
                transition_receipt=MappingProxyType(transition_receipt),
            )
            self._enqueue_admitted_target_v1(target_item)
            successor = VerifiedSuccessorV1(
                source_state_id=source.state_id,
                target_state_id=target_id,
                producer_id=registration.producer_id,
                branch_id=branch.branch_id,
                target_owner=admission.owner,
                owner_digest=admission.owner_digest,
                t5_ticket_receipt=MappingProxyType(ticket_receipt),
                transition_receipt=MappingProxyType(transition_receipt),
            )
            return RuntimeDecisionV1(
                accepted=True,
                reason_code=RuntimeRejectCode.ACCEPT,
                detail="candidate projected, classified, admitted and enqueued",
                successor=successor,
            )
        except (RuntimeContractError, state_contract.StateContractError) as exc:
            if isinstance(exc, RuntimeContractError):
                code = exc.code
                detail = exc.detail
            else:
                code = RuntimeRejectCode.TARGET_ADMISSION_REJECTED
                detail = f"{exc.code.value}: {exc.detail}"
            return RuntimeDecisionV1(
                accepted=False,
                reason_code=code,
                detail=detail,
            )

    def admit_candidate_transition_v1(
        self,
        source_item: RuntimeQueueItemV1,
        produced: ProducedCandidateV1,
    ) -> RuntimeDecisionV1:
        """Admit a one-use candidate issued by this runtime's executor."""

        return self._admit_candidate_transition_v1(source_item, produced)

    def run_state_once_v1(
        self, source_item: RuntimeQueueItemV1
    ) -> RuntimeDecisionV1:
        """Run the fixed terminal-first and producer precedence for one state."""

        try:
            source = self.verify_source_state_v1(source_item)
            terminal_routes = self.terminal_dispatch_precedence.get(
                source.owner, ()
            )
            routes = self.dispatch_precedence.get(source.owner)
            if not routes and not terminal_routes:
                raise RuntimeContractError(
                    RuntimeRejectCode.DEAD_END,
                    f"owner {source.owner!r} has no dispatch routes",
                )
            terminal_guard_misses: list[dict[str, str]] = []
            for index, entry in enumerate(terminal_routes):
                registration = self.terminal_producers[entry.producer_id]
                branch = registration.branch(entry.branch_id)
                source_terminal = self._source_terminal_only_first_v1(
                    source=source,
                    producer_id=registration.producer_id,
                    branch=branch,
                )
                if isinstance(source_terminal, VerifiedTerminalV1):
                    return RuntimeDecisionV1(
                        accepted=True,
                        reason_code=RuntimeRejectCode.ACCEPT,
                        detail="terminal-only source schedule preempted dispatch",
                        terminal=source_terminal,
                    )
                executor = self.terminal_executors[registration.producer_id]
                output = executor(source, entry.branch_id)
                if isinstance(output, GuardMissV1):
                    terminal_guard_misses.append(
                        {
                            "producer_id": entry.producer_id,
                            "branch_id": entry.branch_id,
                            "reason_code": output.reason_code,
                        }
                    )
                    continue
                if isinstance(output, CandidateTransitionV1):
                    raise RuntimeContractError(
                        RuntimeRejectCode.TERMINAL_ONLY_CANDIDATE,
                        "terminal-only producer returned a candidate",
                    )
                if not isinstance(output, TerminalDraftV1):
                    raise RuntimeContractError(
                        RuntimeRejectCode.PRODUCER_RESULT_INVALID,
                        "terminal-only producer returned an unsupported result",
                    )
                dispatch_receipt = seal_v1(
                    {
                        "schema_id": "runtime_terminal_dispatch_receipt_v1",
                        "schema_version": 1,
                        "source_state_id": source.state_id,
                        "source_owner": source.owner,
                        "ordered_routes": [
                            {
                                "producer_id": route.producer_id,
                                "branch_id": route.branch_id,
                            }
                            for route in terminal_routes
                        ],
                        "selected_index": index,
                        "selected_producer_id": entry.producer_id,
                        "selected_branch_id": entry.branch_id,
                        "prior_guard_misses": terminal_guard_misses,
                        "source_terminal_miss": source_terminal.evidence_id,
                    }
                )
                terminal = self._verified_terminal_only_v1(
                    source=source,
                    producer_id=registration.producer_id,
                    branch=branch,
                    draft=output,
                    dispatch_receipt=dispatch_receipt,
                )
                return RuntimeDecisionV1(
                    accepted=True,
                    reason_code=RuntimeRejectCode.ACCEPT,
                    detail="terminal-only producer returned an independently verified terminal",
                    terminal=terminal,
                )
            if not routes:
                return RuntimeDecisionV1(
                    accepted=False,
                    reason_code=RuntimeRejectCode.DEAD_END,
                    detail=f"all terminal-only guards missed: {terminal_guard_misses}",
                )
            first_registration = self.producers[routes[0].producer_id]
            first_branch = first_registration.branch(routes[0].branch_id)
            source_terminal = self._source_terminal_first_v1(
                source=source,
                producer_id=first_registration.producer_id,
                branch=first_branch,
            )
            if isinstance(source_terminal, VerifiedTerminalV1):
                return RuntimeDecisionV1(
                    accepted=True,
                    reason_code=RuntimeRejectCode.ACCEPT,
                    detail="source terminal preempted producer execution",
                    terminal=source_terminal,
                )
            guard_misses: list[dict[str, str]] = []
            for index, entry in enumerate(routes):
                registration = self.producers[entry.producer_id]
                branch = registration.branch(entry.branch_id)
                executor = self.executors.get(entry.producer_id)
                if executor is None:
                    raise RuntimeContractError(
                        RuntimeRejectCode.UNKNOWN_PRODUCER,
                        f"producer {entry.producer_id!r} has no executable implementation",
                    )
                output = executor(source, entry.branch_id)
                if isinstance(output, GuardMissV1):
                    guard_misses.append(
                        {
                            "producer_id": entry.producer_id,
                            "branch_id": entry.branch_id,
                            "reason_code": output.reason_code,
                        }
                    )
                    continue
                dispatch_receipt = seal_v1(
                    {
                        "schema_id": "runtime_dispatch_precedence_receipt_v1",
                        "schema_version": 1,
                        "source_state_id": source.state_id,
                        "source_owner": source.owner,
                        "ordered_routes": [
                            {
                                "producer_id": route.producer_id,
                                "branch_id": route.branch_id,
                            }
                            for route in routes
                        ],
                        "selected_index": index,
                        "selected_producer_id": entry.producer_id,
                        "selected_branch_id": entry.branch_id,
                        "prior_guard_misses": guard_misses,
                        "source_terminal_miss": source_terminal.evidence_id,
                    }
                )
                if isinstance(output, TerminalDraftV1):
                    terminal = self._verified_terminal_v1(
                        source=source,
                        producer_id=entry.producer_id,
                        branch=branch,
                        draft=output,
                        dispatch_receipt=dispatch_receipt,
                    )
                    return RuntimeDecisionV1(
                        accepted=True,
                        reason_code=RuntimeRejectCode.ACCEPT,
                        detail="producer returned an independently verified terminal",
                        terminal=terminal,
                    )
                if not isinstance(output, CandidateTransitionV1):
                    raise RuntimeContractError(
                        RuntimeRejectCode.PRODUCER_RESULT_INVALID,
                        "producer returned an unsupported result type",
                    )
                candidate_digest = canonical_digest_v1(
                    {
                        "producer_id": output.producer_id,
                        "branch_id": output.branch_id,
                        "witness_payload": dict(output.witness_payload),
                        "ticket_type": output.ticket_type,
                    }
                )
                execution_id = "execution:" + canonical_digest_v1(
                    {
                        "source_state_id": source.state_id,
                        "candidate_digest": candidate_digest,
                        "dispatch_digest": dispatch_receipt["digest"],
                    }
                )
                self._issued_candidates[execution_id] = (
                    source.state_id,
                    candidate_digest,
                )
                produced = ProducedCandidateV1(
                    candidate=output,
                    execution_id=execution_id,
                    dispatch_receipt=MappingProxyType(dispatch_receipt),
                )
                assert isinstance(source_terminal, TerminalMissV1)
                return self._admit_candidate_transition_v1(
                    source_item,
                    produced,
                    _verified_source=source,
                    _source_terminal=source_terminal,
                )
            return RuntimeDecisionV1(
                accepted=False,
                reason_code=RuntimeRejectCode.DEAD_END,
                detail=f"all registered guards missed: {guard_misses}",
            )
        except (RuntimeContractError, state_contract.StateContractError) as exc:
            if isinstance(exc, RuntimeContractError):
                code = exc.code
                detail = exc.detail
            else:
                code = RuntimeRejectCode.SOURCE_NOT_ADMITTED
                detail = f"{exc.code.value}: {exc.detail}"
            return RuntimeDecisionV1(False, code, detail)


__all__ = [
    "BranchRegistrationV1",
    "TerminalOnlyBranchRegistrationV1",
    "TerminalOnlyProducerRegistrationV1",
    "CandidateTransitionV1",
    "GuardMissV1",
    "IDENTITY_MARK",
    "InitializerRegistrationV1",
    "LOWER_EQUATION_MARK",
    "PersistentSelectorRuntimeV1",
    "ProducerRegistrationV1",
    "ProducedCandidateV1",
    "DispatchEntryV1",
    "TerminalDispatchEntryV1",
    "RuntimeContractError",
    "RuntimeDecisionV1",
    "RuntimeQueueItemV1",
    "RuntimeRejectCode",
    "SourceExecutionContextV1",
    "T5StateDescriptorV1",
    "TargetProjectionV1",
    "TerminalDraftV1",
    "TerminalMissV1",
    "TransitionValidationV1",
    "VerifiedSuccessorV1",
    "VerifiedTerminalV1",
    "compute_t5_potential_v1",
    "make_potential_receipt_v1",
    "make_t5_ticket_receipt_v1",
    "verify_t5_ticket_v1",
]
