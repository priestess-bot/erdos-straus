---
kind: claim
claim_id: even-predecessor-two-denominator-lift-obstruction
title: 邻近偶数源的标准解不能保留两个分母提升
statement: 设 p=1 mod24 为素数，r 为满足 1<=r<=p-2 的奇数，n=p-r。偶数 n 的标准解 4/n=1/(n/2)+1/n+1/n 不存在保留其中任意两个分母、只替换第三项而得到 4/p 的正整数解的提升。
claim_status: established
topics:
- descent
- obstruction
- egyptian-fractions
- solution-lift
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1--4"
  role: divisor-and-solution-context
visibility: public
last_checked: '2026-07-23'
---

# 邻近偶数源的标准解不能保留两个分母提升

## 定理

设 \(p\equiv1\pmod{24}\) 为素数，令 \(r\) 是满足

\[
1\le r\le p-2,\qquad r\equiv1\pmod2
\]

的整数，并设 \(n=p-r\)。于是 \(n\) 为正偶数，且有标准源解

\[
\frac4n=\frac1{n/2}+\frac1n+\frac1n. \tag{1}
\]

从 (1) 中保留任意两个分母、只替换第三个分母，不可能得到 \(4/p\) 的正整数解。

## 证明

一般的一项替换公式给出：若替换源分母 \(a\)，则目标分母必须是

\[
a'=\frac{npa}{np-4(p-n)a}. \tag{2}
\]

分母为正是必要条件。标准三元组中只有 \(a=n/2\) 和 \(a=n\) 两种情形。

### 替换 \(n/2\)

令

\[
q=p-2r.
\]

若 \(q\le0\)，(2) 的分母不正。若 \(q>0\)，由 (2) 得

\[
a'=\frac{np}{2q}.
\]

整数性迫使 \(q\mid n\)，因为 \(q<p\) 且 \(\gcd(q,p)=1\)。又

\[
n=p-r=q+r,
\]

故 \(q\mid r\)，进而 \(q\mid p=q+2r\)。由 \(p\) 的素性和 \(0<q<p\)，
只能有 \(q=1\)。于是

\[
r=\frac{p-1}{2}=12t
\quad\text{当 }p=24t+1,
\]

这与 \(r\) 为奇数矛盾。

### 替换 \(n\)

令

\[
q=p-4r.
\]

同样地，\(q\le0\) 时 (2) 不可能；当 \(q>0\) 时，

\[
a'=\frac{np}{q}.
\]

整数性迫使 \(q\mid n\)。而

\[
n=p-r=q+3r,
\]

所以 \(q\mid3r\)。这给出

\[
q\mid3p=3q+12r.
\]

因 \(0<q<p\) 且 \(p>3\) 是素数，故 \(q\in\{1,3\}\)。若 \(q=1\)，则

\[
r=\frac{p-1}{4}=6t
\]

为偶数；若 \(q=3\)，则 \(p=4r+3\equiv3\pmod4\)。两种情形都与假设矛盾。

两个 \(n\) 坐标相同，故这覆盖了全部三种替换选择，定理得证。

## 对递降的含义

每个奇数目标 \(p\) 都有任意多个较小偶数邻居 \(n=p-r\)，而偶数 \(n\) 的 (1) 是无需
猜想的显式源解。本定理排除整条最直接的递降路线：不能希望固定或可变的邻近偶数距离
\(r\) 加上这个标准源解，并仅改动一个分母就解决所有核心素数。

这不排除保留一个分母并重组另外两项，或在 \(n\) 选取不同的源解；它也不排除一般的
带标记递降。它只精确排除了这一个原本会给出无条件源解的简单家族。
