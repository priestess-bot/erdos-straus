---
kind: claim
claim_id: t6-sp21-scoped-terminal-priority-safety
title: SP-21 冻结优先级策略下的 scope-bound successor safety
statement: >-
  对任意有限冻结 action policy，只要每个 action replay 确定、terminal HIT certificate
  可靠、selected producer 之前的每个 action 都实际 Pass，且 selected producer 的
  E1--E5/R 与全称 lift 已独立验证，则 selector 的实际输出要么是最早可达的 terminal，
  要么是安全的 verified successor。该结论只要求
  MISS_HIGHER_PRIORITY_POLICY_COMPLETE，明确令 global_exhaustion=false；不要求
  Sol(S) 为空或穷尽所有未注册 terminal family。具体 q=1 coordinator policy、actual
  source、authority、admission、queue 和 T6 totality 不在本 claim 的结论内。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
  - T6
  - SP-21
  - terminal-first
  - policy-priority
  - successor-safety
  - proof-boundary
  - E1-E5
  - re-entry
sources:
  - document: docs/standalone-proof-propositions-2026-08-28/SP-21-ABSTRACT-SAFETY-PROOF-2026-08-29.md
    role: reviewed canonical proof
  - document: docs/standalone-proof-propositions-2026-08-28/SP-21-proof-review-2026-08-29.md
    role: review verdict and scope boundary
  - document: docs/archive/proof-submissions/2026-08-29/SP-21-submitted-proof-2026-08-29.md
    role: preserved submitted derivation
  - reproduction: reproductions/sp04_q1_m23/sp04_verifier.py
    role: independent M23 control replay
  - reproduction: reproductions/sp05_complete_terminal_decision/sp05_independent_replayer.py
    role: independent p=21169 full terminal replay
visibility: public
last_checked: '2026-08-29'
---

# Scope-Bound Successor Safety

Let \(\mathcal P=(A_0,\ldots,A_N)\) be a finite frozen policy. A selected producer
does not become safe merely because a local arithmetic predicate misses. It becomes
safe only after all earlier actions have replayed to their unique continuation
outputs, the selected action has fired, and its separately verified E1--E5/R
bundle supplies a universal lift.

The essential formal correction is:

\[
\operatorname{Reach}_{\mathcal P,j}(S)
\Longleftrightarrow
\operatorname{PriorClear}_{\mathcal P,j}(S)
\land
\operatorname{NoRejectBefore}_{\mathcal P,j}.
\]

With this reachability condition, a terminal HIT at a reachable earlier index
is an actual terminal output; a selected producer with an independently valid
edge and lift is a safe successor. An unregistered or explicitly later terminal
formula may still exist, but it does not invalidate the lift or change the
frozen earlier-action trace.

The clearance type is strictly distinct from a global miss:

\[
\mathsf{MISS\_HIGHER\_PRIORITY\_POLICY\_COMPLETE}
\ne
\mathsf{MISS\_COMPLETE}.
\]

For \(p=21169\), the complete M23 factor-pair screens miss while the later
gap-31 certificate exists. This provides a finite control that the distinction
is necessary, not merely terminological.
