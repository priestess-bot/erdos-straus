---
kind: concept
concept_id: t5-global-well-foundedness-contract-v2
title: T5 完整全局良基合同：persistent successor 的单一相位序与规范势
summary: 把状态合同中所有被接纳为 persistent successor 的输出统一到一个固定的全局相位注册表和七元自然数词典序势；terminal、analysis evidence、pending normalization 和 macro checkpoint 均不产生递归边。E1--E4 已完成的 candidate 只有在该规范势严格下降时才可标为 verified_edge；该规则不声称任意 candidate 自动得到 ticket，因此 RESET 回返、PRE/ABSORB 二环、standalone stutter 与无付款 phase reset 在合同层被永久排除。
topics:
  - proof-program
  - state-transition
  - well-founded-descent
  - phase
  - reset
  - type-I
  - type-II
  - atomic-split
  - selector
used_by:
  - type-I-t5-full-contract-level-global-well-foundedness
  - type-I-t5-full-transition-surface-exhaustion
sources:
  - concept: denominator-escape-state-contract
    role: E1--E5 base contract and legal-state schema
  - claim: type-I-phase-labeled-candidate-selector-well-founded-schedule
    role: PRE/ABSORB cycle obstruction and phase schedule
  - claim: type-I-marked-support-accumulation-rechart-saturation
    role: absorbed-support rank
  - claim: type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
    role: sharp Type-I rank Lambda-sharp
  - claim: type-II-relation-reach-gcd-shadow-endpoint-descent
    role: Type-II q descent
  - claim: type-II-q-one-full-carrier-phase-root-entry
    role: G-to-Type-I one-way phase entry
  - claim: type-I-atomic-admission-v1-finite-grammar-integration
    role: finite T2 atomic arm interface
visibility: public
last_checked: '2026-08-17'
---
# T5 完整全局良基合同

## 1. T5 的目标量词

T5 只证明递归图的**良基性**，不证明 selector totality。完整 T5 的目标是：

> 本 v2 把一个**预先固定且从状态本身可重算的**全局势写成 E5 admission rule。一个已通过
> E1--E4 的 candidate，只有实际携带该规则的 strict-decrease ticket 后，才可成为 persistent
> successor；未携带者只能是 candidate、analysis evidence、internal checkpoint 或 rejection。

这把 recursive eligibility 的判据固定在合同层，而不依赖手工边名单；它不证明任意 E1--E4
算术构造会自动满足该判据。

## 2. 四种非递归对象

以下对象不参与 T5 的下降链：

1. `terminal_leaf`：Type I/II/root/generalized-dyadic 已在当前 receipt 中恢复结果，没有 successor；
2. `analysis_evidence`：Fourier、商群、q-adic necessary condition、自然尾 relation graph 等尚未支付
   完整 E1--E5；
3. `pending_dispatch` normalization：只重算 target typed data，不改变数学状态，不是 proof edge；
4. macro internal checkpoint：可以局部升秩或 stutter，但不进入 persistent queue，只有
   parent-to-final-target 的组合 macro 接受 E5。

因此 T5 只需要排序真正写入 persistent queue 的 successor states。

## 3. 全局 phase registry

固定 major phase：

\[
\Phi=
\begin{cases}
4,&\mathrm{TYPEII\_REL},\\
3,&\mathrm{TYPEII\_G\_HANDOFF},\\
2,&\mathrm{TYPEI},\\
1,&\mathrm{GENERIC\_MARKED}.
\end{cases}
\]

`GENERIC_MARKED` 用于不属于已定义 Type-I/II phase 的较小 marked equation；v2 不允许它在同一
\(\rho\) 下产生任意自定义 successor。它只能 terminal 或进一步严格降低 equation/induction rank，
直到另有具名 phase adapter 把它纳入上述 phase registry。

对 Type-I 再固定不可回返 protocol：

\[
\Psi=
\begin{cases}
4,&\mathrm{CHARGED},\\
3,&\mathrm{PRE},\\
2,&\mathrm{ABSORB},\\
1,&\mathrm{RESET}.
\end{cases}
\]

允许同一 \(\rho\) 下的 protocol 动作只有：

- CHARGED 内严格 local drop；
- CHARGED -> PRE/ABSORB/RESET 的一次性向下提交（前提是 E1--E4 已独立完成）；
- PRE 内降其 local rank，PRE -> ABSORB；
- ABSORB 内降其 local rank；
- RESET 内降 reset carrier rank；
- **禁止** ABSORB/RESET/PRE 无付款回到更高 protocol。

现有 joined-support overflow RESET 不需要进入 RESET protocol：它保留旧支撑于
\(A'=\operatorname{lcm}(A,t)\) 并严格降低 charged-support rank，因此仍是 CHARGED->CHARGED。
只有会丢弃旧 support、历史上可制造 carrier cycle 的 legacy reset 才进入不可回返 RESET。

## 4. phase-local canonical ranks

固定根素数 \(p_0\)，令

\[
B_{p_0}=\frac{(p_0-1)^2}{4}.
\]

### 4.1 TYPEII_REL

若 source cofactor 为 \(q\)，local rank 为

\[
L_{\rm II}(S)=(q,0,0,0).
\]

proper endpoint 与 gcd-shadow 的 F/hit/G target 均从整数重算。F target 若仍在 Type-II relation
phase，必须满足 \(q'<q\)；G target 直接转入 major phase 3，因此无须在 G phase 继续使用 q 作为
下降量。

### 4.2 TYPEII_G_HANDOFF

local rank 全零。任何合法 G->Type-I handoff 只需要 E1--E4；major phase 3->2 自动支付 E5。
现有 full-carrier q=1 root、actual ordinary positive-q relative adapter 和条件 c=3
source-lineage relay 是这个通用规则的实例。positive-q focused controls 不提供 actual source
receipt，故它们本身不是 edge；一旦 theorem hypothesis 中的 source receipt 已提供，adapter
通过 E1--E4，并由本条 phase ticket 支付 E5。后续 Type-I totality 仍是 T6 gap，不是 T5 gap。

### 4.3 TYPEI / CHARGED

每个 CHARGED state 必须有 charged support \(A\mid K\)。定义

\[
J_p(S)=\left\lfloor\frac{B_p}{A}\right\rfloor,
\qquad
C_p(S)=\frac KA.
\]

再定义 regeneration token：

\[
\eta_p(S)=
\begin{cases}
\nu_p(E-1),&\text{仅当 state 持有带 }E>1\text{ 的具名 immediate d=1 regeneration token},\\
0,&\text{其它 CHARGED state}.
\end{cases}
\]

local rank 为

\[
L_{\rm charged}(S)=(J_p,C_p,\eta_p,0).
\]

这统一：support accumulation、same-chart support promotion、joined-support overflow reset、fixed-n
bounded divisor、high-support rank-aware bundle、q=1 d=1 relay/regeneration、three/fourth/H4 persistent
macros 以及 T2 atomic strict edges。

### 4.4 TYPEI / PRE

使用已有两阶段 theorem 的 rank：

\[
L_{\rm PRE}(S)=(a,0,0,0).
\]

PRE 只允许严格降低 a 的边；formal PRE edge 若未来补齐 E1--E4，无需重做 T5。

### 4.5 TYPEI / ABSORB

固定一次性 \(\varepsilon\in\{\min,\max\}\)，令

\[
L_{\rm ABSORB}(S)=(R,m,r_\varepsilon,0).
\]

只允许已有 phase schedule 中严格降低这组字典序的 rechart/pruning。没有 E1--E4 的 formal cursor
仍然不是 edge。

### 4.6 TYPEI / RESET

legacy carrier reset 若真正拥有 E1--E4，只能进入 RESET protocol，并保存正整数 reset carrier
\(M\)：

\[
L_{\rm RESET}(S)=(M,0,0,0).
\]

RESET 内只允许 \(M\) 严格下降；同一 \(\rho\) 下禁止返回 CHARGED/PRE/ABSORB。这样仓库已有
\(38\to12\to132\to330\to132\) carrier re-entry path 永远不能组成 recursive cycle：进入 RESET
后，导致 12->132 或 132->330 的向上 re-entry 根本没有 admission。

## 5. 统一七元势

定义

\[
\boxed{
\Pi_{T5}(S)=
(\rho(S),\Phi(S),\Psi(S),r_1(S),r_2(S),r_3(S),r_4(S))
\in\mathbb N^7
}
\]

按字典序，其中非 Type-I state 取 \(\Psi=0\)，各 local tuple 按第 4 节填入
\((r_1,r_2,r_3,r_4)\)。`GENERIC_MARKED` local tuple 取全零。

\(\mathbb N^7\) 的字典序良基。

## 6. 规范 admission rule 与合同推论

作为 state contract 的 E5 规范，一张拟产生 persistent target 的 receipt 在 E1--E4 后，只有以下三种 admission ticket：

1. `OUTER_RANK_DROP`：\(\rho(T)<\rho(S)\)。后续 phase/protocol/local fields 可全部重置；
2. `PHASE_DROP`：\(\rho\) 不变而 \((\Phi,\Psi)\) 字典序严格下降；后续 local fields 可重置；
3. `LOCAL_DROP`：\(\rho,\Phi,\Psi\) 全部不变，且对应 phase 的 canonical local tuple 严格下降。

如果三者都不是，则输出必须是 `REJECT_NONDECREASING_SUCCESSOR` 或保持为非递归 evidence/checkpoint。

因此每个 admitted edge 都满足

\[
\Pi_{T5}(T)<\Pi_{T5}(S).
\]

这不是按 edge 临时挑势：phase、protocol 和 local evaluator 都是 state normal form 的规范字段，进入
state_id，并由 target verifier 从原始整数重算。它也不把“E1--E4 已完成”误写成“ticket 已存在”；
后者仍是把 candidate 提升为 `verified_edge` 的独立 E5 义务。

## 7. 当前合同输出面的闭合审计

状态合同的 selector 只有 Type-I hit、Type-II hit、support switch、q-adic lift、generalized dyadic
terminal 五种输出；root terminal 是终端标签，不是第六种 edge。

- 两种 hit 与 root terminal：无 successor；
- generalized dyadic：若 receipt 已恢复解则 terminal；若建较小 source state，必须有
  \(\rho(T)<\rho(S)\)，属于 ticket 1；
- support switch：若产生 persistent state，必须被正规化到 Type-II、G handoff、Type-I 某 protocol
  或 generic marked。之后只能按 ticket 1--3 入队；
- q-adic lift：necessary congruence 本身是 evidence。只有构造完整 state、E4 lift 并通过 ticket 1--3
  才能成为 edge。

所有其它 Fourier/quotient/relation/capacity 计算在状态合同中已经标为 analysis evidence，或者属于
macro checkpoint。因此**当前状态合同内**的 persistent successor surface 被上述三种 ticket 穷尽。

故不存在第四种“先入队、以后再想 E5”的合法对象。

## 8. 与 T6 的严格分界

T5 完成后仍可能存在 actual reachable state 没有 terminal，也没有任何能通过 E1--E4 + T5 ticket 的
candidate。这是

\[
\forall S\;\exists\text{ outgoing action}
\]

的 T6 totality 问题，而不是 T5 well-foundedness 缺口。

特别地，positive-q 新 root 的首条 local edge 之后没有后续 Type-I edge、c=8 double-low
不存在、某 overflow 没有 rank-improving bundle、marked terminal membership 未证明，都只会
使 selector 停在“没有 outgoing edge”，不会制造 T5 cycle 或迫使修改全局势。
