import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_shared_selector_audit",
    ROOT / "reproductions" / "h19_k23_shared_selector_audit.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class H19K23SharedSelectorAuditTests(unittest.TestCase):
    def test_small_parameter_fixture_has_shared_type_ii_certificates(self):
        result = audit.run_audit(8, 59)
        self.assertEqual(result["prime_count"], 29)
        self.assertEqual(result["captured_count"], 29)
        self.assertEqual(result["misses"], [])
        self.assertEqual(result["largest_minimum_gap"], 23)
        self.assertEqual(
            result["minimum_gap_histogram"],
            {"3": 10, "7": 10, "11": 4, "15": 3, "19": 1, "23": 1},
        )

    def test_parallel_branch_audit_matches_serial_fixture(self):
        self.assertEqual(audit.run_audit(8, 59), audit.run_audit(8, 59, workers=2))

    def test_compact_records_keep_the_ordinary_tail_closure_fields(self):
        result = audit.run_audit(8, 59, compact=True)
        self.assertEqual(result["record_format"], "compact-tail")
        self.assertEqual(
            set(result["records"][0]["first_witness"]),
            {"gap", "x", "type_ii_divisor"},
        )

    def test_streamed_compact_audit_is_parseable_and_complete(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "compact-audit.json"
            summary = audit.run_compact_audit_to_file(output, 8, 59, workers=2)
            with output.open(encoding="utf-8") as handle:
                result = json.load(handle)
        self.assertEqual(result["record_format"], "compact-tail")
        self.assertEqual(result["prime_count"], 29)
        self.assertEqual(result["captured_count"], 29)
        self.assertEqual(result["captured_count"], len(result["records"]))
        self.assertEqual(result["misses"], [])
        self.assertEqual(summary["minimum_gap_histogram"], result["minimum_gap_histogram"])
        self.assertEqual(
            set(result["records"][0]["first_witness"]),
            {"gap", "x", "type_ii_divisor"},
        )

    def test_checked_artifact_summary(self):
        with (
            ROOT / "reproductions" / "h19-k23-shared-selector-audit.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["parameter_limit_exclusive"], 1024)
        self.assertEqual(result["gap_cap"], 239)
        self.assertEqual(result["prime_count"], 2687)
        self.assertEqual(result["captured_count"], 2687)
        self.assertEqual(result["misses"], [])
        self.assertEqual(result["largest_minimum_gap"], 59)

    def test_extended_sixteen_thousand_three_hundred_eighty_four_layer_audit(self):
        with (
            ROOT / "reproductions" / "h19-k23-shared-selector-audit-16384.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["parameter_limit_exclusive"], 16_384)
        self.assertEqual(result["gap_cap"], 239)
        self.assertEqual(result["prime_count"], 39_658)
        self.assertEqual(result["captured_count"], 39_658)
        self.assertEqual(result["misses"], [])
        self.assertEqual(result["largest_minimum_gap"], 71)
        self.assertEqual(result["minimum_gap_histogram"]["71"], 2)
        records = [
            row for row in result["records"] if row["first_witness"]["gap"] == 71
        ]
        self.assertEqual(
            [row["prime"] for row in records],
            [23_563_608_395_688_001, 5_771_131_031_426_401],
        )
        self.assertTrue(all(row["first_witness"]["shared_divisor"] == 72 for row in records))

    def test_extended_thirty_two_thousand_seven_hundred_sixty_eight_layer_audit(self):
        with (
            ROOT / "reproductions" / "h19-k23-shared-selector-audit-32768.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["parameter_limit_exclusive"], 32_768)
        self.assertEqual(result["gap_cap"], 239)
        self.assertEqual(result["prime_count"], 77_823)
        self.assertEqual(result["captured_count"], 77_823)
        self.assertEqual(result["misses"], [])
        self.assertEqual(result["largest_minimum_gap"], 87)
        self.assertEqual(result["minimum_gap_histogram"]["87"], 2)

    def test_extended_sixty_five_thousand_five_hundred_thirty_six_layer_audit(self):
        with (
            ROOT / "reproductions" / "h19-k23-shared-selector-audit-65536.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["parameter_limit_exclusive"], 65_536)
        self.assertEqual(result["gap_cap"], 239)
        self.assertEqual(result["prime_count"], 152_893)
        self.assertEqual(result["captured_count"], 152_893)
        self.assertEqual(result["misses"], [])
        self.assertEqual(result["largest_minimum_gap"], 87)
        self.assertEqual(result["minimum_gap_histogram"]["83"], 1)

    def test_extended_one_hundred_thirty_one_thousand_layer_audit(self):
        with (
            ROOT / "reproductions" / "h19-k23-shared-selector-audit-131072.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["parameter_limit_exclusive"], 131_072)
        self.assertEqual(result["gap_cap"], 239)
        self.assertEqual(result["prime_count"], 299_782)
        self.assertEqual(result["captured_count"], 299_782)
        self.assertEqual(result["misses"], [])
        self.assertEqual(result["largest_minimum_gap"], 87)
        self.assertEqual(result["minimum_gap_histogram"]["63"], 4)

    def test_extended_two_hundred_sixty_two_thousand_layer_audit(self):
        with (
            ROOT / "reproductions" / "h19-k23-shared-selector-audit-262144.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["parameter_limit_exclusive"], 262_144)
        self.assertEqual(result["gap_cap"], 239)
        self.assertEqual(result["prime_count"], 588_526)
        self.assertEqual(result["captured_count"], 588_526)
        self.assertEqual(result["misses"], [])
        self.assertEqual(result["largest_minimum_gap"], 99)
        self.assertEqual(result["minimum_gap_histogram"]["99"], 1)


if __name__ == "__main__":
    unittest.main()
