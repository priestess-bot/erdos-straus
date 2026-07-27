import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_global_tail_one_support_closure",
    ROOT / "reproductions" / "h19_k23_global_tail_one_support_closure.py",
)
assert SPEC and SPEC.loader
closure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = closure
SPEC.loader.exec_module(closure)


class H19K23GlobalTailOneSupportClosureTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_global_closure_input(self):
        with (
            ROOT / "reproductions" / "h19-k23-full-global-tail-closure-1048576.json"
        ).open(encoding="utf-8") as handle:
            source = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-one-support-closure-1048576.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(closure.run_audit(source), checked)

    def test_checked_artifact_eliminates_every_support_two_rewrite(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-one-support-closure-1048576.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["input_parameter_limit_exclusive"], 1_048_576)
        self.assertEqual(result["input_rewrite_count"], 5_254)
        self.assertEqual(result["retained_support_zero_or_one_count"], 5_214)
        self.assertEqual(result["rerouted_support_two_count"], 40)
        self.assertEqual(sum(result["final_rewrite_support_histogram"].values()), 5_254)
        self.assertNotIn("2", result["final_rewrite_support_histogram"])
        self.assertTrue(all(row["new_global_tail_gap"] > row["old_global_tail_gap"] for row in result["reroutes"]))
        self.assertTrue(all(row["new_support_defect"] <= 1 for row in result["reroutes"]))


if __name__ == "__main__":
    unittest.main()
