# T6 Phase 2 q=1 root prefix-scoped E1 handoff

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

## Inputs downstream work may rely on

For the same exact HEAD, downstream work may consume only a V4 receipt whose
entire chain independently replays:

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

## Next phase: complete one phase-root E2--E5 pilot

The next minimal theorem should convert the accepted V4 occurrence into one
fully replayable q=1 G to Type-I phase-root edge.  Keep the work in the
following dependency order.

### 1. E2 deterministic target projection

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

### 2. Common target owner and E3 normal form

Pass the serialized target through the actual frozen persistent-state facts
validator and all fifteen V1 family predicates.  Prove that the unique owner is
`type_i_full_carrier_post_g`, with the exact V1 owner digest and no specialized
family overlap.  Then verify the source and target from raw integers and issue
an E3 receipt that is suitable for common selector re-entry.

This target classifier must be a distinct target-side authority.  The current
V4 root owner is scoped to `ROOT_SOURCE_DISPATCH_ONLY` and cannot be reused as
target admission merely because both use the V1 grammar.

### 3. E4 universal identity lift

Issue a separate E4 receipt for the explicit map

\[
\Phi:\operatorname{Sol}(p)\longrightarrow\operatorname{Sol}(p),
\qquad \Phi(u)=u.
\]

The verifier must establish the statement for the whole target solution set,
bind the exact source and target state IDs, and show that the formula reads no
unknown solution.  A boolean copied from the existing math replay is not E4
authority.

### 4. E5/T5 phase-drop ticket

Recompute both full seven-component T5 potentials from the accepted persistent
source and final target.  The expected ticket is a `PHASE_DROP` from
`TYPEII_G_HANDOFF` to `TYPEI`; it must be issued by the fixed T5 admission
contract, not by the E2 projector or edge assembler.  Bind the no-return rule
that forbids a Type-I target from re-entering the Type-II G handoff phase.

### 5. Common edge admission and re-entry

Only after E2, E3, E4 and E5 independently replay should a new coordinator
extension grant a phase-root producer/branch and combine the five receipts into
one `verified_edge`.  The final target must enter the same common persistent
state grammar and selector runtime used by every other family.  Queue or
enqueue authority, if introduced, must be a separate explicit grant and must
remain absent from all failed or partial paths.

## Acceptance criteria for the next handoff

The phase-root pilot is ready for independent review only when it demonstrates:

- p1201 and p2521: V3 prefix MISS, V4 scoped E1, deterministic E2 target,
  unique target owner/E3, universal E4, strict E5 and common re-entry;
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
