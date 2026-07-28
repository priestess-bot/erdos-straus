---
kind: claim
claim_id: type-I-pminusone-miss-upper-b3-reselection-profile-500m
title: 五亿p减一遗漏经上半区源重选的B不大于三闭合
statement: 对五亿p减一桥遗漏的185个最短上半区源状态，119个直接有B=1的Type I正规形实现。其余66个从m不大于215的Type I盒完整生成全部偶上半区源状态后，65个可重选为B=1；唯一B=1遗漏为p=218482009，其所生成的上半区源状态均不存在B=1实现，但有最小B=3实现。按当前最短源优先的选择，184个B=1实现中有26个正规形缺口超过215，最大为597803。因此185点在该有限源状态生成窗口中均可重选为上半区B不大于3的Type I终端桥，但该窗口不界定重建后的B=1正规形缺口，也不证明597803为最小可能缺口。
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

的源状态。这里的 \(m\le215\) 只界定**生成候选源状态**的正规形；每个候选
\((p,n,E)\) 随后按

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
| 上半区 \(B=1\) 仍遗漏（在所生成源状态中） | 1 |
| 上半区 \(B\le3\) 闭合 | 185 |
| 按最短源优先选择时，重建的 \(B=1\) 正规形缺口超过 215 | 26 |
| 按最短源优先选择时，重建的 \(B=1\) 正规形最大缺口 | 597,803 |

唯一的上半区 \(B=1\) 遗漏为

\[
p=218\,482\,009.
\]

在整个指定盒中，它的三个可实现 \(B=1\) 源状态都在下半区；最小上半区实现为

\[
(p-n,E)=(683\,769,869\,070\,400),\qquad B=3.
\]

因此，“最短源状态没有 \(B=1\)”在 65 个点上只是源状态选择不当；但 \(p=218\,482\,009\)
说明从这个有限源状态窗口产生的上半区源不能全部立即收缩为 \(B=1\)。另一方面，按最短源
优先选出的 26 个 \(B=1\) 重建缺口已经超过 215，故不能把该源状态窗口误读为 \(B=1\)
正规形的缺口界；这也不是最小缺口的下界。

## 含义与边界

该结果解释上一张三级溢出边界：高指数溢出通常可由**换源**消除，而不是从同一 \(K\) 上继续
增加指数库存。换源本身却可能把正规形缺口从候选窗口推出很远。它没有给出如何对任意核心素数
构造该替代源，也不证明统一 \(B\le3\) 界或 \(B=1\) 缺口界。

下一条全称引理必须同时选择源状态和正规形；仅在预先选定的 \((p,n,E)\) 上分析除子积集，
无法控制这个重选自由度。

重建命令：

~~~bash
python3 reproductions/type_i_pminusone_miss_upper_b3_reselection_profile.py
python3 -m unittest tests/test_type_i_pminusone_miss_upper_b3_reselection_profile.py -q
~~~
