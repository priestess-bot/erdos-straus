---
kind: claim
claim_id: type-I-high-anchor-cofactor-terminal-guarded-adapter
title: 高锚点 cofactor 宏的 terminal-first guarded adapter 合同
statement: 对已满足 E1--E5 的高锚点宏 H=>T，只有在可重放的优先级前缀回执证明 H 与非持久 transient S 都未产生任何优先于该宏的 terminal 或 alternate 输出，并且调度器保证 T 在任何继续展开前重新经过同一优先级前缀时，才可将该宏登记为 recursive verified_edge。现有独立 macro replay 只证明算术、来源、提升和势；它没有这种 dispatcher 回执，故保持 analysis_evidence 是必要的，而不是 E1--E5 的缺口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-anchor-cofactor-macro-e1-e4-admission
  - type-I-high-anchor-cofactor-outer-rank-composition
  - type-I-high-anchor-direct-c1-finite-menu-exhaustion
  - type-I-unified-terminal-first-selector-contract
topics:
  - type-I
  - high-carrier
  - macro-edge
  - terminal-first
  - selector
  - dispatcher
  - proof-contract
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_anchor_cofactor_macro_replay.py
    role: independently verified H-to-S-to-T E1--E5 macro receipts
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: current priority list and status boundary, but not a state dispatcher
visibility: public
last_checked: '2026-08-06'
---

# 高锚点 cofactor 宏的 terminal-first guarded adapter 合同

## 1. 结论与对象

设已由

\[
P\longrightarrow H\Longrightarrow S\longrightarrow T
\tag{1}
\]

重放出的 high-anchor cofactor 宏已经通过 E1--E5。这里 \(H\) 与 \(T\) 是持久状态，
而 \(S\) 是 bundle 内部的 transient overflow；递归候选是 \(H\Longrightarrow T\)，
不是 \(S\to T\)。

E1--E5 仅断言该宏若被选择，则其来源、算术、连续性、解提升和良基下降正确。它不回答
调度问题：在选择此宏之前，是否有更高优先级的 terminal 或 alternate 输出。因而下列
`terminal_first_guarded_high_anchor_cofactor_v1` 是把候选宏提升为递归边的最小额外合同。

## 2. 最小 guarded receipt

记当前状态调度器在宏之前的全部输出分支为有限有序前缀

\[
\mathcal P=(\mathcal P_1,\ldots,\mathcal P_m),
\tag{2}
\]

其中每一项是一个具名、版本固定的 terminal 或 alternate verifier。它不是“所有未来可能的
证书”的空泛断言，而是当前 selector normal form 中明确优先于该宏的分支清单。

对 (1)，注册回执至少须包含：

```text
certificate_type = terminal_first_guarded_high_anchor_cofactor_v1
macro_receipt_digest = hash(verified H=>T macro receipt)
edge_id = hash(H, T)
selector_normal_form = versioned state dispatcher
priority_prefix = ordered verifier identifiers and versions
priority_prefix_digest = hash(priority_prefix)
source_guard = replay(P, H, priority_prefix) = no_preempting_output
transient_guard = replay(P, S, priority_prefix) = no_preempting_output
target_entry_policy = dispatch_before_expand
scope = source-tree scope propagated from P through H,S,T
```

`source_guard` 与 `transient_guard` 必须逐项保存输入 state ID、输出（或显式
`no_output`）、verifier digest 和总 hash。若某一项输出 terminal，adapter 返回该叶；若
输出优先 alternate edge，adapter 返回该边；两者都不能继续生成宏边。这里的 `no_output`
只相对于 (2)，而非对未经形式化的全宇宙搜索宣称不存在证书。

对 \(T\)，最小合同不要求在 \(H\) 的调用中预先再跑一次全部菜单。它要求工作表入口不变式：

\[
\boxed{\text{任何 persistent state 在产生出边前，必先运行 }\mathcal P.}
\tag{3}
\]

因此宏边只把 \(T\) 入队为 `pending_dispatch`；它绝不能在入队时立即继续展开。若实现选择
eager 检查 \(T\)，同一条规则可由 `target_guard=no_preempting_output` 代替 (3)，但那不是
递归注册的必要字段。

此外，宏回执的 E1--E5、typed \(T\to H\) 解提升、parent/bundle/cofactor 全内容摘要仍须
保持不变。若包含 \(h=0,c=1\) checkpoint，则还必须把冻结 action-menu digest 和耗尽位
写入 guarded receipt；现行严格 \(\Lambda_p\) macro verifier 直接拒绝这类未付款 action，
所以 v1 不可静默放宽该限制。

## 3. 兼容性定理

**定理。** 设宏回执已验证 E1--E5，guarded receipt 满足第 2 节，并且状态机满足 (3)。
则将 \(H\Longrightarrow T\) 登记为 `verified_edge` 不会绕过任何优先于该宏的 terminal
或 alternate 分支。

**证明。** 对 \(H\)，`source_guard` 重放 (2)。若有首个输出，adapter 按顺序返回它；只有
所有项都为 `no_output` 时才选择宏。对 transient \(S\) 同理，故 bundle 内部不能藏入一个
被跳过的高优先级输出。宏的 E1--E5 再给出所选边的合法性。\(T\) 只是 `pending_dispatch`；
由 (3)，其第一次出边之前必重放 (2)，故任何在 \(T\) 可见的优先输出先于进一步递归。
因此整个执行与 terminal/alternate 优先级兼容。证毕。

## 4. 缺字段的严格边界

该合同也给出一个必要性意义上的 no-go。若删除以下任一项：

- `source_guard`：可向 \(\mathcal P\) 加入只在 \(H\) 命中的 terminal verifier；宏的
  E1--E5 与所有算术 hash 均不变，却会跳过 terminal。
- `transient_guard`：同样可加入只在 \(S\) 命中的 terminal 或 alternate；由于 \(S\) 不入队，
  它不会被后续 scheduler 自动补查。
- `target_entry_policy` 或 eager `target_guard`：可令 \(T\) 命中一个高优先级输出，再由
  直接递归展开绕过它。
- `priority_prefix_digest`：改变分支顺序、verifier 版本或新增优先分支后，旧的
  `no_output` 仍会被误复用。

所以“`terminal_first` 字符串”或一个控制例中恰好存在 terminal leaf 都不能代替 guarded
receipt。它们既不编码菜单穷尽性，也不绑定顺序和版本。

## 5. 对当前实现的结论

[`type_i_high_anchor_cofactor_macro_replay.py`](../reproductions/type_i_high_anchor_cofactor_macro_replay.py)
已经独立重放 \(p=1201\) 与 \(p=60913\) 的 E1--E5 宏，并有意保持
`selector_status=analysis_evidence`、`recursive_edge_eligible=false`。这是正确边界：它输出
`terminal_first` 控制叶，但没有第 2 节的逐状态、版本绑定的 `source_guard` /
`transient_guard`。

当前 [`type_i_representation_dual_capacity_selector.py`](../reproductions/type_i_representation_dual_capacity_selector.py)
保存 `SELECTOR_ORDER`、静态结果和 `verified_edge` 状态检查，却没有一个输入任意状态并执行
有序 \(\mathcal P\) 的 dispatcher，也没有 `pending_dispatch` 工作表入口。因此不能仅把宏
回放的两个布尔字段改为 true；应先实现本卡的 guarded adapter，再将它插入一个明确的
priority prefix。旧的 direct \(S\to T\) charged-parent registry 保持不变。

这一步会把“宏形状正确”升级为“在已声明的 terminal-first normal form 下可安全调度”，
但不解决全称存在性：仍须证明每个 terminal-first unresolved high anchor 能生成这样的宏、
terminal 或其它已付款分支。
