---
kind: claim
claim_id: type-I-edge-local-atomic-ownership-sufficiency
title: 单后继 atomic edge 的局部 owner 充分性与 pooled-capacity 边界
statement: 若版本化 selector 在固定 terminal/alternate prefix 后至多选择一个 atomic successor，selected occurrence 由 immutable source/path identity 唯一标识，target support 完整吸收本 action 的 colored maximal blocks，且证明不跨 outgoing actions 汇总容量，则验证该 selected edge 不需要跨 action global one-use ledger。若 Fourier/Hall/flow 同时汇总多个 action 的 demand，则该结论失效：不同 action 可引用同一个物理 token，必须有 global ledger 或等价的不可重复收费证明。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-atomic-owner-epoch-locality
  - denominator-escape-state-contract
topics:
  - atomic-split
  - owner
  - one-use
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_atomic_admission_v1_contract.py
    role: edge-local and pooled-token controls
visibility: public
last_checked: '2026-08-17'
---
# 单后继 atomic edge 的局部 owner 充分性

若本次递归只选择一个 successor，则被吸收的完整素数幂块进入 target charged support；同一指数的
block 不能在同一 edge epoch 再成为 fresh。未来同素数的 fresh block 必须具有更高指数。

但这不是 pooled-capacity theorem：多个未选 action 同时进入 Hall/flow 不等式时，仍可能重复引用
同一 physical occurrence。
