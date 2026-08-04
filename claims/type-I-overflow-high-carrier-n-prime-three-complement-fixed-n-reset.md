---
kind: claim
claim_id: type-I-overflow-high-carrier-n-prime-three-complement-fixed-n-reset
title: exact n=p 高载体中 3|C 的固定 n 支撑重置
statement: 设 p=1 (mod 24)，B_p=(p-1)^2/4，Q=(p-3)/2，且 exact n=p G-anchor 的旧支撑为 A=B_p/C，其中 2<=C<Q、C|B_p、3|C。则 G-anchor phase 为 t=A-(p-1)/6，目标 overflow 的补余固定为 n_*=(p^2-5p+7)/3、d=2C/3、Md=2B_pQ/3。取 L=2B_p/3（C=3）或 L=B_p/3（C>3），有 L|Md、A<L<=B_p、4L>n_* 和 floor(B_p/L)<floor(B_p/A)；canonical chart 为 (4L-n_*, L(p-Md/L))，C>3 时恰为 (p-2,B_p)，C=3 时仍为 overflow。若来源回执另行提供 Sol(p) 标记集、完整可达性和恒等提升，则这些公式补齐 E1--E5；本卡的合成回执不自动升级为递归边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-high-carrier-n-prime-g-anchor-phase
  - type-I-overflow-fixed-n-bounded-divisor-saturation
  - type-I-overflow-same-chart-support-promotion
topics:
- type-I
- overflow
- high-carrier
- n-equals-p
- G-state
- fixed-n
- support-reset
- three-divisible-complement
- conditional-edge
- proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: 3|C fixed-n divisor classifier and verifier
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: synthetic conditional-reset profiles
visibility: public
last_checked: '2026-08-04'
---

# exact \(n=p\) 高载体中 \(3\mid C\) 的固定-\(n\) 支撑重置

## 1. 参数化

令

\[
B=B_p=\frac{(p-1)^2}{4},\qquad
Q=\frac{p-3}{2},\qquad
c=\frac{p-1}{6},\qquad A=\frac{B}{C},
\]

其中 \(2\le C<Q\)、\(C\mid B\)、\(3\mid C\)。于是 \(A Q>B\)，是 exact \(n=p\)
G-anchor 的真高载体区域。由相位公式，因

\[
(p-1)c=\frac{2B}{3}=A\frac{2C}{3},
\]

有

\[
t_A=A-c,\qquad
R_{AQ}=4AQ-n_* ,\qquad
n_*:=4Qc-\frac{p-4}{3}=\frac{p^2-5p+7}{3}.
\tag{1}
\]

同时

\[
d=\frac{2C}{3},\qquad
S:=A Qd=\frac{2BQ}{3},\qquad
pn_*=4S+1.
\tag{2}
\]

所以所有 \(3\mid C\) 的 G-anchor 高载体共享同一个 fixed-\(n_*\) 乘积 \(S\)。

## 2. 两个确定除子

若 \(C=3\)，取

\[
L=\frac{2B}{3};
\]

若 \(C>3\)，取

\[
L=\frac{B}{3}.
\]

两种情况下均有 \(L\mid S\)、\(A<L\le B\) 且 \(4L>n_*\)。固定-\(n_*\) 图表为

\[
R_L=4L-n_*,\qquad
K_L=L\left(p-\frac{S}{L}\right).
\tag{3}
\]

当 \(C>3\) 时，\(S/L=2Q=p-3\)，因此

\[
(R_L,K_L)=(p-2,B).
\tag{4}
\]

这正是对偶 G 图表，且 \(\Pi_B(L)=3<C=\Pi_B(A)\)。当 \(C=3\) 时，
\(S/L=Q\)，\(\Pi_B(L)=1<3\)，而 \(R_L>p\)，目标仍是 overflow。

统一地，

\[
\Pi_B(L)=\left\lfloor\frac{B}{L}\right\rfloor
<\left\lfloor\frac{B}{A}\right\rfloor=C.
\tag{5}
\]

## 3. 条件性 E1--E5 边界

若来源状态已经携带完整 \(\operatorname{Sol}(p)\) 标记集，并且 exact \(n=p\) G-anchor
行确实来源可达，则 (2)--(5) 给出：

- E1：固定-\(n_*\) canonical chart 恒等式；
- E2：\(L\mid K_L\)；
- E3：来源回执的 exact G-anchor 状态；
- E4：\(\operatorname{Sol}(p)\) 对图表独立，取恒等提升；
- E5：式 (5) 的外层势严格下降。

因此该子族是一个条件性 verified fixed-\(n\) support-reset edge：\(C>3\) 到达 G
marked-absorb 图表，\(C=3\) 到达新的 overflow 图表。当前 synthetic profile 没有
来源标记和完整 Reach 证明，选择器故意保持 analysis_evidence。

## 4. 聚焦回执

选择器对 \(p=73\) 的 \(C=3,6,9,12,18,24,27\) 以及 \(p=97\) 的
\(C=3,6,9,12,18,24,36\) 全部重算式 (1)--(5)。两组均得到 6 条 G-chart target、
1 条 \(C=3\) overflow target，且每行势严格下降。

复现：

    python3 reproductions/type_i_representation_dual_capacity_selector.py --verify

该结果把 exact \(n=p\) 真高载体余项进一步缩小到 complements not divisible by 3，
或来源标记尚未建立的状态；它不是所有高载体 overflow 的全称闭合。
