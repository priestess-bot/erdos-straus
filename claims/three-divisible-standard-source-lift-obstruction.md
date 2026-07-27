---
kind: claim
claim_id: three-divisible-standard-source-lift-obstruction
title: 3 的倍数标准源解不能保留两项提升到核心素数
statement: 令 p=1 mod24 为素数，3<=n<p 且 3|n。标准解 4/n=1/(n/3)+2/(2n) 不存在保留任意两个分母、只替换第三项而得到 4/p 的整数解。
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

# \(3\mid n\) 标准源解不能保留两项提升到核心素数

## 定理

令 \(p\equiv1\pmod{24}\) 为素数，\(3\le n<p\)、\(3\mid n\)。标准恒等式为

\[
\frac4n=\frac1{n/3}+\frac1{2n}+\frac1{2n}. \tag{1}
\]

不存在从 (1) 保留任意两个分母、只替换另一分母而得到 \(4/p\) 解的正整数提升。

## 证明

只须考察两个不同的被替换坐标。

### 替换 \(n/3\)

由 `two-denominator-lift-criterion`，唯一候选为

\[
a'=\frac{pn}{4n-p}.
\]

正性要求 \(m=4n-p>0\)。又 \(n<p\)，故

\[
\gcd(m,n)=\gcd(p,n)=1.
\]

若 \(a'\) 为整数，则 \(m\mid pn\)，从而 \(m\mid p\)。素性给出 \(m=1\) 或
\(m=p\)。前者会令 \(4n=p+1\)，但 \(p+1\equiv2\pmod4\)；后者会令
\(n=p/2\)。两者皆不可能。

### 替换一个 \(2n\)

此时唯一候选为

\[
b'=\frac{2pn}{8n-7p}.
\]

令 \(D=8n-7p\)。正性下 \(0<D<p\)，且 \(D\) 是奇数。整数性给出
\(D\mid2pn\)。由于 \(p\nmid D\)，先得 \(D\mid2n\)，再由
\(D=8n-7p\) 得 \(D\mid7p\)。故 \(D\mid7\)，即 \(D=1\) 或 \(D=7\)。

当 \(D=1\) 时，

\[
n=\frac{7p+1}{8}=21\frac{p-1}{24}+1\equiv1\pmod3,
\]

与 \(3\mid n\) 矛盾。当 \(D=7\) 时，\(8n=7(p+1)\)，但
\(p+1\equiv2\pmod8\)，也不可能。

两个坐标均不可能，定理成立。

## 含义

连同 `even-predecessor-two-denominator-lift-obstruction` 与
`three-mod-four-standard-source-lift-obstruction`，这表明用已知无条件标准解作源时，
最短的二分母保留提升已在偶数、\(3\pmod4\) 与 \(3\mid n\) 三个基本类中失败。
它不否定使用这些 \(n\) 的非标准源解，也不否定保留一个分母或重组全部三项的提升。
