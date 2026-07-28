---
kind: claim
claim_id: type-I-pminusone-miss-upper-b1-gap-extension-500m
title: 五亿 p减一遗漏经四缺口扩展的上半区 B 等于一状态闭合
statement: 对五亿p减一桥遗漏的185个点，从m<=215的完整上半区源状态生成窗口已有184个具有B=1的Type I实现；这些实现的最大缺口实际为597803。唯一遗漏p=218482009在仅继续直接穷尽m=219,223,227,231后，于m=231出现三个上半区B=1桥，故185点均具有上半区B=1 Type I桥。该结果否定将短盒B=3回退解释为全局B=1障碍，但不提供m<=231的统一缺口界。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- p-minus-one
- upper-half-source
- source-reselection
- small-B
- gap-extension
- finite-audit
- selector-boundary
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-terminal-bridge-context
visibility: public
last_checked: '2026-07-28'
---

# 五亿 \(p-1\) 遗漏经四缺口扩展的上半区 \(B=1\) 状态闭合

[上半区源重选 \(B\le3\) 剖面](type-I-pminusone-miss-upper-b3-reselection-profile-500m.md)
在共同的

\[
3\le m\le215,\quad m\equiv3\pmod4
\]

盒中生成的上半区源状态留下唯一 \(B=1\) 遗漏 \(p=218{,}482{,}009\)，并以 \(B=3\) 回退。
该事实只说明这个**固定短缺口的源状态生成窗口**中不能要求 \(B=1\)，并不说明此素数在更大
缺口处没有 \(B=1\) 桥。其余 184 个状态虽有 \(B=1\) 实现，但这些重建正规形的最大缺口已达
\(597{,}803\)，并不落在这个短盒中。

本审计不重新扫描整个范围，只对这个唯一遗漏继续穷尽四个后继缺口

\[
m\in\{219,223,227,231\}.
\]

每张 \(B=1\) Type I 正规形的全部严格最大尾反向提升均被检查，只保留偶上半区源，再按

\[
C\mid K,\qquad4C\equiv-1\pmod R
\]

重建其源状态 \(B=1\) 实现。

## 结果

| 项目 | 数值 |
| --- | ---: |
| \(p-1\) 桥遗漏 | 185 |
| 源状态生成窗口 \(m\le215\) 中已有 \(B=1\) 实现 | 184 |
| 前 184 个 \(B=1\) 实现的最大正规形缺口 | 597,803 |
| 延伸窗口检查的 \(B=1\) 正规形 | 1 |
| 延伸窗口检查的严格反向边 | 3 |
| 于 \(m=231\) 释放的点 | 1 |
| 上半区 \(B=1\) 状态闭合（不设统一缺口界） | 185 |

释放点的正规形和三个上半区源为

\[
(m,A,B,C)=(231,4952,1,11030),\quad R=191,\quad K=10{,}432{,}515{,}930,
\]

\[
(p-n,E)\in
\{(458617,87595848),(3569,681680),(43,8214)\}.
\]

按最短源距离选择，最后一个状态给出 \(n=p-43=218{,}481{,}966\)。它直接说明此前短盒中的
\(B=3\) 不是此目标的内在指数需求，而是 \(B\) 与允许缺口之间的有限盒权衡。

## 含义与边界

这个结果把当前下一步收紧为：不能把“一个 \(m\le215\) 的源状态窗口中 \(B=1\) 失败”当作
反驳全称 \(B=1\) 策略的证据。需要研究的是自适应缺口与源状态如何共同产生除子剩余命中，
并解释为什么源状态重选会放大重建正规形的缺口，而不是固定 \(B\) 或固定缺口的单独菜单。

它仍只是一个 185 点的有限审计。\(m=231\) 只释放最后一个源状态；其余重建的 \(B=1\)
正规形已超过该界。它没有给出任何对任意核心素数有效的缺口上界，也没有证明原混合终端选择引理。

重建命令：

~~~bash
python3 reproductions/type_i_pminusone_miss_upper_b1_gap_extension.py
python3 -m unittest tests/test_type_i_pminusone_miss_upper_b1_gap_extension.py -q
~~~
