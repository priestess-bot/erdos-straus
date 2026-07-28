---
kind: claim
claim_id: p-plus-one-density-one-certificate
title: (p+1)/2 平方根证书覆盖相对密度一的核心素数
statement: 满足 p<=X、p=1 mod 24 且 (p+1)/2 没有 3 mod 4 素因子的素数数量为 O(X/(log X)^(3/2))；因此 p-plus-one-sqrt-certificate 的 Type I 构造覆盖相对密度一的核心素数。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- sieve
- density
- certificate
- type-I
sources:
- paper: elsholtz_tao2013
  locator: "Appendix A, shifted-prime additive functions and sieve estimates"
  role: methodological-foundation
visibility: public
last_checked: '2026-07-23'
---

# (p+1)/2 平方根证书覆盖相对密度一的核心素数

## 精确表述

令

\[
R(X)=\#\left\{p\le X:p\equiv1\pmod{24},\ p\text{ prime},\\
q\nmid\frac{p+1}{2}\text{ for every }q\equiv3\pmod4\right\}.
\]

则

\[
R(X)\ll\frac{X}{(\log X)^{3/2}}.
\]

由 `p-plus-one-sqrt-certificate`，补集中的每个核心素数都有 \(m\le\sqrt p\) 的 Type I 证书。又
\(\pi(X;24,1)\asymp X/\log X\)，故未被该构造覆盖的核心素数相对密度为 \(0\)。

## 筛法证明

写 \(p=24t+1\)，则 \((p+1)/2=12t+1\)。对每个奇素数 \(\ell>3\)，在 \(t\pmod\ell\) 上筛去：

- 当 \(\ell\equiv1\pmod4\) 时，只筛去 \(24t+1\equiv0\pmod\ell\) 的一个剩余类；
- 当 \(\ell\equiv3\pmod4\) 时，另筛去 \(12t+1\equiv0\pmod\ell\) 的一个剩余类。

在第二种情形，这两个剩余类不同，因此局部禁类数为 \(2\)。设 \(V(z)\) 为相应筛积，则算术级数中的 Mertens 定理给出

\[
V(z)=
\prod_{\substack{\ell\le z\\\ell\equiv1\ (4)}}\left(1-\frac1\ell\right)
\prod_{\substack{\ell\le z\\\ell\equiv3\ (4)}}\left(1-\frac2\ell\right)
\asymp(\log z)^{-3/2}.
\]

标准 Selberg 上界筛应用于区间 \(t\le X/24\) 给出

\[
S(X,z)\ll XV(z)+z^2(\log z)^{O(1)}.
\]

取 \(z=X^{1/4}\)。被 \(R(X)\) 计数的每个充分大的素数都属于该筛余集，故
\(R(X)\ll X/(\log X)^{3/2}\)。

这里筛去 \(24t+1\equiv0\pmod\ell\) 并不是把“\(24t+1\) 为素数”替换成
一个未经证明的条件。若被计数的 \(p>z\) 是素数，它本来就不含任何
\(\ell\le z\) 的素因子；至多 \(p\le z\) 的有限前缀需要另计，贡献 \(O(z)\)，
并被上述上界吸收。这一条正是筛维中恒有的 \(1\) 的来源。

这里的估计是本库基于标准上界筛的推导：对平方自由模数 \(d\)，上述禁类的交集计数为主项 \(X\omega(d)/(24d)\) 加上 \(O(\omega(d))\)，恰满足上界筛的余项假设。所引论文提供本问题中移位素数与筛法的背景，不应误读为其原文逐字陈述了这个特定的证书族。

## 边界条件

相对密度一不等于“没有例外”。该界仍与无限个未覆盖核心素数相容，因而不能替代所需的逐点短证书或递降引理。
