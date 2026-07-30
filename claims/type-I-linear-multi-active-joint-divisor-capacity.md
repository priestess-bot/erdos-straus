---
kind: claim
claim_id: type-I-linear-multi-active-joint-divisor-capacity
title: 线性同块多活跃方向的联合除子容量
statement: 固定核心素数 p、线性块标签 t、不同素数集合 Q 和模数窗口 I；若多个方向的 q 进幂同时整除 tR+1，则联合高度层由精确多除子集合 D_k(p,t,Q;I) 控制，层析给出 sum_R product_{q in Q} v_q(tR+1) 的严格容量上界。该结论推广配对容量到任意同块活跃集合，仍不提供 Fourier 支撑的跨状态重复性。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- finite-fourier
- relation-lattice
- multi-active
- divisor-lattice
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

# 线性同块多活跃方向的联合除子容量

## 多方向层

固定 \(p\)、块标签 \(t\)、不同素数集合
\(Q=\{q_1,\ldots,q_d\}\) 以及窗口
\(I=[R_{\min},R_{\max}]\cap\mathbb Z\)。写

\[
B_R=tR+1,\qquad h_q(R)=v_q(B_R).
\]

对多指标 \(\mathbf k=(k_q)_{q\in Q}\)，令

\[
Q^{\mathbf k}=\prod_{q\in Q}q^{k_q},
\]

并定义精确多除子集合

\[
\mathcal D_{\mathbf k}(p,t,Q;I)=
\left\{d:
d\mid\frac{p-t}{Q^{\mathbf k}},\quad
Q^{\mathbf k}d\equiv1\pmod t,\quad
\frac{Q^{\mathbf k}d-1}{t}\in I
\right\}.
\tag{1}
\]

若 \(Q^{\mathbf k}\nmid p-t\)，约定该集合为空。令

\[
N_{\mathbf k}=
\#\{R\in I:h_q(R)\ge k_q\text{ 对所有 }q\in Q\}.
\]

则

\[
\boxed{
N_{\mathbf k}\le|\mathcal D_{\mathbf k}(p,t,Q;I)|.
}
\tag{2}
\]

## 联合高度容量

对每个满足层条件的 \(R\)，取

\[
d=\frac{B_R}{Q^{\mathbf k}}.
\]

由 \(B_R\mid p-t\) 得到 (1) 中的除子条件；由
\(B_R\equiv1\pmod t\) 得到同余条件；不同 \(R\) 给出不同 \(d\)，所以映射是单射，
证明 (2)。

层析恒等式给出

\[
\sum_{R\in I}\prod_{q\in Q}h_q(R)
=
\sum_{k_q\ge1}N_{\mathbf k}.
\]

因此有严格容量界

\[
\boxed{
\sum_{R\in I}\prod_{q\in Q}h_q(R)
\le
\sum_{k_q\ge1}|\mathcal D_{\mathbf k}(p,t,Q;I)|,
}
\tag{3}
\]

其中只有有限多个 \(Q^{\mathbf k}\mid p-t\) 的层非空。也可以同时加入模数差装箱，
将每一层右端替换为

\[
\min\left\{
\left\lfloor\frac{R_{\max}-R_{\min}}{Q^{\mathbf k}}\right\rfloor+1,
|\mathcal D_{\mathbf k}(p,t,Q;I)|
\right\}.
\tag{4}
\]

## 与统一选择器的接口

若内部证书的多个活跃方向经高度优先规则落在同一个块 \(tR+1\)，则其联合高度需求
可以直接代入 (3)。特别地，\(|Q|=2\) 恢复配对容量，\(|Q|>2\) 保留全部同块方向，
避免把同一状态的多个方向拆成若干互相独立的容量账本。

该结论只处理同块集合。若不同方向落在不同块，必须改用双颜色共享模数交集或多颜色
容量，不能把 (3) 跨颜色相乘。

## 冻结诊断边界

对四个冻结对抗核心，以稳定子活跃方向作诊断输入，并对每个高度优先载体块保留全部
同块活跃方向，得到 79 个“状态—载体块”记录：

\[
\text{下界联合需求}=114,
\qquad
\text{实际联合需求}=139,
\qquad
\text{精确联合容量}=139.
\]

这是精确饱和而不是容量矛盾；它说明仅靠同块 \(q\)-进层析无法制造额外余量，后续必须
把 Fourier 相位质量、目标纤维稀疏度或状态提升成本作为额外需求加入。

该有限统计仍不证明稳定子方向等于规范 Fourier 支撑，也不说明 45 个状态已覆盖某个
核心素数的全部可达状态。
