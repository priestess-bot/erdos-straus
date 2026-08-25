from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "f2_post_g_h4_target_owner.py"
SPEC = importlib.util.spec_from_file_location("f2_h4_owner", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load H4 target owner verifier")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class F2PostGH4TargetOwnerTest(unittest.TestCase):
    def test_focused_owner_shapes(self) -> None:
        result = MODULE.verify()
        self.assertEqual(
            result["status"], "FOCUSED_H4_HIGH_SUPPORT_OWNER_SHAPES_REPLAYED"
        )
        self.assertTrue(all(row["support_gt_Bp"] for row in result["controls"]))
        self.assertTrue(all(row["R_gt_p"] for row in result["controls"]))
        self.assertTrue(all(not row["recursive_edge_eligible"] for row in result["controls"]))


if __name__ == "__main__":
    unittest.main()
