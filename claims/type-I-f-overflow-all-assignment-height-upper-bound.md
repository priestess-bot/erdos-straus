---
kind: claim
claim_id: type-I-f-overflow-all-assignment-height-upper-bound
title: 全部合法载体分配下的 F 溢出高度上界
statement: 对冻结的 253 个平方终端 F 状态，枚举全部 506 个满足活跃方向基线的线性源/方向分配，并允许每个溢出素因子独立选择两个源块中 q 进高度较高者。在这一乐观上界下，165 个状态没有任何分配能够承担全部溢出；1701 个溢出层中有 1348 层在所有分配下都缺少足够高度。该有限结果给出选择不变的高度缺口，但尚未把缺口转化为严格算术下降。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-multi-support-height-boundary
  - type-I-f-square-terminal-overflow-support-alignment
topics:
- type-I
- F-state
- overflow-radius
- q-adic
- capacity
- source-selection
- descent
- proof-program
sources:
- claim: type-I-f-overflow-multi-support-height-boundary
  role: deterministic-height-boundary
- claim: type-I-f-square-terminal-relation-certificate
  role: finite-box-certificate
visibility: public
last_checked: '2026-07-30'
---

# 全部合法载体分配下的 F 溢出高度上界

## 乐观上界定义

输入是 253 个平方终端 F 状态及其半径不超过 6 的首个目标仿射格见证。对每个状态，
枚举同一核心素数、同一模数 (R) 下的全部线性源 ((a,s))，以及所有满足 Fourier
活跃方向最低高度要求的有向分配 \((q_a,q_s)\)。

对每个溢出素因子 (q)，不强制它使用 (q_a) 或 (q_s) 的指定颜色，而是允许它在
两个源块中自由选择高度较高者：

\[
h_q^{\max}(a,s)=
\max\bigl(v_q(aR+1),v_q(sR+1)\bigr).
\]

因此这是一个对真实载体能力有利的上界；若在该上界下仍无法承担溢出，则任何更严格的
颜色冲突或基线收费也无法解决。

## 结果

结果文件
`reproductions/type-i-f-overflow-all-assignment-height-upper-bound-results.json` 的
SHA-256 为

```text
62fb9fc0f59bb011ad39276c3cd450ee1fe93fbafba7e7fc5f3800517f0bd3c5
```

摘要为：

```text
state_count: 253
total_admissible_assignment_count: 506
overflow_layer_count: 1701
universally_unsupported_excess_layer_count: 1348
state_category_counts:
  no_assignment_can_carry_all_excess: 165
  some_assignment_can_carry_all_excess: 88
assignment_can_carry_all_excess_count: 176
assignment_can_carry_baseline_plus_excess_count: 0
```

全部 253 个状态至少有一个满足活跃基线的合法分配；但在逐坐标采用最大块高度的
乐观模型下，165 个状态仍没有任何分配可以承担全部溢出。换言之，这 165 个状态的
高度缺口与先前选择哪一个确定性载体无关。

## 研究含义与边界

这条边界把当前选择器缺口压缩成一个明确候选集：若不能在这些状态中找到目标命中，
就必须证明普适高度缺口会导致跨状态容量矛盾，或构造从盒外关系向量到更小源的严格
下降。它尚未证明二者之一；高度不足也可能通过改变模数、标签、溢出坐标或源族来释放。

该审计只覆盖已在半径 6 内找到见证的 253 个状态，并且按逐坐标最大高度计算，忽略
不同溢出坐标之间的竞争。因此它是选择不变的必要性边界，不是最终容量定理。

## 复现

```text
python3 reproductions/type_i_f_overflow_all_assignment_height_upper_bound.py
```

脚本锁定 Fourier、分色、溢出、平方终端四个输入哈希，并枚举每个状态的全部合法源/方向分配。
