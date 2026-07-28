import importlib.util
import json
from pathlib import Path
import sys
import unittest

import sympy


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_linear_general_b_obstruction_mixture_profile_600m.py"
RESULT = ROOT / "reproductions" / "type-i-linear-general-b-obstruction-mixture-profile-600m-results.json"

SPEC = importlib.util.spec_from_file_location("linear_general_b_obstruction_mixture", SCRIPT)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeILinearGeneralBObstructionMixtureProfile600MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = profile.run_audit()
        cls.profiles = {
            int(item["prime"]): item for item in cls.payload["profiles"]
        }

    def test_hash_frozen_input_and_reproducible_artifact(self):
        self.assertEqual(self.payload, json.loads(RESULT.read_text(encoding="utf-8")))
        self.assertEqual(profile.load_primes(), list(profile.EXPECTED_PER_PRIME))
        self.assertEqual(
            (
                self.payload["input_prime_count"],
                self.payload["linear_R_count"],
                self.payload["directed_linear_source_state_count"],
                self.payload["classification_totals"],
            ),
            (7, 278, 490, profile.EXPECTED_TOTALS),
        )

    def test_each_failure_class_has_its_exact_membership_meaning(self):
        for item in self.profiles.values():
            counts = {"hit": 0, "finite_exponent": 0, "subgroup_character": 0}
            for record in item["records"]:
                kind = record["classification"]
                counts[kind] += 1
                target_hits = int(record["target_divisor_hit_count"])
                in_group = bool(record["target_in_generated_subgroup"])
                if kind == "hit":
                    self.assertGreater(target_hits, 0)
                    self.assertTrue(in_group)
                elif kind == "finite_exponent":
                    self.assertEqual(target_hits, 0)
                    self.assertTrue(in_group)
                else:
                    self.assertEqual(kind, "subgroup_character")
                    self.assertEqual(target_hits, 0)
                    self.assertFalse(in_group)
            self.assertEqual(counts, item["classification_counts"])

    def test_direct_square_divisor_oracle_agrees_with_all_278_classes(self):
        for prime, item in self.profiles.items():
            for record in item["records"]:
                R = int(record["R"])
                K = (prime * R + 1) // 4
                direct_hits = [
                    int(divisor)
                    for divisor in sympy.divisors(K * K)
                    if (4 * int(divisor) + 1) % R == 0
                ]
                self.assertEqual(len(direct_hits), record["target_divisor_hit_count"])
                self.assertEqual(bool(direct_hits), record["classification"] == "hit")

    def test_878089_slice_agrees_with_its_existing_complete_profile(self):
        item = self.profiles[878_089]
        self.assertEqual(item["classification_counts"], {
            "hit": 1,
            "finite_exponent": 2,
            "subgroup_character": 21,
        })
        self.assertEqual(item["hit_R"], [59])
        self.assertEqual(item["finite_exponent_R"], [279, 503])


if __name__ == "__main__":
    unittest.main()
