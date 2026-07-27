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
    "type_ii_tail_shifted_quadratic_square_necessity_400m",
    "type_ii_tail_shifted_quadratic_square_necessity.py",
)
opposite = load_module(
    "type_ii_tail_shifted_quadratic_opposite_pair_profile_400m",
    "type_ii_tail_shifted_quadratic_opposite_pair_profile.py",
)
outer = load_module(
    "type_ii_tail_shifted_quadratic_outer_structural_profile_400m",
    "type_ii_tail_shifted_quadratic_outer_structural_profile.py",
)
two_sided = load_module(
    "type_ii_tail_shifted_quadratic_two_sided_completion_400m",
    "type_ii_tail_shifted_quadratic_two_sided_completion.py",
)


class TypeIITailShiftedQuadraticFourLayerStructuralClosure400MTests(unittest.TestCase):
    @staticmethod
    def offset_payload():
        path = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-offset-profile-400m-results.json"
        return json.loads(path.read_text(encoding="utf-8"))

    def test_structural_artifacts_rebuild(self):
        square_result = square.run_audit(self.offset_payload())
        expected_square = json.loads(
            (ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-square-necessity-400m-results.json").read_text(encoding="utf-8")
        )
        self.assertEqual(square_result, expected_square)
        opposite_result = opposite.run_audit(square_result)
        expected_opposite = json.loads(
            (ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-opposite-pair-profile-400m-results.json").read_text(encoding="utf-8")
        )
        self.assertEqual(opposite_result, expected_opposite)
        expected_outer = json.loads(
            (ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-outer-structural-profile-400m-results.json").read_text(encoding="utf-8")
        )
        self.assertEqual(outer.run_audit(opposite_result, 202_521), expected_outer)
        expected_two_sided = json.loads(
            (ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-two-sided-completion-400m-results.json").read_text(encoding="utf-8")
        )
        self.assertEqual(two_sided.run_audit(opposite_result), expected_two_sided)

    def test_four_layers_close_all_one_hundred_eight_pressure_rays(self):
        opposite_payload = json.loads(
            (ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-opposite-pair-profile-400m-results.json").read_text(encoding="utf-8")
        )
        minimal = [
            record
            for record in opposite_payload["records"]
            if record["symmetric_box_subgroup_saturation_witness_count"]
            or record["inverse_pairing_parity_witness_count"]
        ]
        outer_result = outer.run_audit(opposite_payload, 202_521)
        two_sided_result = two_sided.run_audit(opposite_payload)
        self.assertEqual(len(opposite_payload["records"]), 108)
        self.assertEqual(len(minimal), 95)
        self.assertEqual(outer_result["later_structural_certificate_count"], 11)
        self.assertEqual(outer_result["later_structural_miss_primes"], [26_034_649, 212_973_049])
        two_sided_records = {
            record["prime"]: record["two_sided_completion"]
            for record in two_sided_result["records"]
        }
        self.assertIsNotNone(two_sided_records[26_034_649])
        self.assertIsNotNone(two_sided_records[212_973_049])
        closed = {record["prime"] for record in minimal}
        closed.update(
            record["prime"]
            for record in outer_result["records"]
            if record["later_structural_certificate"] is not None
        )
        closed.update(prime for prime, witness in two_sided_records.items() if witness is not None)
        self.assertEqual(len(closed), 108)


if __name__ == "__main__":
    unittest.main()
