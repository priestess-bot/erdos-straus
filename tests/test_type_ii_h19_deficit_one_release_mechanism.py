import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_deficit_one_release_mechanism",
    ROOT / "reproductions" / "type_ii_h19_deficit_one_release_mechanism.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class H19DeficitOneReleaseMechanismTests(unittest.TestCase):
    def test_fixed_prime_lift_congruence_has_exact_persistence_and_gain_classes(self):
        # M(7)=23 for p=13.  The q=23 exponent persists iff j is a multiple of 23.
        self.assertEqual(
            audit.fixed_prime_lift_predictions(13, 7, 15, 23, 23, 1),
            (False, False),
        )
        self.assertEqual(
            audit.fixed_prime_lift_predictions(13, 7, 191, 23, 23, 1),
            (True, False),
        )
        # With j=23*15, M(7+8j)=23*(1+2*13*15) gains a second 23.
        self.assertEqual(
            audit.fixed_prime_lift_predictions(13, 7, 2767, 23, 23, 1),
            (True, True),
        )

    def test_artifact_rebuilds_exactly(self):
        with (ROOT / "reproductions" / "type-ii-h19-deficit-one-saturated-prime-profile-1b-results.json").open(encoding="utf-8") as handle:
            profile = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-deficit-one-release-mechanism-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(audit.run_audit(profile), checked)

    def test_most_releases_do_not_restore_any_initial_saturated_prime(self):
        with (ROOT / "reproductions" / "type-ii-h19-deficit-one-release-mechanism-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["delta_one_later_release_count"], 38)
        self.assertTrue(result["all_fixed_prime_lift_congruences_verified"])
        self.assertEqual(
            result["release_mechanism_histogram"],
            {
                "all_saturated_primes_absent": 28,
                "same_prime_exponent_gain": 5,
                "same_prime_persists_without_gain": 5,
            },
        )
        for record in result["records"]:
            if record["mechanism_kind"] == "all_saturated_primes_absent":
                self.assertTrue(all(item["later_exponent"] == 0 for item in record["initial_saturated_primes"]))


if __name__ == "__main__":
    unittest.main()
