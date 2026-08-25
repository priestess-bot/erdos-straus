from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "f2_post_g_low_chart_exit.py"
SPEC = importlib.util.spec_from_file_location("f2_low_chart_exit", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load low-chart exit verifier")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class F2PostGLowChartExitTest(unittest.TestCase):
    def test_focused_post_g_roots_exit(self) -> None:
        result = MODULE.verify()
        self.assertEqual(result["status"], "FOCUSED_LOW_CHART_EXITS_REPLAYED")
        self.assertEqual([row["p"] for row in result["controls"]], [73, 241, 2521])
        self.assertTrue(all(row["step_count"] >= 1 for row in result["controls"]))
        self.assertTrue(all(row["status"] in {"terminal", "overflow"} for row in result["controls"]))


if __name__ == "__main__":
    unittest.main()
