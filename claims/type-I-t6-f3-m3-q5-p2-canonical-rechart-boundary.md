---
kind: claim
claim_id: type-I-t6-f3-m3-q5-p2-canonical-rechart-boundary
title: m=3 q=5 genuine two-sided p2 checkpoint is an unpaid root rechart
statement: >-
  On the actual source-bound minimal m=3,5|D_star genuine two-sided p2
  endpoint, let L_omega=E_u E_v=1+p^2 chi. The canonical target has
  cofactor p-1 and is exactly the same a=1,d=1 root-chart family with
  root parameter varrho'=varrho+chi*T, where
  T=p^2 varrho-(p+1)/2. Thus T'=L_omega*T, A'=A L_omega, and K'=K
  L_omega. This is arithmetic chart reparameterization with increasing
  root parameter, not an E1/E3 state re-entry or a strict T5 successor.
  It removes the direct canonical p2 rechart as a possible paid macro but
  does not close the genuine two-sided p2 residual.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-t6-f3-policy-endpoint-p2-divisor-source-normal-form
  - type-I-overflow-full-product-d-one-a-one-s-zero-endpoint-boundary
topics:
  - type-I
  - F3
  - m-three
  - q-five
  - p-squared
  - two-sided
  - rechart
  - T5
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_t6_f3_policy_endpoint_p2_gate.py
    role: exact p2 rechart parameter identity
visibility: public
last_checked: '2026-08-25'
---

# Genuine two-sided p2 rechart boundary

Fix a source-bound two-sided endpoint with

\[
L_\omega=E_uE_v=1+p^2\chi,\qquad \chi>0.
\tag{1}
\]

The policy-endpoint normal form gives canonical target cofactor
\[
c_T=p-1,
\qquad K_T=K L_\omega.
\tag{2}
\]

Write the original a=1,d=1 root chart as

\[
g=\frac{p+1}{2},
\qquad T=p^2\varrho-g,
\qquad A=gT,
\qquad K=A(p-1).
\tag{3}
\]

Set

\[
\varrho'=\varrho+\chi T.
\tag{4}
\]

Then

\[
p^2\varrho'-g
=T+p^2\chi T
=L_\omega T,
\tag{5}
\]

so the canonical target is precisely the root chart with parameter
\(\varrho'>\varrho\), support \(A'=A L_\omega\), and capacity
\(K'=K L_\omega\). Its charged cofactor remains \(p-1\), hence the
parent-to-checkpoint local rank is unchanged. No source path, terminal
receipt, state identity, owner, admission, or strict ticket transfers across
(4). A valid p2 closure must therefore use a new continuous suffix ending in
a terminal or a genuinely strict final target.
