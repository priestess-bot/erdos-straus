# T6 Branch-Scoped E1 V2 Boundary (2026-08-27)

## Result

A mathematically sound rank-decreasing reduction does not require proof that
every possible terminal certificate for its source is absent. It does require
an actual source occurrence and complete replay of every coordinator action
ordered before the selected branch:

~~~text
prior terminal action -> MISS
prior producer action -> GUARD_FALSE
selected producer      -> GUARD_TRUE
~~~

The proposed V2 structural foundation therefore uses:

~~~text
MISS_HIGHER_PRIORITY_POLICY_COMPLETE
REGISTERED_HIGHER_PRIORITY_ONLY
BEFORE_SELECTED_BRANCH_ONLY
terminal_universe_status = NOT_ASSERTED_NOT_REQUIRED
global_exhaustion = false
~~~

This is policy-relative route clearance, not a relabeling of prefix MISS as a
global terminal miss.

## Soundness Controls

\(p=1201\) and \(p=2521\) both miss gaps \([3,7,11]\), have a gap-23 terminal,
and have the ordinary q1 phase-root reduction formula. Under a hypothetical
policy that places the producer before gap 23, the reduction arithmetic
remains sound. If gap 23 is placed before the producer, terminal preemption
invalidates the old policy/index receipt.

These are algebraic and policy-mutation controls. Neither input currently has
an authoritative V2 selection/E1 bundle, common admission or recursive
re-entry.

## Goal Compatibility

The current Goal has not been amended. Gate 4 requires a matching terminal to
preempt a producer, and Gate 5 requires a complete source terminal schedule.
Consequently this branch-scoped result does not close either gate.

A Goal-compatible corollary must prove that every registered terminal capable
of overlapping the selected branch either:

1. occurs before the branch in the complete owner/domain schedule; or
2. has a guard disjoint from the selected producer guard.

It must then add common admission, an independently replayed cross-bound
E1--E5 bundle, and recursive re-entry before the candidate can become a
verified recursive edge.

## Contract Boundary

The V1 structured receipt remains unchanged and continues to require
MISS_COMPLETE. The V2 foundation separates:

~~~text
BranchSelectionReceiptV2
E1OccurrenceReceiptV2
E1IndependentReplayReceiptV2
~~~

The foundation is constructor-disabled through its public API and
zero-authority. It validates canonical wires, contiguous prior decisions, a
selected-producer-pinned integer occurrence path, receipt cross-binding and
distinct replayer IDs/digests. The external authority-policy digest is kept
separate from the route-policy digest, but both remain inert caller inputs.
The copied consumed-occurrence fields are structural binding only, not
independent consumption evidence. The module does not authenticate its
caller-supplied policy, source, role grants or replay implementations, and
cannot authorize E1, a producer, admission, queue mutation or enqueue.

V3/V4/V5/V6 remain q1 substrate rather than current authoritative E1. V7
external policy authentication, a Goal-compatible complete terminal schedule,
issuer/verifier grants, E2--E5, common admission and re-entry remain absent.
F1, F2, F3 and T6 remain OPEN.
