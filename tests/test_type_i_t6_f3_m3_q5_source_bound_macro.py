import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_t6_f3_m3_q5_source_bound_macro",
    ROOT / "reproductions" / "type_i_t6_f3_m3_q5_source_bound_macro.py",
)
assert SPEC and SPEC.loader
macro = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = macro
SPEC.loader.exec_module(macro)


class TypeIT6F3M3Q5SourceBoundMacroTests(unittest.TestCase):
    def test_source_path_is_content_bound_and_replayable(self):
        receipt = macro.source_path_receipt(
            73, 3, state_id="test-state", scope="charged_history_only"
        )
        payload = dict(receipt)
        observed = payload.pop("digest")
        self.assertEqual(observed, macro.digest(payload))
        self.assertEqual(receipt["root_endpoint"], (3, 2_328_260))
        self.assertEqual(receipt["state_id"], "test-state")

    def test_missing_scope_is_not_silently_accepted(self):
        first = macro.source_path_receipt(
            73, 3, state_id="test-state", scope="charged_history_only"
        )
        second = macro.source_path_receipt(
            73, 3, state_id="test-state", scope="fresh_source_tree_only"
        )
        self.assertNotEqual(first["digest"], second["digest"])

    def test_strict_high_target_gets_local_drop(self):
        source = macro.chart(73, 1)
        result = macro.serialize_endpoint(
            prime=73,
            support=source["A"],
            capacity=source["K"],
            residual=source["R"],
            left=761_905,
            right=10_582,
        )
        self.assertEqual(result["target_shape"], "TYPEI_CHARGED_OVERFLOW")
        self.assertEqual(result["T5_ticket"], "LOCAL_DROP")
        self.assertLess(result["target_cofactor"], 72)

    def test_p_stutter_has_no_standalone_ticket(self):
        source = macro.chart(73, 50)
        result = macro.serialize_endpoint(
            prime=73,
            support=source["A"],
            capacity=source["K"],
            residual=source["R"],
            left=38_356_274,
            right=532_725,
        )
        self.assertEqual(result["target_shape"], "P2_OR_OTHER_P_STUTTER_CHECKPOINT")
        self.assertIsNone(result["T5_ticket"])
        self.assertEqual(result["target_cofactor"], 72)

    def test_manifest_keeps_math_and_integration_gaps_open(self):
        result = macro.run()
        self.assertEqual(
            result["status"],
            "PARTIAL_MATHEMATICAL_CLOSURE_INTEGRATION_AND_P2_OPEN",
        )
        self.assertIn("R2_M3_Q5_NONMINIMAL_ROOT_RESIDUE", result["open_leaf_ids"])
        self.assertIn("R2_M3_Q5_SHORT_TWO_SIDED_P2", result["open_leaf_ids"])
        self.assertFalse(result["control_summary"]["fixtures_are_actual_track_evidence"])


if __name__ == "__main__":
    unittest.main()
