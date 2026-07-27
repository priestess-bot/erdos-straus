---
kind: claim
claim_id: three-mod-four-nonstandard-source-lift-obstruction
title: 3 mod 4 非标准平方尾源解也不能作单项提升
statement: 设 p=1 mod24 为素数、3<=n<p 且 n=3 mod4。对非标准源解 4/n=1/a+1/b+1/c，其中 a=(n+1)/4、b=(n+1)^2/4、c=nb，不存在保留任意两个源分母、只替换第三个分母而得到 4/p 的正整数提升。
claim_status: established
topics:
- descent
- lifting-obstruction
- nonstandard-source
- unit-fractions
- proof-program
sources:
- paper: subramanian2026
  locator: "Equation (2.9)"
  role: nonstandard-source-identity
- paper: elsholtz_tao2013
  locator: "Section 2"
  role: equation-and-parameterization-context
visibility: public
last_checked: '2026-07-24'
---

# \(3\pmod4\) 非标准平方尾源解也不能作单项提升

## 定理

设

\[
p\equiv1\pmod{24},\qquad 3\le n<p,\qquad n\equiv3\pmod4.
\]

令

\[
a=\frac{n+1}{4},\qquad b=\frac{(n+1)^2}{4},\qquad c=nb. \tag{1}
\]

则

\[
\frac4n=\frac1a+\frac1b+\frac1c, \tag{2}
\]

但不能保留其中任意两个分母、只替换剩余一个分母而得到 \(4/p\) 的正整数解。

## 证明

先由 (1) 直接计算

\[
\frac1a+\frac1b+\frac1c
=\frac4{n+1}+\frac4{(n+1)^2}+\frac4{n(n+1)^2}
=\frac4n,
\]

故 (2) 是有效源解。

设 \(r=p-n>0\)。two-denominator-lift-criterion 表明，替换源分母 \(w\) 的必要且
充分条件包含

\[
D_w=np-4rw>0,\qquad D_w\mid npw. \tag{3}
\]

### 替换 \(b\) 或 \(c\)

对 \(b\)，由 (1) 有

\[
D_b=np-r(n+1)^2
=n^2-r(n^2+n+1)<0. \tag{4}
\]

对 \(c\)，有

\[
D_c=np-rn(n+1)^2
=n\bigl(n-r(n^2+2n)\bigr)<0. \tag{5}
\]

两式都与 (3) 的正性矛盾。

### 替换 \(a\)

此时

\[
D_a=np-r(n+1)=n(n+1)-p. \tag{6}
\]

若 \(D_a\le0\)，仍与 (3) 矛盾。故设 \(D_a>0\)。由于 \(n(n+1)\) 被 \(4\) 整除、
\(p\equiv1\pmod4\)，\(D_a\) 是奇数。又 \(p>n+1\)（两者皆为奇数），所以

\[
\gcd(D_a,n)=\gcd(D_a,n+1)=\gcd(D_a,p)=1. \tag{7}
\]

由 (3) 和 \(a=(n+1)/4\)，以及 \(D_a\) 为奇数，得到

\[
D_a\mid\frac{np(n+1)}4.
\]

结合 (7)，只可能 \(D_a=1\)。这迫使

\[
p=n(n+1)-1\equiv3\pmod4,
\]

与 \(p\equiv1\pmod4\) 矛盾。三种替换均不可能，定理得证。

## 含义

three-mod-four-standard-source-lift-obstruction 只排除了经典重复尾
\((a,n(n+1)/2,n(n+1)/2)\)。本定理处理来自 Subramanian 2026 的不同平方尾
\((a,b,nb)\)，因此不能把“尝试另一个已知 \(3\pmod4\) 恒等式”当作二分母保留递降的
遗漏空间。它不排除一分母保留、非线性耦合，或带因子标记的提升。
