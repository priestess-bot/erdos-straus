import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "targeted_descent_bridge",
    ROOT / "reproductions" / "targeted_descent_bridge.py",
)
assert SPEC and SPEC.loader
targeted_bridge = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = targeted_bridge
SPEC.loader.exec_module(targeted_bridge)


class TargetedDescentBridgeTests(unittest.TestCase):
    def test_reverse_lift_formula_finds_a_known_local_lift(self):
        lifts = targeted_bridge.reverse_two_tail_lifts(73, 4_015)
        self.assertIn(
            {"source_denominator": 33, "source_term": 15},
            lifts,
        )

    def test_first_composite_escape_has_no_two_tail_bridge_for_selected_ray(self):
        result = targeted_bridge.run_audit(2_451_289, 1, 2, 13)
        self.assertEqual(
            result["type_ii_raw_ray"],
            {
                "a": 1,
                "c": 2,
                "k": 13,
                "h": 103,
                "gap": 23_799,
                "x": 618_772,
                "divisor": 2,
                "y": 63_733_514,
                "z": 19_718_256_962_404,
            },
        )
        self.assertEqual(result["total_reverse_two_tail_lifts"], 0)

    def test_targeted_bridge_artifact(self):
        with (
            ROOT / "reproductions" / "targeted-bridge-2451289-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime"], 2_451_289)
        self.assertEqual(result["total_reverse_two_tail_lifts"], 0)

    def test_bounded_ac_first_term_artifact(self):
        with (
            ROOT / "reproductions" / "targeted-bridge-2451289-ac14-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        audit = result["ac_first_term_audit"]
        self.assertEqual(audit["ac_bound"], 14)
        self.assertEqual(audit["distinct_target_solutions"], 21)
        self.assertEqual(audit["solutions_with_first_term_bridge"], 0)
