import importlib.util
import json
import math
from pathlib import Path
import sys
import unittest

import sympy


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_finite_exponent_dilation_boundary_297640249",
    ROOT / "reproductions" / "type_i_finite_exponent_dilation_boundary_297640249.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


def independent_centered_half_residues(factors, modulus, dilation):
    """Build a half-box directly without the production membership helper."""
    residues = {1}
    for prime, exponent in factors:
        powers = [
            pow(prime, coordinate, modulus)
            for coordinate in range(-dilation * exponent, dilation * exponent + 1)
        ]
        residues = {left * right % modulus for left in residues for right in powers}
    return residues


def independent_target_in_dilated_spectrum(factors, modulus, dilation):
    """Decide target membership using a separately written 2-by-3 MITM oracle."""
    left = independent_centered_half_residues(factors[:2], modulus, dilation)
    right = independent_centered_half_residues(factors[2:], modulus, dilation)
    return any(
        (modulus - 1) * pow(residue, -1, modulus) % modulus in right for residue in left
    )


class TypeIFiniteExponentDilationBoundary297640249Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = profile.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-finite-exponent-dilation-boundary-297640249-results.json"
            ).read_text(encoding="utf-8")
        )
        cls.factors = [
            (int(item["prime"]), int(item["exponent"]))
            for item in cls.actual["K_factorization"]
        ]

    def test_checked_artifact_matches_complete_run(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["input_sha256"], profile.EXPECTED_INPUT_SHA256)

    def test_input_state_is_the_frozen_finite_exponent_obstruction(self):
        self.assertEqual(self.actual["prime"], profile.PRIME)
        self.assertEqual(self.actual["R"], profile.MODULUS)
        self.assertEqual(
            self.actual["K"],
            (profile.PRIME * profile.MODULUS + 1) // 4,
        )
        self.assertEqual(
            self.actual["K"],
            math.prod(prime**exponent for prime, exponent in self.factors),
        )
        self.assertEqual(
            self.factors,
            [
                (int(prime), int(exponent))
                for prime, exponent in sympy.factorint(self.actual["K"]).items()
            ],
        )
        self.assertEqual(self.actual["original_classification"], "finite_exponent")

    def test_independent_mitm_oracle_proves_first_entrance_at_fifty(self):
        for dilation in range(1, 50):
            with self.subTest(dilation=dilation):
                self.assertFalse(
                    independent_target_in_dilated_spectrum(
                        self.factors,
                        profile.MODULUS,
                        dilation,
                    )
                )
        self.assertTrue(
            independent_target_in_dilated_spectrum(
                self.factors,
                profile.MODULUS,
                50,
            )
        )

    def test_stored_centered_witness_has_exact_bounds_and_target_residue(self):
        dilation = int(self.actual["first_target_dilation"])
        vector = [int(value) for value in self.actual["centered_exponent_witness"]]
        self.assertEqual(dilation, 50)
        self.assertEqual(len(vector), len(self.factors))
        self.assertEqual(
            profile.centered_residue(self.factors, vector, profile.MODULUS),
            profile.MODULUS - 1,
        )
        self.assertTrue(
            all(
                abs(value) <= dilation * exponent
                for value, (_, exponent) in zip(vector, self.factors)
            )
        )
        self.assertEqual(
            self.actual["positive_exponent_vector_in_K_to_2c"],
            [
                dilation * exponent + value
                for value, (_, exponent) in zip(vector, self.factors)
            ],
        )


if __name__ == "__main__":
    unittest.main()
