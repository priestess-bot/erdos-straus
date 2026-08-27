---
kind: claim
claim_id: type-I-root-capacity-stutter-m-three-high-cofactor-near-gap-complete-miss
title: proper-root m=3 high-cofactor 两条近 gap 的完整 Bradford MISS
statement: >-
  在 actual proper-root m=3,d_core=13,s_d=3 natural-fan miss core 中，
  p=52C-3、C>=1993、C=1 mod6。对两条合法 gaps m+=4C+3 与 m-=4C-1，
  Bradford Type I 和 Type II divisor sets 均为空。Type I 以 certificate divisor
  d|x^2 与 complement e=x^2/d 区分，借助 kappa=(4e+1)/m=3 mod4 的精确
  Diophantine equations得到唯一 formal high solution C=2774，但它不在 actual core。
  结果只关闭这两条固定 gap terminal screens，不证明其它 gap、actual source、E1--E5 或 T6 closure。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-m-three-high-cofactor-terminal-screen-boundary
  - type-I-root-capacity-stutter-m-three-natural-fan-high-cofactor-barrier
  - short-certificate-equivalence
topics:
  - type-I
  - type-II
  - f3
  - proper-root
  - m-three
  - high-cofactor
  - bradford-gap
  - family-empty
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-m-three-high-cofactor-terminal-screen-boundary
    role: near-gap Type-II emptiness and direct terminal context
  - claim: type-I-root-capacity-stutter-m-three-natural-fan-high-cofactor-barrier
    role: actual high-cofactor domain C>=1993
  - claim: short-certificate-equivalence
    role: Bradford Type-I/II divisor equivalence
visibility: public
last_checked: '2026-08-27'
---

# proper-root m=3 high-cofactor 两条近 gap 的完整 Bradford MISS

## 1. Scope and notation

Work in the actual `m=3`, \(d_{\rm core}=13\), \(s_d=3\) high-cofactor
natural-fan miss core:

\[
p=52C-3,\qquad C\ge1993,\qquad C\equiv1\pmod6.
\tag{1}
\]

Set

\[
m_+=4C+3,quad x_+=14C,
\qquad
m_-=4C-1,quad x_-=14C-1.
\tag{2}

\]

Both gaps are legal. The Type-II sets were already shown empty. This claim
completes the Type-I screen. In this section `d` always means the Bradford
certificate divisor \(d\mid x^2\); its complement is

\[
e=\frac{x^2}{d}.
\tag{3}

The core label \(d_{\rm core}=13\) is unrelated to the certificate divisor.

## 2. Exact Type-I equations

Because \((x_\pm,m_\pm)=1\), each certificate divisor is coprime to its
gap. The Type-I condition is

\[
m_\pm\mid4x_\pm^2+d.
\tag{4}

For the plus gap,

\[
4x_+^2\equiv441\pmod {m_+},
\]

so

\[
d=j m_+-441,\qquad j\ge1.
\tag{5}

For the minus gap,

\[
4x_-^2\equiv25\pmod {m_-},
\]

so

\[
d=j m_--25,\qquad j\ge1.
\tag{6}

Since \(de=x_\pm^2\) and \((d,m_\pm)=1\), define

\[
\kappa=\frac{4e+1}{m_\pm}>0.
\tag{7}

\]

The gaps are \(3\pmod4\), hence \(\kappa\equiv3\pmod4\). Expanding
\((jm-a)(\kappa m-1)=4x^2\) gives the exact equations

\[
(j\kappa-49)m_+=j+441\kappa-294,
\tag{8}

\]

\[
(j\kappa-49)m_-=j+25\kappa+70.
\tag{9}

\]

No Type-II inequality such as \(d\le x\) has been used.

## 3. Finite high-domain analysis

The bounds from (1) are

\[
m_+\ge7975,\qquad m_-\ge7971.
\tag{10}

\]

Equations (8)--(9) force \(j\kappa>49\). Rewriting them as

\[
j(\kappa m_+-1)=49m_++441\kappa-294,
\]

\[
j(\kappa m_--1)=49m_-+25\kappa+70
\]

shows \(j\le16\), \(\kappa\le51\) for the plus case, and
\(\kappa\le47\) for the minus case. More precisely,

\[
j-\frac{49}{\kappa}
=\frac{(21\kappa-7)^2}{\kappa(\kappa m_+-1)}\in(0,1),
\tag{11}

\]

\[
j-\frac{49}{\kappa}
=\frac{(5\kappa+7)^2}{\kappa(\kappa m_--1)}\in(0,1).
\tag{12}

\]

The values \(\kappa=3\) and \(7\) are immediately impossible: the first
would force \(j=17\), while the second puts an integer strictly between
\(7\) and \(8\). The remaining \(\kappa\equiv3\pmod4\) values give the
following complete table, where the entries are the value of \(m_+\) and
\(m_-\) forced by (8)--(9):

\[
\begin{array}{c|c|c|c}
\kappa&j&m_+&m_-\\
\hline
11&5&2281/3&175/3\\
15&4&575&449/11\\
19&3&1011&137/2\\
23&3&2463/5&162/5\\
27&2&2323&747/5\\
31&2&13379/13&847/13\\
35&2&15143/21&947/21\\
39&2&583&1047/29\\
43&2&18671/37&31\\
47&2&4087/9&1247/45\\
51&1&11099&\text{not allowed}
\end{array}
\tag{13}

\]

For the minus gap, no integer table entry reaches \(m_-\ge7971\). For the
plus gap, the only integer entry reaching \(m_+\ge7975\) is

\[
m_+=11099,\qquad C=\frac{11099-3}{4}=2774.
\]

But \(2774\equiv2\pmod6\), contrary to (1). Thus both Type-I sets are
empty in the actual high-cofactor domain.

## 4. Complete two-gap result

Combining the preceding Type-I argument with the already established Type-II
emptiness gives

\[
\boxed{
\mathcal D_I(p,m_+)=\mathcal D_{II}(p,m_+)=
\mathcal D_I(p,m_-)=\mathcal D_{II}(p,m_-)=\varnothing.}
\tag{14}

\]

The excluded formal plus solution is real arithmetic, not a missing table row:
for \(C=2774\),

\[
d=10658,\qquad e=141512,\qquad de=38836^2,
\]

but its associated \(p=144245\equiv5\pmod{24}\) is outside the core prime
domain. This prevents the result from being misread as a no-go for arbitrary
large \(C\).

## 5. Boundary

This claim closes only the complete Bradford screens at the two named gaps.
It does not prove that every other gap misses, that an actual source exists,
or that a nonterminal state has a recursive edge. It supplies no E1--E5,
admission, re-entry, or global T6 conclusion.
