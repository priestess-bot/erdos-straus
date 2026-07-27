---
kind: claim
claim_id: type-II-target-outside-support-quadratic-separation
title: Type II 支撑外失败的平方商二次特征分界
statement: "对固定 Type II AC 射线，令 G=U(4AC)、K 为移位整数素因子残数生成的子群。若 -1 不在 K，则存在二次特征 chi: G to {plus or minus 1}，在 K 上为 1 且 chi(-1)=-1，当且仅当 -1 不在 K times G squared。此时 chi(p)=1。进一步令 H 为核心素数 p=1 mod 24 可取的模 4AC 残数子群；在二次可分时，存在对 H 非平凡的分离特征当且仅当 H 不包含于 K times G squared。"
claim_status: established
topics:
- type-II
- divisor-residues
- subgroup-structure
- quadratic-character
- finite-abelian-groups
- proof-program
sources:
- paper: grynkiewicz_marchan_ordaz2009
  locator: "subsequence-product framework"
  role: structural-context
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-application-context
visibility: public
last_checked: '2026-07-24'
---

# Type II 支撑外失败的平方商二次特征分界

## 定理

令

\[
M=4AC,\qquad G=U(M),\qquad N=p+4A^2C,
\]

并令 \(K\le G\) 为 \(N\) 的全部素因子残数所生成的子群。设
\(-1\notin K\)，即目标残数在支撑外。记平方子群为

\[
G^2=\{g^2:g\in G\}. \tag{1}
\]

则以下两件事等价：

1. 存在群同态 \(\chi:G\to\{\pm1\}\)，满足

\[
\chi(K)=\{1\},\qquad \chi(-1)=-1; \tag{2}
\]

2.

\[
-1\notin KG^2. \tag{3}
\]

在这两件事成立时，因 \(N\bmod M=p\bmod M\in K\)，必有

\[
\chi(p)=1. \tag{4}
\]

因此支撑外失败精确分为可由二次特征分离的情形 (3)，以及平方饱和后仍包含
\(-1\) 的二次不可分核 \(-1\in KG^2\)。

## 证明

令 \(Q=G/(KG^2)\)。这是一个初等二元阿贝尔群，因为每个 \(g^2\) 在商中皆为
单位元。条件 (3) 等价于 \(-1\) 在 \(Q\) 中非平凡。于是把 \(Q\) 视为
\(\mathbb F_2\) 向量空间，存在一个线性泛函在 \(-1\) 的像上取 \(1\)。
将其与 \(G\to Q\) 复合，并把 \(0,1\) 分别写成 \(+1,-1\)，即得 (2)。

反向地，任何满足 (2) 的 \(\chi\) 都消去 \(K\) 和 \(G^2\)，却不消去 \(-1\)，
故 (3) 必成立。最后，全部素因子残数的乘积属于 \(K\)，且等于
\(N\equiv p\pmod M\)，所以 (4) 成立。

## 对核心同余类非平凡的精确条件

令

\[
H_M=\{r\in U(M):r\equiv1\pmod{\gcd(M,24)}\}. \tag{5}
\]

这恰是核心素数 \(p\equiv1\pmod{24}\) 在模 \(M\) 下可取的残数子群。假设 (3)
成立。则存在满足 (2) 且在 \(H_M\) 上非平凡的 \(\chi\)，当且仅当

\[
H_M\not\subset KG^2. \tag{6}
\]

事实上，令 \(V=G/(KG^2)\)。此时 \(-1\) 在 \(V\) 中非零。若 \(H_M\) 在 \(V\)
中的像为零，则每个消去 \(K\) 的二次特征都在 \(H_M\) 上平凡。反之，若其像含有
非零元 \(h\)，可在有限域 \(\mathbb F_2\) 上选择线性泛函，使 \(-1\) 的像取值为
\(1\)，且 \(h\) 的像也取值为 \(1\)；相应特征即满足要求。

因此 (6) 才是“二次特征对核心素数提供真实额外限制”的正确判据。此时
\(\chi(p)=1\) 把固定射线的允许核心残数限制到 \(H_M\) 的一个真指数二子群。

## 范围与边界

即使满足 (6)，选择到的 \(\chi\) 仍可随 \(K\) 及射线变化；不能直接把它当作独立的
筛维。它的价值是提供精确的代数分层：\(-1\in KG^2\) 是二次不可分核；
\(-1\notin KG^2\) 但 \(H_M\subset KG^2\) 是对核心同余平凡的可分层；只有 (6)
才是核心活跃的二次特征层。

在 \(p\le10^5\)、\(A,C\le5\) 的精确审计中，20,089 条支撑外失败里有 19,608 条
二次可分、481 条二次不可分。前者再分为 3,439 条核心活跃和 16,169 条核心平凡。
该比例是探索线索，不是渐近定理。

## 复现

运行 python3 reproductions/divisor_residue_structure.py --audit-limit 100000 --ac-bound 5。
