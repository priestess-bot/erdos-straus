# T2 Atomic-Admission v1：最终局部 grammar

## 1. 输入域

冻结

\[
\mathcal A_{\rm v1}=\mathcal A_{H4}\sqcup\mathcal A_{C8}.
\]

`A_H4` 要求真实 persistent q=1 high-C=2 H4 parent、可重放 parent/raw path、版本化
terminal/alternate priority prefix 和 canonical atomic owner。`A_C8` 要求真实 q=1 c=8
persistent parent，并附加 actual double-low 谓词。

Generic `path_anchored_atomic_split_complete_excess_v1` 只提供 payload schema；它不能独立创造
source origin。`s=0` fixed controls、bare chart、target-derived source 和 standalone stutter 均不在
输入域。

## 2. 必须冻结的 receipt

每个输入至少记录：

- `adapter_version`、`arm_id`；
- `source_state_id`、`source_origin_tag`、`source_tree_scope`；
- `parent_receipt_digest`、`raw_path_digest`；
- `candidate_menu_digest`、`priority_prefix_digest`；
- canonical two-color `owner_tuple`；
- source `(p,R,K,A)`；
- maximal complete-excess payload `(Q_x,beta_x,Q_y,beta_y)`；
- canonical target integers；
- target-local rechart digest；
- local E5 classification。

Target F/G/hit 必须从 target integers 重算，不得继承 source 标签。

## 3. 输出

adapter 只能返回：

1. `DIRECT_TERMINAL`；
2. `PENDING_DISPATCH_LOCAL_STRICT`；
3. `BOUNDARY`；
4. `REJECT`。

任何 `c_M=C` standalone stutter 不得成为 persistent successor。

## 4. edge-local ownership

若一个 arm 在固定 priority prefix 后最多消费一个 atomic action，selected occurrence 由
`(arm_version, source_state_id, physical_path_digest)` 唯一标识，且 proof step 不把其它
outgoing action 的容量同时求和，则该 edge 的 E1--E5 不需要跨 action global one-use ledger。

这不能推广到 Fourier/Hall/flow pooled-capacity 证明：两个 action 可以各自合法引用同一个容量
1 的 physical token，而 pooled demand 会把它重复计数。

## 5. H4 与 c=8

H4 parent-anchored macro 已把 actual parent、terminal-first、canonical q-word、maximal split、
target-local rechart、identity lift 与 phase-local strict E5 一并支付，所以是 v1 的
`LIVE_CLOSED_ARM`。

c=8 double-low macro 在实际 endpoint 满足 `1<=c_a,C<=7` 时同样局部闭合；但现有 focused
control 是 non-low，因此 existence/totality 移交算术 selector，而不是继续挂在 T2。

## 6. T2 交付

```text
T2_ATOMIC_ADMISSION_V1 = PHASE_LOCAL_GRAMMAR_CLOSED
```

T2 只回答“一个 actual atomic receipt 出现后能否被安全接纳”；全局 phase 与 well-order 由 T5
消费。
