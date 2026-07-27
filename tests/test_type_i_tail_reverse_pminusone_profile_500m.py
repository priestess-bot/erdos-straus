import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_tail_reverse_pminusone_profile_500m",
    ROOT / "reproductions" / "type_i_tail_reverse_pminusone_profile_500m.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeITailReversePMinusOneProfile500MTests(unittest.TestCase):
    def test_known_pminusone_witness_rebuilds(self):
        witness, forms, lifts = profile.first_pminusone_edge(67_369, 215)
        self.assertGreater(forms, 0)
        self.assertGreater(lifts, 0)
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(witness["source_denominator"], 67_368)
        self.assertLess(witness["a"], witness["b"])

    def test_profile_artifact_partitions_the_complete_residual(self):
        closure = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-even-source-closure-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        result = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-pminusone-profile-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(result["ordinary_tail_residual_count"], len(closure["records"]))
        self.assertEqual(
            (result["p_minus_one_captured_count"], len(result["p_minus_one_misses"])),
            (1_532, 185),
        )
        self.assertEqual(result["p_minus_one_misses"][0], 297_049)
        self.assertEqual(
            result["p_minus_one_captured_count"] + len(result["p_minus_one_misses"]),
            result["ordinary_tail_residual_count"],
        )
        for record in result["records"]:
            self.assertEqual(record["p_minus_one_witness"]["source_denominator"], record["prime"] - 1)


if __name__ == "__main__":
    unittest.main()
