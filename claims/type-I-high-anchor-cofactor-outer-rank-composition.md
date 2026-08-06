---
kind: claim
claim_id: type-I-high-anchor-cofactor-outer-rank-composition
title: 高锚点 direct cofactor 与外层支撑秩重置的词典序拼接
statement: 固定核心素数 \(p\equiv1\pmod {24}\)，令 \(B_p=(p-1)^2/4\)、\(\Pi_p(A)=\lfloor B_p/A\rfloor\)。在只含两类非终端边的固定 \(p\) 子图中：(D) canonical、通过 gate 的高锚点 direct cofactor 宏步，且抑制 \(h=0,c=1\) 的完整自环；(O) 已独立满足 \(\Pi_p(A_T)<\Pi_p(A_S)\) 的外层秩边，所有顶点的 charged support 都整除其 \(K\)。则 \(\Lambda_p=(\Pi_p(A),\Omega(K/A))\) 是严格良基的 E5 秩。特别地，带 `support_reset_paid` 的 fixed-n/fixed-s bounded-divisor 边可以安全结束一个 high-cofactor epoch 并重置其 token/局部元数据，因为第一坐标严格下降；但没有 \(\Pi_p\) 支付的 forgetful RESET、跨 \(p\) 或 capability-changing \(c=1\) 自环不在该定理范围内。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-anchor-three-phase-nonreturn-window
  - type-I-high-anchor-direct-cofactor-lexicographic-rank
  - type-I-overflow-fixed-n-overflow-rank-descent
  - type-I-overflow-fixed-n-bounded-divisor-saturation
  - type-I-overflow-fixed-s-dual-outer-rank-descent
  - type-I-overflow-fixed-s-bounded-divisor-saturation
  - type-I-overflow-outer-rank-reset
  - type-I-overflow-same-chart-support-promotion
  - type-I-overflow-phase-reset-cycle-boundary
topics:
  - type-I
  - high-carrier
  - r-chart
  - outer-rank
  - support-reset
  - phase
  - well-founded-descent
  - scheduler
  - proof-boundary
sources:
  - claim: type-I-high-anchor-three-phase-nonreturn-window
    role: direct-cofactor phase and support-multiplier identities
  - claim: type-I-overflow-fixed-n-bounded-divisor-saturation
    role: fixed-n paid-reset E1--E5 edges
  - claim: type-I-overflow-fixed-s-bounded-divisor-saturation
    role: fixed-s paid-reset E1--E5 edges
  - reproduction: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: frozen paid-reset and RESET-cycle compatibility checks
  - reproduction: reproductions/type_i_high_anchor_token_exit_p73_reentry.py
    role: focused paid-exit and reentry boundary at p=73
visibility: public
last_checked: '2026-08-06'
---

# 高锚点 direct cofactor 与外层支撑秩重置的词典序拼接

## 1. 问题与范围

direct high-cofactor 的正相位 token 只在同一不重置链中有效；而 fixed-\(n\)、
fixed-\(s\) 有界除子允许由严格外层势支付 `support_reset_paid`。两者此前没有
共同的 E5 账本，因此不能仅因每一段各自下降，就断言 token exit 后仍无循环。

本卡给出恰好需要的拼接。固定

\[
p\equiv1\pmod {24},\qquad B_p=\frac{(p-1)^2}{4},\qquad
\Pi_p(A)=\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{1}
\]

考虑一个固定 \(p\) 的递归子图。每个非终端顶点至少是一个合法 charged chart

\[
pR+1=4K,\qquad A\mid K,\qquad R>0.
\tag{2}
\]

并且每条非终端边只能属于下列两类。

1. **D（direct cofactor）**：source 是高锚点 \(p<R<4A\)，并通过
   \(A_C=\operatorname{lcm}(A,C)\mid rC\) gate；target 持久化
   \(A_T=A_C\)。所有 terminal/alternate 分派已经先执行。若 \(h=0,c=1\)，
   只有在完整 state、capability 和 bundle digest 都不变时才把它作为
   `STUTTER_EXHAUSTED`，不入递归队列。
2. **O（外层秩边）**：E1--E4 已由独立合同证明，且它的非终端 successor 仍满足
   (2) 并明确携带
   \[
   \Pi_p(A_T)<\Pi_p(A_S).
   \tag{3}
   \]
   这里允许 \(A_S\nmid A_T\)，也允许 token、epoch 或其他局部字段被重置；
   (3) 是唯一允许这种重置的付款。

这一定义故意不把尚无 (3) 的 forgetful RESET、跨素数边、raw/noncanonical
carrier，或改变 capability 的同算术 \(c=1\) action 放进图中。

令 \(\Omega(n)\) 为 \(n\) 的素因子重数总数，\(\Omega(1)=0\)。定义

\[
\boxed{
\Lambda_p(p,R,K;A)=
\left(\Pi_p(A),\ \Omega(K/A)\right)
\in\mathbb N_0^2
}
\tag{4}
\]

并采用第一坐标优先的字典序。

## 2. 一个基本的容量倍增事实

若 \(1\le A\le B_p\) 且 \(c\ge2\)，则

\[
\boxed{\Pi_p(cA)<\Pi_p(A).}
\tag{5}
\]

事实上，令 \(q=\lfloor B_p/A\rfloor\ge1\)。由
\(B_p/A<q+1\)，有

\[
\frac{B_p}{cA}\le\frac{B_p}{2A}<\frac{q+1}{2}\le q.
\]

左端的整数部分因此小于 \(q\)，即得 (5)。这一步不要求 \(cA\le B_p\)；
越出容量盒时 successor 的 \(\Pi_p\) 只是变成零。

## 3. direct cofactor 的逐相位支付

对 D 边，按三相引理的记号写

\[
K=AB,\qquad g=(A,C),\quad A=ga,\quad C=gc,\quad r=at,
\]

并令

\[
h=\frac{rC-K}{pA},\qquad A_T=Ac,\qquad K_T=rC=Act,
\qquad ct=B+ph.
\tag{6}
\]

已有三相引理给出 \(h\in\{0,1,2\}\)。下列三种情形穷尽所有 D 宏步。

### 3.1 正相位 \(h>0\)

正相位支付界给出 \(c\ge h+1\ge2\)，而正相位 source barrier 给出

\[
A< p.
\tag{7}
\]

核心素数范围内 \(p\ge73\)，所以 \(p-1\le B_p\)。因此
\(A\le p-1\le B_p\)，由 (5)

\[
\Pi_p(A_T)=\Pi_p(cA)<\Pi_p(A).
\tag{8}
\]

不必控制 \(\Omega(K_T/A_T)=\Omega(t)\)：第一坐标已经严格支付此步。特别地，
这比只在一个 scope 中消费一次 token 更强，因为 E5 不依赖 token 是否可由外部
epoch 改写。

### 3.2 严格零相位 \(h=0,\ c>1\)

此时 (6) 化为

\[
K_T=K,\qquad A_T=cA,\qquad c\mid B,
\qquad \frac{K_T}{A_T}=\frac{B}{c}.
\tag{9}
\]

若 \(A\le B_p\)，由 (5) 仍有第一坐标严格下降。若 \(A>B_p\)，则
\(\Pi_p(A)=\Pi_p(A_T)=0\)，但 (9) 给出

\[
\Omega(K_T/A_T)
=\Omega(B/c)
=\Omega(B)-\Omega(c)
<\Omega(B).
\tag{10}
\]

所以这两种子情形均使 \(\Lambda_p\) 严格下降。

### 3.3 精确零相位 \(h=0,\ c=1\)

式 (9) 现在给出

\[
(R_T,K_T;A_T)=(R,K;A).
\tag{11}
\]

故 (4) 不下降。这不是技术性例外：\(p=97\)、
\((R,K;A)=(99,2401;2401)\) 有实际的 \(c=1\) macro self-loop。它只能在
terminal-first 和 alternate 检查完成后、且完整 action digest 不增加任何能力时被抑制；
否则需要另一个独立的 capability 秩，不能偷用本引理。特别地，调度器必须提供
规范的有限 action menu，或为尚未尝试的 action 引入严格的 `remaining_actions` 秩；
不能因算术 checkpoint 相同而把不同 bundle 的新证明能力静默丢弃。

由 3.1--3.3 可得：

\[
\boxed{\text{每一条被入队的 D 边都严格降低 }\Lambda_p.}
\tag{12}
\]

## 4. 外层重置的拼接定理

**定理。** 在第 1 节定义的子图中，\(\Lambda_p\) 是每条非终端边的严格良基 E5 秩。

**证明。** D 边由 (12) 严格下降。对 O 边，(3) 直接使 (4) 的第一坐标严格下降，
所以不论 \(K_T/A_T\)、token、scope、epoch 或 capability 的后续值为何，均有

\[
\Lambda_p(T)<_{\rm lex}\Lambda_p(S).
\tag{13}
\]

\(\mathbb N_0^2\) 的字典序良基，故不存在无限的非终端 D/O 路径。证毕。

这正是 `token_exit` 的严格含义：它不是自由重入，而是

```text
direct epoch --[Pi strictly decreases]--> token_exit / new epoch
```

因此新 epoch 可以使用新的 high-nonreturn token；其局部重置已经由更高优先级的
\(\Pi_p\) 付款。相反，普通 token carry 边不必重置 token，而没有 (3) 的 exit
永远不能由这一定理授权。

## 5. 已有外层边的兼容性

下列既有 normal form 都把 (3) 作为 E5 的显式条件，故只要 endpoint 满足第 1 节的
charged-state 条件，就可作为 O 边。若 O 的 target 还要进入 D，则另须在该点独立满足
high-canonical/gate 与 parent-adapter 条件：

- `overflow_fixed_n_outer_rank_reset_v1`；
- `overflow_fixed_n_bounded_divisor_outer_rank_v1`；
- `overflow_fixed_s_outer_rank_reset_v1`；
- `overflow_fixed_s_bounded_divisor_outer_rank_v1`；
- `overflow_outer_rank_reset_v1`；
- `overflow_same_chart_support_promotion_v1`。

特别地，有界 fixed-\(n\)/fixed-\(s\) 的 `support_reset_paid=true` 不再是
high-cofactor token 的未支付漏洞：它们逐回执保存
\(\Pi_p(A_T)<\Pi_p(A_S)\)。冻结结果中有 8 条这样的 verified receipt（fixed-\(n\)
与 fixed-\(s\) 各 4 条）；其中 7 条落入 chart-level high region，余下的
\(p=73,A:7\to18,R_T=71<p\) 是 marked absorb。这个枚举只检验当前回执与本定理的
接口兼容，不是其全称存在性证明。

例如 \(p=73\) 的 fixed-\(n\) paid reset 把

\[
A:19\longmapsto1034,
\qquad \Pi_{73}:68\longmapsto1,
\tag{14}
\]

所以即使 \(19\nmid1034\)，新 epoch 仍被第一坐标严格置于旧 epoch 之下。

对 \(p=73\) 的专用、只读复核进一步排除了一个容易误判的局部重入情形。8 条
`support_reset_paid` 中唯一有 \(A_T<p\) 的回执是

\[
(A,R,K)=(7,359,6552)\longmapsto(18,71,1296),
\qquad \Lambda_{73}:(185,6)\longmapsto(72,5).
\tag{15}
\]

在 \(A<p\) 范围内，保留 \(18\) 的可能 support 为
\(18,36,54,72\)，其 canonical chart 都有 \(R=71<p\)，所以不会进入 D 的高锚点
入口。纯 chart 枚举虽在 \(A=31,34\) 找到 \(h=1\) gate，但强制当前
complete-excess bundle 后，23 个小 high chart 中唯一通过 gate 的是
\(A=69,R=155,h=0\)。因此当前发生器没有给这个素数制造“paid exit 后实际正相位
重入”。这是冻结回执及当前 bundle adapter 的有限事实，不是对任意 \(p\) 或任意
future adapter 的存在性定理。

## 6. 可数深度界

O 边的 source 不必相对于其 charged support canonical，所以不能把
\(K/A<p\) 当作全图不变量。不过路径仍有下列显式界。只要
\(\Pi_p(A)>0\)，每条 O 边按定义降低第一坐标；每条被入队的 D 边也按第 3 节降低
第一坐标（此时 \(A\le B_p\)）。因此到达 \(\Pi_p=0\) 之前至多经过
\(\Pi_p(A_0)\) 条边。

在 \(\Pi_p=0\) 时，O 边不可能存在。若路径还能走 D，则该 D source 按定义是
canonical high chart；于是

\[
\frac KA<p.
\tag{16}
\]

这是因为 \(K/A<p+1/(4A)\) 且 \(K/A\) 为整数；等号 \(K/A=p\) 又会使
\(p\mid(pR+1)\)，不可能。正相位也不可能存在，因为它会要求
\(A<p<B_p<A\)，而 \(c=1\) 已被抑制。因此只剩严格零相位，它保持 canonical chart
并按 (10) 递减第二坐标；且

\[
\Omega(K/A)\le\left\lfloor\log_2(p-1)\right\rfloor.
\tag{17}
\]

若某条 O 边直接抵达非canonical 的 \(\Pi_p=0\) 状态，它在本 D/O 模块中没有后继，
这不会增加路径长度。故从任一初始状态出发，本子图中非终端宏边的数目至多为

\[
\boxed{
\Pi_p(A_0)+\left\lfloor\log_2(p-1)\right\rfloor.
}
\tag{18}

这只是所定义 D/O 模块的深度界，不是整个 selector 的路径界。

## 7. 精确边界

本定理只完成 E5 的拼接，不改变任何 cofactor receipt 的 E1--E4 身份。当前 direct
cofactor r-chart 仍须逐条给出完整 parent ledger、F/G lift、state capability 和
terminal-first 结果，才可从 `candidate_transition` 升为递归边。

尤其不能把 p=73 的 forgetful RESET 重新放进图中：其 continuation 有

\[
132\longmapsto330\longmapsto132,
\qquad \Pi_{73}:9\longmapsto3\longmapsto9,
\tag{19}
\]

第二步没有严格 \(\Pi_p\) 支付，正是被本卡排除的无成本重入。跨 \(p\)、raw
carrier、任意 support-decreasing edge，以及 metadata 改变的 \(c=1\) action 也都
需要额外且不可重置的外层秩；不能把 (4) 外推到它们。

若将本卡实现为 scheduler wrapper，state identity 至少还须绑定 \(p,R,K,A\)、
normal form、E1--E4/lift receipt digest、root-entry/source-tree scope、charged-parent
adapter、direct epoch、canonical checkpoint 以及 terminal/alternate action-menu digest。
`high_nonreturn_token` 可以保留为诊断和 provenance 字段，但不再承担 E5；新的
direct epoch 只能经 (3) 的付费父边开启，而不是重写根 epoch 或遗忘旧 action 账本。
