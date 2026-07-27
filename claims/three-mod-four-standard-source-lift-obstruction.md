---
kind: claim
claim_id: three-mod-four-standard-source-lift-obstruction
title: 3 mod 4 标准源解不能保留任意两项提升到核心素数
statement: 令 p=1 mod24 为素数，3<=n<p 且 n=3 mod4。标准解 4/n=1/((n+1)/4)+2/(n(n+1)/2) 不存在保留其中任意两个分母、只替换另一分母而得到 4/p 的整数解。
claim_status: established
topics:
- descent
- lifting-obstruction
- unit-fractions
- proof-program
sources:
- paper: elsholtz_tao2013
  locator: "Section 2"
  role: equation-and-parameterization-context
visibility: public
last_checked: '2026-07-23'
---

# \(3\pmod4\) 标准源解不能保留任意两项提升到核心素数

## 定理

令 \(p\equiv1\pmod{24}\) 是素数，且

\[
3\le n<p,\qquad n\equiv3\pmod4.
\]

记

\[
a=\frac{n+1}{4},\qquad b=\frac{n(n+1)}2.
\]

则

\[
\frac4n=\frac1a+\frac1b+\frac1b,
\]

但不存在正整数 \(a'\) 或 \(b'\)，使

\[
\frac4p=\frac1{a'}+\frac1b+\frac1b. \tag{1}
\]

或

\[
\frac4p=\frac1a+\frac1{b'}+\frac1b. \tag{2}
\]

换言之，从这条无条件标准源解出发，保留任意两个分母的单项替换都不能形成严格递降提升。

## 证明

### 替换小分母 \(a\)

若 (1) 成立，直接消去两个 \(1/b\) 项，或应用
`two-denominator-lift-criterion`，都给出唯一可能的替换值

\[
a'=\frac{npa}{np-4(p-n)a}
=\frac{p n(n+1)}{4D},
\qquad D=n(n+1)-p. \tag{3}
\]

若 \(D\le0\)，右式不为正，矛盾。于是设 \(D>0\)。由于 \(n\equiv3\pmod4\)，
\(S=n(n+1)\) 被 \(4\) 整除，故 \(D=S-p\) 是奇数。

又 \(n<p\)，且 \(n=p-1\) 与 \(n\equiv3\pmod4\) 不相容于
\(p\equiv1\pmod4\)，所以 \(p\nmid S\)。因此

\[
\gcd(D,S)=\gcd(S-p,S)=\gcd(p,S)=1,
\]

并且 \(\gcd(D,p)=1\)。结合 \(D\) 为奇数，得到

\[
\gcd\!\left(D,\frac{pS}{4}\right)=1.
\]

式 (2) 的整数性强制 \(D\mid pS/4\)，从而 \(D=1\)。但此时

\[
p=S-1\equiv-1\equiv3\pmod4,
\]

与 \(p\equiv1\pmod4\) 矛盾。

### 替换一个重复大分母 \(b\)

令 \(r=p-n\)。由 \(p\equiv1\pmod4\)、\(n\equiv3\pmod4\)，有
\(r\equiv2\pmod4\)，特别地 \(r\ge2\)。若 (2) 成立，则一项替换公式的分母为

\[
np-4rb
=n\bigl(p-2r(n+1)\bigr). \tag{4}
\]

但 \(n=p-r\)，且

\[
r(n+1)-2(p-1)=(r-2)n\ge0.
\]

所以 \(2r(n+1)\ge4(p-1)>p\)，使 (4) 严格为负。由一项替换的正性必要条件，
\(b'\) 不可能为正整数。这覆盖了两个相同的 \(b\) 坐标，故定理得证。

## 含义

`even-predecessor-two-denominator-lift-obstruction` 已排除所有偶数 \(n\) 的标准源解。
本定理再完整排除所有 \(n\equiv3\pmod4\) 的标准源解。故想用一个无条件可解的较小
分母实例进行二分母保留提升时，不能只依赖这些最基本的经典解；必须使用非标准源解、
保留至多一个分母，或同时重组全部三项。
