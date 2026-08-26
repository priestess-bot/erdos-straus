# T6 q=1 root source-scoped E1 rebind 条件性复核

复核日期：2026-08-27
范围：V4 `ROOT_SOURCE_SCOPED_E1` occurrence 到 V5 admitted V1 base source 的 V6 pure rebind。
裁定：`ACCEPT_CONDITIONAL`（独立攻击复核接受条件性结论；不是 external peer review）。

## 裁定的精确内容

在同一个已审阅 exact HEAD 上，若 V4 的 q=1 root receipt 与 V5 的 V1
base-admission receipt 独立重放为同一 V2 root chain，则 V6 可以确定性地产生
`Q1_ROOT_SOURCE_SCOPED_E1_REBIND_RECEIPT_V1`。它将

```text
V2 RawRootSourceStateV2 ID/digest
  -> V5 V1 ROOT_INITIALIZER_OUTPUT ID/wire digest
```

重新锚定。V1 source owner、owner digest 和 source potential 均对 V5 V1 state
重新计算；它们不复制 V2/V4 owner、candidate 或 potential digest。输出的语义固定为

```text
representation_namespace = Q1_ROOT_SOURCE_SCOPED_E1_REBIND_V1
path_semantics           = DERIVED_WITNESS_NOT_V1_STATE_PATH
not_transition           = true
```

因此它是一个 derived witness sidecar，不是 V1 state path、structured E1 leaf 或
successor transition。

## 已复核控制

`p=1201,2521` 的 V3 registered-prefix MISS、V4 occurrence 和 V5 V1 base source
通过 rebind。`p=73,193,241441` 的 terminal HIT 均在 V4/V5/rebind 之前抢占，不能构成
可 rebind 输入。`p=1201` 的 gap-23 Type-I `d=34` 仍在 `[3,7,11]` 注册前缀以外，故
`global_exhaustion=false` 和 `next_unchecked_gap=15` 不变。

V6 focused suite 的 9 项测试均通过：

1. `test_positive_controls_rebind_to_new_v1_source_without_recursive_authority`
2. `test_v4_and_v5_source_swaps_fail_closed`
3. `test_namespaced_rebind_is_rejected_by_legacy_structured_e1_parser`
4. `test_v4_and_v5_role_grants_are_registry_pinned`
5. `test_candidate_injection_and_miss_complete_relabel_fail`
6. `test_authority_and_state_mutations_fail_after_reseal`
7. `test_serializer_replays_cross_receipt_ids_and_derived_maps`
8. `test_boolean_and_float_source_controls_fail`
9. `test_terminal_hits_preempt_before_any_rebind`

攻击面覆盖 cross-source/cross-receipt swap、role-grant mutation、candidate injection、
将 prefix MISS 重标为 `MISS_COMPLETE`、authority/state mutation 后 reseal、derived map
injection、布尔/浮点输入，以及 terminal-first preemption。旧
`E1OccurrenceReceiptV1` parser 对 V6 wire 的 field set 不匹配拒绝，是刻意保留的
negative control。

## 仅有的正向标记

```text
v4_root_source_scoped_e1       = true
root_source_scoped_e1_rebound  = true
source_rebind_authority         = true
```

除上述 namespaced rebind markers 外，generic/successor E1、producer、branch、admission、
persistent admission、queue/enqueue、E2--E5、T5 potential/ticket、re-entry、terminal leaf 和
global exhaustion 都是 false。尤其，V6 不把
`MISS_REGISTERED_PRIORITY_COMPLETE` 提升成旧结构化 E1 所需的 `MISS_COMPLETE`。

## 条件与未闭合边界

V6 是 pure module/schema/test bundle；当前没有 V6 exact-HEAD registry、controlled
orchestrator 或 independent replayer。模块内的 local grant 不是外部 Git trust anchor，也不
赋予 production authority。V5 的 selected-commit condition 因而完整保留：repository-selected
exact commit 必须另有 immutable 或 signed trust anchor；同时改写 pin 和实现的提交不继承本结论。

本裁定不建立 generic E1、successor E1、producer、target terminal scope、E2、target owner/E3、
E4、E5、shared target admission、queue mutation、re-entry、Gate 2、完整 Gate 4、Gate 5、F1、F2、
F3、T6 或 Erdős--Straus 猜想的闭合。

## 后续动作

下一步有两条合法路线：为固定 V6 policy 建立独立审阅的 exact-HEAD registry、controlled
orchestrator 和 independent replayer；或者转向独立的 target-terminal/E2 设计，同时将 V6 保持
为非授权的 source correspondence。两条路线都不得把此 rebind 当作 generic E1 或 production
successor。

## 证据

- `claims/t6-coordinator-q1-root-source-scoped-e1-rebind-v1.md`
- `scripts/t6_q_one_root_source_scoped_e1_rebind_v1.py`
- `schemas/t6-q-one-root-source-scoped-e1-rebind-v1.schema.json`
- `tests/test_t6_q_one_root_source_scoped_e1_rebind_v1.py`
- `claims/t6-coordinator-q1-root-prefix-scoped-e1-authority-v4.md`
- `claims/t6-coordinator-q1-root-v1-base-admission-authority-v5.md`
