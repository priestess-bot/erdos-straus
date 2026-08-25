from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT / "reproductions" / "type_i_f2_high_support_c1_r_three_hard_core_partition.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location("r_three_hard_core_partition", MODULE_PATH)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot import {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PARTITION = load_module()


class RThreeHardCorePartitionTests(unittest.TestCase):
    def test_character_and_modulo_twenty_four_partitions(self) -> None:
        PARTITION.check_character_and_parity_partitions()

    def test_hard_core_control_misses_all_p_divisor_mixed_gaps(self) -> None:
        PARTITION.check_hard_core_control_and_mixed_gap_misses()


if __name__ == "__main__":
    unittest.main()
