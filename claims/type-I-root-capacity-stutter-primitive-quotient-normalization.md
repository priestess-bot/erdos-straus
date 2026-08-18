---
kind: claim
claim_id: type-I-root-capacity-stutter-primitive-quotient-normalization
title: proper-root stutter 的 primitive quotient 正规化与 cyclotomic 饱和
statement: >-
  对满足 actual proper-root stutter 算术条件的整数 p,h,m,e,a，令
  b=e-1、N=a^2-ab+b^2=hk、g=gcd(a,b)，并假设 h divides p^2+p+1。
  则 g divides h,k,m。写 a=gA、b=gB、h=g alpha、k=g kappa、m=gM，便有
  gcd(A,B)=1、e=gB+1，以及精确 primitive system
  A^2-AB+B^2=alpha kappa、A+alpha=eM、pA+B=e alpha。
  进一步，令 C_p=p^2+p+1，则
  e^2 alpha+e(A-2B)+kappa=g A^2(C_p/h)，从而
  g divides alpha+kappa+A-2B。若 q 是 q|kappa、q不整除h 的素数，并令
  v=C_p/h，则 q不整除gA，且 q|v 当且仅当 q|e 或
  B congruent to (p+1)A mod q。故所有 quotient-only 素因子 q|k、q不整除h
  必满足 q|kappa 且 q不整除g；所有 q|g 则同时整除 h,k,m,a,b，且 q not equal 3 时
  是既有 q|u root-capacity source-menu 的输入。此正规化不保证 menu 命中，不
  physicalize primitive kappa 因子，也不构造 E1--E5 successor。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-common-divisor-alignment
  - type-I-root-capacity-stutter-finite-curve-constraint
  - type-I-root-capacity-stutter-provenance-dispatch
topics:
  - type-I
  - root-capacity
  - stutter
  - eisenstein-quotient
  - primitive-normal-form
  - cyclotomic-saturation
  - cyclotomic-complement
  - provenance
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-common-divisor-alignment
    role: shared-factor-divides-h-and-k
  - claim: type-I-root-capacity-stutter-finite-curve-constraint
    role: actual-stutter-linear-identities
  - claim: type-I-root-capacity-stutter-provenance-dispatch
    role: h-supported-q-source-menu-boundary
  - reproduction: reproductions/type_i_root_capacity_stutter_primitive_quotient_normalization.py
    role: exact-normalization-saturation-and-quotient-split-controls
visibility: public
last_checked: '2026-08-18'
---

# proper-root stutter 的 primitive quotient 正规化与 cyclotomic 饱和

## 1. Scope

Fix the arithmetic data of an actual proper-root stutter receipt:

\[
a=em-h,
\qquad
pa=e(h-1)+1,
\qquad
b=e-1,
\tag{1}
\]

\[
N=a^2-ab+b^2=hk,
\qquad
h\mid C_p:=p^2+p+1.
\tag{2}
\]

The conclusion below is an exact normalization of these integer equations. It
does not assert that every normalized tuple is an actual maximal receipt, and
it does not create a recursive selector output.

Put

\[
g=(a,b).
\tag{3}
\]

The common-divisor alignment theorem already gives

\[
g\mid(h,k).
\tag{4}
\]

## 2. Primitive quotient coordinates

Since \(b=e-1\), one has \(e\equiv1\pmod g\), hence \((e,g)=1\). From
the first equation in (1), together with \(g\mid a,h\), it follows that

\[
g\mid em,
\qquad\text{and therefore}\qquad
\boxed{g\mid m.}
\tag{5}
\]

Define positive integers

\[
A=\frac ag,
\qquad B=\frac bg,
\qquad
\alpha=\frac hg,
\qquad
\kappa=\frac kg,
\qquad M=\frac mg.
\tag{6}
\]

Then \((A,B)=1\), \(e=gB+1\), and division of (1)--(2) by the
appropriate powers of \(g\) gives the exact primitive system

\[
\boxed{
\begin{aligned}
A^2-AB+B^2&=\alpha\kappa,\\
A+\alpha&=eM,\\
pA+B&=e\alpha.
\end{aligned}}
\tag{7}
\]

Conversely, (6)--(7), together with \(e=gB+1\), reconstruct the two
stutter equations in (1) and the norm factorization in (2). Thus the
normalization does not discard a branch of the integer stutter curve; it
separates the common Eisenstein-coordinate factor \(g\) from the remaining
primitive quotient factor \(\kappa\).

## 3. Cyclotomic saturation

The cyclotomic calculation used by the common-divisor alignment theorem is

\[
a^2C_p=h\bigl(e^2h+e(a-2b)+k\bigr).
\tag{8}
\]

Substitute (6) into (8) and cancel \(g^2\). This yields

\[
A^2C_p
=\alpha\bigl(e^2\alpha+e(A-2B)+\kappa\bigr).
\tag{9}
\]

Because the actual root gate gives \(C_p=g\alpha(C_p/h)\), (9) has the
stronger integral form

\[
\boxed{
e^2\alpha+e(A-2B)+\kappa
=gA^2\frac{C_p}{h}.}
\tag{10}
\]

In particular, reducing (10) modulo \(g\), using \(e\equiv1\pmod g\),
gives the compact saturation gate

\[
\boxed{g\mid\alpha+\kappa+A-2B.}
\tag{11}
\]

Equation (11) is unavailable on an abstract stutter curve which fails
\(h\mid C_p\). It is therefore an actual-root restriction rather than a
formal reparameterization.

## 4. Quotient-only cyclotomic split

Put

\[
v=\frac{C_p}{h}.
\]

Use \(e\alpha=pA+B\) from (7) in (10). This removes the normalized
height from the left-hand side and gives the exact bridge

\[
\boxed{
gA^2v=\kappa+e\bigl((p+1)A-B\bigr).}
\tag{12}
\]

Now let \(q\) be a prime with

\[
q\mid\kappa,
\qquad q\nmid h.
\tag{13}
\]

The second condition gives \(q\nmid g\alpha\). Since

\[
A^2-AB+B^2=\alpha\kappa
\]

is divisible by \(q\), \(q\mid A\) would force \(q\mid B\), contrary to
\((A,B)=1\). Thus \(gA^2\) is a \(q\)-unit. Reducing (12) modulo \(q\)
therefore gives the exact dichotomy

\[
\boxed{
q\mid v
\quad\Longleftrightarrow\quad
q\mid e
\quad\text{or}\quad
B\equiv(p+1)A\pmod q.}
\tag{14}
\]

For the proper-root notation \(h=3u\) and
\(C_p=3M_0\), this is a split according to whether \(q\mid M_0/u\).
In particular, a quotient-only factor outside the cyclotomic complement
must satisfy both \(q\nmid e\) and
\(B\not\equiv(p+1)A\pmod q\).

This is an arithmetic partition of the primitive quotient factor only. It
does not turn either branch into a source occurrence, a terminal, a target,
an E4 lift, or a T5-admissible successor.

## 5. Provenance partition of the quotient

Every prime factor of \(g\) divides all of

\[
g\mid(a,b,h,k,m).
\tag{15}
\]

For a proper-root receipt with \(h=3u\), any such prime \(q\ne3\) divides
\(u\), so it is already in the input class of the root-capacity
external-source menu. This statement concerns provenance only: that finite
menu can still be empty.

On the other hand, if

\[
q\mid k,
\qquad q\nmid h,
\tag{16}
\]

then \(q\nmid g\) by (4), and \(k=g\kappa\) gives

\[
\boxed{q\mid\kappa.}
\tag{17}
\]

Thus every genuinely quotient-only carrier occurs in the primitive factor
\(\kappa\), never in the shared coordinate factor \(g\). A prime of
\(\kappa\) may still be \(h\)-supported when it also divides
\(g\alpha=h\); (17) is a one-way localization, not a claim that all of
\(\kappa\) is quotient-only.

This reduces the QC1 provenance problem to two explicitly different inputs:
the shared \(g\)-part has an existing source type, whereas primitive factors
of \(\kappa\) outside \(h\) require an independent physicalization or a
TR1-style exit. It supplies neither a terminal certificate nor E1--E5.

## 6. Focused reproduction

```bash
python3 reproductions/type_i_root_capacity_stutter_primitive_quotient_normalization.py --verify
python3 -m unittest tests/test_type_i_root_capacity_stutter_primitive_quotient_normalization.py
```

The controls replay one shared-factor root-shape tuple, a quotient-only
control outside the cyclotomic complement, a quotient-only control in its
\(q\mid e\) branch, and an abstract \(k=3\) curve point that fails the
cyclotomic root gate. They do not search for actual receipts, terminals,
sources, or selector paths.
