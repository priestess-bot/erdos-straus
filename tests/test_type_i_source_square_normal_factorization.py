import math
import unittest

import sympy


def source_lambda(shift: int) -> int:
    if shift <= 0 or shift % 2 == 0:
        raise ValueError("shift must be a positive odd integer")
    return 4 if shift % 4 == 1 else 2


def canonical_square_parts(value: int, divisor: int) -> tuple[int, int, int]:
    if value <= 0 or divisor <= 0 or value * value % divisor:
        raise ValueError("require positive value and divisor|value^2")
    common = math.gcd(value, divisor)
    beta = divisor // common
    if common % beta:
        raise AssertionError("divisor|value^2 did not imply beta|gcd")
    gamma = common // beta
    alpha = value // common
    if value != alpha * beta * gamma:
        raise AssertionError("source value did not reconstruct")
    if divisor != beta * beta * gamma:
        raise AssertionError("source-square divisor did not reconstruct")
    if math.gcd(alpha, beta) != 1:
        raise AssertionError("canonical alpha and beta are not coprime")
    return alpha, beta, gamma


def all_square_part_decompositions(
    value: int, divisor: int
) -> list[tuple[int, int, int]]:
    decompositions = []
    for beta_value in sympy.divisors(divisor):
        beta = int(beta_value)
        beta_square = beta * beta
        if divisor % beta_square:
            continue
        gamma = divisor // beta_square
        if value % (beta * gamma):
            continue
        alpha = value // (beta * gamma)
        if math.gcd(alpha, beta) == 1:
            decompositions.append((alpha, beta, gamma))
    return decompositions


def normalized_source_state(prime: int, shift: int, divisor: int) -> dict[str, int]:
    if prime % 24 != 1:
        raise ValueError("prime must lie in the core residue class")
    if shift <= 0 or shift % 2 == 0 or shift > (prime - 1) // 2:
        raise ValueError("shift is outside the upper-half positive range")
    lam = source_lambda(shift)
    source = prime - shift
    if source % lam:
        raise AssertionError("lambda does not divide the source")
    reduced_source = source // lam
    if divisor <= 0 or reduced_source * reduced_source % divisor:
        raise ValueError("D must be a positive divisor of u^2")
    bridge_factor = lam * divisor
    if (bridge_factor - 1) % shift:
        raise ValueError("lambda*D misses 1 modulo the shift")
    modulus = (bridge_factor - 1) // shift
    if modulus < 3 or modulus % 4 != 3:
        raise AssertionError("the recovered modulus is not positive and 3 mod 4")
    if math.gcd(source, 4) != lam or math.gcd(bridge_factor, 4) != lam:
        raise AssertionError("lambda does not equal both normalized gcds")

    alpha, beta, gamma = canonical_square_parts(reduced_source, divisor)
    eta = 4 // lam
    affine_numerator = alpha * modulus + beta
    if affine_numerator % eta:
        raise AssertionError("the affine cofactor is not integral")
    affine_cofactor = affine_numerator // eta
    target_product = (prime * modulus + 1) // 4
    if target_product != beta * gamma * affine_cofactor:
        raise AssertionError("K did not factor as beta*gamma*L")
    if source * target_product // bridge_factor != alpha * gamma * affine_cofactor:
        raise AssertionError("nK/E did not match alpha*gamma*L")
    if (
        4 * target_product * target_product // bridge_factor
        != eta * gamma * affine_cofactor * affine_cofactor
    ):
        raise AssertionError("4K^2/E did not match eta*gamma*L^2")
    if bridge_factor >= 2 * target_product:
        raise AssertionError("source state is not in the strict upper half")
    return {
        "prime": prime,
        "shift": shift,
        "source": source,
        "lambda": lam,
        "u": reduced_source,
        "D": divisor,
        "R": modulus,
        "E": bridge_factor,
        "K": target_product,
        "alpha": alpha,
        "beta": beta,
        "gamma": gamma,
        "eta": eta,
        "L": affine_cofactor,
    }


class TypeISourceSquareNormalFactorizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        states = []
        for prime_value in sympy.primerange(2, 5_000):
            prime = int(prime_value)
            if prime % 24 != 1:
                continue
            for shift in range(1, (prime - 1) // 2 + 1, 2):
                lam = source_lambda(shift)
                reduced_source = (prime - shift) // lam
                for divisor_value in sympy.divisors(reduced_source * reduced_source):
                    divisor = int(divisor_value)
                    if (lam * divisor - 1) % shift:
                        continue
                    states.append(normalized_source_state(prime, shift, divisor))
        cls.states = states

    def test_exact_source_enumeration_below_5000(self):
        self.assertEqual(len(self.states), 8_707)
        for state in self.states:
            self.assertEqual(state["lambda"], math.gcd(state["source"], 4))
            self.assertEqual(state["lambda"], math.gcd(state["E"], 4))
            self.assertEqual(state["E"], state["shift"] * state["R"] + 1)
            self.assertEqual(state["E"], state["lambda"] * state["D"])
            self.assertEqual(state["source"], state["lambda"] * state["u"])
            self.assertEqual(state["u"] * state["u"] % state["D"], 0)
            self.assertEqual(
                state["u"], state["alpha"] * state["beta"] * state["gamma"]
            )
            self.assertEqual(state["D"], state["beta"] ** 2 * state["gamma"])
            self.assertEqual(math.gcd(state["alpha"], state["beta"]), 1)
            self.assertEqual(state["K"], state["beta"] * state["gamma"] * state["L"])
            self.assertGreaterEqual(state["R"], 3)
            self.assertEqual(state["R"] % 4, 3)
            self.assertLess(state["E"], 2 * state["K"])

    def test_canonical_decomposition_is_unique(self):
        for state in self.states:
            expected = (
                state["alpha"],
                state["beta"],
                state["gamma"],
            )
            self.assertEqual(
                all_square_part_decompositions(state["u"], state["D"]),
                [expected],
            )
            common = math.gcd(state["u"], state["D"])
            self.assertEqual(state["beta"], state["D"] // common)
            self.assertEqual(common % state["beta"], 0)
            self.assertEqual(state["gamma"], common // state["beta"])

    def test_beta_one_is_exactly_the_linear_source_case(self):
        beta_one_count = 0
        for state in self.states:
            is_linear = state["source"] % state["E"] == 0
            self.assertEqual(is_linear, state["beta"] == 1)
            if not is_linear:
                continue
            beta_one_count += 1
            linear_coefficient = state["source"] // state["E"]
            self.assertEqual(linear_coefficient, state["alpha"])
            self.assertEqual(
                state["prime"],
                linear_coefficient
                + state["shift"]
                + linear_coefficient * state["shift"] * state["R"],
            )
            self.assertEqual(
                state["prime"] * state["R"] + 1,
                (linear_coefficient * state["R"] + 1) * state["E"],
            )
            self.assertEqual(state["D"], state["gamma"])
            self.assertEqual(
                state["K"],
                state["gamma"] * (linear_coefficient * state["R"] + 1) // state["eta"],
            )
        self.assertEqual(beta_one_count, 1_865)

    def test_p97_s57_is_rejected_by_the_upper_half_guard(self):
        prime = 97
        shift = 57
        lam = source_lambda(shift)
        source = prime - shift
        reduced_source = source // lam
        divisor = 100
        modulus = (lam * divisor - 1) // shift
        bridge_factor = lam * divisor
        target_product = (prime * modulus + 1) // 4

        self.assertEqual((lam, source, reduced_source), (4, 40, 10))
        self.assertEqual(
            (divisor, modulus, bridge_factor, target_product),
            (100, 7, 400, 170),
        )
        self.assertEqual(reduced_source * reduced_source % divisor, 0)
        self.assertEqual((lam * divisor - 1) % shift, 0)
        self.assertGreater(shift, (prime - 1) // 2)
        self.assertGreaterEqual(bridge_factor, 2 * target_product)
        with self.assertRaisesRegex(ValueError, "upper-half"):
            normalized_source_state(prime, shift, divisor)

    def test_nonpositive_parameters_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "positive"):
            canonical_square_parts(10, 0)
        with self.assertRaisesRegex(ValueError, "positive"):
            normalized_source_state(97, 1, 0)


if __name__ == "__main__":
    unittest.main()
