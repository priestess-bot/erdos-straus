---
kind: claim
claim_id: t6-q-one-phase-root-prestate-v2-nonauthorizing-construction
title: q=1 phase-root 的零权限 V2 prestate 构造
statement: >-
  Given a core prime p whose q=1 G factorization is independently recomputed
  and an externally supplied, explicitly non-E1 V1-source binding, the
  prestate constructor deterministically seals P, C, L, D, A, and, only after
  a finite target-scope MISS, Q=PhaseRootTargetPrestateV2. P is the canonical
  full-carrier chart; C is a pinned V1 predicate preclassification; L replays
  Bradford gaps 3,7,11 and anchor-sink in finite scope; D is target-only N7
  coordinates; A binds the lower-rank objects; Q has a content-addressed
  semantic state ID and only an A-origin reference. A finite HIT preempts A
  and Q. The construction has no owner digest, E1--E5 receipt, ticket,
  admission, producer, queue, or re-entry authority.
claim_status: established
proof_provenance: repository_derivation
review_status: independent_review
depends_on:
  - type-II-q-one-full-carrier-phase-root-entry
  - t6-q-one-phase-root-target-terminal-transport-anchor-miss-v1
  - t6-persistent-selector-state-v1
topics:
  - T6
  - q-one
  - phase-root
  - prestate
  - content-addressing
  - terminal-first
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-phase-root-entry
    role: canonical full-carrier target formula
  - claim: t6-q-one-phase-root-target-terminal-transport-anchor-miss-v1
    role: finite target terminal scope and anchor-sink miss
  - concept: t6-persistent-selector-state-v1
    role: predicate semantics and V1 successor-cycle boundary
  - reproduction: scripts/t6_q_one_phase_root_prestate_v2.py
    role: strict V2 prestate construction and replay
visibility: public
last_checked: '2026-08-27'
---

# q=1 Phase-Root Prestate V2

## Construction

The implementation constructs only the strict acyclic prefix

~~~text
P -> {C, L, D} -> A -> Q.
~~~

P recomputes

\[
p=24t+1,\qquad X=6t+1,\qquad
R=16t+3,\qquad K=X(16t+1),
\]

and verifies the complete q=1 G factorization of \(X\). Its facts are the
canonical ROOT_SOL, TYPEI, CHARGED, FULL_CARRIER_POST_G V1 semantic facts.

C loads the V1 state-contract module from its sibling absolute path under a
private module name, pins its exact source bytes, and evaluates its public
fifteen family predicates on a minimal local predicate view. The unique result
is the predicted label type_i_full_carrier_post_g at index 14. This is a
preclassification, not an owner digest or E3.

L accepts only ExternalQOneSourceBindingV2. Its binding scope is fixed to
EXTERNAL_Q1_SOURCE_PREIMAGE_NOT_E1, so it records source identity material
without claiming source actualness. It replays the ordered target families

~~~text
Bradford gap 3
Bradford gap 7
Bradford gap 11
phase-root anchor sink
~~~

with global_exhaustion=false. A HIT has next_unchecked_gap=null and prevents
construction of A and Q.

D seals only

\[
\Pi_T=\left(p,2,4,\frac{(p-1)^2}{4},K,0,0\right)
\]

with status TARGET_ONLY_NO_TICKET. A binds the external source binding and
the four lower-rank artifacts. Q is a NONAUTHORIZING_Q1_PHASE_ROOT_TARGET
state whose identity depends only on the canonical target semantics and the
two-field A-origin reference.

All artifacts use exact-field mappings, type-sensitive canonical JSON,
recomputed SHA-256 seals, and content IDs. Parsing replays the complete
lower-rank construction. The public serializer additionally performs
non-recursive semantic checks, so a hand-built object with a recomputed but
semantically false seal cannot be exported.

## Controls

The focused suite establishes:

| Input | finite result | Q |
|---:|---|---|
| \(p=73\) | gap-7 HIT | absent |
| \(p=1201\) | [3,7,11,anchor] MISS | constructed |
| \(p=2521\) | [3,7,11,anchor] MISS | constructed |
| \(p=97\) | not q=1 G | rejected |

Negative controls reject type-confused false/0 wires with or without
resealing, foreign dependency artifacts, owner/bundle/E1/admission/queue
fields, preloaded contract-module substitution, and a manually constructed
semantic Q forgery.

## Boundary

The external source binding deliberately remains opaque. It prevents direct
use of a prestate object as a source artifact, but it does not authenticate
actual source occurrence, V1 admission, or generic E1. Any later bundle or
admission layer must independently parse and authenticate the real V1 source
wire through an exact-HEAD coordinator registry.

This construction is not E2 issuance: it has no actual E1 premise, no final
owner/E3, no E4, no E5, no producer, no terminal-complete schedule, and no
queue or recursive re-entry. It does not change F1, F2, F3, T6, or the
Erdős--Straus conjecture.
