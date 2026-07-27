import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(name: str) -> dict[str, object]:
    with (ROOT / "reproductions" / name).open(encoding="utf-8") as handle:
        return json.load(handle)


class H19K23GlobalTailPressureExtensionTests(unittest.TestCase):
    def test_extended_global_closure_has_no_miss_and_expected_defects(self):
        result = load("h19-k23-full-global-tail-closure-2097152.json")
        self.assertEqual(result["input_parameter_limit_exclusive"], 2_097_152)
        self.assertEqual(result["input_record_count"], 4_466_959)
        self.assertEqual(result["direct_global_tail_count"], 4_457_134)
        self.assertEqual(result["rewritten_global_tail_count"], 9_825)
        self.assertEqual(result["rewrite_support_defect_histogram"], {"0": 4670, "1": 5087, "2": 68})
        self.assertEqual(result["global_tail_misses"], [])

    def test_extended_support_and_base_only_closures_form_exact_partitions(self):
        one_support = load("h19-k23-global-tail-one-support-closure-2097152.json")
        base_only = load("h19-k23-global-tail-base-only-descent-2097152.json")
        self.assertEqual(one_support["input_rewrite_count"], 9_825)
        self.assertEqual(one_support["rerouted_support_two_count"], 68)
        self.assertEqual(one_support["final_rewrite_support_histogram"], {"0": 4697, "1": 5128})
        self.assertEqual(base_only["input_rewrite_count"], 9_825)
        self.assertEqual(base_only["initial_base_only_count"], 4_697)
        self.assertEqual(base_only["input_one_support_count"], 5_128)
        self.assertEqual(base_only["later_base_only_reroute_count"], 5_106)
        self.assertEqual(base_only["base_only_rewrite_count"], 9_803)
        self.assertEqual(base_only["global_base_only_pressure_count"], 22)
        self.assertEqual(
            sum(
                1
                for row in base_only["global_base_only_pressure_records"]
                if row["current_global_tail_gap"] in {31, 35, 39, 59, 71}
            ),
            22,
        )

    def test_old_pressure_set_is_a_proper_subset_of_the_extended_set(self):
        previous = load("h19-k23-global-tail-base-only-descent-1048576.json")
        extended = load("h19-k23-global-tail-base-only-descent-2097152.json")
        old_primes = {
            int(row["prime"]) for row in previous["global_base_only_pressure_records"]
        }
        new_primes = {
            int(row["prime"]) for row in extended["global_base_only_pressure_records"]
        }
        self.assertEqual(len(old_primes), 12)
        self.assertEqual(len(new_primes), 22)
        self.assertTrue(old_primes < new_primes)
        self.assertEqual(
            sum(
                row["shared_selector_gap"] == 51
                for row in extended["global_base_only_pressure_records"]
            ),
            1,
        )


if __name__ == "__main__":
    unittest.main()
