---
kind: claim
claim_id: type-I-linear-two-adic-kneser-terminal-selector
title: 线性二残数逃逸与两块 Kneser 密度的组合终端选择器
statement: 设线性源 p=a+s+asR、s 为奇数、R=3 mod4，并令 K=(pR+1)/4。若某端点 t∈{a,s} 满足 t=3 mod4 且 -1∈<2 mod R>，则 -1∈H_R(K)。对 K=γL 的任意两块分解，若 X=A_R(γ)、Y=A_R(L)、T=Stab_H(XY) 满足 |XT|+|YT|-|T|>|H_R(K)|/2，则 -1∈C_R(K)，从而存在 d|K²、d≤K、d=-K modR；结合 E=sR+1 得到原混合终端选择器的偶因子分支。素数 R=3 mod8 时，-1∈<2 modR> 自动成立。该组合判据只覆盖满足二残数与密度条件的线性状态，不是全称证明。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- two-adic
- subgroup-escape
- Kneser-theorem
- two-block
- general-b
- terminal-bridge
- mixed-selector
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-terminal-selector-context
- paper: grynkiewicz_marchan_ordaz2009
  locator: Theorem C
  role: Kneser-product-set-input
visibility: public
last_checked: '2026-07-29'
---

# 线性二残数逃逸与两块 Kneser 密度的组合终端选择器

## 条件

设核心素数的线性源状态为

$$
p=a+s+asR,
\qquad s\text{ 为奇数},
\qquad R\equiv3\pmod4,
\qquad K=\frac{pR+1}{4}. \tag{1}
$$

假设一个端点 (t\in\{a,s\}) 满足

$$
t\equiv3\pmod4,
\qquad -1\in\langle2\bmod R\rangle. \tag{2}
$$

取该线性状态的任意两块分解 (K=\gamma L)，并定义

$$
\mathscr H=\mathcal H_R(K),
\qquad X=\mathcal A_R(\gamma),
\qquad Y=\mathcal A_R(L),
\qquad T=\operatorname{Stab}_{\mathscr H}(XY). \tag{3}
$$

要求两块在稳定子群商中违反半密度必要条件：

$$
|XT|+|YT|-|T|>\frac{|\mathscr H|}{2}. \tag{4}
$$

## 结论

在 (1)--(4) 下，

$$
-1\in\mathcal C_R(K). \tag{5}
$$

因此存在

$$
d\mid K^2,
\qquad d\le K,
\qquad d\equiv-K\pmod R, \tag{6}
$$

可恢复一般 (B) 的 Type I 正规形。另一方面，线性源本身给出

$$
E_0=sR+1,
\qquad E_0\mid4K,
\qquad E_0\equiv1\pmod R,
\qquad 2\mid E_0,
\qquad E_0\le4K-2R. \tag{7}
$$

所以该状态同时满足目标混合终端选择器的偶因子分支。

当 (R) 是素数且 (R\equiv3\pmod8) 时，Euler 判据给出

$$
2^{(R-1)/2}\equiv-1\pmod R,
$$

故 (2) 的第二项自动成立。

## 证明

由 (t\equiv3\pmod4)、(R\equiv3\pmod4)，两端点块均为偶数。置

$$
G=\frac{tR+1}{2},
\qquad H'=\frac{uR+1}{2},
$$

其中 (u) 是另一个端点，则 (G\mid K)，且

$$
2G=tR+1\equiv1\pmod R.
$$

所以 (G\equiv2^{-1}\pmod R)。因 (G\) 是 (K) 的除子，
(G) 及 (K/G) 给出中心化平方除子谱中的 (2^{-1}) 与 (2)，从而

$$
2\in\mathscr H. \tag{8}
$$

结合 (2)，得到 (-1\in\langle2\rangle\subseteq\mathscr H)。因此该状态不可能是
G 型；若仍未命中，则它属于 F 型。

对 F 型状态，上一条[两块 Kneser 必要条件](type-I-linear-two-block-kneser-f-obstruction.md)
给出

$$
|XT|+|YT|-|T|\le\frac{|\mathscr H|}{2},
$$

这与 (4) 矛盾。因此未命中不可能发生，得到 (5)。由中心化谱定义，取互补因子可令
(d\le K)，得到 (6)。最后 (7) 是线性源的因式分解

$$
4K=(aR+1)(sR+1)
$$

与 (s,R) 的奇偶性直接推出的偶终端桥条件。证毕。

## 研究边界

该组合器把一个局部状态的失败分成两层可证伪条件：

1. 没有端点 (t\equiv3\pmod4)，或 (-1\notin\langle2\rangle)，二残数逃逸不能排除 G 型；
2. 已排除 G 型但 (4) 失败，说明两块除子谱在稳定子群商中仍有半密度缺口。

因此它没有证明每个普通 Type II 遗漏都存在合适的线性状态。全称推进的最小目标是：
对每个遗漏素数找到一个满足 (2) 的线性状态，并证明其两块稳定子群商违反 (4)；若
某状态的 (T) 非平凡，还需用跨模数标签块的共享因子结构解释该周期，而不能把它当作
随机密度损失。

这条组合器也不覆盖需要四阶或更高阶角色的 G 型状态，不能替代二次互反拉回和高阶角色
分析。它的价值在于：一旦条件 (2)、(4) 同时得到，目标端平方除子与源端偶因子会在同一
证明步骤中闭合，无需再额外选择一个递降源。
