from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "audit_t6_constructor_inventory_v1.py"
SPEC = importlib.util.spec_from_file_location("audit_t6_constructor_inventory_v1", MODULE_PATH)
if SPEC is None or SPEC.loader is None:  # pragma: no cover - import bootstrap guard
    raise RuntimeError(f"cannot load audit module from {MODULE_PATH}")
AUDIT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = AUDIT
SPEC.loader.exec_module(AUDIT)


def load_inventory() -> dict[str, Any]:
    return json.loads(
        (ROOT / "data" / "t6-constructor-inventory-v1.json").read_text(encoding="utf-8")
    )


class T6ConstructorInventoryV1Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source_signals = AUDIT.discover_source_signals(ROOT, ("reproductions", "scripts"))
        cls.queue_signals = AUDIT.discover_queue_api_signals(ROOT, ("reproductions", "scripts"))

    def audit_mutation(self, inventory: dict[str, Any]):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "inventory.json"
            path.write_text(json.dumps(inventory), encoding="utf-8")
            return AUDIT.audit_inventory(
                ROOT,
                path,
                source_signals=self.source_signals,
                queue_api_signals=self.queue_signals,
            )

    def test_canonical_inventory_is_honest_but_not_closure_ready(self) -> None:
        result = AUDIT.audit_inventory(
            ROOT,
            source_signals=self.source_signals,
            queue_api_signals=self.queue_signals,
        )
        self.assertTrue(result.ok, "\n".join(result.errors))
        self.assertFalse(result.closure_ready)
        self.assertEqual(result.queue_api_signals, ())
        self.assertTrue(
            any("total_cofactor_typed_adapter.py:registration" in item for item in result.source_signals)
        )

    def test_missing_registered_constructor_fails_closed(self) -> None:
        inventory = load_inventory()
        inventory["entries"] = [
            entry
            for entry in inventory["entries"]
            if entry["registry_correspondence"]["id"] != "same_chart_support_promotion"
        ]
        result = self.audit_mutation(inventory)
        self.assertFalse(result.ok)
        self.assertTrue(any("REGISTRY_MISSING_IN_INVENTORY" in error for error in result.errors))

    def test_new_source_signal_fails_closed(self) -> None:
        extra = (
            *self.source_signals,
            "reproductions/future_constructor.py:emit:recursive_edge_eligible_nonfalse",
        )
        result = AUDIT.audit_inventory(
            ROOT,
            source_signals=extra,
            queue_api_signals=self.queue_signals,
        )
        self.assertFalse(result.ok)
        self.assertTrue(any("SOURCE_SIGNAL_UNINVENTORIED" in error for error in result.errors))

    def test_atomic_target_without_t2_coverage_fails_closed(self) -> None:
        inventory = load_inventory()
        entry = next(
            item
            for item in inventory["entries"]
            if item["registry_correspondence"]["id"] == "h4_a_one_atomic_macro"
        )
        entry["t2_t3_coverage"]["T2"] = "UNASSIGNED"
        result = self.audit_mutation(inventory)
        self.assertFalse(result.ok)
        self.assertTrue(any("atomic target lacks T2v1" in error for error in result.errors))

    def test_archive_cannot_become_an_active_implementation(self) -> None:
        inventory = load_inventory()
        inventory["entries"][0]["implementation"]["file"] = (
            "docs/archive/proof-packages/fake.py"
        )
        result = self.audit_mutation(inventory)
        self.assertFalse(result.ok)
        self.assertTrue(any("ARCHIVE_POLLUTION" in error for error in result.errors))

    def test_enqueue_gate_cannot_be_claimed_without_queue_api(self) -> None:
        inventory = load_inventory()
        inventory["entries"][0]["serializer"]["enqueue_gate"] = (
            "reproductions/type_ii_initial_q_one_root_dispatch.py:initial_dispatch"
        )
        result = self.audit_mutation(inventory)
        self.assertFalse(result.ok)
        self.assertTrue(any("claims enqueue gate" in error for error in result.errors))

    def test_total_cofactor_queue_flag_remains_unassigned(self) -> None:
        inventory = load_inventory()
        rows = {
            row["anchor"]: row
            for row in inventory["source_signal_anchors"]
            if "type_i_overflow_total_cofactor_typed_adapter.py" in row["anchor"]
        }
        self.assertEqual(len(rows), 2)
        self.assertEqual({row["maps_to"] for row in rows.values()}, {"UNASSIGNED"})
        self.assertEqual(
            {row["disposition"] for row in rows.values()},
            {"UNREGISTERED_RELATIVE_ADAPTER_INPUT", "FIXTURE_MANUFACTURED_QUEUE_FLAG"},
        )

    def test_f1_cannot_be_upgraded_while_unknowns_remain(self) -> None:
        inventory = copy.deepcopy(load_inventory())
        inventory["closure_assessment"]["F1_reachable_state_exhaustion"] = "ESTABLISHED"
        result = self.audit_mutation(inventory)
        self.assertFalse(result.ok)
        self.assertTrue(any("upgrades F1" in error for error in result.errors))


if __name__ == "__main__":
    unittest.main()
