---
kind: claim
claim_id: gap-three-two-denominator-lift-obstruction
title: 缺口 m=3 递降的二分母保留障碍
statement: 令 p=24t+1 为素数且 n=(p+3)/4=6t+1。若 (a,b,c) 是 4/n 的正整数解，则不存在正整数 a' 使 (a',b,c) 是 4/p 的解；经置换后，对任意保留源解两个分母的提升亦成立。
claim_status: established
topics:
- descent
- obstruction
- gap-three
- egyptian-fractions
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1--3"
  role: first-denominator-and-certificate-framework
- paper: bright_loughran2020
  locator: "equation (1.2)"
  role: cleared-denominator-surface-equation
visibility: public
last_checked: '2026-07-23'
---

# 缺口 m=3 递降的二分母保留障碍

## 定理

令 \(p=24t+1\) 是素数，\(t\ge1\)，并令

\[
n=\frac{p+3}{4}=6t+1.
\]

设

\[
\frac4n=\frac1a+\frac1b+\frac1c
\]

是任意正整数解。不存在正整数 \(a'\) 使

\[
\frac4p=\frac1{a'}+\frac1b+\frac1c.
\]

由于方程对三个分母对称，这排除了所有“保留源解的任意两个分母、只替换第三个”
的提升规则。

## 证明

若这样的 \(a'\) 存在，则两式相减给出

\[
\frac1{a'}
=\frac1a+\frac4p-\frac4n
=\frac1a-\frac{12(n-1)}{np}.
\]

记

\[
D=np-12(n-1)a.
\]

正性和整数性分别要求 \(D>0\) 与

\[
a'=\frac{npa}{D}\in\mathbb N.
\]

由 \(D>0\) 得

\[
a<\frac{np}{12(n-1)}
=2t+\frac5{12}+\frac1{72t}<2t+1.
\]

因此可写 \(a=2t-r\)，其中 \(0\le r\le2t-1\)。于是

\[
D=(72r+30)t+1.
\]

首先证明 \(D\) 与 \(p\) 互素。直接计算有

\[
24D-(72r+30)p=-6(12r+1).
\]

若 \(p\mid D\)，则 \(p\mid6(12r+1)\)。但 \(p>3\)，且

\[
0<12r+1\le24t-11<p=24t+1,
\]

矛盾。因此 \(\gcd(D,p)=1\)。整数性于是迫使 \(D\mid na\)。

令 \(g=\gcd(D,n)\)。又

\[
D=(12r+5)n-(12r+4),
\]

故 \(g\mid12r+4=4(3r+1)\)。\(D,n\) 都是奇数，所以 \(g\mid3r+1\)，
从而 \(g\le3r+1\)。由 \(D\mid na\) 和 \(\gcd(D/g,n/g)=1\)，得到

\[
\frac Dg\mid a.
\]

然而

\[
\begin{aligned}
D-(3r+1)a
&=(72r+30)t+1-(3r+1)(2t-r)\\
&=66rt+28t+3r^2+r+1>0.
\end{aligned}
\]

所以 \(D/g\ge D/(3r+1)>a\)，不可能整除正整数 \(a\)。矛盾，定理得证。

## 对递降计划的含义

缺口 \(m=3\) 自然提出较小分母 \(n=(p+3)/4\)。本定理说明，即使已知
\(\operatorname{Sol}(n)\)，也不能通过保留其中两个分母来构造
\(\operatorname{Sol}(p)\)。这比“共同缩放无效”更强，但仍只排除一类特定映射：
它不排除同时改变两个或三个分母的非线性提升，也不否定 \(m=3\) 的直接除子证书。
