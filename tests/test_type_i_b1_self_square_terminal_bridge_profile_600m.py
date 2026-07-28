from fractions import Fraction
import json
from pathlib import Path
import unittest

from reproductions import type_i_b1_self_square_terminal_bridge_profile_600m as bridge


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "reproductions" / "type-i-b1-self-square-terminal-bridge-profile-600m-results.json"


class TypeIBOneSelfSquareTerminalBridgeTests(unittest.TestCase):
    def test_displayed_b1_self_square_witness(self):
        witness = bridge.self_square_witness(337, 17, 5, 118, 7, 590)
        self.assertEqual(
            witness,
            {
                "A": 17,
                "B": 1,
                "C": 5,
                "H": 118,
                "m": 3,
                "R": 7,
                "K": 590,
                "E": 400,
                "source_denominator": 280,
                "source_term": 413,
                "quotient": 14,
                "upper_half": True,
            },
        )
        assert witness is not None
        self.assertEqual(
            Fraction(4, witness["source_denominator"]),
            Fraction(1, witness["source_term"])
            + Fraction(1, witness["A"] * witness["C"])
            + Fraction(1, witness["A"] * witness["C"] * witness["H"]),
        )

    def test_upper_half_condition_is_exact_on_the_profile(self):
        payload = bridge.run_audit()
        self.assertEqual(payload["selected_B_one_target_count"], 1964)
        self.assertEqual(payload["self_square_bridge_count"], 1092)
        self.assertEqual(payload["self_square_upper_half_count"], 1090)
        self.assertEqual(payload["parity_failure_count"], 807)
        self.assertEqual(payload["small_complement_failure_count"], 68)
        self.assertEqual(
            payload["self_square_origin_counts"],
            {
                "500_direct_extension": 1,
                "500_direct_upper": 907,
                "600_direct_upper": 157,
                "600_reselected_upper": 27,
            },
        )
        for record in payload["records"]:
            prime = int(record["prime"])
            witness = record["witness"]
            self.assertEqual(bool(witness["upper_half"]), int(witness["H"]) > 8 * int(witness["C"]))
            self.assertEqual(int(witness["source_denominator"]) % 2, 0)
            self.assertTrue(2 <= int(witness["source_denominator"]) < prime)
            self.assertEqual(
                Fraction(4, int(witness["source_denominator"])),
                Fraction(1, int(witness["source_term"]))
                + Fraction(1, int(witness["A"]) * int(witness["C"]))
                + Fraction(1, int(witness["A"]) * int(witness["C"]) * int(witness["H"])),
            )

    def test_checked_in_artifact_is_reproducible(self):
        self.assertEqual(json.loads(RESULT.read_text(encoding="utf-8")), bridge.run_audit())


if __name__ == "__main__":
    unittest.main()
