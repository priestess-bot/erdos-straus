import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "reproductions" / filename)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


bridge = load_module(
    "boundary_gap_27_reverse_two_tail_bridge",
    "boundary_gap_27_reverse_two_tail_bridge.py",
)
targeted = load_module("targeted_descent_bridge_for_reverse_divisor_test", "targeted_descent_bridge.py")


class BoundaryGap27ReverseTwoTailBridgeTests(unittest.TestCase):
    def test_divisor_enumerator_matches_direct_small_scan(self):
        for prime, target_term in ((73, 20), (73, 220), (73, 4_015), (193, 1_331_700)):
            _, divisor_lifts = bridge.reverse_two_tail_lifts_by_divisors(prime, target_term)
            direct_lifts = targeted.reverse_two_tail_lifts(prime, target_term)
            self.assertEqual(
                [(item["source_denominator"], item["source_term"]) for item in divisor_lifts],
                [(item["source_denominator"], item["source_term"]) for item in direct_lifts],
                (prime, target_term),
            )

    def test_normal_form_maximum_tail_selector_matches_generic_divisor_scan(self):
        prime, gap = 477_015_289, 27
        for A, B, C in ((29, 433, 9_497), (29, 1, 4_112_201), (12_557, 1, 9_497)):
            certificate = bridge.short_certificate.type_i_normal_form_certificate(prime, gap, A, B)
            assert certificate is not None
            target_factors = bridge.type_i_target_factorizations(prime, gap, A, B, C)[2]
            generic = bridge.reverse_two_tail_lifts_by_divisors(prime, certificate.z, target_factors)
            normal = bridge.type_i_normal_reverse_two_tail_lifts(prime, gap, A, B, C)
            self.assertEqual(normal, generic, (A, B, C))

    def test_boundary_gap_twenty_seven_audit_rebuilds_and_has_two_even_sources(self):
        artifact = ROOT / "reproductions" / "boundary-gap-27-reverse-two-tail-477015289-results.json"
        expected = json.loads(artifact.read_text(encoding="utf-8"))
        actual = bridge.run_audit()
        self.assertEqual(actual, expected)
        self.assertEqual(actual["total_reverse_two_tail_lift_count"], 2)
        hits = [
            (record["divisor"], term["replaced_target_position"], lift)
            for record in actual["records"]
            for term in record["reverse_two_tail_by_replaced_target_term"]
            for lift in term["reverse_two_tail_lifts"]
        ]
        self.assertEqual(
            hits,
            [
                (3_458_361_041, 2, {"source_denominator": 32_897_608, "source_term": 8_833_617, "bridge_divisor": 61_564_910_063_707_146_394_555_256_094_736}),
                (1_497_470_330_753, 2, {"source_denominator": 475_989_640, "source_term": 55_344_063_985, "bridge_divisor": 328_365_451_112_903_404_437_355_024}),
            ],
        )
        self.assertTrue(all(lift[2]["source_denominator"] % 2 == 0 for lift in hits))


if __name__ == "__main__":
    unittest.main()
