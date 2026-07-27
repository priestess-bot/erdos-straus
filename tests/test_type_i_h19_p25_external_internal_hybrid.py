import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_h19_p25_external_internal_hybrid",
    ROOT / "reproductions" / "type_i_h19_p25_external_internal_hybrid.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIH19P25ExternalInternalHybridTests(unittest.TestCase):
    def test_external_partition_and_low_support_internal_fallback_rebuild(self):
        paths = {
            "k2": "type-i-k2-mod7-even-source-audit-1b-results.json",
            "k6": "type-i-h19-k6-after-k2-boundary-1b-results.json",
            "variable": "type-i-h19-variable-even-scale-after-k6-1b-results.json",
            "support": "type-i-h19-even-source-support-min-1b-results.json",
        }
        inputs = {
            key: json.loads((ROOT / "reproductions" / value).read_text(encoding="utf-8"))
            for key, value in paths.items()
        }
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-h19-p25-external-internal-hybrid-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit(**inputs)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["p_eq_25_mod_48_count"],
                actual["fixed_k2_terminal_count"],
                actual["fixed_k6_terminal_count"],
                actual["variable_even_scale_terminal_count"],
                actual["external_residue_boundary_count"],
                actual["uncovered_count"],
            ),
            (243, 124, 48, 43, 28, 0),
        )
        self.assertEqual(actual["internal_bridge_support_histogram"], {"1": 11, "2": 17})


if __name__ == "__main__":
    unittest.main()
