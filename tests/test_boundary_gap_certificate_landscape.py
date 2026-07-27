import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "boundary_gap_certificate_landscape",
    ROOT / "reproductions" / "boundary_gap_certificate_landscape.py",
)
assert SPEC and SPEC.loader
landscape = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = landscape
SPEC.loader.exec_module(landscape)


class BoundaryGapCertificateLandscapeTests(unittest.TestCase):
    def test_boundary_short_gap_landscape_rebuilds_exactly(self):
        artifact = ROOT / "reproductions" / "type-i-boundary-gap-27-landscape-477015289-results.json"
        expected = json.loads(artifact.read_text(encoding="utf-8"))
        actual = landscape.run_scan()
        self.assertEqual(actual, expected)
        self.assertEqual(actual["first_certificate_gap"], 27)

        gaps = {entry["gap"]: entry for entry in actual["gaps"]}
        for gap in (3, 7, 11, 15, 19, 23):
            self.assertEqual(gaps[gap]["type_i"], [])
            self.assertEqual(gaps[gap]["type_ii_divisors"], [])

        gap_27 = gaps[27]
        self.assertEqual(gap_27["factorization"], {"29": 1, "433": 1, "9497": 1})
        self.assertEqual(gap_27["type_ii_divisors"], [])
        self.assertEqual(
            [(entry["divisor"], entry["normal_form"]) for entry in gap_27["type_i"]],
            [
                (7_986_977, [29, 433, 9_497]),
                (3_458_361_041, [29, 1, 4_112_201]),
                (1_497_470_330_753, [12_557, 1, 9_497]),
            ],
        )
        self.assertTrue(
            all(entry["normal_tail_deflation"] is None for entry in gap_27["type_i"])
        )

    def test_complete_hundred_thousand_short_gap_box_has_no_normal_tail_deflation(self):
        artifact = ROOT / "reproductions" / "type-i-boundary-short-gap-tail-100k-477015289-results.json"
        expected = json.loads(artifact.read_text(encoding="utf-8"))
        actual = landscape.run_scan(477_015_289, 100_003)
        self.assertEqual(actual, expected)
        type_i = [entry for gap in actual["gaps"] for entry in gap["type_i"]]
        type_ii_count = sum(len(gap["type_ii_divisors"]) for gap in actual["gaps"])
        self.assertEqual(len(type_i), 125)
        self.assertEqual(type_ii_count, 86)
        self.assertTrue(all(entry["normal_tail_deflation"] is None for entry in type_i))


if __name__ == "__main__":
    unittest.main()
