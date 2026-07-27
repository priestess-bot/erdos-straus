import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "weighted_cyclic_repeated_tail_audit",
    ROOT / "reproductions" / "weighted_cyclic_repeated_tail_audit.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class WeightedCyclicRepeatedTailAuditTests(unittest.TestCase):
    def test_known_noncore_witness_reconstructs(self):
        witness = audit.witness_at(31, 1, 2, 8)
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(witness["source_denominator"], 30)
        self.assertEqual(witness["target_solution"], [16, 248, 16])

    def test_small_core_box_has_no_witness(self):
        result = audit.run_audit(200, 12)
        self.assertEqual(result["core_primes"], 3)
        self.assertEqual(result["witnesses"], 0)
        self.assertGreater(result["candidates_checked"], 1_000)


if __name__ == "__main__":
    unittest.main()
