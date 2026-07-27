import importlib.util
import json
import math
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_global_tail_private_cofactors",
    ROOT / "reproductions" / "h19_k23_global_tail_private_cofactors.py",
)
assert SPEC and SPEC.loader
cofactors = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = cofactors
SPEC.loader.exec_module(cofactors)


class H19K23GlobalTailPrivateCofactorTests(unittest.TestCase):
    def test_collision_primes_are_exactly_the_menu_difference_primes(self):
        self.assertEqual(cofactors.collision_primes(), (2, 3, 5, 7, 11, 13))
        audit = cofactors.run_audit()
        self.assertEqual(audit["tail_gaps"], [31, 35, 39, 47, 59, 71, 79, 91, 95])
        self.assertEqual(audit["collision_primes"], [2, 3, 5, 7, 11, 13])

    def test_private_cofactors_are_pairwise_coprime_on_concrete_global_tail_points(self):
        for prime in (508_413_877_101_691_201, 1_431_455_361_734_959_201):
            checked = cofactors.verify_private_separation(prime)
            values = [row["private_cofactor"] for row in checked["tail_rows"]]
            self.assertEqual(len(values), 9)
            for index, value in enumerate(values):
                for other in values[index + 1 :]:
                    self.assertEqual(math.gcd(value, other), 1)

    def test_checked_artifact_matches_symbolic_menu_audit(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-private-cofactors.json"
        ).open(encoding="utf-8") as handle:
            artifact = json.load(handle)
        self.assertEqual(artifact, cofactors.run_audit())


if __name__ == "__main__":
    unittest.main()
