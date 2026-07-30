---
kind: claim
claim_id: type-I-linear-two-color-carrier-intersection-capacity
title: 线性双颜色载体的共享模数交集容量
statement: 对线性状态 p=a+s+asR，若两个选定素数方向 q1、q2 分别由载体块 t1R+1、t2R+1 承担，则固定 p、q1、q2、t1、t2 和模数窗口 I 后，同时满足两条载体除子条件的状态数受精确交集除子集合 D_{k,l}(p;t1,t2,q1,q2;I) 控制；联合高度层 N_{k,l} 还受模数差的 q1^k q2^l 装箱上界控制。该引理覆盖双方向分色，不把两个颜色的独立容量未经证明地相乘；它不保证 Fourier 证书必然产生固定的双方向。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- finite-fourier
- relation-lattice
- two-active
- colored-capacity
- q-adic
- divisor-lattice
- cross-state
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-linear-normal-form-context
visibility: public
last_checked: '2026-07-30'
---

# 线性双颜色载体的共享模数交集容量

## 设置

固定线性状态

\[
p=a+s+asR,\qquad
U=sR+1,\qquad
V=aR+1,\qquad
UV=4K.
\]

选择两个不同素数方向 \(q_1\ne q_2\)，以及它们的载体标签
\[
t_1,t_2\in\{s,a\},
\qquad
B_i=t_iR+1\quad(i=1,2).
\]

这里允许 \(t_1=t_2\)，那是同颜色情形；\(t_1\ne t_2\) 则是两个方向分落在不同块上的双颜色情形。由线性恒等式

\[
B_i\mid p-t_i.
\tag{1}
\]

若 \(q_i^{k_i}\mid B_i\)，则必有 \(q_i^{k_i}\mid p-t_i\)。同时 \(q_i\nmid t_i\)，因为
\(q_i\mid t_i\) 会与 \(q_i\mid(t_iR+1)\) 矛盾。

## 精确交集除子集合

令 \(I=[R_{\min},R_{\max}]\cap\mathbb Z\)，并取 \(k,\ell\ge1\)。当
\(q_1^k\mid p-t_1\) 且 \(q_2^\ell\mid p-t_2\) 时，定义

\[
\begin{aligned}
\mathcal D_{k,\ell}
(p;t_1,t_2,q_1,q_2;I)
=\biggl\{(d_1,d_2):\;&
d_1\mid\frac{p-t_1}{q_1^k},\
d_2\mid\frac{p-t_2}{q_2^\ell},\\
&q_1^kd_1\equiv1\pmod {t_1},\
q_2^\ell d_2\equiv1\pmod {t_2},\\
&\frac{q_1^kd_1-1}{t_1}
=\frac{q_2^\ell d_2-1}{t_2}\in I
\biggr\}.
\end{aligned}
\tag{2}
\]

若任一整除条件失败，则约定 \(\mathcal D_{k,\ell}=\varnothing\)。定义联合高度层

\[
N_{k,\ell}
=\#\left\{R\in I:
v_{q_1}(t_1R+1)\ge k,\
v_{q_2}(t_2R+1)\ge\ell,\
B_i\mid p-t_i\ (i=1,2)
\right\}.
\tag{3}
\]

对每个 \(R\) 取
\[
d_i=\frac{t_iR+1}{q_i^{k_i}},
\qquad (k_1,k_2)=(k,\ell).
\]
式 (1) 保证 \(d_i\) 是相应整数的除子，两个 \(R\) 不同则共同的模数
\(R=(q_i^{k_i}d_i-1)/t_i\) 不同。因此映射 \(R\mapsto(d_1,d_2)\) 是单射，得到

\[
\boxed{
N_{k,\ell}
\le
\left|\mathcal D_{k,\ell}
(p;t_1,t_2,q_1,q_2;I)\right|.
}
\tag{4}
\]

这是双颜色交集的精确容量；它同时保留两个 \(p-t_i\) 的除子结构和共享模数条件，严格
强于分别计算两个单颜色容量后再相乘或相加的未经证明估计。

## 联合高度与模数差装箱

若固定一组状态的 \(t_1,t_2,q_1,q_2\)，并令
\[
h_1(R)=v_{q_1}(t_1R+1),
\qquad
h_2(R)=v_{q_2}(t_2R+1),
\]
则层析恒等式给出

\[
\sum_{R}h_1(R)h_2(R)
=\sum_{k,\ell\ge1}N_{k,\ell}
\le
\sum_{k,\ell\ge1}
\left|\mathcal D_{k,\ell}
(p;t_1,t_2,q_1,q_2;I)\right|.
\tag{5}
\]

另一方面，若 \(R,R'\) 同属这一固定颜色组，且两者都在联合层
\(N_{k,\ell}\) 中，则
\[
q_1^k\mid t_1(R-R'),
\qquad
q_2^\ell\mid t_2(R-R').
\]
由于 \(q_i\nmid t_i\)，且 \(q_1\ne q_2\)，得到
\[
q_1^kq_2^\ell\mid R-R'.
\]
因此还满足区间装箱上界

\[
\boxed{
N_{k,\ell}
\le
\left\lfloor
\frac{R_{\max}-R_{\min}}{q_1^kq_2^\ell}
\right\rfloor+1.
}
\tag{6}
\]

实际使用时应对 (4) 与 (6) 逐层取较小者，再用 (5) 求联合高度容量。

当 \(t_1=t_2\) 时，两个方向在同一载体块上，(2)--(6) 退化为配对载体容量的双素数
特例；当 \(t_1\ne t_2\) 时，式 (2) 的共同 \(R\) 等式正是分色之间不能独立计数的
约束。

## 与对偶支撑三分的接口

对规范 Fourier/格证书的活跃支撑 \(Q_{\mathrm{cert}}\)，双方向分支应先选定
\(q_1,q_2\) 及其实际载体颜色：

1. 若颜色相同，使用[线性多活跃状态的配对载体与除子型 q 进容量](type-I-linear-multi-active-pair-divisor-capacity.md)；
2. 若颜色不同，使用本卡的共享模数交集容量；
3. 若支撑超过两个，先由两个载体块的鸽巢原理提取同色配对，再可比较剩余方向；
4. 若不同状态的 \(q_i,t_i\) 不同，必须按 \((q_1,q_2,t_1,t_2)\) 分组，不能把颜色
   或素数方向未经规范化地合并。

本卡完成的是双方向分色的算术容量接口。它仍没有证明一般 F 型 Fourier 证书会在
不同状态之间重复使用同一个方向对，也没有把相位预算自动转成 \(h_i\ge h_0\)；
这两项仍是统一选择器的开放桥梁。
