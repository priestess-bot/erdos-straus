---
kind: claim
claim_id: type-I-pminusone-miss-upper-b3-reselection-profile-500m
title: 五亿p减一遗漏经上半区源重选的B不大于三闭合
statement: 对五亿p减一桥遗漏的185个最短上半区源状态，119个直接有B=1的Type I正规形实现。其余66个逐点穷尽同一m不大于215 Type I盒的全部偶上半区源状态后，65个可重选为B=1；唯一B=1遗漏为p=218482009，其所有上半区B=1状态均不存在，但有最小B=3实现。因此185点在该有限盒中均可重选为上半区B不大于3的Type I终端桥。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- p-minus-one
- upper-half-source
- source-state
- normal-form
- source-reselection
- small-B
- selector-boundary
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-terminal-bridge-context
visibility: public
last_checked: '2026-07-28'
---

# 五亿 p减一遗漏经上半区源重选的 \(B\le3\) 闭合

[最短源状态三级溢出剖面](type-I-pminusone-miss-source-overflow-profile-500m.md)的 185 个
\(p-1\) 桥遗漏都已有最短上半区源状态，但其中 66 个在该**同一**状态上没有 \(B=1\)
实现。本审计不把这种状态失败误作目标素数失败。

对每个这类点，完整枚举同一

\[
3\le m\le215,\qquad m\equiv3\pmod4
\]

Type I 正规形盒的全部严格最大尾反向提升，只保留偶且满足

\[
n\ge\frac{p+1}{2}
\]

的源状态。每个候选 \((p,n,E)\) 先按

\[
R=\frac{E-1}{p-n},\qquad K=\frac{pR+1}{4}
\]

以 \(B=1\) 的精确除子条件 \(C\mid K,\ 4C\equiv-1\pmod R\) 检查；仍失败时才完整
枚举该源状态的所有 \(BC\mid K\) 正规形实现并最小化 \(B\)。每张输出证书均重建目标与源
的单位分数恒等式。

## 结果

| 项目 | 数值 |
| --- | ---: |
| \(p-1\) 桥遗漏 | 185 |
| 存储的最短上半区源已为 \(B=1\) | 119 |
| 经源重选后成为 \(B=1\) | 65 |
| 上半区 \(B=1\) 仍遗漏 | 1 |
| 上半区 \(B\le3\) 闭合 | 185 |

唯一的上半区 \(B=1\) 遗漏为

\[
p=218\,482\,009.
\]

在整个指定盒中，它的三个可实现 \(B=1\) 源状态都在下半区；最小上半区实现为

\[
(p-n,E)=(683\,769,869\,070\,400),\qquad B=3.
\]

因此，“最短源状态没有 \(B=1\)”在 65 个点上只是源状态选择不当；但 \(p=218\,482\,009\)
说明即允许完整有限源重选，也不能把上半区终端分支统一收缩为 \(B=1\)。

## 含义与边界

该结果解释上一张三级溢出边界：高指数溢出通常可由**换源**消除，而不是从同一 \(K\) 上继续
增加指数库存。它没有给出如何对任意核心素数构造该替代源，也不证明统一 \(B\le3\) 界。

下一条全称引理必须同时选择源状态和正规形；仅在预先选定的 \((p,n,E)\) 上分析除子积集，
无法控制这个重选自由度。

重建命令：

~~~bash
python3 reproductions/type_i_pminusone_miss_upper_b3_reselection_profile.py
python3 -m unittest tests/test_type_i_pminusone_miss_upper_b3_reselection_profile.py -q
~~~
