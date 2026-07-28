import importlib.util
import itertools
import json
import math
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_linear_cross_modulus_layer_profile_600m.py"
RESULT = (
    ROOT
    / "reproductions"
    / "type-i-linear-cross-modulus-layer-profile-600m-results.json"
)
INPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-general-b-obstruction-mixture-profile-600m-results.json"
)

spec = importlib.util.spec_from_file_location("cross_modulus_layers_600m", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


def direct_spectrum(factors, modulus):
    residues = {1}
    for prime, exponent in factors:
        powers = [
            pow(prime, coordinate, modulus)
            for coordinate in range(-exponent, exponent + 1)
        ]
        residues = {
            left * right % modulus for left in residues for right in powers
        }
    return residues


class LinearCrossModulusLayerProfile600MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = module.run_audit()
        cls.checked = json.loads(RESULT.read_text(encoding="utf-8"))
        cls.source = json.loads(INPUT.read_text(encoding="utf-8"))

    def test_checked_artifact_matches_complete_run(self):
        self.assertEqual(self.actual, self.checked)
        self.assertEqual(
            self.actual["aggregate_cross_modulus_layer_classification_counts"],
            {
                "both_layers_hit": 3,
                "excess_layer_hit": 1,
                "mixed_layers_required": 11,
                "shared_layer_hit": 5,
            },
        )
        self.assertEqual(
            self.actual["mixed_layer_minimum_excess_support_counts"],
            {"1": 10, "2": 1},
        )

    def test_all_278_source_modulus_pairs_obey_the_gcd_identity(self):
        for profile in self.source["profiles"]:
            prime = int(profile["prime"])
            records = profile["records"]
            for left, right in itertools.combinations(records, 2):
                R_left = int(left["R"])
                R_right = int(right["R"])
                K_left = (prime * R_left + 1) // 4
                K_right = (prime * R_right + 1) // 4
                self.assertEqual((R_left - R_right) % 4, 0)
                self.assertEqual(
                    math.gcd(K_left, K_right),
                    math.gcd(K_left, abs(R_left - R_right) // 4),
                )

    def test_layer_spectra_reconstruct_all_twenty_target_hits(self):
        for profile in self.actual["profiles"]:
            for record in profile["records"]:
                modulus = int(record["R"])
                factor_groups = [
                    [
                        (int(item["prime"]), int(item["exponent"]))
                        for item in record[key]
                    ]
                    for key in (
                        "K_factorization",
                        "shared_layer_factorization",
                        "excess_layer_factorization",
                    )
                ]
                full, shared, excess = [
                    direct_spectrum(factors, modulus) for factors in factor_groups
                ]
                self.assertEqual(
                    full,
                    {
                        left * right % modulus
                        for left in shared
                        for right in excess
                    },
                )
                self.assertIn(modulus - 1, full)


if __name__ == "__main__":
    unittest.main()
