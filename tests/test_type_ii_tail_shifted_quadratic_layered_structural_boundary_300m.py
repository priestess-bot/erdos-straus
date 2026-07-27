import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "reproductions" / filename)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


square = load_module(
    "type_ii_tail_shifted_quadratic_square_necessity_300m",
    "type_ii_tail_shifted_quadratic_square_necessity.py",
)
opposite = load_module(
    "type_ii_tail_shifted_quadratic_opposite_pair_profile_300m",
    "type_ii_tail_shifted_quadratic_opposite_pair_profile.py",
)
outer = load_module(
    "type_ii_tail_shifted_quadratic_outer_structural_profile_300m",
    "type_ii_tail_shifted_quadratic_outer_structural_profile.py",
)
completion = load_module(
    "type_ii_tail_shifted_quadratic_source_factor_completion_300m",
    "type_ii_tail_shifted_quadratic_source_factor_completion.py",
)


class TypeIITailShiftedQuadraticLayeredStructuralBoundary300MTests(unittest.TestCase):
    @staticmethod
    def offset_payload():
        path = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-offset-profile-300m-results.json"
        return json.loads(path.read_text(encoding="utf-8"))

    def test_artifacts_rebuild(self):
        square_result = square.run_audit(self.offset_payload())
        expected_square = json.loads(
            (ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-square-necessity-300m-results.json").read_text(encoding="utf-8")
        )
        self.assertEqual(square_result, expected_square)
        opposite_result = opposite.run_audit(square_result)
        expected_opposite = json.loads(
            (ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-opposite-pair-profile-300m-results.json").read_text(encoding="utf-8")
        )
        self.assertEqual(opposite_result, expected_opposite)
        expected_outer = json.loads(
            (ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-outer-structural-profile-300m-results.json").read_text(encoding="utf-8")
        )
        self.assertEqual(outer.run_audit(opposite_result, 202_521), expected_outer)
        expected_completion = json.loads(
            (ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-source-factor-completion-300m-results.json").read_text(encoding="utf-8")
        )
        self.assertEqual(completion.run_audit(opposite_result), expected_completion)

    def test_one_mixed_factor_pressure_point_remains_after_three_layers(self):
        opposite_payload = json.loads(
            (ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-opposite-pair-profile-300m-results.json").read_text(encoding="utf-8")
        )
        minimal = [
            record
            for record in opposite_payload["records"]
            if record["symmetric_box_subgroup_saturation_witness_count"]
            or record["inverse_pairing_parity_witness_count"]
        ]
        outer_result = outer.run_audit(opposite_payload, 202_521)
        completion_result = completion.run_audit(opposite_payload)
        self.assertEqual(len(opposite_payload["records"]), 89)
        self.assertEqual(len(minimal), 79)
        self.assertEqual(outer_result["later_structural_certificate_count"], 8)
        self.assertEqual(outer_result["later_structural_miss_primes"], [26_034_649, 212_973_049])
        completion_records = {
            record["prime"]: record["source_factor_completion"]
            for record in completion_result["records"]
        }
        self.assertIsNotNone(completion_records[26_034_649])
        self.assertIsNone(completion_records[212_973_049])
        covered = {record["prime"] for record in minimal}
        covered.update(
            record["prime"]
            for record in outer_result["records"]
            if record["later_structural_certificate"] is not None
        )
        covered.update(prime for prime, witness in completion_records.items() if witness is not None)
        self.assertEqual(len(covered), 88)
        self.assertNotIn(212_973_049, covered)
        residual = next(record for record in opposite_payload["records"] if record["prime"] == 212_973_049)
        self.assertEqual(residual["minimum_signed_prime_support_count"], 5)
        self.assertEqual(residual["minimum_signed_l1_displacement"], 6)


if __name__ == "__main__":
    unittest.main()
