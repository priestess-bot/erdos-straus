import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "reverse_lift_full_certificate_lattice_audit",
    ROOT / "reproductions" / "reverse_lift_full_certificate_lattice_audit.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class ReverseLiftFullCertificateLatticeAuditTests(unittest.TestCase):
    def test_small_audit_covers_every_core_prime(self):
        result = audit.run_audit(1_000)
        self.assertEqual(result["core_prime_count"], 14)
        self.assertEqual(result["captured_count"], 14)
        self.assertEqual(result["misses"], [])
        self.assertEqual(result["first_hit_certificate_type_counts"], {"I": 14, "II": 0})
        self.assertEqual(result["replaced_target_position_counts"], {"0": 0, "1": 0, "2": 14})
        self.assertEqual(result["unresolved_core_prime_source_count"], 0)
        self.assertEqual(result["records"][0]["prime"], 73)
        self.assertEqual(result["records"][0]["reverse_two_tail_lift"], {
            "replaced_target_position": 2,
            "replaced_target_term": 30_660,
            "source_denominator": 48,
            "source_term": 35,
        })

    def test_checked_artifact_summary(self):
        with (
            ROOT
            / "reproductions"
            / "reverse-lift-full-certificate-lattice-10k-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 10_000)
        self.assertEqual(result["core_prime_count"], 143)
        self.assertEqual(result["captured_count"], 143)
        self.assertEqual(result["misses"], [])
        self.assertEqual(
            result["certificate_candidates_checked_until_first_hit_or_exhaustion"],
            876,
        )
        self.assertEqual(result["first_hit_certificate_type_counts"], {"I": 143, "II": 0})
        self.assertEqual(
            result["replaced_target_position_counts"], {"0": 0, "1": 0, "2": 143}
        )
        self.assertEqual(result["even_source_denominator_count"], 110)
        self.assertEqual(result["unresolved_core_prime_source_count"], 0)
        self.assertEqual(result["maximum_first_hit_gap"], 23)


if __name__ == "__main__":
    unittest.main()
