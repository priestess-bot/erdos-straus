---
kind: claim
claim_id: three-divisible-standard-two-tail-descent
title: 三倍数标准源保留大尾并重组两项的完整递降族
statement: 令 p=1 mod24 为素数，p/2<n<p 且 3|n。写 R=8n-p、S=2np。标准源解 4/n=1/(n/3)+2/(2n) 可通过保留一个分母 2n、重组另两项提升为 4/p=1/(2n)+1/u+1/v，当且仅当存在 e|S^2、e<=S，使 R 整除 S+e；互素性自动给出互补因子的同余。此时 u=(S+e)/R、v=(S+S^2/e)/R。固定 p,n 并按 u<=v 排序时，该条件穷尽所有这样的提升；若目标首分母在自然范围，则恢复 Type I/II 除子证书。
claim_status: established
topics:
- descent
- certificate
- egyptian-fractions
- divisor-parametrization
- three-divisible-source
- solution-lift
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

# 三倍数标准源保留大尾并重组两项的完整递降族

## 定理

令 \(p\equiv1\pmod {24}\) 为素数，并设

\[
\frac p2<n<p,\qquad3\mid n. \tag{1}
\]

定义

\[
R=8n-p,\qquad S=2np. \tag{2}
\]

则下列两项等价：

1. 存在正整数 \(u\le v\)，使
   \[
   \frac4p=\frac1{2n}+\frac1u+\frac1v; \tag{3}
   \]
2. 存在正除子 \(e\mid S^2\)、\(e\le S\)，满足
   \[
   R\mid S+e. \tag{4}
   \]

此时

\[
u=\frac{S+e}{R},\qquad v=\frac{S+S^2/e}{R}, \tag{5}
\]

且有严格提升

\[
\frac4n=\frac1{n/3}+\frac1{2n}+\frac1{2n}
\quad\Longrightarrow\quad
\frac4p=\frac1{2n}+\frac1u+\frac1v. \tag{6}
\]

令 \(x=\min(2n,u,v)\)。若

\[
\frac p4<x\le\frac p2, \tag{7}
\]

则 \(m=4x-p\) 位于 \(3\le m\le p-2\)，并可从目标解恢复 Type I 或 Type II
除子证书。固定 \((p,n)\)，(4) 穷尽了该标准源中保留一个 \(2n\)、同时重组另两项的
所有自然证书提升。

## 证明

标准三倍数恒等式给出 (6) 左边。保留其中一个 \(1/(2n)\) 后，目标剩余项满足

\[
\frac1u+\frac1v=\frac4p-\frac1{2n}=\frac{8n-p}{2np}=\frac RS. \tag{8}
\]

清分母并配方得到

\[
(Ru-S)(Rv-S)=S^2. \tag{9}
\]

令 \(e=Ru-S\)。若 \(u\le v\)，正性、(9) 和排序分别给出 \(e\mid S^2\)、
\(e\le S\)。又因 \(n<p\)、\(p\) 为奇素数且 \(R=8n-p\) 为奇数，
\[
\gcd(R,S)=\gcd(8n-p,2np)=1.
\]
所以一分母提升判据的互素推论把两个因子同余化简为单条件 (4)；反解就是 (5)。
反向代入 (9) 即恢复
(8) 与 (3)，从而得到 (6)。由于 (n<p)，源秩严格下降。

在 (7) 下，\(x\) 是目标首分母，且 \(m=4x-p\equiv3\pmod4\)。
short-certificate-equivalence 因而给出所述 Type I/II 证书。

## 与两项保留障碍的差别

three-divisible-standard-source-lift-obstruction 排除的是从

\[
\left(\frac n3,2n,2n\right)
\]

保留**两个**分母、只替换第三项的提升。这里仅保留一个 \(2n\)，同时重组
\(n/3\) 与另一个 \(2n\)，所以不与该障碍冲突。

与 even-standard-two-tail-descent 也有实质差异：由 (1) 保留的 \(2n>p\)，
故不产生后者“缺口必大于 \(p/3\)”的论证。实际可有自然范围内的较短缺口。

## 严格例子

取

\[
p=8329,\qquad n=4620,\qquad e=168.
\]

则

\[
\frac4{4620}
=\frac1{1540}+\frac1{9240}+\frac1{9240}
\quad\Longrightarrow\quad
\frac4{8329}
=\frac1{9240}+\frac1{2688}+\frac1{1231359360}. \tag{10}
\]

目标首分母 \(2688\) 给出 Type I 证书

\[
(m,d)=(2423,168). \tag{11}
\]

并且

\[
3m=7269<8329=p, \tag{12}
\]

所以这一机制确实可以落入 \(m<p/3\) 的区域；这只是一个可核验实例，不是统一
短界的证明。

## 边界

该定理完整分类的是固定 \((p,n)\) 的一类标记提升。它尚未构造每个核心素数所需的
\((n,e)\)，因而不能闭合“短证书或递降”状态图。其价值在于增加了一个使用无条件标准源、
且不受偶数大尾 \(p/3\) 边界限制的可搜索分支。

这里的 \(p/2<n<p\) 不是任意截断。`three-divisible-tail-window-localization` 证明：
若把同一保留 \(2n\) 的构造下探到 \(p/4<n<p/2\)，它与偶数源 \(2n\) 的大尾提升逐因子
完全相同；若 \(p/8<n<p/4\)，则又只是首分母 \(2n\) 的直接证书。因此本卡片保留的
区间正是相对于这两类已有机制的非冗余窗口。
