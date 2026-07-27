---
kind: claim
claim_id: three-p-plus-one-density-one-descent
title: (3p+1)/4 标记递降覆盖相对密度一的核心素数
statement: 满足 p<=X、p=1 mod24 且 (3p+1)/4 没有 2 mod3 素因子的素数数量为 O(X/(log X)^(3/2))；因此 three-p-plus-one-descent-certificate 覆盖相对密度一的核心素数，并给出 O(sqrt(p)) 的 Type I 缺口及严格可提升的较小实例。
claim_status: established
topics:
- sieve
- density
- descent
- certificate
- type-I
sources:
- paper: elsholtz_tao2013
  locator: "Appendix A, shifted-prime additive functions and sieve estimates"
  role: methodological-foundation
visibility: public
last_checked: '2026-07-23'
---

# \((3p+1)/4\) 标记递降覆盖相对密度一的核心素数

令

\[
R_3(X)=\#\left\{p\le X:p\equiv1\pmod{24},\ p\text{ prime},
\ q\nmid\frac{3p+1}{4}\text{ for every }q\equiv2\pmod3\right\}.
\]

则

\[
R_3(X)\ll\frac{X}{(\log X)^{3/2}}. \tag{1}
\]

由 `three-p-plus-one-descent-certificate`，其补集中的每个核心素数都有
\(m=O(\sqrt p)\) 的 Type I 证书，并有一条到 \(n=(3p+1)/4<p\) 的显式可提升边。
由于 \(\pi(X;24,1)\asymp X/\log X\)，该分支覆盖相对密度一的核心素数。

## 筛法证明

写 \(p=24t+1\)，则

\[
\frac{3p+1}{4}=18t+1.
\]

对每个素数 \(\ell>3\)，在 \(t\pmod\ell\) 上筛去：

- 当 \(\ell\equiv1\pmod3\) 时，只筛去 \(24t+1\equiv0\pmod\ell\) 的一个类；
- 当 \(\ell\equiv2\pmod3\) 时，另筛去 \(18t+1\equiv0\pmod\ell\) 的一个类。

两类在 \(\ell>3\) 时不同，否则 \(24\equiv18\pmod\ell\) 将迫使 \(\ell\mid6\)。
故局部筛积为

\[
V_3(z)=
\prod_{\substack{\ell\le z\\\ell\equiv1\ (3)}}\left(1-\frac1\ell\right)
\prod_{\substack{\ell\le z\\\ell\equiv2\ (3)}}\left(1-\frac2\ell\right)
\asymp(\log z)^{-3/2}. \tag{2}
\]

这里使用算术级数中的 Mertens 定理。标准 Selberg 上界筛对区间 \(t\le X/24\) 给出

\[
S_3(X,z)\ll XV_3(z)+z^2(\log z)^{O(1)}.
\]

取 \(z=X^{1/4}\)。被 \(R_3(X)\) 计数的充分大素数没有任何被筛去的因子，
因而属于该筛余集，结合 (2) 得到 (1)。对平方自由模数，禁类交集数为主项
\(X\omega(d)/(24d)\) 加上 \(O(\omega(d))\)，满足此上界筛所需的余项估计。

## 边界

密度一仍允许无限个例外；(1) 不构造例外上的短证书或递降选择器。因此它缩小了
全称目标的残余集，但不代替所需的逐点引理。
