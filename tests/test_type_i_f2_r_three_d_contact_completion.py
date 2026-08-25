from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_i_f2_r_three_d_contact_completion.py"
SPEC = importlib.util.spec_from_file_location("f2_r_three_d_completion", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class RThreeDContactCompletionTests(unittest.TestCase):
    def test_composite_controls_reconstruct_certificates(self) -> None:
        for row in (
            (769, 1, 14, 14, 1, 15),
            (21_937, 1, 2_771, 2, 12, 231),
            (20_809, 1, 1_308, 4, 11, 119),
        ):
            self.assertGreater(MODULE.factor_certificate(*row)["g"], 1)

    def test_prime_d_control(self) -> None:
        MODULE.verify_prime_d_empty()

    def test_focused_controls_replay(self) -> None:
        MODULE.verify()


if __name__ == "__main__":
    unittest.main()
