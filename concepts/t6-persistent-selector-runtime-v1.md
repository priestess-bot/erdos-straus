---
kind: concept
concept_id: t6-persistent-selector-runtime-v1
title: T6 producer projection、独立验证、唯一准入与持久队列 runtime v1
summary: 在非循环 PersistentSelectorStateV1 之上固定唯一执行链：已接纳 source 重放、source terminal-first、registered producer、无 authority candidate、coordinator-owned projector、独立 E1--E4 validator、target terminal-first、N7 T5 ticket、共同 state admission 与唯一 enqueue。该 runtime 是 protocol freeze，不证明任何 producer 的 guard totality，也不把接口存在误报为 F1/F2/F3 闭合。
topics:
  - proof-program
  - selector
  - runtime
  - producer
  - admission
  - persistent-state
  - t5
  - t6
used_by: []
sources:
  - concept: t6-persistent-selector-state-v1
    role: noncircular header, family predicates, owner and admission gate
  - concept: t5-global-well-foundedness-contract-v2
    role: frozen N7 potential and ticket semantics
  - document: docs/T6_F2_F3_HIGH_CONCURRENCY_EXECUTION_PLAN.md
    role: F2/F3 wave runtime protocol and freeze requirements
  - data: data/t6-f2-f3-wave1-workpack.json
    role: audited integration baseline and track ownership
visibility: public
last_checked: '2026-08-24'
---
# T6 producer projection、独立验证、唯一准入与持久队列 runtime v1

## 1. 作用域

`PersistentSelectorStateV1` 已经把合法 header 与 family/owner 结论分开，但基线仍缺一条
authoritative 执行链。`scripts/t6_persistent_selector_runtime_v1.py` 固定如下 protocol：

```text
admitted source
  -> source receipt / owner / N7 potential replay
  -> source terminal-first schedule
  -> registered producer branch
  -> authority-free CandidateTransitionV1
  -> coordinator-owned TargetProjectionV1
  -> independently registered E1--E4 validator
  -> target terminal-first schedule
  -> semantic N7 potential recomputation and ticket validation
  -> PersistentSelectorStateV1 extractor/classifier/admission
  -> sole enqueue mutation
```

这是一份 **Freeze A protocol**，不是 constructor exhaustion theorem。只有实际注册并实现上述
全部接口的 branch 才可执行；未注册、缺 projector、缺 terminal schedule、缺独立 validator 或
ticket 不下降都会 fail closed。

## 2. Candidate 不拥有递归权

producer 只能返回三种类型：

1. `GuardMissV1`；
2. `TerminalDraftV1`，随后必须由登记的独立 terminal verifier 重放；
3. `CandidateTransitionV1`，只含 producer/branch、算术 witness 与 ticket **请求**。

candidate 任意深度出现以下字段都会被拒绝：

```text
owner / family / normal_form / normalized_state
recursive_edge_eligible / persistent_queue / selector_status
```

target facts 只能由 coordinator-owned projector 从 source 与 witness 重算。owner、matched families、
owner digest 与 state ID 则继续由 noncircular state contract 独立计算。

## 3. E1--E5 不由 runtime 伪造

branch registration 中的 claim references 只声明依赖，不能自动使 E1--E4 为真。每个 branch 必须
登记一个独立 transition validator，返回绑定 source ID、producer、branch 与 projection digest 的
`TransitionValidationV1`。只有 `E1=E2=E3_pre_admission=E4=true` 且证据 ID 非空，runtime 才继续。

E3 的最后一步仍由共同 state admission 实际执行；validator 只能证明 projector 的 pre-admission
schema/normal-form 条件，不能预填 owner。E5 由 runtime 从语义字段重算 source/target 势并验证：

\[
\Pi(S),\Pi(T)\in\mathbb N^7,
\qquad
\Pi(T)<_{\rm lex}\Pi(S).
\]

`OUTER_RANK_DROP`、`PHASE_DROP`、`LOCAL_DROP` 必须与首个严格下降坐标相符。candidate 提供的
ticket 字符串只是请求；相等、上升或 ticket 类型不匹配均被拒绝。

## 4. Terminal-first 的两个边界

source schedule 在 producer 执行前运行，命中后直接返回 verified terminal。candidate project 后还要
运行 target schedule；命中同样优先于持久准入。两种 terminal 都要求登记 verifier 与 lift evidence，
且不会写入 queue。

因此 producer 不能以“更早已 miss”替代目标重算，也不能在已存在 direct terminal 时同时登记 edge。

## 5. 唯一 queue mutation

runtime 内唯一增加 persistent state 的方法是私有 `_enqueue_admitted_target_v1`。它只接受已经：

- 通过共同 state admission；
- 获得 recomputed owner/digest；
- 获得可重放 N7 potential receipt；
- 对 successor 获得独立 transition receipt 与 strict ticket receipt

的 `RuntimeQueueItemV1`。重复 state ID 被拒绝。调用方拿不到以布尔值直接写 queue 的接口。

## 6. 当前证明边界

本协议闭合 Freeze A 的接口定义和接口内 safety，但尚未证明：

- 基线 18 个 source signal 已全部获得正确 disposition；
- 每个登记 producer 有互斥穷尽 guard partition；
- 每个数学 branch 有通过的独立 E1--E4 validator；
- 七轨所有 target shapes 都已进入 Freeze B grammar；
- initializer 到全部后继的实际 trace 已连续迁移到此 runtime。

所以当前仍是：

```text
RUNTIME_PROTOCOL_V1 = FROZEN_CANDIDATE
F1 = OPEN_MINIMAL_GAPS
F2 = OPEN
F3 = OPEN_MINIMAL_GAPS
T6 = OPEN
```

聚焦验证：

```bash
python3 -m unittest tests.test_t6_persistent_selector_runtime_v1 -v
```
