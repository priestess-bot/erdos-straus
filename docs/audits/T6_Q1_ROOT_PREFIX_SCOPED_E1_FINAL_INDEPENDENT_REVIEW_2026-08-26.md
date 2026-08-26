# T6 q=1 root prefix-scoped E1 final independent review

Date: 2026-08-26

Review target: active V4 candidate bytes in the integration worktree, based on
the frozen V3 production-terminal authority at
`b7ce0fd5e3d4e721096cce89fe42e4e40932dfc6`.

## Verdict

```text
V4 exact-HEAD registry contract              ACCEPT
Three loader-free V4 role contracts          ACCEPT
Controlled orchestration and replay          ACCEPT
q=1 root registered-prefix scoped E1         ESTABLISHED IN THIS SCOPE
Generic/successor E1 and E2--E5 edge          OPEN
Gate 2 / Gate 4 / T6 / Erdos-Straus           OPEN
```

This is an independent repository-level proof-contract and implementation
review.  It is not external academic peer review.  The accepted statement is
the narrow source-occurrence theorem below; it is not a recursive selector
edge.

## 1. Evidence

### 1.1 Exact-HEAD authority surface

`t6_coordinator_role_registry_v4` is active with status
`HEAD_BOUND_Q1_ROOT_PREFIX_SCOPED_E1_AUTHORITY_NO_SUCCESSOR_OR_RECURSION`.
It inherits the four V3 production-terminal roles without modifying them and
adds exactly three loader-free roles:

| V4 role | Authorized capability | Explicit boundary |
|---|---|---|
| `COMMON_ROOT_OWNER_CLASSIFIER` | classify the common owner of the actual ordinary parentless q=1 G root | no terminal-result dependency, no prefix MISS, no E1 |
| `INDEPENDENT_SCOPE_AWARE_E1_VALIDATOR` | replay the registered-prefix MISS and validate its root-source E1 scope | no common-owner authority and no E1 issuance |
| `REGISTERED_PREFIX_E1_CONSUMER` | combine the owner and scope receipts into one `ROOT_SOURCE_SCOPED_E1` occurrence | no generic/successor E1, producer, admission or queue |

The inherited V3 roles plus these three roles give seven effective
capabilities only as registry bookkeeping.  V4 grants exactly three new roles.

Two additional artifacts are pinned but are deliberately non-roles:

| Non-role artifact | Class | Function |
|---|---|---|
| `t6_q_one_root_prefix_scoped_e1_orchestrator_v2.py` | `CONTROLLED_LOADER_ORCHESTRATOR_ONLY` | load the exact requested HEAD, project the three grants and assemble the role chain |
| `t6_q_one_root_prefix_scoped_e1_receipt_verifier_v2.py` | `POST_ISSUANCE_REPLAY_DEPENDENCY_ONLY` | independently rebuild the expected output wire and compare it with the issued receipt |

Both controlled loaders bind their own path and bytes, the exact full commit
and tree, every execution dependency, the loader/caller AST contract and the
fixed call table.  Caller-owned registries, worktree drift, alternate module
paths and Git replacement objects do not acquire authority.

The reviewed role-module blob SHA-256 values are:

```text
owner classifier     500e44221ab8591c3725c56579306a5aa5a79d3570c8cd5c194ae8380e71197b
scope validator      a8565979e368f3c78691f887e4447f5d653cbfd15a6d14fb0dd38f3ac2d660b1
E1 consumer          056e10087d76a012ce1abba8b8e657f6fdb988c3ccc47f2fed99372a8016b0f3
orchestrator         f5b31286be17b102f35684d193a96491f34a8be85f88f11b8aec0b9573fa1def
post-issue replayer  917b431d5920f99fc800cf653c7d9993bfe48b5b2bb1e1c9812319f2d5cf91bc
receipt schema       32f2914a1337a9e3e090b932c4c8d6c92313e40abea6b2715a0b6fd0f12b6021
```

These hashes identify the reviewed candidate bytes.  They do not replace the
required replay against the eventual published commit.

### 1.2 Exact V1 owner equivalence

The owner role does not infer ownership from a terminal result.  It rebuilds
the canonical source body, root anchor, raw source state and issuer actualness
from the raw q=1 G integers.  Its normalized header is accepted by the actual
frozen V1 facts validator, evaluates all fifteen V1 family predicates in
`FAMILY_PRECEDENCE_V1` order, and has the unique match
`type_ii_relation_g_endpoint` at zero-based precedence index 2.

The owner preimage is exactly the V1 preimage over
`contract_id`, `schema_version`, `state_id`, `facts_digest`, `owner`,
`matched_families` and `precedence_index`.  The focused test reconstructs a
real `VerifiedSelectorHeaderV1`, calls the V1 classifier and
`owner_digest_v1`, and obtains the same classification, bare digest and
`owner:<digest>` identifier.  This establishes equivalence to the frozen V1
owner contract for this root domain, not a second approximate grammar.

The resulting scope remains `ROOT_SOURCE_DISPATCH_ONLY`.  It is not common
persistent target admission.

### 1.3 Terminal-first and prefix controls

The role-level negative controls establish that the production terminal HIT
cases

```text
p=73       ROOT_TERMINAL_HIT at gap 7, Type II
p=193      ROOT_TERMINAL_HIT at gap 7, Type I
p=241441   ROOT_TERMINAL_HIT at gap 11
```

are rejected with `TERMINAL_SOURCE_NOT_MISS` before any scoped E1 receipt can
be produced.  The exact-HEAD integration suite independently exercises the
same early rejection for `p=73`.

The positive controls

```text
p=1201     MISS_REGISTERED_PRIORITY_COMPLETE for gaps [3,7,11]
p=2521     MISS_REGISTERED_PRIORITY_COMPLETE for gaps [3,7,11]
```

pass exact-HEAD orchestration and post-issuance replay.  Their consumer output
has `root_source_scoped_e1=true`, but keeps
`e1_authority=false`, `generic_e1=false`, `successor_e1=false`,
`persistent_admission=false`, `queue_authority=false` and
`global_exhaustion=false`.

The validator also scans gap 23 only as an outside-scope control.  At
`p=1201`, gap 23 has a Type-I certificate with `d=34`.  Therefore a successful
MISS for the registered priority prefix `[3,7,11]` cannot be relabeled as a
global terminal miss.  The authorized scope records `next_unchecked_gap=15`
and `remaining_domain_unchecked=true`.

### 1.4 Focused verification replay

The final review reran the three current V4 suites on 2026-08-26:

| Suite | Result | Principal coverage |
|---|---:|---|
| `test_t6_coordinator_role_registry_v4` | 16/16 PASS | active/fail-closed registry, exact roles/non-roles, pins, DAG, V3 binding, schema/matrix parity and denials |
| `test_t6_q_one_root_prefix_scoped_e1_roles_v2` | 9/9 PASS | V1 owner equivalence, HIT rejection, prefix validation, gap-23 boundary, authority and serializer mutations |
| `test_t6_q_one_root_prefix_scoped_e1_orchestrator_v2` | 7/7 PASS | p1201/p2521 exact-HEAD issue/replay, p73 early rejection, cross-source/HEAD, stale modules, worktree/path drift and Git replace controls |
| **Total** | **32/32 PASS** | focused V4 contract surface |

Commands used:

```bash
python3 -m unittest tests.test_t6_coordinator_role_registry_v4 -v
python3 -m unittest tests.test_t6_q_one_root_prefix_scoped_e1_roles_v2 -v
python3 -m unittest tests.test_t6_q_one_root_prefix_scoped_e1_orchestrator_v2 -v
```

## 2. Inference supported by the evidence

For one actual parentless ordinary q=1 G root at one exact HEAD, after an
independently replayed V3 production MISS for the registered priority gaps
`[3,7,11]`, the V4 chain establishes

```text
actual root source
  -> exact V1 common root owner
  -> independently validated registered-prefix scope
  -> deterministic full-carrier phase-root witness
  -> ROOT_SOURCE_SCOPED_E1 occurrence
```

The source-scoped occurrence is tied to

\[
t=(p-1)/24,\qquad X=(p+3)/4,\qquad
R=16t+3,\qquad K=X(16t+1),
\]

with the checked chart identity `4K=pR+1` and the fresh source

\[
(p,R(p-1)-p,p-1)\longrightarrow(1,R-1,1).
\]

On this exact statement the final independent reviewer found no remaining
blocking contract or proof issue and returned `ACCEPT`.

## 3. Explicit non-claims

This review does not establish any of the following:

- generic E1 or successor E1;
- an authorized producer, branch, candidate, continuation or direct use of a
  terminal receipt as continuation authority;
- E2 target construction authority;
- E3 common target normal form, target ownership or re-entry;
- E4 universal solution-lift authority;
- E5/T5 strict-decrease ticket authority;
- persistent admission, enqueue or queue mutation;
- global terminal exhaustion or `MISS_COMPLETE`;
- complete Gate 2 or Gate 4;
- F1, F2, F3, T6 global selector totality;
- the Erdos-Straus conjecture.

In particular, the consumer's arithmetic `math_replay` is evidence for the
next phase-root construction; it is not by itself an E2--E5 edge receipt.

## 4. Publication boundary

The 32 focused tests exercise exact-HEAD behavior through committed fixture
repositories.  At the time of this review the V4 candidate was not yet part of
the integration branch HEAD.  After commit, the resolver, p1201/p2521
orchestration and independent replay must be run against that exact full commit
ID, followed by the repository's Gate 0/live-snapshot provenance checks.  No
status beyond the narrow V4 scoped-E1 result may be upgraded by that publication
step.
