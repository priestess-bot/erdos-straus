---
kind: claim
claim_id: even-standard-two-tail-descent
title: 偶数标准源保留一项并重组两尾的完整递降族
statement: 令 p=1 mod24 为素数且 p/2<n<p 为偶数。写 R=4n-p、S=np。标准源解 4/n=1/(n/2)+2/n 可通过保留一个分母 n、重组另两项提升为 4/p=1/n+1/u+1/v，当且仅当存在 e|S^2、e<=S，使 R 整除 S+e；互素性自动给出互补因子的同余。此时 u=(S+e)/R、v=(S+S^2/e)/R。固定 p,n 并按 u<=v 排序时，该因子条件穷尽所有这样的提升。若 min(n,u,v) 位于自然首分母范围，则显式恢复 Type I/II 除子证书。
claim_status: established
topics:
- descent
- certificate
- egyptian-fractions
- divisor-parametrization
- even-source
- solution-lift
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1--4"
  role: divisor-certificate-and-lift-context
visibility: public
last_checked: '2026-07-24'
---

# 偶数标准源保留一项并重组两尾的完整递降族

## 定理

令 \(p\equiv1\pmod {24}\) 为素数，且

\[
\frac p2<n<p,\qquad 2\mid n. \tag{1}
\]

定义

\[
R=4n-p,\qquad S=np. \tag{2}
\]

则下列两项等价：

1. 存在正整数 \(u\le v\)，使
   \[
   \frac4p=\frac1n+\frac1u+\frac1v; \tag{3}
   \]
2. 存在正除子 \(e\mid S^2\)、\(e\le S\)，满足
   \[
   R\mid S+e. \tag{4}
   \]

在此情形

\[
u=\frac{S+e}{R},\qquad v=\frac{S+S^2/e}{R}, \tag{5}
\]

并有严格提升

\[
\frac4n=\frac1{n/2}+\frac1n+\frac1n
\quad\Longrightarrow\quad
\frac4p=\frac1n+\frac1u+\frac1v. \tag{6}
\]

令 \(x=\min(n,u,v)\)。若

\[
\frac p4<x\le\frac p2, \tag{7}
\]

则 \(m=4x-p\) 满足 \(3\le m\le p-2\)，并可从右式恢复一张 Type I 或 Type II
除子证书。固定 \((p,n)\)，(4) 因而穷尽了所有从该标准偶数源保留一个 \(n\)、同时重组
另两个分母的自然证书提升。

## 证明

标准偶数恒等式给出 (6) 的左边。保留其中一个 \(1/n\) 后，(3) 余下的条件为

\[
\frac1u+\frac1v=\frac4p-\frac1n=\frac{4n-p}{np}=\frac RS. \tag{8}
\]

将其清分母并配方：

\[
(Ru-S)(Rv-S)=S^2. \tag{9}
\]

若 \(u\le v\)，令 \(e=Ru-S\)。正性、(9) 及排序分别给出

\[
e\mid S^2,\qquad e\le S,
\]

由于 \(n<p\) 且 \(p\) 为奇素数，
\[
\gcd(R,S)=\gcd(4n-p,np)=1.
\]
故一分母提升判据的互素推论表明，\(R\mid S+e\) 已自动蕴含
\(R\mid S+S^2/e\)。因此 \((u,v)\) 为整数恰好给出单条件 (4)；反解即为 (5)。
反向代入 (9) 后得到 (8)，再加
(1/n) 即为 (3)，从而 (6) 成立。由于 (n<p)，源秩严格较小。

条件 (7) 使目标有一个自然首分母 \(x\)。又 \(p\equiv1\pmod4\)、\(x\) 为整数，故

\[
m=4x-p\equiv3\pmod4.
\]

short-certificate-equivalence 遂将右端目标解转换为该缺口的 Type I/II 除子证书。

## 强短界的边界

这条机制的证书虽在自然范围内，但不可能满足 \(m\le p/3\)。事实上，若 (3) 的
最小分母就是 \(n\)，则由 (1) 有 \(n>p/2\)。否则令最小分母为 \(x<n\)；目标中仍有
保留的 \(n<p\) 和第三个正单位分数，故

\[
\frac4p>\frac1x+\frac1n>\frac1x+\frac1p,
\]

从而 (x>p/3)。两种情形均给出

\[
m=4x-p>\frac p3. \tag{10}
\]

因此它可提供严格递降边和自然 Type I/II 证书，却不能单独证明诸如
\(m\le p/3\) 的强“短缺口”版本。这一限制来自保留的目标分母 \(n>p/2\)，而不是
对一般重组提升的否定。

## 两个此前残余的严格边

该构造绕过 even-predecessor-two-denominator-lift-obstruction：后者只排除保留**两个**
标准源分母并替换一个分母；这里恰好保留一个 \(n\)，并重组 \(n/2\) 与另一个 \(n\)。

\[
\begin{aligned}
\frac4{12198}
 &=\frac1{6099}+\frac1{12198}+\frac1{12198}
 &&\Longrightarrow&
\frac4{21169}
 &=\frac1{12198}+\frac1{9348}+\frac1{7057998628},\\
\frac4{27764}
 &=\frac1{13882}+\frac1{27764}+\frac1{27764}
 &&\Longrightarrow&
\frac4{48409}
 &=\frac1{27764}+\frac1{21454}+\frac1{22848467092}.
\end{aligned} \tag{11}
\]

相应因子分别为

\[
(p,n,e)=(21169,12198,342),\qquad(48409,27764,1262). \tag{12}
\]

在这两个例子中，最小目标分母分别为 (9348,21454)，并直接给出 Type I 证书

\[
(m,d)=(16223,342),\qquad(37407,1262). \tag{13}
\]

前一组与后一组都属于平移/固定 \(M\) 平方因子族留下的有限残余；这里给出的是新的
“一项保留、两项重组”标记递降边。

## 边界

这个定理完整分类的是**固定 \((p,n)\)** 的该种提升，不是对每个核心素数选择一组
\((n,e)\) 的定理。事实上，条件 (4) 仍然是关于 \(S^2=p^2n^2\) 的因子存在问题；证明
它总可解将给出一个新的全局证书选择器。故该构造扩展了递降图，却不构成
Erdos--Straus 猜想或目标全称引理的证明。
