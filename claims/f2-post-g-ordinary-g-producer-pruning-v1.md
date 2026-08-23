---
kind: claim
claim_id: f2-post-g-ordinary-g-producer-pruning-v1
title: 冻结 selected graph 中 positive-q G 的无种子性与 c=3 alternate 的 precedence 消去
statement: >-
  在以 initial_q_one_root_dispatch_v1 为唯一 initializer、以当前 registered producer
  source/target 图为递归语法、并禁止 TYPEI 非终端返回 TYPEII 的冻结 selected graph 中，
  Type-II relation F family 没有 seed；所有能产生 Type-II F/G endpoint 的 relation producer
  又都要求一个先验 F source 并严格降低 q。因此 positive-q G endpoint 在该图中不可达。
  唯一可达 ordinary G seed 是 initializer 的 q=1 G；在它上面，q=1 full-carrier handoff
  无附加 source-lineage 假设并产生确定 p-only target，而 c=3 relay 还要求额外 lineage
  receipt。固定 full-carrier-first precedence 后，c=3 relay 永不被 selected graph 调用，
  应视为 nonrecursive alternate，而不是活动 producer。该结论在新增 Type-II seed/producer、
  允许 TYPEI->TYPEII 返回或改变 precedence 时自动重开；它不声称抽象 positive-q G
  整数 family 为空。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-initial-q-one-root-terminal-or-full-carrier-dispatch
  - type-II-relation-reach-proper-endpoint-descent
  - type-II-relation-reach-gcd-shadow-endpoint-descent
  - type-II-q-one-full-carrier-phase-root-entry
  - type-II-positive-q-G-full-carrier-phase-root-entry
  - type-II-q-one-c3-source-lineage-phase-root-entry
  - type-I-t5-full-contract-level-global-well-foundedness
topics:
  - F2
  - post-G
  - reachability
  - Type-II
  - positive-q
  - q-one
  - source-lineage
  - precedence
  - producer-pruning
  - proof-boundary
sources:
  - data: data/t6-proof-frontier-v2.json
    role: frozen initializer and registered source-target graph
  - data: data/t6-wave1/f2-post-g-g-producer-pruning-v1.json
    role: machine-readable induction and reopen conditions
  - reproduction: reproductions/f2_post_g_g_producer_pruning.py
    role: focused graph-drift verifier
visibility: public
last_checked: '2026-08-24'
---

# ordinary G producer pruning

## 1. 要证明的不是算术 family 空性

positive-(q) G phase-root 定理的量词是正确的相对量词：若 actual、terminal-first 的
ordinary positive-(q) G source 已经存在，则它有一条 E1--E5 handoff。本卡不否定该
蕴含，也不声称满足其整数同余的对象不存在。

这里研究的是当前 selected graph 的 source lineage。记 (mathcal R_p^{\rm sel}) 为从唯一
initializer 出发、每个状态只执行固定 precedence 选择的 registered producer 所得闭包。
使用以下冻结规则：

1. initializer 只输出 root terminal，或 (q=1) ordinary G；
2. Type-II relation producer 的 source 必须为 F endpoint，且 nonterminal target 的
   (q') 满足 (q'<q)；
3. `TYPEII_G_HANDOFF -> TYPEI` 是单向 phase drop；`TYPEI -> TYPEII_REL/G_HANDOFF`
   的非终端返回被禁止；
4. q=1 G 上先执行无附加 lineage 假设的 full-carrier handoff。

## 2. F family 无种子引理

令 (F_n) 表示长度至多 (n) 的 selected trace 中出现的 Type-II relation F states。

- 基础步：initializer 的非终端输出是 q=1 G，不是 F，故 (F_0=\varnothing)。
- 归纳步：当前能输出 Type-II F target 的 producer 只有 proper-endpoint descent 与
  gcd-shadow descent；二者都要求 source 已是 Type-II F。因此若 (F_n=\varnothing)，
  则 (F_{n+1}=\varnothing)。Type-I phase 又不能生成一个 relation source。

于是

\[
\boxed{F_n=\varnothing\quad(n\ge0).}
\tag{1}
\]

这不是从 family registry 的“状态 OPEN/CLOSED”字段推断；它使用 initializer target、两类
producer 的 source guard 和 phase 单向性作结构归纳。

## 3. positive-q G 无种子引理

当前能输出 Type-II relation G target 的 producer仍只有上述两类 F-source descent。由 (1)，
它们从未获得 source。因此 selected graph 中不存在由 relation descent 产生的 G endpoint。
initializer 唯一的 G seed 又满足 (q=1)。故

\[
\boxed{
S\in\mathcal R_p^{\rm sel},\ S\text{ ordinary Type-II G}
\Longrightarrow q(S)=1.
}
\tag{2}
\]

特别地，registered `positive_q_g_full_carrier_phase_root` 在当前 selected graph 没有 source。
它仍可保留为相对 theorem/control，但不能作为 activity inventory 中必须实现的 queue producer。

## 4. c=3 alternate 被 precedence 严格支配

在 (2) 的唯一 G source (S_1) 上，q=1 full-carrier theorem 只要求 actual ordinary G、
terminal-first miss 与普通 (operatorname{Sol}(p)) mark，并产生唯一 p-only target (T_X)。
c=3 relay 除同一 source 条件外，还要求一份额外 source-lineage receipt (L_3)。所以其
定义域满足

\[
D_{c3}\subseteq D_{\rm full}.
\tag{3}
\]

且 full-carrier rule 的 target/ticket 不依赖 (L_3)。若固定

```text
q_one_full_carrier_phase_root_entry_v1
  before
c3_source_lineage_even_tail_root_receipt_v1
```

则：

- (L_3) 不存在时，只能调用 full-carrier；
- (L_3) 存在时，full-carrier 仍先被选择并退出 Type-II G phase；
- 退出后同 phase 的 c=3 alternate 不再有调用点。

因此 c=3 relay 在 selected graph 中永不被调用。它不是 family-empty theorem，而是
`NONRECURSIVE_SUPERSEDED_ALTERNATE` 的 producer disposition。

## 5. 重开条件与边界

下列任一变化都会使 (1)--(3) 重新成为义务：

1. initializer 或新 producer 生成 positive-(q) F/G seed；
2. 新 producer 从非 F source 生成 Type-II relation endpoint；
3. 允许 Type-I 非终端返回 Type-II phase；
4. c=3 被排在 full-carrier 之前，或 selector 同时选择多个 G exits；
5. F1 source inventory 发现一个尚未登记的 Type-II seed constructor。

所以准确结论是

```text
POSITIVE_Q_G_IN_FROZEN_SELECTED_GRAPH = FAMILY_EMPTY
C3_LINEAGE_RELAY_SELECTED_PRODUCER = NONRECURSIVE_SUPERSEDED_ALTERNATE
ABSTRACT_POSITIVE_Q_G_RELATIVE_THEOREM = RETAINED
F2_POST_G_TYPEI_TOTALITY = OPEN
```

该 producer pruning 只消除两个不必要的 runtime actualization 分支；q=1 full-carrier 后的
Type-I continuation 仍需单独闭合。
