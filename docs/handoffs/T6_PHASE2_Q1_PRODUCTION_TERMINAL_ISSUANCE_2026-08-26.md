# T6 Phase 2 q=1 production terminal issuance handoff

Date: 2026-08-26

## Established subgate

The parentless ordinary `q=1 G` root path now has a production issuance and
post-issuance replay layer:

```text
raw q1 G + exact HEAD
  -> authorized root initializer occurrence
  -> non-authorizing exact-HEAD terminal decision assembler
  -> TERMINAL_ISSUER
  -> root-terminal HIT or registered-prefix MISS receipt
  -> independent exact-HEAD receipt replay
```

Coordinator registry v3 grants exactly four roles:

```text
ROOT_INITIALIZER
TERMINAL_ISSUER
TERMINAL_SCHEDULER
INDEPENDENT_COVERAGE_VERIFIER
```

The assembler and production receipt verifier remain pinned non-role
dependencies. E1, queue, producer, branch and T5 authority remain false.

## Receipt semantics

The HIT receipt binds a reconstructible Type I/II certificate and verifies the
root equation. It closes only that root occurrence:

```text
terminal_leaf_authority          = true
root_proof_close_authority       = true
registered_prefix_miss_authority = false
global_exhaustion                = false
```

The MISS receipt is deliberately narrower:

```text
outcome                           = MISS_REGISTERED_PRIORITY_COMPLETE
ordered_gaps                      = [3, 7, 11]
next_unchecked_gap                = 15
global_exhaustion                 = false
terminal_leaf_authority           = false
registered_prefix_miss_authority  = true
root_proof_close_authority        = false
```

It cannot be consumed as the legacy unqualified `MISS_COMPLETE` and carries no
producer continuation authority.

## Exact controls

Production issue followed by issuer-independent receipt replay succeeds for:

```text
p=73       Type II gap-7 root HIT
p=193      Type I gap-7 root HIT
p=241441   gap-11 root HIT
p=1201     registered gaps-3/7/11 MISS
p=2521     registered gaps-3/7/11 MISS
```

Unresealed HIT/MISS exchange, prefix-to-global promotion, authority, state,
grant and HEAD changes fail at the schema or outer-seal layer. The deeper
control records an important trust boundary: an internally coherent `p=73`
receipt can be resealed locally with a `p=1201` body/anchor/state chain, so the
local serializer is not an authority verifier. The test confirms local
acceptance before the independent replayer rebuilds the expected root chain
from raw input and rejects that receipt.

Registry artifacts carry transitive dependency semantic pins. The current
controlled loaders additionally freeze loader/caller AST, executable paths and
call tables against the dependency manifest. This is a theorem about the fixed
policy and bytes, not a general decision procedure for arbitrary Python. A
change to the loader contract, resolver or explicit pins creates a new authority
policy and requires a new review.

## Remaining boundary

This handoff does not establish common owner classification, a scope-aware E1
consumer, E2--E5, a producer branch, target re-entry or queue mutation. Complete
Gate 4, Gate 5, F1, F2, F3 and T6 remain open. The next minimal integration step
is:

```text
production registered-prefix MISS
  -> common q1 root owner receipt
  -> prefix-aware E1 policy
  -> terminal-first q1 handoff pilot
```

The prefix-aware E1 policy must preserve `next_unchecked_gap=15` and may not
infer global terminal exhaustion.
