---
kind: claim
claim_id: t6-live-audit-snapshot-v2-contract
title: T6 live audit snapshot v2 provenance and state contract
statement: >-
  For a trusted push to the repository main branch, a live T6 audit snapshot
  can name a last verified HEAD only after independently replaying a clean PASS
  Gate-0 manifest at that commit and matching its raw bytes to the immutable
  direct-upload artifact identified by the official GitHub workflow, run,
  attempt and successful gate-zero job metadata. The snapshot separately binds
  the workpack origin, integration-audited commit, current observed HEAD, last
  verified HEAD, current claim/runtime/producer/terminal/grammar/T5/test/review
  digest vector and the README/ledger/frontier consumer policy. A verified
  ancestor is reported as ADVANCED_UNVERIFIED at a later HEAD. HEAD verification
  alone does not authorize a theorem-status change: that additionally requires
  a current-digest independent-review basis, non-diverged integration history
  and all consumer bindings. No such independent current-digest basis is
  registered by this claim.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
  - T6
  - audit
  - provenance
  - CI
  - proof-boundary
sources:
  - reproduction: scripts/t6_live_audit_snapshot_v2.py
    role: HEAD-bound snapshot generator, content replay and GitHub provenance verifier
  - reproduction: tests/test_t6_live_audit_snapshot_v2.py
    role: provenance, historical-head, mutation, schema and workflow controls
  - source: schemas/t6-live-audit-snapshot-v2.schema.json
    role: strict snapshot state-machine schema
  - source: schemas/t6-gate0-run-provenance-v1.schema.json
    role: strict locator and service-provenance schema
  - source: .github/workflows/research-kb-ci.yml
    role: direct manifest upload and dependent snapshot job
visibility: public
last_checked: '2026-08-26'
---

# T6 live audit snapshot v2 provenance and state contract

## Scope

The generated snapshot lives at
`data/t6-wave1/t6-live-audit-snapshot-v2.json`. It is deliberately ignored by
Git and uploaded as a CI artifact. A tracked file cannot contain the SHA of the
commit containing that same file without creating a self-reference problem.

The snapshot distinguishes four commit roles:

1. the historical workpack origin;
2. the integration commit audited by the frozen wave1 inputs;
3. the current observed HEAD whose Git objects supply all live digests;
4. the most recent HEAD backed by a verified Gate-0 run and immutable artifact.

Those roles are not aliases. In particular, an old workpack or integration SHA
cannot be reported as the current verified HEAD merely because it remains an
ancestor.

## Provenance gate

Manifest content replay and service provenance are independent checks. Content
replay recomputes the manifest seal, exact HEAD/tree, command matrix, result
status, fixed test-discovery skip policy and all declared digest domains in a
detached checkout. Provenance then queries GitHub's official API and requires:

- the fixed repository and active workflow ID, name and path;
- a `push` run on `main` at the manifest HEAD and exact attempt;
- the unique `gate-zero` job to have completed successfully;
- an unexpired direct-upload artifact with the fixed manifest filename;
- the artifact size and server SHA-256 to match the same captured manifest
  bytes used by content replay;
- the artifact's workflow-run record to bind the same repository, run and HEAD.

`GITHUB_*` environment variables are only an additional cross-check. They do
not create provenance. A local file carrying plausible run IDs, or a manifest
sealed without executing the workflow, cannot satisfy the service metadata and
artifact digest gate.

Environment values are not stored in the permanent basis. They are checked
strictly when verification runs inside the same GitHub run named by the
locator; local replay and a later workflow replaying an older green run rely on
the official API and immutable artifact instead of inheriting unrelated current
run variables.

The overall workflow run is still `in_progress` while its dependent snapshot
job executes. That transient run status is checked but is not sealed into the
permanent Gate-0 basis. The stable basis records the already completed and
successful `gate-zero` job. A later replay of the same successful run therefore
produces identical provenance after the run changes to `completed`; if the
completed run instead has a non-success conclusion, replay fails closed.

## State machine

Let `H` be the API-attested Gate-0 HEAD and `C` the current observed HEAD.

| Relation | Snapshot state | Status upgrade |
|---|---|---|
| no attested `H` | `NO_VERIFIED_HEAD` | blocked |
| `H = C` | `VERIFIED_HEAD` | still subject to every review/consumer gate |
| `H` is a strict ancestor of `C` | `UNVERIFIED_HEAD_ADVANCE` | blocked |
| otherwise | `DIVERGED_FROM_VERIFIED_HEAD` | blocked |

The Python verifier recomputes this relation from the Git graph. The Draft
2020-12 schema independently rejects contradictory null/basis/relation/state
combinations and forbids an upgrade when integration diverges, consumer
bindings are stale or the current-digest review basis is missing.

## Current boundary

This contract establishes an auditable engineering state object. It does not
establish producer completeness, complete terminal schedules, E1--E5 runtime
admission, F1/F2/F3 closure, T6 selector totality or the Erdos-Straus
conjecture. The current implementation deliberately emits
`current_digest_audit.status = MISSING` unless an independent reviewer supplies
an exact current-HEAD digest-vector basis. Consequently the present integration
must keep `status_upgrade_allowed = false` even when its Gate-0 HEAD is verified.
