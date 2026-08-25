---
kind: claim
claim_id: type-II-q-one-c9-r23-fixed-tail-terminal-ray
title: q=1 C=9 R=23 row 的固定尾终端子射线
statement: >-
  Let p be a core prime with p=1033 modulo 11088. Equivalently, in the q=1
  C=9 R=23 row write p=1008j+25 with j=1 modulo 11. Then
  K=(23p+1)/4 is divisible by 22, and e=K/22 satisfies e=17 modulo 23.
  The exact identity 4/p=1/e+1/K+1/(pK) is a direct Type I terminal.
  This is an outer p-level terminal leaf, not a C=9 persistent successor or
  a total terminal rule for the remaining R=23/35/11 rows.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c9-high-r-side-dual-small-chart
topics:
  - type-II
  - q-one
  - cofactor-nine
  - R-twenty-three
  - fixed-tail
  - terminal
  - proof-boundary
sources:
  - reproduction: reproductions/type_ii_q_one_c9_r23_fixed_tail_terminal_ray.py
    role: exact ray, divisor congruence, and certificate replay
visibility: public
last_checked: '2026-08-25'
---

# q=1 C=9 R=23 fixed-tail terminal ray

## 1. Fixed-tail certificate

For any canonical chart

\[
pR+1=4K,
\tag{1}
\]

suppose a divisor \(e\mid K^2\) satisfies

\[
e\equiv-K\pmod R.
\tag{2}
\]

Then both

\[
a=\frac{K+e}{R},
\qquad
b=\frac{K+K^2/e}{R}
\tag{3}
\]

are positive integers. Since \(4K\equiv1\pmod R\), \(K\) is invertible
modulo \(R\), and (2) also gives \(K^2/e\equiv-K\pmod R\). Thus

\[
(Ra-K)(Rb-K)=K^2,
\]

so \(R/K=1/a+1/b\). Combining this with
\[
\frac4p=\frac RK+\frac1{pK}
\tag{4}
\]
gives a direct Type I terminal.

## 2. The R=23 C=9 subray

The R=23 row of the C=9 r-side dual is

\[
p=1008j+25,
\qquad
K=\frac{23p+1}{4}=5796j+144.
\tag{5}
\]

If \(j\equiv1\pmod{11}\), equivalently

\[
\boxed{p\equiv1033\pmod{11088},}
\tag{6}
\]

then

\[
22\mid K,
\qquad
e:=\frac K{22}\equiv17\pmod{23}.
\tag{7}
\]

Equation (7) is exactly (2), because \(K\equiv6\pmod{23}\). Formula (3)
reduces to \(a=e\), \(b=K\), and therefore every core prime in (6) has

\[
\boxed{
\frac4p=
\frac1{K/22}+\frac1K+\frac1{pK}.}
\tag{8}
\]

For \(p=1033\), this is

\[
\frac4{1033}
=\frac1{270}+\frac1{5940}+\frac1{6136020}.
\tag{9}
\]

## 3. Boundary

This terminal is available before any q1 C=9 macro is admitted. It does not
show that every \(p=336k+25\) input is terminal: the R=23 q1-G control
\(p=3049\) is outside (6) and misses this fixed-tail divisor condition.
No source receipt, ABSORB re-entry, shared producer, F2 totality, or T6
totality is claimed for the complementary rows.
