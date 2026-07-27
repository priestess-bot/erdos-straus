import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_tail_reverse_even_source_support_minimization",
    ROOT / "reproductions" / "type_i_tail_reverse_even_source_support_minimization.py",
)
assert SPEC and SPEC.loader
support_min = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = support_min
SPEC.loader.exec_module(support_min)


class TypeITailReverseEvenSourceSupportMinimizationTests(unittest.TestCase):
    def test_four_support_boundary_records_rebuild(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-even-source-support-min-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        records = {record["prime"]: record["selected_edge"] for record in expected["records"]}
        for prime in (42_622_969, 357_834_409):
            witness, _, _ = support_min.least_support_edge(prime, 215)
            self.assertEqual(witness, records[prime])
            self.assertEqual(witness["E_prime_support_count"], 4)
        self.assertEqual(
            expected["least_E_support_histogram"], {"1": 1_061, "2": 621, "3": 33, "4": 2}
        )


if __name__ == "__main__":
    unittest.main()
