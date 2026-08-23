from __future__ import annotations

import copy
from contextlib import contextmanager
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module(
    "audit_t6_constructor_inventory_v1_negative_controls",
    ROOT / "scripts" / "audit_t6_constructor_inventory_v1.py",
)
STATE_FIXTURES = load_module(
    "t6_persistent_selector_state_v1_negative_control_fixtures",
    ROOT / "tests" / "test_t6_persistent_selector_state_v1.py",
)
CONTRACT = STATE_FIXTURES.CONTRACT

INVENTORY_PATH = ROOT / "data" / "t6-constructor-inventory-v1.json"
CANONICAL_INVENTORY = json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))
BASELINE_SOURCE_SIGNALS = tuple(
    row["anchor"] for row in CANONICAL_INVENTORY["source_signal_anchors"]
)
BASELINE_QUEUE_SIGNALS: tuple[str, ...] = ()


def audit_inventory_document(inventory: dict):
    with tempfile.TemporaryDirectory() as temporary:
        path = Path(temporary) / "inventory.json"
        path.write_text(json.dumps(inventory), encoding="utf-8")
        return AUDIT.audit_inventory(
            ROOT,
            path,
            source_signals=BASELINE_SOURCE_SIGNALS,
            queue_api_signals=BASELINE_QUEUE_SIGNALS,
        )


@contextmanager
def mutable_registry_root():
    """Build a small overlay with mutable active data and linked evidence."""

    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        shutil.copytree(ROOT / "data", root / "data")
        for directory in ("claims", "concepts", "reproductions", "scripts"):
            (root / directory).symlink_to(ROOT / directory, target_is_directory=True)
        yield root


def mutate_registered_edge_targets(root: Path, edge_id: str, targets: list[str]) -> None:
    for relative, field in (
        ("data/t6-proof-frontier-v2.json", "registered_edges"),
        ("data/t6-selector-obligation-ledger-v1.json", "concrete_edge_families"),
    ):
        path = root / relative
        document = json.loads(path.read_text(encoding="utf-8"))
        edge = next(item for item in document[field] if item["id"] == edge_id)
        edge["target_family_ids"] = targets
        path.write_text(json.dumps(document), encoding="utf-8")


class ConstructorInventoryNegativeControls(unittest.TestCase):
    def test_missing_constructor_symbol_fails_closed(self) -> None:
        inventory = copy.deepcopy(CANONICAL_INVENTORY)
        entry = inventory["entries"][0]
        entry["implementation"]["symbols"] = ["missing_constructor_symbol_v99"]

        result = audit_inventory_document(inventory)

        self.assertFalse(result.ok)
        self.assertTrue(
            any("missing symbol" in error for error in result.errors), result.errors
        )

    def test_registry_with_extra_producer_fails_closed(self) -> None:
        inventory = copy.deepcopy(CANONICAL_INVENTORY)
        removed = inventory["entries"].pop(1)

        result = audit_inventory_document(inventory)

        registry_id = removed["registry_correspondence"]["id"]
        self.assertFalse(result.ok)
        self.assertTrue(
            any(
                error.startswith("REGISTRY_MISSING_IN_INVENTORY[frontier]")
                and registry_id in error
                for error in result.errors
            ),
            result.errors,
        )

    def test_registry_with_missing_producer_fails_closed(self) -> None:
        inventory = copy.deepcopy(CANONICAL_INVENTORY)
        extra = copy.deepcopy(inventory["entries"][1])
        extra["id"] = "edge.future_unregistered_constructor"
        extra["registry_correspondence"]["id"] = "future_unregistered_constructor"
        inventory["entries"].append(extra)

        result = audit_inventory_document(inventory)

        self.assertFalse(result.ok)
        self.assertTrue(
            any(
                error.startswith("INVENTORY_EDGE_NOT_IN_REGISTRY[frontier]")
                and "future_unregistered_constructor" in error
                for error in result.errors
            ),
            result.errors,
        )

    def test_new_atomic_or_marked_target_requires_t2_t3(self) -> None:
        edge_id = "q_one_g_full_carrier_phase_root"
        targets = [
            "type_i_full_carrier_post_g",
            "t2_v1_atomic_pending_target",
            "generic_nontrivial_marked_state",
        ]
        with mutable_registry_root() as root:
            mutate_registered_edge_targets(root, edge_id, targets)
            result = AUDIT.audit_inventory(
                root,
                source_signals=BASELINE_SOURCE_SIGNALS,
                queue_api_signals=BASELINE_QUEUE_SIGNALS,
            )

        self.assertFalse(result.ok)
        self.assertTrue(
            any("atomic target lacks T2v1 coverage" in error for error in result.errors),
            result.errors,
        )
        self.assertTrue(
            any(
                "nontrivial marked target lacks a T3 extension" in error
                for error in result.errors
            ),
            result.errors,
        )

    def test_archive_cannot_be_promoted_to_active_constructor_source(self) -> None:
        inventory = copy.deepcopy(CANONICAL_INVENTORY)
        inventory["scope"]["active_source_roots"].append("docs/archive")

        result = audit_inventory_document(inventory)

        self.assertFalse(result.ok)
        self.assertTrue(
            any(error.startswith("ARCHIVE_POLLUTION") for error in result.errors),
            result.errors,
        )

    def test_new_constructor_signal_is_discovered_then_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            scripts = root / "scripts"
            scripts.mkdir()
            (scripts / "future_constructor.py").write_text(
                "def future_constructor():\n"
                "    return {'recursive_edge_eligible': True}\n",
                encoding="utf-8",
            )
            new_signals = AUDIT.discover_source_signals(root, ["scripts"])

        self.assertEqual(
            new_signals,
            (
                "scripts/future_constructor.py:future_constructor:"
                "recursive_edge_eligible_nonfalse",
            ),
        )
        result = AUDIT.audit_inventory(
            ROOT,
            source_signals=(*BASELINE_SOURCE_SIGNALS, *new_signals),
            queue_api_signals=BASELINE_QUEUE_SIGNALS,
        )
        self.assertFalse(result.ok)
        self.assertTrue(
            any(error.startswith("SOURCE_SIGNAL_UNINVENTORIED") for error in result.errors),
            result.errors,
        )


class PersistentAdmissionNegativeControls(unittest.TestCase):
    def decision(self, raw, rules=None):
        return CONTRACT.reject_before_persistent_queue_v1(
            raw, rules or STATE_FIXTURES.registry()
        )

    def test_unknown_header_and_version_have_stable_reason_codes(self) -> None:
        for field, value, expected in (
            ("schema_id", "future_selector_state", CONTRACT.RejectCode.UNKNOWN_SCHEMA),
            ("schema_version", 2, CONTRACT.RejectCode.UNKNOWN_VERSION),
        ):
            with self.subTest(field=field):
                raw = STATE_FIXTURES.make_state()
                raw[field] = value
                raw["state_id"] = CONTRACT.build_state_id_v1(raw)
                self.assertEqual(self.decision(raw).reason_code, expected)

    def test_malformed_source_receipt_has_stable_reason_code(self) -> None:
        raw = STATE_FIXTURES.make_state()
        del raw["source_receipt"]["digest"]
        raw["state_id"] = CONTRACT.build_state_id_v1(raw)

        self.assertEqual(
            self.decision(raw).reason_code,
            CONTRACT.RejectCode.MALFORMED_SOURCE_RECEIPT,
        )

    def test_empty_owner_is_rejected_by_real_queue_gate(self) -> None:
        raw = STATE_FIXTURES.make_state(
            STATE_FIXTURES.facts(full_carrier_scope=False)
        )

        self.assertEqual(
            self.decision(raw).reason_code, CONTRACT.RejectCode.FAMILY_NO_MATCH
        )

    def test_mutated_owner_registry_overlap_is_rejected(self) -> None:
        header = STATE_FIXTURES.extract(STATE_FIXTURES.make_state())
        predicates = tuple(CONTRACT.FAMILY_PREDICATES_V1) + (
            CONTRACT.FamilyPredicateV1("mutated_overlap", lambda _header: True),
        )

        with self.assertRaises(CONTRACT.StateContractError) as caught:
            CONTRACT.classify_selector_owner_v1(header, predicates=predicates)

        self.assertEqual(
            caught.exception.code, CONTRACT.RejectCode.FAMILY_ILLEGAL_OVERLAP
        )

    def test_precedence_mutation_invalidates_owner_digest(self) -> None:
        selector_facts = STATE_FIXTURES.facts(
            provenance_kind="OVERFLOW",
            is_overflow=True,
            support_A=1,
            carrier_M=37,
            overflow_d=71,
            chart_R=75,
            chart_K=1369,
            same_chart_promotion_receipt=True,
        )
        header = STATE_FIXTURES.extract(STATE_FIXTURES.make_state(selector_facts))
        canonical = CONTRACT.classify_selector_owner_v1(header)
        predicates = list(CONTRACT.FAMILY_PREDICATES_V1)
        low_index = next(
            index
            for index, item in enumerate(predicates)
            if item.family_id == "type_i_low_support_persistent_overflow"
        )
        low = predicates.pop(low_index)
        a_one_index = next(
            index
            for index, item in enumerate(predicates)
            if item.family_id == "type_i_a_one_overflow"
        )
        predicates.insert(a_one_index, low)
        changed = CONTRACT.classify_selector_owner_v1(
            header, predicates=tuple(predicates)
        )

        self.assertNotEqual(changed.owner, canonical.owner)
        with self.assertRaises(CONTRACT.StateContractError) as caught:
            CONTRACT.verify_owner_digest_v1(
                header, changed, canonical.owner_digest
            )
        self.assertEqual(
            caught.exception.code, CONTRACT.RejectCode.OWNER_DIGEST_MISMATCH
        )

    def test_unregistered_target_is_rejected_by_real_queue_gate(self) -> None:
        raw = STATE_FIXTURES.make_state()
        rules = STATE_FIXTURES.registry(
            initializer_targets=frozenset({"type_ii_relation_g_endpoint"})
        )

        self.assertEqual(
            self.decision(raw, rules).reason_code,
            CONTRACT.RejectCode.PRODUCER_TARGET_OWNER_NOT_DECLARED,
        )

    def test_serializer_cannot_bypass_receipt_or_queue_gate(self) -> None:
        missing_receipt = STATE_FIXTURES.make_state()
        del missing_receipt["source_receipt"]
        missing_receipt["state_id"] = CONTRACT.build_state_id_v1(missing_receipt)
        self.assertEqual(
            self.decision(missing_receipt).reason_code,
            CONTRACT.RejectCode.MISSING_TOP_LEVEL_FIELD,
        )

        unknown_gate = STATE_FIXTURES.make_state()
        unknown_gate["queue_gate"] = "DIRECT_SERIALIZER_BYPASS"
        unknown_gate["state_id"] = CONTRACT.build_state_id_v1(unknown_gate)
        self.assertEqual(
            self.decision(unknown_gate).reason_code,
            CONTRACT.RejectCode.UNKNOWN_QUEUE_GATE,
        )


if __name__ == "__main__":
    unittest.main()
