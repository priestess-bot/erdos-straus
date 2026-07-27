---
kind: claim
claim_id: type-II-h19-external-scale-multicover-absorption
title: H19 富尺度五重覆盖的模七零出口吸收
statement: 在 H19-k23 模二十九分裂的残存 d=10 分支中，全部静态可用尺度为 k|1200600，共144个。H19 加这144条完整外部源余商型有覆盖素数 {7,37,53,61,73}，但没有 H19 射线证书或来源递降。按最小覆盖素数作完整分裂 w=7z+c 后，全部7个子类仍无 H19 射线证书、无144条来源中的完整外部源递降，且覆盖集精确变为 {37,53,61,73}。因此“每次局部覆盖细分均有正比例即时证书或递降出口”的候选收缩引理在该模型中为假。
claim_status: computationally_reproduced
topics:
- type-II
- type-I
- descent
- external-source
- adaptive-family
- state-transition
- conditional-boundary
- obstruction
- proof-program
sources:
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-factorization-context
- paper: bradford2024
  locator: "Propositions 1 and 3"
  role: external-source-descent-context
visibility: public
last_checked: '2026-07-25'
---

# H19 富尺度五重覆盖的模七零出口吸收

## 状态

在 [H19-k23 模二十九出口分类](type-II-h19-external-scale-k23-branching.md) 的残存
\(d=10\) 分支，参数可写为

\[
p=6Q_{19}(3335w+1197)+8\,328\,961. \tag{1}
\]

对这个进程，每个参数值都可使用的外部源尺度恰为

\[
k\mid1\,200\,600,
\]

共有 144 个。把 H19 的 20 条一私有余因子型和这 144 条完整外部源余商型合并，
得到 164 条原始线性型。所有 H19 射线和所有来源的完整平方因子递降均避靶，但局部
覆盖素数为

\[
\{7,37,53,61,73\}. \tag{2}
\]

## 模七分裂

按 (2) 的最小素数细分

\[
w=7z+c,\qquad0\le c<7. \tag{3}
\]

对全部七个子类，重新计算所有固定因子、H19 射线因子和 144 个来源的完整除子残数。
每一个子类都有：

| 项目 | 结果 |
|---|---|
| H19 Type II 射线证书 | 无 |
| 完整外部源严格递降 | 无 |
| 原始线性型数 | 164 |
| 覆盖素数 | \(\{37,53,61,73\}\) |

也就是说，素数 \(7\) 在七个子类中都被吸收到固定因子，除此之外没有产生即时的
证书或严格递降。

## 对势能路线的限制

这给出对以下候选引理的精确反例：

\[
\text{每个局部覆盖素数在其完整细分中都给出正比例的即时出口}. \tag{4}
\]

这里 (4) 的出口比例为零。该结果不排除在随后处理 \(37,53,61,73\) 后出现出口，
也不排除记录多个覆盖素数的更深势能；但任何正向分支收缩定理都不能只按当前覆盖素数
逐个贪心细分。

运行

```bash
python3 reproductions/type_ii_h19_external_scale_multicover_absorption.py
python3 -m unittest tests/test_type_ii_h19_external_scale_multicover_absorption.py -q
```

可重建 (1)--(3) 的全部状态、七个子类和零出口检查。
