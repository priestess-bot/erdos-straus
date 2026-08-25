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
  universal lift, and re-entry. It does not close QC1.
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
that equality is retained as a separate rank-stutter residual.
