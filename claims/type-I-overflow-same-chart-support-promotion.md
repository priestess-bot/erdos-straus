---
kind: claim
claim_id: type-I-overflow-same-chart-support-promotion
title: overflow 同图表支撑升级
statement: 设已验证来源回执给出的 overflow canonical chart 满足 pn=4Md+1、R_M>p，并携带 A|M、M/A≥2 和 M≤B_p=(p-1)^2/4。则在不改变 (p,R_M,K_M) 图表的情况下，可把 absorbed support 从 A 升到 M；由于 M|K_M、Sol(p) 对图表独立且 floor(B_p/M)<floor(B_p/A)，这给出完整 E1--E5、恒等解提升和严格外层秩下降的同图表 overflow 后继。后续精确秩 (floor(B_p/A),K/A) 已把该定理扩展到任意 M：第一坐标不降时第二坐标严格下降；真正边界改为 source 必须 persistent，transient receipt 必须比较真实 parent target。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-marked-support-accumulation-rechart-saturation
  - type-I-overflow-fixed-n-bounded-divisor-saturation
  - denominator-escape-state-contract
topics:
- type-I
- overflow
- complete-excess
- same-chart
- support-promotion
- outer-rank
- high-carrier
- complement-boundary
- marked-solution
- proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: same-chart support promotion implementation and verifier
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: focused source-row replay
visibility: public
last_checked: '2026-08-11'
---

# overflow 同图表支撑升级

## 1. 来源条件

设一个已验证来源回执的 overflow 已规范化为

\[
4K_M=pR_M+1,\qquad K_M=MC,\qquad R_M>p,
\]

并令

\[
n=4M-R_M,\qquad d=p-C.
\]

于是

\[
pn=4Md+1.
\tag{1}
\]

设当前状态携带 absorbed support \(A\)，满足

\[
A\mid M,\qquad \frac{M}{A}\ge2,\qquad
M\le B_p:=\frac{(p-1)^2}{4}.
\tag{2}
\]

\(M/A\ge2\) 是 bundle 容量确实在旧 support 之外增加了至少一个因子的结构条件；
它不能从任意行列式四元组自动推出，必须由来源回执提供。complete-excess bundle、已有
overflow 重入边或其它已验证来源都必须逐行核验这一条件。

## 2. 同图表后继

把同一个 canonical chart 的 absorbed support 改写为

\[
A'=M.
\]

因为 \(K_M=MC\)，有 \(A'\mid K_M\)。图表本身不变，所以

\[
(p,R_M,K_M;A')
\]

仍是合法 overflow 状态。标记集取图表无关的 \(\operatorname{Sol}(p)\)，并用恒等映射
\(W_T=W_S=\operatorname{Sol}(p)\) 提升全部标记解。

外层势为

\[
\Pi_p(A)=\left\lfloor\frac{B_p}{A}\right\rfloor.
\]

由 \(M/A\ge2\) 和 \(M\le B_p\)，有 \(M>A\)，且

\[
\Pi_p(M)
=\left\lfloor\frac{B_p}{M}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor
=\Pi_p(A).
\tag{3}
\]

因此 E1 由同一 canonical chart 和 (1) 给出，E2 由 \(M\mid K_M\) 给出，E3 由
来源回执给出，E4 由 \(\operatorname{Sol}(p)\) 恒等提升给出，E5
正是 (3)。这是一条完整的
overflow_same_chart_support_promotion_v1 verified edge。

注意 \(R_M>p\) 没有改变：该边只支付 support phase 的严格下降，目标仍须交给后续
overflow 选择器，不能把同图表升级误写成 Type I/II 终端。

## 3. 余项收缩

这条引理立即排除所有满足 (2) 的来源回执 overflow。若 \(M>B_p\)，同图表升级不能
使用当前外层势，因为 \(\Pi_p(M)=0\) 不再属于该势域。更强的算术边界如下。令

\[
S=Md=\frac{pn-1}{4}.
\]

若 \(n\le p-4\)，则 \(S<B_p\)，与 \(S\ge M>B_p\) 矛盾；\(n=p\) 时

\[
S=\frac{p^2-1}{4}=B_p+\frac{p-1}{2}>B_p,
\]

恰好允许。又 \(n\equiv1\pmod4\)，故高载体残差满足

\[
n=p\quad\text{或}\quad n\ge p+4.
\]

这些状态仍需要 bounded divisor、固定-\(s\) alternate、直接 Type I/II 或另一个
不可重置外层秩。

对当前 12 个聚焦来源行，selector 重放得到 11 条同图表 verified edge；唯一被该
分支拒绝的是 lcm_cycle_step_0，其

\[
p=73,\qquad M=1518>B_{73}=1296.
\]

这个计数只是回放证据，不是全称扫描；全称结论由 (1)--(3) 的条件性定理承担，
高载体边界由 \(S=Md\) 的不等式给出。

## 复现

    python3 reproductions/type_i_representation_dual_capacity_selector.py --verify

## 下游无界升级

本卡使用的单坐标势只覆盖 \(M\le B_p\)。后续精确容量秩

\[
\Lambda_p^\sharp(S)
=\left(\left\lfloor\frac{B_p}{A_S}\right\rfloor,\frac{K_S}{A_S}\right)
\]

已经删除该上界：对真实 persistent source，只要 \(A\mid M\mid K_M\) 且
\(M>A\)，第一坐标若不降，第二坐标仍从 \((M/A)(K_M/M)\) 严降到
\(K_M/M\)。因此上文的 `lcm_cycle_step_0` 不再是同图表拒绝项；它产生
\((R,K;A)=(3743,68310;1518)\) 的合法高支撑 target。

必须保留的边界改为 persistence：若 overflow chart 只是 parent 内部 receipt，不能
把 transient-to-target 的下降记在 parent 上。该高支撑 target 在 sink 最小节点的
实际 F bundle 给出 parent 容量 \(45\to47\) 上升，而内部 receipt 会伪示
\(87937\to47\) 下降。完整边界见
[overflow 同图表支撑升级的无界精确秩与高支撑父端点边界](type-I-overflow-unbounded-same-chart-promotion-persistence-boundary.md)。
这只排除该 candidate；后续遍历完整 sink SCC 的 rank-aware 选择器以一条额外 raw
边构造了 \(45\to44\) 的真实出口，见
[高支撑 rank-aware sink-bundle 有限选择器](type-I-high-support-rank-aware-sink-bundle-selector.md)。
