import importlib.util
import itertools
import json
import math
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_linear_cross_modulus_layer_profile_500m.py"
RESULT = (
    ROOT
    / "reproductions"
    / "type-i-linear-cross-modulus-layer-profile-500m-results.json"
)
INPUT = (
    ROOT
    / "reproductions"
    / "type-i-global-linear-b1-failure-general-b-profile-500m-results.json"
)

spec = importlib.util.spec_from_file_location("cross_modulus_layers", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


def direct_centered_spectrum(factors, modulus):
    residues = {1}
    for prime, exponent in factors:
        powers = [
            pow(prime, coordinate, modulus)
            for coordinate in range(-exponent, exponent + 1)
        ]
        residues = {
            residue * power % modulus
            for residue in residues
            for power in powers
        }
    return residues


class LinearCrossModulusLayerProfile500MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = module.run_audit()
        cls.checked = json.loads(RESULT.read_text(encoding="utf-8"))
        cls.source = json.loads(INPUT.read_text(encoding="utf-8"))

    def test_checked_artifact_matches_complete_run(self):
        self.assertEqual(self.actual, self.checked)
        self.assertEqual(
            self.actual["aggregate_cross_modulus_layer_classification_counts"],
            {"mixed_layers_required": 9, "shared_layer_hit": 3},
        )

    def test_pairwise_identity_is_independently_recomputed(self):
        for profile in self.source["general_B_failure_profiles"]:
            records = sorted(profile["records"], key=lambda record: int(record["R"]))
            for left, right in itertools.combinations(records, 2):
                R_left = int(left["R"])
                R_right = int(right["R"])
                self.assertEqual((R_left - R_right) % 4, 0)
                expected = math.gcd(
                    int(left["K"]), abs(R_left - R_right) // 4
                )
                self.assertEqual(math.gcd(int(left["K"]), int(right["K"])), expected)

    def test_layer_products_reconstruct_each_centered_target_spectrum(self):
        result_profiles = {
            int(profile["prime"]): profile for profile in self.actual["profiles"]
        }
        for source_profile in self.source["general_B_failure_profiles"]:
            prime = int(source_profile["prime"])
            for record in result_profiles[prime]["records"]:
                modulus = int(record["R"])
                full_factors = [
                    (int(item["prime"]), int(item["exponent"]))
                    for item in record["K_factorization"]
                ]
                shared_factors = [
                    (int(item["prime"]), int(item["exponent"]))
                    for item in record["shared_layer_factorization"]
                ]
                excess_factors = [
                    (int(item["prime"]), int(item["exponent"]))
                    for item in record["excess_layer_factorization"]
                ]
                self.assertEqual(
                    int(record["shared_layer"]) * int(record["excess_layer"]),
                    int(record["K"]),
                )
                full = direct_centered_spectrum(full_factors, modulus)
                shared = direct_centered_spectrum(shared_factors, modulus)
                excess = direct_centered_spectrum(excess_factors, modulus)
                product = {
                    left * right % modulus for left in shared for right in excess
                }
                self.assertEqual(full, product)
                self.assertIn(modulus - 1, full)
                classification = record[
                    "target_hit_cross_modulus_layer_classification"
                ]
                if classification == "mixed_layers_required":
                    self.assertNotIn(modulus - 1, shared)
                    self.assertNotIn(modulus - 1, excess)
                elif classification == "shared_layer_hit":
                    self.assertIn(modulus - 1, shared)
                    self.assertNotIn(modulus - 1, excess)
                else:
                    self.fail(f"unexpected frozen classification: {classification}")


if __name__ == "__main__":
    unittest.main()
