# Erdos–Straus T6 本轮证明工作包

打包日期：2026-08-17

## 范围

本压缩包只包含本轮围绕 T6 新增或修改的文件，不包含远程 GitHub 仓库的其余源码、`.git` 历史、缓存、依赖或此前生成的整仓压缩包。

- 上游基线：`203716ba6f6478ded538674e34f214384d15fd1b`
- 本轮最终提交：`1caa7db4d82d23baa000f833687e4246708a57c6`
- 提交范围：`203716b..1caa7db`
- 仓库文件变更：24 个（新增或修改）
- 代码变更统计：3585 行新增、84 行删除

## 目录

- `files/`：24 个新增或修改后的完整文件，保持原仓库目录结构。
- `patches/`：本轮两个 Git 提交的可应用补丁。
- `CHANGED_FILES.txt`：逐文件新增/修改状态清单。
- `DIFFSTAT.txt`：变更统计。
- `SHA256SUMS`：包内全部文件的 SHA-256 校验值。

## 本轮已建立的结果

1. ordinary、actual、terminal-first positive-q G 的 full-carrier phase-root 相对适配器。
2. proper-root stutter 中 `k=1` actual 子域的全称排除。
3. `c=h` named odd-distance fan 的条件性 no-go。
4. 当前 named reachable graph 上的 T2/T3 closed-world coverage 审计。
5. 数值线索的 terminal-first preemption 核验。
6. T5/state-contract/taxonomy/theorem-ledger 与上述结果的同步。

## 重要状态边界

本工作包没有宣称 T6 已彻底闭合。当前仍保留的主要开放量词包括：

- proper-root `k>1` 的 quotient-carrier physicalization（QC1/TR1）；
- c=8 分支的 actual/global exhaustion；
- 对每个 actual reachable nonterminal state 的 verified outgoing edge 非空性；
- 在上述 totality 成立后固定不读取未知解的 deterministic selector。

因此，包内文档一致标记 `T6_GLOBAL_SELECTOR_TOTALITY=OPEN`。

## 已完成验证

- 新增 focused verifiers 通过；
- T5 transition-surface audit 通过；
- Python `py_compile` 通过；
- Ruff 检查通过；
- knowledge-base validation 通过（1382 documents）；
- `git diff --check` 通过。

