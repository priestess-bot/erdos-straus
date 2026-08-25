---
kind: claim
claim_id: type-I-t6-f3-tr1-dyadic-fresh-child-normalization
title: TR1 dyadic-fresh endpoint has a strict complete-excess child normal form
statement: >-
  In an actual low proper-root stutter receipt, the condition
  2|gcd(D_star,E) forces a sharp 2-adic shape: the source support has
  v2(A)>=v2(p-1)+2 and the stutter parameter satisfies v2(m+2)=v2(p-1).
  Its source-bound dyadic raw child is p-free, retains a nontrivial selected
  complete-excess block, and splits into terminal, strict one-sided, strict
  atomic, or one atomic-companion stutter gate. This is conditional E1/E2/E5
  arithmetic; source transcript, terminal priority, E3/E4 and re-entry remain
  open.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-t6-f3-tr1-fresh-dstar-endpoint-split
  - type-I-t6-f3-qc1-endpoint-excess-deflation
  - type-I-root-capacity-stutter-receipt-factor-split
topics:
  - type-I
  - F3
  - TR1
  - proper-root
  - dyadic
  - complete-excess
  - atomic-split
  - p-free
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_f3_root_landing_and_tr1_dyadic_boundaries.py
    role: local dyadic arithmetic control
  - claim: type-I-t6-f3-tr1-fresh-dstar-endpoint-split
    role: source-bound fresh-factor raw suffix
visibility: public
last_checked: '2026-08-25'
---

# TR1 dyadic-fresh child normalization

Let an actual low proper-root stutter receipt have

\[
2\le h<p,\quad z=ED,\quad
\lambda=v_2(p-1)\ge3,\quad
\alpha=v_2(A),\quad\varepsilon=v_2(E),
\tag{1}

\]

and suppose

\[
2\mid(D_*,E),\qquad D_*=D/(D,h^2-1).
\tag{2}

## 1. Forced 2-adic shape

Maximality gives

\[
v_2(D)=\alpha,\qquad
v_2(K)=\alpha+\lambda,\qquad
v_2(z)=\alpha+\varepsilon>\alpha+\lambda.
\tag{3}

Since \(D\mid ph+1\) and \(h\) is odd, (2) forces

\[
\boxed{
\alpha\ge\lambda+2,\qquad
v_2(h^2-1)=\lambda+1,\qquad
v_2(D_*)=\alpha-\lambda-1>0.}
\tag{4}

Writing \(D=mp+1-h\), the same congruence calculation gives

\[
\boxed{v_2(m+2)=\lambda,\qquad v_2(m)=1,\qquad
m=2^\lambda t-2\quad(t\text{ odd}).}
\tag{5}

This is a necessary shape, not a contradiction. For example
\((p,h,D,m,e)=(283,1101,32,4,9737)\) has \(D_*=4\), but is non-core,
high-height and not an actual receipt.

## 2. The dyadic child remains nontrivial

Assume the required source-forward transcript reaches \((z,h,1)\). The dyadic
raw suffix produces the primitive p-free child

\[
x=z/2,\qquad y=R-z/2.
\tag{6}

Set

\[
\mu=
\begin{cases}
1,&\varepsilon\ge\lambda+2,\\
\lambda+1,&\varepsilon=\lambda+1.
\end{cases}
\tag{7}

The selected-side maximal normalization is exactly

\[
\boxed{E_x=E/2^\mu,\qquad M_x=AE_x,}
\tag{8}

and

\[
D_x=
\begin{cases}
D,&\varepsilon\ge\lambda+2,\\
2^\lambda D,&\varepsilon=\lambda+1.
\end{cases}
\tag{9}

Even at the boundary \(\varepsilon=\lambda+1\), \(E_x>1\). Otherwise
\(E=2^{\lambda+1}\) and the stutter congruence \(E\equiv1\pmod p\) would
force \(p=3\), impossible in the core domain. Thus \(M_x>A\), and

\[
\boxed{c_x=\langle-2^\mu\rangle_p\in[1,p-2].}
\tag{10}

## 3. Exact child split

After the child terminal-first policy misses, let \(Q_y\) be the maximal
block of the opposite side.

| Opposite side | Consequence |
|---|---|
| \(Q_y=1\) | one-sided strict complete-excess kernel with support \(M_x\) |
| \(Q_y>1\), \(F_y\not\equiv2^\mu\pmod p\) | genuine atomic split with strict cofactor \(\langle-2^\mu F_y^{-1}\rangle_p\) |
| \(Q_y>1\), \(F_y\equiv2^\mu\pmod p\) | R6 full-capacity \(W_y\)-word to a p-free terminal-or-single-side endpoint |

Here \(F_y=Q_y/(A,Q_y)\). The R6-specific full-capacity theorem proves
\(W_y\not\equiv(h+1)/2\pmod p\), so stripping the complete \(W_y\) word,
with terminal-first replay at every internal prefix, reaches a p-free endpoint
with \(Q_u=1\). The endpoint is therefore terminal or single-side arithmetic,
not a genuine atomic endpoint. Canonical final lcm/rank, E3/E4 and re-entry
remain open.

The result reduces the dyadic-fresh TR1 arithmetic subleaf to terminal,
one-sided or a remaining canonical lcm/rank branch. It still requires an
actual source receipt, every child terminal receipt, canonical target typing,
universal lift and shared re-entry before it can be counted as a selector
successor.
