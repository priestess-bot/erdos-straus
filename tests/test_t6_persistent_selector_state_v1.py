from __future__ import annotations

import copy
import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "t6_persistent_selector_state_v1.py"
SPEC = importlib.util.spec_from_file_location(
    "t6_persistent_selector_state_v1", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError(f"cannot import {MODULE_PATH}")
CONTRACT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = CONTRACT
SPEC.loader.exec_module(CONTRACT)

ADAPTER_PATH = ROOT / "reproductions" / "type_i_overflow_total_cofactor_typed_adapter.py"
ADAPTER_SPEC = importlib.util.spec_from_file_location(
    "type_i_overflow_total_cofactor_typed_adapter", ADAPTER_PATH
)
if ADAPTER_SPEC is None or ADAPTER_SPEC.loader is None:  # pragma: no cover
    raise RuntimeError(f"cannot import {ADAPTER_PATH}")
TOTAL_COFACTOR = importlib.util.module_from_spec(ADAPTER_SPEC)
sys.modules[ADAPTER_SPEC.name] = TOTAL_COFACTOR
ADAPTER_SPEC.loader.exec_module(TOTAL_COFACTOR)


P = 73
INITIALIZER = "fixture_initializer_v1"
SUCCESSOR = "fixture_successor_v1"


def facts(**updates):
    result = {
        "major_phase": "TYPEI",
        "type_i_protocol": "CHARGED",
        "t5_eta_p": 0,
        "pre_a": None,
        "absorb_m": None,
        "absorb_r_epsilon": 0,
        "reset_carrier": None,
        "endpoint_fiber": "NONE",
        "relation_q": None,
        "provenance_kind": "FULL_CARRIER_POST_G",
        "full_carrier_scope": True,
        "atomic_arm": "NONE",
        "dispatch_status": "NONE",
        "proper_root_k": None,
        "proper_root_height_class": "NONE",
        "proper_root_height": None,
        "proper_root_r": None,
        "is_overflow": False,
        "support_A": 5,
        "carrier_M": None,
        "overflow_d": None,
        "chart_R": 3,
        "chart_K": 55,
        "sink_scc_receipt": False,
        "same_chart_promotion_receipt": False,
    }
    result.update(updates)
    return result


def proper_root_chart(prime: int, root_parameter: int) -> dict[str, int]:
    half = (prime + 1) // 2
    support = half * (prime * prime * root_parameter - half)
    carrier = support * (prime - 1)
    residual = (
        2 * prime**3 * root_parameter
        - prime * prime
        - 2 * prime * root_parameter
        - prime
        + 1
    )
    return {"support_A": support, "chart_K": carrier, "chart_R": residual}


def c8_parent_chart(prime: int, s: int) -> dict[str, int]:
    assert prime == 48 * s + 1
    n = 132 * s + 1
    support = (prime * n - 1) // 4
    return {
        "support_A": support,
        "chart_K": support * (prime - 1),
        "chart_R": (prime - 1) * n - 1,
    }


def mark_receipt(
    kind: str = CONTRACT.ROOT_SOL,
    equation_rank: int = P,
    root_context: int = P,
):
    return CONTRACT.seal_receipt_v1(
        {
            "schema_id": CONTRACT.MARK_SCHEMA_ID,
            "schema_version": 1,
            "receipt_id": f"mark:{kind}:{equation_rank}",
            "kind": kind,
            "root_context": root_context,
            "equation_rank": equation_rank,
        }
    )


def terminal_receipt(outcome: str = "MISS"):
    return CONTRACT.seal_receipt_v1(
        {
            "schema_id": CONTRACT.TERMINAL_FIRST_SCHEMA_ID,
            "schema_version": 1,
            "receipt_id": f"terminal:{outcome.lower()}",
            "scope": "fixture_terminal_scope",
            "outcome": outcome,
        }
    )


def make_state(
    selector_facts=None,
    *,
    gate: str = CONTRACT.ROOT_INITIALIZER_OUTPUT,
    producer: str = INITIALIZER,
    branch: str = "root_nonterminal",
    parent_state_id: str | None = None,
    mark_kind: str = CONTRACT.ROOT_SOL,
    equation_rank: int = P,
    root_context: int = P,
    terminal_outcome: str = "MISS",
):
    selector_facts = facts() if selector_facts is None else selector_facts
    terminal = terminal_receipt(terminal_outcome)
    common = {
        "schema_version": 1,
        "receipt_id": f"source:{producer}:{branch}:{parent_state_id}",
        "producer_id": producer,
        "branch_id": branch,
        "root_context": root_context,
        "equation_rank": equation_rank,
        "target_facts_digest": CONTRACT.canonical_digest_v1(selector_facts),
        "terminal_first_digest": terminal["digest"],
    }
    if gate == CONTRACT.ROOT_INITIALIZER_OUTPUT:
        source = CONTRACT.seal_receipt_v1(
            {
                "schema_id": CONTRACT.INITIALIZER_RECEIPT_SCHEMA_ID,
                **common,
                "status": "NONTERMINAL_INITIALIZER_OUTPUT",
            }
        )
    else:
        source = CONTRACT.seal_receipt_v1(
            {
                "schema_id": CONTRACT.SUCCESSOR_RECEIPT_SCHEMA_ID,
                **common,
                "status": "VERIFIED_EDGE",
                "parent_state_id": parent_state_id,
                "E1": True,
                "E2": True,
                "E3": True,
                "E4": True,
                "E5": True,
                "T5_ticket": "LOCAL_DROP",
            }
        )
    raw = {
        "schema_id": CONTRACT.STATE_SCHEMA_ID,
        "schema_version": CONTRACT.STATE_SCHEMA_VERSION,
        "state_id": "pending",
        "artifact_class": "persistent_state",
        "consumer": "t6_selector",
        "queue_gate": gate,
        "producer_id": producer,
        "branch_id": branch,
        "parent_state_id": parent_state_id,
        "root_context": root_context,
        "equation_rank": equation_rank,
        "mark": mark_receipt(mark_kind, equation_rank, root_context),
        "terminal_first": terminal,
        "source_receipt": source,
        "facts": selector_facts,
    }
    raw["state_id"] = CONTRACT.build_state_id_v1(raw)
    return raw


ALL_FAMILIES = frozenset(CONTRACT.FAMILY_PRECEDENCE_V1)


def registry(
    *,
    initializer_targets: frozenset[str] = ALL_FAMILIES,
    successor_sources: frozenset[str] = frozenset({"type_i_full_carrier_post_g"}),
    successor_targets: frozenset[str] = ALL_FAMILIES,
):
    return {
        INITIALIZER: CONTRACT.ProducerRuleV1(
            producer_id=INITIALIZER,
            queue_gate=CONTRACT.ROOT_INITIALIZER_OUTPUT,
            branch_ids=frozenset({"root_nonterminal"}),
            source_owners=frozenset(),
            target_owners=initializer_targets,
        ),
        SUCCESSOR: CONTRACT.ProducerRuleV1(
            producer_id=SUCCESSOR,
            queue_gate=CONTRACT.ADMITTED_SUCCESSOR,
            branch_ids=frozenset({"overflow_target", "proper_target"}),
            source_owners=successor_sources,
            target_owners=successor_targets,
        ),
    }


def extract(raw, rules=None):
    return CONTRACT.extract_verified_selector_header_v1(raw, rules or registry())


class IndependentHeaderTests(unittest.TestCase):
    def test_extractor_succeeds_before_family_totality(self) -> None:
        raw = make_state(facts(full_carrier_scope=False))
        header = extract(raw)
        self.assertEqual(header.facts["major_phase"], "TYPEI")
        with self.assertRaises(CONTRACT.StateContractError) as caught:
            CONTRACT.classify_selector_owner_v1(header)
        self.assertEqual(caught.exception.code, CONTRACT.RejectCode.FAMILY_NO_MATCH)
        decision = CONTRACT.reject_before_persistent_queue_v1(raw, registry())
        self.assertFalse(decision.accepted)
        self.assertEqual(decision.reason_code, CONTRACT.RejectCode.FAMILY_NO_MATCH)

    def test_classifier_cache_is_not_a_legal_input(self) -> None:
        raw = make_state()
        raw["owner"] = "type_i_full_carrier_post_g"
        raw["state_id"] = CONTRACT.build_state_id_v1(raw)
        decision = CONTRACT.reject_before_persistent_queue_v1(raw, registry())
        self.assertEqual(
            decision.reason_code, CONTRACT.RejectCode.CIRCULAR_CACHE_FIELD
        )

    def test_unknown_schema_and_version_fail_closed(self) -> None:
        raw = make_state()
        raw["schema_id"] = "future_state_v9"
        raw["state_id"] = CONTRACT.build_state_id_v1(raw)
        self.assertEqual(
            CONTRACT.reject_before_persistent_queue_v1(raw, registry()).reason_code,
            CONTRACT.RejectCode.UNKNOWN_SCHEMA,
        )
        raw = make_state()
        raw["schema_version"] = 2
        raw["state_id"] = CONTRACT.build_state_id_v1(raw)
        self.assertEqual(
            CONTRACT.reject_before_persistent_queue_v1(raw, registry()).reason_code,
            CONTRACT.RejectCode.UNKNOWN_VERSION,
        )

    def test_receipt_mutation_is_detected_before_state_id_check(self) -> None:
        raw = make_state()
        raw["source_receipt"]["branch_id"] = "tampered"
        raw["state_id"] = CONTRACT.build_state_id_v1(raw)
        decision = CONTRACT.reject_before_persistent_queue_v1(raw, registry())
        self.assertEqual(
            decision.reason_code, CONTRACT.RejectCode.RECEIPT_DIGEST_MISMATCH
        )

    def test_terminal_hit_never_reaches_persistent_classifier(self) -> None:
        raw = make_state(terminal_outcome="HIT")
        decision = CONTRACT.reject_before_persistent_queue_v1(raw, registry())
        self.assertEqual(
            decision.reason_code,
            CONTRACT.RejectCode.TERMINAL_OUTPUT_NOT_PERSISTENT,
        )

    def test_unknown_producer_and_gate_bypass_fail_closed(self) -> None:
        raw = make_state(producer="unregistered")
        decision = CONTRACT.reject_before_persistent_queue_v1(raw, registry())
        self.assertEqual(decision.reason_code, CONTRACT.RejectCode.UNKNOWN_PRODUCER)

        raw = make_state()
        raw["queue_gate"] = CONTRACT.ADMITTED_SUCCESSOR
        raw["state_id"] = CONTRACT.build_state_id_v1(raw)
        decision = CONTRACT.reject_before_persistent_queue_v1(raw, registry())
        self.assertEqual(
            decision.reason_code, CONTRACT.RejectCode.PRODUCER_GATE_MISMATCH
        )


class FamilyPredicateTests(unittest.TestCase):
    def classify(self, selector_facts, **state_kwargs):
        return CONTRACT.classify_selector_owner_v1(
            extract(make_state(selector_facts, **state_kwargs))
        )

    def test_named_family_predicates_have_direct_witnesses(self) -> None:
        witnesses = {
            "type_ii_relation_f_endpoint": facts(
                major_phase="TYPEII_REL",
                type_i_protocol=None,
                endpoint_fiber="F",
                relation_q=2,
                provenance_kind="ORDINARY_ENDPOINT",
                full_carrier_scope=False,
                support_A=None,
                chart_R=None,
                chart_K=None,
            ),
            "type_ii_relation_g_endpoint": facts(
                major_phase="TYPEII_G_HANDOFF",
                type_i_protocol=None,
                endpoint_fiber="G",
                relation_q=1,
                provenance_kind="ORDINARY_ENDPOINT",
                full_carrier_scope=False,
                support_A=None,
                chart_R=None,
                chart_K=None,
            ),
            "type_i_full_carrier_post_g": facts(),
            "h4_non_v1_branch_or_descendant": facts(
                provenance_kind="H4_RESIDUAL"
            ),
            "c8_terminal_first_surviving_parent": facts(
                provenance_kind="C8_PARENT",
                full_carrier_scope=False,
                is_overflow=True,
                **c8_parent_chart(157_393, 3_279),
            ),
            "type_i_c2_19_macro_target": facts(provenance_kind="C2_19_MACRO"),
            "proper_root_stutter_k_one": facts(
                provenance_kind="PROPER_ROOT",
                full_carrier_scope=False,
                proper_root_k=1,
                proper_root_height_class="LOW",
                proper_root_height=3,
                proper_root_r=1,
                is_overflow=True,
                **proper_root_chart(73, 1),
            ),
            "proper_root_stutter_k_gt_one": facts(
                provenance_kind="PROPER_ROOT",
                full_carrier_scope=False,
                proper_root_k=2,
                proper_root_height_class="LOW",
                proper_root_height=3,
                proper_root_r=1,
                is_overflow=True,
                **proper_root_chart(73, 1),
            ),
            "proper_root_high_endpoint": facts(
                provenance_kind="PROPER_ROOT",
                full_carrier_scope=False,
                proper_root_k=None,
                proper_root_height_class="HIGH",
                proper_root_height=543,
                proper_root_r=90,
                is_overflow=True,
                **proper_root_chart(313, 90),
            ),
            "type_i_absorb_marked_residual": facts(
                type_i_protocol="ABSORB",
                provenance_kind="MARKED_ABSORB",
                support_A=5,
                chart_R=3,
                chart_K=55,
                absorb_m=3,
                absorb_r_epsilon=0,
            ),
            "type_i_a_one_overflow": facts(
                provenance_kind="OVERFLOW",
                is_overflow=True,
                support_A=1,
                carrier_M=37,
                overflow_d=71,
                chart_R=75,
                chart_K=1369,
                same_chart_promotion_receipt=True,
            ),
            "type_i_high_support_sink": facts(
                provenance_kind="OVERFLOW",
                is_overflow=True,
                support_A=1369,
                carrier_M=None,
                overflow_d=71,
                chart_R=75,
                chart_K=1369,
                sink_scc_receipt=True,
            ),
            "type_i_low_support_persistent_overflow": facts(
                provenance_kind="OVERFLOW",
                full_carrier_scope=False,
                is_overflow=True,
                support_A=37,
                carrier_M=74,
                overflow_d=71,
                chart_R=75,
                chart_K=1369,
                same_chart_promotion_receipt=True,
            ),
            "type_i_a_gt_one_overflow_residual": facts(
                provenance_kind="OVERFLOW",
                full_carrier_scope=False,
                is_overflow=True,
                support_A=37,
                carrier_M=None,
                overflow_d=71,
                chart_R=75,
                chart_K=1369,
            ),
            "generic_nontrivial_marked_state": facts(
                major_phase="GENERIC_MARKED",
                type_i_protocol=None,
                provenance_kind="GENERIC_MARKED",
                full_carrier_scope=False,
                support_A=None,
                chart_R=None,
                chart_K=None,
            ),
        }
        self.assertEqual(set(witnesses), set(CONTRACT.FAMILY_PRECEDENCE_V1))
        for expected, selector_facts in witnesses.items():
            kwargs = {}
            if expected == "generic_nontrivial_marked_state":
                kwargs = {
                    "mark_kind": CONTRACT.NONTRIVIAL_MARK,
                    "equation_rank": 37,
                }
            elif expected in {
                "proper_root_high_endpoint",
                "c8_terminal_first_surviving_parent",
            }:
                kwargs = {"root_context": 313, "equation_rank": 313}
                if expected == "c8_terminal_first_surviving_parent":
                    kwargs = {"root_context": 157_393, "equation_rank": 157_393}
            with self.subTest(family=expected):
                self.assertEqual(self.classify(selector_facts, **kwargs).owner, expected)

    def test_precedence_resolves_only_declared_overflow_overlaps(self) -> None:
        selector_facts = facts(
            provenance_kind="OVERFLOW",
            is_overflow=True,
            support_A=1,
            carrier_M=37,
            overflow_d=71,
            chart_R=75,
            chart_K=1369,
            same_chart_promotion_receipt=True,
        )
        classification = self.classify(selector_facts)
        self.assertEqual(classification.owner, "type_i_a_one_overflow")
        self.assertEqual(
            set(classification.matched_families),
            {
                "type_i_a_one_overflow",
                "type_i_low_support_persistent_overflow",
            },
        )

    def test_full_carrier_scope_does_not_launder_incomplete_overflow(self) -> None:
        selector_facts = facts(
            provenance_kind="OVERFLOW",
            full_carrier_scope=True,
            is_overflow=True,
            support_A=1,
            carrier_M=None,
            overflow_d=None,
            chart_R=75,
            chart_K=1369,
        )
        header = extract(make_state(selector_facts))
        with self.assertRaises(CONTRACT.StateContractError) as caught:
            CONTRACT.classify_selector_owner_v1(header)
        self.assertEqual(caught.exception.code, CONTRACT.RejectCode.FAMILY_NO_MATCH)

    def test_unexpected_overlap_is_rejected(self) -> None:
        header = extract(make_state())
        predicates = tuple(CONTRACT.FAMILY_PREDICATES_V1) + (
            CONTRACT.FamilyPredicateV1("rogue_family", lambda _header: True),
        )
        with self.assertRaises(CONTRACT.StateContractError) as caught:
            CONTRACT.classify_selector_owner_v1(header, predicates=predicates)
        self.assertEqual(
            caught.exception.code, CONTRACT.RejectCode.FAMILY_ILLEGAL_OVERLAP
        )

    def test_precedence_change_changes_owner_and_digest(self) -> None:
        selector_facts = facts(
            provenance_kind="OVERFLOW",
            is_overflow=True,
            support_A=1,
            carrier_M=37,
            overflow_d=71,
            chart_R=75,
            chart_K=1369,
            same_chart_promotion_receipt=True,
        )
        header = extract(make_state(selector_facts))
        canonical = CONTRACT.classify_selector_owner_v1(header)
        predicates = list(CONTRACT.FAMILY_PREDICATES_V1)
        a_one = next(
            item for item in predicates if item.family_id == "type_i_a_one_overflow"
        )
        low = next(
            item
            for item in predicates
            if item.family_id == "type_i_low_support_persistent_overflow"
        )
        predicates.remove(low)
        predicates.insert(predicates.index(a_one), low)
        changed = CONTRACT.classify_selector_owner_v1(
            header, predicates=tuple(predicates)
        )
        self.assertEqual(canonical.owner, "type_i_a_one_overflow")
        self.assertEqual(changed.owner, "type_i_low_support_persistent_overflow")
        self.assertNotEqual(canonical.owner_digest, changed.owner_digest)

    def test_owner_digest_is_a_gate_output_not_an_input(self) -> None:
        raw = make_state()
        decision = CONTRACT.reject_before_persistent_queue_v1(raw, registry())
        self.assertTrue(decision.accepted)
        header = extract(raw)
        classification = CONTRACT.classify_selector_owner_v1(header)
        CONTRACT.verify_owner_digest_v1(
            header, classification, decision.owner_digest
        )
        with self.assertRaises(CONTRACT.StateContractError) as caught:
            CONTRACT.verify_owner_digest_v1(header, classification, "owner:bad")
        self.assertEqual(
            caught.exception.code, CONTRACT.RejectCode.OWNER_DIGEST_MISMATCH
        )

    def test_high_proper_root_cannot_smuggle_low_height_k(self) -> None:
        raw = make_state(
            facts(
                provenance_kind="PROPER_ROOT",
                proper_root_height_class="HIGH",
                proper_root_height=219,
                proper_root_r=1,
                proper_root_k=2,
            )
        )
        decision = CONTRACT.reject_before_persistent_queue_v1(raw, registry())
        self.assertEqual(
            decision.reason_code, CONTRACT.RejectCode.MALFORMED_SELECTOR_FACTS
        )

    def test_proper_root_height_must_replay_from_cyclotomic_root_data(self) -> None:
        forged = facts(
            provenance_kind="PROPER_ROOT",
            proper_root_height_class="HIGH",
            proper_root_height=74,
            proper_root_r=1,
            proper_root_k=None,
        )
        decision = CONTRACT.reject_before_persistent_queue_v1(
            make_state(forged), registry()
        )
        self.assertEqual(
            decision.reason_code, CONTRACT.RejectCode.MALFORMED_SELECTOR_FACTS
        )

    def test_proper_root_chart_must_replay_from_root_parameter(self) -> None:
        forged = facts(
            provenance_kind="PROPER_ROOT",
            full_carrier_scope=False,
            proper_root_height_class="LOW",
            proper_root_height=3,
            proper_root_r=1,
            proper_root_k=2,
            is_overflow=False,
        )
        decision = CONTRACT.reject_before_persistent_queue_v1(
            make_state(forged), registry()
        )
        self.assertEqual(decision.reason_code, CONTRACT.RejectCode.INVALID_CHART_FACTS)

    def test_lineage_overflow_states_keep_their_specific_owner(self) -> None:
        proper = facts(
            provenance_kind="PROPER_ROOT",
            full_carrier_scope=False,
            proper_root_height_class="HIGH",
            proper_root_height=543,
            proper_root_r=90,
            proper_root_k=None,
            is_overflow=True,
            **proper_root_chart(313, 90),
        )
        proper_header = extract(
            make_state(proper, root_context=313, equation_rank=313)
        )
        proper_owner = CONTRACT.classify_selector_owner_v1(proper_header)
        self.assertEqual(proper_owner.owner, "proper_root_high_endpoint")
        self.assertEqual(
            set(proper_owner.matched_families),
            {"proper_root_high_endpoint", "type_i_a_gt_one_overflow_residual"},
        )

        c8 = facts(
            provenance_kind="C8_PARENT",
            full_carrier_scope=False,
            is_overflow=True,
            **c8_parent_chart(157_393, 3_279),
        )
        c8_header = extract(
            make_state(c8, root_context=157_393, equation_rank=157_393)
        )
        c8_owner = CONTRACT.classify_selector_owner_v1(c8_header)
        self.assertEqual(c8_owner.owner, "c8_terminal_first_surviving_parent")
        self.assertEqual(
            set(c8_owner.matched_families),
            {"c8_terminal_first_surviving_parent", "type_i_a_gt_one_overflow_residual"},
        )

    def test_charged_overflow_flag_cannot_disagree_with_chart(self) -> None:
        understated = facts(
            provenance_kind="OVERFLOW",
            full_carrier_scope=False,
            is_overflow=False,
            support_A=37,
            carrier_M=None,
            overflow_d=71,
            chart_R=75,
            chart_K=1369,
        )
        overstated = facts(is_overflow=True)
        for selector_facts in (understated, overstated):
            with self.subTest(selector_facts=selector_facts):
                decision = CONTRACT.reject_before_persistent_queue_v1(
                    make_state(selector_facts), registry()
                )
                self.assertEqual(
                    decision.reason_code, CONTRACT.RejectCode.INVALID_CHART_FACTS
                )

    def test_absorb_requires_semantic_low_chart_and_rank_fields(self) -> None:
        invalid = facts(
            type_i_protocol="ABSORB",
            provenance_kind="MARKED_ABSORB",
            support_A=37,
            chart_R=75,
            chart_K=1369,
            absorb_m=3,
        )
        decision = CONTRACT.reject_before_persistent_queue_v1(
            make_state(invalid), registry()
        )
        self.assertEqual(
            decision.reason_code, CONTRACT.RejectCode.UNKNOWN_HEADER_VALUE
        )

    def test_atomic_pending_checkpoint_cannot_be_queued(self) -> None:
        raw = make_state(
            facts(
                provenance_kind="ATOMIC_PENDING",
                atomic_arm="H4_A1",
                dispatch_status="PENDING",
            )
        )
        decision = CONTRACT.reject_before_persistent_queue_v1(raw, registry())
        self.assertEqual(
            decision.reason_code,
            CONTRACT.RejectCode.PENDING_OUTPUT_NOT_PERSISTENT,
        )


class QueueAndTraceTests(unittest.TestCase):
    def overflow_state(self, parent_state_id: str):
        return make_state(
            facts(
                provenance_kind="OVERFLOW",
                full_carrier_scope=False,
                is_overflow=True,
                support_A=1,
                carrier_M=None,
                overflow_d=71,
                chart_R=75,
                chart_K=1369,
            ),
            gate=CONTRACT.ADMITTED_SUCCESSOR,
            producer=SUCCESSOR,
            branch="overflow_target",
            parent_state_id=parent_state_id,
        )

    def test_undeclared_target_owner_is_rejected_by_real_gate(self) -> None:
        raw = make_state()
        rules = registry(
            initializer_targets=frozenset({"type_ii_relation_g_endpoint"})
        )
        decision = CONTRACT.reject_before_persistent_queue_v1(raw, rules)
        self.assertEqual(
            decision.reason_code,
            CONTRACT.RejectCode.PRODUCER_TARGET_OWNER_NOT_DECLARED,
        )

    def test_conditional_total_cofactor_control_cannot_self_register(self) -> None:
        source = TOTAL_COFACTOR.fixture_source(3, 45, 15, 37)
        self_report = TOTAL_COFACTOR.registration(
            source,
            parent_receipt_digest="self-reported-parent",
            terminal_first_digest="self-reported-miss",
            terminal_first_miss=True,
            persistent_queue=True,
        )
        control = TOTAL_COFACTOR.verify_transition(
            source, self_report, M=45, d=15, n=37
        )
        self.assertEqual(control["kind"], "relative_verified_edge")

        projected = make_state(
            facts(
                provenance_kind="OVERFLOW",
                full_carrier_scope=False,
                is_overflow=True,
                support_A=1,
                carrier_M=None,
                overflow_d=71,
                chart_R=75,
                chart_K=1369,
            ),
            gate=CONTRACT.ADMITTED_SUCCESSOR,
            producer=TOTAL_COFACTOR.ADAPTER_VERSION,
            branch="relative_total_cofactor_target",
            parent_state_id=source["state_id"],
        )
        decision = CONTRACT.reject_before_persistent_queue_v1(
            projected, registry()
        )
        self.assertFalse(decision.accepted)
        self.assertEqual(decision.reason_code, CONTRACT.RejectCode.UNKNOWN_PRODUCER)

    def test_initializer_and_successor_trace_replay(self) -> None:
        root = make_state()
        child = self.overflow_state(root["state_id"])
        receipt = CONTRACT.verify_persistent_trace_v1([root, child], registry())
        self.assertEqual(receipt.base_steps, 1)
        self.assertEqual(receipt.successor_steps, 1)
        self.assertEqual(
            receipt.owners,
            ("type_i_full_carrier_post_g", "type_i_a_one_overflow"),
        )
        self.assertIn("not_universal", receipt.statement_scope)

    def test_successor_with_unseen_parent_is_rejected(self) -> None:
        child = self.overflow_state("state:missing")
        with self.assertRaises(CONTRACT.StateContractError) as caught:
            CONTRACT.verify_persistent_trace_v1([child], registry())
        self.assertEqual(caught.exception.code, CONTRACT.RejectCode.PARENT_NOT_REACHABLE)

    def test_source_owner_declaration_is_checked_in_trace_step(self) -> None:
        root = make_state()
        child = self.overflow_state(root["state_id"])
        rules = registry(
            successor_sources=frozenset({"type_ii_relation_f_endpoint"})
        )
        with self.assertRaises(CONTRACT.StateContractError) as caught:
            CONTRACT.verify_persistent_trace_v1([root, child], rules)
        self.assertEqual(
            caught.exception.code,
            CONTRACT.RejectCode.PRODUCER_SOURCE_OWNER_NOT_DECLARED,
        )

    def test_initializer_cannot_be_reused_as_a_recursive_gate(self) -> None:
        first = make_state()
        second = copy.deepcopy(first)
        second["branch_id"] = "root_nonterminal"
        second["source_receipt"] = CONTRACT.seal_receipt_v1(
            {
                **{
                    key: value
                    for key, value in second["source_receipt"].items()
                    if key != "digest"
                },
                "receipt_id": "second-root",
            }
        )
        second["state_id"] = CONTRACT.build_state_id_v1(second)
        with self.assertRaises(CONTRACT.StateContractError) as caught:
            CONTRACT.verify_persistent_trace_v1([first, second], registry())
        self.assertEqual(caught.exception.code, CONTRACT.RejectCode.TRACE_ROOT_ORDER)


if __name__ == "__main__":
    unittest.main()
