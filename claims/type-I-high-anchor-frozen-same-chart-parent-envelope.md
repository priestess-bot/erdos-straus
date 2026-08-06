---
kind: claim
claim_id: type-I-high-anchor-frozen-same-chart-parent-envelope
title: 冻结同图表父边的内容寻址证据域包装
statement: 对冻结 selector 工件 `type-i-representation-dual-capacity-selector-results.json`（SHA-256 `d5899f44423b64709384aa282a70cd6168f3380932456f0e8564256d2017aba7`）中 11 条严格 high canonical 的 `overflow_same_chart_support_promotion_v1` verified-parent occurrence，可以不补造任何数值选择历史地重算其 determinant、同图表支撑提升、canonical chart、严格 absorbed-support 势和 Sol(p) 恒等标记；把工件 SHA-256 与原 receipt digest 一同绑定为有限证据域 scope 后，得到 11 张带 source/successor content address、具名 adapter、全真 replay checks 与 global-solution-marking typed fiber 的 `frozen_same_chart_parent_envelope_v1` 回执。该包装只是在冻结工件内重建该一个家族的 parent API，明确不注册 selector 边；它不添加 H/S/T 的局部 F/G/hit 重分类或 terminal/alternate-first 菜单，故不能仅由该 envelope 推出完整 high-cofactor macro E4 或递归资格。
claim_status: established
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-high-anchor-frozen-parent-atlas-gate-boundary
  - type-I-high-anchor-cofactor-macro-e1-e4-admission
topics:
  - type-I
  - high-carrier
  - parent-api
  - content-addressing
  - same-chart
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_anchor_frozen_same_chart_parent_envelope.py
    role: read-only reconstruction and tamper rejection
  - result: reproductions/type-i-high-anchor-frozen-same-chart-parent-envelope-results.json
    role: 11 scoped parent envelopes and six-family audit
  - input: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: frozen legacy receipts
visibility: public
last_checked: '2026-08-06'
---

# 冻结同图表父边的内容寻址证据域包装

## 1. 问题的精确范围

冻结 parent atlas 的 51 条 strict verified-parent high-anchor occurrence 来自六个 normal
form（本回放从同一冻结工件动态重算这张数量表）：

| normal form | high-parent occurrence |
|---|---:|
| `overflow_fixed_n_bounded_divisor_outer_rank_v1` | 12 |
| `overflow_fixed_n_outer_rank_reset_v1` | 6 |
| `overflow_fixed_s_bounded_divisor_outer_rank_v1` | 10 |
| `overflow_fixed_s_outer_rank_reset_v1` | 7 |
| `overflow_outer_rank_reset_v1` | 5 |
| `overflow_same_chart_support_promotion_v1` | 11 |

这些旧回执已经有数值 source/successor、`edge_id`、全真 E1--E5 和
`Sol(p)` 恒等标记，但没有 state-level content id、显式 scope、具名 replay adapter、
replay checks 或局部 fiber 类型。不能仅因 `selector_status=verified_edge` 就把它们当作
高锚宏的 parent API。

本卡只包装最后一个家族。选择它不是因为其余五个不可能重放，而是它在 receipt 固定后没有
未序列化的 selector 选择：设 source support 为 (A)，successor support 为 (M)，则

\[
  A<M\le B_p,\qquad A\mid M,\qquad M/A\ge2,
\]
\[
  pn=4Md+1,\qquad R=4M-n,\qquad K=M(p-d),\qquad
  \operatorname{canonical\_chart}(p,M)=(R,K),
\]
且
\[
  \left\lfloor B_p/M\right\rfloor<\left\lfloor B_p/A\right\rfloor.
\]

这些等式、端点和旧 edge digest 全部位于单张 receipt；本 adapter 还在输入工件中按
receipt digest 重新定位它，故可以在不执行 selector/history 的前提下重放其冻结证据绑定。

## 2. 冻结证据域 adapter

令 (D) 为输入 JSON 的 SHA-256。对于每张符合上节条件的旧 receipt，定义

```text
scope = frozen_selector_artifact_sha256:D
adapter = frozen_same_chart_parent_envelope_v1
fiber.kind = global_solution_marking
fiber.marking = Sol(p)
fiber.local_chart_classification = unclassified
fiber.reclassification_required = true
```

再以 `(equation_target,R,K,A,state_class,fiber_class,scope)` 的 canonical hash 形成 source
与 successor 的 `state_id`。新 edge id 同时绑定 adapter、输入工件 SHA-256、旧 receipt
digest、旧 edge id、两个 content-addressed state；验证时重新从该工件找回 digest 对应的
receipt 并完整重构 envelope，故不能用同一数值 chart 或自洽的新 hash 偷换另一份旧证据。

该 scope 的语义仅为有限、不可变工件的 evidence namespace。它没有声称恢复了旧 selector 的
live source tree；因此包装结果明确保持

```text
selector_status = analysis_evidence
recursive_edge_eligible = false
```

这是一条必要的范围界线，而不是 API 检查失败。

## 3. 可复现结论

`type_i_high_anchor_frozen_same_chart_parent_envelope.py --verify` 对 11 个同图表 strict
high parents 全部重新验证，并将每一张 envelope 与输入工件中的原 receipt digest 逐一绑定：

| 项目 | 数量 |
|---|---:|
| family 的 verified-parent occurrence | 11 |
| strict high canonical successor | 11 |
| 全真 frozen parent envelope | 11 |
| 注册为 selector edge | 0 |
| 产生完整 macro E4 certificate | 0 |

验证器还将第一张 envelope 的 successor support 篡改为 1；重新由 legacy receipt 构造的
期望 envelope 不再相等，包装 verifier 拒绝该回执。

## 4. 不能由这一步补出的信息

这个 one-family adapter 没有新增以下数据：

1. (H,S,T) 三图表各自的 F/G/hit 证书；
2. 若为 G，分离 character 与 empty-fiber certificate；若为 F/hit，局部 witness 与
   signed defect；
3. `T -> H` 的 marked-solution lift 所需的逐图表 reclassification；
4. terminal/alternate-first 调度已经穷尽的回执。

旧 `target_fiber.status=inherited_full_solution_set` 只证明图表无关的
\(\operatorname{Sol}(p)\) 恒等标记。它不能替代上列局部证明，尤其不能由 source 的 F
witness 复制到 target。因此本卡没有把任何 envelope 升格为 high-cofactor 宏候选。

此外，冻结 atlas 的 11 个同图表高锚仍全在 cofactor support gate
\(A/(A,C)\mid r\) 前失败；即使 parent API 已完整封装，也没有该工件内的可定义
\(H\to T\) 目标。见
[冻结 verified-parent atlas 的 high-R cofactor gate 边界](type-I-high-anchor-frozen-parent-atlas-gate-boundary.md)。

## 5. 后续接口

该 adapter 可以作为将来 gate-pass frozen parent 的 E3 输入，但只有同时新增：

1. deterministic high-R bundle 的同 scope 传播；
2. H/S/T 的独立 typed F/G/hit verifier；
3. terminal-first completion；
4. 宏 E5 支付；

后，才可按
[高锚 cofactor 宏 E1--E4 准入合同](type-I-high-anchor-cofactor-macro-e1-e4-admission.md)
讨论注册。不得通过把 `unclassified` 静默标为 F 或 G 来绕开这些条件。
