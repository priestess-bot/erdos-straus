---
kind: claim
claim_id: type-I-overflow-fixed-s-bounded-divisor-saturation
title: overflow 对偶 fixed-s 的有界除子外层秩递降
statement: 设 verified overflow 满足 pn=4Md+1、M=kp+r、1≤r<p，并令 s=(4rd+1)/p。若当前 absorbed support 满足 1≤A≤B_p=(p-1)^2/4，且存在 L|rd 使 A<L≤B_p、4L>s、floor(B_p/L)<floor(B_p/A)，则 R_L=4L-s、K_L=L(p-rd/L) 给出保持 Sol(p) 恒等提升、完整 E1--E5 和严格外层势下降的 overflow_fixed_s_bounded_divisor_outer_rank_v1 边；若 R_L<p 则为 marked absorb，否则仍为 overflow。A|L 不是必要条件：若 A∤L，严格外层势显式支付 support reset。该存在性条件不对所有 overflow 自动成立。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - type-I-overflow-fixed-s-dual-outer-rank-descent
  - type-I-overflow-fixed-n-bounded-divisor-saturation
topics:
- type-I
- overflow
- determinant
- fixed-s
- bounded-divisor
- support-reset
- outer-rank
- well-founded-descent
- typed-receipt
- proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: bounded fixed-s divisor selector and E1--E5 verifier
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: focused 12-fixture bounded-dual classification
visibility: public
last_checked: '2026-08-04'
---

# overflow dual fixed-s bounded-divisor outer-rank descent

## 1. 算术恒等式

设已验证 overflow 状态满足 pn=4Md+1，M=kp+r，1≤r<p。

由 M=kp+r 消去 k 得 p*s=4*r*d+1，其中 s=(4*r*d+1)/p。

因此 s 是正整数。对任意 L|r*d 定义 R_L=4L-s、K_L=L*(p-r*d/L)。
若 4L>s，则 R_L>0；直接计算得 4*K_L=p*R_L+1，且 L|K_L。

## 2. 支持势与完整边

令 B_p=(p-1)^2/4，Pi(A)=floor(B_p/A)。

若 1≤A≤B_p、A<L≤B_p 且 Pi(L)<Pi(A)，则 Sol(p) 是图表无关的标记集，
可用恒等映射作解提升。E1--E3 来自行列式恒等式和 L|r*d，E4 来自恒等提升，
E5 正是 Pi(L)<Pi(A)。

如果 L 不包含旧支撑 A，这并不破坏边的合法性；状态记录把严格势下降标记为
`support_reset_paid`，不再声称旧支撑包含于后继支撑。若 A|L，则同时保留旧支撑。

当 R_L<p 时后继是 `marked_absorb`；当 R_L>p 时后继仍是 overflow，但
absorbed-support 势已经严格下降。选择器取所有合格 L 中的最大者，只用于消除
选择歧义，不承担存在性证明。

## 3. 适用边界与回放

该引理只对给定的有界除子 L|r*d 提供完整递降边；它不声称每个 overflow 都有这样的 L。
当前 12 个冻结 overflow 回放中，选择器得到 11 条 verified edge，其中 1 条为
R_L<p 的 marked absorb，10 条仍为 overflow；唯一拒绝项是
`reachable_conflict_bundle_3`，其对偶载体 r=1 且没有合格 L。

复现命令：

```bash
python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
```

结果位于 `reproductions/type-i-representation-dual-capacity-selector-results.json` 的
`overflow_fixed_s_bounded_divisor_outer_rank` 分支。该回放收缩了双通道的有限余项，
但没有关闭递归可达 A>1 overflow 的全称存在性。
