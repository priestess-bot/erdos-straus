---
kind: claim
claim_id: type-I-target-fiber-fourier-overflow-generating-function
title: 目标纤维溢出的精确 Fourier 生成函数
statement: 对有限阿贝尔群中的生成元、目标元和有限指数预算，目标纤维逐坐标盒外量的计数生成函数等于一个显式的有限特征平均。其零函数、常数项和最小支撑分别精确判定 G 型不可达、F-box 命中和 F-box miss 的 Pareto 极小溢出；任一公共正整数权下的最小溢出价格等于相应一元特化的消失阶。该证书不依赖 Smith 原像或关系格基的选择。
claim_status: established
proof_provenance: repository_derivation
review_status: independent_review
depends_on:
  - type-I-f-overflow-lower-modulus-weighted-cost-interface
  - type-I-f-relation-lattice-certificate-reconstruction
topics:
- type-I
- F-state
- G-state
- Fourier
- relation-lattice
- generating-function
- overflow
- Pareto
- capacity-interface
sources:
- claim: type-I-f-overflow-lower-modulus-weighted-cost-interface
  role: overflow-and-weighted-cost-definition
- claim: type-I-f-relation-lattice-certificate-reconstruction
  role: target-fiber-lattice-input
visibility: public
last_checked: '2026-07-30'
---

# 目标纤维溢出的精确 Fourier 生成函数

## 定理

设 \(G\) 是有限阿贝尔群，\(g_1,\ldots,g_r\in G\)，目标为 \(y\in G\)，并给定
预算 \(\nu_i\in\mathbb Z_{\ge0}\)。记

\[
\phi(z)=\prod_{i=1}^r g_i^{z_i},\qquad
\operatorname{ov}_\nu(z)_i=(|z_i|-\nu_i)_+.
\]

对每个特征 \(\chi\in\widehat G\)，令
\(\lambda_{i,\chi}=\chi(g_i)\)，并在形式幂级数环中定义

\[
P_{i,\chi}(T_i)
=\sum_{n=-\nu_i}^{\nu_i}\lambda_{i,\chi}^{n}
+\sum_{e\ge1}
\left(
\lambda_{i,\chi}^{\nu_i+e}
+\lambda_{i,\chi}^{-\nu_i-e}
\right)T_i^e.
\tag{1}
\]

它也可写成显式有理形式

\[
P_{i,\chi}(T_i)
=S_{\nu_i}(\lambda_{i,\chi})
+\frac{T_i\lambda_{i,\chi}^{\nu_i+1}}
       {1-T_i\lambda_{i,\chi}}
+\frac{T_i\lambda_{i,\chi}^{-\nu_i-1}}
       {1-T_i\lambda_{i,\chi}^{-1}},
\tag{2}
\]

其中 \(S_\nu(\lambda)=\sum_{n=-\nu}^{\nu}\lambda^n\)。定义目标纤维生成函数

\[
\mathcal F_y(\mathbf T)
=\frac1{|G|}\sum_{\chi\in\widehat G}
\overline{\chi(y)}\prod_{i=1}^rP_{i,\chi}(T_i).
\tag{3}
\]

则对每个 \(\mathbf e\in\mathbb Z_{\ge0}^r\)，有精确计数恒等式

\[
\boxed{
[\mathbf T^{\mathbf e}]\mathcal F_y
=\#\left\{
z\in\mathbb Z^r:
\phi(z)=y,
\ \operatorname{ov}_\nu(z)=\mathbf e
\right\}.}
\tag{4}
\]

特别地，(3) 的所有系数都是非负整数，而不是可能发生复数抵消的近似指标。

## 证明

固定 \(i\)。若盒外量为零，则允许的指数恰为
\(-\nu_i\le z_i\le\nu_i\)，它们给出 (1) 的常数项。若盒外量为
\(e_i\ge1\)，则只有

\[
z_i=\nu_i+e_i
\quad\text{或}\quad
z_i=-\nu_i-e_i,
\]

恰好给出 \(T_i^{e_i}\) 的两个项。因此，乘积
\(\prod_iP_{i,\chi}(T_i)\) 中 \(\mathbf T^{\mathbf e}\) 的系数是

\[
\sum_{\operatorname{ov}_\nu(z)=\mathbf e}\chi(\phi(z)).
\]

代入 (3) 并交换有限系数和有限特征和，再使用有限阿贝尔群的特征正交关系

\[
\frac1{|G|}\sum_{\chi\in\widehat G}
\overline{\chi(y)}\chi(x)
=\mathbf 1_{x=y},
\]

即得 (4)。式 (2) 只是对 (1) 中两个几何级数求和；其分母常数项为 1，因而也可
合法地解释为形式幂级数。证毕。

## G、盒命中与 Pareto 边界的统一判据

令 \(H=\langle g_1,\ldots,g_r\rangle\)。由 (4) 立即得到：

\[
\begin{aligned}
\mathcal F_y\equiv0
&\Longleftrightarrow y\notin H,\\
[\mathbf T^{\mathbf0}]\mathcal F_y>0
&\Longleftrightarrow
\phi^{-1}(y)\cap\prod_i[-\nu_i,\nu_i]\ne\varnothing.
\end{aligned}
\tag{5}
\]

所以零函数是精确的 G 型不可达证书，正常数项是有限盒命中证书；若生成函数非零但
常数项为零，则恰为 F-box miss。并且

\[
\min_{\preceq}\operatorname{supp}(\mathcal F_y)
=\operatorname{Pareto}_\nu(\phi^{-1}(y)),
\tag{6}
\]

即生成函数的 Newton 支撑边界正是所有不可支配的盒外向量。

若 \(y\in H\)，对任意正整数权 \(w_i\)，作一元特化 \(T_i=X^{w_i}\)。由于 (4)
的系数非负，特化后不同多重指标落到同一次数时不会抵消，故

\[
\boxed{
\operatorname{ord}_{X=0}
\mathcal F_y(X^{w_1},\ldots,X^{w_r})
=\min_{z:\phi(z)=y}
\sum_iw_i\operatorname{ov}_\nu(z)_i
=\Omega_w(y).}
\tag{7}
\]

若 \(y\notin H\)，则约定
\(\operatorname{ord}_{X=0}0=\min\varnothing=\Omega_w(y)=+\infty\)，式 (7)
在扩展实数意义下仍成立。

正有理权可统一放大为整数权；一般正实权仍可直接在 (6) 的支撑上取最小值。

## 对统一选择器的意义与边界

这一定理把此前分开的三种对象放入同一个规范对象中：

- 全部 Fourier 系数消失对应 G 型；
- 常数项对应有限盒中的 Type I 目标命中；
- 首个非零支撑层对应 F 型的选择不变溢出，完整极小支撑给出 Pareto 需求。

它只依赖 \(G\)、生成元、目标和预算，不依赖 Smith 分解中选取的特解、关系格基或
最短路搜索的平局规则。因此，关系格证书与 Fourier 证书在此处是同一目标纤维的两种
坐标描述。

本定理尚未证明某个盒外坐标必须映射到共同的标签差、模数差或块因子 \(q\)-进容量。
从 (7) 得到容量矛盾，仍需一个保持层数且跨状态兼容的算术载体映射。
