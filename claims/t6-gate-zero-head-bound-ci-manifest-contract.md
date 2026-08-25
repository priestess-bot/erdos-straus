---
kind: claim
claim_id: t6-gate-zero-head-bound-ci-manifest-contract
title: T6 Gate 0 HEAD-bound CI manifest integrity contract
statement: >-
  The Gate 0 runner owns a fixed command matrix and derives its result rather
  than accepting a caller-supplied PASS value. Each emitted manifest binds the
  tested Git HEAD and tree, Python and workflow identity, the knowledge-base
  claim set, T6 runtime sources, local producer registry, frozen grammar and
  complete Python test inventory to content digests. The verifier independently
  recomputes those bindings and rejects a changed checkout, missing command,
  duplicate JSON key, altered digest or forged PASS. The run manifest is an
  ephemeral CI artifact because committing a file that names its containing
  commit would be self-referential. This is a repository verification contract,
  not evidence that an arbitrary HEAD is green and not a theorem-status update.
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
`data/t6-wave1/ci-run-manifest-v1.json` after checkout. That path is ignored by
Git and uploaded by GitHub Actions. A tracked live manifest cannot bind its own
containing commit SHA without a fixed-point problem.

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

## Content bindings

File-set receipts bind sorted repository-relative paths, Git modes, byte sizes
and SHA-256 content hashes. The manifest records independent aggregate digests
for all claim cards, all `scripts/t6_*.py` runtime sources and every tracked
Python file under `tests/`. The grammar digest is recomputed using the legacy
canonical encoding declared by the frozen wave1 grammar file. The producer
registry digest is explicitly scoped to the executable local runtime registry;
it does not claim that a shared all-producer registry exists.

## Failure boundary

The verifier rejects at least the following conditions:

- tested HEAD or tree differs from the current checkout;
- GitHub's checkout SHA differs from the tested SHA;
- the checkout contains an unrecorded tracked or untracked change;
- a digest scope changes by content, path, mode, addition or deletion;
- the stored grammar hash differs from an independent recomputation;
- a command or result is missing, duplicated, reordered or altered;
- `status = PASS` is not exactly derived from successful command results;
- the manifest payload digest or JSON object structure is invalid.

Consequently a green artifact is evidence only for its exact `head_sha`. It
cannot be inherited by a later commit, and it cannot promote F1, F2, F3, T6 or
the Erdos-Straus conjecture.
