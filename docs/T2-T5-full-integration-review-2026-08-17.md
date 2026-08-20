# T2 + T5 FULL 合并复核（2026-08-17）

## 2026-08-20 版本化处置

本文件的原始复核结论保持不变，但命题编号不再混用：

- `T2v1 = CLOSED_PHASE_LOCAL`：只指 H4 `a=1` actual arm 与 conditional c=8
  double-low arm 的有限 receipt grammar；
- `T2*`：所有 actual raw path、所有 c=8 parent 及 future atomic surface 的强版本，仍未
  证明，但其未覆盖状态由 T6-F1/F2 管理，不再称作“尚未修完的 pre-T6 内核”；
- `T5v1 = CLOSED_CONTRACT_LEVEL`：只指合同认可的 `verified_edge` 沿固定
  \(\mathbb N^7\) 势严格下降；
- `T6_GLOBAL_SELECTOR_TOTALITY = OPEN`。

任何 future atomic constructor 必须先通过 constructor admission firewall；不允许先进入
递归图再以后补 T2/T3、serializer、lift 或 T6 owner。机器边界见
`data/pre-t6-contract-kernel-v1.json` 和 `data/t6-proof-frontier-v2.json`。

## 审查对象

复核包为 [`../archive/proof-packages/raw/erdos_straus_T2_T5_FULL_2026-08-17.zip`](../archive/proof-packages/raw/erdos_straus_T2_T5_FULL_2026-08-17.zip)，SHA-256 为
`abce823e05ff38c7fca13162d76bfd45ede0ec722ebb9dfac775c52d941aad40`。
包内 SHA-256 manifest、focused verifiers 和 bundle validation 均通过。合并前，包内
`denominator-escape-state-contract` 快照与仓库基线逐字一致；合同第 4 节确实把 selector
输出限制为 Type I hit、Type II hit、support switch、q-adic lift 和 generalized dyadic
terminal 五类，并要求每条 recursive edge 通过 E1--E5。

本复核采用的是合同与证明边界审查，不把 package 内 JSON 自己列出五类输出的事实，误作对所有
尚未定义算术构造的外部穷尽定理。

## 接纳结论

### T2 v1

`T2_ATOMIC_ADMISSION_V1 = PHASE_LOCAL_GRAMMAR_CLOSED` 可以接纳，严格范围是

\[
\mathcal A_{\mathrm{v1}}=\mathcal A_{H4}\sqcup\mathcal A_{C8}.
\]

- H4 `a=1` arm 是带 actual parent/source/path 的局部闭合 arm。
- c=8 arm 以 actual double-low 为前提；它没有证明该前提总会发生。
- owner-local 结论只适用于固定优先级后至多消费一个 action 的单边证明，不能扩展到
  Fourier、Hall 或 flow 的 pooled-capacity 论证。
- standalone stutter、bare chart、target-derived source 和 control-only fixture 均不获得
  persistent-edge 资格。

因此 v1 关闭的是有限 receipt grammar，不是原始“每个 actual raw legal path”量词下的完整 T2。

### T5

`T5_GLOBAL_WELL_FOUNDEDNESS = CONTRACT_LEVEL_WELL_FOUNDEDNESS_CLOSED` 可以接纳，含义严格为：

\[
\text{verified\_edge}(S,T)\Longrightarrow \Pi_{T5}(T)<\Pi_{T5}(S),
\qquad
\Pi_{T5}\in\mathbb N^7.
\]

其中 E5 的唯一 admission tickets 是 `OUTER_RANK_DROP`、`PHASE_DROP` 和 `LOCAL_DROP`。在这些
规则下，字典序 \(\mathbb N^7\) 良基；PRE/ABSORB 二环、formal self-loop 与 legacy RESET
re-entry 都不能同时被录入合同认可的递归图。当前 state contract 的五类 selector 输出也都已被
映射到 terminal、outer-rank drop 或三种 ticket 之一。

## 必须保留的边界

以下更强说法没有被本次合并接受：

1. E1--E4 已完成的任意算术 candidate 会自动得到 T5 ticket。
2. 当前五类合同输出穷尽所有未来可能发明的数学构造。
3. 每个 actual reachable nonterminal state 已有 terminal 或 admitted successor。
4. T2 v1 已覆盖所有 atomic arm，或 c=8 double-low 对所有 endpoint 成立。

第 1 项由 E5 admission rule 处理，而不是由算术定理自动推出；第 3 项正是 T6 global-selector
totality。故 T5 的闭合不会把 Erdős--Straus 猜想或 T6 标为已解决。

## 合并时的修正

- T5 的 claim、concept 和 integration text 已明确其为合同准入规则，避免把定义性排除混写成
  对所有 E1--E4 candidate 的存在性定理。
- T2 focused verifier 现检查文档承诺的 adapter version、source/target chart、maximal payload、
  target rechart digest 和 local E5 classification。
- T5 evaluator 现拒绝负的 local rank，并把 regeneration token 限定为 \(E>1\)，确保
  \(\nu_p(E-1)\) 有定义且运行时 rank 的值域确为 \(\mathbb N^7\)。
- transition-surface verifier 现直接检查当前 state contract 的五个输出节、E1--E5 gate、T5
  section，以及每个 taxonomy reference 是否解析为真实 claim 或 concept。

所有新 claim 仍是 `repository_derivation` / `internal_review`；这次复核不把内部可复现性升级为
外部同行确认。

## 当前状态

```text
T1V1_TO_T5V1_PRE_T6_KERNEL          = CLOSED_WITH_EXPLICIT_SCOPE
T2_ATOMIC_ADMISSION_V1              = PHASE_LOCAL_GRAMMAR_CLOSED
T2_STRONG_RESEARCH_EXTENSION        = NOT_A_KERNEL_PREREQUISITE
T5_GLOBAL_WELL_FOUNDEDNESS_V1       = CONTRACT_LEVEL_WELL_FOUNDEDNESS_CLOSED
T6_GLOBAL_SELECTOR_TOTALITY         = OPEN
ERDOS_STRAUS_CONJECTURE             = OPEN
```

验证入口：

```bash
python3 reproductions/type_i_atomic_admission_v1_contract.py
python3 reproductions/type_i_t5_full_global_well_foundedness.py
python3 reproductions/type_i_t5_transition_surface_audit.py
python3 scripts/kb.py validate
python3 scripts/kb.py build
```
