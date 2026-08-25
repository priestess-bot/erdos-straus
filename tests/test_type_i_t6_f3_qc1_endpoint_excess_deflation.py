from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_i_t6_f3_qc1_endpoint_excess_deflation.py"
SPEC = importlib.util.spec_from_file_location("qc1_endpoint_excess_deflation", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class QC1EndpointExcessDeflationTests(unittest.TestCase):
    def test_capacity_boundary_cases(self) -> None:
        self.assertEqual(MODULE.deflation_control(337, 421, 7, 49 * 619)["mu"], 2)
        self.assertEqual(MODULE.deflation_control(3529, 4411, 7, 343 * 96281)["mu"], 3)

    def test_controls(self) -> None:
        MODULE.verify()


if __name__ == "__main__":
    unittest.main()
