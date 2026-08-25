---
kind: claim
claim_id: t6-coordinator-head-bound-role-registry-v1
title: T6 HEAD-bound evidence-only role inventory Slice 1
statement: >-
  Slice 1 provides a deterministic evidence inventory resolved from regular
  blobs in an exact requested Git commit. The executing resolver and governing
  JSON Schema must be clean and byte-identical to their corresponding blobs in
  that commit, and every resolver Git invocation disables replacement objects.
  The exact-HEAD Draft 2020-12 schema and additional fail-closed checks require
  every role-grant, branch-binding and complete-terminal-schedule list to be
  empty. Shared structured-receipt, persistent-state and T5 modules are pinned
  only as evidence. The q=1 reason codes are declared blockers, not semantic
  proofs. This inventory grants no producer, validator, projector, terminal
  scheduler or T5-ticket authority and does not close Gate 2 or any mathematical
  frontier.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
  - T6
  - evidence-inventory
  - Git
  - content-addressing
  - proof-boundary
sources:
  - source: data/t6-wave1/t6-coordinator-role-registry-v1.json
    role: evidence-only source inventory with zero role grants
  - source: schemas/t6-coordinator-role-registry-v1.schema.json
    role: exact-HEAD machine-readable zero-authority contract
  - reproduction: scripts/t6_coordinator_role_registry_v1.py
    role: self-bound Git-object evidence resolver
  - reproduction: tests/test_t6_coordinator_role_registry_v1.py
    role: schema, toolchain, replacement-object and mutation controls
visibility: public
last_checked: '2026-08-26'
---

# T6 HEAD-bound evidence-only role inventory Slice 1

## Established engineering boundary

The tracked source inventory does not authorize any role. The resolver accepts
only a repository locator and a lowercase full commit object ID. It reads the
fixed inventory, schema and evidence paths from that commit's Git tree and emits
a deterministic ephemeral payload containing:

```text
head SHA and tree SHA
resolver/schema execution binding
inventory source digest
resolved evidence blob and symbol or JSON-pointer digests
evidence-only artifact digest inventory
five empty role-subregistry digests
declared blocked-candidate evidence
```

The artifact inventory has schema ID
`t6_evidence_artifact_digest_inventory_v1`, explicitly records
`role_authority=false`, and is deliberately not schema-compatible with
`ArtifactDigestManifestV1`. Turning selected evidence pins into a trusted role
manifest requires a separate extraction and Gate-0-attested authorization step.

Every Git subprocess is run with `GIT_NO_REPLACE_OBJECTS=1`. Commit and blob
replace refs therefore cannot change the objects being attested. The resolver
also refuses to operate when its worktree copy or the schema worktree copy is
dirty, untracked, non-regular, or byte-different from the requested-HEAD blob.
It separately checks that the executing resolver's backing file bytes are
exactly the resolver blob named by that commit. This is a trusted-process CLI
boundary, not a defense against arbitrary in-process monkeypatching.

The inventory is validated by the Draft 2020-12 schema loaded from the same
commit. Duplicate JSON keys and non-finite values are rejected before schema
validation. Static Python parsing pins a named module-level symbol without
importing or executing the referenced module. This is evidence identification,
not callable authority. Because `ast.dump` is interpreter-contract dependent,
each Python symbol digest also binds a recorded `python_ast_contract` containing
the executing implementation, Python major.minor, and the fixed AST-dump format
version.

## Zero role authority

The following source arrays are empty and schema-constrained to remain empty:

```text
role_grants
branch_bindings
complete_terminal_schedules
```

Consequently the producer, independent-validator, projector,
terminal-schedule and T5-ticket subregistries all summarize empty grant lists.
The structured receipt verifier, state header/classification functions, family
precedence, queue gate and T5 functions remain evidence artifacts only. A later
Gate-0-attested authority layer must decide whether and how any role is granted.

## q=1 declared blockers

The q=1 local runtime module and its named producer, projector, validator,
terminal-schedule and terminal-verifier symbols are content-pinned under a
blocked candidate. Its exact declared reason-code set is:

```text
LEGACY_BOOL
LOCAL_TERMINAL_SCOPE
SAME_MODULE_ROLE_COLLISION
```

The resolver proves that these declarations and symbols occur in the pinned
inventory/module bytes. It does not prove the semantic truth of the reason
codes. Independent runtime and proof review supplied those conservative
blockers; a future revision must replace them with positive, separately reviewed
authority evidence before activation.

## Non-claim

This Slice 1 does not grant or test producer/validator separation, integrate
structured receipts into the runtime, establish a complete terminal schedule,
activate the q=1 pilot, close Gate 2, close F1/F2/F3, close T6, or prove the
Erdos--Straus conjecture.
