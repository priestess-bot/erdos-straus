---
kind: claim
claim_id: power-two-internal-rays-superlog-residual
title: 有限幂二内部射线给出任意对数幂的共同残余界
statement: 令 A_j=2^(j+1) (1<=j<=L)。若 R_L(X) 计数 p<=X、p=1 mod24 的素数中同时逃过七条既有因子分支及全部 L 条 3p+A_j 内部 Type I 射线者，则 R_L(X)=O_L(X/(log X)^((L+9)/2))。因而逃过全部幂二射线的共同残余对每个固定 B 都是 O_B(X/(log X)^B)；这不推出残余为空。
claim_status: established
topics:
- sieve
- density
- certificate
- type-I
- internal-parameter
- ray
- residual-set
- proof-program
sources:
- paper: elsholtz_tao2013
  locator: "Appendix A, shifted-prime additive functions and sieve estimates"
  role: methodological-foundation
- paper: bradford2024
  locator: "Proposition 1"
  role: Type-I-certificate-equivalence
visibility: public
last_checked: '2026-07-23'
---

# 有限幂二内部射线给出任意对数幂的共同残余界

令

\[
A_j=2^{j+1}\quad(1\le j\le L),
\]

并令 \(R_L(X)\) 计数所有 \(p\le X\)、\(p\equiv1\pmod{24}\) 的素数，要求它们同时
未被 `seven-branch-sieve-residual` 的七条分支以及
`three-p-plus-power-two-internal-type-I-ray` 的 \(A_1,\ldots,A_L\) 射线覆盖。则

\[
R_L(X)\ll_L\frac{X}{(\log X)^{(L+9)/2}}. \tag{1}
\]

特别地，令 \(R_\infty(X)\) 为逃过七条分支和**所有** \(A=2^a\ge4\) 射线的
核心素数数目，则对每个固定 \(B>0\)，

\[
R_\infty(X)\ll_B\frac{X}{(\log X)^B}. \tag{2}
\]

## 证明

固定 \(L\)。对每条射线 \(A_j\)，上一张卡片的残数配对给出：在固定
\(p\pmod{12A_j}\) 后，若该射线失败，则 \(3p+A_j\) 的所有素因子落入一个
横截面 \(T_j\subseteq(\mathbb Z/12A_j\mathbb Z)^\times\)，且

\[
|T_j|=\frac12\varphi(12A_j). \tag{3}
\]

可选横截面及 \(p\) 的残数类都只有有限多个。取

\[
Q=12A_L,
\]

并固定其中一个 \(p\pmod Q\) 的核心类和一组 \((T_1,\ldots,T_L)\)。对任何不整除
有限个线性式行列式的奇素数 \(\ell\)，当

\[
\ell\pmod{12A_j}\notin T_j,
\]

筛去线性式 \(3p+A_j\equiv0\pmod\ell\) 的一个根。按 (3)，在
\((\mathbb Z/Q\mathbb Z)^\times\) 的素数类上，这个额外禁根的平均数为 \(1/2\)。

不同 \(j\) 的新增根在奇素数 \(\ell\) 处不会重合：根重合将推出
\(\ell\mid A_i-A_j\)，而 \(A_i-A_j\) 是非零的 \(2\) 的幂。它们与七条已有线性式
的根至多在整除固定非零行列式的有限个 \(\ell\) 处重合。有限例外只改变常数。

`seven-branch-sieve-residual` 已给出基准筛维 \(9/2\)。故本固定系统的筛维为

\[
\frac92+\frac L2=\frac{L+9}{2}. \tag{4}
\]

对该有限线性筛系统使用相同的 Selberg 上界筛，并对有限多个 \(p\) 类及横截面选择
求和，得到 (1)，其中隐含常数可依赖于 \(L\)。

对任意 \(B>0\)，取正整数 \(L\ge\max\{1,2B-9\}\)。逃过所有幂二射线的集合
包含于对应的 \(R_L\)，故 (1) 给出 (2)。

## 边界

\(L=1\) 时，(1) 正是 `eight-branch-sieve-residual` 的 \(O(X/(\log X)^5)\)
界。式 (2) 是“比任意固定对数幂都稀薄”的**上界**，不是有限性定理：一个无限集合
仍可满足全部这些上界。并且 `three-p-plus-power-two-internal-type-I-ray` 给出
\(A\le(3p+9)/32\) 的必要条件，所以固定 \(p\) 只会看到有限条可用射线。因而它不能
替代对每个残余 \(p\) 构造证书或真正递降边的任务。
