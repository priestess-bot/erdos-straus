import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_source_state_b1_product_boundary",
    ROOT / "reproductions" / "type_i_source_state_b1_product_boundary.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeISourceStateB1ProductBoundaryTests(unittest.TestCase):
    def test_all_b1_misses_are_finite_product_not_subgroup_obstructions(self):
        h19 = json.loads(
            (ROOT / "reproductions" / "type-i-h19-even-source-support-min-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        tail = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-even-source-support-min-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-source-state-b1-product-boundary-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit(h19, tail)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["total_B_eq_1_miss_count"],
                actual["total_subgroup_obstruction_count"],
                actual["total_finite_product_obstruction_count"],
            ),
            (89, 0, 89),
        )
        self.assertEqual(
            [(profile["B_eq_1_miss_count"], profile["finite_product_obstruction_count"])
             for profile in actual["profiles"]],
            [(17, 17), (72, 72)],
        )


if __name__ == "__main__":
    unittest.main()
