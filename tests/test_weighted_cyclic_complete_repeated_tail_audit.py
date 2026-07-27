import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "weighted_cyclic_complete_repeated_tail_audit",
    ROOT / "reproductions" / "weighted_cyclic_complete_repeated_tail_audit.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class WeightedCyclicCompleteRepeatedTailAuditTests(unittest.TestCase):
    def test_even_k_uses_smaller_minimal_source(self):
        source_denominator, source = audit.minimal_source(552)
        self.assertEqual(source_denominator, 1_103)
        self.assertEqual(source, (276, 608_856, 608_856))

    def test_first_core_witness_reconstructs_and_tracks_p_tails(self):
        witness = audit.witness_at(2_161, 1, 49, 552)
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(witness["target_solution"], [25_932, 1_192_872, 552])
        self.assertEqual(witness["p_divisible_count"], 2)

    def test_small_core_box_has_no_witness(self):
        result = audit.run_audit(200, 12)
        self.assertEqual(result["core_primes"], 3)
        self.assertEqual(result["witnesses"], 0)
        self.assertGreater(result["candidates_checked"], 5_000)


if __name__ == "__main__":
    unittest.main()
