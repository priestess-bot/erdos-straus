---
kind: claim
claim_id: type-I-t6-f3-m3-q5-p2-two-sided-residual-boundary
title: Genuine two-sided m=3 q=5 p2 endpoint remains an unpaid residual
statement: >-
  For a source-bound actual low proper-root m=3, 5|D_star receipt whose
  recanonicalized p-free endpoint is genuinely two-sided, write
  u=E_u D_u and v=E_v D_v with respect to the original K=A(p-1). If
  E_u,E_v>1 and E_u E_v=1+p^2 chi, then the canonical target has cofactor
  p-1 and is an increasing a=1,d=1 root-chart reparameterization. The
  existing source-bound macro therefore supplies no strict T5 ticket or
  recursive admission for this endpoint. Closure still requires an empty
  theorem, a terminal-first certificate, or a new source-forward final
  atomic macro with E1--E5; the arithmetic p2 normal form alone is not any
  of these.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-t6-f3-m3-q5-source-bound-macro-interface
  - type-I-t6-f3-policy-endpoint-p2-divisor-source-normal-form
topics:
  - type-I
  - F3
  - m-three
  - q-five
  - p-squared
  - two-sided
  - source-bound
  - T5
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_t6_f3_m3_q5_p2_two_sided_boundary.py
    role: independent arithmetic negative control and object-separation control
visibility: public
last_checked: '2026-08-25'
---

# Genuine two-sided \(p^2\) residual boundary

## 1. Exact input

Take an already admitted `ACTUAL_PERSISTENT` source and a replayable path receipt
through the \(m=3,\ 5\mid D_*\) branch. Require the terminal-first scheduler and all
priority prefixes to have returned `MISS`. At the resulting primitive \(p\)-free
endpoint let

\[
u+v=R,\qquad (u,v)=1,\qquad p\nmid uv,
\]

and recompute, relative to the **original** \(K=A(p-1)\),

\[
u=E_uD_u,\qquad v=E_vD_v.
\]

The complete-excess normal form gives

\[
D_u,D_v\mid K,\qquad (D_u,D_v)=1,
\]

and the cross-divisor conditions

\[
D_u\mid pE_vD_v+1,\qquad
D_v\mid pE_uD_u+1.
\tag{1}
\]

The genuine two-sided \(p^2\) leaf is the exact predicate

\[
E_u>1,\qquad E_v>1,\qquad
L_\omega:=E_uE_v=1+p^2\chi,\qquad \chi\ge1.
\tag{2}
\]

This is a predicate on the final recanonicalized endpoint. It is not the first-child
multiplier \(L_1\), and no \(L_1\)-congruence may be substituted for (2).

## 2. What the existing macro proves

The endpoint support and canonical cofactor are forced:

\[
M=\operatorname{lcm}(A,Q_u,Q_v)=A L_\omega,
\qquad
c_T=\left\langle-L_\omega^{-1}\right\rangle_p=p-1.
\tag{3}
\]

Consequently

\[
K_T=K L_\omega,
\qquad
R_T=\frac{4K_T-1}{p}.
\tag{4}
\]

For the \(a=1,d=1\) root chart write

\[
g=\frac{p+1}{2},\qquad
T=p^2\varrho-g,\qquad A=gT.
\tag{5}
\]

With

\[
\varrho'=\varrho+\chi T,
\]

we have

\[
T'=p^2\varrho'-g=(1+p^2\chi)T=L_\omega T,
\qquad A'=A L_\omega,
\qquad K'=K L_\omega.
\tag{6}
\]

Thus the direct canonical image is an increasing reparameterization of the same root
chart. It keeps the canonical cofactor at \(p-1\); it does not produce a strict local
rank drop. The p2 checkpoint is therefore an internal macro object, not a persistent
successor.

## 3. E1--E5 audit

| obligation | exact status on the two-sided p2 leaf |
|---|---|
| E1 | The upstream path receipt is available only for the source-to-endpoint macro. No new source-forward occurrence is supplied by the canonical rechart. |
| E2 | The arithmetic image (3)--(4) is deterministic once the endpoint is validated. |
| E3 | No active admission receipt binds the rechart as a new recursive state; an owner label cannot be inferred from the checkpoint name. |
| E4 | The usual \\(\operatorname{Sol}(p)\\) identity lift is conditional on a validated target and does not create admission. |
| E5 | The direct image has \(c_T=p-1\), so the fixed T5 potential has no strict ticket from this image. |
| re-entry | Not established. A later source-forward suffix must be constructed and normalized before re-entry can be checked. |

The existing macro consequently closes strict \(L_\omega\not\equiv1\pmod p\) leaves
only. It does not close (2).

## 4. Smallest remaining theorem

For every input satisfying (1)--(2), prove exactly one of the following:

1. `FAMILY_EMPTY`, by an argument using the full actual divisor/source hypotheses;
2. `TERMINAL`, with terminal-first priority and a replayable certificate; or
3. a source-forward final atomic macro whose final target has deterministic E1, E2,
   E3 owner/admission, universal E4, strict parent-to-final E5, and active re-entry.

Higher congruences such as \(L_\omega\equiv1\pmod {p^3}\), a finite scan, or the
increasing canonical rechart do not satisfy this disjunction.

## 5. Scope boundary

The arithmetic control in the accompanying reproduction is deliberately not claimed to
be an actual \(m=3,\ 5\mid D_*\) witness. It demonstrates only that the two-sided \(p^2\)
normal form is internally consistent and that direct canonical recharting cannot pay E5.
Therefore this claim narrows the residual; it does not prove that the residual is nonempty,
and it does not close F3 or T6.
