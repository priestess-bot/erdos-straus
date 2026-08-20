---
kind: claim
claim_id: type-I-t5-full-contract-level-global-well-foundedness
title: T5 完整状态合同层全局良基性
statement: 对 denominator-escape state contract 的 persistent recursive states 增加规范 major phase TYPEII_REL>TYPEII_G_HANDOFF>TYPEI>GENERIC_MARKED；TYPEI 内增加不可回返 protocol CHARGED>PRE>ABSORB>RESET，并按 normal form 定义 TYPEII 的 q、CHARGED 的 (floor(B_p/A),K/A,eta_p)、PRE 的 a、ABSORB 的 (R,m,r_epsilon)、RESET 的 M 作为 local ranks。以 induction rank、major phase、protocol 和四个 local fields 组成 N^7 字典序势 Pi_T5。任何 E1--E4 完成的 persistent successor 只有 outer-rank drop、phase/protocol drop 或 same-phase local drop 三种 admission ticket；否则不得标为 verified_edge。于是所有合同认可 recursive edges 在同一 Pi_T5 下严格下降，整个合同级递归图无无限路径和 directed cycle。terminal、analysis evidence、pending normalization 与 macro checkpoint 不属于递归边。该结论不证明任何 state 必有 outgoing edge，selector totality 独立属于 T6。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - denominator-escape-state-contract
  - type-I-phase-labeled-candidate-selector-well-founded-schedule
  - type-I-marked-support-accumulation-rechart-saturation
  - type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
  - type-I-overflow-outer-rank-reset
  - type-II-relation-reach-proper-endpoint-descent
  - type-II-relation-reach-gcd-shadow-endpoint-descent
  - type-II-q-one-full-carrier-phase-root-entry
  - type-II-q-one-c3-source-lineage-phase-root-entry
topics:
  - well-founded-descent
  - state-machine
  - phase
  - reset
  - type-I
  - type-II
  - proof-contract
sources:
  - concept: t5-global-well-foundedness-contract-v2
    role: canonical phase registry and proof
  - reproduction: reproductions/type_i_t5_full_global_well_foundedness.py
    role: all admission-mode controls and historical cycle rejection
  - data: data/t5-full-phase-registry-v2.json
    role: machine-readable canonical rank evaluator
visibility: public
last_checked: '2026-08-17'
---
# T5 完整状态合同层全局良基性

完整证明见 `concepts/t5-global-well-foundedness-contract-v2.md`。

关键变化是：T5 不再是“当前 edge allowlist 的共同 rank”，而成为 `verified_edge` 的合同级 admission
定理。任何未来算术 edge 只需支付 E1--E4 并匹配三个 rank ticket 之一；若需要同 \(\rho\) 向上重置
phase/protocol，则该动作按定义不是 recursive edge，除非先证明一个更外层 rank drop。因而新 arithmetic
families 不要求重写 T5 theorem。
