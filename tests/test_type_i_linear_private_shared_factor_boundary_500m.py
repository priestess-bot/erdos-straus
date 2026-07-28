import importlib.util
import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path
import unittest

import sympy


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_linear_private_shared_factor_boundary_500m.py"
RESULT = (
    ROOT
    / "reproductions"
    / "type-i-linear-private-shared-factor-boundary-500m-results.json"
)
INPUT = (
    ROOT
    / "reproductions"
    / "type-i-global-linear-b1-failure-general-b-profile-500m-results.json"
)

spec = importlib.util.spec_from_file_location("private_shared_boundary", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


def direct_centered_spectrum(factors, modulus):
    residues = set()
    for vector in itertools.product(
        *(range(-exponent, exponent + 1) for _, exponent in factors)
    ):
        residue = 1
        for (prime, _), coordinate in zip(factors, vector):
            residue = residue * pow(prime, coordinate, modulus) % modulus
        residues.add(residue)
    return residues


class LinearPrivateSharedFactorBoundary500MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = module.run_audit()
        cls.checked = json.loads(RESULT.read_text(encoding="utf-8"))
        cls.source = json.loads(INPUT.read_text(encoding="utf-8"))

    def test_checked_artifact_matches_complete_run(self):
        self.assertEqual(self.checked, self.actual)

    def test_private_shared_partition_and_spectra_are_independently_recomputed(self):
        source_profiles = {
            int(profile["prime"]): profile
            for profile in self.source["general_B_failure_profiles"]
        }
        aggregate = Counter()
        for profile in self.actual["profiles"]:
            prime = int(profile["prime"])
            source_records = source_profiles[prime]["records"]
            occurrences = defaultdict(int)
            for source_record in source_records:
                for factor in source_record["K_factorization"]:
                    occurrences[int(factor["prime"])] += 1
            self.assertEqual(profile["complete_linear_R_count"], len(source_records))
            for record in profile["records"]:
                modulus = int(record["R"])
                factors = [
                    (int(factor["prime"]), int(factor["exponent"]))
                    for factor in record["K_factorization"]
                ]
                self.assertEqual(
                    int(record["K"]),
                    int(sympy.prod(q**exponent for q, exponent in factors)),
                )
                private = [factor for factor in factors if occurrences[factor[0]] == 1]
                shared = [factor for factor in factors if occurrences[factor[0]] > 1]
                self.assertEqual(
                    record["private_factorization"],
                    [{"prime": q, "exponent": exponent} for q, exponent in private],
                )
                self.assertEqual(
                    record["shared_factorization"],
                    [{"prime": q, "exponent": exponent} for q, exponent in shared],
                )
                private_spectrum = direct_centered_spectrum(private, modulus)
                shared_spectrum = direct_centered_spectrum(shared, modulus)
                target = modulus - 1
                self.assertEqual(
                    record["private_centered_spectrum_residue_count"],
                    len(private_spectrum),
                )
                self.assertEqual(
                    record["shared_centered_spectrum_residue_count"],
                    len(shared_spectrum),
                )
                self.assertEqual(
                    record["minus_one_in_private_centered_spectrum"],
                    target in private_spectrum,
                )
                self.assertEqual(
                    record["minus_one_in_shared_centered_spectrum"],
                    target in shared_spectrum,
                )
                classification = record["target_hit_private_shared_classification"]
                aggregate[classification] += 1
                if classification == "mixed_private_shared":
                    self.assertNotIn(target, private_spectrum)
                    self.assertNotIn(target, shared_spectrum)
                elif classification == "shared_block_hit":
                    self.assertNotIn(target, private_spectrum)
                    self.assertIn(target, shared_spectrum)
                else:
                    self.fail(f"unexpected frozen classification: {classification}")
        self.assertEqual(
            dict(sorted(aggregate.items())),
            {"mixed_private_shared": 8, "shared_block_hit": 4},
        )


if __name__ == "__main__":
    unittest.main()
