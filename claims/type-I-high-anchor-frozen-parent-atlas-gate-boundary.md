---
kind: claim
claim_id: type-I-high-anchor-frozen-parent-atlas-gate-boundary
title: 冻结 verified-parent atlas 的 high-R cofactor gate 边界
statement: 对冻结 selector 工件 `type-i-representation-dual-capacity-selector-results.json`（SHA-256 `d5899f44423b64709384aa282a70cd6168f3380932456f0e8564256d2017aba7`）递归提取的 76 个 verified-edge occurrence，51 个严格 verified-parent 后继是 fixed-p high canonical 锚（31 个不同的 (p,R,A)）。它们全部能以 `high_R_path_anchored_bundle_v1` 重放至 overflow，但没有一个通过 direct cofactor gate A/gcd(A,C) divides r：35 个有 A/gcd(A,C)>r，余下 16 个有较小的 A/gcd(A,C) 而仍不整除 r。因此此冻结 atlas 不产生任何可定义 Lambda_p(H->T) 的 direct-cofactor 宏候选，更不产生可闭合 E1--E4 的递归宏边。
claim_status: established
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-high-anchor-cofactor-macro-e1-e4-admission
  - type-I-high-anchor-cofactor-outer-rank-composition
  - type-I-overflow-fixed-n-bounded-divisor-saturation
  - type-I-overflow-fixed-s-bounded-divisor-saturation
topics:
  - type-I
  - high-carrier
  - parent-atlas
  - r-chart
  - cofactor
  - support-gate
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_anchor_parent_atlas.py
    role: read-only recursive receipt extraction and deterministic high-R replay
  - result: reproductions/type-i-high-anchor-parent-atlas-results.json
    role: frozen input hash, per-parent replay rows, and aggregate boundary
  - reproduction: reproductions/type_i_high_r_chart_two_anchor.py
    role: canonical chart and high_R_path_anchored_bundle_v1 implementation
  - reproduction: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: frozen verified parent receipts
visibility: public
last_checked: '2026-08-06'
---

# 冻结 verified-parent atlas 的 high-R cofactor gate 边界

## 1. 严格范围

高锚 direct cofactor 的正确形状是 `P -> H => S -> T`。本卡只从冻结工件中递归读取
`selector_status=verified_edge` 与 `recursive_edge_eligible=true` 的 receipt，严格以其
`successor_state` 为 H；纯数值 chart 不会被合成为 parent。

严格 high parent 要求：p 是 1 mod 24 的素数，pR+1=4K，A divides K，
`canonical_chart(p,A)=(R,K)`，p<R<4A，p does not divide R，且 parent 自身带全真
E1--E5 与 Sol(p) 恒等提升。只有这样的行计入下文的 51 条。

## 2. 可复跑结果

输入的 SHA-256 为：

```text
d5899f44423b64709384aa282a70cd6168f3380932456f0e8564256d2017aba7
```

| 项目 | occurrence 数 |
|---|---:|
| 递归发现的 verified-edge | 76 |
| 纯数值 high successor | 66 |
| 严格 verified-parent high anchor | 51 |
| 其中不同的 (p,R,A) | 31 |
| bundle 重放为 overflow | 51 |
| 通过 A/gcd(A,C) divides r | 0 |
| A/gcd(A,C)>r | 35 |
| A/gcd(A,C)<=r 但不整除 r | 16 |
| 定义且严格下降的 Lambda_p(H->T) | 0 |
| 完整闭合的宏 E1--E4 | 0 |

每一行都通过 raw source 和 complete-excess bundle 的重放，并给出 overflow 中间 chart S。
失败发生在其后精确的 cofactor gate。令 a=A/gcd(A,C)，M=kp+r，0<r<p；所有行都有
a not divides r。因此 A_T=lcm(A,C) 不整除 K_T=rC，target 不能成为 charged canonical
chart。故 Lambda_p 在 T 处无定义，而不是已经定义但未证明下降。

## 3. E1--E4 的第二道边界

即使未来某行通过 gate，当前 51 张 parent receipt 也都缺少 parent adapter/version、
replay checks、source/successor content address、`source_tree_scope` 与 parent typed fiber。
它们也没有 H/S/T 三个 chart 的 typed F/G/hit 证书和 T-to-H typed lift。因此旧 receipt 的
数值端点不能推出宏 E3/E4。

结论有两层：当前有限 atlas 首先被 arithmetic gate 完全阻断；而新的 gate 命中也仍须满足
`type-I-high-anchor-cofactor-macro-e1-e4-admission` 的 scoped、content-addressed typed
合同，才能成为候选宏边。本卡不是全称否定定理，只记录冻结 verified-parent 覆盖图。

## 4. 下一步

新的 parent dispatcher 应把

```text
A/gcd(A,C) divides (M mod p)
```

作为预筛条件。命中后还必须输出完整 P-to-H receipt、H/S/T typed F/G 证书、scope/hash
链和 terminal/alternate-first 结果；E5 再由 Lambda_p 组合秩支付。
