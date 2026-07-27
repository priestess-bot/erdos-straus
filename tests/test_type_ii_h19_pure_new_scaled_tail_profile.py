import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_pure_new_scaled_tail_profile",
    ROOT / "reproductions" / "type_ii_h19_pure_new_scaled_tail_profile.py",
)
assert SPEC and SPEC.loader
scaled_profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = scaled_profile
SPEC.loader.exec_module(scaled_profile)


class TypeIIH19PureNewScaledTailProfileTests(unittest.TestCase):
    def test_scaled_only_witness_reconstructs_a_marked_strict_source(self):
        witness = scaled_profile.pure_new_scaled_tail_witness(
            176_089, 238, set(), scaled_profile.single.primes_through(1_000)
        )
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(witness["h"], 5_711)
        self.assertEqual(witness["gap"], 31)
        self.assertEqual(witness["shared_divisor"], 280)
        self.assertEqual(witness["first_scale"], 9)
        self.assertEqual(witness["source_denominator"], 5_661)

    def test_shift_cap_is_validated(self):
        with self.assertRaises(ValueError):
            scaled_profile.run_profile(
                {
                    "prime_limit": 100,
                    "base_shift_bound": 19,
                    "profiles": [],
                },
                19,
            )

    def test_checked_artifact_separates_unscaled_and_scaled_only_states(self):
        path = ROOT / "reproductions" / "type-ii-h19-pure-new-scaled-tail-1b-s1008-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["new_factor_state_count"], 541)
        self.assertEqual(result["pure_new_scaled_tail_count"], 330)
        self.assertEqual(result["ordinary_same_certificate_tail_count"], 282)
        self.assertEqual(result["scaled_only_count"], 48)
        self.assertEqual(len(result["missing_through_cap"]), 211)
        self.assertEqual(result["maximum_first_pure_new_scaled_tail_shift"], 1_000)
        self.assertIn(176_089, result["scaled_only_primes"])
        record = next(row for row in result["records"] if row["prime"] == 176_089)
        self.assertEqual(record["first_pure_new_scaled_tail_shift"], 238)
        self.assertEqual(record["selected_witness"]["first_scale"], 9)

    def test_marked_tail_misses_have_an_independent_finite_descent_closure(self):
        with (
            ROOT / "reproductions" / "type-ii-h19-pure-new-scaled-tail-1b-s1008-results.json"
        ).open(encoding="utf-8") as handle:
            marked = json.load(handle)
        with (
            ROOT / "reproductions" / "type-ii-h19-tail-deflation-short-closure-1b-results.json"
        ).open(encoding="utf-8") as handle:
            tails = json.load(handle)
        marked_misses = set(marked["missing_through_cap"])
        ordinary_tail_primes = {record["prime"] for record in tails["tail_records"]}
        self.assertEqual(len(marked_misses & ordinary_tail_primes), 210)
        self.assertEqual(marked_misses - ordinary_tail_primes, {225_289})


if __name__ == "__main__":
    unittest.main()
