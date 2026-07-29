---
kind: claim
claim_id: type-I-normal-even-source-parity-truncated-density-criterion
title: Type I 偶源桥的二进截断半密度判据
statement: 设 L=2K、R 为奇数且 gcd(L,R)=1，令 ell=v_2(L)，D_R^par(L)={d modR:d|L、v_2(d)<ell}，H_R(L) 为 L 的素因子残数生成子群。若 2∈H_R(L) 且 2|D_R^par(L)|>|H_R(L)|，则存在互素 a,b|L，a≡2b modR，且 E=La/b 为偶数、E|L^2、E≡2L modR。对 Type I 情形 L=2K、4K≡1 modR，E≡1 modR；若该碰撞可取 a<2b，则还满足 E≤2L-2R。半密度本身仍不保证大小方向。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- terminal-bridge
- even-source
- parity
- divisor-residues
- finite-product
- density
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-terminal-selector-context
visibility: public
last_checked: '2026-07-29'
---

# Type I 偶源桥的二进截断半密度判据

## 截断残数集

设 \(L=2K\)，\(R\) 为奇数且 \((L,R)=1\)，并令

\[
\ell=v_2(L)\ge1.
\]

定义排除最高二进层的除子残数集

\[
\mathcal D_R^{\mathrm{par}}(L)
=\{d\bmod R:d\mid L,\ v_2(d)<\ell\}, \tag{1}
\]

以及由 \(L\) 的素因子残数生成的子群

\[
\mathcal H_R(L)=\langle q\bmod R:q\mid L\rangle. \tag{2}
\]

这里的截断不是要求除子为奇数；它保留所有低于 \(L\) 的最高二进赋值层，因此在碰撞约化后
仍能控制分母的二进指数。

## 判据

若

\[
2\in\mathcal H_R(L),
\qquad
2|\mathcal D_R^{\mathrm{par}}(L)|
>
|\mathcal H_R(L)|, \tag{3}
\]

则存在互素正整数 \(a,b\mid L\)，满足

\[
a\equiv2b\pmod R, \qquad v_2(b)<\ell. \tag{4}
\]

令

\[
E=L\frac ab. \tag{5}
\]

则

\[
E\mid L^2,\qquad E\equiv2L\pmod R,\qquad 2\mid E. \tag{6}
\]

在 Type I 情形 \(L=2K\)、\(4K\equiv1\pmod R\) 时，(6) 的同余化为

\[
E\mid4K^2,\qquad E\equiv1\pmod R,\qquad 2\mid E. \tag{7}
\]

若同一碰撞的约化代表还满足

\[
a<2b, \tag{8}
\]

则自动有

\[
E\le2L-2R=4K-2R. \tag{9}
\]

## 证明

由 \(2\in\mathcal H_R(L)\)，乘法平移
\(2\mathcal D_R^{\mathrm{par}}(L)\) 仍位于同一个子群，且与原集合等势。条件 (3) 的
鸽巢原理给出 \(u,v\mid L\)，其中

\[
v_2(u),v_2(v)<\ell,\qquad u\equiv2v\pmod R. \tag{10}
\]

令 \(g=(u,v)\)、\(a=u/g\)、\(b=v/g\)。则 \(a,b\mid L\)、\((a,b)=1\) 且
\(a\equiv2b\pmod R\)。由于

\[
v_2(b)=v_2(v)-v_2(g)\le v_2(v)<\ell, \tag{11}
\]

而 \(v_2(L)=\ell\)，得到

\[
v_2(E)=\ell+v_2(a)-v_2(b)
\ge\ell-v_2(b)\ge1. \tag{12}
\]

所以 \(E\) 为偶数。互素性和 \(a,b\mid L\) 给出

\[
\frac{L^2}{E}=\frac{Lb}{a}\in\mathbb Z, \tag{13}
\]

从而 \(E\mid L^2\)。又 \((L,R)=1\)，由 \(a\equiv2b\pmod R\) 得

\[
E\equiv L\frac ab\equiv2L\pmod R. \tag{14}
\]

这证明 (6)--(7)。最后若 (8) 成立，写
\(2b-a=qR\)。由于 \(q\ge1\)，且 \(v_2(b)<\ell=v_2(L)\) 与 \(b\mid L\) 一起给出
\(b\le L/2\)，故 \(Lq\ge2b\)，于是

\[
2L-E=L\frac{2b-a}{b}=L\frac{qR}{b}\ge2R. \tag{15}
\]

一般碰撞未必满足 \(a<2b\)，故大小方向不能从 (3) 单独推出。证毕。

## 与普通半密度判据的关系

普通判据对全部 \(\mathcal D_R(L)\) 做半密度计数，但可能选到分母含有 \(L\) 的完整
二进因子，从而 \(E\) 变奇。本卡把该失败层从计数域中预先删除，换取自动偶性；代价是
半密度条件更强。它与[比二除子残数的半密度入口引理](type-I-normal-even-source-ratio-two-density-criterion.md)
互补：

\[
\text{截断半密度}
\Longrightarrow
\text{偶性闭合}
\quad+\quad
\text{另检 }a<2b\text{ 的大小方向}. \tag{16}
\]

因此它仍不是原混合终端选择引理的证明。下一步的精确子目标是证明某类线性源状态的
\(\mathcal D_R^{\mathrm{par}}(2K)\) 在 \(\mathcal H_R(2K)\) 中达到半密度，并同时提供一个小侧
碰撞；若该条件失败，则需要转入另一模数或严格递降。
