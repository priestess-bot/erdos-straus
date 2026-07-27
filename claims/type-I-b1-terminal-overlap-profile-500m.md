---
kind: claim
claim_id: type-I-b1-terminal-overlap-profile-500m
title: 五亿普通尾遗漏中的B等于1终端桥重叠剖面
statement: 在p<=500000000的1717个完整普通Type II双尾遗漏中，m<=215的B=1最短偶源桥捕获1713个。其1400个选中桥的源恰为p-1；对每个这类桥，若q=(m+1)/4、r=(R+1)/4，则q不整除r。其余313个选中桥使用p-1以外的偶源。前一结论是一般B=1同缺口重叠判据的必要余项：若q|r，则该缺口已有普通Type II双尾，不能属于输入遗漏集。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- type-II
- terminal-bridge
- p-minus-one
- b1
- overlap
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-and-Type-II-certificate-context
visibility: public
last_checked: '2026-07-28'
---

# 五亿普通尾遗漏中的 B 等于 1 终端桥重叠剖面

输入是完整的五亿普通 Type II 双尾遗漏集，以及该集上所有 \(B=1\)、\(m\le215\) Type I
正规形最大尾偶源边中按源距离选择的首边。后者有 1,713 条记录，另有四个点在该 \(B=1\) 盒内
没有偶源边。

对每条选中的 \(p-1\) 源边，写

\[
q=\frac{m+1}{4},\qquad r=\frac{R+1}{4}.
\]

因为源为 \(p-1\)，桥因子必为 \(E=R+1=4r\)。一般重叠判据表明：若 \(q\mid r\)，则同一
缺口直接有普通 Type II 双尾；这与输入是完整普通尾遗漏相矛盾。

精确重建得到：

| 选中桥类别 | 数量 |
| --- | ---: |
| 源为 \(p-1\)，且 \(q\nmid r\) | 1,400 |
| 其它偶源 | 313 |
| \(B=1\) 盒内遗漏 | 4 |

例如首个 \(p-1\) 类记录为

\[
p=67369,\quad m=35,\quad R=47,\quad E=48,\quad
(q,r)=(9,12),
\]

故 \(9\nmid12\)。这一点属于完整普通尾遗漏集，说明 \(q\nmid r\) 的余项可以是真正需要
Type I 分支的状态，而不仅是形式上的可能性。

这份剖面只描述每个点按源距离选出的 \(B=1\) 桥；它不排除同一点还存在别的桥，也不证明
\(q\nmid r\) 足以使普通 Type II 尾失败。它的用途是把下一阶段的 \(p-1,B=1\) 因子状态
准确收缩到 \(q\nmid r\) 的部分。

可复现命令：

~~~bash
python3 reproductions/type_i_b1_terminal_overlap_profile.py
python3 -m unittest tests/test_type_i_b1_terminal_overlap_profile.py -q
~~~
