import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_pure_new_tail_mark_profile",
    ROOT / "reproductions" / "type_ii_h19_pure_new_tail_mark_profile.py",
)
assert SPEC and SPEC.loader
tail_mark = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = tail_mark
SPEC.loader.exec_module(tail_mark)


class TypeIIH19PureNewTailMarkProfileTests(unittest.TestCase):
    def test_known_pure_new_tail_witness_reconstructs_a_strict_source(self):
        witness = tail_mark.pure_new_tail_witness(
            345_601, 315, set(), tail_mark.single.primes_through(1_000)
        )
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(witness["h"], 5_879)
        self.assertEqual(witness["gap"], 59)
        self.assertEqual(witness["source_denominator"], 5_761)

    def test_shift_cap_is_validated(self):
        with self.assertRaises(ValueError):
            tail_mark.run_profile(
                {
                    "prime_limit": 100,
                    "base_shift_bound": 19,
                    "profiles": [],
                },
                19,
            )

    def test_checked_artifact_records_the_same_certificate_boundary(self):
        path = ROOT / "reproductions" / "type-ii-h19-pure-new-tail-mark-1b-s1008-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["new_factor_state_count"], 541)
        self.assertEqual(result["pure_new_tail_descent_count"], 282)
        self.assertEqual(len(result["missing_through_cap"]), 259)
        self.assertEqual(result["maximum_first_pure_new_tail_shift"], 1_000)
        record = next(row for row in result["records"] if row["prime"] == 345_601)
        self.assertEqual(record["first_pure_new_tail_shift"], 315)
        self.assertEqual(record["selected_witness"]["h"], 5_879)


if __name__ == "__main__":
    unittest.main()
