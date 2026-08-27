# F2 C8 Outgoing Coverage Correction (2026-08-27)

## Finding

The previous C8 matrix described `C8-O2-DOUBLE_LOW` and `C8-O3-OTHER` as an
exclusive nonterminal partition. That description obscured the quantifier of
the existing parent-anchored second-full-excess theorem.

For every actual C8 parent with a complete terminal-first `MISS`, the theorem

`type-I-c8-second-full-excess-parent-anchored-universal-fallback`

constructs the same deterministic parent macro

\[
H=(p,R,8M;M),\qquad Q=(R-1)/2,\qquad A_T=MQ,
\]

with

\[
75c_T\equiv64\pmod p,
\qquad 9\le c_T\le p-2,
\qquad \Pi_{T5}(T)<\Pi_{T5}(P).
\]

Its construction contains no double-low hypothesis. Section 5 of that claim
explicitly states that the fallback is usable even when the double-low
predicate holds.

The correct mathematical coverage is therefore

\[
\operatorname{terminalFirst}(P)=\mathrm{HIT}
  \Longrightarrow \operatorname{TERMINAL}(P),
\]

\[
\operatorname{terminalFirst}(P)=\mathrm{MISS}
  \Longrightarrow \operatorname{C8SecondFullExcessParentMacro}(P).
\]

`DOUBLE_LOW` remains a possible alternate atomic route inside the second line.
It can be given priority only after a shared runtime proves a complete,
source-bound candidate universe and common admission. It must not block,
disable, or be used to infer the universal fallback.

## What This Does Not Establish

The correction is arithmetic coverage only. It does not turn a C8 input into a
current `VERIFIED_SUCCESSOR`. The following obligations remain independent and
open:

- actual admitted parent and replayable parent-to-checkpoint path (E1);
- a complete terminal-first receipt rather than a local `MISS` boolean;
- full target factorization and terminal/hit/F/G classification;
- shared producer, state-owner validation, sealed E3 admission, and queue
  authority;
- re-entry and downstream totality of `type_i_a_gt_one_overflow_residual`.

The fallback is a parent macro, not a `T2v1` atomic arm. Its final target has
the existing high-support overflow owner shape; it must not be serialized as
`AtomicPendingTargetV1` or attributed to `C8_DOUBLE_LOW`.

## Consequence for the Frontier

This removes only a false *mathematical* prerequisite from the C8 outgoing
description. It does not reduce the live F2 residual count, does not close an
active producer, and does not change F1, F2, F3, T6, or the conjecture.

The nearest useful mathematical continuation is to analyze the structured
high-support target family \(A_T=MQ\), subject to the still-external receipt
and admission obligations, rather than to seek universal existence of a
double-low factor. The new
`type-I-c8-second-full-excess-parent-anchored-target-pfree-overlap-compression`
claim gives its first useful post-fallback invariant: the next complete-excess
block is p-free and nontrivial, but the explicit arithmetic control in that
claim shows that the overlap bound alone does not pay a strict next capacity
drop.
