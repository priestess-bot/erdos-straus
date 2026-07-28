import importlib.util
import json
import math
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_tail_upper_b1_completion_profile_500m",
    ROOT / "reproductions" / "type_i_tail_upper_b1_completion_profile_500m.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeITailUpperB1CompletionProfile500MTests(unittest.TestCase):
    def assert_source_first_coordinates(self, prime, certificate):
        gap = int(certificate["gap"])
        A, B, C = (int(value) for value in certificate["normal_form"])
        R = int(certificate["R"])
        K = int(certificate["K"])
        E = int(certificate["E"])
        source = int(certificate["source_denominator"])
        shift = prime - source

        self.assertEqual(B, 1)
        self.assertEqual(shift % 2, 1)
        self.assertGreaterEqual(source, (prime + 1) // 2)
        self.assertEqual(R % 4, 3)
        self.assertEqual(E, shift * R + 1)
        self.assertEqual((source * source // math.gcd(E, 4)) % E, 0)
        self.assertEqual(K % C, 0)
        self.assertEqual((4 * C + 1) % R, 0)

        H = K // C
        self.assertEqual((H + 1) % R, 0)
        self.assertEqual((4 * C + 1) // R, gap)
        self.assertEqual(A, (H + 1) // R)
        self.assertEqual(prime, 4 * A * C - gap)
        self.assertEqual(4 * K, prime * R + 1)
        self.assertLess(E, 2 * K)

    def external_retraction_source(self, prime, certificate):
        """Return the canonical external source when this B=1 form retracts."""
        gap = int(certificate["gap"])
        A, B, C = (int(value) for value in certificate["normal_form"])
        R = int(certificate["R"])
        K = int(certificate["K"])
        k = (R + 1) // 4

        self.assertEqual(B, 1)
        if K % k:
            return None

        self.assertEqual(((prime - 1) // 4) % k, 0)
        source = K // k
        self.assertEqual((R * prime + 1) % (R + 1), 0)
        self.assertEqual(source, (R * prime + 1) // (R + 1))
        self.assertEqual(4 * K, (R + 1) * source)
        self.assertEqual(K % C, 0)
        self.assertEqual((C + K) % R, 0)
        self.assertEqual(gap, (4 * C + 1) // R)

        u = (K + C) // R
        v = K * u // C
        self.assertEqual((K + C) % R, 0)
        self.assertEqual(K * u % C, 0)
        self.assertEqual(u, A * C)
        self.assertEqual(v, A * C * (A * R - 1))
        self.assertEqual(
            Fraction(4, source),
            Fraction(1, K) + Fraction(1, u) + Fraction(1, v),
        )
        self.assertEqual(
            Fraction(4, prime),
            Fraction(1, prime * K) + Fraction(1, u) + Fraction(1, v),
        )
        return source

    def test_composed_upper_b1_closure_rebuilds_all_tail_misses(self):
        base = json.loads(
            (
                ROOT / "reproductions" / "type-i-tail-reverse-b1-even-source-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        direct_extension = json.loads(
            (
                ROOT / "reproductions" / "type-i-direct-b1-gap-extension-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        pminus_extension = json.loads(
            (
                ROOT / "reproductions" / "type-i-pminusone-miss-upper-b1-gap-extension-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        expected = json.loads(
            (
                ROOT / "reproductions" / "type-i-tail-upper-b1-completion-profile-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        actual = profile.run_profile(base, direct_extension, pminus_extension)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["ordinary_tail_miss_count"],
                actual["direct_upper_B_eq_1_count"],
                actual["lower_source_state_reselected_B_eq_1_count"],
                actual["lower_source_state_direct_gap_extension_count"],
                actual["direct_B_eq_1_gap_extension_count"],
                actual["upper_B_eq_1_closure_count"],
                actual["maximum_selected_B_eq_1_normal_gap"],
            ),
            (1717, 1709, 3, 1, 4, 1717, 5963),
        )
        self.assertEqual(
            [row["prime"] for row in actual["lower_source_state_reselected_records"]],
            [629_689, 58_757_449, 83_445_289],
        )
        self.assertEqual(
            actual["lower_source_state_direct_gap_extension_record"]["prime"], 218_482_009
        )

    def test_completed_closure_has_source_first_B1_coordinates(self):
        base = json.loads(
            (
                ROOT / "reproductions" / "type-i-tail-reverse-b1-even-source-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        completed = json.loads(
            (
                ROOT / "reproductions" / "type-i-tail-upper-b1-completion-profile-500m-results.json"
            ).read_text(encoding="utf-8")
        )

        checked = 0
        source_equals_bridge_factor_count = 0
        external_retraction_count = 0
        even_external_retraction_count = 0

        def record(prime, certificate):
            nonlocal checked
            nonlocal source_equals_bridge_factor_count
            nonlocal external_retraction_count
            nonlocal even_external_retraction_count

            self.assert_source_first_coordinates(prime, certificate)
            source_equals_bridge_factor_count += int(
                certificate["E"] == certificate["source_denominator"]
            )
            external_source = self.external_retraction_source(prime, certificate)
            external_retraction_count += int(external_source is not None)
            even_external_retraction_count += int(
                external_source is not None and external_source % 2 == 0
            )
            checked += 1

        for row in base["records"]:
            prime = int(row["prime"])
            certificate = profile.stored_witness(prime, row["minimum_b1_source_witness"])
            if 2 * int(certificate["source_denominator"]) >= prime + 1:
                record(prime, certificate)

        extra_certificates = [
            *(row["certificate"] for row in completed["lower_source_state_reselected_records"]),
            completed["lower_source_state_direct_gap_extension_record"]["certificate"],
            *(row["certificate"] for row in completed["direct_B_eq_1_gap_extension_records"]),
        ]
        for certificate in extra_certificates:
            prime = int(certificate["source_denominator"]) + int(certificate["source_distance"])
            record(prime, certificate)

        self.assertEqual(checked, completed["upper_B_eq_1_closure_count"])
        self.assertEqual(source_equals_bridge_factor_count, 0)
        self.assertEqual(
            (
                external_retraction_count,
                even_external_retraction_count,
                external_retraction_count - even_external_retraction_count,
                checked - external_retraction_count,
            ),
            (1132, 636, 496, 585),
        )


if __name__ == "__main__":
    unittest.main()
