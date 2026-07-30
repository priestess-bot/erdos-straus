---
kind: claim
claim_id: type-I-f-overflow-universal-support-profile
title: 历史重复高度代理子集的多坐标和混合符号剖面
statement: 对历史重复当前高度代理筛出的165个F状态，半径六以内的确定性首个目标仿射见证均至少包含两个溢出坐标；支持大小2/3/4/5/6的状态数分别为22/55/56/25/7，符号类别为混合114、全负49、全正2，152个见证含规范活跃支持之外的素因子。这些统计精确描述冻结首见证，但165集合不再解释为穷尽合法载体后的普适缺口，首见证也不能代表完整目标纤维；故本卡只保留为历史代理剖面，不能排除完整纤维中的其它支持或定向表示。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-all-assignment-height-upper-bound
  - type-I-f-overflow-active-support-boundary
  - type-I-f-current-block-saturation-and-signed-denominator-defect
topics:
- type-I
- F-state
- relation-lattice
- overflow-radius
- multi-support
- q-adic
- descent
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-context
visibility: public
last_checked: '2026-07-30'
---

# 历史重复高度代理子集的多坐标和混合符号剖面

## 结果

对历史字段 `no_assignment_can_carry_all_excess` 筛出的 165 个状态，复用半径六以内
的确定性首个目标仿射格见证，得到：

```text
overflow support size: 2 -> 22, 3 -> 55, 4 -> 56, 5 -> 25, 6 -> 7
single-coordinate witnesses: 0
sign classes: all_negative 49, mixed 114, all_positive 2
active-support classes: all_active 13, has_inactive 152
total witness excess: 1512
universal unsupported excess layers: 1348
minimum total excess: 3
maximum total excess: 23
```

这里的 support size 统计全部首见证的**所有**盒外坐标。后续联合压力卡所说的 22 个
“单坐标”状态，只统计历史重复高度规则筛出的 `universally_unsupported` 子支持；它可以
是完整 overflow support 的真子集。因此“全部首见证至少两个盒外坐标”与“22 个代理
unsupported 支持只有一个坐标”不是同一口径，也不矛盾。

因此这 165 个**首见证**从第一层就是多坐标对象；不能把这批历史代理数据约化为一个
单独素因子 \(q\)。绝大多数首见证还包含规范 Fourier 支撑之外的素因子，而且符号通常
混合。它不说明完整目标纤维的所有 Pareto 极小表示都具有相同支持或符号。

## 对证明桥梁的限制

后续完整目标纤维审计已经证明全部单坐标选择不变下限为零，也证明 165 集合所依赖的
当前高度比较是反事实重复抵扣。因此本卡不再约束全称容量引理。它仍提示任何分析这些
冻结首见证的候选映射必须允许

1. 至少两个素因子坐标的联合需求；
2. 正负指数同时出现时的方向耦合；
3. 非活跃素因子进入载体或下降映射。

完整主线应改用原始指数盒上的全部带符号 Pareto 前沿和最小投影阻碍；不能用本卡的
确定性首见证支持分布替代该选择不变对象。

## 复现

```bash
python3 reproductions/type_i_f_overflow_universal_support_profile.py
```

结果文件：

```text
reproductions/type-i-f-overflow-universal-support-profile-results.json
```

输入哈希：

```text
assignment 62fb9fc0f59bb011ad39276c3cd450ee1fe93fbafba7e7fc5f3800517f0bd3c5
support    93c571a0fdfe12d18028c21d10c1f8445b1e34ae979489c852478d0bce8ad9b1
```

结果文件 SHA-256：

```text
c965936db508f5ccd553b79c94eb1b422b74ae4a78e51972306c7ebc7ad257a0
```
