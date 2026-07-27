import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_tail_reverse_even_source_divisor_audit",
    ROOT / "reproductions" / "type_i_tail_reverse_even_source_divisor_audit.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeITailReverseEvenSourceDivisorAuditTests(unittest.TestCase):
    def test_every_even_source_record_has_an_even_target_side_bridge_divisor(self):
        closure = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-even-source-closure-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-even-source-divisor-audit-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit(closure)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (actual["even_source_record_count"], actual["all_reconstructed_R_odd"], actual["all_reconstructed_E_even"]),
            (1_717, True, True),
        )


if __name__ == "__main__":
    unittest.main()
