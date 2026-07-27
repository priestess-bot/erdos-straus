import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_global_tail_base_only_descent",
    ROOT / "reproductions" / "h19_k23_global_tail_base_only_descent.py",
)
assert SPEC and SPEC.loader
descent = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = descent
SPEC.loader.exec_module(descent)


class H19K23GlobalTailBaseOnlyDescentTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_both_inputs(self):
        with (
            ROOT / "reproductions" / "h19-k23-full-global-tail-closure-1048576.json"
        ).open(encoding="utf-8") as handle:
            global_payload = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-one-support-closure-1048576.json"
        ).open(encoding="utf-8") as handle:
            one_support_payload = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-base-only-descent-1048576.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(descent.run_audit(global_payload, one_support_payload), checked)

    def test_only_twelve_global_base_only_pressure_records_remain(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-base-only-descent-1048576.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["input_parameter_limit_exclusive"], 1_048_576)
        self.assertEqual(result["input_rewrite_count"], 5_254)
        self.assertEqual(result["initial_base_only_count"], 2_512)
        self.assertEqual(result["input_one_support_count"], 2_742)
        self.assertEqual(result["later_base_only_reroute_count"], 2_730)
        self.assertEqual(result["base_only_rewrite_count"], 5_242)
        self.assertEqual(result["global_base_only_pressure_count"], 12)
        self.assertTrue(
            all(
                row["new_global_tail_gap"] > row["current_global_tail_gap"]
                and row["new_support_defect"] == 0
                for row in result["base_only_reroutes"]
            )
        )
        self.assertTrue(
            all(
                row["shared_selector_gap"] == 27
                and row["current_global_tail_gap"] in {31, 35, 39}
                for row in result["global_base_only_pressure_records"]
            )
        )


if __name__ == "__main__":
    unittest.main()
