---
kind: claim
claim_id: t6-coordinator-q1-root-terminal-authority-v3
title: q=1 根终端 decision 的四角色 HEAD-bound authority registry v3
statement: >-
  Coordinator registry v3 grants exactly four distinct exact-HEAD roles on the
  ordinary parentless q=1 G root domain: ROOT_INITIALIZER, TERMINAL_ISSUER,
  TERMINAL_SCHEDULER and INDEPENDENT_COVERAGE_VERIFIER. Every executable is
  bound by tracked blob, stable symbol-set AST, local-import closure, dependency
  manifest, transitive dependency-semantic pins and semantic pins; every role
  grant repeats its artifact semantic and dependency pins. The evidence-only
  root envelope remains self-non-authorizing.
  ROOT_INITIALIZER authorizes its deterministic parentless occurrence, while only
  TERMINAL_ISSUER may attest the separate source-actualness sidecar and issue one
  of two production receipts. A root HIT has terminal-leaf and root-proof-close
  authority. A gaps-3/7/11 MISS has only registered-prefix-miss authority,
  global_exhaustion=false and next_unchecked_gap=15. The exact-HEAD assembler and
  independent production-receipt verifier are pinned non-role dependencies.
  Registry v3 cross-checks the v2 source/resolver, role manifest, scheduler and
  coverage-verifier digests. E1, queue, producer, T5 and branch authority remain
  false, so neither receipt permits recursive continuation.
claim_status: established
proof_provenance: repository_derivation
review_status: independent_review
topics:
  - T6
  - q-one
  - role-registry
  - root-initializer
  - terminal-issuer
  - terminal-first
  - exact-head
  - proof-boundary
sources:
  - data: data/t6-wave1/t6-coordinator-role-registry-v3.json
    role: fixed HEAD-free four-role source registry and authority policies
  - source: schemas/t6-coordinator-role-registry-v3.schema.json
    role: exact source, role, dependency, receipt and denial schema
  - reproduction: scripts/t6_coordinator_role_registry_v3.py
    role: exact-HEAD artifact/grant resolution and v2-v3 cross-registry replay
  - reproduction: tests/test_t6_coordinator_role_registry_v3.py
    role: focused pin, separation, dependency, receipt and authority attacks
  - source: scripts/t6_q_one_terminal_issuer_v1.py
    role: authorized source-actualness attestor and terminal decision issuer
  - source: scripts/t6_q_one_terminal_receipt_verifier_v1.py
    role: pinned post-issuance independent wire replay dependency
  - source: docs/audits/T6_Q1_PRODUCTION_TERMINAL_FINAL_INDEPENDENT_REVIEW_2026-08-26.md
    role: independent contract review, resolved findings and exact proof boundary
visibility: public
last_checked: '2026-08-26'
---

# Coordinator registry v3

## 1. 四个且仅四个角色

```text
INDEPENDENT_COVERAGE_VERIFIER = 1
ROOT_INITIALIZER              = 1
TERMINAL_ISSUER               = 1
TERMINAL_SCHEDULER            = 1
authorized branches           = []
```

`ROOT_INITIALIZER` 固定现有 q=1 root-envelope module 的 body、anchor、state factories。
该 module 的对象继续保存 `initializer_authority=false`：它们只描述无环 source shape，不自带
actualness。role grant 允许 coordinator 把这条 deterministic parentless construction 作为合法
root occurrence 的输入；实际 `QOneRootSourceActualnessReceiptV1` 只能由另一个 module 中的
`TERMINAL_ISSUER` 后置 attest。

initializer 与 issuer 必须具有不同 path、blob 和 semantic digest。issuer 不能以
同模块 helper 同时制造 source 并给自己授予 occurrence。actualness sidecar 绑定 root problem、
raw q=1 G replay、body/anchor/state、initializer+issuer grants、exact HEAD/tree 和 v3 role manifest；
同时固定：

```text
source_actualness = true
root_initializer_authority = true
initializer_output_self_authorizing = false
actualness_attestor_role = TERMINAL_ISSUER
persistent_admission = false
common_owner_authority = false
e1_authority = false
queue_authority = false
```

## 2. Non-role dependency DAG

assembler 精确登记为 `ISSUER_DEPENDENCY_ONLY`，不获得角色。production receipt verifier
登记为 `POST_ISSUANCE_REPLAY_DEPENDENCY_ONLY`，也不获得角色。

```text
v2 resolver + root initializer + scheduler + coverage verifier
                         -> exact-HEAD assembler

v2 resolver + root initializer + assembler
                         -> TERMINAL_ISSUER

v2 resolver + root initializer + assembler
                         -> post-issuance receipt verifier
```

当前固定 issuer bytes 不直接调用 scheduler、coverage verifier 或 receipt verifier；
scheduler/coverage 只由 assembler 的既有 fresh-execution path 消费。receipt verifier 不 import
issuer，而是从同一 raw root input、两份 registries、root factories 和 assembler 独立重建
expected production wire。因此不存在 issuer--verifier hash cycle。

上图只画 artifact DAG。issuer 与 receipt verifier 还 fresh 执行 v3 authority resolver；该 resolver
属于 exact-HEAD self/schema/registry toolchain binding，不作为依赖自身 registry pin 的 artifact，
从而避免 self-hash cycle。其 path 同时是 controlled-loader contract 中唯一额外允许的
`execution_toolchain_path`，不能被 caller 替换。

每个 executable artifact 固定：

```text
expected_blob_sha256
expected_symbol_ast_sha256 map
expected_symbol_set_digest
expected_local_import_closure_digest
expected_dependency_manifest_digest
expected_semantic_sha256
```

每个 dependency manifest 还要求 `artifact_semantic_pins` 的 key 集合精确等于
`execution_artifact_ids union binding_artifact_ids`，并在完整 DAG 解析后逐项等于 dependency 的
实际 semantic digest。role grant 再次固定 artifact semantic 与 dependency-manifest digest。
因此 dependency 合法更新而 consumer 未重签时仍会 fail closed；必须按拓扑序显式更新 consumer
pin，不能自动继承权限。

assembler、issuer 与 receipt verifier 内含 exact-HEAD fresh loader。resolver 额外固定每个 module
唯一 loader helper、唯一 caller 的 stable AST digest、全部 executable path constants、helper call
table，并要求该表精确对应 dependency manifest 加显式 v3 toolchain path。`compile`/`exec` 只能
出现在固定 helper 中，helper 也只能由固定 caller 以登记的 path constants 调用。即便把含额外
`compile`/`exec` direct loader 的 artifact blob/symbol/closure/semantic/grant 全部重签，该受控
loader 形状仍被拒绝；这不是对任意 Python execution mechanism 的完备静态证明。

## 3. v2-v3 cross binding

v3 不把 v2 evidence registry 改写成 issuer registry。resolver 从 requested HEAD fresh 执行固定
的 v2 resolver，重验 v2 仍只有 scheduler/verifier 两个角色、issuer/initializer/E1/queue/
producer/T5 均为空，并记录：

```text
v2 registry digest
v2 role-manifest digest
v2 scheduler/verifier role subdigests
v2 scheduler/verifier semantic digests
```

随后要求 v3 中相同 scheduler/verifier 的 cross pins 与 v2 resolved artifacts 逐项一致。production
receipt 同时绑定 v2 evidence registry 与 v3 authority registry，不能用一个 digest 冒充二者。

## 4. 两种 production authority

共同输入只能是 repository locator、exact full HEAD 和 raw q=1 G integers。caller 不能提交
state、domain、assembler decision、coverage DTO、callable、registry 或 authority flags。

`ProductionQOneRootTerminalReceiptV1` 必须重放 selected Type I/II certificate 和原始根方程。
它具有：

```text
terminal_leaf_authority = true
root_proof_close_authority = true
registered_prefix_miss_authority = false
producer_continuation_allowed = false
```

`ProductionQOneRegisteredPrefixMissReceiptV1` 固定：

```text
outcome = MISS_REGISTERED_PRIORITY_COMPLETE
coverage_semantics = REGISTERED_PRIORITY_ONLY
ordered_gaps = [3, 7, 11]
next_unchecked_gap = 15
global_exhaustion = false
terminal_leaf_authority = false
registered_prefix_miss_authority = true
root_proof_close_authority = false
producer_continuation_allowed = false
```

它不得使用旧的无 scope `MISS_COMPLETE`，也不能直接进入 E1 或 queue。

issuer module 的 local serializers 只检查 exact receipt class、局部字段/preimage、固定 authority
常量和 outer content seal。它们不重新解析 repository/HEAD，不认证 registry/grant/module-binding，
也不从 raw input 重建 body、anchor、state 或 assembler evidence 的 digest preimage。因此，一组内部
一致但换到另一条 source/registry 链后重新封口的 receipt，不能仅凭 local serializer 获得权限。
这类 cross-chain/body-anchor-state swap 必须由 pinned post-issuance exact-HEAD receipt verifier 以
显式 raw q=1 G input、两份 registries 和 assembler replay 拒绝。

## 5. 已执行的负控制

V3 registry focused tests 实际覆盖：artifact/grant/document pin drift；dependency semantic 变化但
consumer 未重签；四角色与两个 non-role 的精确基数；issuer direct execution dependency、replayer
execution-import issuer 与 dependency cycle；完整重签后在 public issuer 中增加未登记
`compile/exec` scheduler path；dynamic loader/import alias；authorized symbol rebinding；forbidden-root
import；v2-v3 cross pins；authority matrix、initializer self-authority、branch/producer denial；无效但
重签的 production JSON Schema；symbolic/abbreviated HEAD、Git replace 与 toolchain worktree drift。

Production focused tests 另覆盖五个真实 HIT/MISS issue-and-replay controls、import alias determinism、
Path subclass 拒绝和 type-specific ID schema。未重封的 HIT/MISS、global、E1、state、grant、HEAD
变异在 Schema 或 outer-seal 层被拒绝。一个完整重封的 `p=73 -> p=1201` body/anchor/state 换链会
通过 local serializer，但被 independent exact-HEAD expected-wire replay 拒绝；这是当前明确到达
深层 source 比较的 coherent forgery control。

本文不声称 selected-certificate null/non-null、registry/decision/evidence coherent reseal、receipt
写回 source-state preimage或任意新执行机制都已有逐项运行控制。前几项应在未来 consumer/E1 接入
时补成显式 mutation；最后一项超出当前 fixed-policy theorem。

上述结论的威胁模型是当前 exact-HEAD resolver/schema/source policy 与固定 executable bytes。
resolver 不是任意 Python 程序的通用语义判定器；若提交同时修改 controlled-loader AST contract、
resolver 和 source policy，或仅将 role artifact 换成使用 `subprocess` 等另一执行机制的新
semantic pin，那都是新的 authority policy，必须重新证明和独立审查，不能引用本 claim 作为
自动继承。后续把 TERMINAL_ISSUER 拆成无 loader 的纯 authority module 可以进一步缩小 trusted
surface，但不属于本 claim 已完成的结论。

## 6. 状态边界

resolved status 精确为：

```text
HEAD_BOUND_Q1_ROOT_TERMINAL_DECISION_AUTHORITY_NO_RECURSION
```

本结果足以对 ordinary parentless q=1 G root domain 的 gaps-3/7/11 schedule 做窄 production
issuance 验收：HIT 可结束根证明，MISS 只证明 registered prefix 完整 miss。它不提供 common
owner、prefix-aware E1 consumer、producer branch、E2--E5、target re-entry 或 queue mutation。
因此完整 Gate 4、Gate 5、F1、F2、F3、T6 与 Erdős-Straus 猜想仍保持开放。
