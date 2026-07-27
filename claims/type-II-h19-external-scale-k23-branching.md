---
kind: claim
claim_id: type-II-h19-external-scale-k23-branching
title: H19 外部尺度 k=23 的模二十九分支出口分类
statement: 在 H19-k10 模五重启的 c=2 分支中，全部静态可用尺度为 k|1800。令该参数再满足 u=23v+9 以启用 k=23；H19 加 36 条静态来源和 k=23 的 57 条一私有余因子线性型恰被 29 覆盖。对全部 v mod29 的精确重算，29 个子类中 1 个目标素数型不本原，5 个有显式 H19 Type II 射线除子，9 个有完整外部源严格递降（其中 4 个与射线命中重叠），18 个仍为无覆盖、无命中的可采纳逃逸状态。故局部覆盖分裂在该节点确实产生 11/29 的无条件出口，但不闭合整个状态树。
claim_status: computationally_reproduced
topics:
- type-II
- type-I
- descent
- external-source
- adaptive-family
- state-transition
- admissibility
- conditional-boundary
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

# H19 外部尺度 k=23 的模二十九分支出口分类

## 父状态

从 [H19-k10 覆盖重启](type-II-h19-external-scale-k10-renewal.md) 的 \(c=2\) 子分支开始，
全部静态可用尺度为 \(k\mid1800\)。令其参数再满足

\[
u=23v+9.
\]

于是

\[
p=6Q_{19}(115v+47)+8\,328\,961. \tag{1}
\]

这个限制使 \(k=23\) 对全部 \(v\) 可用。将 H19 的 20 条一私有余因子型、全部
\(k\mid1800\) 的 36 条来源余商型与 \(k=23\) 的来源余商型合并，共得 57 条原始
仿射线性型。它们的覆盖素数恰为

\[
\{29\}. \tag{2}
\]

## 完整分支分类

令

\[
v=29w+d,\qquad 0\le d<29. \tag{3}
\]

对每个 \(d\)，脚本重新提取所有 H19 射线的固定因子，枚举每个来源 \(M_k^2\) 的
完整除子残数，并保持检查所有 57 条余因子型的有限域可采纳性。结果是：

| 结局 | 子类数 |
|---|---:|
| 目标素数型非本原 | 1 |
| 有 H19 Type II 射线除子 | 5 |
| 有完整外部源严格递降 | 9 |
| 至少一个无条件出口 | 11 |
| 无出口且无覆盖的可采纳状态 | 18 |

“至少一个无条件出口”是前三行的并集；其中 4 个子类同时有射线证书和外部源递降。
射线行保存实际整除 \(p+4s\) 且同余 \(-1\) 的因子型；来源行保存命中完整
\(M_k^2\) 除子残数目标的基因子与余商指数。因此这两类不是“若某仿射余因子为素数”
才成立的模型性出口。

剩余 18 个子类在这一模型中仍有 57 条原始、无覆盖线性型，所有 H19 射线仍避靶，
所有列出来源的完整平方因子目标仍缺失。它们仅在 Dickson 素数元组猜想或 Schinzel
假设下给出无穷实际素数。

## 含义

这是当前状态树中第一个同时含有真实出口和条件性重启的完整局部横截面。它说明
“覆盖后细分”不能简单地二分为闭合或重启：正确的状态转移应记录出口比例、出口类型和
仍存分支的强制因子来源。

这仍不足以证明递归会终止。要形成正向定理，需要证明每次类似的可采纳重启都消耗一个
可累计资源，或证明残存分支的比例沿某个自适应尺度/移位规则趋于零。

运行

```bash
python3 reproductions/type_ii_h19_external_scale_k23_branching.py
python3 -m unittest tests/test_type_ii_h19_external_scale_k23_branching.py -q
```

可重建 (1)--(3) 的覆盖根、29 个子类的全部分类及每张出口见证。
