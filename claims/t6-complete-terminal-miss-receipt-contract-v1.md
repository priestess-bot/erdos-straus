---
kind: claim
claim_id: t6-complete-terminal-miss-receipt-contract-v1
title: T6 非授权终端 miss 回执类型边界 v1
statement: >-
  LocalTerminalMissReceiptV1 and CompleteTerminalMissReceiptV1 are disjoint,
  exactly shaped and canonically sealed types. A local miss binds one named
  family attempt to a source state or target projection and the fixed
  production registry, but carries no complete-schedule or queue authority.
  The future complete shape additionally requires an exact HEAD, PRODUCTION
  authority and registry class, schedule/domain/coverage digests, frozen family
  order and local receipt digests. The fixed production registry currently
  contains only LOCAL_ONLY schedules, zero COMPLETE schedules and no HEAD-role
  authority. Consequently every complete-miss claim, including a correctly
  shaped and sealed typed object, is rejected as SCHEDULE_NOT_COMPLETE after
  binding checks. This claim establishes no complete terminal replay or T6
  selector result.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
  - T6
  - terminal-first
  - proof-receipt
  - proof-boundary
sources:
  - reproduction: scripts/t6_complete_terminal_receipts_v1.py
    role: strict type, canonical seal, fixed-registry and fail-closed verifier
  - reproduction: tests/test_t6_complete_terminal_receipts_v1.py
    role: non-authority, binding, parser and cross-import controls
  - data: data/t6-wave1/t6-complete-terminal-schedule-registry-v1.json
    role: fixed production registry with zero complete schedules
  - source: schemas/t6-complete-terminal-miss-receipt-v1.schema.json
    role: exact local and future-complete receipt schemas
  - claim: t6-terminal-miss-scope-taxonomy-v2
    role: later shape-only distinction between registered-prefix and universe miss semantics
  - claim: t6-coordinator-head-bound-terminal-prefix-role-registry-v2
    role: later exact-HEAD scheduler/verifier capabilities with issuer explicitly absent
  - claim: t6-q-one-exact-head-terminal-decision-assembler-v2
    role: later source-bound execution evidence with every issuance authority still false
visibility: public
last_checked: '2026-08-26'
---

# T6 non-authorizing terminal miss receipt boundary v1

## 1. 已建立的内容

`LocalTerminalMissReceiptV1` 是一个严格的 `MISS_LOCAL` 记录。它只包含：

- source state 或 target projection 的 ID/digest；
- scheduler input digest；
- 固定 production registry digest 和 LOCAL_ONLY schedule ID；
- family、顺序位置、evaluator ID/digest；
- evaluator 输入/输出 digest 与 canonical receipt seal。

receipt 没有任意 payload、certificate、successor、admission 或 queue 字段；精确字段
解析和 JSON Schema 的 `additionalProperties: false` 会拒绝增加这些字段。

source schedule 的 subject 必须恰好是序列化 source state。target schedule 的
subject 必须恰好是 projection，同时 scheduler input digest 绑定 predecessor source
和 projection。两类 subject 不可互换。

## 2. 未来 complete 类型

`CompleteTerminalMissReceiptV1` 目前只是未来生产证明的严格数据形状。除了 subject
和 scheduler input，它还必须绑定：

1. `head_sha` 和 `authority_class=PRODUCTION`；
2. production `registry_id/class/digest`；
3. schedule、owner-domain membership replay；
4. 有序 family 和逐项 local miss digest；
5. coverage theorem、reproduction、verifier 与 replay digest。

这些字段能够描述未来 Gate 4 需要验证的证据，但字段齐全和自洽 seal 本身不产生
authority。

其中 domain membership 明确分开绑定 replay artifact 的 ID/digest 与本次 replay
输出 digest，不能用一次输出的自哈希替代固定 verifier artifact。receipt parser 还要求
对象的具体类型恰好等于 v1 dataclass；添加 `queue_gate`、E1 或其他字段的 dataclass
子类与带额外 JSON 字段的 mapping 同样被拒绝。

## 3. 当前不可签发定理

固定生产注册表满足：

```text
registry_class = PRODUCTION
status = NO_COMPLETE_SCHEDULE_AUTHORITY
head_authority_status = HEAD_ROLE_REGISTRY_REQUIRED
complete_schedules = []
complete_miss_issuance_enabled = false
```

现有 q1 gap-3/gap-7 与 source/target/checkpoint anchor 名称全部只是
`LOCAL_ONLY`。模块没有 TEST_ONLY registry、callable artifact manifest、complete
schedule replay 或 complete receipt issuance API，也不接受 caller 提供另一个 registry。

因此对任意输入 (C)，`verify_complete_terminal_miss_receipt_v1` 只可能：

1. 因类型、seal、HEAD、registry 或 subject 绑定错误而拒绝；或
2. 在这些检查全部通过后，以 `SCHEDULE_NOT_COMPLETE` 拒绝。

不存在返回 verified complete receipt 的路径。旧三字段 `TerminalMissV1`、local
receipt、自封装 TEST_ONLY/production mapping，以及直接构造的 typed complete object
都不能跨越这个边界。

## 4. 未建立的内容

本合同不证明任何 terminal family 完备，不签发生产 `MISS_COMPLETE`，不接入 E1，
也不授权 persistent queue。真正的 complete replay/issuance 仍需：

- HEAD-bound coordinator role registry；
- Gate 4 冻结的 production COMPLETE schedule；
- 独立的 domain、coverage 和 family replay；
- 对这些证据的 coordinator-owned runtime 集成。

所以本合同不关闭 F1、F2、F3、T6，也不证明 Erdos-Straus 猜想。

## 5. v2 scope clarification

后续 scope taxonomy 已把本卡中尚未签发的 `MISS_COMPLETE` 分成两个不同语义：有限注册
优先前缀的 `MISS_REGISTERED_PRIORITY_COMPLETE`，以及只可作为 shape 声明的全自然缺口
`TERMINAL_UNIVERSE_MISS_EVIDENCE_ONLY`。前者必须记录下一未检查 gap，不能声称全局穷尽；
后者若未来经完整语义重放，将报告根反例而不是允许 producer continuation。该 v2 类型层
同样没有 issuer 或 E1 权限。后续 coordinator registry v2 虽已固定并授权 gaps 3/7/11
scheduler 与 independent coverage verifier 的代码 capability，但其
`issuer_count=0`；因此仍不改变本卡“当前不可签发”的结论。
后续 exact-HEAD assembler 已把 evidence-only root state 与实际 scheduler/coverage replay
绑定为后置 decision，但同样固定 issuer/terminal/E1/queue authority 为 false，仍不是本卡
所缺的 production receipt。
