# T6 Phase 2 q=1 root prefix-scoped E1 handoff, with V5 base admission and V6 conditional rebind update

Date: 2026-08-26

## Established handoff point

The q=1 root path now has a reviewed, exact-HEAD role chain from the V3
production terminal result to one narrowly scoped source occurrence:

```text
raw ordinary parentless q=1 G root
  -> V3 production terminal issuance and independent replay
  -> ROOT_TERMINAL_HIT: stop
  -> registered-prefix MISS [3,7,11]: continue only inside V4 scope
  -> COMMON_ROOT_OWNER_CLASSIFIER
  -> INDEPENDENT_SCOPE_AWARE_E1_VALIDATOR
  -> REGISTERED_PREFIX_E1_CONSUMER
  -> ROOT_SOURCE_SCOPED_E1 receipt
```

The V4 roles are loader-free.  Exact-HEAD loading/orchestration and independent
post-issuance replay are pinned non-role dependencies.  The current focused
verification result is `32/32 PASS` (`16` registry, `9` role and `7`
exact-HEAD integration tests).

## 2026-08-27 V5 base-admission extension

V5 resolves the object mismatch only at the base-admission layer. Its active
exact-HEAD registry has 12 pinned artifacts and exactly two new roles:

| Role | Narrow capability | Explicit exclusion |
|---|---|---|
| `Q1_ROOT_V1_BASE_MATERIALIZER` | materialize a canonical V1 `ROOT_INITIALIZER_OUTPUT` q=1 G state | no admission, queue, successor or E1--E5 authority |
| `INDEPENDENT_Q1_ROOT_V1_BASE_ADMISSION_VERIFIER` | issue the matching V1 base admission | no enqueue, successor, producer, E1--E5, T5 or global authority |

For `p=1201` and `p=2521`, a V3 registered-prefix MISS plus independently
replayed V4 owner/scope evidence produces an admitted V1 base state. The V5
pipeline deliberately does **not** consume a V4 E1 consumer receipt: V4 E1
and candidate fields are excluded from the V1 state and semantic-origin
preimage. `p=73`, `p=193` and `p=241441` remain terminal-first HIT controls
and reject before base admission.

The V2 root occurrence is therefore reanchored to a newly derived V1 state ID
and a newly recomputed V1 owner digest; neither V2 nor V4 owner digest is
copied. The canonical root potential `(p,3,0,0,0,0,0)` is recorded only as
evidence, with `t5_potential_authority` and `t5_ticket_authority` both false.
The final receipt may set `persistent_admission=true`, but all of the following
remain false:

```text
queue / enqueue / successor / producer = false
E1 / E2 / E3 / E4 / E5 / T5            = false
global exhaustion / terminal leaf        = false
```

The V5 claim remains `conditional` / `internal_review`. Its exact-HEAD
controls protect the reviewed repository-selected commit from worktree drift,
Git replacement and routing/pin drift, but do not make an arbitrary
caller-selected commit an external trust root. The selected commit must have an
external immutable or signed trust anchor before this narrow admission is used
as a published authority.

## 2026-08-27 V6 pure rebind extension

V6 supplies only a conditional, loader-free pure rebind between the existing
objects. Given a V4 `ROOT_SOURCE_SCOPED_E1` receipt and a V5 admitted V1 base
receipt at the same reviewed exact HEAD, it independently replays the common
V2 root chain and emits a separate
`Q1_ROOT_SOURCE_SCOPED_E1_REBIND_RECEIPT_V1`:

```text
V2 RawRootSourceStateV2 ID/digest
  -> V5 V1 ROOT_INITIALIZER_OUTPUT ID/wire digest
```

For `p=1201` and `p=2521`, the V3 registered-prefix MISS controls pass this
pure map. `p=73`, `p=193` and `p=241441` remain terminal-first HIT controls and
preempt before a V4/V5/rebind pair exists. The V1 source owner, owner digest
and source potential are recomputed against the V1 state; no V2 or V4 owner,
candidate or potential digest is copied.

The output is a namespaced derived witness, not a V1 state path or transition:

```text
representation_namespace = Q1_ROOT_SOURCE_SCOPED_E1_REBIND_V1
path_semantics           = DERIVED_WITNESS_NOT_V1_STATE_PATH
not_transition           = true
```

Only these authority markers are true:

```text
v4_root_source_scoped_e1       = true
root_source_scoped_e1_rebound  = true
source_rebind_authority         = true
```

Every generic/successor E1, producer, admission, queue/enqueue, E2--E5, T5,
re-entry and global authority bit is false. The legacy structured-E1 parser
rejects this receipt because it requires `MISS_COMPLETE`; V6 has only the
registered-priority prefix MISS with `next_unchecked_gap=15` and
`global_exhaustion=false`.

V6 has no exact-HEAD registry, controlled orchestrator or independent replayer.
It is therefore `conditional` / `internal_review`, and the V5
selected-commit/external-trust condition persists. It is not a generic E1,
production successor or queue authority.

## Inputs downstream work may inspect

For the same exact HEAD, later proof design may inspect the following V4/V5
facts. V6 may combine them only into its namespaced source-correspondence
sidecar; they do not by themselves authorize a generic E1 or successor.

- actual ordinary parentless q=1 G source and root initializer preimages;
- exact V1 owner `type_ii_relation_g_endpoint`, with identical V1 owner digest;
- V3 production `MISS_REGISTERED_PRIORITY_COMPLETE` for ordered gaps
  `[3,7,11]`;
- `next_unchecked_gap=15`, `global_exhaustion=false` and
  `remaining_domain_unchecked=true`;
- deterministic phase-root arithmetic

\[
t=(p-1)/24,
\quad X=(p+3)/4,
\quad R=16t+3,
\quad K=X(16t+1),
\]

  together with `4K=pR+1`, support `A=1`, the actual p-edge and fresh-source
  identities;
- the intended target shape
  `TYPEI/CHARGED/FULL_CARRIER_POST_G`, while target admission remains open.

Production HITs are terminal-first.  In the focused controls, `p=73`, `p=193`
and `p=241441` are rejected before E1.  `p=1201` and `p=2521` pass the scoped
prefix-MISS chain.  The `p=1201`, gap-23, Type-I `d=34` control remains outside
the authorized prefix and prevents any global-exhaustion inference.

## Current authority boundary

The final V4 receipt authorizes only the actual root-source occurrence needed
to begin a phase-root edge proof:

```text
root_source_scoped_e1              = true
scope_aware_consumer_authority     = true
root_source_occurrence_authority   = true

e1_authority                       = false
generic_e1                         = false
successor_e1                       = false
producer_authority                 = false
producer_continuation_allowed      = false
persistent_admission               = false
queue_authority                    = false
e2/e3/e4/e5 authority              = false
global_exhaustion                  = false
```

Therefore this handoff is not yet a `verified_edge`, does not close Gate 2 or
Gate 4, and does not change F1, F2, F3, T6 or Erdos-Straus status.

## Object-layer correction

The V4 `RawRootSourceStateV2` is an actual root occurrence, but it explicitly
has `persistent_admission=false` and is not a V1 runtime parent.  A normal
`ADMITTED_SUCCESSOR` issued directly from that V2 state would fail the common
runtime with `SOURCE_NOT_ADMITTED`.

The conservative migration path is therefore architecture A:

```text
V4 actual q=1 G occurrence
  -> canonical V1 ROOT_INITIALIZER_OUTPUT materialization
  -> independent common base admission (queue still false)
  -> V6 pure V4-to-V1 source rebind (still no successor authority)
  -> ordinary phase-root successor pipeline
```

Making the Type-I target itself the initializer output would remove the G state
from the persistent reachable domain and change the existing trace/T5/F1
quantifiers.  That alternative is not adopted.

V5 now supplies the two base-gate roles: a non-admitting V1 source materializer
and an independent base-admission verifier. Terminal schema translation,
orchestration and post-issuance replay remain non-roles. The new V1 state and
owner digests are recomputed; V4 digests are bound to a different V2 state ID
and cannot be copied.

## Next phase: establish V6 exact authority or pivot to target-terminal/E2 research

The object rebind itself now exists only as a pure conditional sidecar. It must
not be promoted to generic E1. The next authority-bearing step is either to
build a V6 exact-HEAD registry, controlled orchestrator and independent
replayer for this fixed rebind policy, or to independently develop the
target-terminal/E2 layer while leaving V6 non-authoritative. A full q=1 G to
Type-I phase-root edge still requires the following dependency order.

### 0. Completed conditionally: V1 root source materialization and base admission

V5 translates the independently replayed V3 production registered-prefix MISS
into a scope-preserving V1 terminal receipt, constructs a parentless
`ROOT_INITIALIZER_OUTPUT` q=1 G state, and runs the frozen V1 facts and owner
evaluation. Only the independent verifier issues base admission; materializer,
adapter and serializer outputs have no authority. Its potential value remains
evidence and does not invoke a T5 evaluator or issue a T5 ticket.

The V1 state preimage is derived from the V2 root source and V3 MISS only; V4
owner/scope receipts are independently replayed after the new state ID exists
and may enter the final admission sidecar, but are not encoded into the state
before classification. V4 E1/candidate data is excluded entirely. V6 now binds
the already-issued V4 scoped occurrence to this precise V1 source ID as a pure
sidecar, rather than reusing its V2 ID; it still carries no generic E1 or
successor authority.

The sidecar must preserve gaps `[3,7,11]`, `next_unchecked_gap=15` and
`global_exhaustion=false`, and must keep successor, E1--E5 and queue authority
false.

### 1. Completed conditionally: V6 source rebind without successor authority

V6 proves the object correspondence required to name the exact V1 source in
later work. It explicitly maps the V4 V2 source occurrence to the V5 V1 base
state and preserves the finite prefix scope. It does not issue a structured E1
receipt, admit a branch, construct a target, or run a T5 comparison. Before a
producer consumes this map, an independently reviewed exact-HEAD authority
layer must freeze its policy, loader/orchestration path and replay boundary.

### 2. E2 deterministic target projection

Freeze one canonical target schema and projector whose only inputs are the
accepted V4 receipt and exact source preimages.  It must serialize every legal
target field, not just `(R,K,A)`, and recompute

```text
major_phase       = TYPEI
type_i_protocol   = CHARGED
provenance_kind   = FULL_CARRIER_POST_G
full_carrier_scope= true
support A         = 1
chart             = (p,R,K)
mark_kind         = ROOT_SOL
```

The E2 projector must not accept caller-provided owner, family, potential,
authority flags or a target solution.

Before E3 or admission, run a target-bound schedule that replays the
equation-level registered gaps `[3,7,11]` and the target-local anchor-sink
predicate in a fixed order.  The result remains scope-bound with
`global_exhaustion=false`; p=1201 gap 23 stays outside scope.

### 3. Common target owner and E3 normal form

Pass the serialized target through the actual frozen persistent-state facts
validator and all fifteen V1 family predicates.  Prove that the unique owner is
`type_i_full_carrier_post_g`, with the exact V1 owner digest and no specialized
family overlap.  Then verify the source and target from raw integers and issue
an E3 receipt that is suitable for common selector re-entry.

This target classifier must be a distinct target-side authority.  The current
V4 root owner is scoped to `ROOT_SOURCE_DISPATCH_ONLY` and cannot be reused as
target admission merely because both use the V1 grammar.

### 4. E4 universal identity lift

Issue a separate E4 receipt for the explicit map

\[
\Phi:\operatorname{Sol}(p)\longrightarrow\operatorname{Sol}(p),
\qquad \Phi(u)=u.
\]

The verifier must establish the statement for the whole target solution set,
bind the exact source and target state IDs, and show that the formula reads no
unknown solution.  A boolean copied from the existing math replay is not E4
authority.

### 5. E5/T5 phase-drop ticket

Recompute both full seven-component T5 potentials from the accepted persistent
source and final target.  The expected ticket is a `PHASE_DROP` from
`TYPEII_G_HANDOFF` to `TYPEI`; it must be issued by the fixed T5 admission
contract, not by the E2 projector or edge assembler.  Bind the no-return rule
that forbids a Type-I target from re-entering the Type-II G handoff phase.

### 6. Common edge admission and re-entry

Only after E2, E3, E4 and E5 independently replay should a new coordinator
extension grant a phase-root producer/branch and combine the five receipts into
one `verified_edge`.  The final target must enter the same common persistent
state grammar and selector runtime used by every other family.  Queue or
enqueue authority, if introduced, must be a separate explicit grant and must
remain absent from all failed or partial paths.

## Acceptance criteria for the next handoff

The phase-root pilot is ready for independent review only when it demonstrates:

- p1201 and p2521: V3 prefix MISS, V5 base admission under the selected-commit
  trust condition, V6's V4-to-V5 pure rebind, and then either a separately
  reviewed V6 exact authority layer or an independently authorized target path;
  only after that deterministic E2 target, unique target owner/E3, universal
  E4, strict E5 and common target admission/re-entry may be evaluated;
- p73, p193 and p241441: production HIT still preempts the producer before E1;
- gap-23 evidence cannot alter the registered-prefix scope or become global
  exhaustion;
- cross-source, cross-HEAD, target-field, owner, lift and T5-ticket swaps fail
  closed;
- no direct receipt serializer, caller boolean or local schema validation can
  issue producer, admission or queue authority;
- the published commit passes exact-HEAD replay after integration.

Even after this pilot succeeds, it closes only one q=1 phase-root edge.  It does
not prove the downstream Type-I selector total, reachable-state exhaustion or
T6 global totality.
