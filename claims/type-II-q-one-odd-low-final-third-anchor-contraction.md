---
kind: claim
claim_id: type-II-q-one-odd-low-final-third-anchor-contraction
title: q=1 odd low-final p=25 mod336 的第三-anchor C=9 contraction
statement: >-
  Let an ordinary q=1 full-carrier odd-t contraction reach its low final
  checkpoint. After the gap-7 preemption, the remaining class is
  p=336k+25. Its low chart is
  (R,K;A)=(80k+7,4(140k+11)(12k+1);2(140k+11)). The complete-excess block
  at its anchor is exactly Q=40k+3, and the carrier
  M=2(140k+11)(40k+3) has canonical chart
  (R_M,K_M)=(1200k+95,9M), with R_M>p and M<=B_p. Hence the low checkpoint
  can remain nonpersistent and the original full-carrier root has a direct
  root-to-high-final CHARGED projection with LOCAL_DROP. This closes the
  q=1 odd low-final interface up to a structured C=9 high overflow; it does
  not provide the overflow's subsequent selector route or global closure.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-odd-low-final-gap-seven-preemption
  - type-II-q-one-full-carrier-root-second-anchor-contraction
  - type-I-universal-p-source-capacity-anchor-orbit
  - t6-persistent-selector-state-v1
  - type-I-t5-full-contract-level-global-well-foundedness
topics:
  - type-II
  - q-one
  - full-carrier
  - third-anchor
  - complete-excess
  - overflow
  - cofactor-nine
  - T5
  - proof-boundary
sources:
  - reproduction: reproductions/type_ii_q_one_odd_low_final_third_anchor_contraction.py
    role: symbolic C=9 chart and root-to-final potential controls
visibility: public
last_checked: '2026-08-25'
---

# q=1 odd low-final third-anchor C=9 contraction

## 1. Remaining low class

The preceding congruence classification shows that an odd q=1 contraction
can be low only for

\[
p\equiv25\ \text{or}\ 265\pmod {336}.
\tag{1}
\]

The latter class is preempted by its direct gap-7 Type II terminal. It
therefore remains only to analyze

\[
p=336k+25,\qquad t=14k+1.
\tag{2}
\]

Substitution into the odd quotient-fold formulas gives the low checkpoint

\[
\boxed{
R_1=80k+7,\qquad
K_1=4(140k+11)(12k+1),\qquad
A_1=2(140k+11).}
\tag{3}
\]

This is not made persistent: it is the third checkpoint of the root-to-final
macro described below.

## 2. Exact complete-excess computation

At the universal anchor of (3),

\[
R_1-1=2(40k+3).
\tag{4}
\]

Put \(Q=40k+3\). The two gcd identities

\[
\begin{aligned}
(Q,140k+11)&=1,\\
(Q,12k+1)&=1
\end{aligned}
\tag{5}
\]

follow respectively from

\[
(140k+11)-3Q=20k+2,\qquad Q-2(20k+2)=-1,
\tag{6}
\]

and

\[
Q-3(12k+1)=4k,\qquad (12k+1)-3(4k)=1.
\tag{7}
\]

Both factors in (3) after the leading \(4\) are odd, so
\(v_2(K_1)=2>v_2(R_1-1)=1\). Equations (4)--(7) prove that the unique
complete-excess block is exactly

\[
\boxed{Q=40k+3,\qquad\beta=2.}
\tag{8}
\]

Since \((A_1,Q)=1\), its canonical carrier is

\[
\boxed{M=A_1Q=2(140k+11)(40k+3).}
\tag{9}
\]

## 3. The forced high C=9 chart

Direct multiplication gives

\[
36M-1=(336k+25)(1200k+95).
\tag{10}
\]

Hence the canonical chart at carrier \(M\) is

\[
\boxed{
R_M=1200k+95,\qquad K_M=9M.}
\tag{11}
\]

The cofactor \(9\) lies in \(\{1,\ldots,p-1\}\), so (11) is the
canonical chart rather than an arbitrary high representative. It satisfies

\[
R_M-p=864k+70>0.
\tag{12}
\]

Moreover

\[
B_p-M
=17024k^2+2312k+78>0,
\tag{13}
\]

where \(B_p=(p-1)^2/4\). Thus \(M\le B_p\) and \(M>1\).

## 4. Root-to-final ticket

Treat the low chart (3), its anchor and the rechart (11) as checkpoint data
inside the same macro that began at the full-carrier root \(S_X\). The only
persistent endpoints are then

\[
S_X=(p,R_X,K_X;1),\qquad
T_9=(p,R_M,K_M;M).
\tag{14}
\]

The final target is an existing `TYPEI/CHARGED` overflow shape. By (13),

\[
\left\lfloor\frac{B_p}{M}\right\rfloor
<
\left\lfloor\frac{B_p}{1}\right\rfloor=B_p.
\tag{15}
\]

Therefore the root-to-\(T_9\) transition has the direct frozen N7 ticket

\[
\boxed{\mathrm{LOCAL\_DROP}.}
\tag{16}
\]

Its E1 remains relative to the actual root path and ordered terminal misses
at all checkpoints; E2 is (3)--(11); E3 is the final overflow projection;
and E4 is the identity on \(\operatorname{Sol}(p)\). No persistent
`ABSORB -> CHARGED` return occurs.

## 5. Boundary

This eliminates the q=1 odd low-final **interface**, not the resulting
overflow problem. The structured final family has cofactor \(9\), high
chart coordinate, and support \(M\), but it still needs a terminal or an
admitted successor/re-entry theorem. The macro also needs its final shared
T2/Gate-3 disposition before it can become a global registry route. Nothing
here closes F2, T6, or the conjecture.
