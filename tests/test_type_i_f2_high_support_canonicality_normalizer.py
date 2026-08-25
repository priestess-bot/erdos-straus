from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_i_f2_high_support_canonicality_normalizer.py"
SPEC = importlib.util.spec_from_file_location("f2_high_support_canonicality", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class HighSupportCanonicalityTests(unittest.TestCase):
    def test_noncanonical_projection_is_strict_but_not_source_evidence(self) -> None:
        record = MODULE.canonicality(MODULE.chart(73, 1369, 74))
        self.assertEqual((record["c"], record["t"], record["R_canonical"]), (1, 1, 75))
        synthetic = MODULE.synthetic_determinant(record)
        self.assertEqual(73 * synthetic["n"], 4 * synthetic["M"] * synthetic["d"] + 1)

    def test_canonical_control_has_zero_excess(self) -> None:
        record = MODULE.canonicality(MODULE.chart(73, 1518, 45))
        self.assertEqual(record["t"], 0)

    def test_focused_controls_replay(self) -> None:
        MODULE.verify()


if __name__ == "__main__":
    unittest.main()
