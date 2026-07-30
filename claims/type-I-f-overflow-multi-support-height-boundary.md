---
kind: claim
claim_id: type-I-f-overflow-multi-support-height-boundary
title: 多支持盒溢出与当前块重复高度的历史边界
statement: 在253个半径六以内有首见证的分色F状态和506个方向编码中，历史脚本比较3402个溢出层与当前块高度，得到706个h_q>=e_q和60个baseline+excess比较命中。后续恒等式证明奇q处e_q已经是超过两个当前块总高度后的精确分母缺陷，因此这些比较会重复使用已经包含在K中的高度；它们只保留为冻结算法的反事实应力统计，不是实际载体覆盖率、容量不足或递降证据。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-multi-support-conditional-capacity
  - type-I-f-overflow-active-support-boundary
  - type-I-f-current-block-saturation-and-signed-denominator-defect
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

# 多支持盒溢出与当前块重复高度的历史边界

## 审计对象

前一张条件性容量卡把每个溢出坐标的超额层数 \(e_q\) 直接加到确定性选择的 \(a/s\)
载体需求。历史脚本逐个比较该需求与当前块高度

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

这里 (3402=2\times1701)：1701 是 253 个物理状态各计一次的首见证溢出层数，3402
则把每个状态的两个等价方向编码分别计入。它不是第二批独立溢出层。旧比较中只有
\(706/3402\approx20.75\%\) 满足 \(h_q\ge e_q\)，加入活跃基线后
只有 \(60/3402\approx1.76\%\)。这些比例不能解释为实际覆盖率：对奇 \(q\)，当前两块
高度之和已经等于 \(v_q(K)\)，而 \(e_q\) 是用尽 \(K\) 后的缺陷；把 \(h_q\) 再与
\(e_q\) 比较是反事实重复抵扣。

## 逻辑边界

1. 506 条记录是 253 个物理源对的两个方向编码，不是 506 个独立载体选择。
2. 当前高度比较既不证明覆盖，也不证明不足；合法资源必须来自 \(K\) 外的新乘子或状态。
3. 38 个半径六以内无见证状态仍不提供目标不存在结论。

可靠的下一步不是继续放大该收费系数，而是从完整目标纤维提取带符号分母缺陷，证明
它到外部 \(q\)-进提升剩余类的映射，或把提升失败转化为严格可提升的算术下降。

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
