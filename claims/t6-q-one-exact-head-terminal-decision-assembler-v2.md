---
kind: claim
claim_id: t6-q-one-exact-head-terminal-decision-assembler-v2
title: q=1 exact-HEAD non-authorizing terminal decision assembler V2
statement: >-
  给定 repository locator、exact full commit ID 与 raw ordinary q=1 G integers，V2 assembler
  先独立解析 repository/full HEAD/tree 并把 executing assembler 的 backing bytes 与 requested HEAD
  对齐，再将 registry resolver、root envelope、scheduler、coverage verifier 四个依赖从该 HEAD 的
  regular blobs 编译到 fresh private namespaces；随后才调用 fresh coordinator role resolver，重验其
  恰有一个 gaps-3/7/11 scheduler role、一个独立 coverage verifier role，且 issuer/initializer/E1/
  queue/producer/T5 authority 全为空，并把 scheduler/verifier 的 blob、symbol、import-closure、semantic
  与 grant pins 对齐。assembler 按 Body->Anchor->RawRootState DAG 构造稳定
  SOURCE_STATE，从 state 字段唯一派生 scheduler domain，顺序执行 authorized scheduler 与独立
  coverage verifier，最后输出 ROOT_TERMINAL_HIT_EVIDENCE 或 PREFIX_MISS_EVIDENCE 的 content-
  addressed typed decision。decision 后置绑定 state/anchor/HEAD/registry/grants/evidence/coverage，
  不进入 state ID；source_actualness 与 initializer/issuer/terminal/E1/queue authority 以及 producer
  continuation 均固定 false。本结果不提供 production issuer、terminal leaf authority、E1、runtime
  admission 或 queue mutation。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
  - T6
  - q-one
  - exact-head
  - terminal-decision
  - registered-priority-prefix
  - content-addressing
  - evidence-only
  - proof-boundary
sources:
  - reproduction: scripts/t6_q_one_terminal_decision_assembler_v2.py
    role: exact-HEAD fresh-dependency execution binding, state-derived execution and decision assembly
  - reproduction: tests/test_t6_q_one_terminal_decision_assembler_v2.py
    role: temporary exact-HEAD integration controls and authority/drift/swap negatives
  - claim: t6-coordinator-head-bound-terminal-prefix-role-registry-v2
    role: exact-HEAD scheduler and coverage-verifier capability grants without issuer
  - claim: t6-q-one-root-initializer-envelope-v2-contract
    role: acyclic evidence-only root SOURCE_STATE identity
  - claim: t6-q-one-registered-priority-prefix-independent-math-evidence-v1
    role: exhaustive registered-prefix evidence and independent coverage replay
visibility: public
last_checked: '2026-08-26'
---

# q=1 exact-HEAD non-authorizing terminal decision assembler V2

## 1. 唯一入口与权限前提

assembler 只有一个 keyword-only API：

```text
assemble_q_one_terminal_decision_v2(
  root,
  requested_head,
  raw_q_one_g
)
```

caller 不能传 registry mapping、artifact、grant、callable、scheduler domain、source state、terminal
evidence、coverage result 或 authority flags。

入口首先独立解析 repository、full HEAD 和 tree，验证 executing assembler backing，并从 exact blobs
fresh-compile 四个依赖；然后才调用 fresh
`t6_coordinator_role_registry_v2.resolve_registry_v2`，并要求 resolved status 精确为

```text
HEAD_BOUND_PREFIX_SCHEDULE_AUTHORITY_NO_ISSUER
```

resolved registry 必须只有：

```text
TERMINAL_SCHEDULER                  = 1
INDEPENDENT_COVERAGE_VERIFIER      = 1
authorized terminal prefix         = 1
authorized branches                = []
issuer count                        = 0
issuer/initializer/E1/queue/
producer/T5 authority               = false
```

assembler 重算 resolved registry、role-authority manifest、两项 grant 和 prefix binding 的 canonical
digests；它不把“两项 executable capability 已获授权”解释为 decision issuer authority。

## 2. exact HEAD 与 fresh dependency execution

所有 Git 命令都固定 `GIT_NO_REPLACE_OBJECTS=1`，并拒绝 symbolic 或 abbreviated HEAD。assembler
从同一 exact commit tree 读取以下 regular blobs：

```text
scripts/t6_q_one_terminal_decision_assembler_v2.py
scripts/t6_coordinator_role_registry_v2.py
scripts/t6_q_one_root_initializer_envelope_v2.py
scripts/t6_q_one_priority_prefix_scheduler_v1.py
scripts/t6_q_one_priority_prefix_coverage_verifier_v1.py
```

对 assembler 自身要求：

1. requested HEAD 中是普通 tracked blob；
2. 当前 repository worktree 文件逐字等于该 blob；
3. 当前执行模块的 `__file__` 是同一路径的普通非 symlink 文件；
4. backing bytes 逐字等于该 blob。

对其余四个 dependency，assembler 不使用 canonical import alias 或此前已加载对象。它先要求
worktree 字节等于 exact-HEAD blob，再直接从该 blob `compile+exec` 到唯一 private `ModuleType`
namespace。private 名称只在 dataclass/module 初始化期间临时进入 `sys.modules`，执行完立即恢复；
后续 resolver、root factories、scheduler、serializer 和 coverage verifier 全部取自本次 fresh
context。因此只修改 helper、class 或 module constant 后预加载模块，再恢复磁盘为 HEAD，不能影响
本次执行；对 canonical module attribute 的同名 wrapper 替换也没有调用路径。

scheduler 与 coverage verifier 还必须与 resolved artifact 的 Git mode/object ID/blob SHA、symbol、
symbol AST、local-import closure、semantic SHA 和 grant semantic pin 一致。fresh module binding
记录 exact blob、private namespace 和实际调用 symbol；registry resolver 也是 fresh context 中的
函数，不会先执行一个 canonical self-restoring wrapper。

assembler 和 root envelope 没有 registry role grant；这正是其 non-authorizing 边界。

这里保留一个不可消除的 trusted-process 边界：当前正在执行的 assembler 是自检逻辑的信任根。
它能证明 backing file 与 requested HEAD 一致，但不能在自身内部无循环地证明“这段已运行代码在
import 前从未被任意进程内攻击替换”。本 claim 不作 assembler 自身 pre-import integrity 定理；
它证明的是在可信当前 assembler 入口下，四个 dependency 的本次执行来自 exact HEAD。

## 3. state-first 无环执行顺序

raw integers 先经 root-envelope factories 构造

```text
CanonicalQOneGSourceBodyV2
  -> RootInitializerAnchorV2
  -> RawRootSourceStateV2
```

其中 anchor 不含 state ID，state ID 不含 terminal/schedule/result。assembler 不接受 caller domain，
而是从 `RawRootSourceStateV2` 的 equation、mark、q、G、phase、provenance、X 与 factorization 字段
逐项生成 `q1_priority_prefix_domain_v1`。因此 scheduler domain digest 被 SOURCE_STATE 的实际内容
唯一决定。

assembler 随后构造 scheduler invocation digest，绑定：

```text
HEAD/tree
registry + role manifest
schedule + two role grants
module binding
body/anchor/state IDs and digests
subject_kind = SOURCE_STATE
derived scheduler domain digest
```

固定调用顺序是：

1. authorized scheduler 生成完整 gaps 3/7/11 evidence；
2. scheduler serializer 重验 evidence；
3. independent coverage verifier 以同一 derived domain 重建完整 expected wire；
4. assembler 将 coverage DTO、verifier grant 与 evidence digest 合成为 coverage replay digest；
5. 再次捕获全部 module bindings，要求执行前后逐字相同；
6. 根据 verified outcome 构造 decision。

## 4. 两种后置 decision

两种 factory-only、frozen、slots 输出分别为：

```text
QOneRootTerminalHitEvidenceV2
QOneRegisteredPrefixMissEvidenceV2
```

共同字段绑定：

```text
HEAD/tree
registry and role-manifest digests
schedule and grant digests
scheduler/verifier semantic pins
module-binding digest
body/anchor/state IDs and digests
scheduler domain/invocation/evidence digests
coverage replay digest
coverage scope, next gap and three scan digests
```

HIT 另保存 selected Type I/II certificate 及 digest。assembler 在 coverage replay 之外再次检查
\(d\mid x^2\)、相应 Type I/II 同余、\(y,z\) 恢复公式与

\[
4xyz=p(xy+xz+yz).
\]

MISS 强制 `selected_certificate=null`，且只表示 registered prefix miss。

两个 decision 都固定：

```text
evidence_class                = EXACT_HEAD_NON_AUTHORIZING_TERMINAL_DECISION
source_actualness             = false
initializer_authority         = false
issuer_authority              = false
terminal_authority            = false
e1_authority                  = false
queue_authority               = false
producer_continuation_allowed = false
global_exhaustion             = false
next_unchecked_gap             = 15
```

decision ID 是后置内容摘要，绝不写回 body、anchor 或 state ID。serializer 对 exact class、全部 typed
字段、authority、certificate、digest 和 ID 重验；经底层对象构造绕过 frozen、重算 seal 的 authority
flip 仍被拒绝。

standalone serializer 只验证 decision 自身的 typed shape、局部数学字段与外层 content seal；它不会
脱离 repository、HEAD、registry 和 scheduler transcript 重新解析各 digest 的 preimage。upstream
provenance 的认证只属于 `assemble_q_one_terminal_decision_v2` 的 exact-HEAD 执行路径。未来 consumer
不得仅凭一个手工构造且局部自洽的 decision object 授予任何权限。

## 5. exact-HEAD 控制

聚焦测试在临时 Git repository 中复制全部 required artifacts 并创建真实 commit；测试提交不会写入
当前项目历史。

- \(p=73\) 输出 `ROOT_TERMINAL_HIT_EVIDENCE`；
- \(p=193\) 输出 Type I、gap 7、\(d=10\) 的 `ROOT_TERMINAL_HIT_EVIDENCE`；
- \(p=1201,2521\) 输出 `PREFIX_MISS_EVIDENCE`；
- symbolic/short/stale HEAD、grant swap、required worktree drift 被拒绝；
- canonical scheduler、root-state factory、coverage module 与 resolver wrapper 的替换不被调用；
- scheduler、coverage verifier、root-envelope helper 的恶意 stale module 即使先加载且磁盘恢复，
  也不进入 fresh dependency execution，副作用不会发生；
- Git replace ref 不能改变 requested HEAD；
- caller domain/authority、legacy state/terminal receipt 字段被拒绝；
- decision authority 重封被拒绝。

```bash
python3 -m unittest tests.test_t6_q_one_terminal_decision_assembler_v2 -v
ruff check scripts/t6_q_one_terminal_decision_assembler_v2.py \
  tests/test_t6_q_one_terminal_decision_assembler_v2.py
python3 -m py_compile scripts/t6_q_one_terminal_decision_assembler_v2.py \
  tests/test_t6_q_one_terminal_decision_assembler_v2.py
```

## 6. 明确非结果

本 assembler 没有 production issuer API，不生成 `RegisteredPriorityPrefixMissReceiptV2` 或任何可被
E1 直接消费的 receipt，不调用 runtime/admission/queue，也不授予 source actualness。它只证明：
在一个 exact HEAD 上，由已授权 scheduler/verifier 对一个 evidence-only root SOURCE_STATE 执行得到
的数学 decision，可以被无环、内容寻址地装配。

未来 production terminal issuer 仍须获得独立 `TERMINAL_ISSUER` grant，并另行绑定 initializer
actualness、common owner、subject occurrence 和 consumer policy。未来 E1V2 还必须显式接受
`MISS_REGISTERED_PRIORITY_COMPLETE` 的有限 scope；不能复用旧 `MISS_COMPLETE` 布尔语义。
