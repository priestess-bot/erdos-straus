from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest

import sympy


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_linear_single_hit_quadratic_compatibility_7.py"
RESULT = ROOT / "reproductions" / "type-i-linear-single-hit-quadratic-compatibility-7-results.json"

SPEC = importlib.util.spec_from_file_location("single_hit_quadratic_compatibility_7", SCRIPT)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeILinearSingleHitQuadraticCompatibility7Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = profile.run_audit()
        cls.stored = json.loads(RESULT.read_text(encoding="utf-8"))

    def test_reproduction_matches_artifact_and_totals(self):
        self.assertEqual(self.payload, self.stored)
        self.assertEqual(self.payload["primes"], list(profile.SINGLE_HIT_PRIMES))
        self.assertEqual(self.payload["quadratic_subgroup_character_R_count"], 185)
        self.assertEqual(self.payload["higher_order_subgroup_character_R_count"], 1)
        self.assertEqual(self.payload["pair_with_shared_odd_prime_count"], 1_132)
        self.assertEqual(self.payload["shared_odd_prime_relation_count"], 1_397)

    def test_every_stored_relation_satisfies_the_two_compatibility_conditions(self):
        for profile_record in self.payload["profiles"]:
            for relation in profile_record["relations"]:
                difference = abs(int(relation["left_R"]) - int(relation["right_R"])) // 4
                q = int(relation["shared_odd_prime"])
                self.assertEqual(difference % q, 0)
                self.assertEqual(
                    int(sympy.jacobi_symbol(
                        int(relation["left_conductor"])
                        * int(relation["right_conductor"]),
                        q,
                    )),
                    1,
                )

    def test_only_one_higher_order_state_is_present(self):
        higher = [
            profile_record["prime"]
            for profile_record in self.payload["profiles"]
            if profile_record["higher_order_subgroup_character_R_count"]
        ]
        self.assertEqual(higher, [57_399_241])


if __name__ == "__main__":
    unittest.main()
