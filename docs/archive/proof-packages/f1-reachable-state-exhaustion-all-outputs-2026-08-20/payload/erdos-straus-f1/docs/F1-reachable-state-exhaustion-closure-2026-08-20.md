# T6 F1 — Reachable-state exhaustion 完整闭包证明

Baseline: `d3b3b6a`  
Date: `2026-08-20`

结论：

```text
T6-F1-REACHABLE-STATE-EXHAUSTION = CLOSED_CONTRACT_LEVEL
```

精确含义：对任意核心输入 `p`，每一个能够合法进入 T6 selector 持久递归队列的状态，都由冻结的 16-family first-match 分类器唯一分类；不存在合法入队但未分类的递归状态。F1 不证明任何 family 都有出口；F2/F3、F4、F5、T6 totality 和 Erdős–Straus 猜想仍开放。

## 1. 状态与 Reach

设冻结 family 注册表为

\[
\mathcal F=(F_1,\ldots,F_{16}),
\]

冻结递归 edge producer 集为

\[
\mathcal E=\{e_1,\ldots,e_{15}\}.
\]

一个对象 `S` 是 legal persistent selector state，当且仅当：

1. `artifact_class=persistent_state`；
2. `consumer=t6_selector`；
3. terminal-first 已执行且未终止；
4. E1--E5 admission 完整；
5. E3 target normal form 已验证；
6. `normalize_selector_family_v1` 从 verified header 重新计算唯一 owner；
7. 该 owner 被绑定在 `selector_family_owner_digest` 中。

以下对象不是 persistent recursive state：terminal certificate、raw checkpoint、analysis evidence、candidate transition、pending dispatch、standalone stutter、formal cursor、未提升 dyadic candidate 和 unadmitted constructor output。

对固定 `p`，定义 `Reach_p` 为合法 persistent enqueue trace 的终点集合。唯一写队列的门是：

- M0 root serializer 的非终端输出；
- 冻结的 15 个 admitted verified-edge target。

于是 `Reach_p` 是以上两个生成规则的最小闭包，不是 family taxonomy 的并集。

## 2. F1-L1：producer 穷尽

M3 constructor admission firewall 是 fail-closed 的。任何新增 constructor 在完成 family 注册、normal form、scope/owner、E3 receipt、terminal priority、T5 ticket 和 frontier owner 之前，不得写入 persistent queue。

因此当前版本所有合法 enqueue event 的 producer 集严格为：

\[
\{\text{root serializer}\}\sqcup\mathcal E.
\]

不存在第三种合法 producer。

## 3. F1-L2：非持久 artifact 隔离

非持久 artifact 不同时具备 `persistent_state`、`t6_selector` consumer 和可重放 E3 receipt，故不能通过任何 enqueue gate。由于 `Reach_p` 是这些 gate 的最小闭包，它们不属于 `Reach_p`。

## 4. F1-L3：verified header extraction

对每张 admitted constructor receipt，E3 已给出 target normal form。定义 `extract_verified_selector_header_v1`，只从：

- verified target normal form；
- actual constructor branch；
- terminal-first verifier；
- mark witness；
- proper-root/overflow witness；

提取有限 typed header。cached `selector_family_id` 和 taxonomy membership 都不是输入。

因此依赖顺序是：

\[
\text{target normal form}\to\text{verified header}\to\text{family owner},
\]

而不是反向使用 family 表证明 target 类型。

## 5. F1-L4：normalizer 总性

`normalize_selector_family_v1` 按固定 first-match precedence 运行。其 owner 单元为：

1. `direct_terminal_leaf`；
2. `initial_core_root`；
3. `generic_nontrivial_marked_state`；
4. `type_ii_relation_f_endpoint`；
5. `type_ii_relation_g_endpoint`；
6. `t2_v1_atomic_pending_target`；
7. `h4_non_v1_branch_or_descendant`；
8. `c8_terminal_first_surviving_parent`；
9. `type_i_c2_19_macro_target`；
10. `proper_root_stutter_k_one`；
11. `proper_root_stutter_k_gt_one`；
12. `type_i_a_one_overflow`；
13. `type_i_high_support_sink`；
14. `type_i_low_support_persistent_overflow`；
15. `type_i_a_gt_one_overflow_residual`；
16. `type_i_full_carrier_post_g`。

Type II 在 terminal miss 后由 fiber `nonempty/empty` 二分；proper-root 由 `k=1/k>1` 二分；overflow 由 `A=1` 与 `A>1` 再按 high/low/residual 分流；最后的 ordinary post-G Type-I residual 只接受合法 Type-I normal form、合法 provenance/scope/owner/E3，不是无条件 `true`。

因此 every legal verified header 至少命中一个 owner。

## 6. F1-L5：normalizer 唯一性

设

\[
A_S=\{i:V_i(S)=\mathrm{true}\}.
\]

normalizer 返回唯一最小下标

\[
j(S)=\min A_S.
\]

所以即使底层算术谓词重叠，owner 仍唯一。唯一性来自有序 first-match，而不是声称所有算术 guard 两两互斥。

## 7. F1-L6：target re-entry

对 initializer 与 15 个 edge producer，queue admission 要求：

1. producer id 已注册；
2. terminal-first 已执行；
3. target 通过 legal-state contract；
4. verified-header extractor 成功；
5. normalizer 返回的 family 在 producer 声明的 target family 集中；
6. owner digest 验证；
7. E1--E5/T5 ticket 验证。

否则 `reject_before_persistent_queue`。

故每个合法 nonterminal target 都重新进入同一分类域。

## 8. 主定理

对 `S in Reach_p`，按最短合法 enqueue trace 长度归纳。

基例：长度 0 时，`S` 是 M0 的非终端持久输出。M0 的 terminal outcome 不入队；其非终端 outcome 经 E3/normalizer 唯一分类。

归纳步：设长度 `n` 的所有可达状态均唯一分类。取长度 `n+1` 的终点 `T`。最后一步必来自某个 admitted producer。若 outcome terminal，则不会得到 Reach 子节点；故 `T` 是 nonterminal persistent target。由 producer 穷尽、verified-header extraction、normalizer 总性与唯一性、target re-entry，`T` 恰属于一个登记 family。

因此：

\[
\boxed{\forall p\;\forall S\in\operatorname{Reach}_p,\quad S\text{ nonterminal}\Rightarrow\exists!F\in\mathcal F\;[C(S)=F].}
\]

## 9. 非循环性

本证明顺序为：

\[
\text{state-output contract}
\to\text{T5 queue admission}
\to\text{constructor firewall}
\to\operatorname{Reach}_p
\to\text{verified header}
\to\text{family owner}.
\]

family registry 不参与 Reach 的生成定义；仅新增 family 不会使状态可达，仅写 arithmetic candidate 也不会使状态可达。只有新增 persistent constructor 才改变 Reach，而这会自动重开 F1。

## 10. 历史 O1 的拆分

旧 `GAP-O1-GLOBAL-EXHAUSTION` 包含两个合取项：

\[
\underbrace{\text{reachable-state classification}}_{\text{F1}}
\land
\underbrace{\text{classified-family exit totality}}_{\text{F2/F3}}.
\]

F1 只关闭第一个。第二个仍开放，所以历史 O1 的当前状态应记为：

```text
DECOMPOSED:
  reachable_state_classification = CLOSED_BY_F1
  classified_family_exit_totality = OPEN_UNDER_F2_F3
```

不能把整个 O1 简写成无条件 CLOSED。

## 11. F1 闭合后的边界

- F1：`CLOSED_CONTRACT_LEVEL`；
- F2：`OPEN`，处理 H4 其它分支、post-G Type I、A>1 overflow、high-support、atomic target、c=8；
- F3：`OPEN`，处理 proper-root k>1、QC1/TR1 physicalization 和 p^2 gate；
- F4：blocked by F2/F3；
- F5：blocked by F4；
- T6 total selector：`OPEN`。

## 12. 重开条件

任一下列变化发生时自动重开 F1：

- 新 persistent constructor；
- 已注册 constructor 新增未登记 target；
- 新 selector-consumable phase/provenance；
- pending/raw/analysis object 获得递归资格；
- 新 nontrivial mark target；
- normalizer precedence/residual coverage 改变；
- E3 不再重算 owner。
