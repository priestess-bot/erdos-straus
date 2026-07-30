---
kind: claim
claim_id: type-I-f-overflow-multi-support-height-boundary
title: 多支持盒溢出收费与实际载体高度的局部边界
statement: 在 253 个半径六以内有溢出见证的分色 F 状态和 506 个确定性双颜色分配中，溢出坐标层总数为 3402；选定载体实际高度至少覆盖对应超额层的只有 706 层，若要求先覆盖活跃基线再覆盖超额层则只有 60 层。该结果说明条件性多支持容量模型的溢出收费不是现有载体高度的自动推论，但不排除其他载体分配或递降解释。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-multi-support-conditional-capacity
  - type-I-f-overflow-active-support-boundary
topics:
- type-I
- F-state
- relation-lattice
- overflow-radius
- multi-support
- q-adic
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-context
visibility: public
last_checked: '2026-07-30'
---

# 多支持盒溢出收费与实际载体高度的局部边界

## 审计对象

前一张条件性容量卡把每个溢出坐标的超额层数 \(e_q\) 直接加到确定性选择的 \(a/s\)
载体需求。这里逐个检查该需求是否已经由被选状态的实际高度

\[
h_q^a=v_q(aR+1),\qquad h_q^s=v_q(sR+1)
\]

支持。活跃 \(q_a,q_s\) 使用原有需求基线；非活跃溢出素数沿用“较高载体优先、平局归
\(a\)”的规则。该审计不枚举其他颜色分配，也不寻找新的源状态。

## 结果

```text
unresolved_record_count: 291
support_record_count: 253
assignment_count: 506
overflow_layer_count: 3402
layer_height_at_least_excess: 706
layer_height_at_least_baseline_plus_excess: 60
assignment_all_excess_supported: 176
assignment_all_baseline_plus_excess_supported: 0
```

因此只有 \(706/3402\approx20.75\%\) 的溢出层满足最宽松的
\(h_q\ge e_q\) 检查；要求覆盖活跃基线后再增加溢出层时，满足数降为
\(60/3402\approx1.76\%\)。这不是容量超载的反例，而是说明“溢出层必然收费到已选载体”
尚未成为状态内事实。

## 逻辑边界

1. 该审计固定了前一张卡的确定性分配和最优双颜色 assignment；其他载体选择可能有
   不同高度。
2. 实际高度不足不排除把溢出转换成新的模数、标签或源距离下降。
3. 38 个半径六以内无见证状态仍不提供目标不存在结论。

可靠的下一步不是继续放大该收费系数，而是证明一个选择不变的多支持高度映射，或把
失败的高度收费转化为严格可提升的算术下降。

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
