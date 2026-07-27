import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
COUNTEREXAMPLE_ARTIFACT = (
    ROOT
    / "reproductions"
    / "type-ii-pure-new-exception-selector-counterexample-1m-h20.json"
)
PRIMARY_H20_ARTIFACT = (
    ROOT
    / "reproductions"
    / "type-ii-pure-new-exception-dynamic-selector-1m-h20-summary.json"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


counterexample = load_module(
    "type_ii_pure_new_exception_selector_counterexample_h20",
    ROOT / "reproductions" / "type_ii_pure_new_exception_selector_counterexample_h20.py",
)
selector = load_module(
    "type_ii_pure_new_exception_dynamic_selector_h20_check",
    ROOT / "reproductions" / "type_ii_pure_new_exception_dynamic_selector.py",
)


class SelectorEnewCounterexampleH20Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit = counterexample.audit_counterexamples()

    def test_checked_artifact_matches_independent_exhaustion(self):
        artifact = json.loads(COUNTEREXAMPLE_ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(artifact, self.audit)

    def test_each_counterexample_fails_both_branches_exhaustively(self):
        self.assertEqual(
            [record["prime"] for record in self.audit["counterexamples"]],
            [214_729, 297_049, 878_089],
        )
        for record in self.audit["counterexamples"]:
            self.assertEqual(
                record["pure_new"]["qualifying_new_prime_factors"], []
            )
            tail = record["dynamic_low_defect_tail"]
            self.assertGreater(tail["eligible_divisor_count"], 0)
            self.assertEqual(tail["matching_divisors"], [])
            external = record["dynamic_external_source_exit"]
            self.assertGreater(external["eligible_square_divisor_count"], 0)
            self.assertEqual(external["matching_square_divisors"], [])

    def test_primary_selector_identifies_the_same_unresolved_primes(self):
        primary = selector.run_experiment(1_000_000, 20, 2)
        primary_artifact = json.loads(PRIMARY_H20_ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(selector.compact_report(primary), primary_artifact)
        self.assertEqual(
            primary["selector_union_unresolved_primes"],
            [214_729, 297_049, 878_089],
        )
        for record in primary["records"]:
            if record["prime"] not in {214_729, 297_049, 878_089}:
                continue
            self.assertIsNone(record["dynamic_low_defect_tail"])
            self.assertIsNone(record["dynamic_external_source_exit"])


if __name__ == "__main__":
    unittest.main()
