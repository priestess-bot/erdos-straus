import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_overflow_total_cofactor_typed_adapter",
    ROOT / "reproductions" / "type_i_overflow_total_cofactor_typed_adapter.py",
)
assert SPEC and SPEC.loader
adapter = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = adapter
SPEC.loader.exec_module(adapter)


class TotalCofactorTypedAdapterTests(unittest.TestCase):
    def registered(self, state):
        return adapter.registration(
            state,
            parent_receipt_digest="unit-parent",
            terminal_first_digest="unit-terminal-miss",
            terminal_first_miss=True,
            persistent_queue=True,
        )

    def test_retypes_f_to_g_and_preserves_scope(self):
        source = adapter.fixture_source(3, 45, 15, 37, "fresh_source_tree_only")
        result = adapter.verify_transition(
            source, self.registered(source), M=45, d=15, n=37
        )
        self.assertEqual(result["kind"], "relative_verified_edge")
        self.assertEqual(result["source"]["typed_classification"], "F")
        self.assertEqual(result["target"]["typed_classification"], "G")
        self.assertEqual(result["target"]["source_tree_scope"], "fresh_source_tree_only")
        self.assertEqual(result["edge"]["t5_ticket"], "LOCAL_DROP")

    def test_retypes_g_to_f_with_exact_separator(self):
        source = adapter.fixture_source(22, 220, 18, 217)
        result = adapter.verify_transition(
            source, self.registered(source), M=220, d=18, n=217
        )
        self.assertEqual(result["kind"], "relative_verified_edge")
        self.assertEqual(result["source"]["typed_classification"], "G")
        self.assertEqual(result["target"]["typed_classification"], "F")
        separator = source["target_fiber"]["emptiness_certificate"]
        self.assertTrue(separator["target_separated"])
        self.assertTrue(separator["generator_phases_integral"])

    def test_hit_target_becomes_root_terminal(self):
        source = adapter.fixture_source(5, 40, 26, 57)
        result = adapter.verify_transition(
            source, self.registered(source), M=40, d=26, n=57
        )
        self.assertEqual(result["kind"], "terminal_leaf")
        self.assertEqual(result["terminal"]["egyptian_denominators"], [22, 110, 4015])

    def test_rejects_stutter_transient_and_priority_gap(self):
        canonical = adapter.build_state(73, 11, 3, "charged_history_only")
        with self.assertRaisesRegex(ValueError, "nondecreasing stutter"):
            adapter.verify_transition(
                canonical, self.registered(canonical), M=3, d=6, n=1
            )

        source = adapter.fixture_source(3, 45, 15, 37)
        transient = self.registered(source)
        transient["persistent_queue"] = False
        with self.assertRaisesRegex(ValueError, "transient"):
            adapter.verify_transition(source, transient, M=45, d=15, n=37)

        missing_parent = self.registered(source)
        missing_parent["parent_receipt_digest"] = ""
        with self.assertRaisesRegex(ValueError, "parent receipt"):
            adapter.verify_transition(source, missing_parent, M=45, d=15, n=37)

        missing_priority = self.registered(source)
        missing_priority["terminal_first_miss"] = False
        with self.assertRaisesRegex(ValueError, "terminal-first"):
            adapter.verify_transition(source, missing_priority, M=45, d=15, n=37)


if __name__ == "__main__":
    unittest.main()
