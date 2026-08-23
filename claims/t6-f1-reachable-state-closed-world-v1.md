---
kind: claim
claim_id: t6-f1-reachable-state-closed-world-v1
title: T6-F1 可达持久状态闭世界的条件引理与当前最小断点
statement: >-
  在非循环 PersistentSelectorStateV1 合同下，已证明 verified header 的合法重叠命中集
  经固定 precedence 有唯一 owner；新 admission gate 对零命中、非法重叠、未知 producer
  和未声明 target 均在入队前失败；并且在 initializer 基础步 B、逐 constructor 重入步 S
  与唯一 gate 假设 X 下，有限迹归纳给出所有实际可达持久状态均有唯一 owner。但是当前
  活动源码既无统一 persistent queue/enqueue gate，也有 9 个 unresolved producer/serializer
  项；C=2 的 H3 仅到 nonrecursive pending-dispatch，若干 registry edge 只有 conditional
  controls，另有未登记的 recursive-edge signals。因此 A2 的逐 constructor guard partition、
  A3 的 family totality、实际 re-entry 与无旁路迹归纳均未建立，T6-F1 必须保持 OPEN。
claim_status: open
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-initial-q-one-root-terminal-or-full-carrier-dispatch
  - type-II-q-one-full-carrier-phase-root-entry
  - type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-atomic-macro-checkpoint-contraction
  - type-I-q-one-full-carrier-d-one-c-eight-double-low-parent-anchored-atomic-macro
  - denominator-escape-state-contract
topics:
  - T6
  - F1
  - reachable-state
  - closed-world
  - constructor
  - serializer
  - guard-partition
  - owner
  - re-entry
  - trace-induction
  - proof-boundary
sources:
  - concept: t6-persistent-selector-state-v1
    role: noncircular-header-owner-admission-and-conditional-induction-kernel
  - data: t6-constructor-inventory-v1.json
    role: source-derived-constructor-and-serializer-inventory
  - data: t6-f1-reachability-proof-receipt-v1.json
    role: machine-readable-A2-A3-verdict
  - document: docs/audits/T6_CONSTRUCTOR_INVENTORY_V1.md
    role: source-registry-delta-and-missing-enqueue-surface
  - document: docs/F1-reachable-state-exhaustion-package-review-2026-08-20.md
    role: previous-circular-closure-rejection
visibility: public
last_checked: '2026-08-23'
---

# T6-F1 可达持久状态闭世界的条件引理与当前最小断点

## 1. 要判定的命题

固定核心素数 \(p\equiv1\pmod {24}\)。令 \(C\) 是从活动源码独立得到的 persistent
constructor/serializer 集，\(Q\) 是唯一入队边界，\(V_1,\ldots,V_{14}\) 是活动
persistent-family predicates。A2--A3 所需的结论不是“registry 中有 14 个 owner 名称”，而是

\[
\begin{aligned}
\forall c\in C\ \forall s\in D_c,
\quad &\operatorname{terminal}_c(s)\\
&\mathbin{\dot\lor}\operatorname{reject}_c(s)\\
&\mathbin{\dot\lor}\bigvee_b
  \left[T=c_b(s)\land Q(T)=\operatorname{ACCEPT}\right],
\end{aligned}
\tag{1}
\]

其中第三类的每个 \(T\) 都必须由同一个 extractor 读取，且

\[
A(T)=\{i:V_i(T)=1\}\ne\varnothing.
\tag{2}
\]

固定 precedence 只能在 (2) 已成立后决定 owner。它不能证明 (2)，也不能证明 \(C\) 已穷尽。

## 2. 已经证明的部分

### 2.1 非循环 header 与条件 owner 唯一性

`extract_verified_selector_header_v1` 在 family 判定之前只核验 schema、直接 chart facts、
mark/source/terminal-first receipts、producer queue rights 和内容摘要。它明确拒绝输入中的
`owner`、`family_id`、`normal_form` 与 normalizer cache。因此 extractor 成功不蕴含
family 命中，旧 F1 包的定义循环已被消除。

若 (2) 非空，且所有命中 pair 都在显式 overlap allowlist 中，则有限全序存在唯一最小元：

\[
\operatorname{owner}(T)=\min_{\prec} A(T).
\tag{3}
\]

若 (2) 为空或有非法 overlap，classifier 分别返回 `FAMILY_NO_MATCH` 或
`FAMILY_ILLEGAL_OVERLAP`，不产生 owner。故 A3 的**条件决定性**已证，但 family totality 未由
(3) 得到。

### 2.2 新 gate 内的失败闭合与单步安全

对任何实际送入 `reject_before_persistent_queue_v1` 的对象，未知 schema/gate/producer/branch、
receipt 摘要失配、terminal output、零 family 命中、非法 overlap、未声明 target owner 都返回稳定
reason code。若它返回 `ACCEPT`，则 target 有唯一 owner、owner digest 可重放，且 owner 属于
producer 声明的 target set。

这是**接口内 safety**，不是“所有历史 constructor 已调用该接口”的证明。

### 2.3 initializer 的算术 guard partition

对核心素数 \(p=24t+1\)，令

\[
X=\frac{p+3}{4}=6t+1.
\tag{4}
\]

若 \(X\) 有素因子 \(\ell\equiv2\pmod3\)，最小这样的 \(\ell\) 给出 gap-3 Type II root
terminal；否则 \(X\) 的全部素因子均为 \(1\pmod3\)，得到 ordinary \(q=1\) G endpoint，
继而进入

\[
R_X=16t+3,
\qquad
K_X=(6t+1)(16t+1),
\qquad
A_X=1.
\tag{5}
\]

两支由“集合是否为空”互斥且穷尽。又有

\[
4K_X=pR_X+1,
\qquad
3\le R_X<p,
\qquad
A_X\mid K_X.
\tag{6}
\]

若 (5) 被投影为 `TYPEI/FULL_CARRIER_POST_G/full_carrier_scope=true`，它只命中
`type_i_full_carrier_post_g`。因此 initializer 的算术 partition 与 target family membership
可符号证明。活动 `initial_dispatch` 尚未生成 `PersistentSelectorStateV1` receipt，也未调用新
gate，所以 A3 的真实基础步 B 仍缺 serializer bridge。

### 2.4 条件迹归纳核

设：

- B：initializer 的唯一非终止输出经 \(Q\) 接纳；
- S：每个接纳 parent 的每个实际入队 successor 都来自登记 producer，且再经 \(Q\) 接纳；
- X：所有 persistent queue mutation 都经过 \(Q\)。

对最短迹长度归纳立即得到：每个实际可达 persistent state 都有唯一 owner。这一结构归纳是
正确的；当前缺的是 B、S、X 的活动源码证明，而不是归纳法本身。

## 3. A2 逐 constructor 裁定

活动 inventory 含一个 initializer 与 15 个 registered edge 名称，但没有任何 observed enqueue
call。逐项裁定如下；“局部”表示书面 guard 内的算术 target/E1--E5 可以重放，不表示其全部输入
已形成 terminal/reject/nonterminal partition。

| constructor 组 | 已建立 | A2 未建立的最小项 |
|---|---|---|
| `initial_q_one_root_dispatch_v1` | (4)--(6) 的 terminal/G 二分与 full-carrier owner | v1 target serializer、producer rule、真实 root enqueue gate |
| Type-II proper endpoint、gcd-shadow | guard 内的较小 endpoint 与 F/G 算术分类 | 对全部 source guards 的 partition、共同 header、actual admission |
| q=1 G handoff | p-only target (5) 与局部 E1--E5 | source receipt 到 v1 schema 的 serializer/gate |
| positive-q G、c=3 lineage | 条件 target 公式 | 活动 controls 缺 actual source/terminal-first receipt；positive-q 明确 `recursive_edge_eligible=false` |
| second-anchor、q=1 d=1 relay | 具名 family 中的局部宏公式 | verifier 是 family/fixture receipt builder，无共同 serializer/gate |
| same-chart、joined reset、A=1 reset、fixed-n | 局部 strict rank identities | fixture-atlas minimal descriptors 不等于统一 E3 target；未实现 terminal/reject partition |
| high-support sink | improvement 非空时的局部选择定理 | 活动实现是聚焦 \(p=73\) control；没有可复用 target serializer |
| C=2 three-anchor | \(P\to H_3\) 的符号容量下降 | `macro_data` 只输出整数摘要；\(H_3\) 只到 nonrecursive pending-dispatch |
| H4 atomic | 书面 actual-parent guard 下的 terminal/candidate 定理 | controls 均 terminal-preempted；无 nonterminal pending target serializer |
| c=8 atomic | double-low 假设下的条件宏定理 | control 未命中 double-low；`suffix_capacity_data` 只输出容量，无 target state |

此外，源码 census 发现六个没有唯一 registry 映射的 non-false eligible producer signals，以及
一个由 fixture 人工传入 `persistent_queue=true` 的 total-cofactor relative adapter。故 A2 连量词域
\(C\) 都尚未冻结；从 15 个 registry 名称反推 constructor 穷尽会再次循环。

## 4. 三个精确断点

### 4.1 最小 producer-set 反例：positive-q registry/control 不一致

`positive_q_g_full_carrier_phase_root` 在 registry 中被计作 registered edge；但活动
`phase_root_entry` control 明确记录 actual source receipt 与 terminal-first receipt 均未供应，
并返回 `recursive_edge_eligible=false`。所以：

- 若 registry 名称就是 \(C\)，则缺 executable serializer；
- 若 executable non-false producer signals 才是 \(C\)，该 registry row 不是活动 producer。

两种解释都不能给出同一个 source-derived closed world。

### 4.2 最小 E3/provenance 断点：\(p=409\) fixed-n control

活动 `verified_fixed_n_edge` 输出

\[
(p,R,K,A)=(409,11,1125,125),
\qquad 4K=pR+1,
\tag{7}
\]

并标记 `recursive_edge_eligible=true`、E1--E5 全真。但该对象没有 parent registration、sealed
terminal-first miss、producer ID 或 enqueue provenance；其 surrounding receipt 还保留 overflow
phase/state label，而 \(R=11<p\)。因此：

- 保留 overflow label 会违反 v1 的 `overflow => R>p`；
- 修正为非 overflow 后仍需一个未给出的 provenance/family projection；
- 无论哪种处理，都不能凭该 control 自报递归资格。

这是 source-level producer-shaped witness，不是“ESC 的数值反例”。它证明当前 E3 output surface
尚未统一。

### 4.3 最小符号重入断点：C=2 的 \(H_3\)

对 \(p\equiv769\pmod {912}\) 的书面 C=2 macro，已有

\[
P\Longrightarrow H_0\Longrightarrow H_1\Longrightarrow H_2
\Longrightarrow H_3,
\qquad
\Lambda_p^\sharp(H_3)=(0,c_3)<(0,p-1)=\Lambda_p^\sharp(P).
\tag{8}
\]

但活动 `macro_data` 只返回 `prime`、三层 capacity 与 `R_3`，不返回 parent/target state、mark、
scope、terminal-first receipt 或 source receipt。书面 claim 只把 \(H_3\) 放入
`pending-dispatch domain`，而活动 taxonomy 明确把 `pending_dispatch normalization` 列为
nonrecursive surface。没有 serializer 将 (8) 投影成
`provenance_kind=C2_19_MACRO` 的 `ADMITTED_SUCCESSOR`。因此实际 successor induction 在
\(P\to H_3\) 处没有可用重入步。

## 5. A3 最终裁定

| A3 子命题 | 裁定 | 精确范围 |
|---|---|---|
| 独立 header 不预设 owner | `ESTABLISHED` | 新 v1 extractor |
| 非空合法命中集的 owner 唯一 | `ESTABLISHED` | 条件引理 (3) |
| 新 gate 内零命中/非法 overlap/未知 producer 失败闭合 | `ESTABLISHED` | 仅对实际调用该 API 的输入 |
| 每个已接纳 target 有唯一 owner | `ESTABLISHED_CONTRACT_LEVEL` | admission safety，不是 constructor totality |
| 每个实际 constructor target 至少命中 family | `OPEN` | A2 projection/partition 未完成 |
| 所有真实 enqueue 均经过新 gate | `OPEN` | 当前没有统一 queue 或 mutation site |
| 所有 nonterminal target 实际重入同一域 | `OPEN` | C=2/H4/c=8/overflow 等 serializer 缺失 |
| initializer 基础步 B | `OPEN_INTEGRATION` | 算术 owner 已证，v1 serializer/gate 未接入 |
| successor 步 S | `OPEN` | inventory unknown 为 9 |
| 无旁路假设 X | `OPEN` | authoritative runtime surface 尚未定义 |
| B、S、X 下的迹归纳 | `ESTABLISHED_CONDITIONAL` | 纯结构归纳，不由有限 trace 测试替代 |

所以当前不能证明

\[
\forall S\in\operatorname{Reach}(p),\quad
S\text{ 非终止}\Longrightarrow\exists!\operatorname{owner}(S).
\tag{9}
\]

准确状态是：

```text
A2_CONSTRUCTOR_GUARD_PARTITION = OPEN_MINIMAL_GAPS
A3_FAMILY_DECISION_LEMMA = ESTABLISHED_CONDITIONAL
A3_ACTUAL_FAMILY_TOTALITY = OPEN
A3_ACTUAL_REENTRY_INDUCTION = OPEN
T6_F1_REACHABLE_STATE_EXHAUSTION = OPEN
```

这不反驳抽象 F1 命题，更不反驳 Erdős--Straus 猜想；它反驳的是“当前 registry、controls 与
局部 receipts 已经足以证明 closed world”这一仓库状态断言。

## 6. 下一条最小定理

下一步应证明 **Producer Projection and Exclusive Admission Theorem v1**：

1. 先处置全部 source signals：每项要么降级为明确 nonrecursive control，要么登记唯一
   producer rule；
2. 对每个登记 producer 的每个 source guard，给出 terminal/reject/nonterminal 的符号 partition；
3. 为每个 nonterminal branch 写 serializer \(\sigma_c\)，生成同一 v1 header 和 sealed receipts；
4. 符号证明 `classify_selector_owner_v1(extract(\sigma_c(T)))` 成功且 target owner 在 producer
   声明集中；
5. 让 initializer 与所有 successor queue writes 只调用新 gate，并证明没有旁路。

只有这五项逐 constructor 完成，B、S、X 才能代入第 2.4 节的归纳核，从而关闭 F1。
