---
kind: claim
claim_id: t6-coordinator-head-bound-terminal-prefix-role-registry-v2
title: T6 q=1 注册终端前缀的 HEAD-bound 双角色授权 v2
statement: >-
  The tracked t6_coordinator_role_registry_v2 source contains no HEAD and grants
  exactly two executable capabilities for the single schedule
  q1_root_gap_3_7_11_registered_priority_prefix_v1: TERMINAL_SCHEDULER to
  replay_q_one_priority_prefix_v1, and INDEPENDENT_COVERAGE_VERIFIER to
  verify_q_one_priority_prefix_coverage_v1. The latter may also perform the
  declared DOMAIN_VERIFIER, CERTIFICATE_VERIFIER and ROOT_TERMINAL_VERIFIER
  capabilities within the same independent replay. The resolver reads an exact
  full Git commit with GIT_NO_REPLACE_OBJECTS, binds its own source, schema and
  registry bytes, requires tracked blob/symbol-AST/import-closure/semantic pins
  and a second semantic pin in each grant, resolves both local AST symbols and
  Git blobs, computes each local-import closure, and requires distinct module
  paths and blob digests. Code changes do not inherit a role unless the tracked
  registry pins are explicitly updated. The
  verifier closure contains neither the scheduler, legacy runtime nor a
  reproduction module. The fixed schedule covers only gaps 3,7,11, names 15 as
  the next unchecked gap, has REGISTERED_PRIORITY_ONLY semantics and
  global_exhaustion=false, and returns only ROOT_TERMINAL_HIT or
  PREFIX_MISS_EVIDENCE_ONLY evidence. Status is exactly
  HEAD_BOUND_PREFIX_SCHEDULE_AUTHORITY_NO_ISSUER: issuer_count=0 and no E1,
  queue, producer, initializer, T5, branch or terminal-issuance authority exists.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
  - T6
  - terminal-first
  - role-registry
  - proof-receipt
  - exact-head
  - proof-boundary
sources:
  - data: data/t6-wave1/t6-coordinator-role-registry-v2.json
    role: fixed HEAD-free two-grant source registry
  - source: schemas/t6-coordinator-role-registry-v2.schema.json
    role: exact source field, artifact, grant, prefix and denial allowlist
  - reproduction: scripts/t6_coordinator_role_registry_v2.py
    role: exact-Git resolver, AST/closure binding and authority separation
  - reproduction: tests/test_t6_coordinator_role_registry_v2.py
    role: focused role, import, copy, replacement and no-issuer controls
  - source: scripts/t6_q_one_priority_prefix_scheduler_v1.py
    role: authorized terminal-prefix scheduler artifact
  - source: scripts/t6_q_one_priority_prefix_coverage_verifier_v1.py
    role: authorized independent coverage/domain/certificate/root-terminal replay artifact
visibility: public
last_checked: '2026-08-26'
---

# T6 coordinator role registry v2

## 1. 授权面

source registry 只允许一个 schedule：

```text
schedule_id = q1_root_gap_3_7_11_registered_priority_prefix_v1
ordered_gaps = [3, 7, 11]
next_unchecked_gap = 15
coverage_semantics = REGISTERED_PRIORITY_ONLY
global_exhaustion = false
outcomes = [PREFIX_MISS_EVIDENCE_ONLY, ROOT_TERMINAL_HIT]
```

它只包含两个 role grants：

| role | artifact | symbol | capabilities |
|---|---|---|---|
| `TERMINAL_SCHEDULER` | `scripts/t6_q_one_priority_prefix_scheduler_v1.py` | `replay_q_one_priority_prefix_v1` | `REGISTERED_PRIORITY_PREFIX_REPLAY` |
| `INDEPENDENT_COVERAGE_VERIFIER` | `scripts/t6_q_one_priority_prefix_coverage_verifier_v1.py` | `verify_q_one_priority_prefix_coverage_v1` | `DOMAIN_VERIFIER`, `CERTIFICATE_VERIFIER`, `ROOT_TERMINAL_VERIFIER` |

后三项是同一个 independent replay 内部已经承担的 capability，不是三个新的角色，也不
产生 producer、issuer 或 admission 权限。

## 2. HEAD 与代码绑定

tracked source registry 不写 `head_sha`，因此没有提交自引用。resolver 的调用者只能提供
repository locator 和 exact full commit object ID；不能提供 registry mapping、path、role、
artifact 或 callable override。所有 Git 调用固定：

```text
GIT_NO_REPLACE_OBJECTS=1
```

resolver 从该 commit 的 tree 读取 registry、schema、scheduler 和 verifier，并验证：

1. 正在执行的 resolver、worktree schema、worktree registry 与 requested-HEAD blob 逐字相同；
2. artifact 是 `scripts/` 下的普通 tracked Python blob；
3. 固定 symbol 在 module scope 恰有一个本地函数定义；
4. source artifact 分别固定 expected module blob、stable symbol AST、local-import closure
   与 semantic digest；grant 再次固定对应 semantic digest，resolver 对每一项重算比较；
5. stable symbol AST 使用 canonical JSON，忽略 Python 版本新增但为空的 `type_params`；
   Python 3.12/3.13 的解释器版本只可由非权限诊断 helper 返回，不进入 resolved payload
   或任何 authority/registry digest；
6. scheduler 与 verifier 的 path、blob digest 和 semantic digest 不同；
7. verifier closure 不含 scheduler、旧 persistent runtime 或 `reproductions/**`；scheduler
   也不能反向导入 verifier，二者除各自 root 外不能共享 local helper；
8. 授权 symbol 在完整 module-scope binding audit 中只有一个无 decorator、无条件定义的
   `FunctionDef`；import alias、assignment、loop/with/match/except target、named expression、
   delete 或其它二次绑定都会拒绝；
9. authorized module 禁止 `importlib`、`runpy`、`pkgutil`、`builtins` loader，以及
   `exec/eval/compile/__import__` 和 `sys.path/modules/meta_path/path_hooks` 动态加载面。

resolver 不 import 或执行两个 artifact。它建立的是 exact-HEAD capability manifest，
不是执行结果或数学真值的签名。

## 3. 固定前缀语义

registry 绑定已有独立证据层的精确接口：完整重放 gaps 3、7、11 中每个
$d\mid x_m^2$ 的 Type I/II 候选，并按 gap、divisor、Type I before Type II 排序。命中
时输出 `ROOT_TERMINAL_HIT` evidence；三层全部 miss 时输出
`PREFIX_MISS_EVIDENCE_ONLY`。后者明确记录 `next_unchecked_gap=15`，不排除 gap 15 以后
的根证书，也不构成 global terminal exhaustion。

本 registry 只授权 scheduler 和 independent verifier 的代码身份及上述 scope。实际
domain/certificate/root-terminal correctness 仍由被固定的 independent verifier 重放；
仅有 registry manifest、DTO 或 digest 不足以证明一次具体 replay 已成功。

## 4. 强制拒绝

schema 与 resolver 同时拒绝：

```text
caller role/artifact/callable override
code drift without explicit artifact and grant pin updates
unknown role or branch binding
producer, initializer, T5, E1 or queue grant
issuer count or issuer authority above zero
tests/docs/archive/reproductions executable grant
scheduler/verifier same path or byte-identical module
verifier import of scheduler, legacy runtime or reproductions
scheduler import of verifier
shared local helper between scheduler and verifier
resolved or unresolved tests/docs/archive/reproductions import
importlib/runpy/pkgutil/builtins loader and dynamic code/import calls
missing, imported-only or ambiguous symbol
decorated, conditional or module-scope rebound authorized symbol
symbolic/abbreviated HEAD and Git replacement refs
dirty resolver/schema/registry relative to requested HEAD
schedule gap/order/scope/global/outcome mutation
```

## 5. 当前边界

resolved status 精确为：

```text
HEAD_BOUND_PREFIX_SCHEDULE_AUTHORITY_NO_ISSUER
issuer_count = 0
issuer_authority = false
e1_authority = false
queue_authority = false
producer_authority = false
initializer_authority = false
t5_authority = false
authorized_branches = []
```

因此本卡不签发 production terminal receipt，不把 prefix miss 接入 E1，不调用旧 runtime，
也不允许任何 queue mutation。将来若要消费这些能力，必须新增独立 issuer/consumer 合同并
重新接受审计；不得仅凭本 registry 的存在扩大权限。本卡不关闭 Gate 2、Gate 4、F1、
F2、F3、T6 或 Erdős-Straus 猜想。
