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


outer = load_module(
    "type_ii_tail_shifted_quadratic_outer_structural_profile_200m",
    "type_ii_tail_shifted_quadratic_outer_structural_profile.py",
)
completion = load_module(
    "type_ii_tail_shifted_quadratic_source_factor_completion_200m",
    "type_ii_tail_shifted_quadratic_source_factor_completion.py",
)


class TypeIITailShiftedQuadraticLayeredStructuralClosure200MTests(unittest.TestCase):
    @staticmethod
    def input_payload():
        path = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-opposite-pair-profile-200m-results.json"
        return json.loads(path.read_text(encoding="utf-8"))

    def test_layer_artifacts_rebuild(self):
        payload = self.input_payload()
        expected_outer = json.loads(
            (ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-outer-structural-profile-200m-results.json").read_text(encoding="utf-8")
        )
        expected_completion = json.loads(
            (ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-source-factor-completion-200m-results.json").read_text(encoding="utf-8")
        )
        self.assertEqual(outer.run_audit(payload, 202_521), expected_outer)
        self.assertEqual(completion.run_audit(payload), expected_completion)

    def test_three_layers_close_all_sixty_five_pressure_rays(self):
        payload = self.input_payload()
        records = payload["records"]
        minimal_hits = [
            record
            for record in records
            if record["symmetric_box_subgroup_saturation_witness_count"]
            or record["inverse_pairing_parity_witness_count"]
        ]
        outer_result = outer.run_audit(payload, 202_521)
        completion_result = completion.run_audit(payload)
        self.assertEqual(len(records), 65)
        self.assertEqual(len(minimal_hits), 57)
        self.assertEqual(outer_result["later_structural_certificate_count"], 7)
        self.assertEqual(outer_result["later_structural_miss_primes"], [26_034_649])
        self.assertEqual(completion_result["source_factor_completion_hit_count"], 2)
        completion_records = {
            record["prime"]: record["source_factor_completion"]
            for record in completion_result["records"]
        }
        witness = completion_records[26_034_649]
        self.assertEqual((witness["u"], witness["v"], witness["w"]), (7, 19, 21_737))
        self.assertEqual(witness["u_squared_v_plus_four_over_t"], 5)
        self.assertEqual((witness["a"], witness["b"]), (2_947, 21_737))
        closed = {record["prime"] for record in minimal_hits}
        closed.update(
            record["prime"]
            for record in outer_result["records"]
            if record["later_structural_certificate"] is not None
        )
        closed.update(
            prime for prime, witness in completion_records.items() if witness is not None
        )
        self.assertEqual(len(closed), 65)


if __name__ == "__main__":
    unittest.main()
