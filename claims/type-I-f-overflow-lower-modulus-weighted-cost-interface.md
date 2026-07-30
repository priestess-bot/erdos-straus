---
kind: claim
claim_id: type-I-f-overflow-lower-modulus-weighted-cost-interface
title: 更小模数 F 关系的选择不变溢出价格接口
statement: 对端点下降后的低模数关系同态 \(\phi_t(z)=\prod q_i^{z_i}\)，令 \(F_t=\phi_t^{-1}(-1)\)、\(B_\nu=\prod[-\nu_i,\nu_i]\)，并以 \(\operatorname{ov}_\nu(z)_i=(|z_i|-\nu_i)_+\) 定义盒外向量。对任意正权 \(w\)，\(\Omega_w(t)=\min_{z\in F_t}\sum_iw_i\operatorname{ov}_\nu(z)_i\) 是与 Smith 原像选择无关的最小溢出价格；F-box hit 当且仅当 \(\Omega_w=0\)，F-box miss 时 \(\Omega_w\ge\min_iw_i\)。该价格可作为跨状态容量的对偶需求接口，但尚未证明其每一层必须支付同一 q-进载体高度或导出严格递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f-overflow-balanced-lower-modulus-fiber-profile
  - type-I-f-overflow-lower-modulus-relation-lattice
topics:
- type-I
- F-state
- relation-lattice
- finite-box
- overflow
- weighted-capacity
- q-adic
- proof-program
sources:
- claim: type-I-f-overflow-balanced-lower-modulus-fiber-profile
  role: quotient-fiber-definition
- claim: type-I-f-overflow-lower-modulus-relation-lattice
  role: affine-lattice-certificate
visibility: public
last_checked: '2026-07-30'
---

# 更小模数 F 关系的选择不变溢出价格接口

## 定义

令 \(q_1,\ldots,q_r\) 是 \(K\) 的不同素因子，\(\nu_i=v_{q_i}(K)\)，并设

\[
\phi_t:\mathbb Z^r\longrightarrow
H_t,\qquad
\phi_t(z)=\prod_{i=1}^r q_i^{z_i}\pmod t,
\]

\[
F_t=\phi_t^{-1}(-1),\qquad
B_\nu=\prod_{i=1}^r[-\nu_i,\nu_i].
\]

对 \(z\in\mathbb Z^r\)，定义逐坐标盒外量

\[
\operatorname{ov}_\nu(z)_i=(|z_i|-\nu_i)_+.
\tag{1}
\]

给定任意权向量 \(w=(w_i)_{i=1}^r\in\mathbb R_{>0}^r\)，定义选择不变的溢出价格

\[
\Omega_w(t)=
\min_{z\in F_t}
\sum_{i=1}^r w_i\,\operatorname{ov}_\nu(z)_i.
\tag{2}
\]

原 F 见证保证 \(F_t\ne\varnothing\)。由于权为正，(2) 的目标函数在
\(\mathbb Z^r\) 上具有有限子水平集，所以最小值确实取得；它不依赖某个任意
Smith 原像 \(z_0\)。若把定义推广到没有原 F 见证的 quotient-G 情形，则约定
\(\Omega_w(t)=+\infty\)；本卡后文的盒命中/盒外等价均在 \(F_t\ne\varnothing\) 的
继承 F 状态上使用。

## 盒命中与盒外的精确判据

\[
\boxed{
\begin{aligned}
F_t\cap B_\nu\ne\varnothing
&\Longleftrightarrow \Omega_w(t)=0,\\
F_t\cap B_\nu=\varnothing
&\Longleftrightarrow \Omega_w(t)>0.
\end{aligned}}
\tag{3}
\]

如果是 F-box miss，则每个 \(z\in F_t\) 至少有一个坐标满足
\(\operatorname{ov}_\nu(z)_i\ge1\)，因此

\[
\Omega_w(t)\ge\min_i w_i.
\tag{4}
\]

更细地，可以保留所有按坐标支配意义极小的向量
\[
\operatorname{Pareto}_\nu(F_t)
=\min_{\preceq}\{\operatorname{ov}_\nu(z):z\in F_t\},
\tag{5}
\]
以避免把多坐标溢出错误压缩为一个标量。

## 证明

若 \(z\in F_t\cap B_\nu\)，则所有盒外量为零，故 \(\Omega_w=0\)。反之，正权使
\(\sum_iw_i\operatorname{ov}_\nu(z)_i=0\) 只能发生在每个坐标盒外量均为零，
即 \(z\in B_\nu\)。这证明 (3)。若盒为空，每个整数向量至少有一个坐标离开其
区间一个单位，代入 (1) 即得 (4)。由于 (2) 对整个目标纤维取最小值，任何选取的
表示 \(z\) 的加权费用都不小于 \(\Omega_w(t)\)；更换 Smith 原像只会更换参数化，
不会改变 \(F_t\) 或该最小值。

## 与跨状态容量的接口和边界

\(\Omega_w\) 解决了“用哪一个盒外表示收费”的选择问题，可以把每个低模数 F-box miss
转成一个规范的对偶需求。若权 \(w_i\) 取为对应素数的 \(q_i\)-进载体价格，则
\(\Omega_w\) 是现有容量账本所需的最小需求下界，而 (5) 记录多支持分配的全部
不可支配选项。

但是下面的算术映射仍未证明：

> 每个正的 \(\operatorname{ov}_\nu(z)_i\) 或其 Pareto 价格，必须在同一核心素数的
> 载体/标签/模数差高度上逐层支付，或者产生一个严格可提升的更小状态。

因此本卡是选择不变的容量接口，不是跨状态超载定理。当前 42 个关系格证书提供
\(F_t\) 的规范输入；下一步应在这些格上证明收费映射，而不是把任意 \(z_0\) 的坐标
直接当作容量需求。

## 关联结果

42 个冻结 F-box miss 的 Smith/Hermite 证书见[端点下降 F-box miss 的更小模数关系格证书](type-I-f-overflow-lower-modulus-relation-lattice.md)。
