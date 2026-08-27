---
kind: claim
claim_id: type-I-root-capacity-stutter-m-three-dual-norm-inverse-divisor-fiber
title: proper-root m=3 dual-norm 的 inverse divisor fiber 与低 A 清除
statement: >-
  在 actual proper-root m=3,d=13,s_d=3 core 中，令
  Q_A=7A^2+A+1、r=Q_A/u。则两条 basic divisor gates 等价于
  r divides Q_A 且 A divides r^2-r+3；令 ell=(r^2-r+3)/A，另有
  r divides ell^2+3ell+63。故固定 A 的 dual-norm system 是 exact finite
  divisor fiber。叠加 d=13,s=3 的 A=52t-1,t=1 mod6,u=2A+481 mod702
  条件，可严格排空 13<=t<=193，因而 t>=199、A>=10347、u>=21175。
  本结论只作 actual necessary-core Diophantine pruning，不给 terminal、E1--E5 或 T6 closure。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction
  - type-I-root-capacity-stutter-m-three-natural-fan-high-cofactor-barrier
topics:
  - type-I
  - f3
  - proper-root
  - m-three
  - dual-norm
  - divisor-fiber
  - finite-clearance
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction
    role: m=3 two divisor gates and actual parameter constraints
  - claim: type-I-root-capacity-stutter-m-three-natural-fan-high-cofactor-barrier
    role: high-end interpretation of the same actual core
visibility: public
last_checked: '2026-08-27'
---

# proper-root m=3 dual-norm 的 inverse divisor fiber 与低 A 清除

## 1. Exact inverse fiber

Work in the actual \(m=3\) divisor-gate core, with

\[
A\mid3u^2-u+1,
\qquad
u\mid Q_A:=7A^2+A+1,
\qquad (A,u)=1.
\tag{1}
\]

Set

\[
r=\frac{Q_A}{u}.
\tag{2}
\]

Since \(Q_A\equiv1\pmod A\), one has \(ur\equiv1\pmod A\). Multiplying
the first divisibility in (1) by \(r^2\) gives

\[
\boxed{
A\mid3u^2-u+1
\Longleftrightarrow
A\mid r^2-r+3.}
\tag{3}
\]

The reverse implication follows by the same multiplication because \(r\) is
a unit modulo \(A\). Thus the two original divisor gates are exactly
equivalent to

\[
\boxed{r\mid Q_A,\qquad A\mid r^2-r+3,\qquad u=Q_A/r.}
\tag{4}
\]

This is an inverse finite divisor fiber at fixed \(A\), not merely a
necessary one-way sieve.

Let

\[
\ell=\frac{r^2-r+3}{A}.
\tag{5}
\]

Multiplying \(Q_A\) by \(\ell^2\) and using \(A\ell=r^2-r+3\) gives

\[
Q_A\ell^2=7(r^2-r+3)^2+\ell(r^2-r+3)+\ell^2.
\]

Reduction modulo \(r\) yields the second-order divisor gate

\[
\boxed{r\mid\ell^2+3\ell+63.}
\tag{6}
\]

In the actual core \(A\equiv3\pmod{24}\), so \(Q_A\equiv1\pmod3\) and
all prime factors of \(r\) are \(1\pmod3\), by the discriminant
\(-243\) of (6). Conversely, for every prime \(q\mid A\), \(q\ne11\),
(3) makes \(-11\) a quadratic residue modulo \(q\). These are support
restrictions, not terminal certificates.

## 2. Actual d=13, s=3 filters

In the \(d=13,s_d=3\) core,

\[
A=52t-1,\qquad t\equiv1\pmod6,\qquad t\ge13,
\tag{7}
\]

and the actual coordinate parameterization gives

\[
u=2A+481+702z,\qquad z\ge0.
\tag{8}

Let \(c=2A+481\). For the values in (7), \((c,702)=1\), so every candidate
in (4) must satisfy

\[
0<r\le R_A:=\left\lfloor\frac{Q_A}{c}\right\rfloor,
\qquad
r\equiv Q_Ac^{-1}\pmod {702},
\tag{9}
\]

in addition to \(A\mid r^2-r+3\). For \(A\ge675\), the general size bound
is

\[
r\le\left\lfloor\frac{Q_A}{2A+6}\right\rfloor
=\frac{7A-21}{2}.
\tag{10}

## 3. Exact clearance through t=193

There are exactly 31 values \(t\equiv1\pmod6\) with
\(13\le t\le193\). For the following 21 values, the displayed prime divisor
\(q\mid A\) has \(\left(\frac{-11}{q}\right)=-1\), so (3) is impossible:

\[
\begin{array}{c|rrrrrrrrrrr}
t&19&43&49&55&61&67&85&91&97&103&109\\
\hline
q&7&149&283&953&7&43&491&19&41&7&1889\\[2pt]
t&115&121&133&139&145&151&169&175&181&187\\
\hline
q&1993&233&461&73&7&2617&29&337&3137&7
\end{array}
\tag{11}

\]

The remaining ten values admit roots of \(r^2-r+3\) modulo \(A\). Solving
that congruence together with (9), the following table lists the least
positive CRT representative \(m\) over all root classes and the upper bound
\(R_A\):

\[
\begin{array}{c|rrrrrrrrrr}
t&13&25&31&37&73&79&127&157&163&193\\
\hline
R_A&1742&3836&4906&5982&12491&13579&22298&27753&28844&34300\\
m&367&48883&28213&6139&75169&36247&850879&51145&937459&5749
\end{array}
\tag{12}

\]

All rows with \(m>R_A\) have no candidate. In the two remaining rows,
direct division gives

\[
Q_{675}\equiv87\pmod {367},
\qquad
Q_{10035}\equiv4976\pmod {5749},
\tag{13}

\]

so those CRT candidates do not divide \(Q_A\). Thus the complete band is
empty:

\[
\boxed{t\ge199,\qquad A\ge10347,\qquad u\ge21175.}
\tag{14}

\]

## 4. Boundary

This is an exact finite Diophantine clearance in the actual necessary core.
It does not prove that every higher \(t\) fiber is empty, does not construct
a terminal or a source path, and does not supply E1--E5, common admission,
re-entry, or a global T6 conclusion.
