---
kind: claim
claim_id: type-I-b1-square-essential-same-gap-nonoverlap-ray
title: B等于一平方本质p减一桥避开同缺口Type II的无穷射线
statement: 存在无穷多个核心素数，每个都具有一个B=1的p减一Type I终端桥，其桥条件只由r|t^2而非r|t成立，故该正规形不能回缩为完整外源；同时同一缺口不存在普通Type II双尾证书。具体地，进程p=17040z+3673中的每个素数项具有此性质。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- type-II
- b1
- p-minus-one
- square-divisibility
- external-source
- same-gap
- dirichlet
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-and-Type-II-certificate-context
visibility: public
last_checked: '2026-07-28'
---

# \(B=1\) 平方本质 \(p-1\) 桥避开同缺口 Type II 的无穷射线

对每个非负整数 \(z\)，定义

\[
\begin{aligned}
q&=5, &m&=4q-1=19,\\
r&=4, &R&=4r-1=15,\\
C&=mr-q=71, &A&=60z+13,\\
p&=4AC-m=17040z+3673.
\end{aligned}
\tag{1}
\]

## 定理

进程 (1) 是原始且恒为 \(1\pmod {24}\) 的等差进程。因而由 Dirichlet 定理，其中有
无穷多个素数 \(p\)。对每个这样的素数：

\[
\begin{aligned}
& (A,1,C) \text{ 是缺口 }m=19\text{ 的 Type I 正规形；}\\
& \text{源 }n=p-1\text{、桥因子 }E=R+1=16\text{ 给出偶终端桥；}\\
& E\nmid p-1,\quad r\nmid K,
\quad\text{故该正规形不回缩为完整平方因子外源；}\\
& q\nmid Ar,\quad\text{故同一缺口没有普通 Type II 双尾证书。}
\end{aligned}
\tag{2}
\]

所以“把每个 \(B=1\) 的 \(p-1\) 桥线性化为外源，或由同缺口普通 Type II 取代”的策略
不能成为全称混合终端选择引理的证明。

## 证明

由 (1)，

\[
p=17040z+3673\equiv1\pmod {24},
\qquad
\gcd(17040,3673)=1.
\tag{3}
\]

Dirichlet 的算术级数素数定理给出无穷多个素数项。又

\[
mR=19\cdot15=4\cdot71+1,
\tag{4}
\]

所以 \((A,1,C)\) 确实是 \(B=1\) 正规形；令

\[
H=AR-1,\qquad K=CH.
\tag{5}
\]

对 \(p-1\) 桥，写 \(t=(p-1)/4\)。这里

\[
t=4260z+918=2(2130z+459),
\tag{6}
\]

括号内恒为奇数。因此

\[
r=4\mid t^2,\qquad r\nmid t.
\tag{7}
\]

[p减一桥判据](type-I-normal-pminusone-upper-half-bridge.md) 由前一项给出桥因子
\(E=4r=16\)；而 [外源回缩判据](type-I-b1-external-source-retraction-criterion.md)
把后一项等价为 \(r\nmid K\)，也等价为 \(E\nmid p-1\)。故该桥是平方本质的，不是
同一正规形的外源回缩。

最后，

\[
Ar=4(60z+13)\equiv2\pmod5.
\tag{8}
\]

故 \(q=5\nmid Ar\)。由
[B等于一同缺口二分](type-I-b1-pminusone-same-gap-dichotomy.md)，这正是该缺口没有
普通 Type II 双尾证书的充要条件。

## 显式素数样本

该射线的前几个素数项为

\[
3673,\quad88873,\quad105913,\quad122953.
\]

它们仅用于回归测试；无穷性来自 (3) 与 Dirichlet 定理，不依赖有限样本。

## 范围

本定理不排除这些素数在**其他缺口**有普通 Type II 证书，也不排除另一张 Type I
正规形可回缩为外源。因此它不是 Erdős--Straus 猜想或原混合选择引理的反例。它只排除
两种过窄的证明归约：固定正规形内的线性外源化，以及把该桥替换成同缺口普通 Type II。
