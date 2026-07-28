import importlib.util
import json
import math
from pathlib import Path
import sys
import unittest

import sympy


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_linear_general_b_obstruction_profile_878089",
    ROOT / "reproductions" / "type_i_linear_general_b_obstruction_profile_878089.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


def direct_linear_source_counts(prime):
    """Recover all linear states by direct odd-shift scanning."""
    counts = {}
    for shift in range(1, (prime - 1) // 2 + 1, 2):
        source = prime - shift
        for bridge in sympy.divisors(source):
            bridge = int(bridge)
            if (bridge - 1) % shift:
                continue
            R = (bridge - 1) // shift
            if R < 3 or R % 4 != 3:
                continue
            a = source // bridge
            if prime != a + shift + a * shift * R:
                raise AssertionError("direct source scan recovered an invalid state")
            counts[R] = counts.get(R, 0) + 1
    return counts


def direct_generated_subgroup(modulus, generators):
    """Independent multiplicative closure oracle for a finite unit group."""
    reached = {1 % modulus}
    pending = [1 % modulus]
    while pending:
        value = pending.pop()
        for generator in generators:
            candidate = value * generator % modulus
            if candidate not in reached:
                reached.add(candidate)
                pending.append(candidate)
    return reached


class TypeILinearGeneralBObstructionProfile878089Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = profile.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-linear-general-b-obstruction-profile-878089.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_complete_run(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["input_sha256"], profile.EXPECTED_INPUT_SHA256)

    def test_all_linear_source_moduli_are_recovered_by_direct_shift_scan(self):
        direct_counts = direct_linear_source_counts(profile.PRIME)
        stored_counts = {
            int(record["R"]): int(record["source_state_count"])
            for record in self.actual["records"]
        }
        self.assertEqual(direct_counts, stored_counts)
        self.assertEqual(sum(direct_counts.values()), 54)
        self.assertEqual(len(direct_counts), 24)

    def test_every_square_spectrum_and_obstruction_class_is_independently_exact(self):
        for record in self.actual["records"]:
            with self.subTest(R=record["R"]):
                R = int(record["R"])
                K = int(record["K"])
                factors = sympy.factorint(K)
                square_divisors = [int(value) for value in sympy.divisors(K * K)]
                centered = {value * pow(K, -1, R) % R for value in square_divisors}
                generated = direct_generated_subgroup(
                    R, {int(prime) % R for prime in factors}
                )
                matches = [value for value in square_divisors if value % R == (-K) % R]
                self.assertEqual(len(square_divisors), record["square_divisor_count"])
                self.assertEqual(
                    len(centered), record["centered_spectrum_residue_count"]
                )
                self.assertEqual(len(generated), record["generated_subgroup_order"])
                self.assertEqual(
                    (R - 1) in centered, record["minus_one_in_centered_spectrum"]
                )
                self.assertEqual(
                    (R - 1) in generated,
                    record["minus_one_in_generated_subgroup"],
                )
                expected_class = (
                    "hit"
                    if matches
                    else "finite_exponent"
                    if (R - 1) in generated
                    else "subgroup_character"
                )
                self.assertEqual(record["classification"], expected_class)
                self.assertEqual(
                    record["least_matching_square_divisor"],
                    min(matches) if matches else None,
                )
                if matches:
                    self.assertLess(min(matches), K)
                    self.assertEqual((K * K // min(matches)) % R, (-K) % R)
                self.assertFalse(
                    any(
                        value % R == (-pow(4, -1, R)) % R for value in sympy.divisors(K)
                    )
                )

    def test_expected_general_B_escape_and_two_finite_exponent_failures(self):
        self.assertEqual(self.actual["B_eq_1_hit_count"], 0)
        self.assertEqual(
            self.actual["general_B_classification_counts"],
            {"finite_exponent": 2, "hit": 1, "subgroup_character": 21},
        )
        self.assertEqual(self.actual["general_B_hit_R"], [59])
        self.assertEqual(self.actual["finite_exponent_failure_R"], [279, 503])
        hit = next(record for record in self.actual["records"] if record["R"] == 59)
        self.assertEqual(hit["least_matching_square_divisor"], 816_781)
        self.assertEqual(hit["K"], 12_951_813)
        self.assertEqual(math.gcd(hit["K"], hit["R"]), 1)


if __name__ == "__main__":
    unittest.main()
