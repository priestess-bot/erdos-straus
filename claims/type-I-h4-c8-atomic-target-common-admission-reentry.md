---
kind: claim
claim_id: type-I-h4-c8-atomic-target-common-admission-reentry
title: H4/c8 原子目标的共用终结序列化与既有 overflow owner 重入
statement: >-
  对任一由 actual persistent parent、完整 terminal-first MISS、真实 H4_A1 或
  C8_DOUBLE_LOW path occurrence 与 canonical 双侧 complete-excess payload 共同确定的
  atomic target，先把 AtomicPendingTargetV1 仅作为非持久内部对象序列化，再从 target
  整数与 K_T 的完整素因子分解独立重算 Bradford terminal 及 centered hit/F/G。
  该过程唯一落在 terminal、recomputed F 或 recomputed G；pending_suffix、
  pending_dispatch 与 inherited label 均不成为最终状态。若非终止 target support
  A_T 严格大于 high checkpoint support A_H>B_p，且 target capacity c_T<C_P，
  则 R_T>p、A_T>1，common PersistentSelectorStateV1 facts 必命中现有
  type_i_a_gt_one_overflow_residual owner；固定 T5 N7 势由
  (p,TYPEI,CHARGED,0,C_P,0,0) 严降至
  (p,TYPEI,CHARGED,0,c_T,0,0)，E4 为 Sol(p) 恒等 lift。于是所有实际满足这些
  parent/path/low-capacity guards 的 H4/c8 F/G 输出可通过同一 common gate 重入，不需
  新 atomic F/G family 或非平凡 mark。本结论不证明 actual c8 double-low occurrence
  存在，也不关闭 c8 OTHER complement 或 H4 非 atomic 分支。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - type-I-path-anchored-atomic-split-total-typed-rechart
  - type-I-q-one-full-carrier-d-one-c-eight-double-low-parent-anchored-atomic-macro
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-atomic-macro-checkpoint-contraction
  - t6-persistent-selector-state-v1
  - type-I-t5-full-contract-level-global-well-foundedness
topics:
  - type-I
  - H4
  - c-eight
  - atomic-split
  - serializer
  - target-rechart
  - admission
  - reentry
  - well-foundedness
  - proof-boundary
sources:
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: canonical-parent-path-payload-target-and-identity-lift
  - claim: type-I-path-anchored-atomic-split-total-typed-rechart
    role: finite-target-terminal-hit-F-G-trichotomy
  - concept: t6-persistent-selector-state-v1
    role: noncircular-common-admission-and-owner-classification
  - reproduction: reproductions/f2_c8_atomic_pending_target_v1.py
    role: track-local-nonpersistent-serializer-and-target-disposition
  - reproduction: reproductions/f2_c8_atomic_common_admission_v1.py
    role: common-gate-projection-and-N7-reentry-controls
visibility: public
last_checked: '2026-08-24'
---
# H4/c8 原子目标的共用终结序列化与既有 overflow owner 重入

## 1. 定理准确处理什么

旧 atomic 接口留下两个惰性标记：H4 输出 `pending_suffix`，c8 输出
`pending_dispatch`。它们表达“目标整数已经构造，但类型还须重算”，不是一种数学状态，
也没有 recursive ticket。本定理把以下对象严格分开：

\[
\text{actual parent/path receipt}
\longrightarrow
\texttt{AtomicPendingTargetV1}
\longrightarrow
\text{terminal/F/G final disposition}
\longrightarrow
\text{common persistent admission}.
\tag{1}
\]

第一箭头仍由 source-specific H4/c8 定理负责；本定理不从裸 chart 或 fixed fixture
构造 actual parent。第二个对象只存在于一次原子动作内部，明确

```text
artifact_class = nonpersistent_atomic_serializer_input
must_never_enter_queue = true
```

最终输出禁止携带 `pending_suffix`、`pending_dispatch`、`later_selector` 或 inherited
F/G/hit label。

## 2. Canonical target 与完全重分类

设已验证的 source-specific atomic receipt 给出核心素数
\(p\equiv1\pmod {24}\)、persistent parent \(P\)、high checkpoint support \(A_H\)、
同一 scope 的 actual raw path 与双色完整超额块 \(Q_x,Q_y\)。令

\[
A_T=\operatorname{lcm}(A_H,Q_x,Q_y),
\qquad
c_T=\langle(4A_T)^{-1}\rangle_p,
\tag{2}
\]

\[
K_T=A_Tc_T,
\qquad
R_T=\frac{4K_T-1}{p}.
\tag{3}
\]

目标 `ChartFacts` 保存 \((p,R_T,K_T,A_T,c_T)\) 与 **完整 \(K_T\) 素因子分解**。
强调这里不是只分解 \(A_T\)：项目的 centered fiber 由 \(K_T\) 的全部素因子及估值定义。

先执行完整 Bradford terminal screen。若未命中，枚举

\[
B_\nu=\prod_{q^\nu\parallel K_T}[-\nu,\nu]
\tag{4}
\]

判断是否有

\[
\prod q^{z_q}\equiv-1\pmod {R_T}.
\tag{5}
\]

若有则为 centered hit terminal。若没有，再在有限 subgroup
\(\langle q:q\mid K_T\rangle\le U(R_T)\) 中判断 \(-1\)：属于 subgroup 为 F，
不属于为 G。三种情形互斥且穷尽；所有摘要都绑定 target chart digest。

因此内部对象没有第四种 `pending` 输出：

\[
\boxed{
\texttt{TARGET\_LOCAL\_TERMINAL}
\ \dot\cup\
\texttt{RECOMPUTED\_F}
\ \dot\cup\
\texttt{RECOMPUTED\_G}.}
\tag{6}
\]

## 3. 为什么 F/G 不需要新 family

source-specific H4/c8 strict atomic arm 的高支撑前提给出

\[
A_T>A_H>B_p=\frac{(p-1)^2}{4}.
\tag{7}
\]

又因为 \(1\le c_T\)，由 (3)、(7)

\[
R_T>p-2.
\tag{8}
\]

同时 \(R_T\equiv3\pmod4\)，而 \(p\equiv1\pmod4\)。大于 \(p-2\) 的首个
\(3\pmod4\) 整数是 \(p+2\)，所以实际有 \(R_T\ge p+2>p\)。

所以每个非终止 target 都满足

\[
A_T>1,
\qquad R_T>p,
\qquad A_T\mid K_T.
\tag{9}
\]

将 (9) 投影到 common `PersistentSelectorStateV1`：

```text
major_phase = TYPEI
provenance_kind = OVERFLOW
is_overflow = true
support_A = A_T > 1
atomic_arm = NONE
dispatch_status = NONE
```

活动 predicate 因而必命中

```text
type_i_a_gt_one_overflow_residual.
```

F/G 留在 independently recomputed `certificate_context`；它们不是 family 名称，也不参与
owner 的定义。故接口请求中的新 `type_i_atomic_f_reentry_target_v1`、
`type_i_atomic_g_reentry_target_v1` family **不需要批准**。H4 与 c8 可用不同 producer/branch，
但共享同一个内部 serializer 和同一个最终 owner。

## 4. Parent-to-final E1--E5

假定 source-specific receipt 已独立支付：

1. actual persistent parent id 与完整 terminal-first MISS；
2. parent-to-H4/c8 checkpoint path；
3. actual raw occurrence 与 canonical two-color payload；
4. (2)--(3) 的唯一 target；
5. \(A_T>A_H>B_p\) 与 \(c_T<C_P\)，其中 \(C_P\) 是 persistent parent 的
   CHARGED capacity。

则 E1 是第 1--3 项，E2 是第 4 项，E3 是第 2 节重分类及第 3 节 common gate，E4 为

\[
W_T=W_P=\operatorname{Sol}(p),
\qquad
\Phi_{T\to P}=\operatorname{id}.
\tag{10}
\]

固定 T5 registry 的 Type-I CHARGED local rank 为

\[
\left(\left\lfloor\frac{B_p}{A}\right\rfloor,
\frac KA,\eta_p,0\right).
\tag{11}
\]

由 \(A_H,A_T>B_p\)，parent 与 target 第一坐标均为零；这里没有 immediate
regeneration token，故 \(\eta_p=0\)。第 5 项给出

\[
\boxed{
(0,C_P,0,0)>(0,c_T,0,0).}
\tag{12}
\]

major phase/protocol 均保持 `TYPEI/CHARGED`，所以 (12) 是 parent-to-final 的
`LOCAL_DROP`，不是 checkpoint-local 排名。finalizer 在 target N7 不严格或 common
re-entry 未通过时失败闭合。

## 5. 两个 common-gate 控制与证明边界

### 5.1 Capacity-one 的精确跨 track 边界

c8 的 universal second-full-excess fallback 另有全称公式

\[
75c_T\equiv64\pmod p,
\qquad 9\le c_T\le p-2,
\tag{13}
\]

所以它不会产生 high-support \(C=1\)。即使某个 optional double-low target 的容量为
1，selector 也可改走该 universal fallback；c8 outgoing totality 不依赖输出 C1。

H4 atomic target 则不同。已有 exact capacity formula 为

\[
c_q\equiv-qE_x^{-1}\pmod p.
\tag{14}
\]

因此

\[
\boxed{c_q=1\iff E_x\equiv-q\pmod p.}
\tag{15}
\]

仓库此前关闭的是 stutter 类 \(E_x\equiv q\pmod p\)，不能借此排除 (15)。写

\[
p=2dq-1,
\qquad
\delta_d=2d(4d^2-2d+1),
\tag{16}
\]

并令 \(D=(M_4,Q_x)\beta_x\)。从同一 source identity
\(qE_xD\equiv q+2d-1\pmod p\) 与 \(q^{-1}\equiv2d\pmod p\)，(15) 给出

\[
\boxed{D\equiv-\delta_d\pmod p.}
\tag{17}
\]

而 source divisibility 不依赖正负号，仍给

\[
\boxed{
D\mid(2d-1)((2d+1)q-1),
\qquad0<D<2dp.}
\tag{18}
\]

actual H4 provenance 还要求 \(d\mid|1536-a(p)|\) 及完整 31-phase、parent/path、
payload 和 priority receipts。仅 (17)--(18) 的算术层并非自动矛盾，例如

\[
(d,q,p,D)=(23,47,2161,4140),
\qquad(35,71,4969,9660)
\tag{19}
\]

满足 \(p,q\) 为素数及负残数/整除门。这两行没有被断言满足 actual 31-phase 或任何
persistent receipt，只是防止把“尚未证明 C1 不可达”误写成 trace-unreachability。
若 actual H4 C1 最终通过 common gate，它会进入现有 high-support owner；同
`TYPEI/CHARGED` 下的后续 complete-excess 已由
`type-I-high-support-empty-improvement-c1-local-minimum-boundary` 证明是局部最小，
必须由其 owner 提供 terminal、lower protocol/phase 或 family-empty 证明。

focused verifier 使用两个独立 chart 控制：

1. \(p=73\) 的已知高支撑严格 target
   \((R,K;A,c)=(315581377367,5759360136948;2879680068474,2)\)。centered box
   不命中，且 \(11^{(R-1)/2}\equiv-1\pmod R\)，故独立重算为 F。
2. \(p=2137\) 的 \((R,K;A,c)=(8551,4568372;1142093,4)\)。完整 \(K\)-support
   在模 \(R\) 的 subgroup 不含 \(-1\)，故独立重算为 G。

两者分别以 `H4_A1`、`C8_DOUBLE_LOW` producer proposal 投影，真实调用 common
`reject_before_persistent_queue_v1`，均得到 owner
`type_i_a_gt_one_overflow_residual`。它们检验实现与定理接口；它们不证明这两个 chart
就是 actual H4/c8 output，也不代替上述全称条件证明。

本定理关闭的是：

```text
actual admitted H4/c8 low-capacity atomic output
    -> no pending marker
    -> target-local terminal/F/G
    -> existing overflow owner
    -> common admission and strict N7 re-entry
```

它没有关闭：

```text
c8 outgoing existence
c8 non-double-low complement
H4 non-atomic branches
source-specific actual occurrence existence
F2 totality or global T6
```

聚焦复核：

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests.test_f2_c8_atomic_pending_target_v1 \
  tests.test_f2_c8_atomic_common_admission_v1 -v
```
