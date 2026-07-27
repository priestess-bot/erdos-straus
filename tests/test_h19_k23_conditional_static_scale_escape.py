import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_conditional_static_scale_escape",
    ROOT / "reproductions" / "h19_k23_conditional_static_scale_escape.py",
)
assert SPEC and SPEC.loader
escape = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = escape
SPEC.loader.exec_module(escape)


class H19K23ConditionalStaticScaleEscapeTests(unittest.TestCase):
    def test_every_post_affine_state_is_admissible_and_staticly_empty(self):
        result = escape.run_audit()
        self.assertEqual(result["state_count"], 14)
        self.assertEqual(result["h19_private_form_count_per_state"], 20)
        self.assertEqual(result["stationary_source_count_per_state"], 37)
        self.assertEqual(result["combined_form_count_per_state"], 57)
        self.assertTrue(
            all(
                state["covering_primes"] == []
                and not state["h19_ray_certificate"]
                and state["complete_square_tail_source_hits"] == 0
                and len(state["sources"]) == 37
                for state in result["states"]
            )
        )

    def test_checked_artifact(self):
        with (
            ROOT / "reproductions" / "h19-k23-conditional-static-scale-escape.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["state_count"], 14)
        self.assertEqual(result["combined_form_count_per_state"], 57)


if __name__ == "__main__":
    unittest.main()
