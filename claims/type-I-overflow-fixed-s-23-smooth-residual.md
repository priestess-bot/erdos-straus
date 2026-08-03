---
kind: claim
claim_id: type-I-overflow-fixed-s-23-smooth-residual
title: fixed-s 的 2,3-光滑载体残余正规形
statement: 设 overflow fixed-s 行列式满足 p*s=4*r*d+1，且 Supp(r*d)⊆{2,3}。则所有 fixed-s 除子唯一落在二维指数格 L=2^i*3^j；若没有满足 A<L≤B_p、4L>s 和 Pi(L)<Pi(A) 的格点，选择器只能登记 analysis_evidence，并把该状态转交 generalized-dyadic、Type II 或 q-adic capacity 分支，不能把空格点当作递归失败。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-fixed-s-bounded-divisor-saturation
  - type-I-generalized-dyadic-natural-lift-equivalence
  - type-I-cross-state-q-adic-capacity-bound
topics:
- type-I
- overflow
- fixed-s
- smooth-support
- generalized-dyadic
- type-II
- q-adic
- proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: typed smooth-residual routing
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: focused smooth-residual receipt
visibility: public
last_checked: '2026-08-04'
---

# fixed-s 的 2,3-光滑载体残余正规形

设

\[
pn=4Md+1,\qquad M=kp+r,\qquad ps=4rd+1,
\]

并令

\[
P=rd,\qquad \operatorname{Supp}(P)\subseteq\{2,3\}.
\]

## 1. 指数格

任意 \(L\mid P\) 唯一写成

\[
L=2^i3^j,\qquad
0\le i\le v_2(P),\quad
0\le j\le v_3(P).
\]

fixed-s 图谱的全部候选因此是一个有限二维指数格；其图表和容量条件为

\[
R_L=4L-s,\qquad
K_L=L\left(p-\frac{P}{L}\right),
\]

\[
A<L\le B_p,\qquad 4L>s,\qquad
\left\lfloor\frac{B_p}{L}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor.
\]

满足这些条件的格点由 fixed-s bounded-divisor 合同直接给出恒等提升和完整 E1--E5。

## 2. 空格点的逻辑边界

若上述指数格没有合格格点，这只证明当前 fixed-s 外层秩菜单没有出口。它不证明
Erdős--Straus 反例，也不证明状态没有其它表示。根据统一选择器合同，该行必须保持

selector_status=analysis_evidence
recursive_edge_eligible=false

并转交三个仍可能携带新信息的分支：

1. generalized-dyadic：把 \(2^i\) 方向投影到已有偶前驱窗口；
2. Type II：检查 \(3\)-方向或共享除子射线的标记证书；
3. q-adic capacity：把指数格边界的缺陷高度与跨状态标签相容性连接。

特别地，指数格为空不能被解释成自然广义二进标记源非空；自然标记的非空性仍由
当前中心 Type I 命中精确决定。

## 3. 聚焦回执

统一选择器当前冻结回放中，reachable_conflict_bundle_3 的
\(P=18=2\cdot3^2\) 没有 fixed-s 合格格点。该行因此被记录为
fixed_s_23_smooth_residual，而不是一般的 admissible_L 算术错误；其后续路由为
generalized-dyadic、Type II 和 q-adic capacity。

这是一条状态类型和证明边界，不是 2,3-光滑残余的全称终端定理。
