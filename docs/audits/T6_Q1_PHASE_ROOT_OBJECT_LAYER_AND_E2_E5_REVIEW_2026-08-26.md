# T6 q=1 phase-root object layer and E2--E5 review

Date: 2026-08-26

Reviewed baseline: exact-HEAD V4 root registered-prefix scoped E1 at
`2d768c1392a41f96d02e14755589bc1e8de5e796`.

## Verdict

```text
V4 source occurrence and registered-prefix E1       ESTABLISHED
E2 phase-root arithmetic and canonical facts        ESTABLISHED MATHEMATICALLY
E3 target V1 owner uniqueness                       ESTABLISHED MATHEMATICALLY
E4 universal identity lift                          ESTABLISHED MATHEMATICALLY
E5 canonical N7 phase drop                          ESTABLISHED MATHEMATICALLY
V4 source as a common persistent V1 state           NOT ESTABLISHED
E2--E5 authority receipts / verified successor      NOT ISSUED
Persistent admission / queue mutation               OPEN
```

The main new result of this review is not another arithmetic formula.  It is a
precise separation between a closed mathematical kernel and an unresolved
object/authority boundary.  The V4 source is an actual root occurrence, but it
is a `RawRootSourceStateV2` with `persistent_admission=false`; it is not an
admitted `PersistentSelectorStateV1` parent.  A normal V1 successor cannot be
issued from it until that mismatch is repaired.

## 1. Mathematical kernel

Let an exact-HEAD V4 receipt accept an actual parentless ordinary q=1 G root
for the core prime

\[
p=24t+1,
\qquad X=\frac{p+3}{4}=6t+1.
\]

Define

\[
R=16t+3,
\qquad K=X(16t+1),
\qquad A=1.
\]

Then

\[
4K=pR+1,
\qquad 3\le R\le p-2,
\qquad X\mid K,
\qquad p\nmid K.
\]

The target-side source is

\[
(p,R(p-1)-p,p-1)\longrightarrow(1,R-1,1),
\]

with p-edge shift 1 and gcd reduction 1.  These identities are already
independently replayed by the V4 consumer and the earlier independent
phase-root verifier.

### 1.1 E2 canonical projection

The V1 target facts are forced to be

```text
major_phase=TYPEI
type_i_protocol=CHARGED
t5_eta_p=0
pre_a=null
absorb_m=null
absorb_r_epsilon=0
reset_carrier=null
endpoint_fiber=NONE
relation_q=null
provenance_kind=FULL_CARRIER_POST_G
full_carrier_scope=true
atomic_arm=NONE
dispatch_status=NONE
proper_root_k=null
proper_root_height_class=NONE
proper_root_height=null
proper_root_r=null
is_overflow=false
support_A=1
carrier_M=null
overflow_d=null
chart_R=R
chart_K=K
sink_scc_receipt=false
same_chart_promotion_receipt=false
```

The inequality `is_overflow=false` is not a declaration: since
`p-R=8t-2>0`, it follows from the formula.  The provenance and fresh scope do
not follow from the chart alone; they must remain bound to the V4 source
lineage.

The low full-carrier chart is unique.  If another low chart has `X | K'`, the
chart equation gives `3R' = 1 (mod X)`.  Together with `R' = 3 (mod 4)`, this
puts `R'` in the same residue class as `R` modulo `4X`.  The allowed low
interval has width less than `4X`, hence `R'=R` and then `K'=K`.

### 1.2 E3 owner uniqueness

For this exact ROOT_SOL target, the frozen V1 facts validator accepts the
facts above.  Of all fifteen predicates:

- the generic, Type-II, H4, C8, C2, proper-root and ABSORB predicates fail by
  mark, phase, protocol or provenance;
- all four overflow predicates fail because `R<p` and `is_overflow=false`;
- `type_i_full_carrier_post_g` is true.

Thus the match set is the singleton

```text
[type_i_full_carrier_post_g]
```

and its zero-based precedence index is 14.  There is no overlap.  This is a
lineage-sensitive theorem: changing `full_carrier_scope` to false leaves a
V1-valid chart with no matching family, while changing provenance may select a
different owner.

Direct controls against the actual frozen V1 validator and all predicates
passed for

```text
p=1201: (t,X,R,K)=(50,301,803,241101)
p=2521: (t,X,R,K)=(105,631,1683,1060711)
```

### 1.3 E4 universal lift

Both endpoints represent the same marked equation interface

\[
W_S=W_T=\operatorname{Sol}(4,p).
\]

For every `u in W_T`, define

\[
\Phi_p(u)=u.
\]

This is total even if the set is empty, does not select or inspect an unknown
solution, and sends every target solution to a source solution because the
equation and ROOT_SOL mark are identical.  An authority receipt must still
bind the two concrete state IDs and independently reconstructed equation
interfaces; the string `identity` alone is not such a receipt.

### 1.4 E5 phase drop

The frozen seven-component potential gives

\[
\Pi(S)= (p,3,0,0,0,0,0)
\]

for the q=1 G source, and

\[
\Pi(T)=
\left(p,2,4,\frac{(p-1)^2}{4},K,0,0\right)
\]

for the Type-I CHARGED target.  The first differing coordinate is the major
phase, `3 -> 2`; therefore the ticket is `PHASE_DROP`, regardless of the later
protocol and local coordinates.  At the same equation rank, the reverse
`2 -> 3` transition cannot receive any T5 ticket.

The concrete target potentials are

```text
p=1201: (1201,2,4,360000,241101,0,0)
p=2521: (2521,2,4,1587600,1060711,0,0)
```

These four subsections close the mathematical content needed by E2--E5.  They
do not issue E2--E5 authority receipts.

## 2. Critical object mismatch

The V4 source object has a V2 root-source state ID and explicitly denies
persistent admission and queue authority.  `PersistentSelectorRuntimeV1`
accepts a successor source only when the exact V1 state is already in its
admitted-state set.  Passing the V4 state directly would therefore fail with
`SOURCE_NOT_ADMITTED`; copying its V2 state ID into a V1 state would be a type
and provenance error.

The correct architecture is:

```text
V3/V4 actual q=1 G root
  -> materialize a new canonical PersistentSelectorStateV1
  -> common ROOT_INITIALIZER_OUTPUT admission
  -> bind V4 E1 to that new admitted V1 source ID
  -> ordinary phase-root successor pipeline
```

The alternative of making the Type-I target itself the initializer output
would remove the G state from the persistent reachable domain and turn the
phase drop into an initializer-internal checkpoint.  That changes the existing
base-plus-successor trace, T5 and F1 quantifiers, so it is not the conservative
migration path.

## 3. Base materialization contract

The V1 q=1 G base must be reconstructed, not relabeled.  Its canonical fields
are:

```text
queue_gate=ROOT_INITIALIZER_OUTPUT
parent_state_id=null
root_context=equation_rank=p
mark=ROOT_SOL(p)
facts=the q=1 G facts independently reconstructed from the V2 root source
terminal_first=a V1 projection of the verified V3 gaps [3,7,11] MISS
source_receipt=NONTERMINAL_INITIALIZER_OUTPUT
```

The terminal projection must retain, in its external binding receipt,

```text
ordered_gaps=[3,7,11]
next_unchecked_gap=15
global_exhaustion=false
coverage_semantics=REGISTERED_PRIORITY_ONLY
```

It is a schema translation of an independently replayed V3 production result,
not a new global terminal theorem.  The terminal wire and V1 state preimage
must not contain the V4 owner or scope-validation digest: state identity must
remain prior to classification.  Only after the V1 state ID exists may the
admission verifier compare its independently recomputed facts, match set,
owner and precedence with V4.  The V1 owner digest cannot equal or copy the V4
owner digest, which is bound to the V2 root-source state ID.

A direct non-authorizing construction check for p=1201 and p=2521 produced
valid V1 initializer states, unique owner `type_ii_relation_g_endpoint` at
precedence index 2, and potentials

```text
(p,3,0,0,0,0,0).
```

This demonstrates that the field mapping is feasible.  It does not grant the
provisional serializer or those provisional state IDs admission authority.

## 4. Minimal next authority DAG

The next registry extension should add exactly two roles:

1. `Q1_ROOT_V1_BASE_MATERIALIZER`: emits the canonical V1 state wire and the
   explicit V2-to-V1 equivalence binding; it has no admission or queue power.
2. `INDEPENDENT_Q1_ROOT_V1_BASE_ADMISSION_VERIFIER`: does not import or call the
   materializer; it independently replays V3/V4, reconstructs the expected V1
   state, runs the frozen V1 facts/extractor/classifier and T5 evaluator, and is
   the only role allowed to issue `persistent_admission=true`.

The deterministic V3-MISS-to-V1-terminal adapter, exact-HEAD orchestrator,
serializer and post-issuance replayer remain pinned non-roles.  The admission
verifier must keep

```text
successor_authority=false
producer_authority=false
E1/E2/E3/E4/E5 authority=false
reentry_authority=false
queue_authority=false
```

Base admission and enqueue are distinct permissions.

After this base gate is independently closed, the successor DAG is:

```text
admitted V1 q=1 G source
  -> frozen phase-root producer/branch
  -> V4 E1 adapter bound to the new V1 source ID
  -> deterministic E2 projector
  -> target-bound terminal scheduler/verifier/issuer
  -> target E3 owner verifier
  -> E4 identity verifier
  -> E5/T5 verifier
  -> non-role edge assembler
  -> common target-admission verifier
  -> separate queue grant, if later authorized
```

For the target schedule, equation-level gaps `[3,7,11]` must be replayed under
the target subject, followed by the target-local anchor-sink check.  At this
phase root `R-1` is even while `K` is odd, so the anchor-sink predicate always
misses.  The total target result is still only a registered finite-scope MISS.
At p=1201, the gap-23 Type-I d=34 certificate remains outside that scope; if a
future schedule includes gap 23, terminal-first must preempt admission.

## 5. Explicit non-results

This review does not establish or authorize:

- V1 base admission for the q=1 G source;
- a source-ID-adapted successor E1;
- target terminal issuance;
- E2--E5 authority receipts;
- a verified successor, common target admission or re-entry;
- queue mutation;
- Gate 2, complete Gate 4, Gate 5, F1/F2/F3, T6 or Erdős--Straus.

The global checklist therefore remains entirely unchecked.
