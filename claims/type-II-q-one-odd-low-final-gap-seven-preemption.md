---
kind: claim
claim_id: type-II-q-one-odd-low-final-gap-seven-preemption
title: q=1 odd second-anchor low final 的模 336 分类与 gap-7 预占
statement: >-
  In the ordinary q=1 full-carrier odd-t second-anchor contraction, the
  final chart is low exactly when p is congruent to 25 or 265 modulo 336.
  Every core prime in the latter class has the direct Type II gap-7
  certificate with x=(p+7)/4 and d=2. Thus an ordered terminal prefix that
  tests this certificate preempts the p=265 mod336 low-final branch before
  q=1 G handoff. The only odd low-final congruence class left after this
  preemption is p=25 mod336; no claim is made that it is terminal or empty.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-root-second-anchor-contraction
  - type-II-q-one-full-carrier-second-anchor-fixed-n-macro
  - short-certificate-equivalence
topics:
  - type-II
  - q-one
  - full-carrier
  - second-anchor
  - terminal-first
  - gap-seven
  - congruence
  - absorb
  - proof-boundary
sources:
  - reproduction: reproductions/type_ii_q_one_odd_low_final_gap_seven_preemption.py
    role: symbolic congruence and exact Type II certificate controls
visibility: public
last_checked: '2026-08-25'
---

# q=1 odd low-final gap-7 preemption

## 1. The odd macro quotient parameter

Let \(p=24t+1\) with \(t\) odd. The q=1 second-anchor macro has

\[
L=2(10t+1),
\tag{1}
\]

and its quotient-fold remainder \(\delta\) determines the unique integer
\(j\) by

\[
14\delta+3=jp,\qquad 1\le j\le13.
\tag{2}
\]

The final determinant parameter is

\[
21n=5jp+7j-15,
\tag{3}
\]

and the final chart has \(R_T=4L-n\). Since

\[
4L=\frac{10p+14}{3},
\tag{4}
\]

substitution of (3) gives

\[
R_T-p=
\frac{(49-5j)p+113-7j}{21}.
\tag{5}
\]

For \(p\ge73\), equation (5) is negative exactly when
\(j\ge10\). But \(p\) is odd, so (2) makes \(j\) odd; hence

\[
R_T<p
\Longleftrightarrow
j\in\{11,13\}.
\tag{6}
\]

Equation (2) also says

\[
j\equiv3p^{-1}\pmod {14}.
\tag{7}
\]

The two values in (6) are therefore equivalent to

\[
p\equiv13,11\pmod {14},
\tag{8}
\]

respectively. Since odd \(t\) means \(p\equiv25\pmod {48}\), Chinese
remaindering gives the exact split

\[
\boxed{
R_T<p
\Longleftrightarrow
p\equiv25\ \text{or}\ 265\pmod {336}.}
\tag{9}
\]

## 2. The 265 mod 336 branch is already terminal

Suppose

\[
p=336k+265.
\tag{10}
\]

Then \(p\equiv6\pmod7\) and \(p\equiv1\pmod8\). Put

\[
x=\frac{p+7}{4}=84k+68.
\tag{11}
\]

Thus \(2\mid x\), \(x\equiv5\pmod7\), and hence

\[
d=2\mid x^2,\qquad d\le x,\qquad 7\mid x+d.
\tag{12}
\]

The Type II divisor criterion gives the explicit terminal

\[
\boxed{
\frac4p=
\frac1x+
\frac1{p(x+2)/7}+
\frac1{p(x+x^2/2)/7}.}
\tag{13}
\]

This check depends only on \(p\), so it is a root-level terminal and must
run before a q=1 G handoff or its later macro states are created.

## 3. Resulting residual

When the ordered terminal prefix contains (13), the \(265\pmod {336}\)
branch cannot reach the q=1 contraction. By (9), the odd low-final residual
therefore reduces to the single congruence class

\[
\boxed{p\equiv25\pmod {336}.}
\tag{14}
\]

For example, \(p=1033\) belongs to (14) and has a low contraction final
chart. It may have other terminal certificates, but that fact is not used in
this proof. Thus (14) is a residual classification, not a nonterminal
example.

This card does not treat even \(t\), whose final macro target is already
high; it does not prove the \(25\pmod {336}\) branch terminal, empty, or
recursively total; and it does not close F2, T6, or the conjecture.
