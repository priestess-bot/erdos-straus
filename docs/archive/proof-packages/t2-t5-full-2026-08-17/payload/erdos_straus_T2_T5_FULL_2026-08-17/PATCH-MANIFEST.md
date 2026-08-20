# Proposed repository patch manifest

## T2 additions

Copy preserving paths:

- `T2_atomic_admission_v1/claims/type-I-atomic-admission-v1-finite-grammar-integration.md`
  -> `claims/type-I-atomic-admission-v1-finite-grammar-integration.md`
- `T2_atomic_admission_v1/claims/type-I-edge-local-atomic-ownership-sufficiency.md`
  -> `claims/type-I-edge-local-atomic-ownership-sufficiency.md`
- `T2_atomic_admission_v1/docs/T2-atomic-admission-v1-integration.md`
  -> `docs/T2-atomic-admission-v1-integration.md`
- `T2_atomic_admission_v1/reproductions/type_i_atomic_admission_v1_contract.py`
  -> `reproductions/type_i_atomic_admission_v1_contract.py`

## FULL T5 additions

- `T5_global_well_foundedness_full/concepts/t5-global-well-foundedness-contract-v2.md`
  -> `concepts/t5-global-well-foundedness-contract-v2.md`
- `T5_global_well_foundedness_full/claims/type-I-t5-full-contract-level-global-well-foundedness.md`
  -> `claims/type-I-t5-full-contract-level-global-well-foundedness.md`
- `T5_global_well_foundedness_full/claims/type-I-t5-full-transition-surface-exhaustion.md`
  -> `claims/type-I-t5-full-transition-surface-exhaustion.md`
- `T5_global_well_foundedness_full/data/t5-full-phase-registry-v2.json`
  -> `data/t5-full-phase-registry-v2.json`
- `T5_global_well_foundedness_full/data/t5-full-transition-taxonomy-v2.json`
  -> `data/t5-full-transition-taxonomy-v2.json`
- `T5_global_well_foundedness_full/reproductions/type_i_t5_full_global_well_foundedness.py`
  -> `reproductions/type_i_t5_full_global_well_foundedness.py`
- `T5_global_well_foundedness_full/reproductions/type_i_t5_transition_surface_audit.py`
  -> `reproductions/type_i_t5_transition_surface_audit.py`
- `T5_global_well_foundedness_full/docs/T5-full-global-well-foundedness-integration.md`
  -> `docs/T5-full-global-well-foundedness-integration.md`

Apply:

- `T5_global_well_foundedness_full/patches/denominator-escape-state-contract.T5-full-v2.patch`

or manually merge its new section 6.9 into `concepts/denominator-escape-state-contract.md`.

## Required merge checks

1. Run `python scripts/kb.py validate` and `python scripts/kb.py build` in the actual repository.
2. Run the source-specific existing verifiers for q-shadow, q=1 root/c3 relay, support/overflow, d=1,
   high-support macros, H4 and c=8.
3. Run both T2/T5 focused verifier scripts from this bundle.
4. Do not change T6/ESC status as a consequence of this patch.
5. Retire `REGISTERED_EDGE_SCHEDULE_CLOSED` as the final T5 wording; keep it only as historical v1.
6. Future persistent edges must satisfy the canonical T5 ticket rule.  Do not expand T5 by ad-hoc
   per-edge potentials.
