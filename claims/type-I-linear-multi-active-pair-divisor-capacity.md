---
kind: claim
claim_id: type-I-linear-multi-active-pair-divisor-capacity
title: 线性多活跃状态的配对载体与除子型 q 进容量
statement: 对线性状态 p=a+s+asR，若所选载体方向集合至少有三个素数，则两个方向必在同一载体块 tR+1 上出现。固定核心素数 p、块标签 t、素数对 q1<q2 及模数窗口 I 后，具有该配对载体的状态数受精确除子集合 D_{q1,q2}(p,t;I) 控制；同时，联合高度层 N_{k,l} 受 D_{q1^k,q2^l}(p,t;I) 控制，层析给出乘积高度容量上界。冻结的四个对抗核心中，45 个 F 状态均有至少三个稳定子商非平凡方向可供载体提取；这只是可用方向的结构上界，不断言所选 Fourier 角色必有三个活跃坐标。该边界需求为 45、精确局部容量为 70，尚未产生容量矛盾。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- f-state
- g-state
- multi-active
- q-adic
- divisor-lattice
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

# 线性多活跃状态的配对载体与除子型 \(q\) 进容量

## 设置与配对载体

固定核心素数 \(p\equiv1\pmod {24}\) 的线性状态写成

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

设 \(Q\) 是所选对偶证书或稳定子商的载体方向集合。对 Fourier 证书应取
\[
Q=Q_{\mathrm{cert}}=\{q:\chi(q)\ne1\};
\]
在冻结审计中使用的是可用方向上界
\[
Q_{\mathrm{stab}}=\{q:q\mathcal A_R(K)\ne\mathcal A_R(K)\}.
\]

对 \(t\in\{s,a\}\) 写

\[
B_t=tR+1.
\]

因为 \(UV=4K\)，每个 \(q\in Q\) 至少整除 \(U\) 或 \(V\) 之一。若

\[
|Q|\ge3,
\]

则鸽巢原理保证存在一个块 \(B_t\) 同时承载两个不同活跃素数 \(q_1<q_2\)：

\[
q_1q_2\mid B_t.
\tag{1}
\]

更精确地，对任意 \(q\mid K\) 写
\[
h_U(q)=v_q(U),\qquad h_V(q)=v_q(V),\qquad \nu_q=v_q(K).
\]
则
\[
h_U(q)+h_V(q)=
\begin{cases}
\nu_q,&q\ne2,\\
\nu_2+2,&q=2.
\end{cases}
\tag{2}
\]
所以每个活跃方向都至少有一个载体块高度
\[
\max\{h_U(q),h_V(q)\}
\ge
\left\lceil\frac{\nu_q+2\mathbf 1_{q=2}}2\right\rceil.
\tag{3}
\]
这是单方向的高度下界；两个方向的高载体可能分落在不同块，因此 (3) 不能单独给出
配对块的联合高度下界。

这一步只使用载体向量和两个块，不使用角色的阶或相位大小。若需要跨状态计数，固定块顺序 \(s\prec a\)，先取第一个含至少两个活跃素数的块，再取其中字典序最小的素数对；这给出每个至少三活跃状态的规范配对。

因此，对任意已选 Fourier/格证书，支撑大小给出一个严格的三分接口：

1. \(|Q_{\mathrm{cert}}|=1\)：进入单素数载荷和标量 \(q\)-进容量分支；
2. \(|Q_{\mathrm{cert}}|=2\)：先检查两个方向是否落在同一块；若不落在同一块，则进入带颜色的双坐标容量或二维关系格分支；
3. \(|Q_{\mathrm{cert}}|\ge3\)：自动进入本卡的配对载体分支。

这只是证书支撑的结构分流，不声称任何 F 型状态都落在第三行；冻结审计的
\(Q_{\mathrm{stab}}\) 统计只能证明有可用方向上界。

## 单层除子容量

固定 \(p,t,q_1,q_2\)，令 \(I=[R_{\min},R_{\max}]\cap\mathbb Z\) 是规范配对状态的模数窗口，并设

\[
Q_2=q_1q_2.
\]

线性恒等式给出

\[
B_t=tR+1\mid p-t.
\tag{4}
\]

因此若 (1) 成立，则 \(Q_2\mid p-t\)，且

\[
d=\frac{tR+1}{Q_2}
\]

是 \((p-t)/Q_2\) 的正除子。定义精确可行除子集合

\[
\mathcal D_{q_1,q_2}(p,t;I)
=\left\{
d:
d\mid\frac{p-t}{Q_2},\quad
Q_2d\equiv1\pmod t,\quad
\frac{Q_2d-1}{t}\in I
\right\},
\tag{5}
\]

当 \(Q_2\nmid p-t\) 时约定该集合为空。

不同 \(R\) 给出不同的 \(B_t\)，从而给出不同的 \(d\)。于是规范配对状态数 \(N_{q_1,q_2}(p,t;I)\) 满足

\[
\boxed{
N_{q_1,q_2}(p,t;I)
\le
|\mathcal D_{q_1,q_2}(p,t;I)|.
}
\tag{6}
\]

这比只要求一个素数 \(q\mid B_t\) 的容量更紧，因为一个候选块必须同时携带两个指定素因子。

## 联合高度层

对同一标签 \(t\) 的状态集合定义

\[
h_i(R)=v_{q_i}(tR+1),
\qquad i=1,2,
\]

以及联合层

\[
N_{k,\ell}
=\#\{R\in I:h_1(R)\ge k,\ h_2(R)\ge\ell\}.
\]

令 \(Q_{k,\ell}=q_1^kq_2^\ell\)。和 (5) 同理，若 \(N_{k,\ell}>0\)，则 \(Q_{k,\ell}\mid p-t\)，并且

\[
N_{k,\ell}
\le
\left|
\mathcal D_{q_1^k,q_2^\ell}(p,t;I)
\right|.
\tag{7}
\]

对两个高度做层析得到

\[
\sum_{R\in I}h_1(R)h_2(R)
=\sum_{k,\ell\ge1}N_{k,\ell}
\le
\sum_{k,\ell\ge1}
\left|
\mathcal D_{q_1^k,q_2^\ell}(p,t;I)
\right|,
\tag{8}
\]

其中只有 \(q_1^kq_2^\ell\mid p-t\) 的有限层非空。也可以把 (7) 与模数差刚性结合，加入

\[
N_{k,\ell}
\le
\left\lfloor\frac{R_{\max}-R_{\min}}{q_1^kq_2^\ell}\right\rfloor+1,
\tag{9}
\]

再取两种上界的逐层最小值。

## 跨状态的有限排除检验

对同一核心素数的完整线性状态集合，按“第一个可配对块、最小素数对、模数 \(R\)”的规则分组。若 \(\mathcal S_{p,t,q_1,q_2}\) 是一个配对组，取其实际模数的最小闭区间 \(I_{p,t,q_1,q_2}\)，则由 (6) 得到

\[
\boxed{
\#\mathcal S_p^{(\ge3)}
\le
\sum_{t,q_1<q_2}
\left|
\mathcal D_{q_1,q_2}
\left(p,t;I_{p,t,q_1,q_2}\right)\right|.
}
\tag{10}
\]

如果完整状态的左端超过右端，则至少一个状态不能同时保持当前 G/F 证书分类，必须进入目标命中、偶终端或其它已经定义的出口。

式 (10) 是依赖完整状态窗口的有限排除检验，不是与 \(p\) 无关的普适常数。它也只覆盖至少三个活跃方向的状态；一、二活跃方向必须保留单素数或单活跃分支。

## 当前边界与尚未闭合的桥

对冻结的四个对抗核心，45 个有限指数 F 状态的活跃方向数均至少为 3，因此规范配对规则覆盖全部 45 个状态。按配对组枚举 (5) 得到 40 个非空组，单位需求数为 45，精确局部容量总和为 70；其中 \(p=878089,26034649,57399241,283319689\) 的容量分别为 \(2,6,49,13\)，对应需求 \(2,6,24,13\)。按同一规范配对记录实际联合高度 \(h_1h_2\)，冻结样本的需求为 99，逐层精确容量为 136。两种统计都未产生容量超载。

这张主张卡推进了“多活跃方向到算术容量”的结构侧：若所选证书确实有至少三个
活跃方向，就会产生一个可验证的配对载体。冻结审计中的三活跃统计来自
\(Q_{\mathrm{stab}}\)，只说明每个状态有足够的可用方向，不能替代
\(Q_{\mathrm{cert}}\) 的对偶支撑证明。一般 Fourier/格证书目前没有保证某个规范配对在所有
失败状态中反复出现，也没有给出统一的联合高度下界。因此 (10) 不能单独推出全称
Type I/II 选择器。
