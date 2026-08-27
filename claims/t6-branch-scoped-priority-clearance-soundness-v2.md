---
kind: claim
claim_id: t6-branch-scoped-priority-clearance-soundness-v2
title: T6 branch-scoped priority clearance 对 policy-relative 递降的充分性 v2
statement: >-
  固定一个 coordinator-owned、全序且可重放的决策 policy pi。对 actual reachable
  source S 和 branch b，若 b 的 guard 成立，pi 中每个严格先于 b 的 terminal action
  重放为 MISS、每个严格先于 b 的 producer guard 重放为 false，并且 b 给出 actual
  E1、deterministic E2、legal E3、universal E4 与 strict E5，则 S->T 是 sound
  deterministic rank-decreasing reduction candidate。只有再加入 common admission、
  cross-bound independent bundle 与 recursive re-entry，才能升级为 runtime verified
  edge 并进入 T5 归纳。当前 Goal 仍要求 complete terminal schedule 和
  terminal-over-producer preemption，本命题不替代该验收门。该结论明确
  global_exhaustion=false，不能把 priority-prefix MISS 重命名为 MISS_COMPLETE；
  V1 合同保持不变。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-t5-full-contract-level-global-well-foundedness
  - t6-terminal-miss-scope-taxonomy-v2
  - denominator-escape-state-contract
topics:
  - T6
  - E1
  - branch-selection
  - terminal-first
  - policy-precedence
  - well-foundedness
  - proof-boundary
sources:
  - claim: type-I-t5-full-contract-level-global-well-foundedness
    role: verified-edge strict rank and well-founded induction
  - claim: t6-terminal-miss-scope-taxonomy-v2
    role: registered-priority versus terminal-universe miss separation
  - concept: denominator-escape-state-contract
    role: E1--E5 transition semantics
visibility: public
last_checked: '2026-08-27'
---

# T6 branch-scoped priority clearance 对 policy-relative 递降的充分性 v2

## 1. Frozen policy semantics

Let \(\mathcal D(S)=(a_0,\ldots,a_{N-1})\) be the finite decision list
registered for the owner of an actual reachable state \(S\), with a
coordinator-owned order. A decision is either a terminal action or a producer
branch. If the selected producer branch is \(b=a_j\), define

\[
\operatorname{Prior}_\pi(b,S)=(a_0,\ldots,a_{j-1}).
\tag{1}
\]

The branch-clearance predicate is

\[
\operatorname{Clear}_\pi(b,S)
\Longleftrightarrow
\operatorname{Guard}_b(S)
\land
\bigwedge_{i<j}
\begin{cases}
\operatorname{MISS}_{a_i}(S),&a_i\text{ is terminal},\\
\neg\operatorname{Guard}_{a_i}(S),&a_i\text{ is producer}.
\end{cases}
\tag{2}
\]

A prior terminal HIT terminates; a prior producer with true guard selects that
earlier branch. Neither outcome may be relabeled as clearance. Each policy row
must bind its action kind, evaluator, guard or certificate contract, and replay
identity. The receipt says nothing about decisions after \(b\), and nothing
about terminal families absent from \(\mathcal D(S)\).

The branch-selection constants are

~~~text
clearance_outcome = MISS_HIGHER_PRIORITY_POLICY_COMPLETE
coverage_semantics = REGISTERED_HIGHER_PRIORITY_ONLY
completeness_scope = BEFORE_SELECTED_BRANCH_ONLY
terminal_universe_status = NOT_ASSERTED_NOT_REQUIRED
global_exhaustion = false
~~~

These constants are distinct from an upstream q1 prefix receipt's
MISS_REGISTERED_PRIORITY_COMPLETE result.

## 2. Policy-relative reduction theorem

Assume (2), and assume branch \(b\) supplies mutually cross-bound receipts for

\[
E1_{\rm actual}(S,b),\qquad E2(S,b)=T,\qquad E3_{\rm legal}(T),
\]

\[
E4:\operatorname{Sol}(T)\longrightarrow\operatorname{Sol}(S),
\qquad
\Pi_{T5}(T)<\Pi_{T5}(S).
\tag{3}
\]

Then \(S\to T\) is a sound deterministic rank-decreasing reduction candidate.
E1 binds the actual occurrence and lineage; E2 fixes the target; legal E3
types the target; E4 lifts every target solution; and E5 strictly decreases
the globally fixed well-founded potential.

Suppose another terminal certificate for \(S\) exists outside the quantified
policy prefix. Its mathematical existence does not falsify any term in (3);
it only means that another proof of \(\operatorname{Sol}(S)\) was available.
This proves route soundness, not compliance with a particular selector's
terminal-preemption rule.

To upgrade the candidate to a runtime verified recursive edge, additionally
require a common-admission receipt for \(T\), one independently replayed bundle
that cross-binds selection and E1--E5, and recursive re-entry
\(T\in\mathcal R_p\). If the resulting selector is total on
\(\mathcal R_p\), well-founded induction on \(\Pi_{T5}\) proves every state in
\(\mathcal R_p\) has a solution. This induction does not require
\(\operatorname{TerminalUniverseMiss}(S)\), but it does require admission and
re-entry closure.

## 3. Determinism controls

Determinism requires the complete ordered prior-decision list. The policy
digest, source owner/domain, selected route, producer, branch and index,
action/evaluator digests, and every replay result must be bound into the
selection receipt. If an action is inserted before \(b\), the policy digest
and index change and the old receipt is invalid.

Two exact algebraic controls expose the distinction:

- \(p=1201\) misses gaps \([3,7,11]\), has a gap-23 Type-I terminal, and has
  the valid q1 phase-root reduction formula.
- \(p=2521\) misses the same prefix, has a gap-23 Type-II terminal, and has
  the same valid reduction formula.

Under a hypothetical policy that places the phase-root branch before gap 23,
the phase-root arithmetic remains a sound reduction candidate. If gap 23 is
inserted before the branch, the terminal must preempt and the old branch
receipt fails its policy binding. These controls do not currently possess an
authoritative selection receipt, E1--E5 bundle, admission or re-entry.

## 4. Contract separation

The existing E1OccurrenceReceiptV1 continues to require MISS_COMPLETE and must
not be weakened or used as a parser for this result. V2 separates:

~~~text
E1OccurrenceReceiptV2
  actual source / parent / lineage / integer occurrence

BranchSelectionReceiptV2
  exact policy and complete prior-action clearance
~~~

An independent replay receipt must bind both by receipt ID/digest and recheck
equality of HEAD, source, owner/domain, policy, route, producer and branch.
No prefix wire may be relabeled as a global miss, and no V2 receipt may be
downcast into V1. A q1 registered-prefix receipt remains a distinct upstream
object with its own result; it is not a second set of constants for
BranchSelectionReceiptV2.

## 5. Current Goal compatibility

The current Goal's Gate 4 requires a matching terminal to preempt a producer,
and Gate 5 requires a complete source terminal schedule. Therefore a
Goal-compatible corollary needs one further policy theorem:

\[
\boxed{
\text{every registered terminal that can overlap }b\text{ precedes }b,
\quad\text{or its guard is disjoint from }\operatorname{Guard}_b.
}
\tag{4}
\]

Together with a complete owner/domain terminal schedule, (4) reduces the Goal
dispatch to the prior-clearance theorem above. Without it, branch-scoped V2 is
an alternative policy-relative research result and does not pass Gate 4 or 5.

## 6. Boundary

This theorem establishes the logical sufficiency of branch-scoped priority
clearance for a policy-relative reduction, plus the exact extra hypotheses
needed for a verified recursive edge. It does not issue E1 or authorize a
producer. O1 still requires a global proof that the coordinator policy covers
every reachable state and intended action. V7 policy authentication, a
Goal-compatible complete terminal schedule, E1 issuance, E2--E5, common
admission, queue mutation and re-entry all remain separate obligations. F1,
F2, F3 and T6 remain OPEN.
