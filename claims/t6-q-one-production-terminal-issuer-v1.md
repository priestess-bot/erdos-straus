---
kind: claim
claim_id: t6-q-one-production-terminal-issuer-v1
title: q=1 root terminal 与注册前缀 MISS 的 production issuer/replay V1
statement: >-
  在 exact HEAD 的 coordinator registry v3 恰好授权 ROOT_INITIALIZER、TERMINAL_ISSUER、
  TERMINAL_SCHEDULER 与 INDEPENDENT_COVERAGE_VERIFIER 四个分离角色，且仍拒绝 E1、queue、
  producer、T5 和 branch authority 时，production issuer 只从 repository locator、full HEAD 与
  raw ordinary q=1 G integers fresh 重建 root envelope 与 exact-HEAD assembler decision，并以后置
  QOneRootSourceActualnessReceiptV1 证明 parentless root occurrence。若 decision 为 HIT，则签发可关闭
  根目标的 ProductionQOneRootTerminalReceiptV1；若为 MISS，则只签发 gaps 3/7/11 的
  ProductionQOneRegisteredPrefixMissReceiptV1，固定 global_exhaustion=false 与 next gap 15。两种
  receipt 均无 persistent admission、common owner、E1、queue 或 producer continuation authority。
  独立 post-issuance verifier 不导入 issuer、scheduler 或 coverage module，而从同一 HEAD/raw input
  重建 source、assembler decision、actualness 和 expected receipt wire，逐字拒绝交换及一致重封换链。
  本结果闭合 q1 root registered-prefix issuance/replay 子门，不闭合完整 Gate 4、E1 或 T6。
claim_status: established
proof_provenance: repository_derivation
review_status: independent_review
topics:
  - T6
  - q-one
  - production-terminal
  - root-initializer-actualness
  - registered-priority-prefix
  - exact-head
  - independent-replay
  - proof-boundary
sources:
  - reproduction: scripts/t6_q_one_terminal_issuer_v1.py
    role: exact-HEAD initializer actualness attestation and production receipt issuance
  - reproduction: scripts/t6_q_one_terminal_receipt_verifier_v1.py
    role: issuer-independent source and production wire reconstruction
  - source: schemas/t6-q-one-production-terminal-receipts-v1.schema.json
    role: exact HIT/MISS receipt types and authority matrix
  - reproduction: tests/test_t6_q_one_terminal_issuer_v1.py
    role: real temporary-HEAD issue/replay controls and mutation suite
  - claim: t6-coordinator-q1-root-terminal-authority-v3
    role: separated exact-HEAD initializer, issuer, scheduler and verifier grants
  - source: docs/audits/T6_Q1_PRODUCTION_TERMINAL_FINAL_INDEPENDENT_REVIEW_2026-08-26.md
    role: independent issuer/replayer review and mutation-layer audit
visibility: public
last_checked: '2026-08-26'
---

# q=1 production terminal issuer/replay V1

## 1. 无环 authority DAG

production 层不修改 evidence-only root state 中的 false authority。完整依赖图为

```text
raw q1G + exact HEAD + registry v3
       |                    |
       v                    v
authorized root occurrence  exact-HEAD assembler evidence
       |                    |
       +---- actualness ----+
                 |
        production issuer
          /             \
 root terminal HIT   registered-prefix MISS
```

`QOneRootSourceActualnessReceiptV1` 和最终 production receipt 都在 body、anchor、state ID 之后构造；
任何 receipt ID 都不写回 source state，故不存在 terminal-result/state-ID 哈希环。

## 2. exact-HEAD role 与依赖隔离

registry v3 必须恰有四个不同 module/digest 的 role grants：

```text
ROOT_INITIALIZER
TERMINAL_ISSUER
TERMINAL_SCHEDULER
INDEPENDENT_COVERAGE_VERIFIER
```

issuer 自身不 top-level import T6 module。它从 requested-HEAD blobs fresh 执行 v2/v3 resolvers、root
envelope 与 assembler；不能直接执行 scheduler、coverage verifier 或 post-issuance verifier。assembler
内部继续承担 scheduler/coverage 的 v2-authorized exact-HEAD 执行。issuer 分别核对 V2 semantic method
得到的 scheduler/verifier pins 与 v3 artifact 的 `expected_v2_semantic_sha256`，并独立核对 v3 semantic
pins；它不要求两种 digest method 的结果相等，只要求 path、blob、symbol 和 schedule 相同。

post-issuance verifier 位于另一模块，不直接 import 或执行 issuer、scheduler、coverage verifier。
它 fresh 执行 v2/v3 resolvers、root envelope 和已 pin 的 assembler；assembler 再沿其已审计依赖
transitively fresh-exec scheduler/coverage。故这里得到的是 issuer-independent 的 production wire 与
source-authority replay，不是独立于 assembler/scheduler/coverage 的第三套数学证明。

执行中的 issuer/verifier 是各自 trusted current-process 入口；二者检查其 backing file 与 requested
HEAD 及 v3 artifact pin 一致，但不声称在自身内部无循环证明 pre-import integrity。

## 3. root actualness sidecar

root envelope 中 `initializer_authority=false` 保持不变。actualness 只能由已核验
`ROOT_INITIALIZER` grant 和独立 `TERMINAL_ISSUER` grant 联合后置 attest。sidecar 显式内嵌并重放：

1. raw q1G exact integers 与完整因子分解；
2. canonical marked root problem \(4/p\)；
3. deterministic initial-G branch mapping；
4. body、anchor、state IDs/digests；
5. initializer contract/domain replay；
6. HEAD、v3 registry/manifest、initializer/issuer grants 与 fresh module binding。

其 authority 固定为

```text
initializer_output_self_authorizing   = false
actualness_attestor_role              = TERMINAL_ISSUER
source_actualness                     = true
root_initializer_authority            = true
terminal_issuer_attestation_authority = true
persistent_admission                  = false
common_owner_authority                = false
e1_authority                          = false
queue_authority                       = false
```

`owner_domain_id` 只是 q1 G root occurrence 的域标签，不是 common classifier owner receipt。

## 4. 两种严格分离的 production receipt

共同字段绑定 V2/V3 registries、role manifests、四项 grants、source actualness、body/anchor/state、
assembler decision/evidence/coverage replay 与 schedule digest，并固定：

```text
source_actualness             = true
root_initializer_authority    = true
issuer_authority              = true
issued_under_terminal_issuer  = true
persistent_admission          = false
common_owner_authority        = false
e1_authority                  = false
queue_authority               = false
producer_continuation_allowed = false
```

### Root terminal HIT

`ProductionQOneRootTerminalReceiptV1` 保存 Type I/II certificate、恢复分母与根方程

\[
4xyz=p(xy+xz+yz),
\]

并固定

```text
outcome                           = ROOT_TERMINAL_HIT
root_outcome_kind                  = ROOT_CERTIFICATE_LEFT_INJECTION
terminal_leaf_authority            = true
registered_prefix_miss_authority   = false
root_proof_close_authority          = true
global_exhaustion                   = false
```

找到一张根证书足以关闭该 root occurrence，但不声称穷尽所有 terminal family。

### Registered-prefix MISS

`ProductionQOneRegisteredPrefixMissReceiptV1` 固定

```text
outcome                           = MISS_REGISTERED_PRIORITY_COMPLETE
coverage_semantics                 = REGISTERED_PRIORITY_ONLY
ordered_gaps                       = [3, 7, 11]
next_unchecked_gap                 = 15
global_exhaustion                  = false
terminal_leaf_authority            = false
registered_prefix_miss_authority   = true
root_proof_close_authority          = false
selected_certificate               = null
```

它不得命名为 `MISS_COMPLETE`，也不能直接进入旧 E1、producer 或 queue。

## 5. local serializer 与 authority verifier 的分界

issuer 的 local serializer 验证 exact class、authority matrix、branch-local certificate/root equation、
nested/top internal relations 和 content seal。它不从 repository/raw input 重新取得 body/anchor/state
preimages，也不重新认证所有 registry/evidence digest preimages。

因此一个重要的预期边界是：攻击者可以把合法 p=73 actualness 中的 body/anchor/state ID/digest
一致替换为另一条 p=1201 root-envelope 链，同步修改 deterministic branch mapping 并重封 nested/top
receipt；local serializer 会接受这个局部自洽对象。这不是 production authority 验证。

独立 verifier 必须以 p=73 raw input 从 exact HEAD 重建 p=73 body/anchor/state 和完整 expected receipt，
并拒绝上述 coherent reseal。production consumer 只能信任该 authority replay 结果，不能仅凭 local
serializer 或 receipt seal 授权。

## 6. 控制与剩余边界

正控制：

- \(p=73\)：Type II gap 7、\(d=1\) root terminal；
- \(p=193\)：Type I gap 7、\(d=10\) root terminal；
- \(p=241441\)：gap 11 root terminal；
- \(p=1201,2521\)：registered-prefix MISS。

简单的 HIT/MISS type、prefix-to-global、E1 authority、state、grant 与 HEAD 未重封变异分别在
JSON Schema 或 outer content-seal 层 fail closed；测试断言精确拒绝层，不把它们表述为已经到达
深层语义比较。type-specific ID prefixes 由 schema 结构测试固定，canonical/alternate import alias
则生成逐字相同的 production receipt。

当前唯一刻意穿过 local serializer 的深层负控制，是把 `p=73` receipt 的完整
body/anchor/state 引用一致换成 `p=1201` 链并重新封口。测试显式断言 local serializer 已接受，
随后 independent exact-HEAD replay 以 `SOURCE_MISMATCH` 或 `WIRE_MISMATCH` 拒绝。本文不声称尚未
实现的 registry/decision/evidence coherent-reseal 变异已被逐项单独测试；它们仍由最终 expected-
wire 全等比较覆盖其合同逻辑，后续 consumer 接入时应扩充为各自的显式负控制。

本结果只闭合 exact q1 root registered-prefix 的 production issuance/replay 子门。完整 Gate 4 仍为
OPEN：其它 owner domains 和 target schedules 尚未覆盖。还缺 common owner/classifier receipt、
prefix-aware E1V2 consumer、producer/branch grant、E2--E5、target re-entry 与唯一 queue mutation。
