import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_global_tail_finite_support_menu_obstruction",
    ROOT / "reproductions" / "h19_k23_global_tail_finite_support_menu_obstruction.py",
)
assert SPEC and SPEC.loader
obstruction = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = obstruction
SPEC.loader.exec_module(obstruction)


class H19K23GlobalTailFiniteSupportMenuObstructionTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_base_obstruction_input(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-base-only-prime-obstruction-2097152.json"
        ).open(encoding="utf-8") as handle:
            base = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-finite-support-menu-obstruction-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(obstruction.run_audit(base), checked)

    def test_mixed_menu_has_no_raw_divisor_from_its_full_nonbase_support(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-finite-support-menu-obstruction-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["global_tail_count"], 72)
        self.assertEqual(result["seed_prime"], 955_643_834_512_728_001)
        self.assertEqual(result["prime_progression_gcd"], 1)
        self.assertEqual(result["core_prime_residue_mod_24"], 1)
        self.assertIn(87_060_409_452_631, result["menu_primes"])
        self.assertEqual(
            {row["mode"] for row in result["local_avoidance"]},
            {"frozen-support", "crt-avoided"},
        )


if __name__ == "__main__":
    unittest.main()
