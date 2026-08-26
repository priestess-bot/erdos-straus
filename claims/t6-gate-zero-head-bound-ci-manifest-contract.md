---
kind: claim
claim_id: t6-gate-zero-head-bound-ci-manifest-contract
title: T6 Gate 0 HEAD-bound CI manifest integrity contract
statement: >-
  The Gate 0 runner owns a fixed command matrix and derives its result rather
  than accepting a caller-supplied PASS value. Each emitted manifest binds the
  tested Git HEAD and tree, replayed Python and workflow identity, the knowledge-base
  claim set, T6 runtime sources, local producer registry, frozen grammar,
  complete Python test inventory, coordinator evidence inventory and the
  complete-terminal registry to content digests. The latter two are explicit
  zero-authority diagnostics: all five coordinator role-grant classes and all
  complete terminal schedules are empty, and complete-miss issuance is disabled.
  Full discovery additionally
  emits a structured receipt for the exact test count and the fixed allowlist of
  optional raw-artifact skips. The verifier independently recomputes the static
  bindings and rejects a changed checkout, missing command, unexpected skip,
  duplicate JSON key, altered digest or forged PASS. The run manifest is an
  ephemeral CI artifact because committing a file that names its containing
  commit would be self-referential. Its content seal is not a signature, so
  provenance must also be established by the successful GitHub Actions run that
  uploaded it. This is a repository verification contract, not evidence that an
  arbitrary HEAD is green and not a theorem-status update.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
  - T6
  - CI
  - audit
  - provenance
  - content-addressing
  - proof-boundary
sources:
  - reproduction: scripts/t6_ci_run_manifest_v1.py
    role: fail-closed Gate 0 command runner, digest generator and verifier
  - reproduction: tests/test_t6_ci_run_manifest_v1.py
    role: manifest mutation, HEAD-binding and command-matrix regression tests
  - source: .github/workflows/research-kb-ci.yml
    role: exact-HEAD workflow execution and artifact upload
  - source: data/t6-wave1/t6-coordinator-role-registry-v1.json
    role: exact-HEAD evidence inventory with zero role grants
  - source: data/t6-wave1/t6-complete-terminal-schedule-registry-v1.json
    role: production namespace with zero complete schedules and issuance disabled
visibility: public
last_checked: '2026-08-26'
---

# T6 Gate 0 HEAD-bound CI manifest contract

## Scope

Gate 0 is an engineering admission condition. It does not establish a
mathematical selector edge or change any theorem status. A repository revision
is Gate-0 verified only when the workflow artifact for that exact revision has
`status = PASS` and the independent verifier accepts every binding.

The manifest is generated at
`data/t6-wave1/ci-run-manifest-v1.json` after checkout. The script name,
transport path and uploaded filename retain the `v1` suffix for workflow
compatibility; the current writer emits the exact internal identity
`t6_ci_run_manifest_v2`, schema version 2 and artifact ID
`ci_run_manifest_v2`. The verifier dispatches only an exact legacy-v1 or
current-v2 identity. Historical v1 manifests remain replayable but cannot carry
or inherit v2 diagnostics. The generated path is ignored by Git and uploaded
by GitHub Actions. A tracked live manifest cannot bind its own containing commit
SHA without a fixed-point problem.

## Required command surface

The runner owns, in order, the following command identities and argument lists:

1. knowledge-base validation and rebuild;
2. generated `index/` cleanliness;
3. the full-tree pre-T6 contract audit;
4. the constructor inventory audit;
5. repository-wide Ruff over `scripts`, `reproductions` and `tests`;
6. byte-code compilation over the same Python surface;
7. `git diff --check`;
8. complete `unittest` discovery under `tests/test_*.py`.

Callers cannot replace a command, omit a result or inject a successful status.
The runner continues after an ordinary command failure so that the artifact
records the complete attempted matrix, then exits nonzero.

The full-discovery process streams its combined output to the CI log while
capturing the same bytes. Its receipt records the parsed `Ran` count, final
summary, output digest and the exact skipped test IDs and reasons. A clean
checkout currently permits exactly 13 skips, all caused by four intentionally
untracked H19 raw replay files larger than the regular GitHub file limit. A new,
missing or renamed skip, or a changed reason, makes Gate 0 fail. This distinguishes
"full discovery completed with the frozen optional evidence boundary" from the
stronger and currently false statement that every large historical raw replay
was rerun in CI.

## Content bindings

File-set receipts bind sorted repository-relative paths, Git modes, byte sizes
and SHA-256 content hashes. The manifest records independent aggregate digests
for all claim cards, all `scripts/t6_*.py` runtime sources and every tracked
Python file under `tests/`. The grammar digest is recomputed using the legacy
canonical encoding declared by the frozen wave1 grammar file. The producer
registry digest is explicitly scoped to the executable local runtime registry;
it does not claim that a shared all-producer registry exists.

Current-v2 manifests also resolve the coordinator role inventory and the
complete-terminal registry from ordinary Git objects at the exact tested HEAD.
They independently recompute the outer inventory digest, the evidence-artifact
inventory digest, five role-subregistry digests and the complete-terminal
registry digest. The diagnosed authority state is deliberately empty:
`role_authority=false`, producer/validator/projector/terminal-schedule/T5-ticket
grant count zero, complete-schedule count zero and
`complete_miss_issuance_enabled=false`. These fields attest exact bytes and the
declared zero-authority boundary; they do not authorize any callable or prove
terminal completeness.

The verifier also requires integer schema versions without Python's boolean-as-
integer coercion and compares the recorded Python implementation and version to
the interpreter performing the replay.

## Failure boundary

The verifier rejects at least the following conditions:

- tested HEAD or tree differs from the current checkout;
- GitHub's checkout SHA differs from the tested SHA;
- the checkout contains an unrecorded tracked or untracked change;
- a digest scope changes by content, path, mode, addition or deletion;
- the stored grammar hash differs from an independent recomputation;
- a command or result is missing, duplicated, reordered or altered;
- full discovery has an unparseable summary or any skip outside the fixed
  optional-raw-artifact allowlist;
- `status = PASS` is not exactly derived from successful command results;
- the manifest payload digest or JSON object structure is invalid.
- a legacy-v1 payload carries current-v2 diagnostics, or a current-v2 payload
  omits, alters or self-reports any coordinator/terminal diagnostic digest.

Consequently a green artifact is evidence only for its exact `head_sha`. It
cannot be inherited by a later commit. A detached manifest file establishes
content consistency but not service provenance by itself. Neither form of Gate
0 evidence, and none of the zero-authority diagnostics, can grant a runtime
role or promote F1, F2, F3, T6 or the Erdos-Straus conjecture.
