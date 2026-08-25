---
kind: claim
claim_id: type-I-t6-f3-qc1-endpoint-excess-deflation
title: QC1 endpoint-excess q deflation has a canonical strict target
statement: >-
  Let an actual low proper-root stutter receipt in the R3/R5 QC1 domain have
  K=A(p-1), z=R-h=E D, canonical maximal receipt, and stutter congruence
  D=1-h modulo p. Let q=q_perp and assume q divides E. The source-forward
  raw deflation z -> z/q is primitive. If a=vq(A), r=vq(p-1),
  k=a+r, and b=vq(z)>k, then its canonical child support is
  Mx=A E/q^mu, with mu=1 for b>=k+2 and mu=r+1 for b=k+1. Its cofactor
  is <-q^mu>_p in [1,p-2], and Mx>A, so the selected-side charged rank
  strictly falls. This is a conditional arithmetic E2/E5 route; it needs a
  verified persistent source path for E1 and still lacks common admission,
  universal lift, and re-entry. If the first two-sided child has the sole
  rank-stutter congruence F_y=q^mu modulo p, a deterministic second raw
  deflation by the least prime factor of F_y not congruent to 1 modulo p
  restores a strict selected-side cofactor. It too remains a conditional raw
  continuation, not a QC1 closure.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-t6-f3-qc1-quotient-only-occurrence-boundary
  - type-I-root-capacity-strict-carry-universal-raw-word-policy-boundary
  - type-I-root-capacity-strict-carry-support-rebase
topics:
  - type-I
  - F3
  - QC1
  - proper-root
  - complete-excess
  - raw-deflation
  - well-foundedness
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_t6_f3_qc1_endpoint_excess_deflation.py
    role: valuation and residue boundary replay
visibility: public
last_checked: '2026-08-25'
---

# QC1 endpoint-excess deflation

Let \(z=R-h=ED\) be the canonical maximal receipt of a low proper-root
stutter state and let \(q=q_\perp\mid E\). Write

\[
a=v_q(A),\qquad r=v_q(p-1),\qquad k=a+r,\qquad b=v_q(z)>k.
\tag{1}
\]

The inequality in (1) is exactly the complete-excess condition, so the
source-forward raw move

\[
(z,h)\longmapsto\left(\frac zq,R-\frac zq\right)
\tag{2}
\]

is primitive. Recomputing the canonical child excess block yields

\[
M_x=\frac{AE}{q^\mu},
\qquad
\mu=
\begin{cases}
1,&b\ge k+2,\\
r+1,&b=k+1.
\end{cases}
\tag{3}
\]

The second case is the capacity boundary: one deflation removes the entire
\(q^{r+1}\) contribution to the support multiplier. It is not the former
formal update \(A\mapsto Aq_\perp\).

Stutter gives \(E\equiv1\pmod p\), while \(4A\equiv-1\pmod p\). Hence

\[
c_x=\left\langle(4M_x)^{-1}\right\rangle_p
=\left\langle-q^\mu\right\rangle_p.
\tag{4}
\]

This is never \(p-1\). For \(\mu=1\), \(q<p/4\). For
\(\mu=r+1\), if \(q^{r+1}\equiv1\pmod p\), writing
\(p=q^rs+1\) and \(q^{r+1}-1=tp\) gives
\(0<t<q\) and \(t\equiv-1\pmod {q^r}\), impossible for \(r\ge2\);
the \(r=1\) case would force \(p=q+1\), not an odd core prime.
Also \(E/q^\mu>1\), since otherwise \(E=q^\mu\not\equiv1\pmod p\).
Thus (2) has an arithmetic strict charged target.

This theorem only supplies a raw occurrence when the parent already carries a
verified source-forward persistent path to \((z,h)\). The universal root word
alone remains analysis evidence. If the opposite side is also excess, its
atomic target is strict unless its multiplier is \(q^\mu\) modulo \(p\);
that equality has the following deterministic second suffix.

## 2. The atomic rank-stutter leaf has a second raw suffix

Suppose the first child is genuinely two-sided, its opposite-side p-free
complete-excess multiplier is \(F_y\), and

\[
F_y\equiv q^\mu\pmod p.
\tag{5}
\]

The first atomic target has cofactor \(p-1\), but (5) is not a raw dead end.
Since \(q^\mu\not\equiv1\pmod p\), also

\[
F_y\not\equiv1\pmod p,
\qquad p\nmid F_y.
\tag{6}
\]

Hence some prime factor of \(F_y\) is not \(1\pmod p\). Fix the least such
prime

\[
s=\min\{\ell:\ell\mid F_y,\ \ell\not\equiv1\pmod p\}.
\tag{7}
\]

For the selected child side, write

\[
a_s=v_s(A),\qquad r_s=v_s(p-1),\qquad b_s=v_s(y)>a_s+r_s,
\tag{8}
\]

and set

\[
\mu_s=
\begin{cases}
1,&b_s\ge a_s+r_s+2,\\
r_s+1,&b_s=a_s+r_s+1.
\end{cases}
\tag{9}
\]

Because \(s\) is carried by the selected complete-excess block, the second
source-forward raw deflation \(y\mapsto y/s\) has recomputed support

\[
M_2=\frac{M_{\rm at}}{s^{\mu_s}},
\qquad
\left\langle(4M_2)^{-1}\right\rangle_p
=\left\langle-s^{\mu_s}\right\rangle_p<p-1.
\tag{10}
\]

The same residue exclusion used for (4) proves the strict inequality in (10).
Thus the former atomic rank-stutter leaf has a deterministic strict
selected-side arithmetic continuation. It still needs a replayable source path,
second-child terminal priority, full recanonicalization, E3/E4 and re-entry;
an opposite-side excess may also remain. For example, the formal control
\(p=337,A=421,q=7,E=7^2\cdot619,F_y=4093\) has
\(F_y\equiv49=q^\mu\pmod{337}\), but \(s=4093\) gives second cofactor
\(288\). This control is arithmetic only, not an actual F3 witness.
