import importlib.util
import math
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("short_certificate", ROOT / "reproductions" / "short_certificate.py")
assert SPEC and SPEC.loader
short_certificate = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = short_certificate
SPEC.loader.exec_module(short_certificate)


class ShortCertificateTests(unittest.TestCase):
    def test_known_gap_certificate(self):
        spf = short_certificate.smallest_prime_factors(100)
        certificate = short_certificate.shortest_gap_certificate(73, 100, spf)
        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertTrue(short_certificate.verify_certificate(certificate))

    def test_gap_is_rejected_outside_bradford_range(self):
        spf = short_certificate.smallest_prime_factors(100)
        self.assertIsNone(short_certificate.certificate_at_gap(73, 1, spf))
        self.assertIsNone(short_certificate.certificate_at_gap(73, 5, spf))
        self.assertIsNone(short_certificate.certificate_at_gap(73, 75, spf))

    def test_type_ii_two_tail_deflation(self):
        limit = 100_000
        spf = short_certificate.smallest_prime_factors(limit)
        witnesses = short_certificate.type_ii_tail_deflation_scan(73, spf)
        self.assertTrue(witnesses)
        for witness in witnesses:
            self.assertLess(witness.source_denominator, witness.prime)
            self.assertEqual(witness.target_solution[1] % witness.prime, 0)
            self.assertEqual(witness.target_solution[2] % witness.prime, 0)
            self.assertEqual(
                short_certificate.Fraction(4, witness.source_denominator),
                sum(
                    (
                        short_certificate.Fraction(1, denominator)
                        for denominator in witness.source_solution
                    ),
                    short_certificate.Fraction(),
                ),
            )
            self.assertEqual(
                tuple(
                    denominator * witness.prime
                    if index in (1, 2)
                    else denominator
                    for index, denominator in enumerate(witness.source_solution)
                ),
                witness.target_solution,
            )

    def test_type_ii_two_tail_deflation_uses_only_p_minus_one_divisors(self):
        limit = 10_000
        spf = short_certificate.smallest_prime_factors(limit)
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            for witness in short_certificate.type_ii_tail_deflation_scan(prime, spf):
                self.assertEqual((prime - 1) % (witness.gap + 1), 0)
                self.assertEqual(witness.gap % 4, 3)

    def test_gap_three_factor_criterion(self):
        limit = 100_000
        spf = short_certificate.smallest_prime_factors((limit + 3) // 4 + 1)
        self.assertFalse(short_certificate.gap_three_criterion(73, spf))
        self.assertTrue(short_certificate.gap_three_criterion(97, spf))
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 == 1:
                self.assertEqual(
                    short_certificate.certificate_at_gap(prime, 3, spf) is not None,
                    short_certificate.gap_three_criterion(prime, spf),
                    prime,
                )

    def test_gap_three_two_denominator_lift_obstruction(self):
        # The formula is intentionally evaluated without a primality guard so
        # this composite example checks the candidate algebra itself.
        self.assertEqual(
            short_certificate.gap_three_two_denominator_lift_candidate(4_225, 350),
            51_038,
        )

        # For prime p=24t+1, positivity confines a replaced denominator to
        # 1..2t; the theorem proves no integral target denominator exists.
        limit = 100_000
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            t = (prime - 1) // 24
            for source_denominator in range(1, 2 * t + 1):
                self.assertIsNone(
                    short_certificate.gap_three_two_denominator_lift_candidate(
                        prime, source_denominator
                    ),
                    (prime, source_denominator),
                )

    def test_three_mod_four_standard_source_lift_obstruction(self):
        # Every n == 3 (mod 4) has the standard source solution
        # 4/n = 1/((n+1)/4) + 2/(n(n+1)/2).  Both distinct coordinates
        # fail as the replaced term, so every two-denominator-preserving
        # one-term lift from this standard source is ruled out.
        for prime in short_certificate.primes_up_to(10_000):
            if prime % 24 != 1:
                continue
            for source in range(3, prime, 4):
                first = (source + 1) // 4
                repeated = source * (source + 1) // 2
                self.assertEqual(
                    short_certificate.Fraction(4, source),
                    short_certificate.Fraction(1, first)
                    + 2 * short_certificate.Fraction(1, repeated),
                )
                for replaced in (first, repeated):
                    self.assertIsNone(
                        short_certificate.three_mod_four_standard_source_lift_candidate(
                            prime, source, replaced
                        ),
                        (prime, source, replaced),
                    )

    def test_three_mod_four_nonstandard_source_lift_obstruction(self):
        # Subramanian's nonstandard source has the square tail
        # (a,b,n*b), not the repeated standard tail. Each one-coordinate
        # lift is nevertheless obstructed for a core target.
        for prime in short_certificate.primes_up_to(10_000):
            if prime % 24 != 1:
                continue
            for source in range(3, prime, 4):
                first = (source + 1) // 4
                middle = (source + 1) ** 2 // 4
                last = source * middle
                self.assertEqual(
                    short_certificate.Fraction(4, source),
                    short_certificate.Fraction(1, first)
                    + short_certificate.Fraction(1, middle)
                    + short_certificate.Fraction(1, last),
                )
                for replaced in (first, middle, last):
                    self.assertIsNone(
                        short_certificate.two_denominator_lift_candidate(
                            prime, source, replaced
                        ),
                        (prime, source, replaced),
                    )

    def test_five_mod_eight_nonstandard_source_lift_obstruction(self):
        # The 5 mod 8 source is distinct from the 3 mod 4 square tail.
        # All three one-coordinate lifts fail for a core target.
        for prime in short_certificate.primes_up_to(10_000):
            if prime % 24 != 1:
                continue
            for source in range(5, prime, 8):
                first = (source + 3) // 4
                middle = source * (source + 3) // 8
                last = 2 * middle
                self.assertEqual(
                    short_certificate.Fraction(4, source),
                    short_certificate.Fraction(1, first)
                    + short_certificate.Fraction(1, middle)
                    + short_certificate.Fraction(1, last),
                )
                for replaced in (first, middle, last):
                    self.assertIsNone(
                        short_certificate.two_denominator_lift_candidate(
                            prime, source, replaced
                        ),
                        (prime, source, replaced),
                    )

    def test_four_divisible_nonstandard_source_lift_obstruction(self):
        # Subramanian's 4-divisible source uses a nonstandard square tail.
        # It is distinct from the usual even repeated tail (n/2,n,n).
        for prime in short_certificate.primes_up_to(10_000):
            if prime % 24 != 1:
                continue
            for source in range(4, prime, 4):
                t = source // 4
                first = t + 1
                middle = (t + 1) ** 2
                last = t * middle
                self.assertEqual(
                    short_certificate.Fraction(4, source),
                    short_certificate.Fraction(1, first)
                    + short_certificate.Fraction(1, middle)
                    + short_certificate.Fraction(1, last),
                )
                for replaced in (first, middle, last):
                    self.assertIsNone(
                        short_certificate.two_denominator_lift_candidate(
                            prime, source, replaced
                        ),
                        (prime, source, replaced),
                    )

    def test_three_divisible_standard_source_lift_obstruction(self):
        # Every multiple of three has the standard source solution
        # 4/n = 1/(n/3) + 2/(2n). Both possible replacement coordinates
        # are ruled out, not only the repeated large denominator.
        for prime in short_certificate.primes_up_to(10_000):
            if prime % 24 != 1:
                continue
            for source in range(3, prime, 3):
                first = source // 3
                repeated = 2 * source
                self.assertEqual(
                    short_certificate.Fraction(4, source),
                    short_certificate.Fraction(1, first)
                    + 2 * short_certificate.Fraction(1, repeated),
                )
                for replaced in (first, repeated):
                    self.assertIsNone(
                        short_certificate.three_divisible_standard_source_lift_candidate(
                            prime, source, replaced
                        ),
                        (prime, source, replaced),
                    )

    def test_two_denominator_lift_criterion(self):
        # A different natural source gap can genuinely lift while retaining
        # two denominators: 4/33 = 1/15 + 1/22 + 1/110.
        lifted = short_certificate.two_denominator_lift_candidate(73, 33, 15)
        self.assertEqual(lifted, 4_015)
        assert lifted is not None
        self.assertEqual(
            short_certificate.Fraction(4, 33),
            short_certificate.Fraction(1, 15)
            + short_certificate.Fraction(1, 22)
            + short_certificate.Fraction(1, 110),
        )
        self.assertEqual(
            short_certificate.Fraction(4, 73),
            short_certificate.Fraction(1, lifted)
            + short_certificate.Fraction(1, 22)
            + short_certificate.Fraction(1, 110),
        )
        self.assertIsNone(short_certificate.two_denominator_lift_candidate(33, 73, 15))
        self.assertIsNone(short_certificate.two_denominator_lift_candidate(73, 33, 16))
        spf = short_certificate.smallest_prime_factors(10_000)
        source_solutions: set[tuple[int, int, int]] = set()
        for first in range((33 + 3) // 4, 33 // 2 + 1):
            for second, third in short_certificate.two_term_unit_fraction_pairs(
                4 * first - 33, 33 * first, spf
            ):
                if first <= second <= third:
                    source_solutions.add((first, second, third))
        self.assertEqual(len(source_solutions), 29)
        liftable = [
            triple
            for triple in source_solutions
            if any(
                short_certificate.two_denominator_lift_candidate(73, 33, coordinate)
                is not None
                for coordinate in triple
            )
        ]
        self.assertEqual(sorted(liftable), [(15, 20, 220), (15, 22, 110)])

    def test_even_predecessor_standard_source_lift_obstruction(self):
        # For every odd r, n=p-r is even and 4/n has the explicit source
        # (n/2, n, n). The theorem rules out both distinct replacement
        # coordinates, for every such r rather than a bounded window.
        for prime in short_certificate.primes_up_to(5_000):
            if prime % 24 != 1:
                continue
            for distance in range(1, prime - 1, 2):
                source = prime - distance
                self.assertEqual(source % 2, 0)
                self.assertEqual(
                    short_certificate.Fraction(4, source),
                    short_certificate.Fraction(1, source // 2)
                    + short_certificate.Fraction(1, source)
                    + short_certificate.Fraction(1, source),
                )
                for replaced in (source // 2, source):
                    self.assertIsNone(
                        short_certificate.two_denominator_lift_candidate(
                            prime, source, replaced
                        ),
                        (prime, distance, replaced),
                    )

    def test_gap_three_fab_translation_parity_obstruction(self):
        limit = 100_000
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            t = (prime - 1) // 24
            product = short_certificate.gap_three_fab_translation_product(prime)
            if t % 2:
                self.assertIsNone(product, (prime, t))
            else:
                self.assertEqual(product, 9 * t // 2, (prime, t))

    def test_one_denominator_lift_factor_criterion(self):
        # 4/25 = 1/10 + 1/17 + 1/850. Retaining 850 and using e=125
        # produces a target solution for p=97 while changing both other terms.
        lifted_pair = short_certificate.one_denominator_lift(97, 850, 125)
        self.assertEqual(lifted_pair, (25, 16_490))
        assert lifted_pair is not None
        self.assertEqual(
            short_certificate.Fraction(4, 25),
            short_certificate.Fraction(1, 10)
            + short_certificate.Fraction(1, 17)
            + short_certificate.Fraction(1, 850),
        )
        self.assertEqual(
            short_certificate.Fraction(4, 97),
            short_certificate.Fraction(1, lifted_pair[0])
            + short_certificate.Fraction(1, lifted_pair[1])
            + short_certificate.Fraction(1, 850),
        )
        self.assertIsNone(short_certificate.one_denominator_lift(97, 850, 1))
        self.assertIsNone(short_certificate.one_denominator_lift(97, 24, 1))
        self.assertEqual(
            short_certificate.coprime_one_denominator_lift(97, 850, 125),
            lifted_pair,
        )
        self.assertIsNone(
            short_certificate.coprime_one_denominator_lift(97, 24, 1)
        )

        # For gcd(R,S)=1, a factor e congruent to -S modulo R forces the
        # complementary factor S^2/e into the same residue class. The
        # standard even and three-divisible preserved denominators are all
        # covered by this finite exhaustive check.
        spf_small = short_certificate.smallest_prime_factors(2_000)
        for prime in short_certificate.primes_up_to(1_000):
            if prime % 24 != 1:
                continue
            preserved_values = {
                n
                for n in range(prime // 2 + 1, prime)
                if n % 2 == 0
            }
            preserved_values.update(
                2 * n
                for n in range(prime // 2 + 1, prime)
                if n % 3 == 0
            )
            for preserved in preserved_values:
                remainder = 4 * preserved - prime
                product = prime * preserved
                self.assertEqual(math.gcd(remainder, product), 1)
                for factor in short_certificate.positive_divisors_square_product_from_spf(
                    prime, preserved, spf_small
                ):
                    if factor > product:
                        continue
                    companion = product * product // factor
                    one_congruence = (product + factor) % remainder == 0
                    two_congruences = one_congruence and (
                        (product + companion) % remainder == 0
                    )
                    self.assertEqual(
                        one_congruence,
                        two_congruences,
                        (prime, preserved, factor),
                    )
                    self.assertEqual(
                        short_certificate.coprime_one_denominator_lift(
                            prime, preserved, factor
                        ),
                        short_certificate.one_denominator_lift(
                            prime, preserved, factor
                        ),
                        (prime, preserved, factor),
                    )

        # The natural m=3 source for p=73 has 11 sorted solutions. None of
        # their 21 distinct denominators survives as a one-coordinate lift.
        p = 73
        n = (p + 3) // 4
        spf = short_certificate.smallest_prime_factors(1_000_000)
        source_solutions: set[tuple[int, int, int]] = set()
        for first in range((n + 3) // 4, 3 * n // 4 + 1):
            for second, third in short_certificate.two_term_unit_fraction_pairs(
                4 * first - n, n * first, spf
            ):
                if first <= second <= third:
                    source_solutions.add((first, second, third))
        self.assertEqual(len(source_solutions), 11)
        source_denominators = {item for triple in source_solutions for item in triple}
        self.assertEqual(len(source_denominators), 21)
        for preserved in source_denominators:
            self.assertEqual(
                short_certificate.two_term_unit_fraction_pairs(
                    4 * preserved - p, p * preserved, spf
                ),
                [],
                preserved,
            )

    def test_medium_three_divisible_tail_is_identical_to_even_tail(self):
        # For p/4 < n < p/2, retaining 2n from the standard 3|n source
        # has exactly the same R, S, factor scan, and target as retaining
        # the even-standard source denominator N=2n.
        limit = 5_000
        spf = short_certificate.smallest_prime_factors(limit + 1)
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            first_source = prime // 4 + 1
            first_source += (-first_source) % 3
            for source in range(first_source, (prime + 1) // 2, 3):
                retained = 2 * source
                remainder = 8 * source - prime
                product = 2 * source * prime
                self.assertEqual(remainder, 4 * retained - prime)
                self.assertEqual(product, retained * prime)
                self.assertEqual(math.gcd(remainder, product), 1)

                medium_factor = None
                medium_target = None
                for factor in short_certificate.positive_divisors_square_factors_from_spf(
                    (2, prime, source), spf
                ):
                    if factor > product or (product + factor) % remainder:
                        continue
                    tail = short_certificate.coprime_one_denominator_lift(
                        prime, retained, factor
                    )
                    self.assertIsNotNone(tail, (prime, source, factor))
                    assert tail is not None
                    gap = 4 * min(retained, *tail) - prime
                    if 3 <= gap <= prime - 2 and gap % 4 == 3:
                        medium_factor = factor
                        medium_target = (retained, *tail)
                        break

                even_witness = short_certificate.even_standard_two_tail_descent_witness(
                    prime, retained, spf
                )
                self.assertEqual(
                    medium_factor is not None,
                    even_witness is not None,
                    (prime, source),
                )
                if even_witness is not None:
                    self.assertEqual(even_witness.factor, medium_factor)
                    self.assertEqual(even_witness.target_solution, medium_target)
                    self.assertEqual(even_witness.source_denominator, retained)

    def test_standard_tail_windows_are_type_i_certificate_windows(self):
        # A Type I certificate whose reconstructed y falls in either
        # standard-tail window reconstructs the same one-denominator tail.
        limit = 5_000
        spf = short_certificate.smallest_prime_factors(limit + 1)
        checked = {"even": 0, "three": 0}
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            for gap in range(3, prime - 1, 4):
                first = (prime + gap) // 4
                for divisor in short_certificate.divisors_of_square(first, spf):
                    if (prime * first + divisor) % gap:
                        continue
                    second = (prime * first + divisor) // gap
                    numerator = prime * (
                        first + prime * first * first // divisor
                    )
                    if numerator % gap:
                        continue
                    third = numerator // gap
                    certificate = short_certificate.GapCertificate(
                        prime, "I", gap, first, divisor, second, third
                    )
                    if not short_certificate.verify_certificate(certificate):
                        continue
                    kind = None
                    source = None
                    if second % 2 == 0 and prime / 2 < second < prime:
                        kind, source = "even", second
                    elif second % 6 == 0 and prime < second < 2 * prime:
                        kind, source = "three", second // 2
                    if kind is None:
                        continue

                    remainder = 4 * second - prime
                    product = prime * second
                    self.assertEqual(
                        divisor,
                        remainder * first - product,
                        (kind, prime, gap, divisor),
                    )
                    self.assertEqual(
                        short_certificate.coprime_one_denominator_lift(
                            prime, second, divisor
                        ),
                        (first, third),
                        (kind, prime, gap, divisor),
                    )
                    if kind == "even":
                        self.assertEqual(
                            short_certificate.Fraction(4, source),
                            short_certificate.Fraction(1, source // 2)
                            + 2 * short_certificate.Fraction(1, source),
                        )
                    else:
                        self.assertEqual(
                            short_certificate.Fraction(4, source),
                            short_certificate.Fraction(1, source // 3)
                            + 2 * short_certificate.Fraction(1, 2 * source),
                        )
                    checked[kind] += 1
        self.assertGreater(checked["even"], 0)
        self.assertGreater(checked["three"], 0)

    def test_linear_ratio_ansatz_translates_to_type_i_certificates(self):
        # Bado's main linear-ratio examples have m=a, x=(p+a)/4 and
        # d=r*x/s; the Type I reconstruction must be the displayed triple.
        examples = (
            (1_009, 3, 1, 11, (253, 85_100, 944_524_900)),
            (2_521, 23, 4, 3, (636, 69_748, 131_876_031)),
        )
        for prime, gap, ratio_numerator, ratio_denominator, expected in examples:
            first = (prime + gap) // 4
            divisor = ratio_numerator * first // ratio_denominator
            second = first * (prime * ratio_denominator + ratio_numerator) // (
                gap * ratio_denominator
            )
            third = (
                prime
                * first
                * (prime * ratio_denominator + ratio_numerator)
                // (gap * ratio_numerator)
            )
            certificate = short_certificate.GapCertificate(
                prime, "I", gap, first, divisor, second, third
            )
            self.assertEqual((first, second, third), expected)
            self.assertTrue(short_certificate.verify_certificate(certificate))
            self.assertEqual(
                short_certificate.Fraction(4, prime),
                sum(
                    (short_certificate.Fraction(1, value) for value in expected),
                    short_certificate.Fraction(),
                ),
            )

    def test_greedy_first_step_for_73_has_no_two_term_terminal(self):
        # The first greedy denominator for 4/73 is 19, leaving 3/(73*19).
        # Its two-term factor criterion needs a divisor congruent to 2 mod 3,
        # but every divisor of (19*73)^2 is 1 mod 3.
        p = 73
        first = (p + 3) // 4
        residual_numerator = 4 * first - p
        residual_denominator = p * first
        self.assertEqual((first, residual_numerator, residual_denominator), (19, 3, 1_387))
        spf = short_certificate.smallest_prime_factors(residual_denominator)
        self.assertEqual(
            short_certificate.two_term_unit_fraction_pairs(
                residual_numerator, residual_denominator, spf
            ),
            [],
        )
        self.assertTrue(
            all(
                divisor % residual_numerator == 1
                for divisor in short_certificate.divisors_of_square(
                    residual_denominator, spf
                )
            )
        )

    def test_audige_divisor_lattice_local_completion_is_a_restricted_solution(self):
        # For n=10, the source's displayed local completion is exact. More
        # generally, a completion d+e+f=4*L/n is precisely a three-unit
        # solution whose denominators divide L=lcm(1,...,n), not an automatic
        # consequence of integrality of 4*L/n.
        n = 10
        lcm = math.lcm(*range(1, n + 1))
        target = 4 * lcm // n
        divisors = {value for value in range(1, lcm + 1) if lcm % value == 0}
        completions = {
            divisor: [
                (other, target - divisor - other)
                for other in divisors
                if target - divisor - other in divisors
            ]
            for divisor in divisors
        }
        feasible = {divisor for divisor, pairs in completions.items() if pairs}

        self.assertEqual((lcm, target, max(feasible)), (2_520, 1_008, 840))
        self.assertIn((140, 28), completions[840])
        first, second, third = (lcm // value for value in (840, 140, 28))
        self.assertEqual((first, second, third), (3, 18, 90))
        self.assertEqual(
            short_certificate.Fraction(4, n),
            sum(
                (short_certificate.Fraction(1, value) for value in (first, second, third)),
                short_certificate.Fraction(),
            ),
        )

    def test_middle_coordinate_lift_matches_a_direct_gap_certificate(self):
        # The lift 4/44 = 1/22 + 1/44 + 1/44 -> 4/73 retains 22.
        # Since 73/4 < 22 < 73/2, 22 must be the target's first
        # denominator and its gap m=15 has a direct certificate.
        p = 73
        c = 22
        pair = short_certificate.one_denominator_lift(p, c, 58_619)
        self.assertEqual(pair, (110, 4_015))
        assert pair is not None
        self.assertEqual(
            short_certificate.Fraction(4, 2 * c),
            short_certificate.Fraction(1, c)
            + short_certificate.Fraction(1, 2 * c)
            + short_certificate.Fraction(1, 2 * c),
        )
        self.assertLess(p / 4, c)
        self.assertLess(c, p / 2)
        self.assertEqual(
            short_certificate.Fraction(4, p),
            short_certificate.Fraction(1, c)
            + short_certificate.Fraction(1, pair[0])
            + short_certificate.Fraction(1, pair[1]),
        )
        spf = short_certificate.smallest_prime_factors(100)
        certificate = short_certificate.certificate_at_gap(p, 4 * c - p, spf)
        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertEqual(certificate.x, c)

    def test_boundary_divisor_classification(self):
        limit = 10_000
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            for gap in range(3, prime - 1, 4):
                x = (prime + gap) // 4
                self.assertEqual(
                    (prime * x + x) % gap == 0,
                    (prime + 1) % gap == 0,
                    (prime, gap, "I", "x"),
                )
                self.assertEqual(
                    (x + 1) % gap == 0,
                    (prime + 4) % gap == 0,
                    (prime, gap, "II", "1"),
                )
                self.assertNotEqual((prime * x + 1) % gap, 0, (prime, gap, "I", "1"))
                self.assertNotEqual(
                    (prime * x + x * x) % gap, 0, (prime, gap, "I", "x^2")
                )
                self.assertNotEqual((x + x) % gap, 0, (prime, gap, "II", "x"))
                self.assertIsNone(
                    short_certificate.type_i_normal_form(prime, gap, 1),
                    (prime, gap, "normal-form d=1"),
                )

    def test_residue_reachability_matches_direct_search(self):
        limit = 10_000
        spf = short_certificate.smallest_prime_factors((limit + 107) // 4 + 1)
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            for gap in range(3, min(107, prime - 2) + 1, 4):
                direct = short_certificate.certificate_at_gap(prime, gap, spf)
                via_residues = short_certificate.type_i_residue_certificate(
                    prime, gap, spf
                ) or short_certificate.type_ii_residue_certificate(prime, gap, spf)
                self.assertEqual(direct is not None, via_residues is not None, (prime, gap))

    def test_p_plus_one_type_i_family(self):
        limit = 100_000
        spf = short_certificate.smallest_prime_factors((limit + 1) // 2 + 1)
        self.assertIsNone(short_certificate.p_plus_one_type_i_certificate(73, spf))
        certificate = short_certificate.p_plus_one_type_i_certificate(97, spf)
        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertEqual(certificate.gap, 7)
        self.assertTrue(short_certificate.verify_certificate(certificate))
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 == 1:
                certificate = short_certificate.p_plus_one_type_i_certificate(prime, spf)
                if certificate is not None:
                    self.assertTrue(short_certificate.verify_certificate(certificate), prime)
                    self.assertLessEqual(certificate.gap * certificate.gap, (prime + 1) // 2)

    def test_p_plus_two_external_source_family(self):
        limit = 100_000
        spf = short_certificate.smallest_prime_factors(limit + 2)
        certificate = short_certificate.p_plus_two_type_i_certificate(73, spf)
        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertEqual((certificate.gap, certificate.x, certificate.divisor), (15, 22, 44))
        self.assertTrue(short_certificate.verify_certificate(certificate))
        self.assertIsNone(short_certificate.p_plus_two_type_i_certificate(97, spf))

        # The first five-branch residual has a simple source-i=2 certificate.
        certificate = short_certificate.p_plus_two_type_i_certificate(2_521, spf)
        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertEqual((certificate.gap, certificate.x, certificate.divisor), (87, 652, 1_304))
        self.assertTrue(short_certificate.verify_certificate(certificate))

        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            value = prime + 2
            prime_residues: list[int] = []
            while value > 1:
                factor = spf[value]
                prime_residues.append(factor % 8)
                while value % factor == 0:
                    value //= factor
            certificate = short_certificate.p_plus_two_type_i_certificate(prime, spf)
            self.assertEqual(
                certificate is None,
                all(residue in (1, 3) for residue in prime_residues),
                prime,
            )
            if certificate is not None:
                self.assertEqual(certificate.divisor, 2 * certificate.x)
                self.assertTrue(short_certificate.verify_certificate(certificate), prime)

    def test_p_plus_six_external_source_family_and_exact_failure_classes(self):
        limit = 100_000
        spf = short_certificate.smallest_prime_factors(limit + 6)
        certificate = short_certificate.p_plus_six_type_i_certificate(937, spf)
        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertEqual((certificate.gap, certificate.x, certificate.divisor), (23, 240, 1_440))
        self.assertTrue(short_certificate.verify_certificate(certificate))
        # A residue 23 divisor need not itself be prime: 2017+6=7*17^2,
        # and the least qualifying divisor is 7*17=119.
        certificate = short_certificate.p_plus_six_type_i_certificate(2_017, spf)
        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertEqual((certificate.gap, certificate.x, certificate.divisor), (119, 534, 3_204))
        self.assertTrue(short_certificate.verify_certificate(certificate))
        self.assertIsNone(short_certificate.p_plus_six_type_i_certificate(73, spf))

        h_one = {1, 7, 13, 19}
        h_two = {1, 5, 7, 11}
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            value = prime + 6
            residues: set[int] = set()
            while value > 1:
                factor = spf[value]
                residues.add(factor % 24)
                while value % factor == 0:
                    value //= factor
            certificate = short_certificate.p_plus_six_type_i_certificate(prime, spf)
            self.assertEqual(
                certificate is None,
                residues <= h_one or residues <= h_two,
                (prime, residues),
            )
            if certificate is not None:
                self.assertEqual(certificate.divisor, 6 * certificate.x)
                self.assertTrue(short_certificate.verify_certificate(certificate), prime)

    def test_three_p_plus_four_internal_type_i_family(self):
        limit = 100_000
        spf = short_certificate.smallest_prime_factors(3 * limit + 4)

        # This is an internal (A,B)=(4,3) point, not an external B=1 point.
        certificate = short_certificate.three_p_plus_four_internal_type_i_certificate(
            313, spf
        )
        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertEqual(
            (certificate.gap, certificate.x, certificate.divisor), (23, 84, 112)
        )
        self.assertEqual(
            short_certificate.type_i_normal_form(
                313, certificate.gap, certificate.divisor
            ),
            (4, 3, 7),
        )

        # Composite divisors matter: 3*1297+4=5*19*41 and m=95 works,
        # although none of those three prime factors is 47 modulo 48.
        certificate = short_certificate.three_p_plus_four_internal_type_i_certificate(
            1_297, spf
        )
        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertEqual(
            (certificate.gap, certificate.x, certificate.divisor), (95, 348, 464)
        )
        self.assertEqual(
            short_certificate.type_i_normal_form(
                1_297, certificate.gap, certificate.divisor
            ),
            (4, 3, 29),
        )

        # The former five-branch residual p=2521 has this internal Type I
        # certificate in addition to its separate Type II certificate.
        certificate = short_certificate.three_p_plus_four_internal_type_i_certificate(
            2_521, spf
        )
        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertEqual(
            (certificate.gap, certificate.x, certificate.divisor), (23, 636, 848)
        )
        self.assertEqual(
            short_certificate.type_i_normal_form(
                2_521, certificate.gap, certificate.divisor
            ),
            (4, 3, 53),
        )
        self.assertIsNone(
            short_certificate.three_p_plus_four_internal_type_i_certificate(73, spf)
        )

        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            value = 3 * prime + 4
            target = (-prime) % 48
            expected_gaps = [
                gap
                for gap in short_certificate.positive_divisors_from_spf(value, spf)
                if gap % 48 == target
            ]
            candidate = short_certificate.three_p_plus_four_internal_type_i_certificate(
                prime, spf
            )
            self.assertEqual(candidate is not None, bool(expected_gaps), prime)
            if candidate is None:
                continue
            self.assertEqual(candidate.gap, expected_gaps[0])
            self.assertEqual(candidate.gap % 48, target)
            self.assertEqual((3 * prime + 4) % candidate.gap, 0)
            self.assertLessEqual(candidate.gap, (3 * prime + 4) // 41)
            self.assertLessEqual(candidate.gap, prime - 2)
            self.assertEqual(
                short_certificate.type_i_normal_form(
                    prime, candidate.gap, candidate.divisor
                ),
                (4, 3, (prime + candidate.gap) // 48),
            )
            self.assertTrue(short_certificate.verify_certificate(candidate), prime)

    def test_three_p_plus_four_failure_has_a_residue_transversal(self):
        # If the (A,B)=(4,3) branch fails, no two prime-factor residue
        # classes may multiply to its target t modulo 48.  Since t has no
        # square root, the involution r -> t/r splits the unit group into
        # eight pairs and the observed classes fit in a transversal.
        limit = 100_000
        spf = short_certificate.smallest_prime_factors(3 * limit + 4)
        units = {value for value in range(1, 48) if math.gcd(value, 48) == 1}
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            target = (-prime) % 48
            self.assertIn(target, (23, 47))
            self.assertFalse(any(value * value % 48 == target for value in units))

            value = 3 * prime + 4
            residues: set[int] = set()
            while value > 1:
                factor = spf[value]
                residues.add(factor % 48)
                while value % factor == 0:
                    value //= factor

            certificate = short_certificate.three_p_plus_four_internal_type_i_certificate(
                prime, spf
            )
            if certificate is not None:
                continue

            self.assertNotIn(target, residues, prime)
            pairs: list[tuple[int, int]] = []
            seen: set[int] = set()
            for residue in sorted(units):
                if residue in seen:
                    continue
                complement = target * pow(residue, -1, 48) % 48
                self.assertIn(complement, units)
                self.assertNotEqual(residue, complement)
                pairs.append((residue, complement))
                seen.update((residue, complement))
            self.assertEqual(len(pairs), 8)
            self.assertEqual(seen, units)

            transversal: set[int] = set()
            for first, second in pairs:
                self.assertFalse(
                    first in residues and second in residues,
                    (prime, target, first, second, residues),
                )
                if first in residues:
                    transversal.add(first)
                elif second in residues:
                    transversal.add(second)
                elif first == target:
                    transversal.add(second)
                elif second == target:
                    transversal.add(first)
                else:
                    transversal.add(first)
            self.assertEqual(len(transversal), 8)
            self.assertTrue(residues <= transversal, (prime, residues, transversal))

    def test_three_p_plus_power_two_internal_type_i_ray(self):
        limit = 100_000
        powers = (4, 8, 16, 32, 64)
        spf = short_certificate.smallest_prime_factors(3 * limit + max(powers))

        # The A=4 ray is exactly the previously isolated internal branch.
        self.assertEqual(
            short_certificate.three_p_plus_power_two_internal_type_i_certificate(
                2_521, 4, spf
            ),
            short_certificate.three_p_plus_four_internal_type_i_certificate(2_521, spf),
        )
        examples = {
            8: (2_689, 95, 696, 1_856, (8, 3, 29)),
            16: (1_321, 23, 336, 1_792, (16, 3, 7)),
            32: (11_497, 23, 2_880, 30_720, (32, 3, 30)),
            64: (22_993, 47, 5_760, 122_880, (64, 3, 30)),
        }
        for a, (prime, gap, x, divisor, normal) in examples.items():
            certificate = short_certificate.three_p_plus_power_two_internal_type_i_certificate(
                prime, a, spf
            )
            self.assertIsNotNone(certificate)
            assert certificate is not None
            self.assertEqual((certificate.gap, certificate.x, certificate.divisor), (gap, x, divisor))
            self.assertEqual(
                short_certificate.type_i_normal_form(prime, gap, divisor), normal
            )
            self.assertTrue(short_certificate.verify_certificate(certificate))

        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            for a in powers:
                value = 3 * prime + a
                modulus = 12 * a
                target = (-prime) % modulus
                expected_gaps = [
                    gap
                    for gap in short_certificate.positive_divisors_from_spf(value, spf)
                    if gap % modulus == target
                ]
                candidate = short_certificate.three_p_plus_power_two_internal_type_i_certificate(
                    prime, a, spf
                )
                self.assertEqual(candidate is not None, bool(expected_gaps), (prime, a))
                if candidate is None:
                    continue
                self.assertEqual(candidate.gap, expected_gaps[0])
                self.assertEqual((3 * prime + a) % candidate.gap, 0)
                self.assertEqual(candidate.gap % modulus, target)
                self.assertLessEqual(candidate.gap, (3 * prime + a) // (11 * a - 3))
                self.assertLessEqual(candidate.gap, prime - 2)
                self.assertEqual(
                    short_certificate.type_i_normal_form(
                        prime, candidate.gap, candidate.divisor
                    ),
                    (a, 3, (prime + candidate.gap) // modulus),
                )
                self.assertTrue(short_certificate.verify_certificate(candidate), (prime, a))

        for invalid_a in (0, 1, 2, 3, 5, 6, 12):
            self.assertIsNone(
                short_certificate.three_p_plus_power_two_internal_type_i_certificate(
                    73, invalid_a, spf
                )
            )

    def test_wide_internal_type_i_factor_ray(self):
        # This covers internal normal forms beyond B=3.  The cofactor bound
        # A-B>B is what makes every matching divisor a natural-gap witness.
        limit = 100_000
        pairs = ((12, 5), (16, 5), (20, 7), (28, 11))
        spf = short_certificate.smallest_prime_factors(
            max(b * limit + a for a, b in pairs)
        )
        examples = {
            (12, 5): (1_033, 167, 300, 720, (12, 5, 5)),
            (16, 5): (7_321, 39, 1_840, 5_888, (16, 5, 23)),
            (20, 7): (2_473, 327, 700, 2_000, (20, 7, 5)),
            (28, 11): (13_537, 15, 3_388, 8_624, (28, 11, 11)),
        }
        for (a, b), (prime, gap, x, divisor, normal) in examples.items():
            certificate = short_certificate.wide_internal_type_i_factor_ray_certificate(
                prime, a, b, spf
            )
            self.assertIsNotNone(certificate)
            assert certificate is not None
            self.assertEqual((certificate.gap, certificate.x, certificate.divisor), (gap, x, divisor))
            self.assertEqual(
                short_certificate.type_i_normal_form(prime, gap, divisor), normal
            )
            self.assertTrue(short_certificate.verify_certificate(certificate))

        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            for a, b in pairs:
                value = b * prime + a
                modulus = 4 * a * b
                expected_gaps = (
                    [
                        gap
                        for gap in short_certificate.positive_divisors_from_spf(value, spf)
                        if gap % modulus == (-prime) % modulus
                    ]
                    if prime > a + 2 * b + 2
                    else []
                )
                candidate = short_certificate.wide_internal_type_i_factor_ray_certificate(
                    prime, a, b, spf
                )
                self.assertEqual(candidate is not None, bool(expected_gaps), (prime, a, b))
                if candidate is None:
                    continue
                self.assertEqual(candidate.gap, expected_gaps[0])
                self.assertEqual((b * prime + a) % candidate.gap, 0)
                self.assertGreaterEqual((b * prime + a) // candidate.gap, a - b)
                self.assertLessEqual(candidate.gap, (b * prime + a) // (a - b))
                self.assertLessEqual(candidate.gap, prime - 2)
                self.assertEqual(
                    short_certificate.type_i_normal_form(
                        prime, candidate.gap, candidate.divisor
                    ),
                    (a, b, (prime + candidate.gap) // modulus),
                )
                self.assertTrue(short_certificate.verify_certificate(candidate), (prime, a, b))

        # On failure, all prime factors of B*p+A fit into one side of the
        # involution r -> -p/r modulo 4AB.
        a, b = 12, 5
        modulus = 4 * a * b
        units = {value for value in range(1, modulus) if math.gcd(value, modulus) == 1}
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1 or prime <= a + 2 * b + 2:
                continue
            candidate = short_certificate.wide_internal_type_i_factor_ray_certificate(
                prime, a, b, spf
            )
            if candidate is not None:
                continue
            target = (-prime) % modulus
            self.assertFalse(any(value * value % modulus == target for value in units))
            value = b * prime + a
            residues: set[int] = set()
            while value > 1:
                factor = spf[value]
                residues.add(factor % modulus)
                while value % factor == 0:
                    value //= factor
            self.assertTrue(residues <= units, (prime, residues))
            self.assertNotIn(target, residues, (prime, residues))
            seen: set[int] = set()
            for residue in units:
                if residue in seen:
                    continue
                complement = target * pow(residue, -1, modulus) % modulus
                self.assertNotEqual(residue, complement)
                self.assertFalse(
                    residue in residues and complement in residues,
                    (prime, residue, complement, residues),
                )
                seen.update((residue, complement))
            self.assertEqual(seen, units)

        for invalid in ((8, 5), (12, 6), (6, 3), (10, 3), (12, 9)):
            self.assertIsNone(
                short_certificate.wide_internal_type_i_factor_ray_certificate(
                    1_033, *invalid, spf
                )
            )

    def test_fixed_gap_type_ii_factor_ray(self):
        limit = 100_000
        gaps = (7, 11, 19, 23)
        spf = short_certificate.smallest_prime_factors(limit + max(gaps))
        examples = {
            (5_569, 7): (34, 41),
            (21_529, 11): (1_077, 5),
            (9_601, 19): (37, 65),
            (42_169, 23): (1_172, 9),
        }
        for (prime, gap), (b, c) in examples.items():
            certificate = short_certificate.fixed_gap_type_ii_factor_certificate(
                prime, gap, spf
            )
            self.assertIsNotNone(certificate)
            assert certificate is not None
            self.assertEqual(
                short_certificate.type_ii_normal_form(
                    prime, gap, certificate.divisor
                ),
                (1, b, c),
            )
            self.assertTrue(short_certificate.verify_certificate(certificate))

        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            for gap in gaps:
                x = (prime + gap) // 4
                expected_factors = (
                    [
                        factor
                        for factor in short_certificate.positive_divisors_from_spf(x, spf)
                        if factor % gap == gap - 1
                    ]
                    if gap <= prime - 2
                    else []
                )
                candidate = short_certificate.fixed_gap_type_ii_factor_certificate(
                    prime, gap, spf
                )
                self.assertEqual(candidate is not None, bool(expected_factors), (prime, gap))
                if candidate is None:
                    continue
                self.assertEqual(
                    short_certificate.type_ii_normal_form(
                        prime, gap, candidate.divisor
                    ),
                    (1, expected_factors[0], x // expected_factors[0]),
                )
                self.assertTrue(short_certificate.verify_certificate(candidate), (prime, gap))

            # A successful divisor can be composite. The converse needed for
            # the sieve is only one-way: on failure, the prime-factor classes
            # contain neither -1 nor a complementary pair.
            for gap in gaps:
                if gap > prime - 2:
                    continue
                candidate = short_certificate.fixed_gap_type_ii_factor_certificate(
                    prime, gap, spf
                )
                if candidate is not None:
                    continue
                x = (prime + gap) // 4
                value = x
                residues: set[int] = set()
                while value > 1:
                    factor = spf[value]
                    residues.add(factor % gap)
                    while value % factor == 0:
                        value //= factor
                units = set(range(1, gap))
                target = gap - 1
                self.assertFalse(
                    any(value * value % gap == target for value in units),
                    gap,
                )
                self.assertNotIn(target, residues, (prime, gap, residues))
                seen: set[int] = set()
                transversal: set[int] = set()
                for residue in sorted(units):
                    if residue in seen:
                        continue
                    complement = target * pow(residue, -1, gap) % gap
                    self.assertNotEqual(residue, complement)
                    self.assertFalse(
                        residue in residues and complement in residues,
                        (prime, gap, residue, complement, residues),
                    )
                    seen.update((residue, complement))
                    transversal.add(
                        residue
                        if residue in residues or complement not in residues
                        else complement
                    )
                self.assertEqual(len(transversal), (gap - 1) // 2)
                self.assertTrue(residues <= transversal, (prime, gap, residues, transversal))

        # q=3 is permitted by the theorem, even though this p has no
        # corresponding factor witness. Composite and 1 mod 4 inputs are
        # rejected before a divisor search.
        self.assertIsNone(
            short_certificate.fixed_gap_type_ii_factor_certificate(73, 3, spf)
        )
        for invalid_gap in (1, 5, 9, 15, 17):
            self.assertIsNone(
                short_certificate.fixed_gap_type_ii_factor_certificate(
                    73, invalid_gap, spf
                )
            )

    def test_lcm_boundary_type_i_face(self):
        spf = short_certificate.smallest_prime_factors(3_000)
        certificate = short_certificate.lcm_boundary_type_i_certificate(97, 7, spf)
        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertEqual((certificate.x, certificate.divisor, certificate.y, certificate.z), (26, 26, 364, 35_308))
        self.assertEqual(math.gcd(certificate.x, certificate.y), certificate.divisor)
        self.assertEqual(certificate.z, 97 * math.lcm(certificate.x, certificate.y))

        # The first geometric-pattern exception has no A=1 Type I certificate
        # at any natural gap, although it has a Type II certificate at m=23.
        self.assertTrue(
            all(
                short_certificate.lcm_boundary_type_i_certificate(2_521, gap, spf)
                is None
                for gap in range(3, 2_521 - 1, 4)
            )
        )
        self.assertIsNotNone(
            short_certificate.certificate_at_gap(2_521, 23, spf)
        )

        limit = 5_000
        spf = short_certificate.smallest_prime_factors(limit)
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            for gap in range(3, min(107, prime - 2) + 1, 4):
                x = (prime + gap) // 4
                expected = any(
                    (prime * x + divisor) % gap == 0
                    for divisor in short_certificate.positive_divisors_from_spf(x, spf)
                )
                candidate = short_certificate.lcm_boundary_type_i_certificate(
                    prime, gap, spf
                )
                self.assertEqual(candidate is not None, expected, (prime, gap))
                if candidate is not None:
                    self.assertEqual(math.gcd(candidate.x, candidate.y), candidate.divisor)
                    self.assertEqual(
                        candidate.z,
                        prime * math.lcm(candidate.x, candidate.y),
                    )

    def test_gap_seven_congruence_family(self):
        expected = {
            3: ("II", 1),
            5: ("I", None),
            6: ("II", 2),
        }
        for prime in short_certificate.primes_up_to(100_000):
            if prime % 24 != 1:
                continue
            certificate = short_certificate.gap_seven_congruence_certificate(prime)
            self.assertEqual(certificate is not None, prime % 7 in expected, prime)
            if certificate is None:
                continue
            self.assertEqual(certificate.certificate_type, expected[prime % 7][0])
            expected_divisor = expected[prime % 7][1]
            if expected_divisor is None:
                expected_divisor = 2 * certificate.x
            self.assertEqual(certificate.divisor, expected_divisor)
            self.assertTrue(short_certificate.verify_certificate(certificate), prime)

    def test_fixed_divisor_gap_generator_and_finite_avoidance_progression(self):
        # The generic generator contains the m=7 family and also discovers
        # the analogous m=11 residue classes without factoring x.
        expected_seven = {3, 5, 6}
        expected_eleven = {7, 8, 10}
        for prime in short_certificate.primes_up_to(100_000):
            if prime % 24 != 1:
                continue
            self.assertEqual(
                short_certificate.fixed_divisor_gap_certificate(prime, 7) is not None,
                prime % 7 in expected_seven,
                (prime, 7),
            )
            self.assertEqual(
                short_certificate.fixed_divisor_gap_certificate(prime, 11) is not None,
                prime % 11 in expected_eleven,
                (prime, 11),
            )

        gaps = [3, 7, 11, 23]
        modulus = short_certificate.fixed_divisor_gap_avoidance_modulus(gaps)
        self.assertEqual(modulus, math.lcm(24, *gaps))
        progression_primes = 0
        for prime in short_certificate.primes_up_to(1_000_000):
            if prime % modulus != 1:
                continue
            progression_primes += 1
            for gap in gaps:
                self.assertIsNone(
                    short_certificate.fixed_divisor_gap_certificate(prime, gap),
                    (prime, gap),
                )
        self.assertGreater(progression_primes, 0)
        with self.assertRaises(ValueError):
            short_certificate.fixed_divisor_gap_avoidance_modulus([5])

    def test_three_p_plus_one_descent_type_i_family(self):
        limit = 100_000
        spf = short_certificate.smallest_prime_factors((3 * limit + 1) // 4 + 1)
        self.assertIsNotNone(
            short_certificate.three_p_plus_one_descent_certificate(73, spf)
        )
        self.assertIsNone(
            short_certificate.three_p_plus_one_descent_certificate(97, spf)
        )

        certificate = short_certificate.three_p_plus_one_descent_certificate(73, spf)
        assert certificate is not None
        self.assertEqual(
            (certificate.gap, certificate.x, certificate.divisor), (7, 20, 80)
        )
        self.assertTrue(short_certificate.verify_certificate(certificate))

        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            source = (3 * prime + 1) // 4
            value = source
            candidate_q = None
            while value > 1:
                factor = spf[value]
                if factor % 3 == 2:
                    candidate_q = factor if candidate_q is None else min(candidate_q, factor)
                while value % factor == 0:
                    value //= factor

            certificate = short_certificate.three_p_plus_one_descent_certificate(
                prime, spf
            )
            self.assertEqual(certificate is not None, candidate_q is not None, prime)
            source_pairs = short_certificate.two_term_unit_fraction_pairs(3, source, spf)
            self.assertEqual(bool(source_pairs), candidate_q is not None, prime)
            for first, second in source_pairs:
                self.assertEqual(
                    short_certificate.Fraction(4, source),
                    short_certificate.Fraction(1, source)
                    + short_certificate.Fraction(1, first)
                    + short_certificate.Fraction(1, second),
                )
                self.assertEqual(
                    short_certificate.Fraction(4, prime),
                    short_certificate.Fraction(1, prime * source)
                    + short_certificate.Fraction(1, first)
                    + short_certificate.Fraction(1, second),
                )
            if certificate is None:
                continue
            assert candidate_q is not None
            q = candidate_q
            r = (source // q + 1) // 3
            self.assertLess(source, prime)
            self.assertLessEqual(q * q, source)
            self.assertEqual(certificate.gap, (4 * q + 1) // 3)
            self.assertEqual(certificate.x, q * r)
            self.assertEqual(certificate.divisor, q * r * r)
            self.assertTrue(short_certificate.verify_certificate(certificate), prime)
            self.assertEqual(
                short_certificate.Fraction(4, source),
                short_certificate.Fraction(1, source)
                + short_certificate.Fraction(1, q * r)
                + short_certificate.Fraction(1, source * r),
            )
            self.assertEqual(
                short_certificate.Fraction(4, prime),
                short_certificate.Fraction(1, prime * source)
                + short_certificate.Fraction(1, q * r)
                + short_certificate.Fraction(1, source * r),
            )

    def test_three_p_plus_one_source_has_no_other_two_denominator_lifts(self):
        # The theorem classifies every two-denominator-preserving lift from
        # n=(3p+1)/4, not only the explicit source point used for its certificate.
        for prime in (73, 97, 2_521):
            source = (3 * prime + 1) // 4
            spf = short_certificate.smallest_prime_factors(source * source // 2 + 1)
            source_solutions: set[tuple[int, int, int]] = set()
            for first in range((source + 3) // 4, source // 2 + 1):
                for second, third in short_certificate.two_term_unit_fraction_pairs(
                    4 * first - source, source * first, spf
                ):
                    if first <= second <= third:
                        source_solutions.add((first, second, third))

            for triple in source_solutions:
                for replaced in set(triple):
                    lifted = short_certificate.two_denominator_lift_candidate(
                        prime, source, replaced
                    )
                    if lifted is not None:
                        self.assertEqual(replaced, source, (prime, triple, lifted))
                        self.assertEqual(lifted, prime * source)

    def test_adaptive_external_source_descent(self):
        # The k=1 slice is the existing q=3 descent. The other examples
        # verify the q=7,11,23 slices and a composite q=15 instance.
        limit = 100_000
        spf = short_certificate.smallest_prime_factors(limit + 1)
        examples = {
            (73, 1): (3, 55, 5, 7, 20, 80),
            (193, 2): (7, 169, 13, 15, 52, 104),
            (1_489, 3): (11, 1_365, 21, 23, 378, 2_268),
            (1_033, 6): (23, 990, 22, 23, 264, 528),
            (1_777, 4): (15, 1_666, 14, 15, 448, 3_584),
        }
        for (prime, k), (q, source, factor, gap, x, divisor) in examples.items():
            witness = short_certificate.external_source_descent_witness(
                prime, spf, k
            )
            self.assertIsNotNone(witness)
            assert witness is not None
            self.assertEqual(
                (witness.q, witness.source_denominator, witness.factor),
                (q, source, factor),
            )
            certificate = witness.certificate
            self.assertEqual(
                (certificate.gap, certificate.x, certificate.divisor),
                (gap, x, divisor),
            )
            self.assertTrue(short_certificate.verify_certificate(certificate))
            self.assertLess(witness.source_denominator, prime)
            self.assertLessEqual(witness.factor * witness.factor, witness.source_denominator)
            self.assertEqual(
                short_certificate.Fraction(4, witness.source_denominator),
                sum(
                    (short_certificate.Fraction(1, value) for value in witness.source_solution),
                    short_certificate.Fraction(),
                ),
            )
            self.assertEqual(
                short_certificate.Fraction(4, prime),
                sum(
                    (short_certificate.Fraction(1, value) for value in witness.target_solution),
                    short_certificate.Fraction(),
                ),
            )
            self.assertEqual(
                sorted(witness.target_solution),
                sorted((certificate.x, certificate.y, certificate.z)),
            )

        # The fixed-k condition is exact, including its failure. With no k
        # supplied, the adaptive search returns the first successful k.
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            base = (prime - 1) // 4
            expected_first = None
            for k in short_certificate.positive_divisors_from_spf(base, spf):
                q = 4 * k - 1
                source = (q * prime + 1) // (q + 1)
                expected_factors = [
                    factor
                    for factor in short_certificate.positive_divisors_from_spf(source, spf)
                    if factor % q == q - 1 and factor <= source // factor
                ]
                witness = short_certificate.external_source_descent_witness(
                    prime, spf, k
                )
                self.assertEqual(witness is not None, bool(expected_factors), (prime, k))
                if witness is None:
                    continue
                self.assertEqual(witness.factor, expected_factors[0], (prime, k))
                if expected_first is None:
                    expected_first = witness
            adaptive = short_certificate.external_source_descent_witness(prime, spf)
            self.assertEqual(adaptive is not None, expected_first is not None, prime)
            if adaptive is not None:
                assert expected_first is not None
                self.assertEqual(adaptive.k, expected_first.k)
                self.assertTrue(short_certificate.verify_certificate(adaptive.certificate))

        self.assertIsNone(short_certificate.external_source_descent_witness(97, spf))
        self.assertIsNone(short_certificate.external_source_descent_witness(73, spf, 5))

    def test_mixed_factor_external_source_descent(self):
        # p=97 is absent from the older d=1 branch: its q=7 source n=85
        # has no -1 divisor.  The factor g=34 of k*n=170 nevertheless
        # supplies a marked source solution and a Type I gap-39 certificate.
        limit = 100_000
        spf = short_certificate.smallest_prime_factors(limit + 1)
        self.assertIsNone(short_certificate.external_source_descent_witness(97, spf))
        witness = short_certificate.mixed_factor_external_source_descent_witness(
            97, spf, 2
        )
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(
            (witness.q, witness.source_denominator, witness.factor), (7, 85, 34)
        )
        self.assertEqual(witness.source_solution, (170, 34, 85))
        self.assertEqual(witness.target_solution, (16_490, 34, 85))
        self.assertEqual(
            (witness.certificate.gap, witness.certificate.x, witness.certificate.divisor),
            (39, 34, 17),
        )
        self.assertTrue(short_certificate.verify_certificate(witness.certificate))
        self.assertEqual(
            sorted(witness.target_solution),
            sorted(
                (
                    witness.certificate.x,
                    witness.certificate.y,
                    witness.certificate.z,
                )
            ),
        )

        # The fixed-k predicate is exact.  Unlike the preceding branch, it
        # factors k*n by merging the independently factorable k and n parts.
        adaptive_misses = 0
        newly_captured = 0
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            base = (prime - 1) // 4
            expected_first = None
            for k in short_certificate.positive_divisors_from_spf(base, spf):
                q = 4 * k - 1
                source = (q * prime + 1) // (q + 1)
                expected_factors = [
                    factor
                    for factor in short_certificate.positive_divisors_product_from_spf(
                        k, source, spf
                    )
                    if factor <= source and factor % q == q - 1
                ]
                fixed = short_certificate.mixed_factor_external_source_descent_witness(
                    prime, spf, k
                )
                self.assertEqual(fixed is not None, bool(expected_factors), (prime, k))
                if fixed is None:
                    continue
                self.assertEqual(fixed.factor, expected_factors[0], (prime, k))
                self.assertTrue(short_certificate.verify_certificate(fixed.certificate))
                self.assertEqual(
                    sorted(fixed.target_solution),
                    sorted(
                        (
                            fixed.certificate.x,
                            fixed.certificate.y,
                            fixed.certificate.z,
                        )
                    ),
                )
                if expected_first is None:
                    expected_first = fixed
            mixed = short_certificate.mixed_factor_external_source_descent_witness(
                prime, spf
            )
            self.assertEqual(mixed is not None, expected_first is not None, prime)
            if short_certificate.external_source_descent_witness(prime, spf) is None:
                adaptive_misses += 1
                newly_captured += mixed is not None

        # This is an exact finite audit, not an extrapolation to all primes.
        self.assertEqual((adaptive_misses, newly_captured), (222, 185))

    def test_quadratic_factor_external_source_descent(self):
        # The full two-unit-fraction tail at k=6 is already stronger than
        # the mixed-factor condition: e=63 divides (6*392)^2 but is not a
        # multiple of 6. It supplies a gap-11 certificate for p=409.
        limit = 100_000
        spf = short_certificate.smallest_prime_factors(limit + 1)
        self.assertIsNone(
            short_certificate.mixed_factor_external_source_descent_witness(409, spf)
        )
        witness = short_certificate.quadratic_factor_external_source_descent_witness(
            409, spf, 6
        )
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(
            (witness.q, witness.source_denominator, witness.factor), (23, 392, 63)
        )
        self.assertEqual(witness.source_solution, (2_352, 105, 3_920))
        self.assertEqual(witness.target_solution, (961_968, 105, 3_920))
        self.assertEqual(
            (witness.certificate.gap, witness.certificate.x, witness.certificate.divisor),
            (11, 105, 175),
        )
        self.assertTrue(short_certificate.verify_certificate(witness.certificate))

        mixed_misses = 0
        newly_captured = 0
        general_misses: list[int] = []
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            base = (prime - 1) // 4
            expected_first = None
            for k in short_certificate.positive_divisors_from_spf(base, spf):
                q = 4 * k - 1
                source = (q * prime + 1) // (q + 1)
                preserved = k * source
                expected_factors = [
                    factor
                    for factor in short_certificate.positive_divisors_square_product_from_spf(
                        k, source, spf
                    )
                    if factor <= preserved and factor % q == (-preserved) % q
                ]
                fixed = short_certificate.quadratic_factor_external_source_descent_witness(
                    prime, spf, k
                )
                self.assertEqual(fixed is not None, bool(expected_factors), (prime, k))
                if fixed is None:
                    continue
                self.assertEqual(fixed.factor, expected_factors[0], (prime, k))
                self.assertTrue(short_certificate.verify_certificate(fixed.certificate))
                self.assertEqual(
                    sorted(fixed.target_solution),
                    sorted(
                        (
                            fixed.certificate.x,
                            fixed.certificate.y,
                            fixed.certificate.z,
                        )
                    ),
                )
                if expected_first is None:
                    expected_first = fixed
            quadratic = short_certificate.quadratic_factor_external_source_descent_witness(
                prime, spf
            )
            self.assertEqual(quadratic is not None, expected_first is not None, prime)

            mixed = short_certificate.mixed_factor_external_source_descent_witness(
                prime, spf
            )
            if mixed is not None:
                self.assertIsNotNone(quadratic, prime)
            else:
                mixed_misses += 1
                if quadratic is not None:
                    newly_captured += 1
                else:
                    general_misses.append(prime)

        # Exact finite audit only. The remaining list is deliberately kept
        # visible as the next selector target rather than hidden by a count.
        self.assertEqual((mixed_misses, newly_captured), (37, 21))
        self.assertEqual(
            general_misses,
            [
                5_209,
                8_329,
                18_169,
                21_169,
                27_481,
                31_849,
                33_529,
                39_769,
                48_409,
                52_369,
                68_329,
                73_849,
                80_809,
                87_481,
                88_729,
                94_009,
            ],
        )

    def test_shifted_quadratic_factor_external_source_descent(self):
        limit = 100_000
        spf = short_certificate.smallest_prime_factors(limit + 1)
        examples = {
            # d=1 recovers the full-tail construction, sometimes with a
            # smaller factor than the preceding mixed-factor witness.
            (97, 2, 1): (7, 85, 5, 3, 25, 125),
            (409, 6, 1): (23, 392, 63, 11, 105, 175),
            # The full shifted tail improves on the old e=k*f slice.
            (2_473, 7, 9): (27, 2_385, 45, 7, 620, 76_880),
            (8_329, 160, 9): (639, 8_316, 4_950, 31, 2_090, 7_942),
            (18_169, 19, 5): (75, 17_930, 55, 3, 4_543, 1_876_259),
        }
        for (prime, k, shift), expected in examples.items():
            q, source, factor, gap, x, divisor = expected
            witness = short_certificate.shifted_quadratic_factor_external_source_descent_witness(
                prime, k, shift, spf
            )
            self.assertIsNotNone(witness)
            assert witness is not None
            self.assertEqual(
                (witness.q, witness.source_denominator, witness.factor),
                (q, source, factor),
            )
            self.assertEqual(
                (witness.certificate.gap, witness.certificate.x, witness.certificate.divisor),
                (gap, x, divisor),
            )
            self.assertTrue(short_certificate.verify_certificate(witness.certificate))
            self.assertEqual(
                sorted(witness.target_solution),
                sorted(
                    (
                        witness.certificate.x,
                        witness.certificate.y,
                        witness.certificate.z,
                    )
                ),
            )

        # On a fixed nonzero shifted ray, both factor congruences and d|e
        # are necessary. The routine must neither omit nor invent a tail.
        k, shift = 19, 5
        q = 4 * k - 1
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1 or (prime - shift) % (4 * k):
                continue
            source = (q * prime + shift) // (q + 1)
            preserved = k * source
            expected_factors = [
                factor
                for factor in short_certificate.positive_divisors_square_product_from_spf(
                    k, source, spf
                )
                if factor <= preserved
                and factor % shift == 0
                and (preserved + factor) % q == 0
                and (preserved + preserved * preserved // factor) % q == 0
            ]
            witness = short_certificate.shifted_quadratic_factor_external_source_descent_witness(
                prime, k, shift, spf
            )
            self.assertEqual(witness is not None, bool(expected_factors), prime)
            if witness is not None:
                self.assertEqual(witness.factor, expected_factors[0], prime)
                self.assertTrue(short_certificate.verify_certificate(witness.certificate))
                source_distance = prime - witness.source_denominator
                self.assertEqual(witness.source_denominator % shift, 0)
                tail_source = witness.source_denominator // shift
                tail_preserved = k * tail_source
                tail_factor = witness.factor // shift
                self.assertEqual(tail_preserved * tail_preserved % tail_factor, 0)
                normalized_gcd = math.gcd(tail_factor, tail_preserved)
                self.assertEqual(
                    (tail_factor // normalized_gcd + tail_preserved // normalized_gcd) % (q // shift),
                    0,
                )
                self.assertEqual(
                    witness.certificate.gap,
                    (4 * tail_factor + 1) // (q // shift),
                )
                self.assertEqual(
                    witness.source_denominator,
                    shift * (source_distance * (q // shift) + 1),
                )

        self.assertIsNone(
            short_certificate.shifted_quadratic_factor_external_source_descent_witness(
                97, 7, 9, spf
            )
        )

    def test_p_minus_one_source_descent(self):
        # The reduced p-1 fan is exactly the part of the complete shifted
        # quadratic family whose smaller source denominator is p-1.
        limit = 10_000
        spf = short_certificate.smallest_prime_factors(limit + 1)
        hits = []
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            reduced = short_certificate.p_minus_one_source_descent_witness(
                prime, spf
            )
            complete = None
            for shift in short_certificate.positive_divisors_from_spf(prime - 1, spf):
                if shift % 4 != 1:
                    continue
                candidate_k = (prime - shift) // 4
                complete = (
                    short_certificate.shifted_quadratic_factor_external_source_descent_witness(
                        prime, candidate_k, shift, spf
                    )
                )
                if complete is not None:
                    break

            self.assertEqual(reduced is not None, complete is not None, prime)
            if reduced is None:
                continue
            assert complete is not None
            self.assertEqual(reduced, complete)
            self.assertEqual(reduced.source_denominator, prime - 1)
            self.assertEqual(
                short_certificate.Fraction(4, prime - 1),
                sum(
                    (
                        short_certificate.Fraction(1, value)
                        for value in reduced.source_solution
                    ),
                    short_certificate.Fraction(),
                ),
            )
            self.assertTrue(short_certificate.verify_certificate(reduced.certificate))
            hits.append(prime)

        self.assertEqual(len(hits), 64)
        self.assertEqual(hits[:4], [313, 409, 457, 937])

    def test_odd_distance_even_source_descent(self):
        # For every fixed odd distance c, this reduced fan is exactly the
        # complete shifted quadratic family whose source is p-c.
        limit = 10_000
        spf = short_certificate.smallest_prime_factors(limit + 1)
        examples = {
            # p, c: q, source, full shifted factor, gap, x, Type I divisor
            (73, 3): (23, 70, 40, 7, 20, 10),
            (337, 7): (47, 330, 176, 15, 88, 44),
            (2_137, 3): (679, 2_134, 485, 3, 535, 57_245),
        }
        for (prime, distance), expected in examples.items():
            witness = short_certificate.even_source_distance_descent_witness(
                prime, distance, spf
            )
            self.assertIsNotNone(witness)
            assert witness is not None
            q, source, factor, gap, x, divisor = expected
            self.assertEqual(
                (witness.q, witness.source_denominator, witness.factor),
                (q, source, factor),
            )
            self.assertEqual(
                (witness.certificate.gap, witness.certificate.x, witness.certificate.divisor),
                (gap, x, divisor),
            )
            self.assertTrue(short_certificate.verify_certificate(witness.certificate))

        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            self.assertEqual(
                short_certificate.even_source_distance_descent_witness(prime, 1, spf),
                short_certificate.p_minus_one_source_descent_witness(prime, spf),
            )
            for distance in (1, 3, 7):
                reduced = short_certificate.even_source_distance_descent_witness(
                    prime, distance, spf
                )
                complete = None
                source = prime - distance
                for shift in short_certificate.positive_divisors_from_spf(source, spf):
                    s = source // shift
                    if s <= 1 or (s - 1) % distance:
                        continue
                    r = (s - 1) // distance
                    if (shift * r + 1) % 4:
                        continue
                    candidate_k = (shift * r + 1) // 4
                    complete = (
                        short_certificate.shifted_quadratic_factor_external_source_descent_witness(
                            prime, candidate_k, shift, spf
                        )
                    )
                    if complete is not None:
                        break
                self.assertEqual(reduced, complete, (prime, distance))

        hits = [
            prime
            for prime in short_certificate.primes_up_to(limit)
            if prime % 24 == 1
            and any(
                short_certificate.even_source_distance_descent_witness(
                    prime, distance, spf
                )
                is not None
                for distance in range(1, 32, 2)
            )
        ]
        self.assertEqual(len(hits), 93)
        self.assertEqual(hits[:4], [73, 313, 337, 409])

        all_distance_hits = {
            prime: next(
                (
                    distance
                    for distance in range(1, prime, 2)
                    if short_certificate.even_source_distance_descent_witness(
                        prime, distance, spf
                    )
                    is not None
                ),
                None,
            )
            for prime in short_certificate.primes_up_to(limit)
            if prime % 24 == 1
        }
        self.assertEqual(
            sum(distance is not None for distance in all_distance_hits.values()),
            112,
        )
        self.assertEqual(
            [prime for prime, distance in all_distance_hits.items() if distance is None],
            [
                97,
                193,
                241,
                577,
                673,
                769,
                1_201,
                1_297,
                1_489,
                1_609,
                2_017,
                2_521,
                2_689,
                2_833,
                3_049,
                3_169,
                3_361,
                3_697,
                3_889,
                4_801,
                5_209,
                5_281,
                5_569,
                6_337,
                6_529,
                8_161,
                8_641,
                8_761,
                9_601,
                9_649,
                9_769,
            ],
        )

    def test_scaled_source_descent(self):
        limit = 100_000
        spf = short_certificate.smallest_prime_factors(limit + 1)

        # b=1 is the already complete shifted quadratic-factor family.
        old = short_certificate.shifted_quadratic_factor_external_source_descent_witness(
            409, 6, 1, spf
        )
        new = short_certificate.scaled_source_descent_witness(409, 6, 1, 1, spf)
        self.assertIsNotNone(old)
        self.assertIsNotNone(new)
        assert old is not None and new is not None
        self.assertEqual(
            (new.source_solution, new.target_solution, new.factor, new.certificate),
            (old.source_solution, old.target_solution, old.factor, old.certificate),
        )

        # b=2 and b=4 are genuinely non-multiple source denominators.
        examples = {
            (8_0809, 67, 2, 7): (603, 80_206, 4_718, 71, 20_220, 1_213_200),
            (8_329, 23, 2, 3): (181, 8_148, 966, 43, 2_093, 27_209),
            (27_481, 1_099, 4, 6): (25, 27_456, 165_792, 151, 6_908, 6_908),
        }
        for (prime, a, b, shift), expected in examples.items():
            distance, source, factor, gap, x, divisor = expected
            witness = short_certificate.scaled_source_descent_witness(
                prime, a, b, shift, spf
            )
            self.assertIsNotNone(witness)
            assert witness is not None
            self.assertEqual(
                (witness.distance, witness.source_denominator, witness.factor),
                (distance, source, factor),
            )
            self.assertEqual(
                (witness.certificate.gap, witness.certificate.x, witness.certificate.divisor),
                (gap, x, divisor),
            )
            self.assertTrue(short_certificate.verify_certificate(witness.certificate))

        # A fixed b=2 ray has no hidden search: every accepted factor is
        # exactly a divisor of (a*n)^2 meeting both tail congruences and the
        # Type I divisibility condition.
        a, b, shift = 23, 2, 3
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            numerator = b * (prime - shift)
            denominator = 4 * a
            if numerator % denominator:
                self.assertIsNone(
                    short_certificate.scaled_source_descent_witness(
                        prime, a, b, shift, spf
                    ),
                    prime,
                )
                continue
            distance = numerator // denominator
            source = prime - distance
            first = a * source // b
            q = 4 * a - b
            expected_factors = []
            if source >= 2 and source % b == 0 and first % shift == 0:
                tail_denominator = a * source
                expected_factors = [
                    factor
                    for factor in short_certificate.positive_divisors_square_product_from_spf(
                        a, source, spf
                    )
                    if factor <= tail_denominator
                    and factor % (b * shift) == 0
                    and (tail_denominator + factor) % q == 0
                    and (tail_denominator + tail_denominator * tail_denominator // factor)
                    % q
                    == 0
                    and 3 <= (4 * factor + b * shift) // q <= prime - 2
                ]
            witness = short_certificate.scaled_source_descent_witness(
                prime, a, b, shift, spf
            )
            self.assertEqual(witness is not None, bool(expected_factors), prime)
            if witness is not None:
                self.assertEqual(witness.factor, expected_factors[0], prime)
                self.assertTrue(short_certificate.verify_certificate(witness.certificate))

        for invalid_b in (0, 3, 5, 6, 8):
            self.assertIsNone(
                short_certificate.scaled_source_descent_witness(
                    80_809, 67, invalid_b, 7, spf
                )
            )

    def test_even_split_descent(self):
        p, n = 5_209, 2_680
        spf = short_certificate.smallest_prime_factors(p + 1)
        witness = short_certificate.even_split_descent_witness(p, n, spf)
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual((witness.factor, witness.replaced_denominator), (80, 1_380))
        self.assertEqual(witness.source_solution, (1_340, 1_380, 46_230))
        self.assertEqual(witness.target_solution, (1_340, 46_230, 481_624_140))
        self.assertEqual(
            (witness.certificate.certificate_type, witness.certificate.gap,
             witness.certificate.x, witness.certificate.divisor),
            ("I", 151, 1_340, 670),
        )
        self.assertTrue(short_certificate.verify_certificate(witness.certificate))

        # Every source containing n/2 is represented by a same-parity factor
        # e of n^2. The function returns precisely the first liftable pair.
        expected = []
        for factor in short_certificate.divisors_of_square(n, spf):
            if factor > n or factor % 2:
                continue
            companion = n * n // factor
            if (n + companion) % 2:
                continue
            a = (n + factor) // 2
            b = (n + companion) // 2
            for replaced, preserved in ((a, b), (b, a)):
                lifted = short_certificate.two_denominator_lift_candidate(
                    p, n, replaced
                )
                if lifted is not None and lifted >= n // 2:
                    expected.append((factor, replaced, preserved, lifted))
        self.assertEqual(expected[0], (80, 1_380, 46_230, 481_624_140))
        self.assertEqual(
            (witness.factor, witness.replaced_denominator, witness.target_solution[1], witness.target_solution[2]),
            expected[0],
        )

        # In the natural first-denominator window, this is the first even
        # source that yields a nonstandard split lift for this target.
        for source in range((p + 3) // 2, n, 2):
            self.assertIsNone(short_certificate.even_split_descent_witness(p, source, spf))
        self.assertIsNone(short_certificate.even_split_descent_witness(p, n - 1, spf))

    def test_residual_split_descent(self):
        # The three possible retained contributions r/n have one common
        # factorization of the residual (4-r)/n.  These examples exercise
        # the r=1,2,3 slices and certify that the retained n/r is the target
        # first denominator.
        cases = (
            (1_129, 304, 1, 8, 104, (304, 104, 3_952), (304, 3_952, 2_230_904),
             ("I", 87, 304, 608)),
            (5_209, 2_680, 2, 80, 1_380, (1_340, 1_380, 46_230),
             (1_340, 46_230, 481_624_140), ("I", 151, 1_340, 670)),
            (73, 60, 3, 24, 84, (20, 84, 210), (20, 210, 30_660),
             ("II", 7, 20, 1)),
        )
        spf = short_certificate.smallest_prime_factors(5_210)
        for (
            p,
            n,
            r,
            factor,
            replaced,
            source_solution,
            target_solution,
            expected_certificate,
        ) in cases:
            with self.subTest(p=p, r=r):
                witness = short_certificate.residual_split_descent_witness(
                    p, n, r, spf
                )
                self.assertIsNotNone(witness)
                assert witness is not None
                self.assertEqual(
                    (witness.factor, witness.replaced_denominator),
                    (factor, replaced),
                )
                self.assertEqual(witness.source_solution, source_solution)
                self.assertEqual(witness.target_solution, target_solution)
                self.assertEqual(
                    (
                        witness.certificate.certificate_type,
                        witness.certificate.gap,
                        witness.certificate.x,
                        witness.certificate.divisor,
                    ),
                    expected_certificate,
                )
                self.assertTrue(short_certificate.verify_certificate(witness.certificate))

        # There is no r=4 residual split, and the retained denominator must
        # lie in the natural Type I/II first-denominator window.
        self.assertIsNone(
            short_certificate.residual_split_descent_witness(73, 60, 4, spf)
        )
        self.assertIsNone(
            short_certificate.residual_split_descent_witness(73, 36, 3, spf)
        )

        # The e-parameterization is complete, not merely a source of the
        # successful examples above.  Compare it to direct enumeration of
        # every ordered two-term residual split for small n.
        for r in (1, 2, 3):
            split_numerator = 4 - r
            for n in range(r, 37, r):
                direct_pairs = set()
                for a in range(1, 2 * n // split_numerator + 1):
                    denominator = split_numerator * a - n
                    if denominator <= 0 or n * a % denominator:
                        continue
                    b = n * a // denominator
                    if a <= b:
                        direct_pairs.add((a, b))
                parameter_pairs = set()
                for factor in short_certificate.divisors_of_square(n, spf):
                    if factor > n:
                        continue
                    companion = n * n // factor
                    if (n + factor) % split_numerator or (
                        n + companion
                    ) % split_numerator:
                        continue
                    parameter_pairs.add(
                        (
                            (n + factor) // split_numerator,
                            (n + companion) // split_numerator,
                        )
                    )
                self.assertEqual(parameter_pairs, direct_pairs, (r, n))

    def test_even_standard_two_tail_descent(self):
        # These two cores were not covered by the earlier fixed-M and
        # residual-split families.  Here a standard even source retains one
        # large n while its other two terms are reassembled exactly.
        cases = (
            (21_169, 12_198, 342, (6_099, 12_198, 12_198),
             (12_198, 9_348, 7_057_998_628), ("I", 16_223, 9_348, 342)),
            (48_409, 27_764, 1_262, (13_882, 27_764, 27_764),
             (27_764, 21_454, 22_848_467_092), ("I", 37_407, 21_454, 1_262)),
        )
        spf = short_certificate.smallest_prime_factors(48_410)
        for (
            p,
            n,
            factor,
            source_solution,
            target_solution,
            expected_certificate,
        ) in cases:
            with self.subTest(p=p):
                witness = short_certificate.even_standard_two_tail_descent_witness(
                    p, n, spf
                )
                self.assertIsNotNone(witness)
                assert witness is not None
                self.assertEqual(witness.factor, factor)
                self.assertEqual(witness.source_solution, source_solution)
                self.assertEqual(witness.target_solution, target_solution)
                self.assertEqual(
                    (
                        witness.certificate.certificate_type,
                        witness.certificate.gap,
                        witness.certificate.x,
                        witness.certificate.divisor,
                    ),
                    expected_certificate,
                )
                self.assertGreater(3 * witness.certificate.gap, p)
                self.assertTrue(short_certificate.verify_certificate(witness.certificate))

        # The factor conditions enumerate every ordered u <= v tail for a
        # fixed p,n, before the natural-certificate filter is applied.
        p, n = 21_169, 12_198
        residual_numerator = 4 * n - p
        tail_denominator = n * p
        parameter_pairs = set()
        for factor in short_certificate.positive_divisors_square_product_from_spf(
            p, n, spf
        ):
            if factor > tail_denominator:
                continue
            companion = tail_denominator * tail_denominator // factor
            if (tail_denominator + factor) % residual_numerator or (
                tail_denominator + companion
            ) % residual_numerator:
                continue
            u = (tail_denominator + factor) // residual_numerator
            v = (tail_denominator + companion) // residual_numerator
            if u <= v:
                parameter_pairs.add((u, v))
        direct_pairs = set()
        for u in range(
            tail_denominator // residual_numerator + 1,
            2 * tail_denominator // residual_numerator + 1,
        ):
            denominator = residual_numerator * u - tail_denominator
            if denominator > 0 and tail_denominator * u % denominator == 0:
                v = tail_denominator * u // denominator
                if u <= v:
                    direct_pairs.add((u, v))
        self.assertEqual(parameter_pairs, direct_pairs)
        self.assertIn((9_348, 7_057_998_628), parameter_pairs)

        self.assertIsNone(
            short_certificate.even_standard_two_tail_descent_witness(21_169, 12_197, spf)
        )

    def test_three_divisible_standard_two_tail_descent(self):
        # Retaining one 2*n from the standard 3|n source changes two source
        # coordinates, so it is outside the known two-denominator obstruction.
        p, n = 8_329, 4_620
        spf = short_certificate.smallest_prime_factors(p + 1)
        witness = short_certificate.three_divisible_standard_two_tail_descent_witness(
            p, n, spf
        )
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(witness.factor, 168)
        self.assertEqual(witness.source_solution, (1_540, 9_240, 9_240))
        self.assertEqual(witness.target_solution, (9_240, 2_688, 1_231_359_360))
        self.assertEqual(
            (
                witness.certificate.certificate_type,
                witness.certificate.gap,
                witness.certificate.x,
                witness.certificate.divisor,
            ),
            ("I", 2_423, 2_688, 168),
        )
        self.assertLess(3 * witness.certificate.gap, p)
        self.assertTrue(short_certificate.verify_certificate(witness.certificate))

        # The factor form is complete for this fixed standard source.
        residual_numerator = 8 * n - p
        tail_denominator = 2 * n * p
        parameter_pairs = set()
        for factor in short_certificate.positive_divisors_square_factors_from_spf(
            (2, p, n), spf
        ):
            if factor > tail_denominator:
                continue
            companion = tail_denominator * tail_denominator // factor
            if (tail_denominator + factor) % residual_numerator or (
                tail_denominator + companion
            ) % residual_numerator:
                continue
            u = (tail_denominator + factor) // residual_numerator
            v = (tail_denominator + companion) // residual_numerator
            if u <= v:
                parameter_pairs.add((u, v))
        direct_pairs = set()
        for u in range(
            tail_denominator // residual_numerator + 1,
            2 * tail_denominator // residual_numerator + 1,
        ):
            denominator = residual_numerator * u - tail_denominator
            if denominator > 0 and tail_denominator * u % denominator == 0:
                v = tail_denominator * u // denominator
                if u <= v:
                    direct_pairs.add((u, v))
        self.assertEqual(parameter_pairs, direct_pairs)
        self.assertIn((2_688, 1_231_359_360), parameter_pairs)

        self.assertIsNone(
            short_certificate.three_divisible_standard_two_tail_descent_witness(
                p, n - 1, spf
            )
        )

    def test_standard_tail_descent_finite_audit(self):
        # This scans every permitted source, rather than only the displayed
        # witness examples. It records finite coverage of the two standard
        # large-tail families and leaves their joint misses visible.
        audit = short_certificate.standard_tail_descent_audit(5_000)
        self.assertEqual(audit["core_prime_count"], 76)
        self.assertEqual(audit["even_standard_hits"], 61)
        self.assertEqual(audit["three_divisible_standard_hits"], 41)
        self.assertEqual(audit["combined_hits"], 67)
        self.assertEqual(
            audit["combined_misses"],
            [73, 97, 193, 577, 601, 1_153, 1_801, 1_873, 4_801],
        )

    def test_affine_standard_tail_type_i_descent(self):
        # The even and three-divisible standard-tail branches share the same
        # affine Type I ray after x=a*t, y=b*t, and d=h*t.
        cases = (
            (21_169, 82, 107, 3, "even", 114,
             (6_099, 12_198, 12_198), (12_198, 9_348, 7_057_998_628),
             ("I", 16_223, 9_348, 342)),
            (8_329, 16, 55, 1, "three", 168,
             (1_540, 9_240, 9_240), (9_240, 2_688, 1_231_359_360),
             ("I", 2_423, 2_688, 168)),
        )
        for (
            p,
            a,
            b,
            h,
            source_kind,
            scale,
            source_solution,
            target_solution,
            expected_certificate,
        ) in cases:
            with self.subTest(p=p, source_kind=source_kind):
                witness = short_certificate.affine_standard_tail_type_i_witness(
                    p, a, b, h, source_kind
                )
                self.assertIsNotNone(witness)
                assert witness is not None
                self.assertEqual(witness.scale, scale)
                self.assertEqual(witness.source_solution, source_solution)
                self.assertEqual(witness.target_solution, target_solution)
                self.assertEqual(
                    (
                        witness.certificate.certificate_type,
                        witness.certificate.gap,
                        witness.certificate.x,
                        witness.certificate.divisor,
                    ),
                    expected_certificate,
                )
                self.assertTrue(short_certificate.verify_certificate(witness.certificate))

        self.assertIsNone(
            short_certificate.affine_standard_tail_type_i_witness(
                21_169, 82, 107, 3, "invalid"
            )
        )

    def test_four_external_source_descent_failure_has_residue_transversals(self):
        # For the four automatic k values, n is 1 modulo the prime q=4k-1.
        # If no -1 divisor exists, the observed factor residues occupy one
        # side of every r -> -1/r pairing.
        limit = 100_000
        spf = short_certificate.smallest_prime_factors(limit + 1)
        for k, q in ((1, 3), (2, 7), (3, 11), (6, 23)):
            units = set(range(1, q))
            for prime in short_certificate.primes_up_to(limit):
                if prime % 24 != 1:
                    continue
                witness = short_certificate.external_source_descent_witness(
                    prime, spf, k
                )
                if witness is not None:
                    continue
                source = (q * prime + 1) // (q + 1)
                self.assertEqual(source % q, 1, (prime, k))
                residues: set[int] = set()
                value = source
                while value > 1:
                    factor = spf[value]
                    residues.add(factor % q)
                    while value % factor == 0:
                        value //= factor
                self.assertTrue(residues <= units, (prime, k, residues))
                self.assertNotIn(q - 1, residues, (prime, k, residues))
                seen: set[int] = set()
                transversal: set[int] = set()
                for residue in units:
                    if residue in seen:
                        continue
                    complement = (-pow(residue, -1, q)) % q
                    self.assertNotEqual(residue, complement)
                    self.assertFalse(
                        residue in residues and complement in residues,
                        (prime, k, residue, complement, residues),
                    )
                    if residue in residues:
                        transversal.add(residue)
                    elif complement in residues:
                        transversal.add(complement)
                    elif residue == q - 1:
                        transversal.add(complement)
                    elif complement == q - 1:
                        transversal.add(residue)
                    else:
                        transversal.add(residue)
                    seen.update((residue, complement))
                self.assertEqual(seen, units)
                self.assertEqual(len(transversal), (q - 1) // 2)
                self.assertTrue(residues <= transversal, (prime, k, residues, transversal))

    def test_shifted_external_source_descent(self):
        limit = 100_000
        spf = short_certificate.smallest_prime_factors(limit + 1)
        examples = {
            (73, 1, 1): (55, 5, 7, 20, 80),
            (2_473, 7, 9): (2_385, 45, 47, 630, 11_340),
            (4_993, 7, 9): (4_815, 45, 47, 1_260, 45_360),
        }
        for (prime, k, shift), (source, factor, gap, x, divisor) in examples.items():
            witness = short_certificate.shifted_external_source_descent_witness(
                prime, k, shift, spf
            )
            self.assertIsNotNone(witness)
            assert witness is not None
            self.assertEqual((witness.source_denominator, witness.factor), (source, factor))
            certificate = witness.certificate
            self.assertEqual(
                (certificate.gap, certificate.x, certificate.divisor),
                (gap, x, divisor),
            )
            self.assertTrue(short_certificate.verify_certificate(certificate))
            self.assertEqual(
                short_certificate.Fraction(4, source),
                sum(
                    (short_certificate.Fraction(1, value) for value in witness.source_solution),
                    short_certificate.Fraction(),
                ),
            )
            self.assertEqual(
                short_certificate.Fraction(4, prime),
                sum(
                    (short_certificate.Fraction(1, value) for value in witness.target_solution),
                    short_certificate.Fraction(),
                ),
            )
            self.assertEqual(
                sorted(witness.target_solution),
                sorted((certificate.x, certificate.y, certificate.z)),
            )

        # For a fixed shifted ray, the routine is exact: it finds precisely
        # the factors whose complementary factor is -1 modulo q.
        k, shift = 7, 9
        q = 4 * k - 1
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1 or (prime - shift) % (4 * k):
                continue
            source = (q * prime + shift) // (q + 1)
            expected = (
                shift < prime
                and (k * source) % shift == 0
                and any(
                    (source // factor) % q == q - 1
                    for factor in short_certificate.positive_divisors_from_spf(source, spf)
                )
            )
            witness = short_certificate.shifted_external_source_descent_witness(
                prime, k, shift, spf
            )
            self.assertEqual(witness is not None, expected, prime)

        self.assertIsNone(
            short_certificate.shifted_external_source_descent_witness(97, 7, 9, spf)
        )

    def test_shifted_external_polynomial_ray(self):
        limit = 100_000
        spf = short_certificate.smallest_prime_factors(limit + 1)
        examples = (
            (1, 15, 2, (433, 4, 406, 14, 15)),
            (5, 15, 6, (31_849, 19, 31_430, 70, 71)),
            (13, 15, 2, (71_161, 49, 70_798, 182, 183)),
        )
        for shift, quotient, tail_index, expected in examples:
            with self.subTest(shift=shift, quotient=quotient, tail_index=tail_index):
                parameters = short_certificate.shifted_external_polynomial_ray_parameters(
                    shift, quotient, tail_index
                )
                self.assertEqual(parameters, expected)
                assert parameters is not None
                prime, k, source, factor, gap = parameters
                self.assertEqual(spf[prime], prime)
                witness = short_certificate.shifted_external_source_descent_witness(
                    prime, k, shift, spf
                )
                self.assertIsNotNone(witness)
                assert witness is not None
                self.assertEqual(
                    (witness.source_denominator, witness.factor, witness.certificate.gap),
                    (source, factor, gap),
                )
                self.assertEqual(
                    (witness.certificate.x, witness.certificate.divisor),
                    (
                        k * factor * tail_index,
                        shift * k * factor * tail_index * tail_index,
                    ),
                )

        # This core prime has the shifted d=5 witness above, but the complete
        # unshifted adaptive family finds no ray at all.
        self.assertIsNone(short_certificate.external_source_descent_witness(31_849, spf))
        self.assertIsNone(
            short_certificate.shifted_external_polynomial_ray_parameters(2, 3, 1)
        )

    def test_p_plus_four_type_ii_family(self):
        limit = 100_000
        spf = short_certificate.smallest_prime_factors(limit + 5)
        self.assertIsNotNone(short_certificate.p_plus_four_type_ii_certificate(73, spf))
        self.assertIsNone(short_certificate.p_plus_four_type_ii_certificate(97, spf))
        certificate = short_certificate.p_plus_four_type_ii_certificate(1129, spf)
        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertEqual((certificate.gap, certificate.divisor), (11, 1))
        self.assertTrue(short_certificate.verify_certificate(certificate))
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 == 1:
                certificate = short_certificate.p_plus_four_type_ii_certificate(prime, spf)
                if certificate is not None:
                    self.assertTrue(short_certificate.verify_certificate(certificate), prime)
                    self.assertLessEqual(certificate.gap * certificate.gap, prime + 4)

    def test_p_plus_eight_type_ii_family(self):
        limit = 6_300_000
        spf = short_certificate.smallest_prime_factors(limit + 9)
        self.assertIsNone(short_certificate.p_plus_eight_type_ii_certificate(73, spf))
        examples = {
            214_729: (6_927, 2),
            3_942_409: (55_527, 2),
            6_294_649: (3_767, 2),
        }
        for prime, (gap, divisor) in examples.items():
            certificate = short_certificate.p_plus_eight_type_ii_certificate(prime, spf)
            self.assertIsNotNone(certificate)
            assert certificate is not None
            self.assertEqual((certificate.gap, certificate.divisor), (gap, divisor))
            self.assertTrue(short_certificate.verify_certificate(certificate), prime)

    def test_four_p_plus_one_type_ii_family(self):
        self.assertIsNone(short_certificate.four_p_plus_one_type_ii_certificate(73, 7))
        certificate = short_certificate.four_p_plus_one_type_ii_certificate(313, 7)
        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertEqual((certificate.gap, certificate.x, certificate.divisor), (47, 90, 4))
        self.assertTrue(short_certificate.verify_certificate(certificate))
        certificate = short_certificate.four_p_plus_one_type_ii_certificate(1201, 31)
        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertEqual((certificate.gap, certificate.x, certificate.divisor), (47, 312, 64))
        self.assertTrue(short_certificate.verify_certificate(certificate))

        limit = 100_000
        spf = short_certificate.smallest_prime_factors(4 * limit + 1)
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            value = 4 * prime + 1
            candidate_q = None
            while value > 1:
                factor = spf[value]
                if factor % 4 == 3:
                    candidate_q = factor
                    break
                while value % factor == 0:
                    value //= factor
            if candidate_q is None:
                continue
            certificate = short_certificate.four_p_plus_one_type_ii_certificate(
                prime, candidate_q
            )
            self.assertIsNotNone(certificate, (prime, candidate_q))
            assert certificate is not None
            self.assertTrue(short_certificate.verify_certificate(certificate), prime)

    def test_external_source_type_i_family(self):
        self.assertIsNone(short_certificate.external_source_type_i_certificate(193, 2, 35))
        certificate = short_certificate.external_source_type_i_certificate(193, 2, 39)
        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertEqual((certificate.gap, certificate.x, certificate.divisor), (39, 58, 116))
        self.assertTrue(short_certificate.verify_certificate(certificate))
        certificate = short_certificate.external_source_type_i_certificate(73, 4, 7)
        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertEqual((certificate.gap, certificate.x, certificate.divisor), (7, 20, 80))
        self.assertTrue(short_certificate.verify_certificate(certificate))

        limit = 10_000
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            for source in range(1, 33):
                for gap in range(3, prime - 1, 4):
                    if (prime + source) % gap or (prime + gap) % (4 * source):
                        continue
                    certificate = short_certificate.external_source_type_i_certificate(
                        prime, source, gap
                    )
                    self.assertIsNotNone(certificate, (prime, source, gap))
                    assert certificate is not None
                    self.assertTrue(short_certificate.verify_certificate(certificate), prime)

    def test_coprime_external_source_tail_deflation_criterion(self):
        # For an external certificate with coprime (source, gap), the
        # general normal-tail selector reduces to q+1 | (gap+1)(source+1).
        limit = 10_000
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            for source in range(1, 33):
                for gap in range(3, prime - 1, 4):
                    certificate = short_certificate.external_source_type_i_certificate(
                        prime, source, gap
                    )
                    if certificate is None or math.gcd(source, gap) != 1:
                        continue
                    A = (prime + gap) // (4 * source)
                    B = (prime + source) // gap
                    q = (B + 1) // source
                    self.assertEqual((4 * A + 1) // gap, q)
                    self.assertEqual(4 * A + 1, gap * q)
                    expected = ((gap + 1) * (source + 1)) % (q + 1) == 0
                    witness = short_certificate.type_i_normal_tail_deflation_witness(
                        prime, gap, source, 1
                    )
                    self.assertEqual(witness is not None, expected, (prime, source, gap))
                    if witness is not None:
                        self.assertEqual(witness.source_solution, (source * A, source * A * B, A * B))
                        self.assertEqual(witness.source_denominator, 4 * A * B // (q + 1))

        prime, source, gap = 477_015_289, 29, 27
        A = (prime + gap) // (4 * source)
        B = (prime + source) // gap
        q = (B + 1) // source
        self.assertEqual((A, B, q), (4_112_201, 17_667_234, 609_215))
        self.assertNotEqual(((gap + 1) * (source + 1)) % (q + 1), 0)
        self.assertIsNone(
            short_certificate.type_i_normal_tail_deflation_witness(prime, gap, source, 1)
        )

    def test_external_source_exactly_matches_x_multiple_type_i_divisors(self):
        limit = 10_000
        spf = short_certificate.smallest_prime_factors((limit + 107) // 4 + 1)
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            for gap in range(3, min(107, prime - 2) + 1, 4):
                x = (prime + gap) // 4
                for divisor in short_certificate.divisors_of_square(x, spf):
                    if divisor % x or (prime * x + divisor) % gap:
                        continue
                    certificate = short_certificate.external_source_type_i_certificate(
                        prime, divisor // x, gap
                    )
                    self.assertIsNotNone(certificate, (prime, gap, divisor))
                    assert certificate is not None
                    self.assertTrue(short_certificate.verify_certificate(certificate), prime)

    def test_type_i_coprime_factor_normal_form(self):
        limit = 10_000
        spf = short_certificate.smallest_prime_factors((limit + 107) // 4 + 1)
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            for gap in range(3, min(107, prime - 2) + 1, 4):
                x = (prime + gap) // 4
                for divisor in short_certificate.divisors_of_square(x, spf):
                    if (prime * x + divisor) % gap:
                        continue
                    normal_form = short_certificate.type_i_normal_form(prime, gap, divisor)
                    self.assertIsNotNone(normal_form, (prime, gap, divisor))
                    assert normal_form is not None
                    a, b, c = normal_form
                    self.assertEqual((x, divisor), (a * b * c, a * a * c))
                    self.assertEqual(math.gcd(a, b), 1)
                    # In normalized Elsholtz--Tao coordinates, (a_ET, c_ET,
                    # d_ET, f) = (b, a, c, gap).
                    self.assertEqual((4 * b * b * c + 1) % gap, 0)
                    self.assertEqual(prime, 4 * b * a * c - gap)
                    certificate = short_certificate.type_i_normal_form_certificate(
                        prime, gap, a, b
                    )
                    self.assertIsNotNone(certificate, (prime, gap, normal_form))
                    assert certificate is not None
                    self.assertEqual(certificate.divisor, divisor)
                    self.assertTrue(short_certificate.verify_certificate(certificate), prime)
                    target_divisor = x * x // divisor
                    self.assertEqual(
                        short_certificate.type_i_normal_form_from_target_divisor(
                            prime, gap, target_divisor
                        ),
                        normal_form,
                    )
                    self.assertEqual(
                        short_certificate.target_divisor_overflow_factor(
                            x, target_divisor
                        ),
                        b,
                    )
                    self.assertEqual(target_divisor, b * b * c)

    def test_target_divisor_overflow_one_private_factor_formula(self):
        for fixed_part, private_prime, exponent in (
            (12, 5, 1),
            (12, 5, 3),
            (45, 2, 2),
            (77, 3, 2),
        ):
            self.assertEqual(math.gcd(fixed_part, private_prime), 1)
            x = fixed_part * private_prime**exponent
            for fixed_divisor in short_certificate.divisors_of_square(
                fixed_part, short_certificate.smallest_prime_factors(fixed_part + 1)
            ):
                for private_exponent in range(2 * exponent + 1):
                    target_divisor = fixed_divisor * private_prime**private_exponent
                    expected = (
                        fixed_divisor // math.gcd(fixed_divisor, fixed_part)
                    ) * private_prime ** max(private_exponent - exponent, 0)
                    self.assertEqual(
                        short_certificate.target_divisor_overflow_factor(
                            x, target_divisor
                        ),
                        expected,
                    )

    def test_type_i_normal_tail_deflation(self):
        witness = short_certificate.type_i_normal_tail_deflation_witness(73, 7, 4, 1)
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(witness.source_denominator, 55)
        self.assertEqual(witness.quotient, 3)
        self.assertEqual(witness.source_solution, (20, 220, 55))
        self.assertEqual(witness.target_solution, (20, 220, 4015))
        self.assertIsNone(
            short_certificate.type_i_normal_tail_deflation_witness(
                1_282_009, 71, 5, 2
            )
        )

    def test_type_ii_coprime_factor_normal_form(self):
        limit = 10_000
        spf = short_certificate.smallest_prime_factors((limit + 107) // 4 + 1)
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            for gap in range(3, min(107, prime - 2) + 1, 4):
                x = (prime + gap) // 4
                for divisor in short_certificate.divisors_of_square(x, spf):
                    if divisor > x or (x + divisor) % gap:
                        continue
                    normal_form = short_certificate.type_ii_normal_form(prime, gap, divisor)
                    self.assertIsNotNone(normal_form, (prime, gap, divisor))
                    assert normal_form is not None
                    a, b, c = normal_form
                    self.assertEqual((x, divisor), (a * b * c, a * a * c))
                    self.assertEqual(math.gcd(a, b), 1)
                    self.assertLessEqual(a, b)
                    self.assertEqual((a + b) % gap, 0)
                    k = (a + b) // gap
                    self.assertEqual(
                        (4 * a * c * k - 1) * (4 * b - 1),
                        4 * k * prime + 1 - 4 * a * (c * k - 1),
                    )
                    certificate = short_certificate.type_ii_normal_form_certificate(
                        prime, gap, a, b
                    )
                    self.assertIsNotNone(certificate, (prime, gap, normal_form))
                    assert certificate is not None
                    self.assertEqual(certificate.divisor, divisor)
                    self.assertTrue(short_certificate.verify_certificate(certificate), prime)
                    # Xu-tame is exactly the K=1 Type II slice: the two
                    # non-leading denominators divide p*x precisely then.
                    self.assertEqual(certificate.y, prime * a * c * k)
                    self.assertEqual(certificate.z, prime * b * c * k)
                    self.assertEqual(math.gcd(k, a), 1)
                    self.assertEqual(math.gcd(k, b), 1)
                    tame = (prime * x) % certificate.y == 0 and (prime * x) % certificate.z == 0
                    self.assertEqual(tame, k == 1)
                    for multiplier in range(1, k + 1):
                        both_divide_scaled = (
                            (multiplier * prime * x) % certificate.y == 0
                            and (multiplier * prime * x) % certificate.z == 0
                        )
                        self.assertEqual(both_divide_scaled, multiplier == k)
                    if k == 1:
                        self.assertEqual(
                            sorted(((prime * x) // certificate.y, (prime * x) // certificate.z)),
                            [a, b],
                        )
                        self.assertEqual((prime * x) // certificate.y + (prime * x) // certificate.z, gap)

    def test_type_ii_factor_generator_is_exact(self):
        limit = 10_000
        spf = short_certificate.smallest_prime_factors((limit + 107) // 4 + 1)
        for prime in short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            for gap in range(3, min(107, prime - 2) + 1, 4):
                x = (prime + gap) // 4
                for divisor in short_certificate.divisors_of_square(x, spf):
                    if divisor > x or (x + divisor) % gap:
                        continue
                    normal_form = short_certificate.type_ii_normal_form(prime, gap, divisor)
                    self.assertIsNotNone(normal_form, (prime, gap, divisor))
                    assert normal_form is not None
                    a, b, c = normal_form
                    k = (a + b) // gap
                    self.assertEqual(4 * a * c * k - 1, (k * prime + a) // b)
                    certificate = short_certificate.type_ii_factor_certificate(prime, a, c, k)
                    self.assertIsNotNone(certificate, (prime, gap, normal_form, k))
                    assert certificate is not None
                    self.assertEqual((certificate.gap, certificate.divisor), (gap, divisor))
                    self.assertTrue(short_certificate.verify_certificate(certificate), prime)

    def test_type_ii_raw_ray_allows_redundant_non_coprime_coordinates(self):
        # This raw ray witness is valid but not in the unique coprime normal
        # form: gcd(2, 40)=2. It normalizes to different A,B,C coordinates.
        certificate = short_certificate.type_ii_raw_ray_certificate(313, 2, 1, 6)
        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertEqual(
            (certificate.gap, certificate.x, certificate.divisor),
            (7, 80, 4),
        )
        self.assertTrue(short_certificate.verify_certificate(certificate))
        self.assertIsNone(short_certificate.type_ii_factor_certificate(313, 2, 1, 6))

    def test_finite_type_ii_factor_templates_have_an_avoiding_core_residue(self):
        templates = [(1, 1, 1), (1, 2, 5), (2, 2, 7), (5, 5, 7)]
        modulus = short_certificate.type_ii_factor_template_avoidance_modulus(templates)
        self.assertEqual(modulus % 24, 0)
        candidate = modulus + 1
        self.assertEqual(candidate % 24, 1)
        for a, c, k in templates:
            factor = 4 * a * c * k - 1
            self.assertGreater(factor, k + a)
            self.assertNotEqual((k * candidate + a) % factor, 0)
            self.assertIsNone(short_certificate.type_ii_factor_certificate(candidate, a, c, k))
        with self.assertRaises(ValueError):
            short_certificate.type_ii_factor_template_avoidance_modulus([(0, 1, 1)])

    def test_finite_small_gap_inventory(self):
        result = short_certificate.run_experiment(10_000, 1_023)
        self.assertEqual(result["uncertified_within_gap_limit"], [])
        self.assertEqual(result["certified_count"], result["core_prime_count"])


if __name__ == "__main__":
    unittest.main()
