---
kind: claim
claim_id: residual-split-source-descent
title: 固定 n/r 的完整残余分裂与短证书提升
statement: 令 r 属于 {1,2,3}、r 整除 n、s=4-r。所有形如 4/n=1/(n/r)+1/a+1/b 的有序源解，恰由 e|n^2、e<=n、e 和 n^2/e 均同余 -n mod s 给出：a=(n+e)/s，b=(n+n^2/e)/s。对核心素数 p，若 n<p、x=n/r 位于自然首分母范围，且替换一个尾分母 c 的 Lambda=np-4(p-n)c 为正且整除 npc，所恢复的 c'=npc/Lambda 与另一尾分母均不小于 x，则得到严格提升至 4/p，并在缺口 m=4x-p 处恢复 Type I/II 除子证书。
claim_status: established
topics:
- descent
- certificate
- egyptian-fractions
- divisor-parametrization
- type-I
- type-II
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1--4"
  role: divisor-certificate-and-lift-context
visibility: public
last_checked: '2026-07-24'
---

# 固定 \(n/r\) 的完整残余分裂与短证书提升

## 定理

令

\[
r\in\{1,2,3\},\qquad r\mid n,\qquad s=4-r. \tag{1}
\]

所有按 \(a\le b\) 排列、并含有指定分母 \(n/r\) 的源解

\[
\frac4n=\frac1{n/r}+\frac1a+\frac1b \tag{2}
\]

与下列因子数据一一对应：

\[
e\mid n^2,\qquad e\le n,\qquad
e\equiv\frac{n^2}{e}\equiv-n\pmod s, \tag{3}
\]

其中

\[
a=\frac{n+e}{s},\qquad b=\frac{n+n^2/e}{s}. \tag{4}
\]

进一步令 \(p\equiv1\pmod {24}\) 为素数，\(n<p\)，并设

\[
x=\frac nr,\qquad m=4x-p. \tag{5}
\]

若

\[
3\le m\le p-2, \tag{6}
\]

并且对 \(c\in\{a,b\}\) 及另一个尾分母 \(h=a+b-c\)，有

\[
\Lambda=np-4(p-n)c>0,\qquad
\Lambda\mid npc,\qquad
h\ge x,\qquad c'=\frac{npc}{\Lambda}\ge x, \tag{7}
\]

则

\[
\frac4n=\frac1x+\frac1h+\frac1c
\quad\Longrightarrow\quad
\frac4p=\frac1x+\frac1h+\frac1{c'} . \tag{8}
\]

这是严格的源降阶边；目标解的首分母为 \(x\)。所以在缺口 \(m\) 存在一张
Type I 或 Type II 除子证书。

## 证明

从 (2) 移项得到

\[
\frac1a+\frac1b=\frac{s}{n}.
\]

清分母并配方，得到

\[
(sa-n)(sb-n)=n^2. \tag{9}
\]

令 \(e=sa-n\)。在 \(a\le b\) 时，正性和 (9) 给出 \(e\mid n^2\)、
\(e\le n\)。两个分母为整数当且仅当 (3) 的两个同余均成立，且 (4) 恢复
\(a,b\)。反向代入 (4) 即恢复 (2)，故参数化完整。

对 (8)，固定 \(x,h\)，仅将 \(c\) 替换为 \(c'\)。
two-denominator-lift-criterion 给出其充要条件恰为 (7)，且替换值为

\[
c'=\frac{npc}{np-4(p-n)c}.
\]

由 \(n<p\)，边严格降到较小源实例。条件 (7) 说明目标三个分母均不小于 \(x\)，
故 \(x\) 是其首分母。条件 (6) 等价于

\[
x=\frac{p+m}{4},\qquad 3\le m\le p-2,\qquad m\equiv3\pmod4.
\]

short-certificate-equivalence 遂将该有序目标解等价地转为缺口 \(m\) 的 Type I/II
除子证书。

## 三个切片

这个参数化把三个此前分开出现的残余统一起来：

| \(r\) | 指定分母 | 残余 | 分裂式 |
| --- | --- | --- | --- |
| 1 | \(n\) | \(3/n\) | \((3a-n)(3b-n)=n^2\) |
| 2 | \(n/2\) | \(2/n\) | \((2a-n)(2b-n)=n^2\) |
| 3 | \(n/3\) | \(1/n\) | \((a-n)(b-n)=n^2\) |

其中 \(r=2\) 正是 even-split-source-descent 的完整因子分裂；该卡片补充
\(r=1,3\) 并统一了提升和证书恢复的条件。

三个严格可核验的例子分别为：

\[
\begin{aligned}
\frac4{304}&=\frac1{304}+\frac1{104}+\frac1{3952}
 &&\Longrightarrow&
\frac4{1129}&=\frac1{304}+\frac1{3952}+\frac1{2230904},\\
\frac4{2680}&=\frac1{1340}+\frac1{1380}+\frac1{46230}
 &&\Longrightarrow&
\frac4{5209}&=\frac1{1340}+\frac1{46230}+\frac1{481624140},\\
\frac4{60}&=\frac1{20}+\frac1{84}+\frac1{210}
 &&\Longrightarrow&
\frac4{73}&=\frac1{20}+\frac1{210}+\frac1{30660}.
\end{aligned} \tag{10}
\]

它们依次使用 \(r=1,2,3\)，并在缺口 \(87,151,7\) 处恢复证书。

## 边界

这是一族完整的**固定指定分母**源解及其可判定提升，不是对每个核心素数都能选择
\((n,r,e,c)\) 的定理。特别是，短证书或递降在自然范围内与 Erdos--Straus
猜想等价，见 short-certificate-descent-completeness-boundary；因此 (3)--(7) 不能被
误读为全局证明。它提供的是可递归搜索的标记边和新的显式证书族。
