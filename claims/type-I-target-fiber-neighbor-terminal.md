---
kind: claim
claim_id: type-I-target-fiber-neighbor-terminal
title: 目标指数纤维反足与近邻终端引理
statement: 对合法 Type I 状态 K=(pR+1)/4，目标指数纤维对取反封闭且无固定点；若其中存在两个不同表示 z,w 满足逐坐标距离不超过对应指数预算，则定向后的比值产生偶数 E，满足 E|4K^2、E=1 mod R、E<=4K-4R，并给出 0<n<p 的偶终端 n=(4K-E)/R。目标纤维大小超过 2^omega(K) 是该近邻对的充分条件，但不是必要条件。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- general-b
- target-fiber
- antipodal
- near-pair
- finite-exponent
- even-terminal
- divisor-residues
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-terminal-selector-context
visibility: public
last_checked: '2026-07-29'
---

# 目标指数纤维反足与近邻终端引理

## 设置

设 $p$ 为核心素数，$R\equiv3\pmod4$，并令

\[
K=\frac{pR+1}{4}=\prod_{i=1}^{r}q_i^{\nu_i},
\qquad r=\omega(K).
\]

因为 $4K\equiv1\pmod R$，所以每个 $q_i$ 都与 $R$ 互素。定义目标指数纤维

\[
\mathcal Z^-_{R,K}
=\left\{z\in\mathbb Z^r:
-\nu_i\le z_i\le\nu_i,
\quad \prod_iq_i^{z_i}\equiv-1\pmod R\right\}.
\]

负指数只表示单位群中的逆元；它不表示有理数除法未被整除。

## 反足对称性

若 $z\in\mathcal Z^-_{R,K}$，则

\[
\prod_iq_i^{-z_i}\equiv(-1)^{-1}\equiv-1\pmod R,
\]

故 $-z\in\mathcal Z^-_{R,K}$。由于 $R>2$，零向量不属于该纤维；因此取反没有固定点，
每个非空目标纤维都有偶数个元素，并且所有大小为 $2$ 的纤维恰为一对
$\{z,-z\}$。这解释了为什么有限审计中的最小目标表示数是 $2$，但它本身不保证近邻终端。

## 近邻终端定理

若存在不同的 $z,w\in\mathcal Z^-_{R,K}$，满足

\[
|z_i-w_i|\le\nu_i\qquad(1\le i\le r),
\]

则交换 $z,w$ 后可设

\[
\rho=\prod_iq_i^{z_i-w_i}<1.
\]

令

\[
U=K\rho=\prod_iq_i^{\nu_i+z_i-w_i},
\qquad E=4U.
\]

则 $U$ 为正整数，且

\[
U\mid K^2,
\qquad U\equiv K\pmod R,
\qquad 0<U<K.
\]

因此

\[
E\mid4K^2,
\qquad E\equiv1\pmod R,
\qquad E\le4K-4R.
\]

定义

\[
n=\frac{4K-E}{R}=\frac{4(K-U)}{R}.
\]

则 $n$ 是正的、可被 $4$ 整除的整数，并且

\[
0<n<p.
\]

所以在同一合法 $(R,K)$ 状态中，近邻目标表示直接给出一般混合 Type I 所需的偶终端。

### 证明

由逐坐标距离假设，
$0\le\nu_i+z_i-w_i\le2\nu_i$，故 $U$ 为整数且 $U\mid K^2$。
目标同余相除得到
$(\rho\equiv(-1)(-1)^{-1}\equiv1\pmod R)$，从而 $U\equiv K\pmod R$。
方向选择给出 $U<K$。于是 $R\mid K-U$，且
$n=4(K-U)/R$ 为正整数；因为 $R$ 为奇数，$R\mid K-U$ 后 $n$ 仍是 $4$ 的倍数。

又 $U<K$ 且二者同余于 $R$，所以 $K-U\ge R$，得到
$E=4U\le4K-4R$。最后
\[
n<\frac{4K}{R}=p+\frac1R,
\]
故整数 $n\le p$。若 $n=p$，则
$4(K-U)=pR=4K-1$，左边被 $4$ 整除而右边不被 $4$ 整除，矛盾；所以 $n<p$。
证毕。

## 装箱推论

把每个坐标区间分成两个半区：
$[0,\nu_i]$ 与 $[-\nu_i,-1]$，并把零归入前一半。共有 $2^r$ 个符号盒。
同一符号盒中的两个指数向量自动满足
$|z_i-w_i|\le\nu_i$；因此

\[
\boxed{
|\mathcal Z^-_{R,K}|>2^{\omega(K)}
\Longrightarrow
\text{存在近邻对，进而存在偶终端}.}
\]

这个阈值只是一个方便的充分条件。没有近邻对时只能推出每个符号盒至多一个元素，
即 $|\mathcal Z^-_{R,K}|\le2^r$；要得到稀疏递降，还需额外的结构定理。

## 逻辑边界

本卡证明的是**固定状态内**的终端构造，不证明每个核心素数都存在目标纤维，也不证明
所有稀疏纤维都能递降。它应作为统一选择器中的第一出口：先检查近邻对；失败后才把纤维
送入 Fourier、关系格或加法组合的对偶证书分支。
