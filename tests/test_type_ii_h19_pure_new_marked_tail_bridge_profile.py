import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_pure_new_marked_tail_bridge_profile",
    ROOT / "reproductions" / "type_ii_h19_pure_new_marked_tail_bridge_profile.py",
)
assert SPEC and SPEC.loader
bridge = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = bridge
SPEC.loader.exec_module(bridge)


class TypeIIH19PureNewMarkedTailBridgeProfileTests(unittest.TestCase):
    def load(self, name):
        with (ROOT / "reproductions" / name).open(encoding="utf-8") as handle:
            return json.load(handle)

    def test_artifact_rebuilds_from_the_checked_input_profiles(self):
        marked = self.load("type-ii-h19-pure-new-scaled-tail-1b-s1008-results.json")
        tails = self.load("type-ii-h19-tail-deflation-short-closure-1b-results.json")
        closure = self.load("type-ii-h19-all-strict-descent-closure-1b-results.json")
        checked = self.load("type-ii-h19-pure-new-marked-tail-bridge-1b-results.json")
        self.assertEqual(bridge.run_profile(marked, tails, closure), checked)

    def test_marked_misses_have_one_external_and_210_independent_two_tails(self):
        result = self.load("type-ii-h19-pure-new-marked-tail-bridge-1b-results.json")
        self.assertEqual(result["pure_new_marked_miss_count"], 211)
        self.assertEqual(result["independent_two_tail_count"], 210)
        self.assertEqual(result["adaptive_external_count"], 1)
        self.assertEqual(result["unclosed_primes"], [])
        self.assertEqual(result["independent_tail_gap_at_most_23"], 194)
        self.assertEqual(result["independent_tail_gap_at_most_63"], 206)
        self.assertEqual(result["maximum_minimal_independent_tail_gap"], 171)
        self.assertEqual(result["high_gap_record_count"], 16)
        self.assertEqual(
            result["adaptive_external_records"],
            [
                {
                    "prime": 225_289,
                    "source_denominator": 197_128,
                    "k": 2,
                    "q": 7,
                    "factor": 41,
                    "gap": 47,
                }
            ],
        )

    def test_high_gap_pressure_list_is_complete_and_ordered(self):
        result = self.load("type-ii-h19-pure-new-marked-tail-bridge-1b-results.json")
        records = result["high_gap_records"]
        self.assertEqual(
            [(record["gap"], record["prime"]) for record in records],
            sorted((record["gap"], record["prime"]) for record in records),
        )
        self.assertEqual(
            [(record["prime"], record["gap"]) for record in records[-4:]],
            [
                (227_018_089, 71),
                (334_152_361, 119),
                (201_866_569, 135),
                (165_882_649, 171),
            ],
        )


if __name__ == "__main__":
    unittest.main()
