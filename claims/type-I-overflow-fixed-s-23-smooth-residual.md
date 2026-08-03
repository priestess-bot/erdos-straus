---
kind: claim
claim_id: type-I-overflow-fixed-s-23-smooth-residual
title: fixed-s 的 2,3-光滑载体残余正规形
statement: '设 overflow fixed-s 行列式满足 p*s=4*r*d+1，且 Supp(r*d)⊆{2,3}。所有 fixed-s 除子落在指数格 L=2^i*3^j。令 L_+=max{L|r*d: L≤B_p, 4L>s}；若 L_+≥2A，则 L_+ 自动满足严格势下降并给出 fixed-s 恒等提升边，因此任何 rejected 行都满足 L_+<2A。若 r=1 或 d=1，该格退化为已分类的一维边界，不应再计入新的二维 overflow 余项；只有 r,d>1 的行才转交 generalized-dyadic、Type II 或 q-adic capacity。'
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-fixed-s-bounded-divisor-saturation
  - type-I-overflow-r-one-dual-boundary
  - type-I-overflow-d-one-p-minus-two-g-rechart
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

定义正的有界格前沿

\[
L_+=\max\{L\mid L\mid P,\ L\le B_p,\ 4L>s\},
\]

若集合为空则令 \(L_+=0\)。若 \(L_+\ge2A\)，则

\[
\left\lfloor\frac{B_p}{L_+}\right\rfloor
\le
\left\lfloor\frac{B_p}{2A}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor,
\]

所以 \(L_+\) 本身就是合格 fixed-s 格点。反之，任何没有合格格点的行都满足

\[
\boxed{L_+<2A.}
\]

这把空格点从任意因子缺失收缩为一个明确的支撑饱和带；它仍不是跨状态容量或递归
下降定理。

## 2. 空格点的逻辑边界

若上述指数格没有合格格点，这只证明当前 fixed-s 外层秩菜单没有出口，并且由上面的
前沿引理知道 \(L_+<2A\)。它不证明 Erdős--Straus 反例，也不证明状态没有其它表示。
根据统一选择器合同，该行必须保持

selector_status=analysis_evidence
recursive_edge_eligible=false

并转交三个仍可能携带新信息的分支：

1. 若 \(r=1\) 或 \(d=1\)，先调用对应的一维 fixed-s 边界和 G/Type II 专门分支；
2. 对 \(r,d>1\) 的真正二维残余，generalized-dyadic 把 \(2^i\) 方向投影到已有偶前驱窗口；
3. Type II 检查 \(3\)-方向或共享除子射线，q-adic capacity 则只在有显式跨状态相位映射时使用。

特别地，指数格为空不能被解释成自然广义二进标记源非空；自然标记的非空性仍由
当前中心 Type I 命中精确决定。

因此，\(r=1\) 或 \(d=1\) 的空格点不是新的二维残余。它们分别落入
[overflow 余数 \(r=1\) 的对偶边界](type-I-overflow-r-one-dual-boundary.md)和
[d=1 overflow 的 \(p-2\) G 重图表正规形](type-I-overflow-d-one-p-minus-two-g-rechart.md)；
只有在 \(r,d>1\) 且 \(L_+<2A\) 时，才保留本卡的二维路由标签。

## 3. 聚焦回执

统一选择器当前冻结回放中，reachable_conflict_bundle_3 的
\(P=18=2\cdot3^2\) 没有 fixed-s 合格格点，且
\[
L_+=18<2A=38,\qquad r=1.
\]
该行因此被记录为一维 fixed-s 边界而不是新的二维残余；其后续路由首先调用
r=1 对偶边界，再保留 Type II 和 q-adic capacity 作为非支撑出口。

这是一条状态类型和支撑饱和边界，不是 2,3-光滑残余的全称终端定理。

## 4. 真正二维的参数化边界

上述一条冻结回执不是二维余项的唯一算术形状。设

\[
P=2^a3^b,\qquad a,b\ge1,\qquad p=4P+1\ \text{为素数},
\]

取

\[
r=2,\qquad d=P/2,\qquad M=kp+r,\qquad A=M,
\]

其中

\[
1\le k\le\left\lfloor\frac{B_p-r}{p}\right\rfloor.
\]

则 \(r,d>1\)、\(rd=P\)、\(s=1\)，并且

\[
n=4kd+1,\qquad
p n=4Md+1,
\]

\[
R_M=4M-n>p,\qquad
K_M=M(p-d).
\]

由于 \(M\ge p+2>P\)，所有 fixed-s 除子 \(L\mid rd=P\) 都满足 \(L<A\)，所以这族
状态的 fixed-s 指数格恒为空，且

\[
L_+\le P<A.
\]

这是一族真实的 \(r,d>1\) 算术 overflow 边界；它说明“2,3-光滑残余只有
\(r=1/d=1\)”是错误的。当前回执只验证素数种子
\[
p\in\{73,97,193,433,1297\}
\]
及每个种子的 \(k=1\) 和允许范围末端，未证明这些状态从原始 F/G Reach 可达。因此它们
保持 analysis_evidence，后续必须寻找 alternate carrier、Type II 终端或显式跨状态
容量映射。
