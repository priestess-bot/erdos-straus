import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_progression_trap",
    ROOT / "reproductions" / "type_ii_progression_trap.py",
)
assert SPEC and SPEC.loader
progression_trap = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = progression_trap
SPEC.loader.exec_module(progression_trap)


class TypeIIProgressionTrapTests(unittest.TestCase):
    def test_record_seed_has_unique_trap_in_scanned_extension(self):
        traps = progression_trap.find_traps(153_633_769, 31, 131)
        self.assertEqual(len(traps), 1)
        trap = traps[0]
        self.assertEqual(
            (
                trap["future_j"],
                trap["gap"],
                trap["fixed_factor"],
                trap["target_scale"],
                trap["cofactor_residue_mod_gap"],
            ),
            (52, 207, 9_682, 47, 34),
        )
        self.assertTrue(
            all(
                progression_trap.certificate_at_index(trap, index)["exact_identity"]
                for index in (0, 1, 2)
            )
        )

    def test_distinguishes_a_second_seed_and_a_no_trap_case(self):
        candidate_count, secondary = progression_trap.find_all_divisor_traps(
            33_011_449, 20
        )
        self.assertEqual(candidate_count, 5_616)
        self.assertEqual(
            [
                (
                    trap["future_j"],
                    trap["gap"],
                    trap["fixed_factor"],
                    trap["target_scale"],
                )
                for trap in secondary
            ],
            [(36, 143, 426, 3), (178, 711, 5_680, 8), (604, 2415, 31_382, 13)],
        )
        no_trap_count, no_traps = progression_trap.find_all_divisor_traps(
            8_803_369, 20
        )
        self.assertEqual(no_trap_count, 3_929)
        self.assertEqual(no_traps, ())

    def test_checked_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-progression-trap-p153633769-j31-to131-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["seed_prime"], 153_633_769)
        self.assertTrue(result["primitive_progression"])
        self.assertEqual(len(result["traps"]), 1)
        self.assertEqual(result["traps"][0]["gap"], 207)
        self.assertTrue(
            all(sample["exact_identity"] for sample in result["first_trap_samples"])
        )

    def test_complete_no_trap_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-progression-trap-p8803369-j20-complete-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertTrue(result["all_divisor_mode"])
        self.assertEqual(result["candidate_gap_count"], 3_929)
        self.assertEqual(result["traps"], [])


if __name__ == "__main__":
    unittest.main()
