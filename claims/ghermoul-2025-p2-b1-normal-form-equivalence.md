---
kind: claim
claim_id: ghermoul-2025-p2-b1-normal-form-equivalence
title: Ghermoul 第二多项式族与 B 等于一 Type I 正规形完全等价
statement: 对正整数 x,y,z，令 q=x(4yz-z-1)-yz、p=4q+1。令 m=4x-1、R=4y-1、A=z、B=1、C=4xy-x-y、H=zR-1、K=CH，则 mR=4C+1、p=4ABC-m 且 4K=pR+1，故 p2 给出 B=1 Type I 正规形。反过来，每张 B=1 自然正规形唯一由 x=(m+1)/4、y=(R+1)/4、z=A 恢复，且 (p-1)/4=p2(x,y,z)。因此 p2 对核心 q=6c 的全称覆盖等价于在核心素数上选择一张 B=1 Type I 正规形；它本身不选择偶终端因子，故不能单独推出混合终端选择引理。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- literature-audit
- polynomial-family
- type-I
- b1
- normal-form
- certificate-selector
- terminal-bridge
sources:
- paper: ghermoul2025
  locator: Equations (5), (19), (26)--(29)
  role: polynomial-family-source
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# Ghermoul 第二多项式族与 \(B=1\) Type I 正规形完全等价

## 前向映射

令 \(x,y,z\) 为正整数，并写 Ghermoul 的第二族为

\[
q=p_2(x,y,z)=x(4yz-z-1)-yz,\qquad p=4q+1. \tag{1}
\]

定义

\[
\begin{aligned}
m&=4x-1, & R&=4y-1, & A&=z,\\
B&=1, & C&=4xy-x-y, & H&=zR-1.
\end{aligned} \tag{2}
\]

则

\[
C=xR-y,\qquad
mR=(4x-1)(4y-1)=4C+1. \tag{3}
\]

又由 (1)，

\[
q=zC-x,\qquad
p=4zC-(4x-1)=4ABC-m. \tag{4}
\]

并且

\[
K=CH,\qquad
4K=4C(zR-1)=pR+1. \tag{5}
\]

所以 (2) 恰是一张 \(B=1\) Type I 自然正规形。其三个分母是

\[
AC=zC,\qquad ACH=zCH,\qquad pK=pCH, \tag{6}
\]

这正与该论文在第二族给出的显式分母相同。

## 反向映射与唯一性

反过来，设给定一张 \(B=1\) 自然正规形

\[
mR=4C+1,\qquad p=4AC-m,\qquad H=AR-1. \tag{7}
\]

由于 \(m\equiv R\equiv3\pmod4\)，唯一写为

\[
x=\frac{m+1}{4},\qquad
y=\frac{R+1}{4},\qquad
z=A. \tag{8}
\]

从 (7) 恢复

\[
C=\frac{mR-1}{4}=4xy-x-y. \tag{9}
\]

于是

\[
\frac{p-1}{4}=AC-x=z(4xy-x-y)-x
=x(4yz-z-1)-yz=p_2(x,y,z). \tag{10}
\]

因此 (2) 与 (8) 互为逆，给出该多项式族和全部 \(B=1\) 自然正规形之间的精确
坐标等价，而不只是一个充分构造。

## 对核心残余的翻译

若 \(p=24c+1\)，则 \(q=(p-1)/4=6c\)。所以 Ghermoul 预印本中尚未证明的
\(p_2\) 覆盖在这个剩余类上的内容，精确等价于：

\[
\text{每个核心素数是否存在一张 \(B=1\) Type I 正规形？} \tag{11}
\]

这比本项目的混合终端选择引理弱。后者还必须选择偶数 \(E\) 满足

\[
E\mid4K^2,\qquad E\equiv1\pmod R,\qquad E\le4K-2R, \tag{12}
\]

并给出可提升的严格源。式 (2)--(10) 只构造目标证书；它没有指定 \(E\)，也没有
证明该正规形属于任何已有的终端桥或严格递降族。

故这个翻译把该预印本纳入当前路线时，不能把“第二族在核心类上覆盖”当成已证结论，更
不能把它误作混合终端选择引理的证明。
