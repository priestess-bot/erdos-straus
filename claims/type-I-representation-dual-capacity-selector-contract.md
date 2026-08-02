---
kind: claim
claim_id: type-I-representation-dual-capacity-selector-contract
title: 表示—对偶—容量统一选择器的状态级 typed 分派合同
statement: 统一选择器可将目标纤维近邻、广义 2^j 偶前驱、固定层商 Fourier、固定-n/固定-s 支撑增长边、overflow 双对偶 hard-core 负边界与 q 进缺陷账本装配为内容寻址的状态回执，并按 direct、near、dyadic、Fourier、fixed-n、fixed-s、hard-core、capacity 的顺序分派；analysis_evidence 永不自动升级为递归边，只有同时具备 E1--E5、已证明解提升和严格势下降才可标记 verified_edge。当前三类状态回执、hard-core 负边界和容量审计仍是 analysis_evidence，但已有固定-n 与固定-s identity-lift 正边被完整重算为 verified_edge；该合同仍不证明全称选择器存在。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-unified-terminal-first-selector-contract
  - p-plus-four-sqrt-certificate
  - type-I-overflow-qadic-obstruction-transfer
  - type-I-overflow-defect-unit-phase-capacity
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - type-I-overflow-fixed-n-overflow-rank-descent
  - type-I-overflow-fixed-s-dual-outer-rank-descent
  - type-I-overflow-fixed-n-gap-dual-obstruction
  - type-I-overflow-outer-rank-reset
  - type-I-overflow-phase-reset-cycle-boundary
  - type-I-fixed-layer-cyclic-fourier-profile
  - type-I-fixed-layer-fourier-qadic-phase-bridge
  - denominator-escape-state-contract
topics:
- type-I
- selector
- representation
- dual
- capacity
- typed-receipt
- state-id
- q-adic
- proof-boundary
- proof-program
sources:
  - claim: type-I-unified-terminal-first-selector-contract
    role: terminal-first-arithmetic-and-Fourier-branches
  - claim: type-I-overflow-qadic-obstruction-transfer
    role: local-overflow-ledger
  - claim: type-I-overflow-defect-unit-phase-capacity
    role: conditional-cross-state-capacity-boundary
  - claim: denominator-escape-state-contract
    role: E1-E5-state-and-edge-contract
visibility: public
last_checked: '2026-08-03'
---

# 表示—对偶—容量统一选择器的状态级 typed 分派合同

## 1. 目的与边界

路线图要求把状态内与 overflow 证据放进同一个可检索对象：目标纤维的表示/近邻、固定层商的
对偶证书、固定-\(n\) 因子间隙/双对偶阻碍，以及 overflow 的 \(q\)-进容量账本。本卡给出
这个对象的最小分派合同。它是证据编排规范，不声称任意
\(p\equiv1\pmod {24}\) 都会命中某一分支。

选择顺序固定为

```text
direct_type_i_or_type_ii
target_fiber_neighbor_terminal
generalized_dyadic_terminal
fixed_layer_quotient_fourier
overflow_fixed_n_charged_support
overflow_fixed_n_outer_rank_reset
overflow_fixed_s_outer_rank_reset
overflow_outer_rank_reset
overflow_hard_core_gap_obstruction
overflow_qadic_phase_capacity
```

同一个状态只选择最先可验证的分支；后续证据仍可作为 `capacity_receipts` 附加保存，
但不能覆盖已选分支的证明边界。

## 2. 状态回执

每个状态回执至少携带：

| 字段 | 语义 |
|---|---|
| `state_id` | 对规范化方程、模数、\(K\) 和证书类型的 JSON 内容寻址哈希 |
| `equation_target` | 当前 Type I 根方程 \(4/p\)；跨状态族账本可使用关系式对象 |
| `modulus_context` | \(R\)、`4K=pR+1` 及 Type I 正规形 |
| `K_context` | \(K\) 与精确素因子赋值 |
| `target_fiber` | `nonempty`、`nonempty_source_profile` 或带分离角色的 `empty` |
| `marked_solution_set` | 明确说明非空、为空或尚未携带；不把较小偶数的标准解伪装成根解 |
| `signed_defect` | 全局带向缺陷；未构造时显式标记 `not_carried`，G 空纤维标记 `not_applicable` |
| `certificate_context` | 表示、对偶或容量证书的来源、阶段和证明边界 |
| `normal_form` | 当前 Type I/II 或终端优先正规形 |
| `potential_record` | 若没有良基势和重算值，显式标记 `absent` |

`state_id` 不依赖回执枚举顺序。输入结果文件的 SHA-256 也必须保留，使回执可以在
知识库中重放。

## 3. 状态类型与升级不变量

分派状态使用以下四级标签：

```text
terminal_leaf
analysis_evidence
candidate_transition
verified_edge
```

当前近邻和广义 \(2^j\) 回执验证的是较小偶前驱的整除、同余和范围；固定层 Fourier
回执验证的是稳定子商、精确谱范数和角色阶债务；固定-\(n\) 回执则重算一个保持
`Sol(p)` 的恒等提升和 absorbed-support 势下降；hard-core 回执精确记录固定-\(n\) 因子
间隙与双对偶未支付 \(q\)-幂；overflow 容量回执验证的是逐素数幂支付、缺陷单位相位分胞
及条件性容量统计。前三类证据、hard-core 负边界和容量审计统一标为
`selector_status=analysis_evidence`、`recursive_edge_eligible=false`；固定-\(n\) 正例可在
E1--E5 完整时标为 `verified_edge`。

升级不变量为：

1. `terminal_leaf` 只能来自已经闭合的直接 Type I/II 证书；标准偶前驱不是该类型；
2. `candidate_transition` 必须给出明确后继和缺失的 E 项，不能只凭较小 \(n\) 或较小
   carrier-size 登记递归；
3. `verified_edge` 必须同时满足 E1--E5、全域解提升和严格势下降，并且
   `recursive_edge_eligible=true`；
4. 任何 `analysis_evidence` 都不得具有递归资格；
5. 缺陷单位只有在实际 alternate/source-switch 证明其同余映射后，才可进入跨状态相位
   容量；原始 \(O_d,O_r\) 不自动是共享相位。
6. `overflow_hard_core_gap_obstruction` 只是否定当前固定-\(n\)/双对偶菜单；它不能
   被解释为无后继、标记纤维为空或猜想反例。

## 4. 当前聚焦回执

统一验证器为

```bash
python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
```

当前输出包含三条状态记录：

| 分支 | 状态数 | 结果 |
|---|---:|---|
| 目标纤维近邻 | 1 | `analysis_evidence`，非空近邻见证，偶前驱提升未证 |
| 广义 \(2^j\) | 1 | `analysis_evidence`，来源为命中状态档案，偶前驱提升未证 |
| 固定层商 Fourier | 1 | `analysis_evidence`，空纤维分离角色，载体映射未证 |

固定层回执另外携带 `generic_spectrum_profile`：在循环商 (C_m) 上保存商表示计数向量、
整数群环自相关、Parseval 非平凡能量和逐角色相位签名。选择器用原始 `H`、`J` 和残余
素数幂块重新生成该 profile 并逐字段比对；profile 缺失或过期时拒绝状态回执。该字段
只加强状态内 Fourier 证据，仍不改变 `carrier_mapping_status=unproved`、
`selector_status=analysis_evidence` 或 `recursive_edge_eligible=false`。

对冻结的 overflow fixture，直接分支另行重建 \(p+4\) 的 Type II 证书。12 条全部为
`terminal_leaf`；唯一 \(d=1\) 的 `accumulated_d_one_boundary` 取
\(q=7\)、\(x=20\)，分母为 \((20,219,4380)\)。因此直接证书在选择顺序上优先于
fixed-\(n\)、fixed-\(s\) 和 RESET；后续递降回执仍作为同一状态的可检索替代证据保存。

另外有一条可完整重算的固定-n 支撑增长边：

| 分支 | 源/后继 | 结果 |
|---|---|---|
| overflow fixed-n | \((p,M,A)=(409,250,5)\to L=125\) | `verified_edge`，\(8323\to332\) 的支撑势严格下降，解提升为恒等映射 |

固定-\(n\) 分支还检查窗口上方的正 overflow 图表：12 个 fixture 中 9 条通过完整
E1--E5，其中 3 条落入 \(R_L<p\) 吸收态，6 条落入 \(R_L>p\) 的严格支撑秩递降。
这 6 条不是直接终端，但可以继续进入 overflow 选择器。详见
[固定 \(n\) 窗口上方的 overflow 支撑秩递降](type-I-overflow-fixed-n-overflow-rank-descent.md)。

对称的 r 侧恒等式 \(M=kp+r\) 给出 \(ps=4rd+1\)。选择
\(L=\operatorname{lcm}(A,r)\) 且 \(L\mid rd\) 时，固定-\(s\) 图谱又产生 7 条完整
E1--E5 外层秩边，其中 5 条与 d 侧重叠、2 条补上此前拒绝的 fixture。详见
[overflow 对偶固定 \(s\) 图谱与 \(r\) 侧外层秩递降](type-I-overflow-fixed-s-dual-outer-rank-descent.md)。

同一选择器还输出 12 个 overflow fixture 的菜单分类：

| 分类 | 数量 | 证明边界 |
|---|---:|---|
| `fixed_n_window_nonempty` | 3 | 固定-\(n\) 因子窗口非空，仍需逐边重算才可升级 |
| `dual_support_preserving` | 0 | 固定-\(n\) 为空后才计入；3 个正通道均已被前一分支覆盖 |
| `hard_core_fixed_n_gap_and_dual_obstruction` | 9 | 固定-\(n\) 因子间隙与两个局部支撑阻碍，纯负边界 |

q-adic 双通道共保存 3 个 `support_preserving_edge`；选择器的优先级分类将它们归入
固定-\(n\) 非空的 3 行。hard-core 回执保存 \(S/A\) 的因子分解、窗口两侧最近因子和两个通道的逐素数幂
deficit；全部保持 `analysis_evidence`、`recursive_edge_eligible=false`。独立主张卡见
[overflow 固定-n 因子间隙与双对偶支撑阻碍的 typed 负边界](type-I-overflow-fixed-n-gap-dual-obstruction.md)。

另有一条 RESET 阶段边界回执：局部 \(t<M\) 与恒等解提升成立，但
\(38\to132\to330\to132\) 的 continuation 形成重入循环。因此该记录是
`candidate_transition`、\(E5=false\)，不可递归；它验证的是 phase 调度边界，而不是
一个新的下降边。详见
[overflow RESET 局部载体下降与重入循环边界](type-I-overflow-phase-reset-cycle-boundary.md)。

RESET 现又增加一条带不可重置外层秩的 typed 分支：先取
\(A'=\operatorname{lcm}(A,t)\)，再要求 \(A'\mid K_t\) 和
\(\Pi_A(A')<\Pi_A(A)\)。聚焦 24 个双通道中 8 条满足完整 E1--E5，其中 3 条到达
\(R_t<p\) 吸收态、5 条仍为 overflow 但支撑秩严格下降；16 条继续保留为
`analysis_evidence`。详见
[overflow RESET 的 joined-support 外层秩递降](type-I-overflow-outer-rank-reset.md)。

另附一条跨状态 overflow 容量回执。它重放 12 个 overflow、24 个双通道和 17 条
阻碍幂记录；相位审计得到 5 个 \(q\) 组、13 个相位胞、5 对兼容记录，容量超载胞为
0。该结果只是负边界：当前没有从缺陷单位得到容量矛盾，也没有生成递归边。

固定-\(n\)/固定-\(s\) 正例只证明这些分支在满足各自整除条件的完整 receipt 上可升级；
它不改变已有事实：一般 \(A>1\) overflow 可能同时失去固定-\(n\) 与固定-\(s\) 的合法
外层秩候选，仍需 alternate、终端或容量证书。

结果文件为
`reproductions/type-i-representation-dual-capacity-selector-results.json`。

## 5. 未闭合的全称缺口

该合同解决的是证据编排和类型安全，不解决以下命题：

- 每个核心素数的 terminal-first 失败状态必有 alternate、终端或合法后继；
- Fourier 角色阶或缺陷单位必能映射为有界、可重复控制的 \(q\)-进载体；
- 丢弃旧 charged support 的 phase reset 具有全局良基秩；
- 某个候选后继对全部标记解都给出 E4 提升并满足 E5。

因此下一步仍应集中证明可达 \(A>1\) overflow 的 support-preserving alternate/终端
完备性，或建立封闭且良基的外层 phase-reset 秩；本卡不把有限回执误写成这些全称结论。
