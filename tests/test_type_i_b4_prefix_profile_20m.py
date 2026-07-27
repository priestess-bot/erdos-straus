import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TypeIBFourPrefixProfile20MTests(unittest.TestCase):
    def test_checked_twenty_million_summary(self):
        result = json.loads(
            (ROOT / "reproductions" / "type-i-b4-prefix-profile-20m-results.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(
            (result["prime_limit"], result["b_cap"], result["core_prime_count"], result["captured_count"]),
            (20_000_017, 4, 158_595, 158_594),
        )
        self.assertEqual((result["misses"], result["first_miss"]), ([21169], 21169))


if __name__ == "__main__":
    unittest.main()
