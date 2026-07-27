---
kind: claim
claim_id: dyachenko-2025-lattice-gap
title: Dyachenko 2025 的对角格窗口命中论证有缺口
statement: Theorem 9.21 的无条件存在性依赖 Proposition 9.25，但其证明错误地用同一个对角平移参数命中两个独立选取的坐标。
claim_status: claimed_with_gap
topics:
- proof-audit
- affine-lattice
- critical-gap
sources:
- dyachenko2025
visibility: public
last_checked: '2026-07-23'
---

# Dyachenko 2025 的对角格窗口命中论证有缺口

## 结论

Theorem 9.21 的无条件存在性依赖 Proposition 9.25，但其证明错误地用同一个对角平移参数命中两个独立选取的坐标。

## 推理与来源

若 p0=(u0,v0) 且 w=(d',d')，由 u* 决定 m=(u*-u0)/d' 后，第二坐标是 v0+md'；它一般不等于独立选取的 v*。同时 Lemma 9.24 把一个秩一对角陪集写成所有固定双坐标剩余类的格点，等号无一般依据。

- Dyachenko 2025, Lemmas 9.22-9.24 and Proposition 9.25.
- Theorem 9.21 explicitly invokes this window-hitting step.

## 显式反例

Proposition 9.25 按其陈述本身就是假的。取

\[
g=2,\qquad b'=c'=1.
\]

则其前提中的互素条件都成立，且

\[
\alpha=\gcd(g,b'+c')=2,\qquad d'=g/\alpha=1,
\]

而相应格为

\[
L=\{(u,v)\in\mathbb Z^2:u+v\equiv0\pmod2\}.
\]

取半开单位矩形

\[
R=[0,1)\times[1,2).
\]

它满足命题要求的 \(H=W=d'=1\)，但唯一的整数点 \((0,1)\) 不属于
\(L\)。故 \(L\cap R=\varnothing\)，直接否定 Proposition 9.25 的结论。

更一般地，对固定 \(p_0=(u_0,v_0)\) 的对角陪集
\(p_0+\mathbb Z(d',d')\)，矩形命中的充要条件是两个整数区间

\[
\left[\left\lceil\frac{x_0-u_0}{d'}\right\rceil,
      \left\lceil\frac{x_0+H-u_0}{d'}\right\rceil-1\right]
\quad\text{与}\quad
\left[\left\lceil\frac{y_0-v_0}{d'}\right\rceil,
      \left\lceil\frac{y_0+W-v_0}{d'}\right\rceil-1\right]
\]

相交。分别有长度至少 \(d'\) 只保证两个区间各自非空，并不保证它们有共同的平移参数。
一个有效但较弱的通用格命中界是 \(H\ge g,\ W\ge1\)：固定任一
\(v\) 后，因 \(b'\) 模 \(g\) 可逆，线性同余唯一确定 \(u\pmod g\)。这也说明
把界从 \(g\) 无条件降到 \(g/\alpha\) 需要新的、未给出的几何论证。

## 边界

这不否定论文中的所有代数恒等式或算法样例，但阻断了对每个 P 的全称存在性。
