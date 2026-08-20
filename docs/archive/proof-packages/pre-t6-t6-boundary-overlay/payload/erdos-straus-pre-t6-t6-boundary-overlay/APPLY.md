# Apply the pre-T6/T6-boundary patch

Target upstream commit:

`ef95ac0f2c3b687bb67d33dc490b248ccd8cfcb0`

Preferred application from a real full checkout:

```bash
git checkout -b pre-t6-boundary-20260820 ef95ac0f2c3b687bb67d33dc490b248ccd8cfcb0
git apply --check /path/to/erdos-straus-pre-t6-t6-boundary.patch
git apply /path/to/erdos-straus-pre-t6-t6-boundary.patch
python scripts/kb.py validate
python reproductions/pre_t6_contract_kernel_audit.py --root . --require-full-tree
python -m unittest tests.test_pre_t6_contract_kernel_audit -v
git add -A
git commit -m "Freeze pre-T6 kernel and isolate T6 proof boundary"
```

Alternatively:

```bash
git checkout -b pre-t6-boundary-20260820 ef95ac0f2c3b687bb67d33dc490b248ccd8cfcb0
git am /path/to/erdos-straus-pre-t6-t6-boundary.mbox
```

The overlay directory is for inspection or manual copying. The patch is the
canonical delivery because it preserves modifications to existing files.

Do not interpret the local packaging commit `b2b9ae0` as an upstream parent.
It was created in a sparse fixed-SHA audit repository. Apply the diff to the
real upstream baseline shown above.
