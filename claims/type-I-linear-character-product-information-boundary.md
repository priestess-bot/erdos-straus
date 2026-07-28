---
kind: claim
claim_id: type-I-linear-character-product-information-boundary
title: 线性 Type I 源的角色总积信息边界
statement: 对任意线性源 p=a+s+asR，令 K=(pR+1)/4，并令 H_R(K) 为 K 的素因子模 R 残数生成的子群。恒有 4 属于 H_R(K)。因而任何在 H_R(K) 上平凡的单位群角色都在 4 上平凡；另一方面，4K=(aR+1)(sR+1) 的两块总积对每个角色都恒取值 1。故仅保留 K 或两块因子的总乘积角色值，不能区分子群障碍与非障碍；选择器证明必须使用各个素因子的角色分布或有限指数盒信息。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- subgroup-character
- factorization
- obstruction
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 线性 Type I 源的角色总积信息边界

## 定理

设

\[
p=a+s+asR,\; s\equiv1\pmod2,\; R\equiv3\pmod4,
\]

并令

\[
K=\frac{pR+1}{4},\;
\mathcal H_R(K)=\left\langle q\bmod R:q\mid K\right\rangle
\le(\mathbb Z/R\mathbb Z)^\times. \tag{1}
\]

则

\[
\boxed{4\in\mathcal H_R(K).} \tag{2}
\]

因此，若单位群角色 \(\chi\) 在 \(\mathcal H_R(K)\) 上平凡，例如它是一般
\(B\) 子群障碍的分离角色，则

\[
\chi(4)=1. \tag{3}
\]

此外，线性源因子化

\[
4K=(aR+1)(sR+1) \tag{4}
\]

在任意单位群角色下恒满足

\[
\chi(aR+1)=\chi(sR+1)=\chi(4K)=1. \tag{5}
\]

故 \(K\) 的总乘积、以及源块与仿射块的总乘积角色值，不能区分
\(-1\notin\mathcal H_R(K)\) 的子群障碍和 \(-1\in\mathcal H_R(K)\) 的非障碍。

## 证明

由 \(4K=pR+1\) 得

\[
4K\equiv1\pmod R,
\]

故 \(K\equiv4^{-1}\pmod R\)。另一方面，\(K\) 本身是它全部素因子残数的积，
所以 \(K\in\mathcal H_R(K)\)。于是 \(4^{-1}\in\mathcal H_R(K)\)，从而得到
(2)。任何在该子群上平凡的角色必满足 (3)。

式 (4) 来自

\[
pR+1=(aR+1)(sR+1).
\]

两个因子都同余于 \(1\pmod R\)，所以任何 \(\chi:U(R)\to\mathbb C^\times\)
都满足 (5)。这说明把素因子角色值先相乘，只会得到恒等的总积信息；它丢弃了
“每一个 \(q\mid K\) 都在 \(\ker\chi\) 内”这一子群障碍真正需要的逐素因子条件。

## 两个显式对照

同一个总积角色值确实可对应相反的子群结论。

第一例取核心素数 \(p=73\) 的线性源

\[
73=18+1+18\cdot1\cdot3,\; R=3,\; K=55=5\cdot11.
\]

令 \(\chi\) 为 \(U(3)\) 的非平凡二次角色。则

\[
\chi(4)=\chi(K)=1,\; \chi(5)=\chi(11)=-1.
\]

所以 \(-1\in\mathcal H_3(55)\)：总积为 \(1\)，但单个素因子并不在角色核中，
这里没有子群障碍。

第二例取冻结剖面中的

\[
p=3942409,\; R=39,\;
K=38438488=2^3\cdot11\cdot436801.
\]

对复合二次角色

\[
\chi(u)=\left(\frac{u}{3}\right)\left(\frac{u}{13}\right),
\]

全部三个不同素因子都满足 \(\chi(q)=1\)，而 \(\chi(-1)=-1\)。因此这是一个
子群障碍；同时仍有 \(\chi(4)=\chi(K)=1\)。两例的总积数据相同，障碍结论相反。

## 对证明路线的限制

该定理不反驳线性一般 \(B\) 选择猜想，也不排除利用不同源状态的实际素因子分布建立
跨源论证。它只排除一种更弱的设想：把每个源状态压缩为 \(\chi(K)\)、
\(\chi(aR+1)\)、\(\chi(sR+1)\) 或它们的有限合取后，再期待从这些总积同余推出
全局矛盾。

因此下一步的共同对象若存在，至少必须保留下列之一：

- 各素因子在角色核外的出现次数或最小违反因子；
- 中心化有限指数盒中的可达坐标；
- 不同移位整数的实际公共素因子或不可共享因子。

这与[一般 \(B\) 中心化平方除子谱障碍二分](type-I-general-b-centered-square-spectrum.md)
的边界一致，并具体解释了为什么
[线性一般 \(B\) 全谱剖面](type-I-global-linear-b1-failure-general-b-profile-500m.md)
中记录角色本身仍不足以比较不同 \(R\)。
