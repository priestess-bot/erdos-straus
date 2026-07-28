---
kind: claim
claim_id: type-I-tail-upper-b1-completion-profile-500m
title: 五亿普通双尾遗漏的上半区 B 等于一终端闭合
statement: 对p<=500000000的1717个普通Type II p-1双尾遗漏，1709个已有m<=215的上半区B=1 Type I桥。其余8个经精确分流闭合：3个从同一短盒生成的上半区源状态重建为B=1，1个在m=231直接命中，4个在m<=999的完整B=1延伸中重选上半区桥。故1717点全部具有上半区B=1 Type I终端桥；所选正规形最大缺口为5963。该为组合式有限审计，不给出全称选择器。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- type-II
- upper-half-source
- source-reselection
- small-B
- gap-extension
- finite-audit
- mixed-selector
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-terminal-bridge-context
visibility: public
last_checked: '2026-07-28'
---

# 五亿普通双尾遗漏的上半区 \(B=1\) 终端闭合

输入是完整的 \(p\le5\cdot10^8\) 普通 Type II \(p-1\) 双尾遗漏集，共 1,717 个目标。
这不是重新扫描全部目标，而是把三个已独立穷尽的有限结果作精确分割，并对每条最终选中的
\(B=1\) Type I 桥重新验证目标与源的单位分数恒等式。

## 分流

| 分支 | 数量 | 最终正规形缺口范围 |
| --- | ---: | ---: |
| 原 \(m\le215\) 审计中已为上半区 \(B=1\) | 1,709 | \(\le215\) |
| 下半区记录经短盒源状态重选 | 3 | \(263,2691,5963\) |
| 最后一个短盒源状态残余的直接延伸 | 1 | \(231\) |
| 原 \(B=1\) 直接遗漏的上半区延伸 | 4 | \(271,351,535,707\) |
| 合计 | 1,717 | 最大 \(5963\) |

三个“下半区记录经短盒源状态重选”的目标为

\[
p\in\{629689,\ 58757449,\ 83445289\}.
\]

它们在短盒中生成的上半区状态都取 \(n=p-1\)，但对应的 \(B=1\) 正规形缺口分别为
\(2691,263,5963\)。最后的短盒源状态残余为

\[
p=218482009,\qquad (m,A,B,C)=(231,4952,1,11030),\qquad n=p-43.
\]

因此得到精确的有限分流

\[
1717
=1709_{\mathrm{direct\ upper}\ B=1}
+3_{\mathrm{source\!-\!state\ reselected}}
+1_{m=231}
+4_{\mathrm{direct\ gap\ extension}}.
\]

## 含义与边界

这提供了原混合终端选择引理的更强有限版本：在该输入上，普通双尾遗漏全部可用上半区
\(B=1\) Type I 分支处理。它也纠正了按“最短源距离”选出的个别 \(B=1\) 实现可能具有很大
缺口的现象：那些是选择规则的输出，不是所需缺口的证明下界。

但这里的上界 \(5963\) 来自明确的 1,717 点组合审计。它没有证明任意核心素数都有 \(B=1\)
分支，也没有构造随 \(p\) 有效的源状态或缺口选择规则。

重建命令：

~~~bash
python3 reproductions/type_i_tail_upper_b1_completion_profile_500m.py
python3 -m unittest tests/test_type_i_tail_upper_b1_completion_profile_500m.py -q
~~~
