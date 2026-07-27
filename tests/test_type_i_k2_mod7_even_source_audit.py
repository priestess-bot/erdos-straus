import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_k2_mod7_even_source_audit",
    ROOT / "reproductions" / "type_i_k2_mod7_even_source_audit.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIK2Mod7EvenSourceAuditTests(unittest.TestCase):
    def test_boundary_factor_rebuilds_to_terminal_even_source(self):
        witness = audit.terminal_factor_certificate(48_605_881, 353)
        self.assertEqual(
            (witness["source_denominator"], witness["mixed_divisor"], witness["gap"]),
            (42_530_146, 706, 807),
        )

    def test_h19_profile_rebuilds(self):
        h19 = json.loads(
            (ROOT / "reproductions" / "type-ii-source-free-transition-h19-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-k2-mod7-even-source-audit-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit(h19)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["p_eq_25_mod_48_count"],
                actual["proper_divisor_terminal_count"],
                actual["single_prime_terminal_count"],
            ),
            (243, 124, 72),
        )


if __name__ == "__main__":
    unittest.main()
