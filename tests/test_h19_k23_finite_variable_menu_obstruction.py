import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_finite_variable_menu_obstruction",
    ROOT / "reproductions" / "h19_k23_finite_variable_menu_obstruction.py",
)
assert SPEC and SPEC.loader
obstruction = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = obstruction
SPEC.loader.exec_module(obstruction)


class H19K23FiniteVariableMenuObstructionTests(unittest.TestCase):
    def test_m31_state_is_outside_the_full_fixed_base(self):
        state = obstruction.m31_uncovered_state()
        self.assertEqual(state["v_mod_29"], 0)
        self.assertEqual(state["target_parameter_residue"], 0)
        self.assertEqual(state["target_residue"], 11)
        self.assertEqual(state["uniform_u_factor"], 133)

    def test_crt_avoids_an_arbitrary_finite_usable_menu_on_a_primitive_prime_progression(self):
        primes = (37, 41, 43, 59)
        result = obstruction.run_audit(primes)
        state = result["state"]
        self.assertEqual(result["avoidance_parameter"] % 31, 0)
        self.assertEqual(
            (-state["q"] * result["u_at_avoidance_parameter"]) % 31,
            state["target_residue"],
        )
        self.assertTrue(all(result["u_at_avoidance_parameter"] % prime for prime in primes))
        self.assertEqual(result["prime_progression_gcd"], 1)

    def test_checked_artifact_matches_default_menu_audit(self):
        with (
            ROOT / "reproductions" / "h19-k23-finite-variable-menu-obstruction.json"
        ).open(encoding="utf-8") as handle:
            artifact = json.load(handle)
        self.assertEqual(artifact, obstruction.run_audit())


if __name__ == "__main__":
    unittest.main()
