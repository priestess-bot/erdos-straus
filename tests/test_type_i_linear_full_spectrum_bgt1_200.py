from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_linear_full_spectrum_bgt1_200.py"
RESULT = ROOT / "reproductions" / "type-i-linear-full-spectrum-bgt1-200-results.json"

SPEC = importlib.util.spec_from_file_location("linear_full_spectrum_bgt1_200", SCRIPT)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeILinearFullSpectrumBGT1200Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = profile.run_audit()
        cls.stored = json.loads(RESULT.read_text(encoding="utf-8"))

    def test_reproduction_matches_hash_frozen_artifact(self):
        self.assertEqual(self.payload, self.stored)
        self.assertEqual(self.payload["selected_prime_count"], 200)
        self.assertEqual(self.payload["linear_R_exhaustively_checked"], 10_292)
        self.assertEqual(self.payload["directed_linear_source_state_count"], 18_074)
        self.assertEqual(
            self.payload["classification_totals"],
            {"hit": 1_018, "finite_exponent": 2_752, "subgroup_character": 6_522},
        )
        self.assertEqual(self.payload["two_residue_eligible_R_count"], 3_209)
        self.assertEqual(self.payload["two_residue_subgroup_escape_R_count"], 351)

    def test_each_selected_point_has_both_obstruction_types_and_a_hit(self):
        for record in self.payload["records"]:
            counts = record["classification_counts"]
            self.assertGreaterEqual(counts["hit"], 1, record["prime"])
            self.assertGreaterEqual(counts["finite_exponent"], 1, record["prime"])
            self.assertGreaterEqual(counts["subgroup_character"], 1, record["prime"])
            self.assertGreaterEqual(counts["hit"], 1)
            self.assertLessEqual(counts["hit"], 11)

    def test_two_residue_escape_has_no_subgroup_character_state(self):
        escape_records = [
            row
            for record in self.payload["records"]
            for row in record["records"]
            if row["two_residue_eligible"] and row["minus_one_in_two_cyclic"]
        ]
        self.assertEqual(len(escape_records), 351)
        self.assertNotIn("subgroup_character", [row["classification"] for row in escape_records])
        self.assertEqual(
            sum(row["classification"] == "hit" for row in escape_records), 129
        )
        self.assertEqual(
            sum(row["classification"] == "finite_exponent" for row in escape_records), 222
        )

    def test_known_complete_spectrum_point_is_preserved(self):
        record = next(row for row in self.payload["records"] if row["prime"] == 878_089)
        self.assertEqual(record["classification_counts"], {"hit": 1, "finite_exponent": 2, "subgroup_character": 21})
        self.assertEqual(record["hit_R"], [59])
        self.assertEqual(record["finite_exponent_R"], [279, 503])


if __name__ == "__main__":
    unittest.main()
