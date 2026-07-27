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


offset = load_module(
    "type_ii_tail_shifted_quadratic_offset_profile_500m",
    "type_ii_tail_shifted_quadratic_offset_profile.py",
)
single = load_module(
    "type_ii_tail_shifted_quadratic_single_offset_search_477015289",
    "type_ii_tail_shifted_quadratic_single_offset_search.py",
)
short_certificate = load_module("gap_27_external_progression_short_certificate", "short_certificate.py")


class TypeIITailShiftedQuadraticOffsetBoundary500MTests(unittest.TestCase):
    @staticmethod
    def external_payload():
        path = ROOT / "reproductions" / "type-ii-tail-deflation-external-boundary-500m-results.json"
        return json.loads(path.read_text(encoding="utf-8"))

    def test_fixed_offset_artifact_rebuilds_and_has_one_miss(self):
        checked = json.loads(
            (ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-offset-profile-500m-results.json").read_text(encoding="utf-8")
        )
        result = offset.run_audit(self.external_payload(), 202_521)
        self.assertEqual(result, checked)
        self.assertEqual(result["zero_offset_quadratic_miss_count"], 124)
        self.assertEqual(result["offset_descent_count"], 123)
        self.assertEqual(result["offset_missing_primes"], [477_015_289])

    def test_the_single_new_pressure_point_misses_the_five_million_offset_box(self):
        checked = json.loads(
            (ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-single-offset-search-477015289-5m-results.json").read_text(encoding="utf-8")
        )
        result = single.run_search(477_015_289, 5_000_001)
        self.assertEqual(result, checked)
        self.assertIsNone(result["offset_descent"])
        self.assertEqual(result["candidate_pairs_examined"], 50)

    def test_the_boundary_point_has_the_gap_twenty_seven_progression_certificate(self):
        prime = 477_015_289
        self.assertEqual(prime % 6_264, 5_425)
        A = (prime + 27) // 116
        B = (prime + 29) // 27
        certificate = short_certificate.external_source_type_i_certificate(prime, 29, 27)
        self.assertIsNotNone(certificate)
        self.assertEqual((A, B), (4_112_201, 17_667_234))
        self.assertEqual((certificate.x, certificate.divisor), (29 * A, 29 * 29 * A))
        self.assertTrue(short_certificate.verify_certificate(certificate))


if __name__ == "__main__":
    unittest.main()
