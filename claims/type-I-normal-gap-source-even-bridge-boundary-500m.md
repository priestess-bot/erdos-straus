---
kind: claim
claim_id: type-I-normal-gap-source-even-bridge-boundary-500m
title: 五亿普通尾遗漏的缺口源偶桥边界
statement: 对p<=500000000的1,717个普通Type II双尾遗漏，完整枚举m<=215的全部Type I正规形并应用固定源n=p-m的缺口源偶桥判据，恰21个点命中、1,696个点遗漏；共检查78,215张正规形，命中的最大首缺口为119。因此n=p-m不是该完整压力集的充分终端选择器。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- type-II
- normal-form
- even-source
- descent
- selector-boundary
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I normal-form context
visibility: public
last_checked: '2026-07-27'
---

# 五亿普通尾遗漏的缺口源偶桥边界

对 [五亿普通尾遗漏](type-I-tail-reverse-even-source-closure-500m.md) 中的每个
$p$，完整枚举

$$
3\le m\le215,\qquad m\equiv3\pmod4
$$

内的所有 Type I 正规形，并对每张正规形应用
[缺口源偶桥判据](type-I-normal-gap-source-even-bridge.md)。换言之，此处只允许严格偶源

$$
n=p-m.
\tag{1}
$$

## 结果

| 项目 | 数值 |
|---|---:|
| 普通 Type II 尾遗漏 | 1,717 |
| 完整枚举的 Type I 正规形 | 78,215 |
| 缺口源偶桥命中 | 21 |
| 缺口源偶桥遗漏 | 1,696 |
| 命中的最大首缺口 | 119 |

首个命中缺口的分布为

$$
15:3,\ 31:10,\ 35:1,\ 39:2,\ 47:1,\ 51:1,\ 71:1,\ 99:1,\ 119:1.
\tag{2}
$$

因此，同一有限压力集在一般偶源选择器下有 1,717 个终端边，但刚性的 (1) 只命中 21 个：

$$
1717=21_{n=p-m}+1696_{\text{no gap-source bridge in }m\le215}.
\tag{3}
$$

## 边界

这是对固定源距离的完整有限反例基准，不是对 Erdős--Straus 猜想或完整 Type I 选择器的反例。
1,696 个遗漏仍可能由其它偶源 $n=p-s$、更大缺口、不同坐标或 Type II 机制闭合。它的结论
仅是：任何试图用“每张正规形都取 $n=p-m$”来证明混合终端引理的路线，已经在这个完整盒内失败。

可复现命令：

~~~bash
python3 reproductions/type_i_normal_gap_source_even_bridge_audit.py
python3 -m unittest tests/test_type_i_normal_gap_source_even_bridge_audit.py -q
~~~
