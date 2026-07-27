import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_multisource_descent_state",
    ROOT / "reproductions" / "type_ii_multisource_descent_state.py",
)
assert SPEC and SPEC.loader
state = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = state
SPEC.loader.exec_module(state)


class TypeIIMultisourceDescentStateTests(unittest.TestCase):
    def test_p3361_has_a_failed_k1_state_then_a_k2_lift(self):
        spf = state.short_certificate.smallest_prime_factors(10_000)
        profile = state.profile_prime(3_361, spf)
        self.assertEqual(profile["first_success_k"], 2)
        self.assertEqual(profile["prior_failure_count"], 1)
        first, second = profile["states_through_first_success"]
        self.assertEqual(
            (first["k"], first["q"], first["target_in_divisor_residues"]),
            (1, 3, False),
        )
        self.assertEqual(
            (
                second["k"],
                second["source_denominator"],
                second["target_in_divisor_residues"],
                second["witness_factor"],
                second["certificate_gap"],
            ),
            (2, 2_941, True, 68, 39),
        )

    def test_checked_twenty_million_state_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-multisource-descent-state-h19-20m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["residual_count"], 65)
        self.assertEqual(
            result["first_success_k_histogram"],
            {"1": 25, "2": 25, "3": 4, "4": 2, "5": 3, "6": 4, "12": 2},
        )
        self.assertGreater(result["total_prior_failure_states"], 0)
        self.assertGreaterEqual(result["maximum_prior_failure_count"], 1)


if __name__ == "__main__":
    unittest.main()
