---
kind: claim
claim_id: type-I-private-quotient-box-saturation
title: Type I 多私有因子商群指数盒的饱和判据
statement: 设 x=E 乘积 r_i^{b_i}，其中 r_i 为互异私有素数且 gcd(E,乘积 r_i)=1。若固定因子的平方除子残数 J=Pi_m(E^2) 已是子群，令 H=<J,r_1,...,r_k>、Q=H/J，并令 S_i={r_i^j J:0<=j<=2b_i}。则 x^2 的除子残数在 Q 中恰为 S_1...S_k；若该乘积集等于 Q 且目标 t=-1/4 属于 H，则必有 Type I 目标证书。更一般地，令 T 为乘积集稳定子群，Kneser 不等式 sum_i |S_iT|-(k-1)|T| >= |Q| 是饱和的充分条件。该判据严格推广一私有因子的三余类饱和，不证明全称混合终端选择器。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- divisor-residues
- private-factors
- quotient-box
- finite-exponent
- Kneser-theorem
- saturation
- obstruction
- mixed-selector
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-divisor-criterion
- paper: grynkiewicz_marchan_ordaz2009
  locator: Theorem C
  role: product-set-growth-context
visibility: public
last_checked: '2026-07-29'
---

# Type I 多私有因子商群指数盒的饱和判据

## 设置

令 \(m\equiv3\pmod4\) 为合法缺口，取

$$
x=E\prod_{i=1}^{k}r_i^{b_i},
\qquad
\gcd\left(E,\prod_i r_i\right)=1, \tag{1}
$$

其中 \(r_i\) 是互异素数，且所有数都与 \(m\) 互素。对正整数 \(N\) 写

$$
\Pi_m(N)=\{d\bmod m:d\mid N\}. \tag{2}
$$

假设固定因子的平方除子谱

$$
J=\Pi_m(E^2) \tag{3}
$$

已经是 \((\mathbb Z/m\mathbb Z)^\times\) 的子群。令

$$
H=\langle J,r_1,\ldots,r_k\rangle,
\qquad
Q=H/J, \tag{4}
$$

并记 \(\bar r_i=r_iJ\in Q\)。

对每个私有方向定义有限指数段

$$
S_i=\{\bar r_i^{\,j}:0\le j\le2b_i\}\subseteq Q,
\qquad
B=S_1S_2\cdots S_k. \tag{5}
$$

这里 \(B\) 是商群中的私有指数盒投影；它不要求各 \(S_i\) 或各 \(r_i\) 互素。

## 精确饱和定理

有精确的商群投影恒等式

$$
\boxed{
\Pi_m(x^2)\text{ 在 }Q\text{ 中的像}=B.
} \tag{6}
$$

特别地，若

$$
B=Q \tag{7}
$$

且目标残数

$$
t=-4^{-1}\pmod m
$$

属于 \(H\)，则

$$
t\in\Pi_m(x^2), \tag{8}
$$

从而存在 Type I 目标平方除子。目标除子取互补因子后可按标准正规化恢复
\(x=ABC\)、\(d=B^2C\) 的 Type I 证书。

因此，任意 Type I 状态的未命中必须满足至少一个精确缺口：

$$
t\notin H
\quad\text{或}\quad
\bar t\notin B,\qquad
\Delta_Q=|Q|-|B|>0. \tag{9}
$$

其中 \(\Delta_Q\) 是私有指数盒在稳定固定层之后的商群缺陷。

## Kneser 饱和充分条件

令

$$
T=\operatorname{Stab}_Q(B).
$$

多项积集 Kneser 不等式给出

$$
|B|
\ge
\sum_{i=1}^{k}|S_iT|-(k-1)|T|. \tag{10}
$$

所以可检验的饱和条件是

$$
\boxed{
\sum_{i=1}^{k}|S_iT|-(k-1)|T|
\ge |Q|
\Longrightarrow B=Q.
} \tag{11}
$$

在 \(T=\{1\}\) 的非周期情形，这简化为

$$
\sum_{i=1}^{k}|S_i|\ge |Q|+k-1. \tag{12}
$$

每个方向的大小可直接由商阶计算：

$$
|S_i|=\min\{2b_i+1,\operatorname{ord}_Q(\bar r_i)\}. \tag{13}
$$

因此 (11)--(13) 把“多个私有因子是否足以填满缺口”转化为有限的阶和预算，而不是
枚举所有 \(x^2\) 除子。

## 已有三余类判据的恢复

当 \(k=1\)、\(b_1=1\) 时，

$$
S_1=\{1,\bar r,\bar r^2\}.
$$

若 \(\operatorname{ord}_Q(\bar r)\le3\)，则 \(S_1=Q\)，(7)--(8) 恢复已有的
一私有因子三余类饱和判据。若固定层未饱和，则本定理不适用，正好保留此前的
“碰撞因子指数不足”分支。

## 证明

任意 \(d\mid x^2\) 可唯一写成

$$
d=d_E\prod_{i=1}^{k}r_i^{j_i},
\qquad
d_E\mid E^2,\quad0\le j_i\le2b_i. \tag{14}
$$

将 (14) 对 \(m\) 取残数并投影到 \(Q\)。固定部分 \(d_E\) 的残数属于 \(J\)，
而私有部分的所有可能残数恰为各 \(S_i\) 的乘积，故像包含于 \(B\)。
反向地，对任意 \(j_i\) 和任意 \(d_E\mid E^2\)，式 (14) 本身就是 \(x^2\) 的除子，
所以每个 \(B\) 中的类都被实现，得到 (6)。

若 \(B=Q\)，则 \(t\in H\) 的商类 \(\bar t\) 属于 \(B\)，与某个固定层残数相乘
即可得到 \(t\in\Pi_m(x^2)\)，证明 (8)。Kneser 的多因子形式直接应用于
\(S_1,\ldots,S_k\) 得到 (10)；若右端达到 \(|Q|\)，而 \(B\subseteq Q\)，则
必有 \(B=Q\)。式 (12)--(13) 是相应的无周期化简和循环子群指数段大小公式。证毕。

## 对混合终端目标的作用

这张卡把 Type I 有限指数分支拆成两个可分别证明的对象：

1. **支撑逃逸**：证明 \(t=-1/4\) 属于固定层与私有方向生成的 \(H\)；
2. **商群饱和**：证明私有指数盒 \(B\) 填满目标所在的商群，或至少包含 \(\bar t\)。

在线性源的混合终端问题中，支撑逃逸可由二残数注入、二次互反拉回或高阶角色分析提供；
一旦同一正规形的目标侧满足 (8)，再结合已有的偶终端桥判据即可检查
\(E\equiv1\pmod R\)、\(E\le4K-2R\) 和偶性。因而后续真正的全称缺口被压缩为：
沿可达线性源状态，固定碰撞层是否最终饱和，或私有指数盒缺陷是否能转成严格递降。

本卡不声称 \(\Delta_Q\) 必为零，也不构造跨 \(R\) 的下降势函数；它是多私有因子有限指数
分支的精确结构定理。
