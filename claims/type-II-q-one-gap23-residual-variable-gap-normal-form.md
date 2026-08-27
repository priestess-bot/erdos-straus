---
kind: claim
claim_id: type-II-q-one-gap23-residual-variable-gap-normal-form
title: q=1 gap-23 残余的可变 gap 正规形与 Type II 递降门槛
statement: >-
  In the q=1 G gap-23 residual s=ell*u, ell||s, ell=s mod 23 in {5,14},
  write p=24ell*u-23 and choose m_a=23+4ell*a. Then
  x_a=(p+m_a)/4=ell(6u+a) and every Type I certificate is exactly a divisor
  condition e_{a,j}|ell^2(6u+a)^2 for e_{a,j}=(4j+3)ell*a+23j+17. Every
  Type II certificate has the usual factor-pair form. It yields the standard
  integer two-tail descent precisely when D_a=6+ell*a divides N_a=6u+a; for
  a>6(u-1)/(ell-1) that descent is impossible. Since q=1 G excludes ell=5,
  ell>=37 and the descent window is at most floor((u-1)/6), while the legal
  gaps run through a=6u-1. This is a terminal/descent normal form and a
  strict no-go for most variable gaps, not a proof that a terminal exists.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-type-II-gap-23-two-box-classification
  - type-II-q-one-gap23-residual-cross-linear-separation
  - short-certificate-equivalence
  - type-II-factor-pair-carrier-strict-descent
topics:
  - T6
  - q-one
  - gap-twenty-three
  - variable-gap
  - type-I
  - type-II
  - descent
  - proof-boundary
sources:
  - claim: type-I-type-II-gap-23-two-box-classification
    role: residual factorization
  - claim: type-II-q-one-gap23-residual-cross-linear-separation
    role: q=1 G exclusion ell not equal to 5
  - claim: short-certificate-equivalence
    role: complete Bradford divisor reconstruction
  - claim: type-II-factor-pair-carrier-strict-descent
    role: Type-II two-tail descent criterion
visibility: public
last_checked: '2026-08-27'
---

# Variable-Gap Residual Normal Form

## 1. Variable Family

Fix the q=1 G gap-23 residual

\[
s=\ell u,\qquad
\ell\parallel s,\qquad
\ell\equiv s\in\{5,14\}\pmod {23},
\tag{1}
\]

where \(\ell\) is prime and every prime factor of \(u\) is
\(1\pmod {23}\). The cross-linear separation theorem gives
\(\ell\ne5\), hence

\[
\ell\ge37,\qquad (\ell,6)=1.
\tag{2}
\]

For a nonnegative integer \(a\), define

\[
p=24\ell u-23,\qquad
m_a=23+4\ell a,\qquad
N_a=6u+a,\qquad
D_a=6+\ell a.
\tag{3}
\]

Then

\[
m_a=4D_a-1,\qquad
x_a=\frac{p+m_a}{4}=\ell N_a.
\tag{4}
\]

The natural-gap condition \(m_a\le p-2\) is exactly

\[
0\le a\le\left\lfloor6u-\frac{12}{\ell}\right\rfloor
=6u-1.
\tag{5}
\]

The last equality uses \(\ell\ge37\).

## 2. Exact Type-I Form

Let \(e=x_a^2/d\). Since \((x_a,m_a)=1\), the complete Type-I condition is

\[
4e+1\equiv0\pmod {m_a}.
\tag{6}
\]

All positive solutions of (6) are

\[
e=e_{a,j}:=(4j+3)\ell a+23j+17,
\qquad j\ge0.
\tag{7}
\]

Thus

\[
\boxed{
\operatorname{TypeI}(m_a)
\Longleftrightarrow
\exists j\ge0:\quad
e_{a,j}\mid\ell^2N_a^2.
}
\tag{8}
\]

For \(j=0\), put

\[
E_a=3\ell a+17.
\tag{9}
\]

Because \((E_a,\ell)=1\), the following is an explicit terminal ray:

\[
\boxed{
E_a\mid N_a^2
\Longrightarrow
\operatorname{TypeI}(m_a).
}
\tag{10}
\]

Take \(e=E_a\) and \(d=x_a^2/E_a\). A narrower parametric subray is

\[
N_a=kE_a
\Longleftrightarrow
(3k\ell-1)a=6u-17k.
\tag{11}
\]

Every nonnegative integral solution of (11) in the range (5) gives a direct
Type-I terminal. No assertion is made that such a solution always exists.

## 3. Type-II Form and Two Explicit Rays

The complete Type-II condition is

\[
\boxed{
\operatorname{TypeII}(m_a)
\Longleftrightarrow
\exists d\mid\ell^2N_a^2:\quad
d\le\ell N_a,\quad
d\equiv-\ell N_a\pmod {m_a}.
}
\tag{12}
\]

Equivalently, there are \(A,B,C,K>0\) with

\[
(A,B)=1,\qquad ABC=\ell N_a,\qquad A+B=m_aK,
\tag{13}
\]

and \(d=A^2C\).

Two conditional \(\ell\)-supported rays are:

\[
d=\ell
\Longrightarrow
m_a\mid N_a+1
\Longleftrightarrow
(4j\ell-1)a=6u+1-23j,
\tag{14}
\]

and, provided \(\ell\le N_a\),

\[
d=\ell^2
\Longrightarrow
m_a\mid N_a+\ell
\Longleftrightarrow
(4j\ell-1)a=6u+\ell-23j.
\tag{15}
\]

Here the integer \(j\) is positive whenever the displayed divisibility is
realized. These are terminal rays, not a covering theorem.

## 4. Strict Integer Descent Gate

For any Type-II factor pair in (13), the usual two-tail source parameter is

\[
n_a=\frac{p+m_a}{m_a+1}
=\frac{\ell N_a}{D_a}.
\tag{16}
\]

Because \((D_a,\ell)=1\),

\[
\boxed{
n_a\in\mathbb N
\Longleftrightarrow
D_a\mid N_a.
}
\tag{17}
\]

Write \(N_a=kD_a\). For \(a>0\),

\[
6(u-k)=a(k\ell-1).
\tag{18}
\]

Therefore \(k<u\), and the factor-pair lift is a strict integer descent:

\[
n_a=\ell k<\ell u=s<p.
\tag{19}
\]

Conversely, if \(D_a\nmid N_a\), this variable-gap Type-II certificate cannot
provide this standard integer two-tail descent. In particular,

\[
D_a>N_a
\Longleftrightarrow
(\ell-1)a>6(u-1)
\tag{20}
\]

is an unconditional obstruction. Hence

\[
\boxed{
a>\frac{6(u-1)}{\ell-1}
\Longrightarrow
\text{no variable-gap Type-II integer descent}.
}
\tag{21}
\]

Since \(\ell\ge37\), a potentially descending value must lie in

\[
a\le\left\lfloor\frac{6(u-1)}{\ell-1}\right\rfloor
\le\left\lfloor\frac{u-1}{6}\right\rfloor,
\tag{22}
\]

whereas the full legal interval runs through \(6u-1\).

For the actual residual control

\[
p=53089,\qquad\ell=2213,\qquad u=1,
\tag{23}
\]

all positive legal \(a\) fail (21). The \(a=0\) member is the already
missed gap 23. This does not rule out a direct terminal at positive \(a\).

## 5. Relation to Current Prefix

The q=1 G condition constrains \(X=6\ell u-5\), while this variable family
uses \(N_a=6u+a\). Their possible common factor satisfies

\[
\gcd(X,N_a)\mid\ell a+5.
\tag{24}
\]

The gap-7 and gap-11 linear forms have only

\[
\gcd(3\ell u-2,N_a)\mid\ell a+4,
\qquad
\gcd(2\ell u-1,N_a)\mid\ell a+3.
\tag{25}
\]

Thus q=1 G and the fixed prefix do not force (10), (14), (15), or (17).
They also do not supply an infinite obstruction without new simultaneous
prime/factorization input.

## 6. Boundary

This theorem provides exact terminal checks and a strict descent threshold.
It does not prove that every residual has a suitable \(a\), establish an
actual source path, construct E1--E5, or close any T6 family beyond the
already empty \(\ell=5\) subleaf.
