---
kind: claim
claim_id: type-I-linear-internal-certificate-carrier-trichotomy
title: 线性内部证书的支撑—载体三分接口
statement: 对线性状态 p=a+s+asR 及一个已选内部 Fourier、关系格或加法组合证书，按活跃素数支撑大小分流：单方向进入标量 q 进容量；双方向按高度优先载体颜色相同或不同分别进入同块配对容量或双颜色共享模数交集容量；至少三方向时两块鸽巢原理给出同一高度优先载体块上的一对，并产生显式联合高度下界。外部 G 型分离角色在 H 上恒等，不属于该三分接口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- finite-fourier
- relation-lattice
- additive-combinatorics
- carrier-vector
- q-adic
- capacity
- cross-state
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-linear-normal-form-context
visibility: public
last_checked: '2026-07-30'
---

# 线性内部证书的支撑—载体三分接口

## 线性状态与内部支撑

固定

\[
p=a+s+asR,
\qquad s\ {\text{odd}},
\qquad R\equiv3\pmod4,
\]

并令

\[
K=\frac{pR+1}{4},
\qquad U=sR+1,
\qquad V=aR+1,
\qquad UV=4K.
\]

设 \(\chi\) 是一个已选的内部角色证书，定义其活跃素数支撑

\[
Q_\chi=\{q\mid K:\chi(q)\ne1\}.
\]

外部 G 型分离角色限制到 \(H=\mathcal H_R(K)\) 后恒等，故
\(Q_\chi=\varnothing\)，由支撑外分离分支处理，不进入本引理。

对 \(q\in Q_\chi\)，定义高度优先载体

\[
t_\chi(q)=\operatorname*{argmax}_{t\in\{s,a\}}v_q(tR+1),
\qquad
h_\chi(q)=v_q(t_\chi(q)R+1),
\]

平手固定取 \(s\prec a\)。由 \(UV=4K\)，

\[
h_\chi(q)\ge
\left\lceil\frac{v_q(K)+2\mathbf1_{q=2}}2\right\rceil.
\tag{1}
\]

## 三个支撑分支

### 单方向

若 \(|Q_\chi|=1\)，记 \(Q_\chi=\{q\}\)。载体
\((q,t_\chi(q),h_\chi(q))\) 直接满足单方向 \(q\) 进容量的输入条件。不同状态若重复同一 \(q\)，块刚性把共同幂
拉回标签差或同标签模数差；可调用
[线性载体块的标签—模数混合 q 进容量](type-I-linear-hybrid-label-modulus-q-adic-capacity.md)。

### 双方向

若 \(Q_\chi=\{q_1,q_2\}\)，比较两个高度优先颜色：

1. 若 \(t_\chi(q_1)=t_\chi(q_2)=t\)，则
   \(q_1^{h_\chi(q_1)}q_2^{h_\chi(q_2)}\mid tR+1\)，进入同块配对容量；
2. 若两个颜色不同，则分别使用 \(t_iR+1\mid p-t_i\)，进入
   [线性双颜色载体的共享模数交集容量](type-I-linear-two-color-carrier-intersection-capacity.md)。

两种情况下都保留实际颜色和高度，不能把两个方向的独立容量未经证明地相乘。

### 至少三方向

若 \(|Q_\chi|\ge3\)，只有两个颜色 \(s,a\)，所以存在不同的 \(q_1,q_2\) 满足

\[
t_\chi(q_1)=t_\chi(q_2)=t.
\]

由 (1) 得到同块联合高度下界

\[
h_\chi(q_1)h_\chi(q_2)
\ge
\left\lceil\frac{v_{q_1}(K)+2\mathbf1_{q_1=2}}2\right\rceil
\left\lceil\frac{v_{q_2}(K)+2\mathbf1_{q_2=2}}2\right\rceil.
\tag{2}
\]

所以该分支进入
[高度优先配对载体容量](type-I-linear-high-carrier-pair-capacity.md)，再由同块精确除子—
剩余集合给出跨状态容量。

## 证明

式 (1) 由两个载体块的 \(q\)-进指数和等于 \(v_q(4K)\) 及最大值不小于平均值得到。
双方向时，两个高度优先颜色要么相同，要么不同；相同颜色给出同块除子条件，不同颜色
给出两个 \(p-t_i\) 除子条件及共同模数交集。至少三方向时，将每个方向按高度优先颜色
放入两个颜色盒，鸽巢原理给出同色的一对，再将 (1) 相乘得到 (2)。

## 逻辑边界

本引理完成的是“已选内部证书 \(\to\) 可调用的算术容量接口”。它不证明：

1. F 型状态一定有内部角色支撑；
2. 规范角色在不同状态中重复使用同一个 \(q\)、颜色或配对；
3. 稳定子活跃方向统计可以替代规范 Fourier/格支撑；
4. 容量已经超过需求或产生严格可提升下降。

因此它是统一选择器的结构分流定理，而不是全称 Type I/II 选择器本身。
