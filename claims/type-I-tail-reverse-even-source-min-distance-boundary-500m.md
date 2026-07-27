---
kind: claim
claim_id: type-I-tail-reverse-even-source-min-distance-boundary-500m
title: 五亿普通双尾遗漏的最短 Type I 偶源距离边界
statement: 对 p<=500000000 的 1,717 个普通 Type II 双尾遗漏，完整枚举 m<=215 的所有 Type I 正规形及每张正规形的严格最大尾反向提升；每点均有偶源桥。若 s=p-n 为所选偶源距离，则精确最小化 s 后，1,645 点有 s<=29，最大最小距离为 48,244,917。因此此有限盒中的一般偶源机制不能约化为固定短距离菜单。
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
last_checked: '2026-07-28'
---

# 五亿普通双尾遗漏的最短 Type I 偶源距离边界

对 [五亿普通尾遗漏](type-I-tail-reverse-even-source-closure-500m.md) 的每个
\(p\)，完整枚举

\[
3\le m\le215,\qquad m\equiv3\pmod4,
\]

内的全部 Type I 正规形，以及每张正规形的全部严格最大尾反向提升。只保留偶源
\(n\)，并在每个 \(p\) 上精确最小化

\[
s=p-n.
\tag{1}
\]

这与按 \(E\) 的素因子支持选择见证不同；本审计直接检验“是否存在真正短的可用源”。

## 结果

| 项目 | 数值 |
|---|---:|
| 普通 Type II 双尾遗漏 | 1,717 |
| 完整枚举的 Type I 正规形 | 78,215 |
| 严格反向提升 | 166,089 |
| 有偶源桥的点 | 1,717 |
| 无偶源桥的点 | 0 |
| 最短源距离 \(s\le29\) 的点 | 1,645 |
| 最大最短源距离 | 48,244,917 |

最短距离的精确分桶为

\[
1645_{\le29}+45_{\le1000}+18_{\le p/1000}
+2_{\le p/100}+7_{\le p/10}=1717.
\tag{2}
\]

最大值发生在

\[
p=493936249,\quad
s=48244917,\quad
m=215,\quad
(A,B,C)=(21,1,5880196).
\tag{3}
\]

因此 \(s\le29\) 在该压力集上覆盖约 \(95.8\%\)，但不是完整有限盒中的选择定理。
特别地，任何试图把 Type I 偶源分支固定为有限短移位菜单的证明路线，必须处理 (2)
中的长尾，而不能从短源集中性推出全称界。

## 边界

这是在 \(p\le500000000\)、\(m\le215\) 和所述严格最大尾提升内的精确有限审计。
它没有给出 \(s\) 的无穷全称上界，也没有证明最短源距离随 \(p\) 的增长规律；更大缺口、
其他 Type I 坐标和 Type II 机制仍未被排除。

可复现命令：

~~~bash
python3 reproductions/type_i_tail_reverse_even_source_min_source_distance.py
python3 -m unittest tests/test_type_i_tail_reverse_even_source_min_source_distance.py -q
~~~
