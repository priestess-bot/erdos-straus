---
kind: claim
claim_id: t6-persistent-selector-runtime-v2-zero-authority-cut
title: T6 persistent selector runtime V2 零授权拒绝截面
statement: >-
  The V2 persistent-selector runtime resolves the coordinator role registry and
  complete-terminal schedule registry from one exact requested Git commit and
  opens only in the current zero-authority state: zero role grants, zero
  authorized routes, zero initializers and zero COMPLETE terminal schedules.
  Its public construction API accepts no caller producer, projector, validator,
  scheduler, evidence-ID or artifact-digest manifest. Under the trusted-process
  and public-factory model, every bootstrap attempt is rejected before queue
  mutation. Legacy/raw successor inputs are rejected, and even a factory-sealed
  acyclic V2 target/transition/sidecar request is replay-checked and then
  rejected because no successor route is authorized. The queue therefore
  remains empty through the public API. This fail-closed migration cut does not
  establish a production route, complete terminal replay, Gate 2, T6 or the
  Erdos--Straus conjecture.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
  - T6
  - persistent-selector
  - exact-HEAD
  - fail-closed
  - proof-boundary
sources:
  - reproduction: scripts/t6_persistent_selector_runtime_v2.py
    role: exact-HEAD zero-authority resolver and immutable rejection runtime
  - reproduction: tests/test_t6_persistent_selector_runtime_v2.py
    role: injection, legacy-type, V2 replay and queue-invariance negative controls
  - data: data/t6-wave1/t6-coordinator-role-registry-v1.json
    role: fixed coordinator evidence inventory with zero role grants
  - data: data/t6-wave1/t6-complete-terminal-schedule-registry-v1.json
    role: fixed production terminal registry with zero COMPLETE schedules
  - source: scripts/t6_acyclic_transition_bundle_v2.py
    role: factory-sealed V2 target, transition and admission-sidecar shapes
visibility: public
last_checked: '2026-08-26'
---

# T6 persistent selector runtime V2 零授权拒绝截面

## 1. 构造来源

`open_runtime_v2(root, requested_head)` 只有 repository locator 和完整 40 位 commit
两个输入。它先调用既有 coordinator role resolver，再从同一个 commit 的 Git tree 直接
读取 complete-terminal registry；caller 不能替换 registry、路径、callable table 或
artifact manifest。执行中的 V2 runtime 自身、terminal contract 与 acyclic V2
dependency 都必须存在于 requested HEAD，并且执行时加载的 backing bytes 与该 HEAD
中的对应 regular blob 逐字匹配。runtime 文件缺失、worktree 漂移或 loaded bytes
漂移都会在 authority snapshot 构造前拒绝。

运行时只在下列事实同时成立时构造：

```text
active role grants             = 0
authorized successor routes    = 0
initializers                    = 0
COMPLETE terminal schedules     = 0
evidence inventory authority    = false
```

计数必须是精确的 JSON/Python integer `0`，`false` 不能冒充零。resolved coordinator
registry 和 authority snapshot 的 canonical digest 都必须重新播放一致。

## 2. 拒绝与队列不变

runtime 以冻结空 tuple 保存 queue，并且没有内部或外部 enqueue API。

- `bootstrap_v2()` 以 `BOOTSTRAP_AUTHORITY_UNAVAILABLE` 拒绝；
- caller raw state、V1 initializer 或 caller manifest 以
  `CALLER_BOOTSTRAP_PAYLOAD_FORBIDDEN` 拒绝；
- V1 `TransitionValidationV1`、`TerminalMissV1`、raw successor、`evidence_ids`
  collection 和 caller manifest 以 `CALLER_OR_LEGACY_SUCCESSOR_FORBIDDEN` 拒绝；
- exact-class acyclic V2 target、final transition bundle 与 admission sidecar 会先重放
  seal 和相互引用，随后仍以 `SUCCESSOR_AUTHORITY_UNAVAILABLE` 拒绝。

所有分支均在 queue mutation 之前结束，测试逐项比较拒绝前后的 queue snapshot。

## 3. 未建立的内容

该截面没有 producer、projector、independent validator、complete terminal scheduler、
T5 ticket verifier 或 initializer 的 active role grant。Acyclic V2 bundle 的字段/seal
自洽也不产生 E1--E5 语义 authority。因此该 claim 只证明当前 runtime 的零授权拒绝
性质，不关闭 Gate 2、F1、F2、F3、T6，也不证明 Erdos--Straus 猜想。

更精确地说，successor request 的当前 replay 只覆盖 `RawTargetStateV2`、
`FinalTransitionReceiptBundleV2`、`StateAdmissionSidecarV2` 的末端 content seal、target
绑定和 edge-anchor 互引；它不重放 upstream projection/preclassification/terminal/T5
draft/anchor，也不检查 E1--E5 receipt digest 的 preimage 或数学语义。由于零 route 会在
其后无条件拒绝，这个缺口不会在本版本产生 queue authority，但它必须在任何正授权
runtime 出现前闭合。

这里的不可变性还是 trusted-process/public-factory theorem，而不是 Python 进程内安全
边界。`object.__new__`、`object.__setattr__`、替换 `sys.modules` callable 或 monkeypatch
均不在 claim 的威胁模型内；生产运行应由受控入口启动，并禁止不受信任代码共享同一
解释器进程。
