---
kind: concept
concept_id: t6-persistent-selector-state-v1
title: T6 非循环持久状态、owner 判定与入队合同 v1
summary: 定义一个先于 normalizer 的最小内容寻址 header：它只核验 schema、直接算术坐标、terminal-first/source/mark receipt 和 producer queue rights，不把 owner、family 或 normal form 当作合法性前提；随后以独立 family predicates、显式合法重叠表和固定 precedence 计算 owner，所有零命中、非法重叠、未知 producer 或未声明 target 均在 persistent queue 前失败。该合同给出 initializer/successor 迹归纳核，但尚未证明活动源码的 constructor inventory 与逐分支 projection 全覆盖，故不关闭 F1。
topics:
  - proof-program
  - selector
  - state-transition
  - persistent-state
  - admission
  - normalization
  - reachable-state
  - T6
used_by: []
sources:
  - concept: denominator-escape-state-contract
    role: E1--E5 and constructor-firewall boundary
  - concept: t5-global-well-foundedness-contract-v2
    role: persistent-successor tickets and phase vocabulary
  - data: t6-proof-frontier-v2.json
    role: current family and registered-edge vocabulary
  - data: t6-selector-obligation-ledger-v1.json
    role: written family guards and F1 boundary
  - document: docs/F1-reachable-state-exhaustion-package-review-2026-08-20.md
    role: circular-definition counterexample and missing-interface diagnosis
visibility: public
last_checked: '2026-08-23'
---
# T6 非循环持久状态、owner 判定与入队合同 v1

## 1. 目标与结论边界

本合同修复旧 F1 包中的逻辑循环。旧定义先要求 normalizer 已返回 owner，再证明每个“合法状态”
都有 owner。这里把三层对象严格分开：

\[
\text{可验证 header}
\quad\longrightarrow\quad
\text{family 判定}
\quad\longrightarrow\quad
\text{persistent queue admission}.
\tag{1}
\]

第一箭头允许失败。也就是说，`extract_verified_selector_header_v1` 可以成功，而
`classify_selector_owner_v1` 随后返回 `FAMILY_NO_MATCH`。因此未分类的 constructor target
仍在合同论域中可见，不会因定义而消失。

活动实现位于：

- `scripts/t6_persistent_selector_state_v1.py`；
- `tests/test_t6_persistent_selector_state_v1.py`。

本合同建立的是 **A1/A3 所需的非循环接口与条件性归纳核**，不是活动源码 constructor
穷尽定理。特别地，它不证明：

```text
T6-F1-REACHABLE-STATE-EXHAUSTION = ESTABLISHED
```

F1 仍须等待 A0 的源码 inventory 与 A2 对每个真实 serializer 的 guard partition/投影证明。
F2、F3、F4、F5、T6 与 Erdős--Straus 猜想也均不由本合同升级。

## 2. 不循环的状态投影

### 2.1 `PersistentSelectorStateV1`

原始对象必须逐项包含：

| 层 | 字段 | 直接检查 |
|---|---|---|
| schema | `schema_id`, `schema_version` | 固定为 `persistent_selector_state_v1`, `1` |
| queue identity | `artifact_class`, `consumer`, `queue_gate` | `persistent_state`, `t6_selector`，以及两个冻结 gate 之一 |
| source identity | `producer_id`, `branch_id`, `parent_state_id` | 必须匹配调用方传入的 source-derived `ProducerRuleV1` |
| equation | `root_context`, `equation_rank` | 正整数、`p = 1 mod 24`、`1 <= rho <= p`，且与 receipts 一致 |
| mark | `mark` | versioned、内容寻址；`ROOT_SOL` 或严格较小的 `NONTRIVIAL_MARK` |
| priority | `terminal_first` | versioned、内容寻址且 outcome 必须为 `MISS` |
| provenance | `source_receipt` | initializer 或 admitted-successor schema，字段和摘要逐字重放 |
| selector facts | `facts` | 下节列出的有限 typed projection |
| content address | `state_id` | 从以上全部输入重算；不含 owner cache |

这里“verified”只表示 receipt 的 schema、坐标绑定和内容摘要可重放。receipt 中 E1--E5
断言的数学正确性仍由相应 constructor 定理承担；SHA-256 不会把断言变成证明。同样，
`p` 为素数的语义来源是 initializer/source receipt 所绑定的上游根域证明，本层只重查
`p = 1 mod 24` 与跨 receipt 一致性，不把有限或概率素性测试冒充全称证明。

### 2.2 classifier 的完整输入

`facts` 恰含以下字段；v1 对缺失字段和未知字段都失败：

```text
major_phase
endpoint_fiber
relation_q
provenance_kind
full_carrier_scope
atomic_arm
dispatch_status
proper_root_k
is_overflow
support_A
carrier_M
overflow_d
chart_R
chart_K
sink_scc_receipt
same_chart_promotion_receipt
```

它们是 serializer 可直接给出或从 receipt 重算的坐标，不是 owner 名称。Type-I header
只检查公共 chart schema

\[
4K=pR+1,
\qquad A\mid K,
\tag{2}
\]

以及所声明 provenance 所需的基本 typed 条件。例如 overflow 要求 `R>p`，proper-root
要提供正整数 `k`，atomic pending 要给出冻结 arm 与 `PENDING`。这些是 owner predicate
的输入，不是假设“某个完整 normal form 已被 normalizer 接纳”。

### 2.3 明确禁止的循环输入

以下 key 在 header 的任意深度出现都会得到 `CIRCULAR_CACHE_FIELD`：

```text
owner
owner_digest
selector_family_id
family_id
normal_form
normalized_state
normalizer_result
```

因此 owner digest 只能是 admission 输出，不能成为 extractor 成功的前提。若活动 serializer
内部保留更丰富的 normal-form 对象，它必须先投影出本合同的独立 header；不能把整块 cached
normalizer result 当作 header。

## 3. 两个 queue gate 与 receipt

v1 只授权：

1. `ROOT_INITIALIZER_OUTPUT`：根 serializer 的唯一非终止输出；没有 persistent parent，使用
   `t6_initializer_nonterminal_receipt_v1`。
2. `ADMITTED_SUCCESSOR`：已准入 constructor 的真实非终止 target；必须有先前 parent、
   `E1=...=E5=true` 与 `OUTER_RANK_DROP`、`PHASE_DROP`、`LOCAL_DROP` 三种 T5 ticket 之一，
   使用 `t6_admitted_successor_receipt_v1`。

`ProducerRuleV1` 不是从 family registry 自动生成的；它必须由 A0 从活动 constructor、serializer
与 enqueue call site 重建。每条 rule 固定：

```text
producer_id
queue_gate
branch_ids
source_owners
target_owners
```

未知 producer、错误 gate、未知 branch、source owner 不在声明域、或分类后的 target owner
不在声明域都会失败。这样 future constructor 不能只靠添加一个 family 字符串绕过 firewall。

`initial_core_root` 是 initializer 的输入义务，`direct_terminal_leaf` 是 terminal-first 的输出义务；
二者都不进入 persistent queue。因此 persistent owner 表包含 frontier 的其余 14 个 family，
而不是把 root input 或 terminal leaf 伪装成递归状态。

## 4. family predicates 与固定 precedence

### 4.1 顺序

活动 precedence 固定为：

1. `generic_nontrivial_marked_state`；
2. `type_ii_relation_f_endpoint`；
3. `type_ii_relation_g_endpoint`；
4. `t2_v1_atomic_pending_target`；
5. `h4_non_v1_branch_or_descendant`；
6. `c8_terminal_first_surviving_parent`；
7. `type_i_c2_19_macro_target`；
8. `proper_root_stutter_k_one`；
9. `proper_root_stutter_k_gt_one`；
10. `type_i_a_one_overflow`；
11. `type_i_high_support_sink`；
12. `type_i_low_support_persistent_overflow`；
13. `type_i_a_gt_one_overflow_residual`；
14. `type_i_full_carrier_post_g`。

前 9 项由 mark/phase/provenance、endpoint `F/G`、atomic arm 或 proper-root `k=1/k>1`
直接决定。overflow 层使用

\[
B_p=\frac{(p-1)^2}{4}
\tag{3}
\]

和 receipt facts 判定：`A=1`、`A>B_p` 且有 sink-SCC receipt、存在同图表 promotion receipt、
以及 `A>1` residual。最后的 full-carrier 同时要求
`provenance_kind=FULL_CARRIER_POST_G` 与 `full_carrier_scope=true`；它不是可以吞掉任意未知
Type-I header 的无条件 fallback。

### 4.2 合法重叠不是任意 first-match

谓词不被假定两两不交。当前只允许一类可解释重叠：

- 四个 overflow 层之间的 refinement/fallback 重叠。

特别地，H4、c=8、C=2、atomic pending、proper-root 与 overflow 不得只因仍携带某个历史
full-carrier scope 就命中 post-G owner；它们必须由自己的 source provenance 分类。这个限制避免
用最后一个宽泛 predicate 掩盖缺失的专用 receipt。

若命中集合为

\[
A(H)=\{i:V_i(H)=1\},
\tag{4}
\]

则 normalizer 依次执行：

1. `A(H)=empty` 时返回 `FAMILY_NO_MATCH`；
2. 若任意命中 pair 不在 `ALLOWED_FAMILY_OVERLAPS_V1`，返回
   `FAMILY_ILLEGAL_OVERLAP`；
3. 否则取固定 precedence 中的最小下标。

所以 precedence 只消歧**显式登记的** refinement，不会吞掉未来意外 overlap。owner digest
绑定 `state_id`、`facts_digest`、完整命中集、owner 与 precedence index。改变 precedence
会改变 owner 或 digest，负控已通过真实 classifier 证明这一点。

## 5. fail-closed reason contract

稳定 reason codes 按义务分组如下：

| 层 | codes |
|---|---|
| schema | `INPUT_NOT_MAPPING`, `UNKNOWN_SCHEMA`, `UNKNOWN_VERSION`, `UNKNOWN_TOP_LEVEL_FIELD`, `MISSING_TOP_LEVEL_FIELD`, `CIRCULAR_CACHE_FIELD` |
| queue | `INVALID_ARTIFACT_CLASS`, `INVALID_CONSUMER`, `UNKNOWN_QUEUE_GATE`, `UNKNOWN_PRODUCER`, `PRODUCER_GATE_MISMATCH`, `PRODUCER_BRANCH_MISMATCH` |
| receipt | `MALFORMED_MARK_RECEIPT`, `MALFORMED_TERMINAL_FIRST_RECEIPT`, `TERMINAL_OUTPUT_NOT_PERSISTENT`, `MALFORMED_SOURCE_RECEIPT`, `RECEIPT_DIGEST_MISMATCH`, `RECEIPT_STATE_MISMATCH` |
| typed facts | `MALFORMED_SELECTOR_FACTS`, `UNKNOWN_HEADER_VALUE`, `INVALID_CORE_CONTEXT`, `INVALID_CHART_FACTS`, `INVALID_ADMISSION_TICKET`, `STATE_ID_MISMATCH` |
| classifier | `FAMILY_NO_MATCH`, `FAMILY_ILLEGAL_OVERLAP`, `PRODUCER_TARGET_OWNER_NOT_DECLARED`, `OWNER_DIGEST_MISMATCH` |
| trace | `TRACE_ROOT_ORDER`, `DUPLICATE_STATE_ID`, `PARENT_NOT_REACHABLE`, `PRODUCER_SOURCE_OWNER_NOT_DECLARED` |

`reject_before_persistent_queue_v1` 是唯一返回 accept/reject decision 的 API。extractor 与 classifier
抛出的具体错误在这里被稳定序列化；调用方不能在某个失败后“仍然排队”。

## 6. 已证明的合同引理

### L1：extractor 非循环性

`extract_verified_selector_header_v1` 的控制流只调用 schema、receipt、内容摘要和直接 facts
验证函数；它不调用任何 `FamilyPredicateV1`、normalizer、owner digest 或 frontier family lookup。
测试构造了一个 extractor 成功但零 family 命中的 Type-I header。因此“header 合法”严格弱于
“可分类”，旧包的循环被实际打破。

### L2：条件 owner 决定性

给定 extractor 输出 `H`。若 (4) 非空，且每对命中 family 均属于显式合法重叠表，则固定有限
全序中存在唯一最小元。故 `classify_selector_owner_v1(H)` 返回唯一 owner。若任一前提失败，
函数不返回 owner 而给出稳定 rejection。这个引理证明的是决定性，不把 `A(H) != empty`
偷放进合法状态定义。

### L3：单步重入安全

设 source-derived producer rule 为 `P`，raw target 为 `T`。若
`reject_before_persistent_queue_v1(T,P)=ACCEPT`，则：

1. `T` 的独立 header 与三个 receipts 均已重放；
2. `T` 有唯一 owner 与可重算 owner digest；
3. 该 owner 属于 producer 明确声明的 target set；
4. terminal、未知 producer、未知 branch、零命中与非法重叠均没有 queue ticket。

这是 admission safety 定理，不是“每个 actual constructor target 都会 ACCEPT”的 totality 定理。

### L4：initializer/successor 迹归纳核

固定核心根 `p`。假设：

- **B**：initializer 的唯一非终止输出通过本 admission，并得到 owner；
- **S**：对每个已经 admission 的 parent，任一真实入队 successor 都来自 source-derived producer
  rule，且该 target 再次通过本 admission；
- **X**：A0 已证明不存在绕过这两个 gate 的真实 persistent enqueue call site。

令 `Reach_n(p)` 为不超过 `n` 个 successor steps 的所有 queue 状态。则对 `n` 归纳：

- `n=0`：由 B，initializer 输出有唯一 owner；
- `n -> n+1`：取最短迹为 `n+1` 的 `T`。其 parent 位于 `Reach_n(p)`，由归纳假设已分类；
  由 X 最后一步属于已登记 successor gate，再由 S，`T` 重新 admission 并有唯一 owner。

所以在 B、S、X 成立时，任意有限可达 persistent trace 的每个状态都有唯一 owner。函数
`verify_persistent_trace_v1` 重放一个给定的有限 topological trace，并检查唯一 base、parent
先出现、source owner/target owner 声明和每步 admission；其 receipt 明确标记
`finite_replay_instance_not_universal_constructor_proof`。有限测试不是 B、S、X 的全称证明。

## 7. 尚未闭合的桥梁

当前活动仓库此前没有统一的 header extractor、owner normalizer 或 queue API；已有 verifier
各自序列化局部状态。因此本文件定义了可接入接口，但不能仅凭自身证明所有历史 constructor
已经使用它。A1/A3 完整验收仍缺：

1. A0 从活动源码而非 frozen registry 重建所有 initializer/constructor/serializer/enqueue site；
2. 为每个真实非终止 branch 给出到本 `facts` projection 的符号推导；
3. 证明每个 branch 的 projection 至少命中一个 predicate，且所有重叠均在显式 allowlist；
4. 把 A0 inventory 编译为 `ProducerRuleV1`，证明 source/target owner sets 与实际 branch 相符；
5. 确认活动 queue 的所有写入都调用 `reject_before_persistent_queue_v1`，不存在旁路。

### 7.1 已发现的最小活动旁路候选

`reproductions/type_i_overflow_total_cofactor_typed_adapter.py` 的相对 adapter 接受调用方提供的
`persistent_queue=True`、非空 parent digest 与 terminal-first miss，然后可在固定控制上返回
`kind=relative_verified_edge`。对应 claim 明确把它限定为：已经外部登记 persistent source 后的
条件性 adapter；它没有证明每个 residual source 实际可达，也不是 frontier 中登记的独立
producer。

因此“adapter 自报 persistent”不能成为 queue right。focused control 先用活动 adapter 重放出
该 `relative_verified_edge`，再把 producer ID
`total_cofactor_typed_projection_v1` 送入本合同的真实 queue gate；由于 source-derived registry
没有该 producer，稳定结果为：

```text
UNKNOWN_PRODUCER
```

这给出一个具体 contract counterexample：若旧流程只相信 `persistent_queue=True`，conditional
control 可以自行升级；新流程要求外部 A0 inventory/registration 授权，因而在授权前失败闭合。
它同时说明第 5 项不是纯文档工作：活动 serializer/enqueue 仍需真正接入 gate，F1 才可能闭合。

只要任一项缺失，准确状态就是：

```text
PERSISTENT_SELECTOR_STATE_V1 = NONCIRCULAR_EXECUTABLE_CONTRACT
FAMILY_DECISION_LEMMA = ESTABLISHED_CONDITIONAL_ON_MATCH_AND_OVERLAP_POLICY
TRACE_INDUCTION_KERNEL = ESTABLISHED_CONDITIONAL_ON_B_S_X
T6_F1_REACHABLE_STATE_EXHAUSTION = OPEN
```

## 8. focused verification

```bash
PYTHONDONTWRITEBYTECODE=1 \
python3 -m unittest tests.test_t6_persistent_selector_state_v1 -v

ruff check \
  scripts/t6_persistent_selector_state_v1.py \
  tests/test_t6_persistent_selector_state_v1.py
```

测试覆盖 extractor 成功而 family 零命中、cached owner/normal-form 拒绝、receipt 篡改、terminal
隔离、unknown producer/gate、14 个 predicate 的直接 witness、合法/非法 overlap、precedence digest、
未声明 target、conditional total-cofactor 自报 persistent 的真实负控、initializer/successor trace
与 parent/source-owner 负控。它们验证实现遵守本合同，
不替代第 7 节的逐 constructor 符号证明。
