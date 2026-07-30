---
kind: claim
claim_id: type-I-target-fiber-coordinate-quotient-floor
title: 目标纤维单坐标缺陷的商群与关系格精确公式
statement: 设有限交换群 H 由 g_1,...,g_r 生成，目标 y 属于 H，F_y 是 y 的完整整数指数纤维。固定坐标 j 并商掉其余生成元所得子群 T_j，则 H/T_j 是由 g_jT_j 生成的循环群；若其阶为 o_j、目标类为 kappa_j，则第 j 坐标的完整投影恰为 kappa_j+o_j Z。因此选择不变盒外下限等于该陪集到零的距离减去指数界后的正部，也等于完整 Pareto 前沿的第 j 坐标最小值；o_j 同时等于完整关系格任一整数基的第 j 行 gcd。
claim_status: established
proof_provenance: repository_derivation
review_status: independent_review
depends_on:
  - type-I-f-relation-lattice-certificate-reconstruction
  - type-I-f-overflow-lower-modulus-weighted-cost-interface
topics:
  - type-I
  - F-state
  - target-fiber
  - finite-abelian-groups
  - quotient-group
  - relation-lattice
  - Pareto
  - selection-invariant
  - proof-program
sources:
  - claim: type-I-f-relation-lattice-certificate-reconstruction
    role: complete-affine-relation-lattice-interface
  - claim: type-I-f-overflow-lower-modulus-weighted-cost-interface
    role: complete-fiber-overflow-interface
visibility: public
last_checked: '2026-07-30'
---

# 目标纤维单坐标缺陷的商群与关系格精确公式

## 定理

设

\[
H=\langle g_1,\ldots,g_r\rangle
\]

是有限交换群，且

\[
\phi:\mathbb Z^r\longrightarrow H,
\qquad
\phi(z)=\prod_{i=1}^r g_i^{z_i}.
\]

对目标 \(y\in H\)，令

\[
F_y=\phi^{-1}(y),
\qquad
\Lambda=\ker\phi.
\]

固定坐标 \(j\)，并定义

\[
T_j=\langle g_i:i\ne j\rangle,
\qquad
Q_j=H/T_j,
\qquad
o_j=\operatorname{ord}_{Q_j}(g_jT_j).
\tag{1}
\]

群 \(Q_j\) 由 \(g_jT_j\) 生成，故是阶为 \(o_j\) 的循环群。存在唯一的
\(\kappa_j\in\mathbb Z/o_j\mathbb Z\) 满足

\[
yT_j=(g_jT_j)^{\kappa_j}.
\tag{2}
\]

目标纤维的第 \(j\) 坐标投影恰为

\[
\boxed{\pi_j(F_y)=\kappa_j+o_j\mathbb Z.}
\tag{3}
\]

给定指数界 \(\nu_j\ge0\)，置

\[
e_j(z)=(|z_j|-\nu_j)_+,
\qquad
\delta_j=\operatorname{dist}(0,\kappa_j+o_j\mathbb Z).
\]

则完整目标纤维上的选择不变单坐标缺陷为

\[
\boxed{
\mu_j:=\min_{z\in F_y}e_j(z)
=(\delta_j-\nu_j)_+.}
\tag{4}
\]

## 商群投影的证明

若 \(z\in F_y\)，在 \(Q_j\) 中其余生成元全部消失，故

\[
(g_jT_j)^{z_j}=yT_j=(g_jT_j)^{\kappa_j}.
\]

于是 \(z_j\equiv\kappa_j\pmod{o_j}\)。反之，若
\(n\equiv\kappa_j\pmod{o_j}\)，则 \(yg_j^{-n}\in T_j\)。按 \(T_j\) 的定义，
存在整数 \(z_i\ (i\ne j)\) 使

\[
yg_j^{-n}=\prod_{i\ne j}g_i^{z_i}.
\]

取 \(z_j=n\) 即得 \(z\in F_y\)，所以 (3) 是等式而非单向包含。
式 (4) 随即来自 (3) 以及函数 \(x\mapsto(x-\nu_j)_+\) 在
\(\mathbb R_{\ge0}\) 上的单调性。

## 与关系格行 gcd 的等价

任取 \(z_0\in F_y\)，则 \(F_y=z_0+\Lambda\)。关系格在第 \(j\) 坐标的投影满足

\[
\pi_j(\Lambda)
=\{n\in\mathbb Z:g_j^n\in T_j\}
=o_j\mathbb Z.
\tag{5}
\]

若 \(b_1,\ldots,b_r\) 是完整关系格 \(\Lambda\) 的任一整数基，并把基向量作为矩阵列，
则

\[
\pi_j(\Lambda)
=\langle (b_1)_j,\ldots,(b_r)_j\rangle_{\mathbb Z}
=d_j\mathbb Z,
\]

其中

\[
d_j=\gcd\bigl(|(b_1)_j|,\ldots,|(b_r)_j|\bigr).
\]

结合 (5) 得

\[
\boxed{d_j=o_j,\qquad z_{0,j}\equiv\kappa_j\pmod{o_j}.}
\tag{6}
\]

这里必须使用完整关系格的整数基或完整生成集；若输入只生成真子格，行 gcd 可能被错误
放大。仿射特解 \(z_0\) 也不能参与 gcd。

## 与完整 Pareto 前沿的等价

令

\[
\mathcal O_y=\{e(z):z\in F_y\}\subseteq\mathbb Z_{\ge0}^r,
\qquad
\mathcal P_y=\min_{\preceq}\mathcal O_y.
\]

则

\[
\boxed{\mu_j=\min_{e\in\mathcal P_y}e_j.}
\tag{7}
\]

确实，取 \(z^*\) 使 \(e_j(z^*)=\mu_j\)，并置 \(v=e(z^*)\)。有限集合

\[
\{u\in\mathcal O_y:u\preceq v\}
\]

有极小元 \(u^*\)。若 \(u^*\) 不是 \(\mathcal O_y\) 的全局 Pareto 极小元，任一严格
支配它的点仍在这个有限集合中，矛盾。因此 \(u^*\in\mathcal P_y\)，且

\[
\mu_j\le u_j^*\le v_j=\mu_j,
\]

从而得到 (7)。这里必须使用完整 Pareto 前沿；截断搜索未必包含实现单坐标最小值的点。

若第 \(j\) 坐标另有数值容量 \(h_j\ge0\)，则扩展界下的坐标缺陷为

\[
\min_{z\in F_y}(|z_j|-\nu_j-h_j)_+
=(\mu_j-h_j)_+.
\tag{8}
\]

所以

\[
\forall z\in F_y,\ e_j(z)>h_j
\quad\Longleftrightarrow\quad
\mu_j>h_j.
\tag{9}
\]

式 (8)--(9) 只是精确的数值比较。若要把 \(h_j\) 解释成真实载体容量，还必须另证
overflow-to-carrier 映射及不同坐标容量的兼容性。

## 量词与 Fourier 边界

单个表示满足 \(e_j(z)>h_j\) 只给出一个坏选择；固定坐标被迫超载要求 (9) 中对完整
目标纤维的全称量化。另一方面，

\[
\forall z\in F_y\ \exists j:\ e_j(z)>h_j
\]

只说明扩展矩形盒与目标纤维不交，并不推出

\[
\exists j\ \forall z\in F_y:\ e_j(z)>h_j.
\]

因此联合障碍不能一般地压缩为某一个私有素数坐标。

最后，不能在已有严格正权的 Fourier 生成函数中直接令 \(w_j=1\)、其余权为零来证明
(4)：这会把其余形式变量置为 1，无限目标纤维上的系数和通常不再是合法形式幂级数。
商群投影给出了不依赖这种零权极限的有限证明。

若 \(y\notin H\)，则 \(F_y=\varnothing\)，此时应把缺陷约定为 \(+\infty\)，而
\(\kappa_j\) 不存在；本定理的有限公式只在 \(y\in H\) 的 F/hit 分支使用。
