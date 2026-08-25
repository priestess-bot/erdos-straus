from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "t6-wave1" / "family-grammar-freeze-v1.json"
SPEC = importlib.util.spec_from_file_location(
    "t6_persistent_selector_state_v1_for_grammar",
    ROOT / "scripts" / "t6_persistent_selector_state_v1.py",
)
assert SPEC and SPEC.loader
contract = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = contract
SPEC.loader.exec_module(contract)


class Wave1FamilyGrammarFreezeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_manifest_matches_executable_owner_precedence(self) -> None:
        grammar = self.manifest["grammar"]
        self.assertEqual(
            tuple(grammar["persistent_owner_precedence"]),
            contract.FAMILY_PRECEDENCE_V1,
        )

    def test_only_declared_overflow_refinements_may_overlap(self) -> None:
        overlap_classes = self.manifest["grammar"]["allowed_overlap_class"]
        overflow = frozenset(overlap_classes["overflow_refinement_only"])
        expected = frozenset(
            frozenset({left, right})
            for left in overflow
            for right in overflow
            if left != right
        )
        expected |= frozenset(
            frozenset({lineage, overflow_owner})
            for lineage, overflow_owners in overlap_classes[
                "lineage_overflow_refinements"
            ].items()
            for overflow_owner in overflow_owners
        )
        self.assertEqual(contract.ALLOWED_FAMILY_OVERLAPS_V1, expected)

    def test_pending_atomic_target_is_not_a_persistent_owner(self) -> None:
        grammar = self.manifest["grammar"]
        self.assertEqual(grammar["persistent_pending_families"], [])
        self.assertNotIn(
            "t2_v1_atomic_pending_target",
            grammar["persistent_owner_precedence"],
        )
        self.assertEqual(
            set(grammar["edge_receipt_atomic_arms"]),
            {"H4_A1", "C8_DOUBLE_LOW"},
        )

    def test_new_owners_are_exact_not_fallbacks(self) -> None:
        owners = set(self.manifest["grammar"]["persistent_owner_precedence"])
        self.assertIn("proper_root_high_endpoint", owners)
        self.assertIn("type_i_absorb_marked_residual", owners)
        decisions = {
            item["decision_id"]: item
            for item in self.manifest["target_shape_decisions"]
        }
        self.assertEqual(
            decisions["QC1_NEW_FAMILY_CANDIDATE"]["decision"],
            "REJECT_UNTIL_INTEGER_OCCURRENCE_THEOREM",
        )
        self.assertEqual(
            decisions["F2_OPEN_RESIDUAL_LABELS"]["decision"],
            "REJECT_GENERIC_RESIDUAL_FAMILY",
        )

    def test_grammar_hash_is_canonical(self) -> None:
        completed = subprocess.run(
            ["jq", "-cS", ".grammar", str(MANIFEST)],
            check=True,
            capture_output=True,
        )
        digest = hashlib.sha256(completed.stdout).hexdigest()
        self.assertEqual(self.manifest["grammar_hash"], digest)


if __name__ == "__main__":
    unittest.main()
