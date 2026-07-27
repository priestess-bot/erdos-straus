import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_h19_even_source_support_minimization",
    ROOT / "reproductions" / "type_i_h19_even_source_support_minimization.py",
)
assert SPEC and SPEC.loader
support_min = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = support_min
SPEC.loader.exec_module(support_min)


class TypeIH19EvenSourceSupportMinimizationTests(unittest.TestCase):
    def test_high_support_boundary_records_rebuild(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-h19-even-source-support-min-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        records = {record["prime"]: record["selected_edge"] for record in expected["records"]}
        for prime, support in ((48_605_881, 4), (707_590_321, 3)):
            witness, _, _ = support_min.support_min.least_support_edge(prime, 215)
            self.assertEqual(witness, records[prime])
            self.assertEqual(witness["E_prime_support_count"], support)
        self.assertEqual(
            expected["least_E_support_histogram"], {"1": 474, "2": 188, "3": 1, "4": 1}
        )


if __name__ == "__main__":
    unittest.main()
