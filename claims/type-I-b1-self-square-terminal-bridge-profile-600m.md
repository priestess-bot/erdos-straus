---
kind: claim
claim_id: type-I-b1-self-square-terminal-bridge-profile-600m
title: 六亿冻结压力集上 B 等于一自平方终端桥剖面
statement: 对六亿冻结普通 Type II 双尾遗漏所选的1,964个上半区 B=1 目标正规形，自平方条件 H 偶且 H>4C 精确命中1,092个，其中1,090个还满足 H>8C，因而给出上半区偶源。其余的 H 奇数计数807、H 不大于4C计数68可以重叠，故不是失败类型的分割，更不构成全称选择器。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- b1
- terminal-bridge
- self-square
- upper-half
- pressure-set
- computational-profile
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 六亿冻结压力集上的 \(B=1\) 自平方终端桥剖面

本剖面从四个已存的、可复算的审计产物重建目标侧数据：五亿范围的直接与上半区补全记录，及
五亿到六亿连续区间的直接与重选记录。它们覆盖冻结的 1,964 个普通 Type II 双尾遗漏点，且每点
选定一张上半区 \(B=1\) Type I 目标正规形。

对每张形式写成

\[
mR=4C+1,\qquad H=AR-1,\qquad K=CH.
\]

逐项检验 [自平方终端桥](type-I-b1-self-square-terminal-bridge.md) 的条件，得到：

| 项目 | 数量 |
| --- | ---: |
| 已选上半区 \(B=1\) 目标正规形 | 1,964 |
| \(H\) 偶且 \(H>4C\) 的自平方桥 | 1,092 |
| 其中 \(H>8C\) 的上半区源桥 | 1,090 |
| \(H\) 为奇数 | 807 |
| \(H\le4C\) | 68 |

最后两行不是互斥分类：同一目标可以同时有奇 \(H\) 和小补因子。因此它们不能相加为“剩余数”，
也不表示这些点没有其他终端桥。

1,092 张自平方桥按原目标来源的精确分布为：五亿直接上半区 907，五亿直接缺口延伸 1，
六亿连续段直接上半区 157，六亿连续段上半区重选 27。所有记录都重放了目标与源的三项单位分数
恒等式，并存入
[`type-i-b1-self-square-terminal-bridge-profile-600m-results.json`](../reproductions/type-i-b1-self-square-terminal-bridge-profile-600m-results.json)。

这是对一个固定、已选正规形集合的完整有限剖面。一般引理的条件是充分的，但本统计不蕴含每个
核心素数都存在满足该条件的 \(B=1\) 正规形，也没有证明 Erdős--Straus 猜想。

复现：

~~~bash
python3 reproductions/type_i_b1_self_square_terminal_bridge_profile_600m.py
python3 -m unittest tests.test_type_i_b1_self_square_terminal_bridge_profile_600m -q
~~~
