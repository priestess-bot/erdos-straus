# H4 clean q-bridge patch verification results

Date: 2026-08-17

Commands executed in the release directory:

```bash
python -m unittest tests.test_type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier -v
python reproductions/type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py --verify-controls
```

Unit-test result:

```text
test_control_multiplier_matches_existing_known_values ... ok
test_corrected_single_side_formula_absorbs_y_block ... ok
test_existing_control_fixtures_pass_e1_e5 ... ok
test_priority_miss_is_a_real_premise ... ok
test_receipt_is_deterministic ... ok
test_target_type_label_is_not_inherited ... ok

Ran 6 tests
OK
```

Control summary:

| fixture | p | q | branch | M_target | capacity | E1–E5 |
| --- | ---: | ---: | --- | ---: | ---: | --- |
| p73 | 73 | 37 | atomic_split | 3559956824877628 | 24 | all true |
| p241 | 241 | 121 | atomic_split | 92255470189779250300 | 80 | all true |

These controls are regression fixtures for local arithmetic and serialization only. They do not independently establish upstream 19-phase H4 provenance and do not replace the universal stutter-closure dependency.
