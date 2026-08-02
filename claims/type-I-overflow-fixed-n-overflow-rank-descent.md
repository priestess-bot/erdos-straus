---
kind: claim
claim_id: type-I-overflow-fixed-n-overflow-rank-descent
title: 固定 n 窗口上方的 overflow 支撑秩递降
statement: 设 overflow 满足 pn=4Md+1、A|M 且 1≤A≤B_p=(p-1)^2/4。令 L=lcm(A,d)、R_L=4L-n、K_L=L(p-Md/L)。若 L>A、R_L>0、canonical_chart(p,L)=(R_L,K_L) 且 floor(B_p/L)<floor(B_p/A)，则 (p,R_L,K_L;L) 是完整 E1--E5 的 overflow_fixed_n_outer_rank_reset_v1 边；R_L<p 时为 marked absorb，R_L>p 时为严格降低 absorbed-support 秩的 overflow 后继。固定 n 窗口为空只排除 R_L<p 的目标，不排除窗口上方的 overflow 递降。
claim_status: computationally_reproduced
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - type-I-overflow-outer-rank-reset
  - type-I-marked-support-accumulation-rechart-saturation
topics:
- type-I
- overflow
- determinant
- fixed-n
- outer-rank
- charged-support
- well-founded-descent
- typed-receipt
- proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: fixed-n window-extension verifier and typed edges
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: focused 12-fixture fixed-n classification
visibility: public
last_checked: '2026-08-03'
---

# 固定 \(n\) 窗口上方的 overflow 支撑秩递降

## 1. 固定-\(n\) 恒等式的完整范围

设已有来源回执的 overflow 满足

\[
pn=4Md+1,\qquad S=Md,\qquad A\mid M.
\]

对

\[
L=\operatorname{lcm}(A,d)
\]

有 \(L\mid S\)。定义

\[
R_L=4L-n,\qquad
K_L=L\left(p-\frac{S}{L}\right).
\]

直接消元给出

\[
4K_L=pR_L+1,\qquad L\mid K_L.
\]

因此固定-\(n\) 因子图谱并不只包含
\[
n<4L<p+n\quad\Longleftrightarrow\quad 0<R_L<p
\]
的吸收目标。若 \(4L\ge p+n\)，则 \(R_L\ge p\)；只要 \(R_L>0\)，它仍是一个
合法 canonical overflow chart，而不是“没有后继”。

## 2. 外层秩边

令

\[
B_p=\frac{(p-1)^2}{4},\qquad
\Pi_A(A)=\left\lfloor\frac{B_p}{A}\right\rfloor.
\]

若

\[
1\le A\le B_p,\qquad
L>A,\qquad
R_L>0,\qquad
\Pi_A(L)<\Pi_A(A),
\]

则目标状态

\[
(p,R_L,K_L;L)
\]

携带旧支撑并严格降低不可重置的 absorbed-support 秩。目标方程仍为 \(4/p\)，标记集
取图表无关的 \(\operatorname{Sol}(p)\)，所以恒等映射给出全域 E4；固定-\(n\) 恒等式、
支撑整除和显式势比较分别给出 E1、E2/E3 和 E5。

- \(R_L<p\)：这是普通 marked_absorb；
- \(R_L>p\)：这是 overflow_fixed_n_outer_rank_reset_v1，目标仍可继续进入
  overflow 选择器；
- \(R_L\le0\)：目标不是正整数图表，不能登记为边。

所以固定-\(n\) 窗口为空时，必须先检查窗口上方的正 overflow 区域，不能直接把该
fixture 标成无固定-\(n\) 后继。

## 3. 聚焦回执

统一 selector 对现有 12 个 overflow fixture 逐项重算：

| 分类 | 数量 |
|---|---:|
| 固定-\(n\) fixture | 12 |
| 完整 E1--E5 边 | 9 |
| \(R_L<p\) 吸收目标 | 3 |
| \(R_L>p\) overflow 目标 | 6 |
| \(R_L\le0\) 或无严格秩的拒绝 fixture | 3 |

新增的 6 条 overflow 后继包括：

- \(p=241,A=38,M=190\to L=494\)；
- \(p=73,A=19,M=38\to L=228\)；
- \(p=73,A=19,M=836\to L=893\)；
- \(p=73,A=19,M=950\to L=342\)；
- \(p=73,A=66,M=1518\to L=924\)；
- \(p=73,A=66,M=924\to L=1518\)。

这些边的目标 \(R_L\) 分别仍大于 \(p\)，但
\(\Pi_A\) 严格下降；例如第一条为
\[
\left\lfloor\frac{(241-1)^2}{4\cdot38}\right\rfloor
=378
\longrightarrow
\left\lfloor\frac{(241-1)^2}{4\cdot494}\right\rfloor
=29.
\]

## 4. 逻辑边界

这条扩展只解决固定-\(n\) d 通道的窗口上方。它不证明每个 overflow 的
\(L=\operatorname{lcm}(A,d)\) 都正；当前 3 个拒绝 fixture 中，\(d=1\) 不增加支撑，
另两个候选满足 \(R_L\le0\)。r 通道仍需独立的支撑整除、alternate 或容量机制。
因而该结果把一部分“固定-\(n\) 空窗口”余项升级为严格递降，但没有闭合
\(A>1\) overflow 的全称存在性。

重放命令：

```bash
python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
```

结果位于
reproductions/type-i-representation-dual-capacity-selector-results.json 的
overflow_fixed_n_outer_rank。
