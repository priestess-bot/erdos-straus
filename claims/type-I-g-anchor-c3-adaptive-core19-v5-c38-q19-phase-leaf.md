---
kind: claim
claim_id: type-I-g-anchor-c3-adaptive-core19-v5-c38-q19-phase-leaf
title: v=5 的第三条 C=38 实际 raw 叶与 q=19 相位层
statement: 在 v=5 的 core-19 素数点 p=1202376916441，universal p-edge 后的全右 raw word (5623,6961,3041,3019) 是一条实际 primitive receipt，并到达第二坐标 z=5208574702312=38*137067755324。由 C2=38、M2=K/38、t2=137067755324 的正向 physical tail 有 mu2=-z^(-1)=-n2*t2^(-1) (mod R)，且 eta(mu2)=mu2^10=zeta^11 (mod 191)。这精确匹配 D=6303,A=573 候选记录内 H_base*19^3=1334507617 的一个 character phase，但在缺少 raw functor 时不唯一决定 candidate label。三张 C=(p-3,19,38) cofactor-overflow 行都通过 A=19 的 E2，并有算术 CarryCore=19；C=19 与 C=38 虽给出同一 r-chart 算术输出 (R_r,K_r)=(63,18937436433946)，但其后继 target carrier 分别为 19、38。因此新叶是真实第三 occurrence，却不建立 candidate label、slot identity、adapter、capacity 或 selector edge；v=5 仍被 (m,d)=(3,11) direct terminal 抢占。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-adaptive-core19-v5-dual-leaf-f19-control
  - type-I-g-anchor-c3-adaptive-core19-v5-signed-marked-source-groupoid
  - type-I-g-anchor-c3-adaptive-core19-v5-q19-phase-compatible-candidate-fiber
  - type-I-g-anchor-c3-adaptive-core19-v5-d6303-complete-fiber-boundary
  - type-I-ordered-raw-lineage-normalized-phase-rigidity
  - type-I-fg-raw-transcript-persistent-ledger-carry-core
topics:
  - type-I
  - type-II
  - c3
  - core19
  - raw-source
  - primitive-receipt
  - signed-tail
  - q-primary
  - q-adic-height
  - candidate-fiber
  - carry-core
  - terminal-preempted
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_c3_adaptive_core19_v5_c38_q19_phase_leaf.py
    role: third raw receipt, physical-tail mark, phase correspondence, carry control, and candidate-label boundary
visibility: public
last_checked: '2026-08-07'
---

# v=5 的第三条 C=38 实际 raw 叶

这是第三条已逐边重放的 raw occurrence，不是第三个已分配的 Type II request。它命中一个
选定 height-\(3\) cofactor \(H_3\) 的 character class，但不从 raw word 中读出这个高度；
新叶与 \(C=19\) 行在粗 \(r\)-chart 投影上相同，且 \(H_3\) 嵌套在 \(A=573\) 的候选记录内。

## 1. 实际 primitive raw receipt

令

\[
\mathsf S=(p,R(p-1)-p,p-1),\qquad
\mathsf A=(1,R-1,1).
\tag{1}
\]

第三支只与 \(C_0,C_1\) 共享 universal \(p\)-edge \(\mathsf S\to\mathsf A\)。此后始终
选择右侧：

\[
\begin{array}{c|c|c}
q&\text{source}&\text{destination}\\ \hline
5623&(1,5210299971230,1)&(926605010,5209373366221,1)\\
6961&(926605010,5209373366221,1)&(748365661,5209551605570,1)\\
3041&(748365661,5209551605570,1)&(1713104770,5208586866461,1)\\
3019&(1713104770,5208586866461,1)&(1725268919,5208574702312,1).
\end{array}
\tag{2}
\]

四个标签均为素数，且每步都满足

\[
v_q(\text{selected})=1>v_q(K)=0,
\qquad \text{unit condition},\qquad \text{gcd reduction}=1.
\tag{3}
\]

它的首标签 \(5623\) 不等于双叶中 p 后的 \(5\)，故这是共享 anchor 后的一条不同 ordered
raw branch；这里不引入 frame merge。

## 2. Physical tail 与相位

末端被追踪的第二坐标为

\[
z=5208574702312=38\cdot137067755324.
\tag{4}
\]

取

\[
\begin{aligned}
C_2&=38,& t_2&=137067755324,\\
M_2&=K/38=41215423770666847308611,&d_2&=p-38,\\
n_2&=4M_2-R=164861695077457089263213.
\end{aligned}
\tag{5}
\]

有 \((t_2,M_2)=(z,R)=1\)、\(0<z<R\)，并且

\[
pn_2=4M_2d_2+1.
\tag{6}
\]

从 \(\mathsf S\) 的第二坐标开始，lineage 在 (2) 的末端仍位于第二坐标，故 physical
orientation 为 \(+1\)。于是

\[
\mu_2=-z^{-1}=-n_2t_2^{-1}=5050926882929\pmod R.
\tag{7}
\]

令 \(\zeta=150\) 和 \(\eta(x)=x^{10}\pmod {191}\)，则

\[
\eta(\mu_2)=52=\zeta^{11}.
\tag{8}
\]

现有 \(D=6303,A=573\) 候选记录满足

\[
\begin{aligned}
H_{\rm base}&=53\cdot3671=194563,\\
H_3&=H_{\rm base}19^3=1334507617,\\
p+4(573\cdot6303)&=901H_3,
\qquad\chi(H_3)=52.
\end{aligned}
\tag{9}
\]

故 \(\chi(H_3)=\eta(\mu_2)\)。相对关系也精确：

\[
\eta(\mu_2\mu_1^{-1})=\zeta^3=\chi(19^2),
\qquad
\eta(\mu_2\mu_0^{-1})=\zeta^{14}=\chi(19^3).
\tag{10}
\]

这条 raw word 不含标签 \(19\)，故 (8)--(10) 只给出 character correspondence，既不是
occurrence 到 \((a,b,H)\) 的 functor，也不从 \(\mu_2\) 恢复 \(v_{19}(H_3)=3\)。

## 3. 三行 carry 控制与同 chart 算术

对 \(C_0=p-3,C_1=19,C_2=38\)，取 \(A=19\)。三张 physical cofactor-overflow
行都满足 determinant 并通过 E2。其余数是

\[
r_0=100198076370,\qquad
r_1=996707180734,\qquad
r_2=498353590367.
\tag{11}
\]

此行集的纯算术 carry 量为

\[
\operatorname{CarryCore}=19.
\tag{12}
\]

但它不能被读成三份容量，因为

\[
19r_1=38r_2=18937436433946,
\qquad
4(19r_1)=4(38r_2)=63p+1.
\tag{13}
\]

所以 \(C=19\) 和 \(C=38\) 具有相同的 \(r\)-chart 算术输出

\[
(R_r,K_r)=(63,18937436433946).
\tag{14}
\]

CarryCore 只计算这三张已声明 physical row 的共同 gcd/E2 数据。(13) 只给出相同
\((R_r,K_r)\)，不等于同一后继状态：cofactor r-chart 合同中的 target carrier 是

\[
M_T=\operatorname{lcm}(A,C),
\qquad
M_T(C_1)=19,\quad M_T(C_2)=38.
\tag{15}
\]

因此任何 merge、slot identity 或 slot count 都必须额外保留 \(M_T\)、entry digest 和
allocation；不能仅凭共同的 r-chart 算术合并或计数它们。

## 4. 固定候选格的 allocation 边界

在固定 \(D=6303\) 的全部 \(A\mid D\) 中，

\[
v_{19}(p+4DA)>0
\Longleftrightarrow
(A,v_{19})=(3,1)\ \text{或}\ (573,3).
\tag{16}
\]

因此这个有限 menu 只有两个 \(q=19\)-active candidate label；当前 raw receipt 没有
给 \(C=38\) 分配任何 label。式 (9) 给出的是一个精确选择：

\[
(\mu_2,H_3)\quad\text{对应}\quad A=573.
\tag{17}
\]

完整 phase-\(\zeta^{11}\) 候选为

\[
\begin{array}{c|c}
A&h\\ \hline
3&19\\
11&70715591,\ 495009137,\ 3465063959\\
573&19,\ 1014049,\ 3307571,\ 1334507617.
\end{array}
\tag{18}
\]

所以仅有 character phase 时没有唯一性。若未来 functor 还保留 cofactor 本身的
\(v_{19}(H)=3\)，则上表唯一的带标签选择是

\[
(A,H)=(573,H_3).
\tag{19}
\]

这是一个条件性的 candidate uniqueness，不是 raw occurrence 的分配定理。没有

\[
\text{occurrence}\longmapsto(a,b,H,\text{slot})
\tag{20}
\]

functor 前，不能由 raw occurrence 排除其它 candidate map 或 allocation。即使选择
\(A=573\)，\(H_{\rm base},H_{\rm base}19,H_{\rm base}19^3\) 也是同一个 \(N_A\) 中
嵌套的因子，不是三块独立的 physical source 或 slot。

此外，v=5 已有 \((m,d)=(3,11)\) direct Type II terminal。故本卡的 raw receipt 在
任何 selector dispatch 前都被 terminal-first 抢占。

## 5. 结论边界

本卡新增的是实际第三 occurrence 及其可重现相位/row 算术。它仍缺少完整
transition/source universe、(16) 的 functor、prefix request/layer allocation、
独立 physical slot、demand-to-slot、target-odd carrier、E4/E5 和 terminal-first
clearance。因此它不构成 Type II adapter、capacity 结论或递降边。

窄复现：

    python3 reproductions/type_i_c3_adaptive_core19_v5_c38_q19_phase_leaf.py --verify
