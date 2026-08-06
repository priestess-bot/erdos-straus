---
kind: claim
claim_id: type-I-high-anchor-token-canonical-checkpoint-propagation
title: 高锚点正相位 token 的 canonical checkpoint 传播合同
statement: 条件性地，固定 p、同一 tree epoch 内，若一次正相位的 canonical target checkpoint 具有 spent support A_star，且所有后继 canonical high-anchor checkpoint 都保留 A_star|A_j，则不能再出现正 cofactor 相位：严格整除增长使 A_j>p，保持相等则回到同一 canonical chart。该条件当前覆盖已审计 selector artifact 中 68 条 A_S|A_T 的 verified edge；8 条 support_reset_paid 和所有 forgetful RESET 是 token_exit，而非 token 的免费重置。要把此合同用作全局选择器秩，仍须证明每条递归路径不会经 token_exit 无偿重入。
claim_status: conditional
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-anchor-positive-phase-one-shot-token
  - type-I-high-anchor-direct-cofactor-lexicographic-rank
  - type-I-overflow-same-chart-support-promotion
  - type-I-overflow-outer-rank-reset
  - type-I-overflow-phase-reset-cycle-boundary
  - type-I-representation-dual-capacity-selector-contract
topics:
  - type-I
  - high-carrier
  - r-chart
  - nonreturn
  - state-contract
  - support-monotone
  - reset
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: existing verified-edge and reset-contract artifact
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: read-only token-propagation classification
visibility: public
last_checked: '2026-08-06'
---

# 高锚点正相位 token 的 canonical checkpoint 传播合同

## 1. 条件性传播引理

令一次正 cofactor 相位的 target 是 canonical 高锚点 checkpoint

\[
\operatorname{Ch}_p(A_\ast)=(R_\ast,K_\ast),\qquad A_\ast>p/2.
\tag{1}
\]

最后一个不等式来自正相位的 \(A_\ast=A c\ge2A>p/2\)。固定同一 \(p\) 与
tree epoch，假设所有后继 canonical high-anchor checkpoint 的 support 满足

\[
A_\ast\mid A_j.
\tag{2}
\]

则没有后继 checkpoint 可以再启动正 cofactor 相位。事实上：

\[
\begin{array}{c|c}
A_j>A_\ast & A_j\ge2A_\ast>p,\ \text{与正相位 source barrier }A_j<p\text{ 矛盾}\\
A_j=A_\ast & \operatorname{Ch}_p(A_j)=\operatorname{Ch}_p(A_\ast)
\end{array}
\tag{3}
\]

第二行使用 canonical checkpoint 的唯一性；删去同 checkpoint 的 stutter 后，任何新的
正相位都会成为第一次正相位之后的相邻正相位，违反一次性 token 引理。

这里绝不能把 (3) 错用到任意满足 \(A\mid K\) 的 overflow chart。例如

\[
p=73,\qquad A=1,\qquad (R,K)=(3,55),\ (7,128)
\]

都满足 \(4K=pR+1\) 和 \(A\mid K\)，但只有前者是 \(A=1\) 的 canonical chart。
high-\(R\) bundle 的 transient overflow 也通常是 carrier \(M\) 的 canonical chart，
而非 charged support \(A\) 的 checkpoint。

## 2. Token 状态合同

为使 (1)--(3) 可由 selector 检查，token 必须绑定于 checkpoint，而非松散的
overflow 行。其最小记录为：

    high_nonreturn_token_v2
      core_prime: p
      tree_epoch: immutable root-entry digest
      source_tree_scope: immutable
      anchor_checkpoint: canonical (p, A, R, K)
      status: available | spent
      spent_base_support: null | A_star

这些字段及影响 E1/E3 的 capability digest 必须参与 state identity。否则已消费与
未消费的同图表状态会被错误合并。

迁移规则为：

| 迁移 | token 处理 |
|---|---|
| 正 cofactor 相位 | available 到 spent，并记录 \(A_\ast=A_T\) |
| \(h=0,c=1\) 的完整宏自环 | token_stutter；只在 capability 与 bundle digest 不变时抑制 |
| \(h=0,c>1\)、same-chart promotion、joined RESET 或任何 \(A_S\mid A_T\) 的严格扩张 | token_carry；spent 时保持 \(A_\ast\mid A_T\) |
| \(A_T=A_S\) 而 \(R,K\) 改变 | token_exit，除非另证同一 canonical checkpoint |
| \(A_S\nmid A_T\)、support 下降、scope/epoch 改变、PRE/ABSORB/raw 非 canonical 状态、跨 p | token_exit，绝不自动回到 available |

token_exit 不是失败结论：它表示该分支必须由已有独立 E5、terminal 或新的 epoch-rank
支付，不能靠局部 token 免费重入。

## 3. 当前 artifact 的边界审计

对当前 selector results artifact 的有 source/successor 的 76 条 verified edge 做只读
分类，得到：

| 类别 | 数量 | 合同处理 |
|---|---:|---|
| \(A_S\mid A_T\) 且严格增长 | 68 | token_carry |
| \(A_T=A_S\) 而 \(R,K\) 改变 | 0 | 当前无此已验证例 |
| \(A_T<A_S\) | 0 | 当前无此已验证例 |
| support_reset_paid，\(A_S\nmid A_T\) | 8 | token_exit |

68 条包括 same-chart promotion、lcm 型 fixed-\(n\)/fixed-\(s\) outer-rank 与 joined
RESET。它们的名称即使含 RESET，也实际通过 \(\operatorname{lcm}(A,t)\) 保留旧 charged
support，故满足 (2)。8 条 bounded-divisor fixed-\(n\)/fixed-\(s\)
support_reset_paid 本身仍可有既有 verified E5，但不能把 token 重新铸造成 available。

这些数量只是现有 artifact 的审计，不是对未来 selector 边或全体算术状态的定理。

## 4. 真正的 reentry 边界

forgetful carrier RESET 仍是 token_exit。\(p=73\) 的

\[
132\longrightarrow30\longrightarrow330\longrightarrow12\longrightarrow132
\]

精确展示了丢弃 charged ledger 后的 reset/reanchor 重入；局部 carrier \(t<M\) 不能阻止
该循环。因此任何全局化必须证明：

1. token_exit 进入 terminal 或已有独立严格 rank；
2. 或者为 token_exit 构造不与旧 epoch 混淆的新 epoch-rank；
3. 而不是把它直接重标为 token available。

本卡给出可安全实现的传播界面和明确的未覆盖面，不声称已完成统一 selector 的全局 E5。
