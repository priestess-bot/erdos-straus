---
kind: claim
claim_id: even-split-source-descent
title: 偶数源非标准二项分裂的完整递降族
statement: 令 p=1 mod24 为素数且 p/2<n<p 为偶数。所有形如 4/n=1/(n/2)+1/a+1/b 的有序源解都由偶因子 e|n^2、e<=n、n^2/e 为偶数唯一给出：a=(n+e)/2、b=(n+n^2/e)/2。若其中 a 或 b 满足 Lambda=np-4(p-n)a>0、Lambda|npa，且替换值 a'=npa/Lambda>=n/2，则替换该项给出严格提升至 4/p；其首分母 n/2 处存在缺口 2n-p 的自然 Type I/II 证书。标准分裂 e=n 已被偶数邻源障碍排除，但非标准 e 可成功。
claim_status: established
topics:
- descent
- certificate
- type-I
- type-II
- egyptian-fractions
- factorization
- even-source
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1--4"
  role: divisor-certificate-and-lift-context
visibility: public
last_checked: '2026-07-24'
---

# 偶数源非标准二项分裂的完整递降族

## 定理

令 \(p\equiv1\pmod{24}\) 是素数，且

\[
\frac p2<n<p,\qquad 2\mid n. \tag{1}
\]

取一个满足

\[
e\mid n^2,\qquad e\le n,\qquad 2\mid e,\qquad
2\mid\frac{n^2}{e} \tag{2}
\]

的因子，并定义

\[
a=\frac{n+e}{2},\qquad
b=\frac{n+n^2/e}{2}. \tag{3}
\]

设 \(c\) 是 \(a,b\) 中任一个，并令

\[
\Lambda=np-4(p-n)c. \tag{4}
\]

若

\[
\Lambda>0,\qquad \Lambda\mid npc,\qquad
c'=\frac{npc}{\Lambda}\ge\frac n2, \tag{5}
\]

则

\[
\frac4n=\frac1{n/2}+\frac1a+\frac1b
\quad\Longrightarrow\quad
\frac4p=\frac1{n/2}+\frac1{a+b-c}+\frac1{c'} . \tag{6}
\]

这是一条严格提升边，且目标解的最小分母是 \(n/2\)。因此在缺口

\[
m=2n-p \tag{7}
\]

处存在一张自然范围的 Type I 或 Type II 除子证书。

反过来，固定偶数 \(n\)，每个按 \(a\le b\) 排序、包含 \(n/2\) 的源解都唯一由
(2)--(3) 的一个 \(e\) 给出。因此 (2) 穷尽了这种显式偶数源上的非标准二项分裂。

## 证明

由 (2)--(3)，

\[
\frac1a+\frac1b
=\frac{2}{n},
\]

所以左式是 \(4/n\)。式 (4)--(5) 正是
two-denominator-lift-criterion 的充要条件，故只替换 \(c\)、保留另两个分母后得到
(6)，并且 \(n<p\) 保证递降严格。

由 (3)，\(a,b\ge n/2\)；条件 (5) 给出 \(c'\ge n/2\)。所以目标三元组的最小分母
恰为 \(n/2\)。由 (1)，

\[
3\le2n-p\le p-2,\qquad 2n-p\equiv3\pmod4. \tag{8}
\]

short-certificate-equivalence 将这个以 \(n/2\) 为首分母的目标解转换为 (7) 处的
Type I 或 Type II 证书。

最后，若

\[
\frac2n=\frac1a+\frac1b,
\]

清分母得到

\[
(2a-n)(2b-n)=n^2. \tag{9}
\]

当 \(a\le b\) 时，令 \(e=2a-n\)。正性及 (9) 给出 \(e\mid n^2\)、\(e\le n\)；
两个分母是整数恰给出 (2) 的偶性条件，并恢复 (3)。反向代入也成立，故参数化完整。

## 非标准成功例

取

\[
p=5209,\qquad n=2680,\qquad e=80.
\]

则

\[
(a,b)=(1380,46230),\qquad
\Lambda=40,\qquad c'=481624140.
\]

于是

\[
\frac4{2680}
=\frac1{1340}+\frac1{1380}+\frac1{46230}
\quad\Longrightarrow\quad
\frac4{5209}
=\frac1{1340}+\frac1{46230}+\frac1{481624140}. \tag{10}
\]

目标首分母 \(1340\) 的缺口为 \(151\)，并恢复 Type I 证书

\[
(m,D)=(151,670). \tag{11}
\]

因子 \(e=n\) 时 (3) 退化为标准偶数源
\((n/2,n,n)\)。even-predecessor-two-denominator-lift-obstruction 说明该标准点永远
不能成功；(10) 显示这种障碍不延伸到完整的因子分裂族。

## 边界

该定理已经穷尽“源中保留 \(n/2\)”的偶数分裂，但仍要为每个 \(p\) 选择一个满足 (1)、
(2)、(5) 的 \(n,e,c\)。例 (10) 是一个严格的局部新边，而非此选择器存在的证明。
它也不覆盖不含 \(n/2\) 的偶数源解，或一般非缩放的一坐标提升。
