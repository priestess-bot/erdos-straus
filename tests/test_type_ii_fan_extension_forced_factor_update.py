import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_fan_extension_forced_factor_update",
    ROOT / "reproductions" / "type_ii_fan_extension_forced_factor_update.py",
)
assert SPEC and SPEC.loader
update = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = update
SPEC.loader.exec_module(update)


class TypeIIFanExtensionForcedFactorUpdateTests(unittest.TestCase):
    def test_nested_modulus_can_only_add_forced_factors(self):
        self.assertEqual(
            update.forced_factor_updates(24, 120, 1, 1, (1, 2)),
            [
                {
                    "shift": 1,
                    "old_forced_factor": 1,
                    "new_forced_factor": 5,
                    "transferred_factor": 5,
                }
            ],
        )

    def test_h23_modulus_growth_updates_shift_five_without_new_collision_prime(self):
        result = update.run_witness()["h22_to_h23"]
        self.assertEqual(
            (result["old_modulus"], result["new_modulus"], result["modulus_growth"]),
            (77_597_520, 1_784_742_960, 23),
        )
        self.assertEqual(result["added_collision_primes"], [])
        self.assertEqual(
            result["forced_factor_updates"],
            [
                {
                    "shift": 5,
                    "old_forced_factor": 3,
                    "new_forced_factor": 69,
                    "transferred_factor": 23,
                }
            ],
        )

    def test_checked_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-fan-extension-forced-factor-update-h23.json"
        ).open(encoding="utf-8") as handle:
            expected = json.load(handle)
        self.assertEqual(update.run_witness(), expected)


if __name__ == "__main__":
    unittest.main()
