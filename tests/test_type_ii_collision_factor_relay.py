import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_collision_factor_relay",
    ROOT / "reproductions" / "type_ii_collision_factor_relay.py",
)
assert SPEC and SPEC.loader
relay = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = relay
SPEC.loader.exec_module(relay)


class TypeIICollisionFactorRelayTests(unittest.TestCase):
    def test_factor_congruence_enumerates_the_canonical_target(self):
        smallest_factors = relay.canonical.ray.short_certificate.smallest_prime_factors(
            2 * 3_361 + 4 * 14
        )
        self.assertIn(
            (125, 5, 5),
            relay.canonical_targets_for_factor(99, 3_361, smallest_factors),
        )

    def test_record_residual_has_a_source_labelled_relay(self):
        smallest_factors = relay.canonical.ray.short_certificate.smallest_prime_factors(
            2 * 3_361 + 4 * 14
        )
        profile = relay.relay_for_prime(3_361, 14, smallest_factors)
        self.assertEqual(profile["relay_count"], 1)
        self.assertEqual(
            profile["relays"][0],
            {
                "h": 99,
                "h_factorization": [
                    {"prime": 3, "exponent": 2},
                    {"prime": 11, "exponent": 1},
                ],
                "shift": 125,
                "a": 5,
                "c": 5,
                "k": 1,
                "gap": 39,
                "divisor": 125,
                "source_labels": [
                    {"prime": 3, "exponent": 2, "source_shifts": [8]},
                    {"prime": 11, "exponent": 1, "source_shifts": [4]},
                ],
            },
        )

    def test_small_h14_audit_has_twelve_relays(self):
        result = relay.run_audit(1_000_000, 14)
        self.assertEqual(result["common_failure_count"], 24)
        self.assertEqual(result["relayed_count"], 12)
        self.assertEqual(result["unrelayed_count"], 12)
        self.assertEqual(
            result["unrelayed_primes"],
            [
                92_569,
                176_089,
                176_401,
                197_521,
                225_289,
                319_321,
                345_601,
                465_721,
                600_961,
                806_521,
                813_121,
                868_849,
            ],
        )

    def test_first_descent_escape_has_no_h14_closure_relay(self):
        result = relay.run_single_prime(2_451_289, 14)
        profile = result["profile"]
        self.assertEqual(profile["closure_value"], 23_423_400)
        self.assertEqual(profile["closure_divisor_count_at_most_2p"], 428)
        self.assertEqual(profile["relay_count"], 0)

    def test_checked_h19_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-collision-factor-relay-h19-10m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 10_000_000)
        self.assertEqual(result["base_shift_bound"], 19)
        self.assertEqual(result["common_failure_count"], 45)
        self.assertEqual(result["relayed_count"], 25)
        self.assertEqual(result["unrelayed_count"], 20)

    def test_checked_h19_one_private_source_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-collision-plus-one-private-relay-h19-10m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["private_source_prime_budget"], 1)
        self.assertEqual(result["relayed_count"], 39)
        self.assertEqual(result["unrelayed_count"], 6)

    def test_checked_h19_two_private_source_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-collision-plus-two-private-relay-h19-10m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["private_source_prime_budget"], 2)
        self.assertEqual(result["relayed_count"], 40)
        self.assertEqual(
            result["unrelayed_primes"],
            [225_289, 2_031_121, 3_569_329, 3_660_721, 7_378_849],
        )

    def test_two_private_sources_still_miss_225289(self):
        result = relay.run_single_prime(225_289, 19, 2)
        profile = result["profile"]
        self.assertEqual(profile["candidate_factor_count_at_most_2p"], 7_885)
        self.assertEqual(profile["relay_count"], 0)

    def test_checked_h19_three_private_source_residual_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-collision-plus-three-private-relay-h19-10m-residual-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["private_source_prime_budget"], 3)
        self.assertEqual(result["relayed_count"], 0)
        self.assertEqual(
            result["unrelayed_primes"],
            [225_289, 2_031_121, 3_569_329, 3_660_721, 7_378_849],
        )
        self.assertEqual(
            result["profiles"][0]["candidate_factor_count_at_most_2p"], 8_185
        )

    def test_225289_first_later_certificate_uses_a_new_fan_factor(self):
        prime = 225_289
        smallest_factors = relay.canonical.ray.short_certificate.smallest_prime_factors(
            prime + 4 * 32
        )
        pair = relay.canonical.canonical_pair(32)
        witness = relay.canonical.witness_for_pair(prime, pair, smallest_factors)
        self.assertIsNotNone(witness)
        self.assertEqual(witness["h"], 2_591)
        self.assertEqual(
            relay.factorization_dict(witness["h"], smallest_factors), {2_591: 1}
        )
        pairs = tuple(
            relay.canonical.canonical_pair(shift) for shift in range(1, 20)
        )
        collision_set = set(relay.collision.collision_primes(tuple(range(1, 20))))
        sources = relay.private_source_factors(
            prime, pairs, smallest_factors, collision_set
        )
        self.assertNotIn(2_591, sources)


if __name__ == "__main__":
    unittest.main()
