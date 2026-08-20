from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "verification"
sys.path.insert(0, str(VER))

import verify_controls
import verify_counterexamples
import verify_downstream_formulas
import verify_state_contract
import verify_symbolic


class ProofPackageTests(unittest.TestCase):
    def test_symbolic(self):
        self.assertEqual(verify_symbolic.verify()["status"], "verified")

    def test_controls(self):
        self.assertEqual(verify_controls.verify()["status"], "verified")

    def test_counterexamples(self):
        self.assertEqual(verify_counterexamples.verify()["status"], "verified")

    def test_state_contract(self):
        self.assertEqual(verify_state_contract.verify()["status"], "verified")

    def test_downstream(self):
        self.assertEqual(verify_downstream_formulas.verify()["status"], "verified")


if __name__ == "__main__":
    unittest.main()
