import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_tail_reverse_even_source_closure",
    ROOT / "reproductions" / "type_i_tail_reverse_even_source_closure.py",
)
assert SPEC and SPEC.loader
even_source = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = even_source
SPEC.loader.exec_module(even_source)


class TypeITailReverseEvenSourceClosureTests(unittest.TestCase):
    def test_full_even_source_closure_rebuilds(self):
        tail = json.loads(
            (ROOT / "reproductions" / "type-ii-tail-deflation-500m-full-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-even-source-closure-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = even_source.run_audit(tail)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (actual["even_source_captured_count"], actual["even_source_misses"], actual["maximum_selected_gap"]),
            (1_717, [], 215),
        )

    def test_three_late_gap_boundaries_rebuild_as_even_sources(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-even-source-closure-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        records = {record["prime"]: record for record in expected["records"]}
        for prime, gap in ((81_209_209, 151), (334_995_049, 135), (493_936_249, 215)):
            witness, _, _ = even_source.first_even_source_edge(prime, 215)
            self.assertEqual(witness, {key: value for key, value in records[prime].items() if key != "prime"})
            self.assertEqual(witness["gap"], gap)
            self.assertEqual(witness["reverse_two_tail_lift"]["source_denominator"] % 2, 0)


if __name__ == "__main__":
    unittest.main()
