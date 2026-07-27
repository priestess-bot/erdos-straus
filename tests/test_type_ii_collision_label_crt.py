import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_collision_label_crt",
    ROOT / "reproductions" / "type_ii_collision_label_crt.py",
)
assert SPEC and SPEC.loader
crt = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = crt
SPEC.loader.exec_module(crt)


class TypeIICollisionLabelCRTTests(unittest.TestCase):
    def test_coprime_crt(self):
        self.assertEqual(crt.combine_coprime_congruences([(2, 3), (5, 7)]), (5, 21))

    def test_delayed_release_label_states(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-collision-label-crt-372271201-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime"], 372_271_201)
        self.assertEqual(
            [
                (
                    row["shift"],
                    row["collision_product"],
                    row["collision_label_crt_residue"],
                    row["collision_label_crt_modulus"],
                )
                for row in result["states"]
            ],
            [(89, 21, 5, 21), (401, 5, 1, 5), (484, 1, 0, 1)],
        )
        self.assertTrue(
            all(
                row["new_prime_residue"] == row["forced_new_prime_residue"]
                for row in result["states"]
            )
        )


if __name__ == "__main__":
    unittest.main()
