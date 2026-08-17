# T5 Global-Well-Foundedness：完整版收口报告

## 结论

T5 不再使用“registered-edge allowlist closed”作为最终状态。完整版状态定义为：

```text
T5_GLOBAL_WELL_FOUNDEDNESS
    = CONTRACT_LEVEL_WELL_FOUNDEDNESS_CLOSED
```

数学含义是：**状态合同中任何拟创建 persistent successor 的 candidate，都必须在创建时携带同一个
canonical T5 rank receipt；否则它根本没有 recursive-edge 资格。** 因而 T5 对当前或未来的算术
candidate 都不再需要逐个发明独立势函数。

T5 与 T6 的分界也随之固定：

- T5：一个 candidate 在完成 E1--E4 后，是否携带既定 ticket，因而能合法进入一个无无限下降/无环的 recursive graph？
- T6：对每个 actual reachable nonterminal state，是否**存在** terminal 或至少一条这样的合法 edge？

T6 的失败不会迫使修改 T5；它只会产生一个 dead-end/selector-totality gap。

## 1. 为什么上一版 T5-v1 不够

旧 v1 证明的是一个人工冻结 edge allowlist 上的共同 \(\mathbb N^5\) rank。它仍留下两个架构问题：

1. 新的 E1--E4 edge family 是否要重新纳入 allowlist；
2. PRE/ABSORB/legacy RESET 等已经知道会出现代数二环或 carrier re-entry 的机制没有进入同一个
   完整 phase contract。

完整版 T5 同时解决这两个问题：递归资格不再来自 edge 名单，而来自通用 admission rule；
phase/reset 的不可回返规则成为 state schema 的一部分。

## 2. 全局 phase tree

同一 induction rank \(\rho\) 下，major phase 只能向下：

```text
TYPEII_REL (4)
    |
    | target reclassifies G / handoff boundary
    v
TYPEII_G_HANDOFF (3)
    |
    | any named E1--E4 handoff
    v
TYPEI (2)
```

不属于这些 root-equation phase 的 smaller/generic marked state 使用 `GENERIC_MARKED (1)`；它在 v2
只允许继续降低 \(\rho\)，不能在同一 \(\rho\) 下自行发明 local recursion。

Type-I 内部再固定：

```text
CHARGED (4) -> PRE (3) -> ABSORB (2)
       \-----------------> RESET (1)
```

箭头表示允许的 phase/protocol 提交方向，不表示这些边必然存在。每条实际边仍需 E1--E4。

关键规则：

- ABSORB 不得返回 PRE/CHARGED；
- RESET 不得在同一 \(\rho\) 下返回 CHARGED/PRE/ABSORB；
- 安全的 joined-support overflow reset 不进入 RESET，而是在 CHARGED 内用 support rank 真下降支付；
- 更小 \(\rho\) 是唯一可以无条件重置整个 phase tree 的外层事件。

## 3. 规范势

定义

\[
\Pi_{T5}(S)
=(\rho,\Phi,\Psi,r_1,r_2,r_3,r_4)\in\mathbb N^7
\]

按字典序。

### TYPEII_REL

\[
(\Phi,\Psi;r_1,r_2,r_3,r_4)=(4,0;q,0,0,0).
\]

F->F proper endpoint/gcd-shadow 用 \(q'<q\) 支付。若 target 重算为 G，则直接 major phase 4->3。
因此 positive-q G 本身不再是 T5 边界；它可以成为合法 G state，只是当前可能没有 T6 handoff。

### TYPEII_G_HANDOFF

\[
(3,0;0,0,0,0).
\]

任何 future G->Type-I handoff，只要 E1--E4 真正成立，就自动由 3->2 支付 E5。现有 q=1
full-carrier root 和 c=3 conditional source-lineage relay 是实例；T5 不再写死 `q=1` 才允许 phase
下降。

### TYPEI / CHARGED

令

\[
B_p=(p-1)^2/4,
\quad
J=\lfloor B_p/A\rfloor,
\quad
C=K/A.
\]

若 state 带 \(E>1\) 的具名 immediate d=1 regeneration token，令 \(\eta=\nu_p(E-1)\)，否则 \(\eta=0\)。

\[
(2,4;J,C,\eta,0).
\]

这一个 local rank 统一现有全部 persistent Type-I 主干：

- marked support accumulation；
- same-chart support promotion；
- joined-support overflow outer reset；
- A=1 dual reset；
- fixed-n bounded divisor / high-carrier R descent；
- high-support rank-aware sink bundle；
- q=1 d=1 relay 与 one-time regeneration；
- three-anchor / fourth-anchor / H4 persistent macros；
- T2 H4/c=8 atomic strict outputs。

### PRE

\[
(2,3;a,0,0,0).
\]

只允许降 \(a\)，或一次性提交到更低 protocol。

### ABSORB

\[
(2,2;R,m,r_\varepsilon,0).
\]

只允许降 \(R\)，或固定 \(R\) 后降 \(m\)/固定方向 \(r_\varepsilon\)。formal cursor 尚缺 E1--E4 时
仍不是 edge；但以后补完 E1--E4 不需要重新设计 T5。

### RESET

\[
(2,1;M,0,0,0).
\]

legacy support-losing reset 一旦进入此 phase，只允许 \(M\) 严降，或者 terminal/outer-rank drop；
不允许 same-\(\rho\) re-entry。

## 4. 三种且仅三种 recursive admission ticket

任一 candidate 完成 E1--E4 后，只有携带下列 ticket 之一才可入队：

### Ticket A — OUTER_RANK_DROP

\[
\rho(T)<\rho(S).
\]

目标的 phase、support、chart、local rank 全部可重置。

### Ticket B — PHASE_DROP

\[
\rho(T)=\rho(S),
\qquad
(\Phi(T),\Psi(T))<(\Phi(S),\Psi(S)).
\]

目标 local fields 可重置。

### Ticket C — LOCAL_DROP

\[
\rho,\Phi,\Psi\text{ 全部相同},
\qquad
L(T)<L(S)
\]

其中 \(L\) 是该 phase 唯一的 canonical local evaluator。

不存在第四种 ticket。尤其禁止：

- “虽然 rank 不降，但这个图在有限范围里看起来没有环”；
- “先入队，之后再找一个 reset”；
- “这个 chart 更小所以应该可以”；
- “内部 checkpoint 最后会下降，所以先把 checkpoint 当 edge”；
- “换一个局部 rank 排序就行”。

## 5. 历史已知回环在完整版 T5 中的处理

### 5.1 PRE / algebraic inverse 二环

已有控制

\[
X=(2,1,35)\to Y=(1,1,71)\to X
\]

证明裸 chart 不可能同时给两边严格势。完整版 T5 允许 PRE 内向前降 \(a\)，允许 PRE->ABSORB，
但禁止 ABSORB->PRE，因此第二步若想成为 inverse re-entry 会被 phase admission 拒绝。

### 5.2 terminal-free formal self-loop

\(p=1009,R=3\) 的 \(\{1,2\}\to\{1,2\}\) 说明 ABSORB 不能保留全部 m=1 formal edge。
T5 只允许固定 \(\varepsilon\) 后严格降低 \(r_\varepsilon\) 的边；self-loop 没有 LOCAL_DROP ticket。

### 5.3 legacy carrier reset re-entry cycle

状态合同记录的 carrier path

```text
38 -> 12 -> 132 -> 330 -> 132
```

说明单独以 carrier size 作“全局 rank”失败。完整版 T5 的处理不是再加一个经验补丁：

- support-preserving、joined-support paid reset 保持 CHARGED，用 \(J\) 真下降；
- support-losing legacy reset 进入 RESET protocol；
- RESET same-\(\rho\) 不得回 CHARGED，也不得在 RESET 内增大 \(M\)。

所以 12->132 这一 re-entry 在 admission 层已经非法，历史 cycle 不可能进入 recursive graph。

## 6. 当前 transition surface 穷尽审计

状态合同声明 selector 只有五种输出：

| 输出 | 是否创建 persistent successor | T5 处理 |
|---|---|---|
| Type I hit | 否 | terminal |
| Type II hit | 否 | terminal |
| support_switch | 有条件 | 必须持有 A/B/C 三种 ticket 之一 |
| q_adic_lift | 有条件 | necessary condition 不是 edge；完整 E1--E4 后仍须 ticket |
| generalized_dyadic_terminal | 通常否 | 若已恢复解则 terminal；若建较小 marked source 则 OUTER_RANK_DROP |

root terminal 只是 Type I/II/direct-root receipt 的结果标签，不是新的 edge type。

此外，下列状态合同对象明确没有 recursive eligibility：fixed-layer Fourier、phase-cell capacity、natural-tail
relation graph 的 \(\kappa\) 迁移、unlifted dyadic candidate、formal cursor before E1--E4、pending
normalization、raw macro checkpoints、standalone stutter、control-only fixture。

因此当前合同的 persistent successor surface 被三种 ticket 穷尽。

## 7. T2 的最终接入

T2 的 H4 actual arm 与 c=8 conditional arm 不再只拥有“局部 strict”标签。只要 actual receipt 通过 T2
source/owner/typed admission：

- 若 support growth 使 \(J\) 降，则走 CHARGED LOCAL_DROP；
- 若已在 \(J=0\) 高支撑层，则由 \(C=K/A\) 从 \(p-1\) 降到 \(\le p-2\)（c=8 为 \(\le7\)）支付；
- standalone stutter 仍没有 ticket。

所以 T2 与 T5 的接口已经固定；它不证明其它 atomic arm、或 c=8 的 double-low 前提，必然产生可入队回执。

## 8. “完整版 T5”之后剩下什么

以下问题仍然存在，但全部是 T6/算术 existence，不是 T5：

- 某个 positive-q G state 是否存在 handoff；
- post-atomic F/G state 是否总有 registered candidate；
- c=8 double-low 是否实际存在；
- high-support sink 改善集合是否总非空；
- marked terminal membership 是否能证明；
- 某个 q-adic/Fourier obstruction 能否真正构造 E1--E4 edge。

这些问题可以让 selector 没有 outgoing edge，但不能再制造 T5 的无限递归或需要修改 T5 势。

## 9. 最终状态

建议仓库把 T5 的旗舰状态写成：

```text
T5_GLOBAL_WELL_FOUNDEDNESS
    = CONTRACT_LEVEL_WELL_FOUNDEDNESS_CLOSED
```

并废弃旧的：

```text
REGISTERED_EDGE_SCHEDULE_CLOSED
```

作为最终表述。后者只保留为历史 v1 milestone。
