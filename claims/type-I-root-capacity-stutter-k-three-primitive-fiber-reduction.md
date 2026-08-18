---
kind: claim
claim_id: type-I-root-capacity-stutter-k-three-primitive-fiber-reduction
title: actual proper-root stutter 的 k=3 primitive Pell fiber 约化
statement: >-
  对核心素数 p≡1 mod24 的 terminal-first 后 actual proper-root stutter receipt，令
  b=e-1、N=a^2-ab+b^2=hk。若 Eisenstein quotient k=3，则 gcd(a,b)=3。
  写 A=a/3、B=b/3、H=h/3、M=m/3，则 A,B 互素、1≤A<B，且
  H=A^2-AB+B^2、e=3B+1、A+H=eM、pA+B=eH。因而
  A divides 3B^2+B-1，e divides (3A+2)^2-3。定义
  d=((3A+2)^2-3)/e，则 d≡1 mod3、gcd(A,d)=1、
  4≤d≤3A-2，并且 A divides 3d^2+d-1。故每个固定 d 只留下有限个
  A-divisor fiber，再由 B、M、p 的闭式唯一重建。特别地 d=1 fiber 只给出
  (A,B,p)=(1,7,939)，不满足核心同余；这精确重现既有 actual-small-root
  theorem 的 (m,a)=(6,3) 排除行，而不是一项额外 T6 closure。该约化不
  physicalize 任意 q|k，不构造 E1--E5 edge，也不关闭 k>1 或 T6 totality。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-finite-curve-constraint
  - type-I-root-capacity-stutter-positive-definite-norm-bound
  - type-I-root-capacity-stutter-common-divisor-alignment
  - type-I-root-capacity-stutter-actual-small-root-exclusion
topics:
  - type-I
  - root-capacity
  - stutter
  - eisenstein-quotient
  - k-three
  - pell-fiber
  - divisor-filter
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-finite-curve-constraint
    role: actual-stutter-linear-identities
  - claim: type-I-root-capacity-stutter-positive-definite-norm-bound
    role: proper-root-range-a-less-than-e
  - claim: type-I-root-capacity-stutter-common-divisor-alignment
    role: gcd-a-b-divides-gcd-h-k
  - claim: type-I-root-capacity-stutter-actual-small-root-exclusion
    role: actual-mod-three-classification
  - reproduction: reproductions/type_i_root_capacity_stutter_k_three_primitive_fiber_reduction.py
    role: exact-reduction-and-d-one-boundary-controls
visibility: public
last_checked: '2026-08-18'
---

# actual proper-root stutter 的 \(k=3\) primitive Pell fiber 约化

## 1. Scope and notation

Fix an actual, terminal-first-surviving proper-root stutter receipt in the
standard core domain

\[
p\equiv1\pmod {24},\qquad h=3u,\qquad 3\nmid u,
\qquad 2\le h<p,
\]

with

\[
b=e-1,\qquad N=a^2-ab+b^2=hk,
\]

and the established stutter identities

\[
a=em-h,\qquad pa+b=eh,\qquad 1\le a<e.
\tag{1}
\]

This card treats only the subcase

\[
\boxed{k=3.}
\tag{2}
\]

It is a reduction of one quotient fiber. It does not turn a quotient factor
into an actual source occurrence and is not a recursive selector claim.

## 2. Primitive reduction at 3

Since \(N=3h\) and \(v_3(h)=1\), one has \(v_3(N)=2\). The actual
modulo-\(3\) classification rules out \(m\equiv2\pmod3\). If
\(m\equiv1\pmod3\), then \(a\equiv2\) and, from \(pa+b=eh\),
\(b\equiv1\pmod3\). Writing \(a=-b+3t\) gives

\[
N=3\bigl(b^2-3bt+3t^2\bigr),
\]

whose parenthesis is a unit modulo \(3\). That would give \(3\nmid k\),
contrary to (2). Hence

\[
m\equiv0\pmod3,\qquad 3\mid a,\qquad 3\mid b.
\tag{3}
\]

The common-divisor alignment theorem gives

\[
(a,b)\mid(h,k)=(3u,3)=3.
\]

Together with (3), this proves

\[
\boxed{(a,b)=3.}
\tag{4}
\]

Define positive integers

\[
A=\frac a3,\qquad B=\frac b3,\qquad H=\frac h3,
\qquad M=\frac m3.
\tag{5}
\]

Then \((A,B)=1\), and division of (1) and \(N=3h\) gives the exact
primitive system

\[
\boxed{
H=A^2-AB+B^2,
\qquad e=3B+1,
\qquad A+H=eM,
\qquad pA+B=eH.}
\tag{6}
\]

The proper-root bound \(a<e\) yields \(A\le B\). Equality would force
\((A,B)=(1,1)\), but then \(A+H=2\) is not divisible by \(e=4\). Thus

\[
\boxed{1\le A<B.}
\tag{7}
\]

## 3. Two Pell-type divisibility gates

The second equality in (6) recovers \(p\) as an integer. Since
\(H\equiv B^2\pmod A\) and \((A,B)=1\), it gives

\[
\boxed{A\mid 3B^2+B-1.}
\tag{8}
\]

For the first equality in (6), the exact identity

\[
9(A+H)=(3A+2)^2-3-(3B+1)(3A-3B+1)
\tag{9}
\]

and \((3B+1,9)=1\) give

\[
\boxed{3B+1\mid(3A+2)^2-3.}
\tag{10}

Thus the two integrality gates have the Pell-type forms

\[
(6B+1)^2-12A\left(\frac{3B^2+B-1}{A}\right)=13,
\tag{11}
\]

and

\[
(3A+2)^2-(3B+1)d=3,
\tag{12}

where

\[
\boxed{d:=\frac{(3A+2)^2-3}{3B+1}\in\mathbb Z_{>0}.}
\tag{13}

The name "Pell-type" only describes these exact norm-style equations; no
Pell equation is asserted to have been globally solved.

## 4. Fixed-\(d\) finite fibers

Because both factors in (13) are \(1\pmod3\),

\[
d\equiv1\pmod3.
\tag{14}

Also \((3B+1)d=(3A+2)^2-3\equiv1\pmod A\), so

\[
\boxed{(A,d)=1.}
\tag{15}

Use \((3B+1)d=9A^2+12A+1\) to eliminate \(B\) from (8). The following
integer identity results:

\[
\begin{aligned}
&3d^2(3B^2+B-1)+(3d^2+d-1)\\
&\qquad=3A(3A+4)(9A^2+12A-d+2).
\end{aligned}
\tag{16}

Since (8) makes the first term on the left divisible by \(A\), (16) gives

\[
\boxed{A\mid C_d:=3d^2+d-1.}
\tag{17}

For fixed \(d\), this is a genuine finite divisor fiber: choose a positive
divisor \(A\) of \(C_d\), then recover at most one candidate

\[
3B+1=\frac{9A^2+12A+1}{d},
\tag{18}

followed by

\[
M=\frac{A+H}{3B+1},
\qquad
p=\frac{(3B+1)H-B}{A}.
\tag{19}

The divisibilities, positivity, core primality, actual maximal-receipt guards,
terminal-first status, and E1--E5 remain separate checks. Equation (17)
does not produce a bound on \(d\), so it is not a finite global selector.

The proper range (7) bounds each candidate's local fiber index. Since
\(3B+1\ge3A+4\),

\[
d<\frac{9A^2+12A+1}{3A+4}<3A+1.
\]

Combining this with (14) gives

\[
\boxed{d\le3A-2.}
\tag{20}

## 5. The \(d=1\) fiber rederives an already excluded core row

Suppose \(d=1\). Equation (13) gives

\[
3B+1=9A^2+12A+1,
\qquad B=3A^2+4A.
\tag{21}

But then \(B\equiv0\pmod A\), so (8) becomes

\[
0\equiv3B^2+B-1\equiv-1\pmod A.
\]

Hence \(A=1\), and (21) gives \(B=7\). Formula (19) now uniquely gives

\[
H=43,\qquad e=22,\qquad M=2,\qquad p=939.
\tag{22}

Since \(939\equiv3\pmod {24}\), it is not a core prime. Therefore

\[
\boxed{
\text{no actual core proper-root stutter with }k=3\text{ has }d=1.}
\tag{23}

Here \(a=3\) and \(m=6\), so this is exactly the \((m,a)=(6,3)\) row
already excluded by the actual-small-root theorem. The value of this card is
not a second closure count for that row; it is the derivation of the new
fixed-\(d\) coordinates and an independent consistency check at their first
fiber.

Together with (14), every remaining actual \(k=3\) candidate satisfies

\[
\boxed{4\le d\le3A-2,\qquad d\equiv1\pmod3,\qquad A\mid C_d.}
\tag{24}

## 6. Cyclotomic gate and proof boundary

The primitive equations also show why the bare cyclotomic divisibility is not
an additional \(k=3\) elimination. Since \((A,H)=1\) and
\(pA+B=eH\), one has \(p\equiv-BA^{-1}\pmod H\), hence

\[
A^2(p^2+p+1)\equiv A^2-AB+B^2=H\equiv0\pmod H.
\tag{25}

Thus \(H\mid p^2+p+1\); when \(p\equiv1\pmod3\) and \(3\nmid H\), this
recovers \(3H\mid p^2+p+1\). The cyclotomic root condition therefore does
not by itself clear the remaining fibers.

This card supplies a finite-fiber parameterization for fixed \(d\) and
rederives the already excluded \(k=3,d=1\) row. It does not prove that every
\(k=3\) fiber is empty, does not physicalize a divisor of \(k\), and does not
provide a terminal or a verified successor. QC1, TR1, and
`T6_GLOBAL_SELECTOR_TOTALITY` remain `OPEN`.

## Focused reproduction

```bash
python3 reproductions/type_i_root_capacity_stutter_k_three_primitive_fiber_reduction.py --verify
python3 -m unittest tests/test_type_i_root_capacity_stutter_k_three_primitive_fiber_reduction.py
```

The verifier replays the exact reduction on a deliberately non-core \(d=1\)
curve point and a core-congruent but non-proper composite shadow. It performs
no parameter scan, no primality search, and no selector or certificate search.
