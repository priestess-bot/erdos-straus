# 近期证明包综合复核与归档（2026-08-21）

> 范围：本报告复核并整理截至 2026-08-21 位于 `docs/` 的七份证明包。原始 ZIP 已迁移到
> [`../archive/proof-packages/raw/`](../archive/proof-packages/raw/)，完整展开视图见
> [`archive/proof-packages/`](archive/proof-packages/)。

## 1. 结论

所有 ZIP 均通过容器完整性检查。F1、T6 workfiles、T2/T5、H4 的内部 manifest 均通过；
q=1 包的内部清单只有它对自身的 self-hash 不匹配，其他列出文件均通过；pre-T6 overlay 和
M-H 包没有内部 detached manifest。M-H 的 patch 能针对声明基线执行 `git apply --check`，其
两个聚焦 verifier 与四项 unit test 在完整仓库依赖环境下通过。

完整性与有限控制不等于全称证明。当前规范结论仍是：T1v1--T5v1 在各自限定范围内成立，
`T6_GLOBAL_SELECTOR_TOTALITY`、F1--F5 和 Erdős--Straus 猜想均为 `OPEN`。

## 2. 逐包处置

| 包 | 可接纳内容 | 明确不接纳/不推出 |
|---|---|---|
| H4 closure release | clean-q 的 E1--E5 relative macro 及其独立控制 | 其它 H4 branch、selector totality。 |
| q=1 fresh handoff | ordinary q=1 G 到 fresh full-carrier root 及首段 Type I segment 的 relative closure | marked state、后续 Type I totality、T6。 |
| T2/T5 full | T2 有限 admission grammar；T5 合同层七元势 | 所有 atomic arm、每个 nonterminal 的 edge 存在。 |
| T6 proof workfiles | positive-q G adapter、`k=1` proper-root exclusion、named-graph audit 等已入库引理 | `k>1` physicalization、c=8 outgoing、全局 selector。 |
| pre-T6/T6 overlay | 冻结 contract-kernel 和 admission firewall 的组织边界 | 语义 reachable-state exhaustion。 |
| F1 reachable-state exhaustion | O1 的分解、future-constructor 重开规则、已知 guard 命中时的 first-match 唯一性 | F1 closure；其 normalizer/owner 论域存在循环定义，producer 穷尽仅假设 registry。 |
| M-H final-two resolution | M 的 canonical complete-excess 算术与 `LOCAL_DROP`；H 的 C=1 同协议局部最小元 | M 的 universal E3/owner/re-entry；H 的一般 C>1 空改善分支；F1/F2/T6 closure。 |

## 3. M/H 的精确边界

M 的 target

\[
M=\operatorname{lcm}(A,Q),\qquad
pR'\equiv-1\pmod{4M},\qquad K'=(pR'+1)/4
\]

是确定的，且 low-support source 有

\[
\left\lfloor B_p/M\right\rfloor<\left\lfloor B_p/A\right\rfloor.
\]

它因此提供 E1 的 source algebra、E2、在 root-wide marking 下的 E4 和 `LOCAL_DROP`。
但它没有为所有 target 给出 E3 typing、owner、serializer 或 re-entry，也未注册到冻结的
15-edge surface。活动结论只能是 `CONDITIONAL_ON_E3_AND_SURFACE_ADMISSION`。

H 的 C=1 结果则是一个有效的局部 no-go：在同一 T5 `TYPEI/CHARGED` protocol，
\((0,1,0,0)\) 不可能被 complete-excess endpoint 严格降低，total-cofactor 是 stutter，
natural dual 又不保留 joined support。该结果要求另找 root terminal、outer-rank drop、
lower-protocol/phase target 或 family-empty proof；它不处理 C>1 的 terminal-first-miss
empty-improvement 状态。

详见 [M/H 复核报告](M-H-final-two-problem-audit-2026-08-20.md)。

## 4. 当前证明边界

```text
T1v1 H4 clean-q closure                 CLOSED_RELATIVE
T2v1 Atomic-Admission                   CLOSED_PHASE_LOCAL
T3v1 Mark Invariant                     CLOSED_CURRENT_GRAPH
T4v1 Fresh-G-Handoff                    CLOSED_RELATIVE
T5v1 Well-Founded Admission             CLOSED_CONTRACT_LEVEL
T6 Global-Selector                      OPEN

T6-F1 reachable-state exhaustion        OPEN
T6-F2 non-proper dispatch totality       OPEN
T6-F3 proper-root physicalization        OPEN
T6-F4 selector assembly and lifts        OPEN
T6-F5 independent closure audit          OPEN
Erdos-Straus conjecture                  OPEN_IN_THIS_REPOSITORY
```

具体量词、frontier owner 和验收门见
[T6 证明边界](T6-proof-boundary-2026-08-20.md) 与
[`data/t6-proof-frontier-v2.json`](../data/t6-proof-frontier-v2.json)。

## 5. 归档原则

原始 ZIP 保留为可校验来源；展开 payload 供全文检索与重读。归档中的 patch、旧 README、
生成 ledger 和 CI 仅描述当时 package snapshot，不能静默覆盖后续主仓库更严格的边界。后续
若要提升任一状态，必须在活动 state contract 中补齐明确量词、E1--E5、target owner/re-entry
及对应 T6 frontier 接口，而不是依赖存档的通过日志。
