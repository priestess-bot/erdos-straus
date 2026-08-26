# T6 q=1 root V1 base-admission conditional review

Date: 2026-08-27

Review target: the reviewed repository-selected exact-HEAD V5 candidate,
`data/t6-wave1/t6-coordinator-role-registry-v5.json`.

## Verdict

```text
V5 exact-HEAD registry / 12 pinned artifacts        ACTIVE
V1 root materialization role                         ACCEPT
Independent V1 base-admission role                   ACCEPT
V2-to-V1 state and owner reanchor                    ACCEPT IN THE STATED SCOPE
Selected-commit external trust anchor                REQUIRED
V5 claim status                                      conditional / internal_review
queue, successor, producer, E1-E5, T5, global        NOT AUTHORIZED
F1 / F2 / F3 / T6 / Erdos-Straus                     OPEN
```

This is a repository-level authority and proof-contract review. It is not
external academic peer review, and it does not turn a repository-selected
commit into an external trust root.

## Evidence

### Registry and role surface

V5 has status
`HEAD_BOUND_Q1_ROOT_V1_BASE_ADMISSION_AUTHORITY_NO_QUEUE_OR_SUCCESSOR` and
activation status `ACTIVE_EXACT_HEAD_AUTHORITY`. Its 12 pinned artifacts cover
the controlled orchestrator, post-issuance replayer, two role implementations,
the terminal adapter, the frozen V1 state contract, and the exact V2/V3/V4
cross-registry dependencies. Only two artifacts receive a role grant:

| Role | Capability | Boundary |
|---|---|---|
| `Q1_ROOT_V1_BASE_MATERIALIZER` | `MATERIALIZE_Q1_G_V1_ROOT_INITIALIZER_OUTPUT` | materializes a parentless V1 base state, but does not admit or enqueue it |
| `INDEPENDENT_Q1_ROOT_V1_BASE_ADMISSION_VERIFIER` | `ISSUE_Q1_G_V1_BASE_ADMISSION_NO_QUEUE` | issues one V1 base admission, but no successor or queue action |

The terminal adapter is only a canonical projection. The exact-HEAD
orchestrator and post-issuance receipt verifier are explicitly non-role
artifacts. The latter rebuilds the expected wire without importing or invoking
the orchestrator.

V5 consumes a V3 production registered-prefix MISS and independently replays
the V4 root owner and scope receipts. It does not accept a caller-supplied V5
grant, V4 receipt, V4 E1 receipt, candidate, state wire, queue token or
authority boolean. The V1 state semantic origin forbids all V4 E1/candidate
fields.

### Controls and object reanchor

The positive exact-HEAD controls are:

```text
p=1201  V3 gaps [3,7,11] registered-prefix MISS -> V1 base admission
p=2521  V3 gaps [3,7,11] registered-prefix MISS -> V1 base admission
```

The terminal-first controls are:

```text
p=73, p=193, p=241441  production HIT -> TERMINAL_SOURCE_NOT_MISS
```

For a positive control, V5 constructs a new V1
`ROOT_INITIALIZER_OUTPUT` state ID and recomputes the V1 owner from the frozen
facts and fifteen-family precedence. The V2/V4 digest is evidence for the
source lineage only; it is neither copied nor accepted as the V1 owner digest.
The receipt may set `persistent_admission=true` and
`v1_base_owner_authority=true`, while its `queue_gate` remains
`ROOT_INITIALIZER_OUTPUT` and no enqueue occurs.

The canonical root potential `(p,3,0,0,0,0,0)` is carried as evidence only.
Both `t5_potential_authority` and `t5_ticket_authority` are false, so this is
not a T5 payment or a phase-drop ticket.

### Focused verification

The latest authority review returned `ACCEPT` after the following focused
checks:

| Suite | Result | Main controls |
|---|---:|---|
| `tests.test_t6_coordinator_role_registry_v5` | 14/14 PASS | active exact-HEAD registry, two role grants, pin and dependency contracts, denials and fail-closed controls |
| `tests.test_t6_q_one_root_v1_base_admission_roles_v1` | 13/13 PASS | p1201/p2521 materialization and admission, V1 owner reanchor, potential-as-evidence, HIT rejection and receipt mutation controls |
| `tests.test_t6_q_one_root_v1_base_admission_orchestrator_v1` | 7/7 PASS | exact-HEAD issue/replay, terminal preemption, cross-source/HEAD, stale preload, worktree drift, Git routing and replace controls |
| **Total** | **34/34 PASS** | reviewed V5 authority surface |

The review also reports passing `ruff`, `py_compile`, JSON-schema validation
and `git diff --check` for the V5 candidate. These are implementation controls,
not a proof of a global selector.

### Commit-trust condition

The exact-HEAD machinery pins tracked blobs, symbol/closure/dependency
manifests, registry bytes and the selected full commit. It rejects worktree
drift, Git replace objects, inherited routing variables and pin drift inside
that selected tree. This protects the reviewed selected commit from being
silently changed during execution.

It does not authenticate an arbitrary caller-selected new commit as an external
trust root. A commit that changes both a role artifact and its pins is a new
authority policy and needs fresh review plus an external immutable or signed
commit trust anchor. This condition is why the public V5 claim remains
`conditional` and `internal_review` rather than being upgraded by the local
`ACCEPT` review.

## Inference supported by the evidence

Subject to the selected-commit trust condition, V5 repairs the narrow object
mismatch identified after V4: an actual V2 q=1 G root can be reanchored as a
new admitted V1 `ROOT_INITIALIZER_OUTPUT` without smuggling V4 E1/candidate
data into the state identity. It establishes a base-state admission for the
two positive controls, not an edge admission.

The next proof object must bind the pre-existing V4
`ROOT_SOURCE_SCOPED_E1` occurrence to this exact admitted V1 source ID. Only
after that rebind can the phase-root pilot issue a target-bound terminal scope,
E2 projection, target owner/E3 receipt, E4 identity lift, E5/T5 ticket and a
separate shared target-admission sidecar.

## Explicit non-claims

This review does not establish:

- a queue entry, enqueue action, successor transition or producer branch;
- generic E1, successor E1, or the V4-E1-to-V1-source rebind;
- E2 target-construction authority, E3 target admission, E4 lift authority,
  E5/T5 authority, re-entry or a verified edge;
- a complete terminal schedule, global exhaustion, terminal leaf or
  `MISS_COMPLETE` result;
- an active verified wave1 producer or any change to the residual counts;
- closure of Gate 2, Gate 4, Gate 5, F1, F2, F3, T6 or the Erdos-Straus
  conjecture.

The global acceptance checklist remains entirely unchecked. Publication must
replay V5 against the final exact committed HEAD and satisfy the stated
selected-commit trust condition before treating this narrow base-admission
receipt as a published authority.
