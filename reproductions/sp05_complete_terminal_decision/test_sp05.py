#!/usr/bin/env python3
from __future__ import annotations

import copy
import unittest
from math import gcd, isqrt

import sp05_contract as C
import sp05_constructor as P
import sp05_independent_replayer as R


def direct_sorted_solution(p: int):
    """Independent finite y-scan for the sorted solution domain."""
    for x in range(p // 4 + 1, (3 * p) // 4 + 1):
        num = 4 * x - p
        den = p * x
        g = gcd(num, den)
        a, b = num // g, den // g
        y_min = b // a + 1
        y_max = (2 * b) // a
        for y in range(max(x, y_min), y_max + 1):
            q = a * y - b
            if q <= 0:
                continue
            z_num = b * y
            if z_num % q:
                continue
            z = z_num // q
            if y <= z and P.verify_egyptian(p, (x, y, z)):
                return (x, y, z)
    return None


def simple_primes(limit: int):
    values = []
    for n in range(2, limit + 1):
        if all(n % d for d in range(2, isqrt(n) + 1)):
            values.append(n)
    return values


class SP05ProofPackageTests(unittest.TestCase):
    def test_complete_factor_pair_search_matches_independent_y_scan(self):
        # This is a focused executable check of the coverage theorem; the
        # mathematical proof in SP-05-complete-proof.md is the authority.
        for p in simple_primes(1000):
            with self.subTest(p=p):
                expected = direct_sorted_solution(p)
                actual = P.complete_factor_pair_search(p)
                self.assertEqual(actual["outcome"], "HIT" if expected else "MISS_COMPLETE")
                if expected:
                    self.assertEqual(tuple(actual["certificate"]["denominators"]), expected)

    def test_p21169_registered_prefix_miss_but_global_hit(self):
        p = 21169
        params = P.ordinary_q1_g_parameters(p)
        self.assertEqual(params["t"], 882)
        self.assertEqual(params["X"], 5293)
        self.assertEqual(params["X_factorization"], [[67, 1], [79, 1]])

        prefix = P.bradford_m23_prefix(p)
        self.assertEqual(prefix["outcome"], "MISS_REGISTERED_PRIORITY_COMPLETE")
        self.assertEqual(prefix["divisor_positions"], 102)
        self.assertEqual(prefix["checks"], 204)

        global_result = P.complete_factor_pair_search(p)
        self.assertEqual(global_result["outcome"], "HIT")
        self.assertEqual(
            global_result["certificate"]["denominators"],
            [5300, 3619899, 19185464700],
        )
        self.assertTrue(P.verify_egyptian(p, global_result["certificate"]["denominators"]))

        # Explicit gap-31, d=1 Type-II control.
        gap31 = P._bradford_certificate(p, 31, 1, "TYPEII")
        self.assertEqual(gap31["denominators"], [5300, 3619899, 19185464700])

    def test_m23_earliest_controls(self):
        controls = {
            73: (7, 1, "TYPEII"),
            241441: (11, 27, "TYPEII"),
            2689: (15, 26, "TYPEI"),
            12721: (19, 7, "TYPEII"),
            1201: (23, 34, "TYPEI"),
            2521: (23, 8, "TYPEII"),
        }
        for p, expected in controls.items():
            with self.subTest(p=p):
                result = P.bradford_m23_prefix(p)
                cert = result["certificate"]
                self.assertEqual(result["outcome"], "HIT")
                self.assertEqual((cert["gap"], cert["divisor"], cert["certificate_kind"]), expected)
                self.assertTrue(P.verify_egyptian(p, cert["denominators"]))

    def test_source_decision_and_independent_replay(self):
        source = C.make_reference_root_state(21169)
        decision = P.complete_source_terminal_decision(source)
        self.assertEqual(decision["outcome"], "HIT")
        replay = R.replay_source_decision(source, decision)
        self.assertTrue(replay["accepted"])

    def test_target_terminal_replay_is_independent_and_preemptive(self):
        source = C.make_reference_root_state(21169)
        projection = C.phase_projection(21169)
        decision = P.complete_target_terminal_decision(source, projection)
        self.assertEqual(decision["outcome"], "HIT")
        self.assertEqual(decision["hit_family"], "P_ONLY_COMPLETE_SCHEDULE")
        self.assertEqual(decision["anchor_result"]["outcome"], "NOT_REACHED")
        replay = R.replay_target_decision(source, P.projection_mapping(projection), decision)
        self.assertTrue(replay["accepted"])

    def test_phase_projection_anchor_and_t5(self):
        for p in (1201, 2521, 21169):
            with self.subTest(p=p):
                projection = C.phase_projection(p)
                self.assertEqual(4 * projection.K, p * projection.R + 1)
                self.assertEqual(gcd(projection.R - 1, projection.K), 1)
                source_vec = C.source_potential(p)
                target_vec = C.target_potential(p)
                C.verify_phase_drop(p, source_vec, target_vec)
                self.assertEqual(source_vec[0], target_vec[0])
                self.assertLess(target_vec[1], source_vec[1])

    def test_reference_fixture_cannot_supply_actualness(self):
        source = C.make_reference_root_state(21169)
        actualness = P.make_reference_actualness_receipt(source)
        with self.assertRaises(P.ConstructorError):
            P.verify_actualness_receipt(source, actualness)
        with self.assertRaises(P.ConstructorError):
            P.select(source, actualness)

    def test_forged_nonzero_actualness_still_rejected(self):
        source = C.make_reference_root_state(21169)
        forged = P.make_reference_actualness_receipt(source)
        forged["authority_class"] = "EXACT_HEAD_V5_V6_ACTUAL_SOURCE"
        forged["v5_admission_receipt_id"] = "forged-v5"
        forged["v5_admission_receipt_digest"] = "a" * 64
        forged["v6_rebind_receipt_id"] = "forged-v6"
        forged["v6_rebind_receipt_digest"] = "b" * 64
        forged = C.seal(forged)
        with self.assertRaisesRegex(P.ConstructorError, "NO_EXTERNAL_ACTUALNESS_AUTHORITY"):
            P.verify_actualness_receipt(source, forged)
        with self.assertRaisesRegex(R.ReplayError, "NO_EXTERNAL_ACTUALNESS_AUTHORITY"):
            R.replay_actualness(source, forged)

    def test_bool_and_float_cannot_alias_q_one_source_field(self):
        for bad_q in (True, 1.0):
            with self.subTest(bad_q=bad_q):
                source = copy.deepcopy(C.make_reference_root_state(21169))
                source["facts"]["relation_q"] = bad_q
                source["source_receipt"]["target_facts_digest"] = C.canonical_digest(
                    source["facts"]
                )
                source["source_receipt"] = C.seal(source["source_receipt"])
                source["state_id"] = C.build_state_id(source)
                with self.assertRaises(C.ContractError):
                    C.validate_root_state_shape(source)
                with self.assertRaises(R.ReplayError):
                    R.validate_source_state(source)

    def test_fake_miss_complete_is_rejected(self):
        source = C.make_reference_root_state(21169)
        decision = P.complete_source_terminal_decision(source)
        forged = copy.deepcopy(decision)
        forged["outcome"] = "MISS_COMPLETE"
        forged["certificate"] = None
        forged = C.seal(forged)
        with self.assertRaises(R.ReplayError):
            R.replay_source_decision(source, forged)

    def test_source_swap_q_path_and_projection_tie_break_controls(self):
        source = C.make_reference_root_state(21169)
        actualness = P.make_reference_actualness_receipt(source)

        q_swap = copy.deepcopy(actualness)
        q_swap["authority_class"] = "EXACT_HEAD_V5_V6_ACTUAL_SOURCE"
        q_swap["v5_admission_receipt_digest"] = "1" * 64
        q_swap["v6_rebind_receipt_digest"] = "2" * 64
        q_swap["occurrence_path"] = ["facts", "t5_eta_p"]
        q_swap = C.seal(q_swap)
        with self.assertRaises(P.ConstructorError):
            P.verify_actualness_receipt(source, q_swap)

        projection = P.projection_mapping(C.phase_projection(21169))
        tie_break = copy.deepcopy(projection)
        tie_break["R"] += 4
        tie_break["K"] += 21169
        with self.assertRaises(R.ReplayError):
            R.validate_projection(21169, tie_break)

        source_swap = C.make_reference_root_state(1201)
        target_shape = C.make_successor_state(
            source_state=source,
            complete_source_miss_digest="3" * 64,
            complete_target_miss_digest="4" * 64,
        )
        with self.assertRaises(C.ContractError):
            C.validate_successor_state_shape(target_shape, source_swap)

    def test_target_terminal_subject_swap_and_t5_drift_controls(self):
        source = C.make_reference_root_state(21169)
        source_decision = P.complete_source_terminal_decision(source)
        projection = P.projection_mapping(C.phase_projection(21169))
        with self.assertRaises(R.ReplayError):
            R.replay_target_decision(source, projection, source_decision)

        target = list(C.target_potential(21169))
        target[1] = 3
        with self.assertRaises(R.ReplayError):
            R.validate_t5(21169, C.source_potential(21169), target)

    def test_shape_only_reentry_requires_registered_owner(self):
        source = C.make_reference_root_state(21169)
        target = C.make_successor_state(
            source_state=source,
            complete_source_miss_digest="5" * 64,
            complete_target_miss_digest="6" * 64,
        )
        registration = C.make_reentry_registration()
        receipt = C.verify_reentry(target, registration)
        self.assertEqual(receipt["outcome"], "PHASE_BODY_ENTERED")

        bad = copy.deepcopy(registration)
        bad["source_owners"] = [C.SOURCE_OWNER]
        bad = C.seal(bad)
        with self.assertRaises(C.ContractError):
            C.verify_reentry(target, bad)


if __name__ == "__main__":
    unittest.main(verbosity=2)
