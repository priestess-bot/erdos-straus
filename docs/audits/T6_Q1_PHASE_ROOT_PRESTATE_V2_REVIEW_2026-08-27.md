# T6 q=1 Phase-Root Prestate V2 Review

Date: 2026-08-27

Reviewed implementation:

- scripts/t6_q_one_phase_root_prestate_v2.py
- tests/test_t6_q_one_phase_root_prestate_v2.py

## Scope

This review concerns only a zero-authority prestate layer. It does not review
or authorize an E2 receipt, actual E1, final owner/E3, E4, E5, admission,
queue mutation, recursive re-entry, F1/F2/F3 closure, or T6.

## Resolved Findings

The initial review found three blocking flaws: type-confused content seals,
bare source strings that could be used to blur ranks, and a cached/self-attested
V1 predicate module. The reviewed revision resolves them as follows.

1. Every parsed artifact wire recomputes its unsigned canonical digest and
   content ID before dependency replay. Artifact equality is canonical JSON
   equality, not Python value equality. Both stale and resealed false versus
   0 mutations are rejected.
2. L, A, and Q consume a separate ExternalQOneSourceBindingV2 rather than
   bare source strings. The binding has a fixed NOT_E1 scope and is a distinct
   artifact type; P/C/L/D/A/Q cannot parse as it.
3. The V1 predicate module is freshly loaded from the sibling absolute path
   under a private name and its bytes are hashed into C. The replay checks the
   complete family vector, the expected owner label, and precedence index 14.
4. C uses a minimal local predicate view, not VerifiedSelectorHeaderV1; it
   cannot be passed to the V1 owner classifier to produce an owner digest.
5. The public serializer performs local semantic validation after checking the
   seal. A manually constructed, correctly resealed Q with a forged
   prestate_kind is rejected.

The q=1 G factorization, finite terminal HIT preemption, exact target facts,
and target-only N7 coordinate draft were also independently replayed on
\(p=73,1201,2521\).

## Verdict

~~~text
ACCEPT as a zero-authority PhaseRootTargetPrestateV2 construction.
NOT an E2/E3/E4/E5 or source-actualness result.
NOT an admission, producer, queue, re-entry, F1/F2/F3, T6, or conjecture result.
~~~

## Residual Risk

ExternalQOneSourceBindingV2 is intentionally an opaque non-E1 wrapper. A
caller can rewrap arbitrary identity strings, including a prestate ID, but
that creates no authority in this module. A future authority layer must not
trust this wrapper as actual source provenance; it must independently parse
and authenticate the real V1 source wire against the exact-HEAD registry.

Trial division and complete square-divisor materialization remain a
zero-authority finite replay implementation, not a resource-bounded large
prime scheduler. No theorem or runtime authority depends on their performance
outside the reviewed scope.
