---
kind: claim
claim_id: type-I-root-capacity-stutter-k-three-vieta-companion-obstruction
title: actual proper-root k=3 的同-M Vieta companion 第二整数门障碍
statement: >-
  对核心素数 p≡1 mod24 的 terminal-first 后 actual proper-root k=3 stutter
  receipt，取 primitive variables A=a/3、B=(e-1)/3、M=m/3，并令
  j=m-(B-A)。保持 A,M 不变而将 B 替换为其第一 primitive equation 的另一个
  Vieta 根 j 时，候选第二方程的商
  p_j=((3j+1)(A^2-Aj+j^2)-j)/A 不是整数。故这一直接同-M Vieta companion
  不能形成 primitive stutter curve point，更不能充当 QC1 physical edge 或
  T6 successor。该障碍不排除其它变换、terminal 或 independent physicalization。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-k-three-primitive-fiber-reduction
topics:
  - type-I
  - root-capacity
  - stutter
  - eisenstein-quotient
  - k-three
  - vieta
  - route-obstruction
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-k-three-primitive-fiber-reduction
    role: primitive-system-fixed-j-bounds-and-divisor-gate
  - reproduction: reproductions/type_i_root_capacity_stutter_k_three_primitive_fiber_reduction.py
    role: Vieta-companion-identities-and-boundary-controls
visibility: public
last_checked: '2026-08-18'
---

# actual proper-root \(k=3\) 的同-\(M\) Vieta companion 第二整数门障碍

## 1. Scope

Fix an actual, terminal-first-surviving proper-root \(k=3\) stutter receipt
in the core domain. Use the primitive variables of the
[\(k=3\) fiber reduction](type-I-root-capacity-stutter-k-three-primitive-fiber-reduction.md):

\[
1\le A<B,
\qquad
H=A^2-AB+B^2,
\qquad
e=3B+1,
\qquad
A+H=eM,
\tag{1}
\]

and set

\[
\rho=B-A,
\qquad j=m-\rho.
\tag{2}
\]

That card already proves, for an actual core candidate,

\[
1\le j\le A-1,
\qquad A\mid L_j:=9j^2+7j+1.
\tag{3}
\]

This card tests one very specific apparent descent: retain \(A,M\), replace
\(B\) by the other root of (1), and try to recover a second primitive
equation. It does not make a statement about all possible Vieta transforms or
about an actual source/path.

## 2. The companion root

Equation (1), viewed as a quadratic in \(B\), is

\[
X^2-(A+3M)X+A^2+A-M=0.
\tag{4}
\]

Its other root is

\[
A+3M-B=A+m-B=m-(B-A)=j.
\tag{5}
\]

Thus with

\[
H_j=A^2-Aj+j^2,
\qquad e_j=3j+1,
\tag{6}
\]

the first primitive equation is indeed preserved:

\[
A+H_j=e_jM.
\tag{7}
\]

The prospective second equation would require an integer

\[
p_j=\frac{e_jH_j-j}{A}.
\tag{8}
\]

The point is that this integrality gate is already impossible in the actual
core range; no source, target, lift, or T5 comparison is reached.

## 3. Second-gate obstruction

First, \((A,j)=1\). Indeed, if a prime divided both \(A\) and \(j\), then
\(A\mid L_j\) from (3) would make it divide \(L_j\), while
\(L_j\equiv1\) modulo that prime, a contradiction.

The numerator in (8) has the exact decomposition

\[
e_jH_j-j
=j(3j^2+j-1)+A(3j+1)(A-j).
\tag{9}
\]

Consequently, if \(p_j\) were integral, then

\[
A\mid Q_j:=3j^2+j-1.
\tag{10}
\]

The core prime is odd, and (1) forces \(A\) odd: if \(A\) were even, then
\((A,B)=1\) would make \(B\) odd, hence \(e\) even and \(H\) odd. The two
sides of \(pA+B=eH\) would then have opposite parity.

Now (3) and (10) imply

\[
A\mid L_j-3Q_j=4(j+1).
\tag{11}
\]

Since \(A\) is odd, \(A\mid j+1\). The range in (3) forces

\[
j=A-1.
\tag{12}
\]

But then

\[
L_{A-1}=9A^2-11A+3\equiv3\pmod A,
\]

so \(A\mid3\). The core range in (3) excludes \(A=1\), leaving only
\(A=3,j=2\). For that pair,

\[
Q_2=13\not\equiv0\pmod3,
\]

contradicting (10). Therefore

\[
\boxed{p_j\notin\mathbb Z.}
\tag{13}
\]

## 4. Consequence and boundary

The same-\(M\) Vieta companion keeps one primitive equation but cannot pass
the second integer gate in the actual core \(k=3\) scope. It therefore cannot
be promoted to a rechart, a terminal, or a recursive edge. In particular,
it cannot supply the missing actual source replay, all-solution lift, or T5
ticket required by QC1.

This is a route obstruction, not a \(k=3\) emptiness theorem. It leaves open
an independent terminal, a transform changing \(A\) or \(M\), a transverse
carrier exit, or a different physicalization of a quotient factor. Thus
`PROPER_ROOT_QC1_OR_TR1` and `T6_GLOBAL_SELECTOR_TOTALITY` remain `OPEN`.

## Focused reproduction

```bash
python3 reproductions/type_i_root_capacity_stutter_k_three_primitive_fiber_reduction.py --verify
python3 -m unittest tests/test_type_i_root_capacity_stutter_k_three_primitive_fiber_reduction.py
```

The controls replay (4)--(9) at the deliberately non-core \(j=0\) boundary
and check the forced residual pair \((A,j)=(3,2)\), whose second gate fails.
They do not search for actual receipts or claim a selector edge.
