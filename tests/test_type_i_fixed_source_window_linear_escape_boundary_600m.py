import importlib.util
import json
import math
from pathlib import Path
import sys
import unittest

import sympy


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT / "reproductions" / "type_i_fixed_source_window_linear_escape_boundary_600m.py"
)
RESULT = (
    ROOT
    / "reproductions"
    / "type-i-fixed-source-window-linear-escape-boundary-600m-results.json"
)

spec = importlib.util.spec_from_file_location("fixed_window_linear_escape", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def independent_linear_states(prime):
    bound = (math.isqrt(1 + 3 * prime) - 1) // 3
    while 3 * (bound + 1) ** 2 + 2 * (bound + 1) <= prime:
        bound += 1
    states = set()
    for u in range(1, bound + 1):
        for source_factor in sympy.divisors(prime - u):
            source_factor = int(source_factor)
            if (source_factor - 1) % u:
                continue
            modulus = (source_factor - 1) // u
            if modulus < 3 or modulus % 4 != 3:
                continue
            other = (prime - u) // source_factor
            if other < u:
                continue
            if other % 2:
                states.add((u, other, modulus))
            if u % 2 and u != other:
                states.add((other, u, modulus))
    return bound, states


def independent_beta(prime, source, bridge_factor):
    distance = prime - source
    lambda_value = 4 if distance % 4 == 1 else 2
    u, D = source // lambda_value, bridge_factor // lambda_value
    common = math.gcd(u, D)
    beta = D // common
    gamma = common // beta
    alpha = u // common
    if u != alpha * beta * gamma or D != beta * beta * gamma:
        raise AssertionError("independent source normalization failed")
    return beta


class FixedSourceWindowLinearEscapeBoundary600MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = module.run_audit()
        cls.checked = json.loads(RESULT.read_text(encoding="utf-8"))

    def test_checked_artifact_matches_complete_run(self):
        self.assertEqual(self.checked, self.actual)

    def test_window_candidates_have_no_beta_one_but_full_linear_spectra_do(self):
        expected = {
            512_335_849: {
                "window_betas": [9142, 37630, 420637],
                "state_count": 87,
                "hit_R": [39, 231],
                "hit_state_count": 4,
                "least": (2073, 6337, 39, 5216, 535),
            },
            531_010_489: {
                "window_betas": [5],
                "state_count": 99,
                "hit_R": [7, 11, 31, 75],
                "hit_state_count": 18,
                "least": (1, 66376311, 7, 467, 267),
            },
        }
        for profile in self.actual["profiles"]:
            prime = int(profile["prime"])
            with self.subTest(prime=prime):
                window_betas = [
                    independent_beta(
                        prime,
                        int(candidate["source_denominator"]),
                        int(candidate["E"]),
                    )
                    for candidate in profile["window"]["B_one_candidates"]
                ]
                self.assertEqual(window_betas, expected[prime]["window_betas"])
                self.assertNotIn(1, window_betas)

                bound, states = independent_linear_states(prime)
                self.assertEqual(bound, profile["full_linear_u_bound"])
                self.assertEqual(len(states), expected[prime]["state_count"])
                target_hits = {}
                for _, _, modulus in states:
                    if modulus in target_hits:
                        continue
                    K = (prime * modulus + 1) // 4
                    target_hits[modulus] = min(
                        (
                            int(C)
                            for C in sympy.divisors(K)
                            if (4 * int(C) + 1) % modulus == 0
                        ),
                        default=None,
                    )
                hit_R = sorted(R for R, C in target_hits.items() if C is not None)
                self.assertEqual(hit_R, expected[prime]["hit_R"])
                hit_states = [
                    (a, s, R, target_hits[R])
                    for a, s, R in states
                    if target_hits[R] is not None
                ]
                self.assertEqual(len(hit_states), expected[prime]["hit_state_count"])

                witness = profile["least_gap_full_linear_B_one_witness"]
                compact = tuple(int(witness[key]) for key in ("a", "s", "R", "C", "m"))
                self.assertEqual(compact, expected[prime]["least"])
                self.assertEqual(witness["source_normalization"]["beta"], 1)
                self.assertIn(
                    (int(witness["a"]), int(witness["s"]), int(witness["R"])),
                    states,
                )
                self.assertEqual(
                    (4 * int(witness["C"]) + 1) // int(witness["R"]),
                    int(witness["m"]),
                )


if __name__ == "__main__":
    unittest.main()
