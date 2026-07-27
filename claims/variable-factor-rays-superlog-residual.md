---
kind: claim
claim_id: variable-factor-rays-superlog-residual
title: 组合变量因子射线给出任意对数幂的共同残余界
statement: 对 L 条 A_j=2^(j+1) 的 3p+A_j Type I 射线和 J 条互异的固定缺口 q_i=3 mod4 Type II 因子射线，逃过七条既有分支及这些射线的核心素数数目为 O_{L,q}(X/(log X)^((L+J+9)/2))。让 L 或 J 随所需的固定幂增加，逃过所有这些射线的集合是任意对数幂稀薄的；这不蕴含其为空。
claim_status: established
topics:
- sieve
- density
- certificate
- type-I
- type-II
- ray
- residual-set
- proof-program
sources:
- paper: elsholtz_tao2013
  locator: "Appendix A, shifted-prime additive functions and sieve estimates"
  role: methodological-foundation
- paper: bradford2024
  locator: "Propositions 1 and 2"
  role: Type-I-II-certificate-equivalence
visibility: public
last_checked: '2026-07-23'
---

# 组合变量因子射线给出任意对数幂的共同残余界

取 \(L\ge0\) 个

\[
A_j=2^{j+1}\quad(1\le j\le L)
\]

的 `three-p-plus-power-two-internal-type-I-ray`，以及 \(J\ge0\) 个互异素数

\[
q_1,\ldots,q_J\equiv3\pmod4,\qquad q_i\ge7,
\]

的 `fixed-gap-type-II-factor-ray`。令 \(R_{L,\boldsymbol q}(X)\) 是 \(p\le X\)、
\(p\equiv1\pmod{24}\) 的素数中，同时逃过七条既有因子分支和这些 \(L+J\) 条射线者。
则

\[
R_{L,\boldsymbol q}(X)
\ll_{L,\boldsymbol q}
\frac{X}{(\log X)^{(L+J+9)/2}}. \tag{1}
\]

## 证明

幂二 Type I 射线的每条失败条件由
`three-p-plus-power-two-internal-type-I-ray` 压入模 \(12A_j\) 的半大小横截面；
固定缺口 Type II 射线的每条失败条件由 `fixed-gap-type-II-factor-ray` 压入模
\(q_i\) 的半大小横截面。有限个 \(p\le\max_i(q_i+1)\) 只改变常数，故可设所有
固定缺口均在自然范围。固定所有有限的横截面选择和 \(p\) 的必要残数类后，在
相应合并模数的每个非例外素数 \(\ell\) 处，每条射线都在其线性移位数为零时增加一个
禁根，并且在算术级数的素数类平均下各贡献

\[
\frac12. \tag{2}
\]

新增线性式彼此只在有限个素数处有同根：\(3p+A_i\) 与 \(3p+A_j\) 的行列式是
\(A_i-A_j\)；\(p+q_i\) 与 \(p+q_j\) 的行列式是 \(q_i-q_j\)；不同类型或与
七条既有式子的行列式也都是固定非零整数。有限例外不影响筛维。

`seven-branch-sieve-residual` 的基准维数为 \(9/2\)，所以固定系统的维数为

\[
\frac92+\frac{L+J}{2}=\frac{L+J+9}{2}. \tag{3}
\]

标准 Selberg 上界筛再对有限多个横截面系统求和，便得到 (1)。

若允许所有 \(A=2^a\ge4\) 射线和所有 \(q\equiv3\pmod4\) 的固定缺口射线，则对
每个固定 \(B>0\)，选取任意满足 \(L+J\ge\max\{1,2B-9\}\) 的有限子族，得到

\[
R_\infty(X)\ll_B\frac{X}{(\log X)^B}. \tag{4}
\]

## 边界

这里 \(L,J\) 和所选 \(q_i\) 都可依赖于所要求的固定 \(B\)，隐含常数也随之变化。
而且对固定 \(p\)，只有 \(q\le p-2\) 的固定缺口射线可用，幂二射线也有
\(A\le(3p+9)/32\) 的必要条件。因此 (4) 是极薄残余的解析上界，绝不是对每个
核心素数的有限分支覆盖，更不能替代真正的递降选择器。
