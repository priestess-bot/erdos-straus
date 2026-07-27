import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_fourth_even_source_small_r_boundary",
    ROOT / "reproductions" / "type_ii_h19_fourth_even_source_small_r_boundary.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19FourthEvenSourceSmallRBoundaryTests(unittest.TestCase):
    def test_checked_artifact_finds_the_first_small_tail_modulus(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-fourth-even-source-small-r-boundary-640775689-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime"], 640_775_689)
        self.assertEqual(result["r_cap"], 15)
        self.assertEqual(result["first_compatible_tail_hit_r"], 15)
        self.assertEqual(
            result["records"],
            [
                {
                    "r": 3,
                    "m1": 480_581_767,
                    "compatible_rays": [],
                    "tail_residue_factor_count": 0,
                },
                {
                    "r": 7,
                    "m1": 1_121_357_456,
                    "compatible_rays": [
                        {"distance": 1, "d": 80_096_961},
                        {"distance": 13, "d": 6_964_953},
                        {"distance": 870_619, "d": 105},
                        {"distance": 6_964_953, "d": 13},
                        {"distance": 80_096_961, "d": 1},
                    ],
                    "tail_residue_factor_count": 0,
                },
                {
                    "r": 11,
                    "m1": 1_762_133_145,
                    "compatible_rays": [],
                    "tail_residue_factor_count": 0,
                },
                {
                    "r": 15,
                    "m1": 2_402_908_834,
                    "compatible_rays": [
                        {"distance": 34_091, "d": 1253},
                        {"distance": 8_431_259, "d": 5},
                    ],
                    "tail_residue_factor_count": 12,
                },
            ],
        )

    def test_invalid_r_caps_are_rejected(self):
        with self.assertRaises(ValueError):
            audit.run_audit(14)


if __name__ == "__main__":
    unittest.main()
