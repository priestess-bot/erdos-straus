import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_b1_self_square_reselection_profile_600m.py"
RESULT_215 = ROOT / "reproductions" / "type-i-b1-self-square-reselection-profile-600m-results.json"
RESULT_999 = ROOT / "reproductions" / "type-i-b1-self-square-reselection-profile-600m-m999-results.json"

SPEC = importlib.util.spec_from_file_location("type_i_b1_self_square_reselection_profile", SCRIPT)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIBOneSelfSquareReselectionProfileTests(unittest.TestCase):
    def test_short_box_profile_is_reproducible(self):
        payload = profile.run_audit()
        self.assertEqual(payload, json.loads(RESULT_215.read_text(encoding="utf-8")))
        self.assertEqual(
            (
                payload["ordinary_tail_pressure_count"],
                payload["self_square_reselection_covered_count"],
                payload["self_square_reselection_miss_count"],
                payload["B_one_normal_forms_exhaustively_checked"],
                payload["upper_self_square_candidate_count"],
                payload["maximum_selected_gap"],
            ),
            (1964, 1844, 120, 17492, 6012, 215),
        )

    def test_extended_box_artifact_replays_every_selected_witness(self):
        payload = json.loads(RESULT_999.read_text(encoding="utf-8"))
        self.assertEqual(
            (
                payload["gap_cap"],
                payload["ordinary_tail_pressure_count"],
                payload["self_square_reselection_covered_count"],
                payload["self_square_reselection_miss_count"],
                payload["B_one_normal_forms_exhaustively_checked"],
                payload["upper_self_square_candidate_count"],
                payload["maximum_selected_gap"],
            ),
            (999, 1964, 1907, 57, 27531, 7856, 971),
        )
        for record in payload["records"]:
            witness = record["selected_witness"]
            self.assertEqual(int(witness["A"]) % 2, 1)
            self.assertGreaterEqual(int(witness["A"]), 2 * int(witness["m"]))
            replay = profile.self_square.self_square_witness(
                int(record["prime"]),
                int(witness["A"]),
                int(witness["C"]),
                int(witness["H"]),
                int(witness["R"]),
                int(witness["K"]),
            )
            self.assertEqual(replay, witness)
            self.assertTrue(bool(witness["upper_half"]))


if __name__ == "__main__":
    unittest.main()
