# T6 q=1 Phase-Root Prestate V2 Boundary

Date: 2026-08-27

## Result

The intended phase-root construction order can be acyclic, but its object
named Q cannot be an admissible PersistentSelectorStateV1. The current V1
successor wire includes a source receipt asserting E1 through E5 before the
state ID is computed, while the independently replayable final bundle needs
the target state ID and final owner digest. Treating that assertion as a
placeholder would either assert an unproved edge or create a content-ID cycle.

The narrow next construction is therefore a non-authorizing
PhaseRootTargetPrestateV2, followed by final owner and receipt objects. It
does not authorize E2, E3, E4, E5, a producer, admission, queue mutation, or
recursive re-entry.

## Mathematical Input

For an ordinary q=1 G input, put

\[
p=24t+1,\qquad X=6t+1,\qquad
R=16t+3,\qquad K=X(16t+1).
\]

Among low full-carrier charts, the target is uniquely fixed by

\[
4K=pR+1,\qquad A=1,\qquad X\mid K,\qquad 3\le R\le p-2.
\]

Its semantic facts are ROOT_SOL, TYPEI, CHARGED,
FULL_CARRIER_POST_G, full_carrier_scope=true, support_A=1, and
is_overflow=false. The frozen V1 predicate table has the unique predicted
label type_i_full_carrier_post_g at index 14. It does not yet have a final
persistent-state owner digest.

The target finite terminal scope can independently replay the p-only
Bradford prefix [3,7,11] and the target-local anchor-sink miss

\[
\gcd(R-1,K)=1.
\]

Its outcome must remain a finite MISS_SCOPE with
next_unchecked_gap=15 and global_exhaustion=false. It is not MISS_COMPLETE.

## Required DAG

Take the exact source state and fixed registry/policy inputs as external
rank \(-1\) data. The only permitted construction order is:

~~~text
0  P  pure canonical target preprojection
1  C  target predicate preclassification
1  L  target-bound finite terminal witness
1  D  target T5 coordinate draft
2  A  edge anchor
3  Q  PhaseRootTargetPrestateV2
4  O  final owner classification and owner digest
5  B  independently replayable E1--E5 bundle
6  admission sidecar and, only if authorized, queue mutation
~~~

| Object | Required inputs | Forbidden fields |
|---|---|---|
| P | \(p,t,X,R,K,A=1\), target facts, ROOT_SOL mark, fixed schema/rule version | source, terminal, owner, potential, state, edge, transition, admission |
| C | P, fixed grammar/predicate/precedence pins, complete match vector | state ID, owner digest, E3/admission conclusion |
| L | source ID/digest, P, exact finite schedule and every replay digest | target state ID, final owner, complete terminal claim |
| D | P, fixed taxonomy pin, \(\Pi_T=(p,2,4,B_p,K,0,0)\) | source potential, ticket, state ID |
| A | source, candidate witness, P/C/L/D IDs and digests | Q/O/B, transition ID, admission |
| Q | P facts and mark, exactly one successor_origin=(A.id,A.digest) | owner, bundle, E1--E5, ticket, queue/admission |
| O | Q.state_id, facts digest, full match vector and precedence | write-back into Q |
| B | all prior objects plus independent verifier and registry pins | mutation of any prior object |

Every reference runs from a lower rank to a higher rank. If a future terminal
policy depends on an owner-domain choice, then L must depend on C; it must
never depend on O.

## V1 Cycle

PersistentSelectorStateV1 accepts an ADMITTED_SUCCESSOR only after its
source_receipt contains exact fields including:

~~~text
parent_state_id, E1, E2, E3, E4, E5, T5_ticket
~~~

All five booleans must already be true. The extractor validates this receipt
before it recomputes:

~~~text
state_id = hash(full raw state).
~~~

In the legacy V1 model, the owner digest in turn hashes state_id, facts
digest, owner, match vector, and precedence index. Hence:

~~~text
V1 successor state ID
  -> requires source receipt asserting E1--E5
  -> final receipt bundle needs target state ID and owner digest
  -> owner digest needs target state ID.
~~~

False, null, pending, or missing booleans fail the V1 schema. True is not an
honest placeholder, and replacing it after bundle replay changes the sealed
receipt and state ID. Embedding a future bundle or transition digest in the
prestate yields the explicit cycle Q.state_id -> B -> Q.state_id.

The V1 owner field is also explicitly excluded from its state identity input.
It cannot be computed early and written back into Q.

## Recommended Boundary

Introduce a V2 pre-admission boundary with two disjoint shapes:

~~~text
PhaseRootTargetPrestateV2
PersistentSelectorStateV2
~~~

The first is content-addressed from P and A only and is never queueable. The
second may exist only after Q, O, B, and an exact-HEAD,
coordinator-owned admission gate independently replay. Existing V1 facts and
predicates may be retained as semantic checks, but the V1 successor receipt
and V1 owner-digest string format cannot be reused as the prestate wire.

The alternative bridge through a provisional V2 object and a later V1
successor produces two state IDs and requires a separate equivalence theorem.
It is not the minimal path.

## Controls and Boundary

The target finite schedule must terminal-preempt p=1201 and p=2521 if it adds
gap 23. Conversely, p=21169 is q=1 G and misses the complete Bradford
screens at gaps [3,7,11,15,19,23]; it prevents that finite prefix from being
mislabeled a complete terminal universe. These are scope controls, not target
terminal receipts.

This handoff is a Phase-2 interface reduction only. It does not close F1,
F2, F3, T6, or the Erdős--Straus conjecture.
