import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "reverse_lift_shortest_certificate_audit",
    ROOT / "reproductions" / "reverse_lift_shortest_certificate_audit.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class ReverseLiftShortestCertificateAuditTests(unittest.TestCase):
    def test_small_audit_is_exact(self):
        result = audit.run_audit(1_000)
        self.assertEqual(result["core_prime_count"], 14)
        self.assertEqual(result["targets_with_reverse_two_tail_lift"], 1)
        self.assertEqual(result["total_reverse_two_tail_lifts"], 1)
        self.assertEqual(result["records"][0]["prime"], 193)
        self.assertEqual(
            result["records"][0]["reverse_two_tail_lifts"],
            [
                {
                    "replaced_target_position": 2,
                    "replaced_target_term": 1_331_700,
                    "source_denominator": 192,
                    "source_term": 9_200,
                }
            ],
        )

    def test_checked_artifact_summary(self):
        with (
            ROOT / "reproductions" / "reverse-lift-shortest-certificate-10k-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 10_000)
        self.assertEqual(result["core_prime_count"], 143)
        self.assertEqual(result["targets_with_reverse_two_tail_lift"], 2)
        self.assertEqual(result["total_reverse_two_tail_lifts"], 3)
        self.assertEqual([record["prime"] for record in result["records"]], [193, 1201])


if __name__ == "__main__":
    unittest.main()
