from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "f2_post_g_g_producer_pruning.py"
SPEC = importlib.util.spec_from_file_location("f2_g_pruning", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load G producer pruning verifier")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class F2PostGGProducerPruningTest(unittest.TestCase):
    def test_frozen_graph_premises(self) -> None:
        result = MODULE.verify()
        self.assertFalse(result["positive_q_G_seed"])
        self.assertEqual(result["initializer_nonterminal_G_q"], 1)
        self.assertEqual(
            result["requested_selected_G_exit"], "q_one_g_full_carrier_phase_root"
        )
        self.assertEqual(len(result["requested_nonrecursive_alternates"]), 2)


if __name__ == "__main__":
    unittest.main()
