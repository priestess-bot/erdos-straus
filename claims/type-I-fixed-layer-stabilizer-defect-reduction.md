---
kind: claim
claim_id: type-I-fixed-layer-stabilizer-defect-reduction
title: 固定层稳定子缺陷约化
statement: 设 K=N product q_i^{b_i} 且固定层 J=C_R(N) 不要求为子群。令 H 为 K 的素因子残数生成子群，P=Stab_H(J)，并投影到 H/P。则 P subset J，pi(J) 无周期，且 pi(C_R(K))=pi(J) product_i pi(S_i^+/-)；在 -1 属于 H 时，-1 属于 C_R(K) 当且仅当 pi(-1) 属于该投影积集。若 -1 不属于 H，应先分出 G 型支撑障碍。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- general-b
- fixed-layer
- stabilizer
- Kneser
- finite-abelian-groups
- F-state
- G-state
- proof-program
sources:
- paper: grynkiewicz_marchan_ordaz2009
  locator: Theorem C
  role: finite-sumset-growth-context
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-terminal-selector-context
visibility: public
last_checked: '2026-07-29'
---

# 固定层稳定子缺陷约化

## 设置

设 $R$ 为奇数，

\[
K=N\prod_{i=1}^{k}q_i^{b_i},
\]

其中 $q_i$ 是固定层 $N$ 以外的不同素数。令

\[
H=\left\langle q:q\mid K\right\rangle\le(\mathbb Z/R\mathbb Z)^\times,
\qquad
J=\mathcal C_R(N),
\qquad
S_i^{\pm}=\{q_i^z:-b_i\le z\le b_i\}.
\]

指数坐标的直接分解给出

\[
\mathcal C_R(K)=J\prod_{i=1}^{k}S_i^{\pm}.
\]

这里不假设 $J$ 是子群；通常它只是含单位元的对称有限子集。

## 稳定子约化定理

令

\[
P=\operatorname{Stab}_H(J)=\{h\in H:hJ=J\},
\qquad
\pi:H\to H/P.
\]

则：

1. $P\subseteq J$，因而 $JP=J$；
2. $\pi(J)$ 在 $H/P$ 中无周期，即
   $\operatorname{Stab}_{H/P}(\pi(J))=\{P\}$；
3. 投影保持积集恒等式：
   \[
   \boxed{\pi(\mathcal C_R(K))
   =\pi(J)\prod_i\pi(S_i^{\pm}).}
   \]
4. 若 $-1\in H$，则目标成员关系精确保留：
   \[
   \boxed{
   -1\in\mathcal C_R(K)
   \Longleftrightarrow
   \pi(-1)\in\pi(J)\prod_i\pi(S_i^{\pm}).}
   \]

若 $-1\notin H$，第四项不适用；该状态先归入 G 型支撑障碍，不能在商群中写成
一个不存在的 $\pi(-1)$。

### 证明

因为 $1\in J$，若 $x\in P$，则
$x=x\cdot1\in xJ=J$，故 $P\subseteq J$。稳定子定义也给出 $JP=J$。

对第三项直接投影积集恒等式即可。若 $xP$ 稳定 $\pi(J)$，则
\[
\pi(xJ)=xP\,\pi(J)=\pi(J),
\]
所以 $xJP=JP$。使用 $JP=J$ 得 $xJ=J$，即 $x\in P$。
因此投影后的固定层无周期，第二项成立。

最后，
\(\mathcal C_R(K)=J\prod_iS_i^{\pm}\) 是 $P$-周期集，因为 $P$ 稳定 $J$。
一个元素是否属于该集合完全由它在 $H/P$ 中的像决定，故得到第四项。
证毕。

## 研究作用与边界

这条定理把“固定层必须恰好是子群”的特殊假设改成稳定子约化。约化后的
\(\pi(J)\) 是无周期缺陷因子，可直接作为 Kneser、Kemperman 或 Pollard 型论证的第一层。
但它只降低有限群表示的周期，不降低 $p$、$R$、缺口或任何算术势函数；因此输出仍是
**商群压缩**，不是算术下降，也不单独给出全称选择器。
