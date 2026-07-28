---
kind: claim
claim_id: type-I-general-b-centered-square-spectrum
title: 一般 B 目标平方除子的中心化谱与精确障碍二分
statement: 对任意互素正整数K,R，令K的素因子q的指数为nu_q(K)。一般B目标条件存在d|K^2且d=-K模R，当且仅当-1属于中心化有限谱{积q^z_q modR:-nu_q(K)<=z_q<=nu_q(K)}。因此失败精确分为两类：-1不在素因子残数生成子群中的子群/角色障碍，或-1在该子群内但不在上述有限指数盒中的有限指数障碍。每个目标命中可由d与K^2/d的互补对规范为d<K；该结论把一般B线性选择器的目标侧障碍完全分类，但不证明不同源模数之间必有命中。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- general-b
- target-square-divisor
- divisor-residues
- finite-product
- subgroup-character
- exponent-saturation
- terminal-bridge
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 一般 \(B\) 目标平方除子的中心化谱与精确障碍二分

## 参数与中心化

令 \(R,K\) 为正整数，\((K,R)=1\)，并写

\[
K=\prod_{q\mid K}q^{\nu_q},\qquad \nu_q=\nu_q(K)\ge1. \tag{1}
\]

定义 \(K\) 的**中心化平方除子谱**与其支持子群为

\[
\mathcal C_R(K)=
\left\{
\prod_{q\mid K}q^{z_q}\pmod R:
-\nu_q\le z_q\le\nu_q
\right\}, \tag{2}
\]

\[
\mathcal H_R(K)=\left\langle q\pmod R:q\mid K\right\rangle
\le (\mathbb Z/R\mathbb Z)^\times. \tag{3}
\]

在[一般 \(B\) 线性终端选择猜想](type-I-linear-source-general-b-terminal-selector-conjecture.md)
中，\(4K=pR+1\) 自动给出 \((K,R)=1\)，而目标条件是

\[
d\mid K^2,\qquad d\equiv-K\pmod R. \tag{4}
\]

所以 (2) 的目标固定为 \(-1\)，不再随 \(K\) 改变。

## 中心化恒等式

**定理。** 在上述条件下，精确有

\[
\boxed{
\mathcal C_R(K)=
\left\{dK^{-1}\pmod R:d\mid K^2\right\}.} \tag{5}
\]

从而

\[
\boxed{
\exists\,d\mid K^2,\ d\equiv-K\pmod R
\quad\Longleftrightarrow\quad
-1\in\mathcal C_R(K).} \tag{6}
\]

**证明。** 任取 \(d\mid K^2\)，写

\[
d=\prod_{q\mid K}q^{b_q},\qquad0\le b_q\le2\nu_q.
\]

相除 \(K\) 后得到

\[
dK^{-1}\equiv\prod_{q\mid K}q^{b_q-\nu_q}\pmod R,
\qquad-\nu_q\le b_q-\nu_q\le\nu_q. \tag{7}
\]

反过来，每一组 \(z_q\in[-\nu_q,\nu_q]\) 令 \(b_q=z_q+\nu_q\)，就得到一个
\(d\mid K^2\)。故 (5) 成立；将 \(dK^{-1}\equiv-1\) 改写为
\(d\equiv-K\) 即得 (6)。证毕。

## 精确障碍二分

因为 \(\mathcal C_R(K)\subseteq\mathcal H_R(K)\)，目标失败有且只有下列两种互斥情形：

\[
\begin{array}{rcll}
-1\notin\mathcal H_R(K)
&:&\text{子群/角色障碍}, &(\mathrm{G})\\
-1\in\mathcal H_R(K)\setminus\mathcal C_R(K)
&:&\text{有限指数障碍}. &(\mathrm{F})
\end{array} \tag{8}
\]

这里 (G) 只依赖 \(K\) 的不同素因子在模 \(R\) 下的残数；(F) 还依赖每个
\(\nu_q(K)\) 的有限上界。它不是启发式分类，而是由 (5) 给出的完备析取。

更具体地，(G) 当且仅当存在一个根单位值角色

\[
\chi:(\mathbb Z/R\mathbb Z)^\times\longrightarrow\mathbb C^\times
\]

使

\[
\chi(q)=1\quad(q\mid K),\qquad\chi(-1)\ne1. \tag{9}
\]

若 \(-1\notin\mathcal H_R(K)\)，就在有限阿贝尔商群
\((\mathbb Z/R\mathbb Z)^\times/\mathcal H_R(K)\) 上取一个不湮灭 \([-1]\) 的角色，并向上拉回；
反向蕴含显然。于是“角色障碍”有了精确、可验证的定义，而不是跨不同模数的非形式化说法。

## 互补与自然定向

若 \(d\) 满足 (4)，则

\[
d'=\frac{K^2}{d} \tag{10}
\]

也满足 (4)，因为在中心化坐标中 \(dK^{-1}\equiv-1\) 的逆仍是 \(-1\)。
故 \(d,d'\) 至少一个不大于 \(K\)。当 \(R\ge3\) 且 \(4K\equiv1\pmod R\) 时，
\(d=K\) 会推出 \(K\equiv-K\pmod R\)，即 \(R\mid2\)，不可能；因而可取

\[
d<K. \tag{11}
\]

这与一般 \(B\) 正规化中交换 \(B,H\) 完全一致，故中心化没有放松目标的自然缺口条件。

## 对证明计划的含义

对一个线性源状态，(8) 已经完整说明目标侧为什么失败；但它**没有**比较不同源状态的
\(R\)。因此全称选择引理尚差的内容可以精确表述为：对同一个普通 Type II 尾遗漏素数，
不能让所有线性源状态都落在 (G) 或 (F) 的失败支中。任意“跨源角色相容”论证必须先给出
不同单位群之间的共同商、导子或显式拉回；仅罗列不同 \(R\) 上的角色并不能构成定理。

对 \(p=878089\) 的完整 24 个线性源模数，这个分类的直接审计见
[一般 \(B\) 中心化谱剖面](type-I-linear-general-b-obstruction-profile-878089.md)。
