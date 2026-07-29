---
kind: claim
claim_id: type-I-linear-f-critical-quotient-boundary
title: 线性 F 型稳定子群商的最小阶与四阶临界结构
statement: 设 gcd(K,R)=1，A=A_R(K)、H=H_R(K)、C=A A^{-1}，且 -1∈H\C。令 T=Stab_H(A)，则 T⊂A⊂C，-1不属于T；商群 H/T 由 A/T 生成、含有非平凡二阶元 -T，且 |H/T|≥4、|A/T|≤|H/T|/2。若 |H/T|=4，则 A/T={T,gT}，其中 gT 为阶四元；K 的所有素因子在商群中的非平凡残数只能集中于一个指数为一的素因子，其余素因子均落在 T 中。这是 F 型未命中的低复杂度临界障碍，不是全称反例。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- finite-exponent
- centered-spectrum
- critical-quotient
- subgroup-structure
- obstruction
- proof-program
sources:
- paper: grynkiewicz_marchan_ordaz2009
  locator: Theorem C
  role: stabilizer-and-critical-product-set-context
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-spectrum-context
visibility: public
last_checked: '2026-07-29'
---

# 线性 F 型稳定子群商的最小阶与四阶临界结构

## 稳定子群商

设

$$
\mathcal A=\mathcal A_R(K),
\qquad
\mathcal H=\mathcal H_R(K),
\qquad
\mathcal C=\mathcal A\mathcal A^{-1},
$$

并假设状态属于 F 型：

$$
-1\in\mathcal H,
\qquad
-1\notin\mathcal C.
$$

令

$$
T=\operatorname{Stab}_{\mathcal H}(\mathcal A),
\qquad
\overline{\mathcal H}=\mathcal H/T,
\qquad
\overline{\mathcal A}=\mathcal A/T.
$$

则有

$$
T\subseteq\mathcal A\subseteq\mathcal C,
\qquad
-1\notin T,
$$

并且 (overline{\mathcal A}) 生成 (overline{\mathcal H})、
(overline{-1}=(-1)T) 是非平凡二阶元，且

$$
|\overline{\mathcal A}|\le\frac{|\overline{\mathcal H}|}{2},
\qquad
|\overline{\mathcal H}|\ge4.
$$

若达到半密度等号，则

$$
\overline{\mathcal H}
=\overline{\mathcal A}
\sqcup\overline{-1}\,\overline{\mathcal A}.
$$

所以 (overline{\mathcal A}) 是商群中每一对反足点的一个代表集。

## 四阶商群的精确分类

若

$$
|\overline{\mathcal H}|=4,
$$

则

$$
|\overline{\mathcal A}|=2,
\qquad
\overline{\mathcal A}=\{1,g\},
\qquad
\operatorname{ord}(g)=4.
$$

因此，对 (K) 的每个素因子 (q)，其商群残数 (\bar q) 只能是 (1)、(g) 或
(g^{-1})；不能是 (g^2=-1)。此外：

* 若某个素因子的残数为 (g) 或 (g^{-1})，其在 (K) 中的指数必须为一，否则 (q^2) 的残数就是 (-1)；
* 不能有两个不同素因子给出非平凡残数，否则两个残数的乘积或两个相同残数的平方会使 (-1) 落入 (mathcal A)，或使 (mathcal A/T) 至少含三个元素；
* 因而四阶商 F 型障碍的非平凡商群支撑只能由一个指数一素因子承担，其他素因子均落在 (T) 中。

## 证明

因为 (1mid K)，有 (1\in\mathcal A)。若 (t\in T)，则

$$
t=t\cdot1\in t\mathcal A=\mathcal A,
$$

故 (T\subseteq\mathcal A)。又 (1\in\mathcal A) 给出
(mathcal A\subseteq\mathcal A\mathcal A^{-1}=\mathcal C)。所以 (-1\notin T)。

每个素因子 (q\mid K) 本身是 (K) 的除子，故 (q\bmod R\in\mathcal A)；这些残数生成
(mathcal H)，从而 (overline{\mathcal A}) 生成 (overline{\mathcal H})。

由于 (-1\notin\mathcal C)，有

$$
\mathcal A\cap(-\mathcal A)=\varnothing.
$$

商群中仍有

$$
\overline{\mathcal A}
\cap
\overline{-1}\,\overline{\mathcal A}
=\varnothing;
$$

否则存在 (a,b\in\mathcal A)、(t\in T) 使 (a=-bt)。因 (T) 稳定 (mathcal A)，
(bt\in\mathcal A)，这会与原交集为空矛盾。两集合等势，得到半密度上界。

若商群只有二阶，则 (overline{\mathcal A}) 含单位元且避开唯一非平凡元，只能是
({1})，与其生成整个商群矛盾，故商群阶至少为四。

当商群阶为四时，半密度上界给出 (|overline{\mathcal A}|\le2)。它含单位元并生成
商群，且不能含唯一二阶元，所以只能是 ({1,g})，其中 (g) 阶为四。若某个素因子
残数为 (g) 或 (g^{-1}) 且指数至少二，则其平方给出 (g^2=-1)，矛盾。若有两个不同
素因子残数非平凡，则 (overline{\mathcal A}) 同时含两个非平凡残数，或者含它们的乘积
(-1)，同样矛盾。证毕。

## 对混合终端目标的意义

这个结论把一类 F 型失败压缩为有限指数、单一商群方向的临界结构。若某个线性状态的
两块或四层分解把所有非平凡因子都推入这样的四阶商，则只需追踪一个指数一素因子及其
标签碰撞来源；任何额外的非平凡层都会立即破坏 F 型障碍并命中一般 (B) 目标。

因此，跨 (R) 的下一步可以先排除以下低复杂度分支：同一核心素数若所有候选状态都落在
四阶临界商中，则这些唯一的指数一非平凡素因子必须同时满足各自的标签差、模数差和二次
互反条件。若这些条件不能相容，就得到目标命中；若能够相容，则留下一个明确的、可递归
追踪的有限指数障碍，而不是不可描述的“密度不足”。

本卡不声称四阶商一定不存在，也不处理商群阶大于四的临界序列；它提供的是后续跨状态
证明所需的低阶障碍分类。
