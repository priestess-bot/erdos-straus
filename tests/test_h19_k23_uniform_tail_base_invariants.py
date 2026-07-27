import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_uniform_tail_base_invariants",
    ROOT / "reproductions" / "h19_k23_uniform_tail_base_invariants.py",
)
assert SPEC and SPEC.loader
invariants = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = invariants
SPEC.loader.exec_module(invariants)


class H19K23UniformTailBaseInvariantTests(unittest.TestCase):
    def test_affine_gcd_extracts_the_existing_stage_bases(self):
        result = invariants.run_audit()
        rows = {row["tail_gap"]: row for row in result["tail_invariants"]}
        expected = {
            31: (133, [2, 7, 19]),
            35: (13, [3, 13]),
            39: (1, [2, 5]),
            47: (1, [2, 3]),
            59: (7, [3, 5, 7]),
            71: (1, [2, 3]),
            79: (1, [2, 5]),
            91: (1, [23]),
            95: (1, [2, 3]),
        }
        self.assertFalse(rows[63]["globally_available"])
        for gap, (factor, primes) in expected.items():
            self.assertTrue(rows[gap]["globally_available"])
            self.assertEqual(rows[gap]["uniform_u_factor"], factor)
            self.assertEqual(rows[gap]["canonical_base_primes"], primes)
            self.assertTrue(
                all(intercept % factor == 0 for intercept in rows[gap]["u_intercepts"])
            )
            self.assertEqual(rows[gap]["u_slope"] % factor, 0)

    def test_checked_artifact_matches_symbolic_audit(self):
        with (
            ROOT / "reproductions" / "h19-k23-uniform-tail-base-invariants.json"
        ).open(encoding="utf-8") as handle:
            artifact = json.load(handle)
        self.assertEqual(artifact, invariants.run_audit())


if __name__ == "__main__":
    unittest.main()
