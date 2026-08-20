# H4 clean q-bridge corrected E1–E5 closure patch

This package closes the **relative** H4 clean-q macro, assuming the existing upstream actual-H4 provenance receipt and a versioned earlier-priority miss receipt.

It contains:

- a complete proof document: `H4_CLEAN_Q_E1_E5_COMPLETE_PROOF.md`;
- a new theorem card: `claims/type-II-q-one-c-two-19-phase-h4-clean-q-e1-e5-relative-macro-closure.md`;
- a generic local E1–E5 verifier/serializer;
- focused unit tests;
- the correction `M_q=lcm(M_4,Q_x,Q_y)` for the old clean-raw-bridge card;
- a state-contract amendment defining safe lazy `pending_dispatch` normalization;
- a reproduction README addition;
- a 2026-08-17 frontier note;
- CI additions for the new test and verifier.

## Apply

From outside a current checkout:

```bash
python h4_closure_patch/apply_h4_closure.py /path/to/erdos-straus
```

Then inside the repository:

```bash
python scripts/kb.py validate
python -m unittest tests.test_type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier -v
python reproductions/type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py --verify-controls
python scripts/kb.py build
git diff --check
```

If Ruff is available, also run:

```bash
ruff check \
  reproductions/type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py \
  tests/test_type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py
```

## Proof boundary

The new theorem is intentionally **relative**. It does not reconstruct or independently certify the upstream 19-phase H4 provenance. The macro consumes that already-verified receipt and closes the downstream clean-q E1–E5 obligations. The p=73 and p=241 controls are regression fixtures only, not a proof of upstream provenance.
