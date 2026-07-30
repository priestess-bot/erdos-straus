---
kind: claim
claim_id: type-I-f-overflow-multi-support-square-descent-boundary
title: 多支持溢出分支的较小块平方终端边界
statement: 对 253 个半径六以内有溢出见证的分色 F 状态及其 506 个确定性双颜色载体分配，较小块平方 E=min(U,V)^2 的整除、同余、源范围、源乘积整除和奇偶性逐项复核全部通过；506 个分配均给出偶终端，0 个落入混合奇偶平方障碍。该结果只提供状态内终端候选，不提供同一状态的目标平方除子命中或全称选择器。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-multi-support-height-boundary
  - type-I-linear-block-square-terminal-boundary
  - type-I-f-full-cross-color-pair-capacity-boundary
topics:
- type-I
- F-state
- overflow-radius
- block-square
- even-terminal
- descent
- multi-support
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-context
visibility: public
last_checked: '2026-07-30'
---

# 多支持溢出分支的较小块平方终端边界

## 审计范围

从双颜色未决记录中保留半径六以内找到目标仿射格见证的 253 个状态；对每个状态，
枚举双颜色容量脚本选出的 2 个方向分配，共 506 个线性源状态 \((a,s,R)\)。令

\[
U=sR+1,\qquad V=aR+1,\qquad X=\min(U,V),\qquad E=X^2.
\]

脚本逐项检查：

\[
E\mid4K^2,\qquad E\equiv1\pmod R,\qquad
n=(UV-E)/R,\quad 0<n<p,
\]

以及 \(E\mid nK\) 和 \(n\equiv E\pmod2\)。这些检查不是只按块大小分类，而是对每个
分配实际计算。

## 结果

```text
unresolved_record_count: 291
support_record_count: 253
assignment_count: 506
even_smaller_block_square_terminal: 506
odd_marked_descent: 0
mixed_parity_square_obstruction: 0
```

因此，在这批有限溢出见证对应的确定性载体分配中，实际载体高度不足并没有产生新的
混合奇偶障碍；每个分配都有一个严格更小的偶源 \(n<p\)。这为“容量收费失败则转入
状态内终端”的分支提供了可复用边界。

## 逻辑边界

1. 38 个状态在半径六以内没有见证，不属于本审计范围。
2. 506 个分配来自一个确定性的双颜色选择规则，不代表所有合法载体分配。
3. F 型状态仍可能没有目标平方除子 \(e\)；较小块平方只验证偶终端 \(E\)，不能单独
   完成 \(p\) 的 Type I 目标—终端双因子选择器。
4. 因此本卡是一个有限的状态内下降出口，尚未给出跨状态可提升递降或全称证明。

下一步应研究：当目标侧保持 F 型而较小块平方给出 \(n\) 时，是否能把该终端与另一个
缺口状态的目标除子拼接，或把 \(n\) 纳入一个有良基势函数的可提升状态链。

## 复现

```bash
python3 reproductions/type_i_f_overflow_multi_support_height_audit.py
```

结果文件：

```text
reproductions/type-i-f-overflow-multi-support-height-audit-results.json
```

结果文件 SHA-256：

```text
45720bcc28c0b4d1b065e27bcd6507e1111fe3bfb89bb4c3aa513f82963d136c
```
