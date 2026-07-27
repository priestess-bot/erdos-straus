import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "chamberland_ac_ray_translation",
    ROOT / "reproductions" / "chamberland_ac_ray_translation.py",
)
assert SPEC and SPEC.loader
translation = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = translation
SPEC.loader.exec_module(translation)


class ChamberlandAcRayTranslationTests(unittest.TestCase):
    def test_non_nested_chamberland_pair_becomes_an_ac_ray(self):
        # Chamberland's p=1009 example: 1009=23*47-4*3*6.
        record = translation.from_chamberland(23, 47, 3, 6)
        self.assertEqual(
            {key: record[key] for key in ("p", "a", "c", "k", "b")},
            {"p": 1009, "a": 3, "c": 2, "k": 1, "b": 44},
        )

    def test_ac_ray_round_trips_to_a_nested_chamberland_pair(self):
        record = translation.to_chamberland(84_525_841, 1, 14, 30, 1679)
        self.assertEqual(
            {key: record[key] for key in ("r", "s1", "s2", "a", "c", "k")},
            {"r": 50_343, "s1": 1, "s2": 14, "a": 1, "c": 14, "k": 30},
        )

    def test_bounded_witnesses_translate_in_the_small_audit(self):
        result = translation.run_audit(10_000, 14)
        self.assertEqual(result["translated_witness_count"], result["core_prime_count"])
        self.assertGreater(result["translated_witness_count"], 0)


if __name__ == "__main__":
    unittest.main()
