---
kind: claim
claim_id: type-II-two-power-character-depth-sieve
title: Type II 支撑外失败的二幂字符深度与增强筛界
statement: 对固定 Type II AC 射线，若目标 -1 在素因子残数生成子群 K 的 2^d 次幂饱和中但不在其 2^(d+1) 次幂饱和中，则存在一个像阶恰为 2^(d+1) 的 Dirichlet 型字符消去 K 且取 -1 为负；因而全部移位数素因子残数落在一个相对大小 2^-(d+1) 的固定字符核中。对 L 条移位互异射线，若每条都属于深度至少 s 的支撑外失败，则其共同核心素数残余为 O(X/(log X)^(1+L(1-2^-(s+1))))。
claim_status: established
topics:
- type-II
- divisor-residues
- finite-abelian-groups
- higher-order-characters
- sieve
- residual-set
- proof-program
sources:
- paper: elsholtz_tao2013
  locator: "Appendix A, shifted-prime additive functions and sieve estimates"
  role: upper-bound-sieve-methodology
- paper: grynkiewicz_marchan_ordaz2009
  locator: "subsequence-product framework"
  role: structural-context
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-application-context
visibility: public
last_checked: '2026-07-24'
---

# Type II 支撑外失败的二幂字符深度与增强筛界

## 深度定义与字符引理

令 \(G=U(M)\)、\(M=4AC\)，并令 \(K\le G\) 是移位数
\(N=p+4A^2C\) 的全部素因子残数生成的子群。假设 \(-1\notin K\)。记

\[
G^{2^d}=\{g^{2^d}:g\in G\},
\]

并定义二幂深度

\[
\nu(K)=\max\{d\ge0:-1\in K G^{2^d}\}. \tag{1}
\]

该最大值存在：当 \(d\) 足够大时，\(-1\) 在有限商群 \(G/K\) 中不可能仍是
\(2^d\) 次幂，否则其非平凡二阶像会同时属于奇阶部分。

**字符引理。** 存在一个群字符

\[
\chi:G\longrightarrow\mu_{2^{\nu(K)+1}}
\]

满足

\[
K\subseteq\ker\chi,\qquad \chi(-1)=-1,\qquad
|\operatorname{im}\chi|=2^{\nu(K)+1}. \tag{2}
\]

**证明。** 在商

\[
Q=G/(K G^{2^{\nu(K)+1}})
\]

中，\(-1\) 非平凡且 \(Q\) 的指数整除 \(2^{\nu(K)+1}\)。有限阿贝尔群的字符对
点分离，故存在 \(Q\) 的角色把 \(-1\) 送至 \(-1\)；复合商映射即得前两式。
又由 (1)，可写 \(-1=kg^{2^{\nu(K)}}\)，其中 \(k\in K\)。于是
\(\chi(g)^{2^{\nu(K)}}=-1\)，迫使 \(\chi(g)\) 的阶为
\(2^{\nu(K)+1}\)，得到第三式。

所以 \(K\) 包含于一个相对大小恰为

\[
2^{-(\nu(K)+1)} \tag{3}
\]

的字符核；所有 \(N\) 的素因子残数也都在此核内。

## 条件性增强筛界

取有限射线集

\[
\mathcal S=\{(A_j,C_j):1\le j\le L\},
\]

并假设 \(A_j^2C_j\) 两两不同。固定 \(s\ge0\)，令
\(R_{\mathcal S}^{\ge s}(X)\) 计数核心素数 \(p\le X\)，要求对每条射线：

1. \(-1\notin K_j\)；以及
2. \(\nu(K_j)\ge s\)。

则

\[
R_{\mathcal S}^{\ge s}(X)
\ll_{\mathcal S,s}
\frac{X}{(\log X)^{1+L(1-2^{-(s+1)})}}. \tag{4}
\]

**证明。** 逐条应用 (2)。深度至少 \(s\) 时，所有素因子残数落在某个固定模
\(4A_jC_j\) 的子群内，其相对大小至多 \(2^{-(s+1)}\)。可选字符核的数目只依赖
于固定模数，故对其有限选择求和即可。固定一组核后，type-II-ac-rays-superlog-residual
的筛法证明逐字适用：第 \(j\) 个移位数的局部允许比例至多 \(2^{-(s+1)}\)，所以平均
禁根贡献至少 \(1-2^{-(s+1)}\)。移位互异保证根不碰撞，Selberg 上界筛给出 (4)。

当 \(s=0\)，每条贡献 \(1/2\)，恢复支撑外层的半大小机制；当 \(s=1\)，每条贡献
\(3/4\)；当 \(s=2\)，每条贡献 \(7/8\)。

## 边界

(4) 不适用于 \(-1\in K\) 的支撑内失败，也不适用于深度零以外未被额外假设排除的
一般支撑外失败。特别地，它不改写原来的全体 Type II 残余界，更不证明残余为空。
其作用是把平方饱和核继续细分成可由高阶字符处理的层，而不是把“二次不可分”误当作
最终障碍。

更强地，不能只把各射线的字符核乘回 \(p\) 的同余条件来寻求矛盾：
type-II-character-product-congruence-compatibility-boundary 证明所有有限个
\(\chi_j(p)=1\) 都由一条 \(p\equiv1\) 的 Dirichlet 素数列同时满足。后续若要利用
字符深度，必须保留移位数的逐素因子条件或其跨移位关联。

在 \(p\le10^5\)、\(A,C\le5\) 的审计中，20,089 条支撑外失败的深度分布为
\[
\nu=0:19608,\qquad \nu=1:469,\qquad \nu=2:9,\qquad \nu=3:3.
\]
例如 \(p=97,(A,C)=(2,4)\) 的深度为 1；\(p=3457,(A,C)=(4,4)\) 的深度为 2；
\(p=14593,(A,C)=(4,4)\) 的深度为 3。

## 复现

运行 python3 reproductions/divisor_residue_structure.py --audit-limit 100000 --ac-bound 5。
