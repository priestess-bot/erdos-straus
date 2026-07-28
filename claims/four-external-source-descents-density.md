---
kind: claim
claim_id: four-external-source-descents-density
title: 四条外部源递降覆盖的共同残余有 3 维筛界
statement: 令 R(X) 计数 p<=X、p=1 mod24 且对 k=1,2,3,6 的 adaptive-external-source-descent 分支均失败的素数，则 R(X)=O(X/(log X)^3)。每条成功分支同时给出 m<=4sqrt(p)/3+1/3 的 Type I 证书和到更小标记源实例的严格提升。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- descent
- certificate
- type-I
- sieve
- density
- factorization
- proof-program
sources:
- paper: elsholtz_tao2013
  locator: "Appendix A, shifted-prime additive functions and sieve estimates"
  role: methodological-foundation
- paper: bradford2024
  locator: "Propositions 1 and 3"
  role: Type-I-certificate-equivalence
visibility: public
last_checked: '2026-07-24'
---

# 四条外部源递降覆盖的共同残余有 3 维筛界

令

\[
\mathcal Q=\{3,7,11,23\},\qquad
k_q=\frac{q+1}{4},\qquad
n_q=\frac{qp+1}{q+1}. \tag{1}
\]

对核心素数 \(p\equiv1\pmod{24}\)，四个 \(k_q\) 都整除
\((p-1)/4\)，所以 adaptive-external-source-descent 对每个 \(q\in\mathcal Q\)
都可适用。令 \(R(X)\) 计数 \(p\le X\) 且这四条分支均失败的核心素数。则

\[
R(X)\ll\frac{X}{(\log X)^3}. \tag{2}
\]

## 因子残数的失败条件

固定 \(q\in\mathcal Q\)。由 (1) 有 \(n_q\equiv1\pmod q\)。这条递降失败当且仅当
\(n_q\) 没有因子 \(f\equiv-1\pmod q\)。

每个 \(q\) 都是 \(3\pmod4\) 素数，所以 \(-1\) 在
\((\mathbb Z/q\mathbb Z)^\times\) 中不是平方。反演平移

\[
r\longmapsto-r^{-1} \tag{3}
\]

把该单位群分成 \((q-1)/2\) 个无固定点二元组。若 \(n_q\) 的两个素因子残数
来自同一二元组，则它们的乘积就是一个 \(-1\pmod q\) 的因子，矛盾。因此，分支失败时
\(n_q\) 的全部素因子残数包含于某个半大小横截面

\[
T_q\subseteq(\mathbb Z/q\mathbb Z)^\times,\qquad |T_q|=\frac{q-1}{2}. \tag{4}
\]

这是失败的必要条件，不是充分分类；横截面内的多个因子仍可能积为 \(-1\)。

## 筛法证明

固定四个横截面 \(T_q\)。除了整除

\[
24\prod_{q\in\mathcal Q}q(q+1)
\prod_{\substack{q,q'\in\mathcal Q\\q<q'}}(q-q') \tag{5}
\]

的有限个素数 \(\ell\) 外，若
\(\ell\pmod q\notin T_q\)，则筛去线性式

\[
qp+1\equiv0\pmod\ell \tag{6}
\]

的唯一根；因为 \(\ell\nmid q+1\)，这等价于 \(\ell\mid n_q\)。同时还筛去
\(p\equiv0\pmod\ell\) 的唯一根。

四条新增根彼此不重合：若 \(qp+1\) 与 \(q'p+1\) 在 \(\ell\) 处有共同根，则
\(\ell\mid q-q'\)，已包含在有限例外中；它们也不可能与 \(p\) 的根重合。对固定
\(q\)，当 \(\ell\) 在模

\[
Q=\prod_{q\in\mathcal Q}q
\]

的可逆残数类中平均时，条件 \(\ell\pmod q\notin T_q\) 的比例是 \(1/2\)。
所以固定横截面系统的筛维是

\[
1+\sum_{q\in\mathcal Q}\frac12=3. \tag{7}
\]

对 \(p=24t+1\) 应用标准 Selberg 上界筛，并用算术级数中的 Mertens 定理估计筛积，
得到 \(O(X/(\log X)^3)\)。四个 \(T_q\) 的选择数有限，对其求和仍给出 (2)。

## 含义与边界

每个未被 \(R(X)\) 计数的 \(p\) 都由 adaptive-external-source-descent 给出：
\[
m\le\frac{4\sqrt p+1}{3},
\]
以及一条显式的带标记严格提升。式 (2) 比只使用 \(q=3\) 分支的
\(O(X/(\log X)^{3/2})\) 残余界更薄，但仍允许无限例外；它没有构造四条分支共同残余上的
选择器，故不完成目标引理。
