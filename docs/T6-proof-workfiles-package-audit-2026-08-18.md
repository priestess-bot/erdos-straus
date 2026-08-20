# T6 证明工作包复核与合并记录

> 复核日期：2026-08-18
>
> 输入包：[`../archive/proof-packages/raw/erdos-straus-T6-proof-workfiles-2026-08-17.zip`](../archive/proof-packages/raw/erdos-straus-T6-proof-workfiles-2026-08-17.zip)
>
> ZIP SHA-256：`c7e7f63da0d040fdbaede1244b774d25c594c60bb4ec51fdfd091577f8c5981a`

## 1. 复核范围

压缩包声明以上游提交 `203716ba6f6478ded538674e34f214384d15fd1b` 为基线，包含 24 个
新增或修改文件、5 个 claim、5 个 focused reproduction、T5 taxonomy/state-contract 同步和
两份随包附带的 patch。复核时先执行 ZIP 完整性测试和包内 SHA-256 清单校验，再把包内完整
文件叠加到干净的 `203716b` 工作树中运行验证；没有直接把 patch 当作当前工作树的唯一来源，
以包内完整文件为准，避免 patch 上下文与当前仓库历史不一致造成误合并。
对当前仓库直接执行 `git apply --check` 时，patch 的部分上下文与现有文件历史不一致；这
不影响完整文件叠加后的验证结果，也正是本次采用文件级审计而非强行套 patch 的原因。

## 2. 合并结果

以下内容已合并到知识库：

- ordinary actual terminal-first positive-q G 到 p-only full-carrier Type-I root 的相对 adapter，
  以及 q=1/positive-q 两个 origin 共用的首条 local-edge normalization；
- proper-root stutter 的 `c=h` named odd-distance translated-square fan no-go；
- actual proper-root quotient 的 `k=1` 全称排除及其 Vieta 无限下降证明；
- 原 T6 数值线索的 root-provenance 失败与 gap-3 terminal-first 抢占审计；
- 当前 named graph 的 ordinary-mark 闭包、T2 named atomic surface 和 c=8 最小剩余量词审计；
- T5 transition taxonomy、state contract、旗舰纲领、T6 入口文档和 theorem ledger 的同步。

## 3. 数学状态判定

| 项目 | 合并后的判定 | 不能推出的内容 |
|---|---|---|
| positive-q ordinary G handoff | `established`, `repository_derivation`, `internal_review` | 不证明 source state 存在；不处理 nontrivial mark 或后续 Type-I totality |
| 首条 origin-normalized local edge | 在 actual handoff root 假设下建立 | focused controls 没有制造 actual parent receipt，因此不是独立的 unconditional edge |
| `c=h` named fan | `established` named-family no-go | 不排除其它 even-source/lift family，不产生 successor |
| proper-root `k=1` | `established`，actual 子域为空 | 不处理 `k>1` quotient physicalization 或 transverse carrier |
| 数值线索审计 | `established`，该点不是 actual receipt 且被 terminal 抢占 | 不构成 proper-root/T6 全称反证 |
| named ordinary-mark/T2 coverage | `established` closed-world audit | 不证明 outgoing existence，不覆盖 future marked/atomic generators |
| T6 selector totality | `OPEN` | 仍缺 QC1、TR1、c=8 outgoing existence 和全局 reachable-state exhaustion |

## 4. 验证记录

在完整仓库临时副本中复核包内文件，结果如下：

```text
unzip -t                                      PASS
SHA256SUMS                                   PASS (全部文件)
py_compile (5 个新增 reproduction)             PASS
ruff check (5 个新增 reproduction)             PASS
5 个 focused verifier                         PASS
python3 scripts/kb.py validate                 PASS: 1382 documents
python3 scripts/kb.py build                    PASS
```

positive-q G 和 named-reachability 两个脚本依赖整仓既有 claim/reproduction；在只解压增量
文件的目录中预期会因缺少上游依赖失败，叠加到完整基线后均通过。所有 controls 都明确输出
conditional 或 closed-world scope，没有将有限扫描升级为 T6 totality。

## 5. 保留的开放边界

本次合并不得把下列命题改写为已证明：

1. 每个 actual reachable nonterminal state 都存在 terminal 或 verified successor；
2. proper-root `k>1` 的 quotient factor 已连接到 actual physical carrier；
3. transverse `D_*` factor 已取得可消费的 source provenance；
4. 每个 terminal-first-surviving c=8 parent 都有 high-q double-low label 或其它合法出口；
5. 首条 Type-I local edge 之后的全局 selector totality；
6. Erdős--Straus 猜想本身已证明。

因此当前旗舰状态继续保持：

```text
T6_GLOBAL_SELECTOR_TOTALITY = OPEN
```
