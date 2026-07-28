---
kind: claim
claim_id: type-I-linear-quadratic-obstruction-reciprocity-pullback
title: 线性一般 B 二次障碍的互反拉回
statement: 对线性状态p=a+s+asR、奇素数q整除K=(pR+1)/4，若q整除标签块tR+1；对每个m整除R且m为3 mod 4的奇平方自由数，令c=R/m，则精确有Jacobi符号恒等式(q/m)=(p c/q)。因而二次角色在K的奇素因子上平凡的要求，等价拉回为这些素因子在二次域Q(sqrt(pR/m))中的分裂条件，另须单独检查q=2。七个完整压力谱逐项复核所有适用(q,t,m)关系。此恒等式不保证角色不存在，也不能处理需要高阶角色的障碍。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- subgroup-character
- quadratic-character
- quadratic-reciprocity
- finite-product
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 线性一般 B 二次障碍的互反拉回

## 定理

设

\[
p=a+s+asR,
\qquad s\equiv1\pmod2,
\qquad R\equiv3\pmod4,
\qquad K=\frac{pR+1}{4}. \tag{1}
\]

令 \(q\mid K\) 为奇素数，并选择 \(t\in\{a,s\}\) 使
\(q\mid tR+1\)。令 \(m\mid R\) 为满足 \(m\equiv3\pmod4\) 的奇平方自由数，置

\[
c=\frac{R}{m}. \tag{2}
\]

则 \(q\nmid pm\)，且有精确恒等式

\[
\boxed{
\left(\frac{q}{m}\right)
=\left(\frac{p(R/m)}{q}\right).
} \tag{3}
\]

左边是模 \(m\) 的二次角色在 \(q\) 上的值，右边是普通 Legendre 符号。故若
\(\chi_m=(\cdot/m)\) 在 \(K\) 的所有奇素因子上平凡，则它们全满足

\[
\left(\frac{p(R/m)}q\right)=1. \tag{4}
\]

反过来，(4) 确保 \(\chi_m\) 在所有**奇**素因子上平凡；当 \(2\mid K\) 时还须额外检查
\(\chi_m(2)=1\)。因此 (4) 是在二次域
\(\mathbb Q(\sqrt{pR/m})\) 中的实际素因子分裂条件，而不是不同模数单位群间的抽象比较。

特别地，若 \(R\) 本身是素数，取 \(m=R\)，则

\[
\boxed{\left(\frac qR\right)=\left(\frac pq\right)}
\qquad(q\mid K,\ q\text{ odd}). \tag{5}
\]

在这一情形，二次 G 型障碍要求每个奇 \(q\mid K\) 在
\(\mathbb Q(\sqrt p)\) 中分裂，并在 \(2\mid K\) 时还要求 \((2/R)=1\)。

## 证明

由 \(q\mid tR+1\)，有 \(tR\equiv-1\pmod q\)。这迫使 \(q\nmid tR\)，并且
\(q\nmid p\)，因为

\[
p-t=\begin{cases}
a(sR+1),&t=s,\\
s(aR+1),&t=a.
\end{cases}
\]

所以 \(p\equiv t\pmod q\)。代入 \(R=mc\) 得

\[
m\equiv-(tc)^{-1}\pmod q. \tag{6}
\]

因 \(m\equiv3\pmod4\)，二次互反律与 (6) 给出

\[
\begin{aligned}
\left(\frac qm\right)
&=\left(\frac{-1}{q}\right)\left(\frac mq\right)\\
&=\left(\frac{-1}{q}\right)
  \left(\frac{-(tc)^{-1}}q\right)\\
&=\left(\frac{tc}{q}\right)
=\left(\frac{pc}{q}\right),
\end{aligned}
\]

即为 (3)。

## 有限审计与范围

程序在七个完整压力谱的所有 490 个有向状态上，枚举 \(K\) 的每个奇素因子、它所整除的每个
标签块，以及 \(R\) 的每个 \(m\equiv3\pmod4\) 奇平方自由因子；每一条 (3) 都以独立 Jacobi
符号计算复核。结果只证明代数拉回恒等式及其有限重放，不说明这些 \(m\) 真的是分离角色。

该工具准确处理二次 G 型障碍，却无法单独处理有限指数障碍；并且既有完整谱中存在需要四阶
角色的少数障碍，所以二次互反路线不能独立完成全称选择器。下一步应把 (3) 与带模数标签块的
私有层比较、以及 \(\mathcal A_R(K)\) 的反足点积集增长相结合。

## 复现

~~~bash
python3 reproductions/type_i_linear_quadratic_obstruction_reciprocity_pullback.py
python3 -m unittest tests.test_type_i_linear_quadratic_obstruction_reciprocity_pullback -v
~~~
