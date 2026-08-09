---
kind: claim
claim_id: type-I-overflow-cofactor-mod-p-fold-r-descent
title: overflow 余因子整体模 p 折叠的严格局部 R 下降
statement: >-
  设核心素数 p=1 (mod 24) 的 verified overflow 满足 pn=4Md+1、1<=d<p，
  并携带 charged support A|M、1<=A<=B_p。写 M=Ab、b>1。对任意 g|b、g>1，
  将 dg=ph+delta 规范化为 1<=delta<p，并令
  (M_T,d_T,n_T;A_T)=(M/g,delta,n-4(M/g)h;A)。该目标总是保留 charged support
  的合法 canonical 算术图表，并严格降低局部势
  (floor(B_p/A),R) 当且仅当 g(p-d)>p。若 g(p-d)<=p，源与目标的 canonical
  (R,K;A) 完全相同，只是不可作为递归边的重分解。特别地，当 M>=2B_p、A<=B_p、
  d^2<p 时，取 g=b 自动满足严格条件，故每个这类高容量 small-d overflow 都有
  一条 support-preserving 的严格局部算术 candidate_transition。该卡只建立该
  重图表及局部下降；后续 canonical 投影定理已对真实 queued source 给出精确
  (floor(B_p/A),K/A) 秩，但升级为 verified_edge 仍须重算目标 typed state、F/G/纤维、
  source scope 与解提升，并通过区分真实 source 和内部 receipt 的 persistence gate。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-cofactor-factor-exchange-carrier-descent
topics:
  - type-I
  - overflow
  - cofactor
  - quotient-fold
  - mod-p
  - R-descent
  - charged-support
  - high-capacity
  - small-d
  - well-founded-descent
  - selector
  - candidate-transition
  - proof-boundary
sources:
  - claim: type-I-overflow-cofactor-factor-exchange-carrier-descent
    role: shared-verified-overflow-and-solution-lift-contract
  - reproduction: reproductions/type_i_overflow_cofactor_mod_p_fold_r_descent.py
    role: focused-arithmetic-strict-and-stutter-receipts
visibility: public
last_checked: '2026-08-09'
---

# overflow 余因子整体模 \(p\) 折叠的严格局部 \(R\) 下降

## 设置

令 \(p\equiv1\pmod {24}\) 为核心素数，且一个已有 source/path/node 回执的
verified overflow 满足

\[
pn=4Md+1,\qquad 1\le d<p.
\tag{1}
\]

设当前 charged support 为

\[
A\mid M,\qquad 1\le A\le B_p:=\frac{(p-1)^2}{4},
\qquad M=Ab,\quad b>1.
\tag{2}
\]

以下是 support-preserving 的 rechart；它不丢弃 \(A\)，也不使用一个较小
载体去重置 support。

## 整体余因子折叠

取任意 \(g\mid b\)、\(g>1\)。因为 \(p\nmid Md\)，也不整除 \(g\) 或 \(d\)，故
Euclidean 分解唯一写成

\[
dg=ph+\delta,
\qquad h\ge0,\qquad 1\le\delta<p.
\tag{3}
\]

令

\[
M_T=\frac Mg,\qquad
d_T=\delta,\qquad
n_T=n-4M_Th,\qquad
A_T=A.
\tag{4}
\]

则

\[
\begin{aligned}
p n_T
&=p(n-4M_Th)\\
&=4M_Tdg+1-4M_Tph\\
&=4M_T\delta+1.
\end{aligned}
\tag{5}
\]

右端为正，故 \(n_T>0\)。又

\[
p n_T\le4M_T(p-1)+1<4M_Tp,
\tag{6}
\]

所以 \(0<n_T<4M_T\)。定义

\[
R_T=4M_T-n_T,
\qquad
K_T=M_T(p-\delta).
\tag{7}
\]

由 (5) 得

\[
R_T>0,\qquad R_T\equiv3\pmod4,\qquad K_T>0,
\qquad pR_T+1=4K_T.
\tag{8}
\]

并且 \(A=A_T\mid M_T\mid K_T\)。因此 (4) 总给出一个合法的 canonical 算术图表，
并完整保留 charged support。

## 严格性判据与不可删的 stutter 门

源 chart 的规范坐标为

\[
R_S=4M-n,\qquad K_S=M(p-d).
\tag{9}
\]

由 (4) 直接得到

\[
\boxed{R_T-R_S=4M_T(1+h-g).}
\tag{10}
\]

因为 \(d<p\)，有 \(h=\lfloor gd/p\rfloor\le g-1\)。等号的精确条件是

\[
h=g-1
\Longleftrightarrow
dg\ge p(g-1)
\Longleftrightarrow
g(p-d)\le p.
\tag{11}
\]

在该非严格情形，\(\delta=p-g(p-d)\)，从而

\[
K_T=M_T(p-\delta)=M(p-d)=K_S,
\qquad R_T=R_S.
\tag{12}
\]

它只是同一 \((R,K;A)\) 的重分解，不能登记为递归边。因此可接受的严格门恰为

\[
\boxed{g(p-d)>p.}
\tag{13}
\]

此时 \(h\le g-2\)，(10) 给出 \(R_T<R_S\)。由于 support 未变，局部良基势

\[
\Lambda_{\mathrm{loc}}(M,d;A)=
\left(\left\lfloor\frac{B_p}{A}\right\rfloor,R\right)
\tag{14}
\]

严格下降。这个势覆盖同一 dispatcher 中的因子转移和余因子交换（它们同样保持
\(A\) 且严格降低 \(R\)），而 fixed-\(s\) 与 bounded shell fold 先严格降低
第一坐标。它本身仍只是局部菜单势；后续的
[canonical 投影与持久化秩](type-I-overflow-total-cofactor-canonical-projection-persistence-rank.md)
用精确 \(K/A\) 替代 \(R\)，并在真实持久端点组成的固定 \(p\) 子图上给出 E5。

## 高容量 small-\(d\) 的算术候选闭合

现在加入

\[
M\ge2B_p,\qquad A\le B_p,\qquad d^2<p.
\tag{15}
\]

由前两项，

\[
b=\frac MA\ge2.
\tag{16}
\]

又 \(p\ge73\) 时 \(d^2<p\) 蕴含 \(d<\sqrt p<p/2\)。取整体余因子
\(g=b\)，便有

\[
b(p-d)>p.
\tag{17}
\]

故 (13) 自动成立，得到显式严格后继

\[
\boxed{
(M,d,n;A)\longmapsto
\left(
A,\;
bd\bmod p,\;
n-4A\left\lfloor\frac{bd}{p}\right\rfloor;\;
A
\right).
}
\tag{18}
\]

若一个具名 target-state adapter 证明 \(R_T<p\) 的目标是 marked absorb，或证明
\(R_T>p\) 的目标是带完整状态字段的 overflow，并确认当前 source 本身是持久队列顶点，
则后续定理的精确 \(K/A\) 秩可支付 E5。这里不再需要因子转移、交换或
\(\operatorname{Div}(bd)\) 是否穿过一个有界容量壳；但这只排除了该算术
rechart 菜单中的余项，尚未生成可递归的完整状态回执。

## 完整状态合同边界

式 (3)--(8) 只重算了算术坐标、正性、canonical 条件与 charged support，因而只覆盖
E2 的算术部分。它不自动继承一个 target state 的 source/path/node scope（E1），也没有
重算 target 的 F/G 标签、hit、纤维、state_id 或状态正规形（E3）。
\(W_T=W_S=\operatorname{Sol}(p)\) 的恒等提升（E4）也只能由一个实际适用的具名
adapter 在 source/target 两端重放后取得；不能由 (5) 单独推出。

后续 canonical 投影定理已经证明：若 source 是真实 queued/content-addressed 顶点，
则 \(\bigl(\lfloor B_p/A\rfloor,K/A\bigr)\) 可与 paid outer-rank 和既有
direct-cofactor 边拼成严格 E5；若当前 determinant chart 只是 parent 内部 receipt，
则必须比较真实 parent--target 端点，不能用 receipt 的下降付款。由于本卡尚未建立这项
persistence 绑定及 E1--E4，当前结果仍登记为 `candidate_transition`、
`recursive_edge_eligible=false`，而非 `verified_edge` 或归纳边。升级所需的最小工作是：

1. 实现并命名一个 target-state adapter，重算 source/target 的 typed fields、F/G、
   hit、纤维与 source scope；
2. 在该 adapter 中回放恒等解提升；
3. 在回执中保存 `persistence_source_state_id` 与真实 parent--target 端点，并重算
   \(\bigl(\lfloor B_p/A\rfloor,K/A\bigr)\) 的前后值；内部 receipt 不得作为秩 source。

严格门不能删除。例如

\[
(p,n,M,d,A,b)=(73,16057,4070,72,74,55)
\]

满足 \(bd=73\cdot54+18\)。折叠后

\[
(M_T,d_T,n_T;A_T)=(74,18,73;74),
\]

但源与目标均为

\[
(R,K;A)=(223,4070;74).
\]

这正是 (11) 的 stutter 情形，故任何仅以 \(M_T<M\) 付款的论证都不够。

## 聚焦复现

    python3 reproductions/type_i_overflow_cofactor_mod_p_fold_r_descent.py --verify

复现器覆盖三个先前的 floor-shell 算术余项、一个 \(d>1\) 控制、一个 proper-cofactor
严格控制和上述 stutter 边界；只核验本引理的精确算术、support persistence 与
严格性判据，不做历史范围扫描，也不声称 state-contract 回放。
