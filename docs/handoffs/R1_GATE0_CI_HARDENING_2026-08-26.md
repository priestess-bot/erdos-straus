# R1 Gate 0 CI hardening handoff

## Boundary

This handoff covers only remediation-plan Gate 0. It does not modify README,
the T6 frontier, residual counters or any existing theorem status.

The immutable starting baseline was:

```text
3a7c0aacebece3dfb3bd7c7f69b2044fd7e7bf08
Freeze terminal-only producer activation boundary
```

The starting worktree already contained an unrelated modification to
`scripts/t6_q_one_full_carrier_runtime_slice_v1.py` and an untracked copy of the
authoritative remediation plan. Neither belongs to this R1 change.

## Observed failures

The active GitHub workflow's latest observed failure was run `32864494048` at
commit `5c82eb8d56f2c5a3267d3f426386ce39a8833af1`. Its pre-T6 audit and 16 audit
tests passed, then Ruff 0.16.4 reported six findings in the old narrow lint step.
The same run warned that `actions/checkout@v4` and `actions/setup-python@v5`
targeted deprecated Node 20. The unfiltered research workflow was disabled
manually and had no green run in its visible history.

An isolated clean clone at the R1 baseline produced:

```text
python scripts/kb.py validate                                      PASS (1448 documents)
python scripts/kb.py build                                         PASS
git diff --exit-code -- index/                                     PASS
python reproductions/pre_t6_contract_kernel_audit.py --root . \
  --require-full-tree                                              PASS
python scripts/audit_t6_constructor_inventory_v1.py                PASS
python -m compileall -q scripts reproductions tests                 PASS
git diff --check                                                   PASS
ruff check scripts reproductions tests                             FAIL (89 findings)
```

The constructor audit reported `closure_ready=false` with 19 warnings. That is
the expected fail-closed F1 boundary, not a command failure and not evidence of
T6 closure.

Full discovery also exposed clean-checkout defects that focused/local runs had
hidden:

| Class | Exact affected surface | Repair |
| --- | --- | --- |
| ignored raw data | 13 high-scale methods across the five `m27`--`m59` selector-profile modules, shared-selector audit, shared-selector tail closure, fixed-tail factor profile and square-root normal-form audit | skip only the named raw replay when its deliberately untracked 65k/131k/262k artifact is absent; tracked smaller fixtures remain mandatory |
| stale receipt wording | `test_type_i_f2_high_support_c1_canonical_dual_absorb_handoff` | align the verifier with the stored `TYPE_SPACE_OWNER_ACCEPTED; PRODUCER_SERIALIZER_COMMON_ADMISSION_REENTRY_OPEN` boundary |
| import-order contamination | all three q1 runtime-slice tests after adapter/runtime tests | give dynamic test modules unique `_under_test` names so cached classes cannot cross runtime module identities; retain the production `isinstance` firewall |

The raw files are 142--549 MiB and are explicitly excluded by `.gitignore`.
Normal CI does not download or silently regenerate them. A developer carrying
the files still replays the high-scale assertions; a clean checkout reports
honest skips rather than `FileNotFoundError`.

## Delivered Gate 0 surface

- `research-kb-ci.yml` is the unfiltered authoritative push, pull-request and
  manual Gate 0 workflow.
- GitHub actions use immutable current v7 release SHAs and Node 24.
- `requirements-ci.txt` pins PyYAML, SymPy and Ruff; `ruff.toml` fixes the
  repository-wide correctness policy to `E4`, `E7`, `E9` and `F`.
- The pre-existing 89 findings on that policy are repaired without changing
  theorem/frontier data.
- `t6_ci_run_manifest_v1.py` runs the complete matrix, emits an artifact even
  after ordinary command failures and independently verifies current-HEAD
  bindings.
- The workflow always verifies and uploads
  `data/t6-wave1/ci-run-manifest-v1.json`; the generated path is intentionally
  ignored by Git.
- Full `unittest discover` replaces hand-picked test modules.
- Test imports no longer mutate canonical runtime module names, so discovery
  order cannot turn valid runtime values into false legacy-object rejections.

## Gate interpretation

Local replay can establish that the implementation and current worktree pass
the matrix. It cannot supply a GitHub `workflow_run_id`. Gate 0 is externally
green only after the pushed exact SHA completes the re-enabled GitHub workflow
and its uploaded manifest verifies with `status = PASS`.
