import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_h19_p25_external_b1_complement",
    ROOT / "reproductions" / "type_i_h19_p25_external_b1_complement.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIH19P25ExternalB1ComplementTests(unittest.TestCase):
    def test_external_methods_cover_every_p25_b1_boundary_point(self):
        paths = {
            "b1": "type-i-h19-b1-source-state-boundary-1b-results.json",
            "k2": "type-i-k2-mod7-even-source-audit-1b-results.json",
            "k6": "type-i-h19-k6-after-k2-boundary-1b-results.json",
            "variable": "type-i-h19-variable-even-scale-after-k6-1b-results.json",
        }
        inputs = {
            key: json.loads((ROOT / "reproductions" / value).read_text(encoding="utf-8"))
            for key, value in paths.items()
        }
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-h19-p25-external-b1-complement-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit(**inputs)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["p_eq_25_mod_48_count"],
                actual["B_eq_1_realization_count"],
                actual["B_eq_1_miss_count"],
                actual["external_or_B_eq_1_covered_count"],
            ),
            (243, 237, 6, 243),
        )
        self.assertEqual(
            (
                actual["B_eq_1_miss_fixed_k2_count"],
                actual["B_eq_1_miss_fixed_k6_count"],
                actual["B_eq_1_miss_variable_scale_count"],
            ),
            (1, 1, 4),
        )


if __name__ == "__main__":
    unittest.main()
