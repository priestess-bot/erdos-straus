import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_mersenne_bridge_selector",
    ROOT / "reproductions" / "type_i_mersenne_bridge_selector.py",
)
assert SPEC and SPEC.loader
selector = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = selector
SPEC.loader.exec_module(selector)


class TypeIMersenneBridgeSelectorTests(unittest.TestCase):
    def test_dyadic_witness_rebuilds(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-mersenne-bridge-selector-21169-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = selector.run_audit()
        self.assertEqual(actual, expected)
        witness = actual["witness"]
        self.assertEqual(
            (witness["E"], witness["R"], witness["K"], witness["normal_form"], witness["gap"]),
            (32, 31, 164060, [1, 5, 1262], 4071),
        )
        self.assertEqual((witness["source_denominator"], witness["bridge_factor"]), (21168, 32))

    def test_invalid_dyadic_factor_pair_is_rejected(self):
        self.assertIsNone(selector.dyadic_p_minus_one_witness(21_169, 5, 1, 1))


if __name__ == "__main__":
    unittest.main()
