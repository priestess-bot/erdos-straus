import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_minimal_collision_support",
    ROOT / "reproductions" / "type_ii_minimal_collision_support.py",
)
assert SPEC and SPEC.loader
support = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = support
SPEC.loader.exec_module(support)


class TypeIIMinimalCollisionSupportTests(unittest.TestCase):
    def test_ten_million_checked_artifact(self):
        path = ROOT / "reproductions" / "type-ii-minimal-collision-support-h19-10m-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["new_factor_state_count"], 34)
        self.assertEqual(result["one_new_witness_count"], 34)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(result["minimum_collision_multiplicity_distribution"], {"0": 32, "1": 2})
        self.assertEqual(result["one_collision_prime_distribution"], {"3": 1, "5": 1})

    def test_two_hundred_million_checked_artifact(self):
        path = ROOT / "reproductions" / "type-ii-minimal-collision-support-h19-200m-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["new_factor_state_count"], 199)
        self.assertEqual(result["one_new_witness_count"], 199)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(
            result["minimum_collision_multiplicity_distribution"], {"0": 193, "1": 6}
        )
        self.assertEqual(
            result["one_collision_prime_distribution"],
            {"3": 2, "5": 1, "7": 1, "13": 1, "17": 1},
        )
        record = next(row for row in result["profiles"] if row["prime"] == 55_722_241)
        self.assertEqual(record["minimum_collision_multiplicity"], 1)
        self.assertEqual(record["first_minimum_collision_shift"], 48)
        self.assertEqual(record["selected_witness"]["h"], 10_751)

    def test_three_hundred_million_checked_artifact(self):
        path = ROOT / "reproductions" / "type-ii-minimal-collision-support-h19-300m-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["new_factor_state_count"], 260)
        self.assertEqual(result["one_new_witness_count"], 260)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(
            result["minimum_collision_multiplicity_distribution"], {"0": 253, "1": 7}
        )
        self.assertEqual(
            result["one_collision_prime_distribution"],
            {"3": 3, "5": 1, "7": 1, "13": 1, "17": 1},
        )
        record = next(row for row in result["profiles"] if row["prime"] == 283_163_161)
        self.assertEqual(record["minimum_collision_multiplicity"], 1)
        self.assertEqual(record["first_minimum_collision_shift"], 53)
        self.assertEqual(record["selected_witness"]["h"], 3_603)

    def test_five_hundred_million_detects_the_first_two_collision_state(self):
        path = ROOT / "reproductions" / "type-ii-minimal-collision-support-h19-500m-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["new_factor_state_count"], 341)
        self.assertEqual(result["one_new_witness_count"], 341)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(
            result["minimum_collision_multiplicity_distribution"], {"0": 332, "1": 8, "2": 1}
        )
        record = next(row for row in result["profiles"] if row["prime"] == 372_271_201)
        self.assertEqual(record["minimum_collision_multiplicity"], 2)
        self.assertEqual(record["first_minimum_collision_shift"], 89)
        self.assertEqual(record["selected_witness"]["h"], 22_071)

    def test_one_billion_keeps_one_two_collision_state_and_closes_all_new_factor_states(self):
        path = ROOT / "reproductions" / "type-ii-minimal-collision-support-h19-1b-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["new_factor_state_count"], 541)
        self.assertEqual(result["one_new_witness_count"], 541)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(
            result["minimum_collision_multiplicity_distribution"], {"0": 530, "1": 10, "2": 1}
        )
        record = next(row for row in result["profiles"] if row["prime"] == 640_775_689)
        self.assertEqual(record["minimum_collision_multiplicity"], 0)
        self.assertEqual(record["first_minimum_collision_shift"], 45)
        self.assertEqual(record["selected_witness"]["h"], 359)

    def test_one_billion_s500_recovers_the_zero_one_collision_profile(self):
        path = ROOT / "reproductions" / "type-ii-minimal-collision-support-h19-1b-s500-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["shift_cap"], 500)
        self.assertEqual(result["new_factor_state_count"], 541)
        self.assertEqual(result["one_new_witness_count"], 541)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(
            result["minimum_collision_multiplicity_distribution"], {"0": 539, "1": 2}
        )
        self.assertEqual(result["one_collision_prime_distribution"], {"5": 1, "17": 1})
        self.assertEqual(
            max(row["first_minimum_collision_shift"] for row in result["profiles"]), 484
        )
        delayed = next(row for row in result["profiles"] if row["prime"] == 372_271_201)
        self.assertEqual(delayed["minimum_collision_multiplicity"], 0)
        self.assertEqual(delayed["first_minimum_collision_shift"], 484)
        self.assertEqual(delayed["selected_witness"]["h"], 3_343)

    def test_one_billion_s1008_recovers_a_pure_new_witness_for_every_state(self):
        path = ROOT / "reproductions" / "type-ii-minimal-collision-support-h19-1b-s1008-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["shift_cap"], 1_008)
        self.assertEqual(result["new_factor_state_count"], 541)
        self.assertEqual(result["one_new_witness_count"], 541)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(result["minimum_collision_multiplicity_distribution"], {"0": 541})
        self.assertEqual(result["one_collision_prime_distribution"], {})
        record = max(result["profiles"], key=lambda row: row["first_minimum_collision_shift"])
        self.assertEqual(record["prime"], 178_400_041)
        self.assertEqual(record["first_minimum_collision_shift"], 1_008)
        self.assertEqual(record["selected_witness"]["h"], 9_743)

    def test_shift_cap_override_can_recover_the_delayed_pure_new_witness(self):
        path = ROOT / "reproductions" / "type-ii-source-free-transition-h19-1b-results.json"
        with path.open(encoding="utf-8") as handle:
            payload = json.load(handle)
        delayed = next(row for row in payload["profiles"] if row["prime"] == 372_271_201)
        payload["profiles"] = [delayed]
        result = support.run_profile(payload, shift_cap_override=484)
        self.assertEqual(result["shift_cap"], 484)
        self.assertEqual(result["minimum_collision_multiplicity_distribution"], {0: 1})
        self.assertEqual(result["profiles"][0]["selected_witness"]["h"], 3_343)


if __name__ == "__main__":
    unittest.main()
