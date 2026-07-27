import importlib.util
from fractions import Fraction
import json
import math
from pathlib import Path
import sys
import unittest

import sympy


ROOT = Path(__file__).resolve().parents[1]
HUNDRED_THOUSAND_ARTIFACT = (
    ROOT
    / "reproductions"
    / "type-ii-pure-new-exception-dynamic-selector-100k-h50-results.json"
)
MILLION_COMPACT_ARTIFACT = (
    ROOT
    / "reproductions"
    / "type-ii-pure-new-exception-dynamic-selector-1m-h100-summary.json"
)
TEN_MILLION_COMPACT_ARTIFACT = (
    ROOT
    / "reproductions"
    / "type-ii-pure-new-exception-dynamic-selector-10m-h100-summary.json"
)
SPEC = importlib.util.spec_from_file_location(
    "type_ii_pure_new_exception_dynamic_selector",
    ROOT
    / "reproductions"
    / "type_ii_pure_new_exception_dynamic_selector.py",
)
assert SPEC and SPEC.loader
selector = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = selector
SPEC.loader.exec_module(selector)


def independent_canonical_modulus(shift: int) -> int:
    factors = sympy.factorint(shift)
    square_root = math.prod(
        int(prime) ** (int(exponent) // 2)
        for prime, exponent in factors.items()
    )
    squarefree = shift // (square_root * square_root)
    return 4 * square_root * squarefree


def independent_exception_primes(limit: int, shift_bound: int) -> list[int]:
    exceptions = []
    for prime in sympy.primerange(2, limit + 1):
        prime = int(prime)
        if prime % 24 != 1:
            continue
        old_support = set()
        for shift in range(1, 20):
            old_support.update(int(factor) for factor in sympy.factorint(prime + 4 * shift))
        captured = False
        for shift in range(20, shift_bound + 1):
            modulus = independent_canonical_modulus(shift)
            for factor in sympy.factorint(prime + 4 * shift):
                factor = int(factor)
                if factor % modulus == modulus - 1 and factor not in old_support:
                    captured = True
                    break
            if captured:
                break
        if not captured:
            exceptions.append(prime)
    return exceptions


class TypeIIPureNewExceptionDynamicSelectorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = selector.run_experiment(100_000, 50, 2)

    def test_true_exception_set_matches_independent_definition(self):
        small = selector.run_experiment(5_000, 30, 2)
        self.assertEqual(
            small["pure_new_exception_primes"],
            independent_exception_primes(5_000, 30),
        )
        self.assertEqual(
            small["core_prime_count"],
            small["pure_new_captured_count"] + small["pure_new_exception_count"],
        )

    def test_pure_new_witness_and_direct_certificate_replay(self):
        spf = selector.short_certificate.smallest_prime_factors(313 + 4 * 50)
        witness = selector.pure_new_witness(313, 50, spf)
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(witness["shift"], 25)
        self.assertEqual(witness["new_prime_factor"], 59)
        self.assertEqual(witness["canonical_modulus"], 20)
        self.assertEqual(witness["shifted_integer"] % witness["new_prime_factor"], 0)
        self.assertEqual(
            witness["new_prime_factor"] % witness["canonical_modulus"],
            witness["canonical_modulus"] - 1,
        )
        self.assertNotIn(
            witness["new_prime_factor"], witness["h19_source_prime_support"]
        )
        certificate = selector.short_certificate.GapCertificate(
            **witness["type_ii_certificate"]
        )
        self.assertTrue(selector.short_certificate.verify_certificate(certificate))

    def test_every_stored_dynamic_certificate_replays_exactly(self):
        for record in self.report["records"]:
            prime = record["prime"]
            tail = record["dynamic_low_defect_tail"]
            if tail is not None:
                certificate = selector.short_certificate.GapCertificate(
                    **tail["type_ii_certificate"]
                )
                self.assertTrue(
                    selector.short_certificate.verify_certificate(certificate)
                )
                self.assertEqual(certificate.y % prime, 0)
                self.assertEqual(certificate.z % prime, 0)
                self.assertEqual(
                    tail["support_defect"], len(tail["new_prime_support"])
                )
                self.assertLessEqual(tail["support_defect"], 2)
                self.assertEqual(
                    4 * tail["divisor"] % tail["gap"],
                    -tail["u"] % tail["gap"],
                )
                self.assertEqual(
                    Fraction(4, tail["source_denominator"]),
                    sum(
                        (Fraction(1, value) for value in tail["source_solution"]),
                        Fraction(),
                    ),
                )
                self.assertEqual(
                    Fraction(4, prime),
                    sum(
                        (Fraction(1, value) for value in tail["target_solution"]),
                        Fraction(),
                    ),
                )

            external = record["dynamic_external_source_exit"]
            if external is not None:
                self.assertLess(external["source_denominator"], prime)
                self.assertEqual(
                    external["source_product"],
                    external["scale"] * external["source_denominator"],
                )
                self.assertEqual(
                    external["source_product"] ** 2
                    % external["square_tail_divisor"],
                    0,
                )
                self.assertLessEqual(
                    external["square_tail_divisor"], external["source_product"]
                )
                self.assertEqual(
                    external["square_tail_divisor"]
                    % external["source_modulus"],
                    (-external["source_product"])
                    % external["source_modulus"],
                )
                self.assertEqual(
                    Fraction(4, external["source_denominator"]),
                    sum(
                        (
                            Fraction(1, value)
                            for value in external["source_solution"]
                        ),
                        Fraction(),
                    ),
                )
                self.assertEqual(
                    Fraction(4, prime),
                    sum(
                        (
                            Fraction(1, value)
                            for value in external["target_solution"]
                        ),
                        Fraction(),
                    ),
                )

    def test_complete_external_search_matches_independent_small_exhaustion(self):
        spf = selector.short_certificate.smallest_prime_factors(2_000)
        for prime in sympy.primerange(2, 2_000):
            prime = int(prime)
            if prime % 24 != 1:
                continue
            base = (prime - 1) // 4
            expected = None
            for scale in sympy.divisors(base):
                scale = int(scale)
                modulus = 4 * scale - 1
                source = (modulus * prime + 1) // (4 * scale)
                source_product = scale * source
                candidates = [
                    int(divisor)
                    for divisor in sympy.divisors(source_product * source_product)
                    if divisor <= source_product
                    and divisor % modulus == (-source_product) % modulus
                ]
                if candidates:
                    expected = (scale, min(candidates))
                    break
            witness = selector.dynamic_external_source_exit(prime, spf)
            actual = (
                None
                if witness is None
                else (witness["scale"], witness["square_tail_divisor"])
            )
            self.assertEqual(actual, expected)

    def test_67369_stores_full_square_tail_and_has_narrow_alternative(self):
        record = next(
            record for record in self.report["records"] if record["prime"] == 67_369
        )
        self.assertIsNone(record["dynamic_low_defect_tail"])
        self.assertEqual(record["availability_class"], "external-only")
        self.assertEqual(record["selected_branch"], "dynamic-external-source-exit")
        external = record["dynamic_external_source_exit"]
        self.assertEqual(external["scale"], 6)
        self.assertEqual(external["source_modulus"], 23)
        self.assertEqual(external["source_product"], 387_372)
        self.assertEqual(external["square_tail_divisor"], 684)

        source = external["source_denominator"]
        source_product = external["source_product"]
        modulus = external["source_modulus"]
        alternative = 3_398
        self.assertEqual(source % alternative, 0)
        self.assertEqual(source_product % alternative, 0)
        self.assertEqual(alternative % modulus, (-source_product) % modulus)
        first_tail = (source_product + alternative) // modulus
        second_tail = source_product * first_tail // alternative
        self.assertEqual((first_tail, second_tail), (16_990, 1_936_860))
        self.assertEqual(
            Fraction(4, source),
            sum(
                (
                    Fraction(1, value)
                    for value in (source_product, first_tail, second_tail)
                ),
                Fraction(),
            ),
        )
        self.assertEqual(
            Fraction(4, 67_369),
            sum(
                (
                    Fraction(1, value)
                    for value in (
                        source_product * 67_369,
                        first_tail,
                        second_tail,
                    )
                ),
                Fraction(),
            ),
        )

    def test_branch_partition_and_coverage_statistics(self):
        report = self.report
        self.assertEqual(report["core_prime_count"], 1_181)
        self.assertEqual(report["pure_new_exception_count"], 477)
        self.assertEqual(
            report["availability_counts"],
            {"both": 469, "tail-only": 7, "external-only": 1, "neither": 0},
        )
        self.assertEqual(
            report["selected_branch_counts"],
            {
                "dynamic-low-defect-tail": 476,
                "dynamic-external-source-exit": 1,
                "unresolved": 0,
            },
        )
        self.assertEqual(
            report["minimum_tail_support_defect_histogram"],
            {"0": 456, "1": 20, "2": 0},
        )
        self.assertEqual(report["selector_union_covered_count"], 477)
        self.assertEqual(report["selector_union_unresolved_primes"], [])
        availability = [record["availability_class"] for record in report["records"]]
        selected = [record["selected_branch"] for record in report["records"]]
        self.assertEqual(len(availability), sum(report["availability_counts"].values()))
        self.assertEqual(len(selected), sum(report["selected_branch_counts"].values()))
        for record in report["records"]:
            expected_availability = selector.availability_class(
                record["dynamic_low_defect_tail"],
                record["dynamic_external_source_exit"],
            )
            expected_selection = selector.selected_branch(
                record["dynamic_low_defect_tail"],
                record["dynamic_external_source_exit"],
            )
            self.assertEqual(record["availability_class"], expected_availability)
            self.assertEqual(record["selected_branch"], expected_selection)

    def test_checked_artifact_matches_the_deterministic_run(self):
        payload = json.loads(HUNDRED_THOUSAND_ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(payload, self.report)

    def test_million_range_compact_artifact_matches_deterministic_run(self):
        report = selector.run_experiment(1_000_000, 100, 2)
        compact = selector.compact_report(report)
        artifact = json.loads(MILLION_COMPACT_ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(compact, artifact)
        self.assertEqual(report["pure_new_exception_count"], 1_285)
        self.assertEqual(report["selector_union_unresolved_count"], 0)

    def test_ten_million_range_compact_artifact_matches_deterministic_run(self):
        report = selector.run_experiment(10_000_000, 100, 2)
        compact = selector.compact_report(report)
        artifact = json.loads(TEN_MILLION_COMPACT_ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(compact, artifact)
        self.assertEqual(report["pure_new_exception_count"], 7_056)
        self.assertEqual(report["selector_union_unresolved_count"], 0)
        self.assertEqual(compact["selected_tail_scale_summary"]["maximum"], 714)


if __name__ == "__main__":
    unittest.main()
