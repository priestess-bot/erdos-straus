---
kind: claim
claim_id: type-I-c8-qstar103-gap403-divisor-layer
title: c8 q-star=103 相位的 gap-403 divisor terminal layer
statement: >-
  在 c8 q-star=103 arithmetic phase s=86+103u、p=4129+4944u 中，gap
  m=403 有 x=103w、w=12u+11。真实 q-star roughness 下，三个固定
  103-adic Type II 小层 d=1,103,103^2 只有 d=103 可存活，且
  u=-1 mod403 时给直接 Type II terminal。u=14 mod179 给 Type I terminal，
  因 e=103*179=-4^{-1} mod403。一般 q=103-containing divisor layer
  精确由 a|w^2 的两个 residue condition 参数化。结论仅是 terminal-first
  arithmetic layer，不构造 actual C8 parent/path、admission 或 T6 closure。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-c8-second-full-excess-parent-anchored-universal-fallback
  - type-II-q-one-full-carrier-qstar-103-rough-selection-criterion
  - short-certificate-equivalence
topics:
  - type-I
  - type-II
  - f2
  - c-eight
  - q-star-103
  - terminal
  - bradford-gap
  - divisor-layer
  - proof-boundary
sources:
  - claim: type-I-c8-second-full-excess-parent-anchored-universal-fallback
    role: c8 arithmetic phase and parent-macro boundary
  - claim: type-II-q-one-full-carrier-qstar-103-rough-selection-criterion
    role: q-star=103 roughness exclusions
  - claim: short-certificate-equivalence
    role: Type-I/II normal-form reconstruction
visibility: public
last_checked: '2026-08-27'
---

# c8 q-star=103 相位的 gap-403 divisor terminal layer

## 1. Phase and gap

In the c8 \(q_\star=103\) arithmetic phase, write

\[
s=86+103u,
\qquad
p=48s+1=4129+4944u,
\tag{1}
\]

and put

\[
h=6u+5,
\qquad
6s-1=103h.
\tag{2}
\]

The actual \(q_\star=103\) roughness condition excludes
\(13\mid h\) and \(31\mid h\), among the other primes below \(103\).

For the legal gap

\[
m=403=13\cdot31,
\]

the Bradford parameter is

\[
x=\frac{p+403}{4}=103w,
\qquad
w=12u+11=2h+1.
\tag{3}
\]

For a core prime \(p>403\), \((x,403)=1\): if \(13\) or \(31\) divided
\(w\), then the identity \(p=4x-403\) would make the same prime divide
\(p\).

## 2. Fixed 103-adic Type-II layers

For \(d=1,103,103^2\), the Type-II condition is

\[
403\mid x+d.
\]

It gives the following exact table:

\[
\begin{array}{c|c|c}
d&\text{condition on }w&\text{disposition}\\
\hline
1&w\equiv313\pmod{403}&13\mid h,\ \text{roughness excludes}\\
103&w\equiv-1\pmod{403}&\text{valid Type-II layer}\\
103^2&w\equiv300\pmod{403}&13\mid h,\ \text{roughness excludes}
\end{array}
\tag{4}

\]

The middle line is equivalently

\[
u\equiv-1\pmod{403}.
\tag{5}

\]

Writing \(u=403v-1\), it gives

\[
w=4836v-1,\qquad x=103(4836v-1),
\]

and

\[
x+103=403\cdot1236v.
\]

Thus \(d=103\mid x^2\), \(d\le x\), and the standard Type-II condition
holds. Its denominators can be written explicitly as

\[
\frac4p
=\frac1x+\frac1{1236pv}
+\frac1{1236pv(4836v-1)}.
\tag{6}

\]

Two apparent large divisors are not core-prime routes:

\[
d=w\Longrightarrow403\mid104w\Longrightarrow31\mid w\Longrightarrow31\mid p,
\tag{7}

\]

\[
d=x\Longrightarrow403\mid206w\Longrightarrow403\mid w\Longrightarrow403\mid p.
\tag{8}

\]

They are therefore excluded for \(p>403\) prime.

## 3. Type-I layer

For a Type-I certificate, let \(e=x^2/d\) be the complementary divisor. The
required residue is

\[
e\equiv-4^{-1}\equiv302\pmod{403}.
\tag{9}

\]

If

\[
u\equiv14\pmod{179},
\tag{10}

\]

then \(179\mid w\). With

\[
e=103\cdot179\equiv302\pmod{403},
\]

one has \(e\mid x^2\), and \(d_I=x^2/e\) is a Type-I certificate. Indeed,
if \(w=179t\), then \(x=et\) and

\[
px+d_I\equiv4x^2+d_I=e t^2(4e+1)\equiv0\pmod{403}.
\tag{11}

\]

This arithmetic progression is not forced composite:

\[
p=73345+884976v
\quad\text{when}\quad u=14+179v,
\]

and its initial term is coprime to the step. This does not assert an actual
C8 parent, complete terminal-first miss, or an admissible state.

## 4. Exact q=103-containing divisor layer

The preceding certificates extend without factoring the large C8 fallback
target. For every \(a\mid w^2\),

\[
a\le w,\qquad a\equiv-w\pmod{403}
\Longrightarrow
d=103a\quad\text{is Type II},
\tag{12}

\]

and

\[
a\equiv179\pmod{403}
\Longrightarrow
e=103a\quad\text{is Type I}.
\tag{13}

\]

Equations (12)--(13) are exact for the \(103\)-containing divisor layer:
they are the Type-II condition \(x+d\equiv0\pmod{403}\) and the Type-I
condition \(e\equiv302\pmod{403}\), respectively. They do not exhaust all
possible gap-403 certificates.

## 5. Boundary

This is a conditional terminal-first arithmetic layer. It does not prove that
an actual C8 parent reaches any listed congruence, that the complete terminal
policy otherwise misses, or that a nonterminal C8 fallback target is admitted.
It provides no E1--E5 bundle, common admission, re-entry, or global T6
conclusion.
