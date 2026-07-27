import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_hybrid_short_or_descent",
    ROOT / "reproductions" / "type_ii_h19_hybrid_short_or_descent.py",
)
assert SPEC and SPEC.loader
hybrid = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = hybrid
SPEC.loader.exec_module(hybrid)


class TypeIIH19HybridShortOrDescentTests(unittest.TestCase):
    def test_three_hundred_million_checked_artifact(self):
        path = ROOT / "reproductions" / "type-ii-h19-hybrid-short-or-descent-300m-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 300_000_000)
        self.assertEqual(result["h19_residual_count"], 328)
        self.assertEqual(result["quadratic_descent_count"], 325)
        self.assertEqual(result["pure_type_ii_fallback_count"], 3)
        self.assertEqual(result["unclosed_primes"], [])
        self.assertEqual(
            [(row["prime"], row["shift"], row["selected_witness"]["h"]) for row in result["fallback_records"]],
            [(35_840_809, 45, 31_139), (132_285_169, 27, 107), (141_326_089, 63, 83)],
        )

    def test_five_hundred_million_checked_artifact(self):
        path = ROOT / "reproductions" / "type-ii-h19-hybrid-short-or-descent-500m-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 500_000_000)
        self.assertEqual(result["h19_residual_count"], 425)
        self.assertEqual(result["quadratic_descent_count"], 422)
        self.assertEqual(result["pure_type_ii_fallback_count"], 3)
        self.assertEqual(result["unclosed_primes"], [])

    def test_one_billion_checked_artifact(self):
        path = ROOT / "reproductions" / "type-ii-h19-hybrid-short-or-descent-1b-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["h19_residual_count"], 664)
        self.assertEqual(result["quadratic_descent_count"], 660)
        self.assertEqual(result["pure_type_ii_fallback_count"], 4)
        self.assertEqual(result["unclosed_primes"], [])
        self.assertEqual(
            [(row["prime"], row["shift"], row["selected_witness"]["h"]) for row in result["fallback_records"]],
            [
                (35_840_809, 45, 31_139),
                (132_285_169, 27, 107),
                (141_326_089, 63, 83),
                (640_775_689, 45, 359),
            ],
        )

    def test_quadratic_descent_misses_have_radius_six_direct_ac_certificates(self):
        with (ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-1b-results.json").open(encoding="utf-8") as handle:
            descent = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-residual-ac-profile-1b-results.json").open(encoding="utf-8") as handle:
            ac_profile = json.load(handle)
        ac_by_prime = {row["prime"]: row["direct_ac_witness"] for row in ac_profile["records"]}
        misses = [
            row["prime"]
            for row in descent["records"]
            if row["quadratic_factor_external_source_descent"] is None
        ]
        self.assertEqual(misses, [35_840_809, 132_285_169, 141_326_089, 640_775_689])
        self.assertEqual(
            {
                prime: {
                    key: ac_by_prime[prime][key]
                    for key in ("radius", "a", "c", "k", "h")
                }
                for prime in misses
            },
            {
                35_840_809: {"radius": 4, "a": 4, "c": 3, "k": 944, "h": 45_311},
                132_285_169: {"radius": 3, "a": 3, "c": 3, "k": 3, "h": 107},
                141_326_089: {"radius": 4, "a": 4, "c": 3, "k": 41_469, "h": 1_990_511},
                640_775_689: {"radius": 5, "a": 3, "c": 5, "k": 6, "h": 359},
            },
        )


if __name__ == "__main__":
    unittest.main()
