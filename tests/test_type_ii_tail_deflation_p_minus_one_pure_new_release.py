import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_deflation_p_minus_one_pure_new_release",
    ROOT
    / "reproductions"
    / "type_ii_tail_deflation_p_minus_one_pure_new_release.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIITailDeflationPMinusOnePureNewReleaseTests(unittest.TestCase):
    def test_every_two_shift_residual_has_a_pure_new_one_prime_release(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-tail-deflation-p-minus-one-pure-new-release-50m-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 50_000_000)
        self.assertEqual(result["base_shift_cap"], 2)
        self.assertEqual(result["release_shift_cap"], 5)
        self.assertEqual(result["residual_count"], 4)
        self.assertEqual(result["pure_new_one_prime_release_count"], 4)
        self.assertEqual(result["non_pure_new_primes"], [])
        self.assertEqual(
            [
                (row["prime"], row["first_release_shift"], row["h"])
                for row in result["records"]
            ],
            [
                (25_073_689, 3, 47),
                (33_011_449, 3, 3_347),
                (42_622_969, 4, 31),
                (48_825_529, 5, 239),
            ],
        )


if __name__ == "__main__":
    unittest.main()
