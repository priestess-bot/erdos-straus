import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_full_global_tail_closure",
    ROOT / "reproductions" / "h19_k23_full_global_tail_closure.py",
)
assert SPEC and SPEC.loader
closure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = closure
SPEC.loader.exec_module(closure)


class H19K23FullGlobalTailClosureTests(unittest.TestCase):
    def test_global_tail_menu_has_the_expected_common_factor(self):
        global_factor, bases = closure.global_tail_bases()
        self.assertEqual(global_factor, 165_600)
        self.assertEqual(len(bases), 72)
        self.assertEqual(bases[31], {2, 7, 19})
        self.assertEqual(bases[159], {2, 5})

    def test_checked_artifact_rewrites_every_record_globally(self):
        with (
            ROOT / "reproductions" / "h19-k23-full-global-tail-closure-1048576.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["input_parameter_limit_exclusive"], 1_048_576)
        self.assertEqual(result["input_record_count"], 2_270_418)
        self.assertEqual(result["direct_global_tail_count"], 2_265_164)
        self.assertEqual(result["rewritten_global_tail_count"], 5_254)
        self.assertEqual(result["global_tail_misses"], [])
        self.assertEqual(sum(result["rewrite_support_defect_histogram"].values()), 5_254)


if __name__ == "__main__":
    unittest.main()
