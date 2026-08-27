---
kind: claim
claim_id: type-I-root-capacity-stutter-m-three-high-cofactor-terminal-screen-boundary
title: proper-root m=3 high-cofactor 的直接 terminal 扇与近 cofactor Type-II 屏蔽
statement: >-
  在 actual proper-root m=3,d=13,s_d=3 natural-fan miss core 中，p=52C-3
  且 C>=1993。若 p+4=52C+1 或 (p+1)/2=26C-1 含有任一 3 mod4 因子 m，
  则分别由 d=1 Type II 或 e=x Type I 给出直接 terminal。因此 survivor 的这两数
  均不得有 3 mod4 素因子。另一方面合法 gaps m=4C+3 与 m=4C-1 的完整 Type-II
  divisor screen 全空。这些结论提供 terminal-first 的必要屏蔽，不证明其余 gap、
  E1--E5 或 T6 closure。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-m-three-natural-fan-high-cofactor-barrier
  - short-certificate-equivalence
topics:
  - type-I
  - type-II
  - f3
  - proper-root
  - m-three
  - terminal-first
  - high-cofactor
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-m-three-natural-fan-high-cofactor-barrier
    role: actual high-cofactor core and C>=1993
  - claim: short-certificate-equivalence
    role: Type-I/II normal-form reconstruction
visibility: public
last_checked: '2026-08-27'
---

# proper-root m=3 high-cofactor 的直接 terminal 扇与近 cofactor Type-II 屏蔽

## 1. Scope and two direct terminal fans

Work in the actual `m=3`, \(d=13\), \(s_d=3\) natural-fan miss core. The
established high-cofactor barrier gives

\[
p=52C-3,\qquad C\ge1993,\qquad C\equiv1\pmod6.
\tag{1}
\]

For a legal gap \(m\equiv3\pmod4\), write

\[
x=\frac{p+m}{4}.
\]

If an odd divisor \(m\equiv3\pmod4\) divides

\[
p+4=52C+1,
\tag{2}
\]

then \(m\mid4(x+1)\), hence \(m\mid x+1\). The Type-II normal form with
\(d=1\mid x^2\) gives a direct terminal certificate.

If instead an odd divisor \(m\equiv3\pmod4\) divides

\[
\frac{p+1}{2}=26C-1,
\tag{3}
\]

then the Type-I normal form with \(e=x\mid x^2\) applies, because
\(m\mid x(p+1)\). Both gaps are proper and legal: a divisor as in (2) or
(3) is smaller than \(p\) and is \(3\pmod4\).

Thus a terminal-first survivor must satisfy the stronger prime-support
exclusion

\[
\boxed{
52C+1\text{ and }26C-1
\text{ have no prime factor }3\pmod4.}
\tag{4}
\]

This is a necessary support condition, not a claim that it is impossible.

## 2. The gap 4C+3 has no Type-II divisor

Set

\[
m_+=4C+3,\qquad x_+=14C.
\]

Any Type-II divisor must satisfy \(d\mid x_+^2\), \(1\le d\le x_+\), and
\(m_+\mid x_++d\). The last two conditions force precisely

\[
d\in\{2C+12,\ 6C+15,\ 10C+18\}.
\tag{5}
\]

For the first value, \((C,C+6)=1\), so divisibility by \(x_+^2=196C^2\)
would imply \(C+6\mid196\), impossible for \(C\ge1993\). The middle value
is divisible by \(3\), while \(3\nmid x_+\). For the last value,
\((C,5C+9)=1\), so divisibility would imply \(5C+9\mid98\), again
impossible. Therefore

\[
\boxed{\mathcal D_{II}(p,4C+3)=\varnothing.}
\tag{6}
\]

## 3. The gap 4C-1 has no Type-II divisor

Set

\[
m_-=4C-1,\qquad x_-=14C-1.
\]

The Type-II congruence and bound now force

\[
d\in\{2C-3,\ 6C-4,\ 10C-5,\ 14C-6\}.
\tag{7}
\]

The second and fourth values are even while \(x_-\) is odd. For the first,

\[
\gcd(2C-3,14C-1)\mid20,
\]

and both numbers are odd, so the gcd is at most \(5\). For the third,

\[
\gcd(10C-5,14C-1)\mid30,
\]

and \(x_-\equiv1\pmod3\), so again the gcd is at most \(5\). If
\(a\mid b^2\), then \(a\le\gcd(a,b)^2\); neither odd candidate in (7)
can therefore divide \(x_-^2\), because each exceeds \(25\). Hence

\[
\boxed{\mathcal D_{II}(p,4C-1)=\varnothing.}
\tag{8}
\]

## 4. Why the two fans are not a cover

The two direct terminal fans are compatible with the fan-miss cofactor support
and with core primality. An arithmetic control is

\[
C=401077,\qquad p=20856001.
\tag{9}
\]

Both \(C\) and \(p\) are prime and \(1\pmod6\) and \(1\pmod{24}\),
respectively. Moreover

\[
p+4=20856005=5\cdot4171201,
\]

and both displayed factors are \(1\pmod4\), while

\[
\frac{p+1}{2}=10428001
\]

is prime and \(1\pmod4\). Thus neither direct fan in Section 1 fires.
All listed primalities are finite trial-division checks.

This control also passes the fixed-fiber and first \(-11\)-norm identities:

\[
F=47628865,\quad H=27397637,\quad u=4979713,
\]

\[
A=1561923,\quad\rho=618622,\quad\lambda=2205129,
\]

with

\[
FH=3p^2+p+1,\qquad AF=3u^2-u+1,
\]

\[
A\lambda=9\rho^2+5\rho+1,\qquad
52C=6A+15\rho+7+\lambda.
\tag{10}

\]

It is deliberately not an actual core receipt: the unconsumed second norm
fails,

\[
7\rho^2+4\rho+1\equiv3179188\not\equiv0\pmod {4979713}.
\tag{11}

\]

Therefore neither the direct fans, nor core support, primality, the fixed
fiber, and the first norm jointly prove a contradiction. This is an arithmetic
negative control only, not a terminal-first survivor or a counterexample.

There is no local support obstruction to the second norm either. If every
prime factor of an odd \(U\) is \(1\pmod3\), then

\[
7r^2+4r+1\equiv0\pmod U
\tag{12}

\]

has a solution. For each prime \(\ell\ne7\) dividing \(U\), the discriminant
is \(-12\), and \(\left(\frac{-3}{\ell}\right)=1\); its roots are simple and
lift to all \(\ell\)-powers by Hensel. At \(\ell=7\), the root
\(r\equiv5\pmod7\) is simple as well. CRT then gives (12). Hence a terminal
or emptiness proof must use the global coupling of \(u\) to \(A,\rho,\lambda\)
and the primitive equations, not just the \(1\pmod3\) support direction.

## 5. Boundary

The claim covers two direct terminal fans and two specified near-cofactor
Type-II screens only. It does not classify all Type-I certificates at these
gaps, all higher gap families, the natural fan itself, or any source/admission
obligation. It supplies no E1--E5 edge or global T6 conclusion.
