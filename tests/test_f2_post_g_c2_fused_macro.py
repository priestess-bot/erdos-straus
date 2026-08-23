from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "f2_post_g_c2_fused_macro.py"
SPEC = importlib.util.spec_from_file_location("f2_c2_fused", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load C2 fused-macro verifier")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class F2PostGC2FusedMacroTest(unittest.TestCase):
    def test_focused_phase_and_checkpoints(self) -> None:
        result = MODULE.verify()
        self.assertEqual(result["status"], "FOCUSED_C2_19_PHASE_CHECKPOINTS_REPLAYED")
        self.assertEqual(result["even_c2"]["q_star"], 19)
        self.assertFalse(result["checkpoints"]["queued"])
        self.assertEqual(result["final_E3"], "not replayed; common serializer required")


if __name__ == "__main__":
    unittest.main()
