import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "even_source_exchange_symmetry",
    ROOT / "reproductions" / "even_source_exchange_symmetry.py",
)
assert SPEC and SPEC.loader
symmetry = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = symmetry
SPEC.loader.exec_module(symmetry)


class EvenSourceExchangeSymmetryTests(unittest.TestCase):
    def test_exchange_state_for_an_in_window_fourth_pressure_ray(self):
        self.assertEqual(
            symmetry.exchange_state(4037, 6901, 23),
            {
                "prime": 640_775_689,
                "distance": 4037,
                "divisor": 6901,
                "r": 23,
                "first_k": 39_681,
                "first_s": 92_852,
                "second_k": 23_213,
                "second_s": 158_724,
                "shared_m1": 3_684_460_212,
            },
        )

    def test_checked_tail_profile_exchange_orbits(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-fourth-even-source-exchange-symmetry-640775689-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime"], 640_775_689)
        self.assertEqual(result["eligible_ray_count"], 25)
        self.assertEqual(result["in_window_directed_partner_count"], 19)
        self.assertEqual(result["in_window_exchange_orbit_count"], 10)
        self.assertEqual(result["unpaired_eligible_ray_count"], 6)

    def test_ineligible_congruence_is_rejected(self):
        with self.assertRaises(ValueError):
            symmetry.exchange_state(3, 1253, 15)


if __name__ == "__main__":
    unittest.main()
