# T6 证明边界（2026-08-20）

> 固定基线：`ef95ac0f2c3b687bb67d33dc490b248ccd8cfcb0`
> 当前状态：`T6_GLOBAL_SELECTOR_TOTALITY = OPEN`。
> 本文只关闭可由现有证据直接完成的结构、账本和局部算术义务；不把 arithmetic dispatch
> 当作 E1--E5 edge。

## 1. T6 的精确目标

对每个核心素数 \(p\equiv1\pmod{24}\) 和每个从规范初始状态实际递归可达的合法状态
\(S\)，需要一个确定、可计算的 selector

\[
\Sigma(p,S)\in
\{\text{root/marked terminal certificate},\ \text{verified edge }S\to T\}.
\]

若输出后继 \(T\)，必须连续提供：

- E1：实际 source receipt 和可重放路径；
- E2：确定性的合法 target；
- E3：target normal form、scope、owner 和 state typing；
- E4：\(W_T\to W_S\) 的全称 lift；
- E5：固定 T5 势上的严格 ticket。

因此下列蕴含均禁止使用：

\[
\text{arithmetic candidate}\not\Rightarrow\text{verified edge},
\]

\[
\text{registered taxonomy}\not\Rightarrow\text{semantic reachable-state exhaustion},
\]

\[
\forall(S,T)\,[\operatorname{verified\_edge}(S,T)\Rightarrow\Pi(T)<\Pi(S)]
\not\Rightarrow
\forall S\,\exists T\,\operatorname{verified\_edge}(S,T).
\]

## 2. 已立即闭合的 T6 项

机器可读状态见 `data/t6-proof-frontier-v2.json`。

| ID | 闭合内容 | 结论强度 |
|---|---|---|
| `T6-M0-INITIAL-SERIALIZER` | 每个核心 \(p\) 的 \(q=1,m=3,X=(p+3)/4\) 初始分派 | 完整 root dispatch；不含后续 totality |
| `T6-M1-NAMED-SURFACE-INVENTORY` | 冻结 16 个 family 和 15 个 edge generator | closed-world inventory |
| `T6-M2-CURRENT-MARK-UNREACHABILITY` | initializer 和 15 条 edge 都不产生 nontrivial mark | closed-world invariant |
| `T6-M3-CONSTRUCTOR-ADMISSION-FIREWALL` | 未注册 atomic/marked target 在合并前被拒绝 | repository policy；新增构造器即重开 |
| `T6-M4-M3-Q5-PFREE-RAW-POLICY` | actual raw occurrence 至多两次 factor consumption 到 p-free primitive node | arithmetic reduction only |
| `T6-M5-PBLOCK-POLICY-ELIMINATION` | p-block 不是 raw policy 的必要独立分支 | arithmetic reduction only |
| `T6-M6-CANONICAL-CHANNEL-PARTITION` | \(L_\omega=1+p\theta\) 后按 \(\theta\bmod p\) 的四个 channel 完备分派 | arithmetic reduction only |
| `T6-M7-P2-RESIDUAL-ISOLATION` | 重复 canonical hard branch 精确压缩到 \(L_\omega\equiv1\pmod{p^2}\) | arithmetic reduction only；gate 未排空 |

其中只有 M0 是完整的 selector 输出闭包。M1--M3 是证明工程闭包；M4--M7 是算术闭包。
审计器强制 M4--M7 的 `edge_complete=false`，避免后续文档把它们静默升级成 verified edge。

## 3. 冻结 family 的明确归属

| family | 当前状态 | 唯一 proof owner |
|---|---|---|
| `initial_core_root` | root 已有 universal successor/terminal | M0 |
| `type_ii_relation_f_endpoint` | 在书面 guard 下有 universal successor | F2 负责全局组合 |
| `type_ii_relation_g_endpoint` | 只有 relative handoff edge | F2 |
| `type_i_full_carrier_post_g` | OPEN | F2 |
| `type_i_low_support_persistent_overflow` | 局部 family 已有 universal successor | F2 负责组合与可达域 |
| `type_i_a_one_overflow` | 局部 family 已有 universal successor | F2 负责组合与可达域 |
| `type_i_a_gt_one_overflow_residual` | OPEN | F2 |
| `type_i_high_support_sink` | improvement 非空时只有 local edge | F2 |
| `proper_root_stutter_k_one` | empty proof 已闭合 | F3 负责与 \(k>1\) 分支拼接 |
| `proper_root_stutter_k_gt_one` | OPEN | F3 |
| `c8_terminal_first_surviving_parent` | OPEN | F2 |
| `h4_non_v1_branch_or_descendant` | OPEN | F2 |
| `type_i_c2_19_macro_target` | OPEN | F2 |
| `t2_v1_atomic_pending_target` | OPEN | F2 |
| `generic_nontrivial_marked_state` | frozen graph 中不可达 | admission firewall |
| `direct_terminal_leaf` | TERMINAL | terminal verifier/lift |

此表只对冻结 grammar 完备。证明“每个 actual reachable state 都在表中”仍是 F1，而不是
M1 的推论。

## 4. 剩余证明前沿：五个定理

### T6-F1：reachable-state exhaustion

必须证明

\[
\forall p\ \forall S\in\operatorname{Reach}(p),
\quad S\text{ 非终端}
\Longrightarrow
S\text{ 在 terminal-first 后恰属于一个登记 family}.
\]

最低验收条件：

1. 从合法 state constructor 作独立结构归纳，而不是从现有 taxonomy 反推；
2. 对每个 constructor 给出完整 guard partition；
3. 证明所有 target 重新进入分类域；
4. 明确 H4、atomic、overflow、post-G 和 marked 输出没有遗漏；
5. 新 family 必须先通过 admission firewall。

F1 未完成以前，“下面的列表是所有剩余数学缺口”只能理解为当前登记清单，不能理解为
语义上绝对穷尽。

**2026-08-20 F1 包复核。** 外部候选包曾把 F1 标为 `CLOSED_CONTRACT_LEVEL`，但其
`legal persistent state` 定义预设 normalizer 已成功分类，且未把 header extractor、normalizer、
owner digest 与 enqueue gate 接入当前状态合同；它也只假设 15 个 registry producer，而没有独立
枚举全部 constructor。因此该闭合结论未被接纳，F1 保持 `OPEN`。完整依据、输入完整性与
可接纳的后续接口见 [F1 reachable-state exhaustion 包复核](F1-reachable-state-exhaustion-package-review-2026-08-20.md)。

### T6-F2：non-proper dispatch totality

必须证明每个已分类、非 proper-root 的非终端状态都 terminal 或有完整 E1--E5 successor。
它合并并保留以下六个 active legacy gap：

1. `GAP-O1-H4-OTHER-BRANCHES`：T1v1 之外所有 H4 branch 和 F/G descendant；
2. `GAP-O1-POST-G-TYPE-I`：ordinary G handoff 首段之后的全部 Type I continuation；
3. `GAP-O1-A-GT-ONE-OVERFLOW`：每个 actual \(A>1\) residual 的 source receipt 与出口；
4. `GAP-O1-HIGH-SUPPORT-ROOT-CAPACITY`：improvement set 为空时的 empty/terminal/edge；
5. `GAP-O1-ATOMIC-TARGET-CLOSURE`：H4/c=8 macro 发出的每个 nonterminal target；
6. `GAP-O3-C8-OUTGOING`：每个 c=8 parent 的 terminal/double-low/other-edge 三分。

“有一条 conditional adapter”不足以关闭某 family；需要证明 adapter 的 guard 对该 family
全覆盖，或给出其余 guard 的 terminal/empty/edge。

### T6-F3：proper-root physicalization

必须证明

\[
\forall S\in\operatorname{ProperRoot}_{k>1},
\quad
\operatorname{terminal}(S)
\lor
\exists T\;\operatorname{verified\_edge}(S,T).
\]

这需要同时完成六个子定理：

1. **全域路由。** 每个 \(k>1\) proper-root 必须确定性进入 QC1、TR1、已覆盖的
   \((m,q)\) slice，或另一显式 family；不能默认所有状态都进入 \(m=3,q=5\)。
2. **persistent E1 source。** 当前 raw factor policy 的每个 factor consumption 和 p-free
   endpoint 必须绑定实际 parent receipt 与可重放路径。
3. **连续 E2--E4。** terminal priority、target typing、normal form、scope/owner 和 lift
   必须覆盖整个 macro，而不是只验证 endpoint 同余。
4. **atomic checkpoint 与 second child。** 第一 canonical child 未终结时，第二 child 的
   存在、确定 tie-break、非重复性、typing、lift 和 E5 ticket 都要证明。
5. **\(p^2\) gate。** 对
   \[
   L_\omega\equiv1\pmod{p^2}
   \]
   证明 family-empty、terminal 或另一条 paid successor。继续提升到 \(p^3\) 而没有严格下降
   不构成闭包。
6. **target recursion。** 所有 channel target 必须落入 F2 已闭合 family、terminal，或有
   F3 内的严格后继；不能把 proper-root gap 转移成未登记 atomic/high-support gap。

#### 当前 \(p^2\) 边界

现有推导还给出二阶必要同余

\[
\ell D_y\equiv
1-D_1+p\left[3+\sigma\bigl((\ell-2)D_1+1\bigr)\right]
\pmod{p^2}.
\]

下一项有效成果必须是对 actual divisor source 的统一解分类：参数范围、除数约束与同余的
相容性、无解证明或可付费 target。只做有限枚举或只写商层 divisor 存在性不提供 E1/E4。

### T6-F4：selector assembly and lifts

F1--F3 关闭后，还要构造一个单一算法而不是一组互不排序的候选规则。必须证明：

- terminal-first 和 branch precedence 无歧义；
- 每个 tie-break 确定且可计算；
- 每条实际选择边都有 E1--E5；
- 每个 terminal certificate 沿父 receipt 全局提升到根；
- 所有递归调用严格降低同一个固定 \(\mathbb N^7\) 势；
- strong induction 不使用任何 open、finite-only 或 analysis-only lemma。

只有此时 T5v1 才能从“每条 admitted edge 下降”升级为 T6 的全局终止证明。

### T6-F5：independent closure audit

最终验收必须在完整 checkout 上由与构造逻辑分离的实现完成：

1. `scripts/kb.py validate` 和索引一致性通过；
2. 每个 selector receipt 独立 replay；
3. v1/v2 family、edge、gap 和 acceptance gate 无漂移；
4. 数学证明由独立审阅者逐量词核验；
5. 所有 `PARTIAL` gate 在证据到位后才升级。

本次新增的结构审计属于 F5 的基础设施，不是 F5 的最终数学闭包。

## 5. 依赖图

最小依赖顺序为

\[
\boxed{T1v1--T5v1}
\longrightarrow
\boxed{F1}
\longrightarrow
\boxed{F2\ \&\ F3}
\longrightarrow
\boxed{F4}
\longrightarrow
\boxed{F5}
\longrightarrow
T6.
\]

F2 和 F3 可以并行研究，但 F1 必须尽早冻结 constructor grammar；否则新 macro 可能不断
制造新的 family，令“剩余问题列表”失去完备性。F4 不能在 F2/F3 之前由 T5 自动得到。

## 6. 当前 acceptance gates

| gate | 状态 |
|---|---|
| pre-T6 contract kernel | ESTABLISHED |
| initial state serializer | ESTABLISHED |
| named surface inventory | ESTABLISHED |
| current graph mark invariant | ESTABLISHED |
| constructor admission firewall | ESTABLISHED |
| \(m=3,q=5\) arithmetic dispatch | ESTABLISHED_ARITHMETIC_ONLY |
| reachable-state exhaustion | OPEN |
| all nonterminal leaves closed | OPEN |
| proper-root physicalization | OPEN |
| deterministic computable selector | OPEN |
| edge E1--E5 coverage | PARTIAL |
| terminal certificate lifts | PARTIAL |
| T5 strong-induction termination | PARTIAL |
| no open/finite-only lemma in closure | OPEN |
| repository artifact consistency | PARTIAL until complete-checkout CI |
| independent closure audit | OPEN |

## 7. 可重放命令

```bash
python reproductions/pre_t6_contract_kernel_audit.py --root .
python reproductions/pre_t6_contract_kernel_audit.py \
  --family proper_root_stutter_k_gt_one
python -m unittest tests.test_pre_t6_contract_kernel_audit -v
```

完整仓库 CI 使用：

```bash
python scripts/kb.py validate
python reproductions/pre_t6_contract_kernel_audit.py --root . --require-full-tree
python -m unittest tests.test_pre_t6_contract_kernel_audit -v
```

## 8. 严格的最终边界

截至本文，能够安全作为后续研究前提的是：

- T1v1--T5v1 的 scoped kernel；
- 初始 root serializer；
- 冻结 transition surface 和 current-mark invariant；
- future constructor admission firewall；
- \(m=3,q=5\) 子分支到 \(p^2\) gate 的 arithmetic reduction。

不能作为前提的是：

- semantic reachable-state exhaustion；
- H4/c=8/post-G/overflow/high-support/atomic family 的全域 totality；
- QC1/TR1 的 actual-carrier physicalization；
- \(L_\omega\equiv1\pmod{p^2}\) 的空性或 paid exit；
- total selector、F0 或猜想本身。

因此当前最短的真实证明边界是

\[
\boxed{
F1\; +\; F2\; +\; F3\; +\; F4\; +\; F5
}
\]

而不是“只剩一个 \(p^2\) 同余命题”。
