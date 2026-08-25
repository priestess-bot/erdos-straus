# Agent 6 对 F3-QC1 R3/R5 的独立交叉复核

> 复核日期：2026-08-24  
> 被复核 worktree：`/home/ymm/math/wt-f3-qc1`  
> 被复核 HEAD：`358d078755ba5de897f3d1cbef39e25ed4a9ce60`，并包含当时未提交的 QC1 claim、receipt、serializer、tests 与 handoff  
> 复核方法：直接检查代数推导、状态合同与代码控制流；未把被审 verifier 的 PASS 当作独立证明  
> 结论：`REJECT_QC1_CLOSURE_MAJOR_REVISION_REQUIRED`

## 1. 复核结论

Agent 5 正确证明了下列算术事实：

1. 在 R3/R5 的定义域中 (k_\perp>1)，所以规范最小素因子
   
   \[
   q_\perp=\min\{q:q\mid k,\ q\nmid h\}
   \]

   全域存在，tie-break 确定；
2. (q_\perp\equiv1\pmod3)、(q_\perp\ge7)，且由既有范数界有
   (q_\perp<p/4)；
3. 在 Eisenstein 整数中，(q_\perp) 的一个确定定向素理想整除
   (eta=a-b\omega)，并且由于 (q_\perp\nmid h)，该 norm occurrence 留在商
   (k=N(\beta)/h) 中；
4. R3/R5 与 (m=3,5\mid D_*)、(k_\perp=1) 两条邻接域在逻辑上分开。

但这些事实没有建立 `QC1PhysicalTransitionV1`。核心问题不是 target 的模算术，而是从
辅助 Eisenstein norm occurrence 到 Type-I charged support 的来源/消费语义没有证明。
因此以下状态不能接纳：

```text
R3/R5 QC1 MATHEMATICAL TRANSITION = ESTABLISHED
MATHEMATICALLY_CLOSED_PENDING_SHARED_REGISTRATION
```

正确状态应保持：

```text
Q_PERP_ARITHMETIC_AND_ORIENTATION = ESTABLISHED
QC1_INTEGER_SOURCE_OCCURRENCE = OPEN
QC1_PHYSICAL_TRANSITION = OPEN
R3 = OPEN_MINIMAL_RESIDUAL
R5 = OPEN_MINIMAL_RESIDUAL
F3 = OPEN
```

## 2. Critical：ideal occurrence 不能直接收费为 charged support

QC1 claim 从

\[
(q_\perp,\omega-\lambda)\mid a-b\omega
\]

直接推出

\[
\mathcal A_T=\mathcal A q_\perp.
\]

这一步没有已有定理支持。现有 Type-I support accumulation 的物理输入是：从真实 persistent
source 出发的 raw path 到达整数节点 (x+y=R)，相对当前整数 capacity (K) 重算唯一
complete-excess block (Q)，并以

\[
A_T=\operatorname{lcm}(A,Q)
\]

收费。atomic owner theorem 只说明**已有合法 physical occurrence**时，单后继 action
不必再证明跨 action one-use；它不会把任意辅助代数环中的素理想因子变成 raw path block。

特别地，claim 声称即使 (q_\perp\mid\mathcal A) 也可再把 support 乘一个 (q_\perp)。
但当前 support 的 (q)-指数是整数 capacity ledger；要把指数再加一，必须证明一个实际整数
side 的 (q)-赋值严格超过当前 (K)-capacity，或另行建立并获准一个保持守恒的新资源语义。
`v_q(k)>=1` 不比较 `v_q(K)`，定向 ideal 也不是该整数 side occurrence。

因此后续 target

\[
L=\mathcal A q_\perp,\qquad
c=\langle-q_\perp^{-1}\rangle_p,
\qquad K_T=Lc
\]

只是一个合法算术 chart，不是从 source 导出的 successor。E2 的整数正确、E4 的同方程恒等
形式和 E5 的数值比较都不能反向补上 E1。

## 3. Critical：实现允许用一个字符串伪造 actualness

track-local serializer 接受 `evidence_class` 为字符串 `ACTUAL_PERSISTENT`，随后仅检查若干
digest 字段非空。它没有执行：

- (p) 的核心素性验证；
- source `state_id` 的内容重放；
- active producer/admission receipt 验证；
- source mark 与 equation rank 验证；
- source path digest 所指 path 的重放；
- terminal-first digest 的 verifier；
- actual maximal receipt 的重算。

随后 `actual_occurrence_bound` 只等价于该字符串判断，`build_transition` 又据此设置
`E1.complete=true` 与 `recursive_edge_eligible=true`。

负控直接把仓库自带的 composite control

```text
p = 54481 = 7 * 43 * 181
```

的 `evidence_class` 从 `CONTRACT_SHAPE_CONTROL_NOT_ACTUAL` 改成
`ACTUAL_PERSISTENT`，其它字段完全不变。结果仍为：

```text
E1.complete = true
recursive_edge_eligible = true
common admission = ACCEPT
```

这不是 fixture 有限性的轻微问题，而是 serializer 的授权边界可绕过。它不能在修复前登记为
active producer。

## 4. Critical：producer、E1--E5 与 terminal miss 由被审对象自行授权

serializer 内部执行了三次定义性自证：

1. 自建 `ProducerRuleV1`，而不是读取 coordinator 冻结的 active registry；
2. 自建 successor receipt，并直接写入 `E1=...=E5=true`；
3. 用任意 label 自行生成 sealed terminal `MISS` receipt，再将其送入 common gate。

common admission kernel 验证 schema、owner predicate 和调用方传入的 producer rule 是否自洽，
不验证这些数学布尔值的来源。故这一 replay 只能证明“若 producer 与 E1--E5 均被授权，target
schema 能被分类”，不能证明 producer 已授权、terminal priority 已运行或 E1--E5 成立。

residual matrix 将 occurrence-unbound 叶标为 empty，并将 occurrence-bound 叶标为
mathematically closed，正是把上面三项自授权误作了 closure。

## 5. Major：source mark 未进入 envelope，target 被无条件重置为 ROOT_SOL

source dataclass 没有 mark receipt、equation rank 或 source owner receipt。target serializer
却无条件创建 `ROOT_SOL` mark，并把 source owner 固定写成
`proper_root_stutter_k_gt_one`。所以一个 nontrivial marked、错误 equation rank、或只是同形的
arithmetic source 都可能被重写为 ordinary root mark。

在 Agent 5 的 intended R3/R5 domain 中 source 应当是 ordinary root-mark state；但这一前提必须
由实际 source admission receipt 重放，不能只存在于 prose 量词里。否则 E4
(operatorname{id}_{\operatorname{Sol}(p)}) 没有验证 source endpoint。

## 6. Major：target owner 是 schema fallback，不是完整 typed E3

target 通过 common minimal header 后唯一命中
`type_i_a_gt_one_overflow_residual`，这是预期的 fail-closed family routing。但当前 header
只验证 (4K=pR+1)、support 整除和少量 provenance facts；serializer 没有独立重算完整
F/G/hit classification、normal form、source scope、charged ledger 或 target parent lineage。

因此“owner 唯一”只证明候选 facts 的分类结果，不等于完整 E3。必须先修复第 2--5 节的
source/cargo/mark 问题，再由活动 serializer 生成完整 target receipt。

## 7. 对验收项的逐项裁定

| 验收项 | 裁定 |
|---|---|
| (q_\perp) 全域存在 | 通过；来自 (k_\perp>1) 的定义 |
| R3/R5 量词与 q5 排除 | 通过；branch predicates 正确 |
| deterministic tie-break | 通过；取最小素因子 |
| actual occurrence | 不通过；ideal factor 是 source arithmetic occurrence，不是 Type-I raw/capacity occurrence |
| E1 | 不通过；缺整数 path/block 或获准的新资源守恒定理 |
| E2 | 仅算术 target 成立；不构成 source-derived successor |
| E3/re-entry | 不通过；self-injected producer rule 与最小 header 分类不是 active admission |
| E4/mark | 不通过；source mark 未验证，target 无条件 ROOT_SOL |
| E5 | 数值比较成立，但依赖未获准的 support charge，不能单独成票 |
| terminal priority | 不通过；MISS receipt 由 track-local helper 自建 |
| finite/fixture 边界 | 文档承认 nonactual control，但实现可由 flag 将其伪造为 actual |

## 8. 最小修复路线

1. 将当前结论降为 `QC1_EISENSTEIN_OCCURRENCE_CANDIDATE`，恢复 R3/R5 的
   occurrence/physicalization residual。
2. 证明下列二者之一：
   - 从 actual proper-root source path 构造一个整数节点，其 unique complete-excess block
     实际携带 (q_\perp) 的新增赋值，并按 lcm 收费；
   - 定义一个独立于 Type-I raw capacity 的新 resource，并证明 occurrence conservation、
     one-use、target state semantics、全域 lift 与 T5 rank，再提交 grammar/interface request。
3. source 输入必须是 common extractor/admission 的已验证 receipt，而非
   `evidence_class` 字符串；必须重放 source mark、owner、scope、state ID、producer 与 parent。
4. common terminal dispatcher 必须由 coordinator 注入 verifier 输出；track 不能自签 MISS。
5. producer rule 必须来自冻结 registry；candidate serializer 不应把 E1--E5 布尔值写真后再用
   同一 gate 验证自身。
6. 增加真实负控：composite (p) + `ACTUAL_PERSISTENT` flag、伪 admission digest、nontrivial
   source mark、复用 occurrence、(q_\perp\mid A) 但无新增 integer capacity 的场景。

在这些修复完成前，Agent 5 的文件可保留为重要的 algebraic target proposal，但不应把
R3/R5 标为 mathematically closed，也不应注册 active QC1 edge。
