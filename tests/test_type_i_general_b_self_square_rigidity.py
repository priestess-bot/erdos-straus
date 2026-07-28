import math
import unittest


def natural_self_square_factor(A: int, B: int, C: int, gap: int, R: int) -> dict[str, int | bool]:
    """Reconstruct the natural general-B square-residue factor from one normal form."""
    if (
        A <= 0
        or B <= 0
        or C <= 0
        or gap * R != 4 * B * B * C + 1
        or math.gcd(A, B) != 1
    ):
        raise ValueError("inputs are not a coprime Type I normal form")
    H = A * R - B
    K = B * C * H
    prime = 4 * A * B * C - gap
    E = 16 * B**4 * C**2
    return {
        "prime": prime,
        "H": H,
        "K": K,
        "E": E,
        "residue_one": E % R == 1,
        "divides_target_square": (4 * K * K) % E == 0,
    }


class TypeIGeneralBSelfSquareRigidityTests(unittest.TestCase):
    def test_b_one_is_exactly_the_divisibility_case(self):
        witness = natural_self_square_factor(17, 1, 5, 3, 7)
        self.assertEqual(witness, {
            "prime": 337,
            "H": 118,
            "K": 590,
            "E": 400,
            "residue_one": True,
            "divides_target_square": True,
        })

    def test_general_b_counterexample_fails_at_the_square_divisibility_gate(self):
        witness = natural_self_square_factor(74, 3, 76, 119, 23)
        self.assertEqual(witness["prime"], 67369)
        self.assertEqual(witness["H"], 1699)
        self.assertEqual(witness["K"], 387372)
        self.assertTrue(bool(witness["residue_one"]))
        self.assertFalse(bool(witness["divides_target_square"]))


if __name__ == "__main__":
    unittest.main()
