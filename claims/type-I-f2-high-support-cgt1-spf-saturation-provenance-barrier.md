---
kind: claim
claim_id: type-I-f2-high-support-cgt1-spf-saturation-provenance-barrier
title: High-support C>1 SPF saturation is not a physical same-chart edge
statement: >-
  Let a terminal-first-surviving high-support Type I CHARGED chart have
  K=A*C, A>Bp, and 1<C<p. For any prime q|C, the formal support update
  A -> A*q lowers capacity C -> C/q arithmetically, but it cannot be a
  current fixed-n or full-block same-chart E1 route. With d=p-C,
  q does not divide d and hence A*q does not divide A*d. A q complete-excess
  block has valuation strictly above vq(K), so lcm(A,Q) does not divide K and
  necessarily re-charts. Thus q|C alone supplies no physical same-chart
  saturation successor. This does not exclude external raw rechart,
  lower-protocol, terminal, or source-unreachability routes.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-fixed-n-bounded-divisor-saturation
  - type-I-path-anchored-atomic-split-complete-excess-admission
topics:
  - type-I
  - F2
  - high-support
  - cofactor-greater-than-one
  - provenance
  - fixed-n
  - complete-excess
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_f2_high_support_anchor_and_saturation_boundaries.py
    role: divisor and valuation boundary replay
visibility: public
last_checked: '2026-08-25'
---

# C>1 saturation provenance barrier

Let \(K=AC\), \(1<C<p\), and \(q\mid C\) be prime. The fixed-\(n\)
determinant carrier is \(S=A(p-C)\). Since

\[
p-C\equiv p\not\equiv0\pmod q,
\tag{1}
\]

we have

\[
\boxed{Aq\nmid A(p-C).}
\tag{2}
\]

Therefore the proposed \(L=Aq\) is not a fixed-\(n\) divisor.

Nor can a canonical full-excess block preserve the old chart. If
\(a=v_q(A)\) and \(c=v_q(C)\ge1\), a \(q\)-complete-excess block must
satisfy

\[
v_q(Q)>v_q(K)=a+c.
\tag{3}
\]

Hence

\[
v_q(\operatorname{lcm}(A,Q))>v_q(K),
\tag{4}
\]

so the new support cannot divide \(K\) and must re-chart. Equations
(2)--(4) remove only the tempting same-chart SPF saturation route from the
empty-improvement residual.
