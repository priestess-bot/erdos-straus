import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_mixed_terminal_dense_interval",
    ROOT / "reproductions" / "type_i_mixed_terminal_dense_interval.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


class TypeIMixedTerminalDenseIntervalTests(unittest.TestCase):
    def test_small_dense_interval_closes_and_partitions_exactly(self):
        result = audit.run_audit(1, 100_000, 215)
        self.assertEqual(result["core_prime_count"], 1_181)
        self.assertEqual(result["ordinary_type_ii_tail_miss_count"], 2)
        self.assertEqual(result["type_i_even_terminal_bridge_count"], 2)
        self.assertEqual(result["even_source_misses"], [])
        self.assertEqual(
            result["ordinary_type_ii_tail_hit_count"]
            + result["type_i_even_terminal_bridge_count"],
            result["core_prime_count"],
        )
        self.assertEqual(result["maximum_selected_type_i_gap"], 31)

    def test_invalid_interval_and_gap_are_rejected(self):
        with self.assertRaises(ValueError):
            audit.run_audit(100, 100, 215)
        with self.assertRaises(ValueError):
            audit.run_audit(1, 100, 210)

    def test_dense_500m_to_600m_artifact_has_only_exact_target_terminal_bridges(self):
        payload = json.loads(
            (
                ROOT / "reproductions" / "type-i-mixed-terminal-dense-500m-600m-results.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(payload["prime_interval"], [500_000_001, 600_000_000])
        self.assertEqual(payload["core_prime_count"], 621_951)
        self.assertEqual(
            (
                payload["ordinary_type_ii_tail_hit_count"],
                payload["ordinary_type_ii_tail_miss_count"],
                payload["type_i_even_terminal_bridge_count"],
                payload["maximum_selected_type_i_gap"],
            ),
            (621_704, 247, 247, 111),
        )
        self.assertEqual(payload["even_source_misses"], [])
        self.assertEqual(
            payload["ordinary_type_ii_tail_hit_count"]
            + payload["type_i_even_terminal_bridge_count"],
            payload["core_prime_count"],
        )

        for record in payload["type_i_even_terminal_bridge_records"]:
            prime = int(record["prime"])
            witness = record["type_i_even_witness"]
            gap = int(witness["gap"])
            A, B, C = (int(value) for value in witness["normal_form"])
            R = (4 * B * B * C + 1) // gap
            H = A * R - B
            K = B * C * H
            E = int(witness["reverse_two_tail_lift"]["bridge_divisor"]) // (prime * prime)
            source = int(witness["reverse_two_tail_lift"]["source_denominator"])
            self.assertEqual(gap * R, 4 * B * B * C + 1)
            self.assertEqual(4 * K, prime * R + 1)
            self.assertEqual(int(witness["reverse_two_tail_lift"]["bridge_divisor"]), prime * prime * E)
            self.assertEqual((E % R, E % 2), (1, 0))
            self.assertEqual(4 * K * K % E, 0)
            self.assertLessEqual(E, 4 * K - 2 * R)
            self.assertEqual(source % 2, 0)
            self.assertEqual(
                Fraction(4, source),
                sum((Fraction(1, value) for value in witness["source_solution"]), Fraction()),
            )


if __name__ == "__main__":
    unittest.main()
