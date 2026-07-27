---
kind: claim
claim_id: six-branch-sieve-residual
title: 六条显式因子证书分支的共同残余有 4 维筛界
statement: 令 R_6(X) 为 p<=X、p=1 mod24 的素数中同时未被五条既有因子分支及 p+2 的 7 mod8 因子分支覆盖的数量，则 R_6(X)=O(X/(log X)^4)。这仍只是密度零结论，不产生逐点的短证书或递降。
claim_status: established
topics:
- sieve
- density
- certificate
- residual-set
- proof-program
sources:
- paper: elsholtz_tao2013
  locator: "Appendix A, shifted-prime additive functions and sieve estimates"
  role: methodological-foundation
- paper: ventas2026
  locator: "Theorem 2.3"
  role: external-source-formulation
visibility: public
last_checked: '2026-07-23'
---

# 六条显式因子证书分支的共同残余有 \(4\) 维筛界

在 `five-branch-sieve-residual` 的五个移位整数之外，加入

\[
p+2=24t+3.
\]

`p-plus-two-external-source-certificate` 说明：只要它含 \(7\pmod8\) 因子便有
Type I 证书。因此共同残余还要求 \(p+2\) 的每个素因子为 \(1\) 或 \(3\pmod8\)。

令 \(R_6(X)\) 为六分支均失败的核心素数数目。则

\[
R_6(X)\ll\frac{X}{(\log X)^4}. \tag{1}
\]

## 筛法证明

沿用 `five-branch-sieve-residual` 的变量 \(p=24t+1\)。对每个奇素数
\(\ell\) ，除了原有禁类外，当

\[
\ell\equiv5,7\pmod8
\]

时，再筛去 \(24t+3\equiv0\pmod\ell\) 这一类。有限个使该类与既有线性类重合的
素数只改变常数：任意两个不同线性式的行列式固定且非零。

四个模 \(24\) 的可逆剩余类中，原五分支的平均禁类数为 \(7/2\)，新类在

\[
5,7,13,23\pmod{24}

\]

中恰出现两类，故再贡献平均 \(1/2\)。因此筛积满足

\[
V_6(z)=\prod_{\ell\le z}\left(1-\frac{\nu_6(\ell)}\ell\right)
\asymp(\log z)^{-4}. \tag{2}
\]

对相同的线性筛系统应用标准 Selberg 上界筛，并取 \(z=X^{1/4}\)，即得 (1)。

## 边界

新分支覆盖了五分支的第一个残余 \(p=2521\)：
\(2521+2=3\cdot29^2\) 含因子 \(87\equiv7\pmod8\)。六分支共同残余仍非空；
例如 \(p=5569\) 的六个移位整数满足相应的失败因子条件。它事实上有缺口
\(m=7\) 的一般 Type I 证书（非端点除子 \(d=17\)），这说明本筛只刻画所列分支的
共同补集，而不是“无证书”的集合。对该补集仍须构造新的因子依赖证书或一个可闭合的
严格递降边。
