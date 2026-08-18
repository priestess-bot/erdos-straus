---
kind: claim
claim_id: type-I-t6-current-named-reachability-t2-t3-coverage-audit
title: T6 当前具名边闭包的 ordinary-mark 不变量与 atomic surface 审计
statement: >-
  固定核心素数 p，并将 current named graph 定义为从 ordinary 根
  W=Sol(p) 出发、只沿 t5-full-transition-taxonomy-v2 中有具体 edge claim 的
  current_verified_edge_families 取传递闭包；contract-only 的 generic marked
  admission、pending normalization、analysis evidence 与 macro checkpoint 均不生成边。
  taxonomy 的 15 个具体边构造器逐一以 W_S=W_T=Sol(p) 的恒等 lift 支付 E4；其中若干
  只是 guarded constructor，不被误计为 selector totality。故路径归纳给出当前具名闭包
  中每个状态仍为 ordinary mark，nontrivial marked state 没有 seed。另一方面，taxonomy
  中仅有的两个 atomic edge family 恰与 T2 v1 的 H4 a=1 和 c=8 double-low 两个 arm
  相同，所以 T2 admission 在当前具名 atomic surface 上闭合。该 closed-world 结论不证明
  抽象 full T2、任意 future marked edge、c=8 double-low existence、T6 totality 或
  Erdos--Straus 猜想；taxonomy 一旦加入新 marked/atomic generator，审计必须重开。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-t5-full-transition-surface-exhaustion
  - type-I-atomic-admission-v1-finite-grammar-integration
  - root-context-terminal-disjunctive-invariant
  - type-II-relation-reach-proper-endpoint-descent
  - type-II-relation-reach-gcd-shadow-endpoint-descent
  - type-II-q-one-full-carrier-phase-root-entry
  - type-II-positive-q-G-full-carrier-phase-root-entry
  - type-II-q-one-c3-source-lineage-phase-root-entry
  - type-II-q-one-full-carrier-second-anchor-fixed-n-macro
  - type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
  - type-I-overflow-outer-rank-reset
  - type-I-overflow-a-one-dual-outer-rank-reset
  - type-I-overflow-high-carrier-fixed-n-R-descent
  - type-I-high-support-rank-aware-sink-bundle-selector
  - type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
  - type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-atomic-macro-checkpoint-contraction
  - type-I-q-one-full-carrier-d-one-c-eight-double-low-parent-anchored-atomic-macro
topics:
  - t6
  - selector
  - reachability
  - marked-solution
  - atomic-admission
  - transition-audit
  - proof-boundary
sources:
  - data: data/t5-full-transition-taxonomy-v2.json
    role: frozen-current-edge-family-surface
  - reproduction: reproductions/type_i_t6_actual_reachable_coverage_audit.py
    role: taxonomy-claim-E4-and-minimal-c8-control-regression-audit
visibility: public
last_checked: '2026-08-18'
---

# T6 当前具名边闭包的 ordinary-mark 不变量与 atomic surface 审计

完整逐行证明、guard/total 分类、c=8 最小剩余量词和数值控制见
[T6 actual-reachable coverage audit](../docs/T6-actual-reachable-coverage-audit-2026-08-17.md)。

## 1. Closed-world 定义

本卡的 `current named graph` 不是状态合同未来可能接纳的一切图。它只含当前 taxonomy 中
有具名构造 claim 的边。`legal smaller marked/equation source` 是 admission class，不是凭空
生成 E1--E4 的构造器；generalized-dyadic evidence、pending normalization 和 macro internal
checkpoint 也不产生 persistent successor。

15 张具体 edge claim 的 source guard 强弱不同：有的在声明域上 total，有的只有 guard 成立时
才构造边。但每张 claim 一旦构造 target，其 E4 都是图表无关
\(W_S=W_T=\operatorname{Sol}(p)\) 的恒等 lift。由根状态开始按路径长度归纳，当前闭包中不可能
首次出现 nontrivial mark。

## 2. Atomic surface

当前 taxonomy 的 atomic edge references 只有 H4 parent-anchored macro 和 c=8 double-low
parent-anchored macro。T2 v1 arm registry 也恰有这两行。因此当前 named atomic receipt 一旦
出现，已有 terminal / strict pending target / boundary / rejection 的确定分派；generic raw
schema 不构成额外 executable arm。

## 3. 边界

这是一条 reachability/coverage 不变量，不是 outgoing-existence theorem。特别地，c=8 的
double-low guard 是否对每个 terminal-first-surviving parent 有可选 label，仍是 T6 的开放量词。
future edge 若创建非平凡 mark 或新增 atomic arm，也必须显式扩张本卡的 closed world，而不能
沿用本结论。

聚焦复核：

```bash
python3 reproductions/type_i_t6_actual_reachable_coverage_audit.py --verify
```
