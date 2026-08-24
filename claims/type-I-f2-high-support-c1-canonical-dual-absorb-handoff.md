---
kind: claim
claim_id: type-I-f2-high-support-c1-canonical-dual-absorb-handoff
title: High-support C=1 canonical dual has a concrete R=3 ABSORB handoff
statement: >-
  Let an actual terminal-first-surviving TYPEI/CHARGED parent be a canonical
  high-support C=1 chart (p,R,A;A), where p is a core prime,
  A>B_p=(p-1)^2/4, and pR+1=4A. Its deterministic derived determinant
  M=A, d=p-1, n=(p-1)R+1 has symmetric low duals
  (p-2,B_p) and (3,N), where N=(3p+1)/4. The R=3 side is the
  smallest positive canonical dual and has support N=K. Therefore a producer
  that consumes the actual parent, runs target terminal-first, and is admitted
  into a semantic TYPEI/ABSORB owner has a deterministic CHARGED-to-ABSORB
  phase-drop with the identity map on Sol(4,p). This establishes E2, E4, and
  the conditional E5 ticket; it does not establish the new producer's
  registration, generic ABSORB E3 owner, target terminal-first serializer, or
  recursive ABSORB re-entry. Hence it is a conditional handoff, not a verified
  successor or C=1/F2/T6 closure.
claim_status: conditional
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - type-I-overflow-d-one-p-minus-two-g-rechart
  - type-I-type-II-mod-three-double-g-exit-obstruction
  - type-I-t5-full-contract-level-global-well-foundedness
  - t6-persistent-selector-state-v1
topics:
  - type-I
  - F2
  - overflow
  - high-support
  - cofactor-one
  - determinant-dual
  - absorb
  - phase-drop
  - proof-boundary
sources:
  - claim: type-I-overflow-determinant-fixed-n-dual-support-conflict
    role: symmetric determinant-dual identities and support-loss boundary
  - claim: type-I-type-II-mod-three-double-g-exit-obstruction
    role: R=3 is not universally terminal
  - concept: t5-global-well-foundedness-contract-v2
    role: CHARGED-to-ABSORB protocol drop
  - reproduction: reproductions/type_i_f2_high_support_c1_canonical_dual_absorb_handoff.py
    role: symbolic dual replay and R=3 control
visibility: public
last_checked: '2026-08-24'
---

# High-support C=1 canonical dual ABSORB handoff

## Scope

Let

\[
p\equiv1\pmod {24},
\qquad
B_p=\frac{(p-1)^2}{4},
\]

and suppose an actual persistent parent has already passed its declared
terminal-first priority:

\[
H=(p,R,K;A,\sigma),
\qquad
K=A>B_p,
\qquad
pR+1=4A,
\qquad
p<R<4A.
\tag{1}
\]

This is exactly the high-support \(C=K/A=1\) branch. The construction below
uses the actual parent as its source. It is not a claim that an arbitrary
bare chart can be enqueued.

## Canonical determinant and the two low duals

There is a unique \(\alpha\in\{1,\ldots,p-1\}\) with
\(4\alpha\equiv1\pmod p\):

\[
\alpha=\frac{3p+1}{4}.
\tag{2}
\]

Writing

\[
A=kp+\alpha,
\qquad
R=4k+3,
\tag{3}
\]

define the deterministic state-derived determinant

\[
M=A,
\qquad
d=p-1,
\qquad
n=(p-1)R+1.
\tag{4}
\]

It obeys

\[
pn=4Md+1,
\qquad
R=4M-n.
\tag{5}
\]

The symmetric-dual remainder is

\[
s=n-4kd=3p-2.
\tag{6}
\]

Consequently the \(d\)-side and \(\alpha\)-side canonical charts are,
respectively,

\[
\begin{aligned}
(R_d,K_d)
&=(4d-s,\ d(p-\alpha))
=\left(p-2,\frac{(p-1)^2}{4}\right),\\
(R_\alpha,K_\alpha)
&=(4\alpha-s,\ \alpha(p-d))
=\left(3,\frac{3p+1}{4}\right).
\end{aligned}
\tag{7}
\]

Both identities are independent of the high support level \(k\). The
\(\alpha\)-side has the least positive possible canonical chart coordinate,
so it is the deterministic selected dual:

\[
\boxed{
H\longmapsto
T_3=\left(p,3,\frac{3p+1}{4};
\frac{3p+1}{4}\right).
}
\tag{8}
\]

It deliberately drops the old charged support \(A\); it cannot be claimed as
a same-protocol CHARGED transition.

## Conditional admission contract

The target must first run its own versioned terminal-first predicates. If one
hits, the output is a terminal for the same root equation. If they all miss,
the only proposed recursive interpretation is

\[
\mathrm{TYPEI/CHARGED}
\longrightarrow
\mathrm{TYPEI/ABSORB}.
\tag{9}
\]

For this specific target:

| Obligation | Status | Reason |
|---|---|---|
| E1 | relative | An actual parent and its source receipt are required; a new registered producer must bind them to (4). |
| E2 | established | Equations (2)--(8) reconstruct one target without a factor choice. |
| E3 | open | The active grammar has no generic ordinary TYPEI/ABSORB owner for this target. |
| E4 | established relative to E3 | Both charts have root \(p\); use the identity on \(\operatorname{Sol}(4,p)\). |
| E5 | established relative to E3 | The frozen T5 protocol order makes CHARGED to ABSORB a phase-drop. |
| re-entry | open | An admitted ABSORB target needs a total, non-upward continuation. |

Thus (8) is a precise target-shape and phase-ticket proposal, not an active
edge.

## Why this is not a terminal theorem

The \(R=3\) target is not automatically a Type I terminal or an F state. For
example, at \(p=241\),

\[
\frac{3p+1}{4}=181\equiv1\pmod3,
\]

and the \(R=3\) chart is G. The stronger double-G controls in the cited
obstruction also exclude treating a fixed finite low-gap menu as its universal
continuation. Therefore the target must be terminal-first classified and, on
a miss, receive an independently admitted ABSORB owner and continuation.

## Boundary

This handoff does **not** prove that:

- every high-support C=1 parent has a current active constructor;
- the current F1 grammar accepts the target;
- the target is terminal;
- an ABSORB continuation is total;
- high-support C=1, F2, T6, or the conjecture is closed.

It replaces the vague phrase “find a lower-protocol exit” by one deterministic
candidate whose remaining obligations are exactly E3, target terminal-first,
and re-entry.
