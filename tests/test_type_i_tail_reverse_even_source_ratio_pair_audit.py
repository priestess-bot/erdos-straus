import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_tail_reverse_even_source_ratio_pair_audit",
    ROOT / "reproductions" / "type_i_tail_reverse_even_source_ratio_pair_audit.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeITailReverseEvenSourceRatioPairAuditTests(unittest.TestCase):
    def test_every_stored_even_bridge_reduces_to_a_ratio_two_divisor_pair(self):
        source = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-even-source-divisor-audit-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-even-source-ratio-pair-audit-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit(source)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (actual["record_count"], actual["all_pairs_coprime"], actual["all_pairs_hit_ratio_two_mod_R"]),
            (1_717, True, True),
        )


if __name__ == "__main__":
    unittest.main()
