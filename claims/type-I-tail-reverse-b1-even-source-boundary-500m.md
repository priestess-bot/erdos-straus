---
kind: claim
claim_id: type-I-tail-reverse-b1-even-source-boundary-500m
title: 五亿普通双尾遗漏的 B=1 偶源桥边界
statement: 对 p<=500000000 的 1,717 个普通 Type II 双尾遗漏，完整枚举 m<=215 的全部 B=1 Type I 正规形及严格最大尾反向提升；仅 1,713 点有偶源桥，四个遗漏为 39407449、63332329、172657489、193288489。因此 B=1 单除子剩余类选择器不是此完整有限盒的充分终端选择器。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- type-II
- normal-form
- even-source
- descent
- divisor-residues
- selector-boundary
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I normal-form context
visibility: public
last_checked: '2026-07-28'
---

# 五亿普通双尾遗漏的 \(B=1\) 偶源桥边界

对 [五亿普通尾遗漏](type-I-tail-reverse-even-source-closure-500m.md) 的每个 \(p\)，完整枚举

\[
3\le m\le215,\qquad m\equiv3\pmod4,
\]

内所有 \(B=1\) 的 Type I 正规形，以及每张正规形的所有严格最大尾反向提升。保留偶源
\(n\)，并以 \(p-n\) 最小化同一 \(p\) 的见证。

## 结果

| 项目 | 数值 |
|---|---:|
| 普通 Type II 双尾遗漏 | 1,717 |
| 检查的 \(B=1\) 正规形 | 15,071 |
| 检查的严格反向提升 | 126,178 |
| 有 \(B=1\) 偶源桥的点 | 1,713 |
| 无 \(B=1\) 偶源桥的点 | 4 |

四个完整遗漏为

\[
39407449,\quad63332329,\quad172657489,\quad193288489. \tag{1}
\]

它们在同一 \(m\le215\) 完整 Type I 盒中仍都有偶源桥；按最短源距的见证分别是

\[
\begin{array}{c|c|c|c}
p & p-n & (m,B,C) & E\\ \hline
39407449 & 7 & (87,2,2126) & 2738\\
63332329 & 1 & (31,2,91) & 48\\
172657489 & 1 & (111,8,62) & 144\\
193288489 & 1 & (103,4,37) & 24
\end{array} \tag{2}
\]

故 \(B=1\) 的

\[
R\mid4C+1,\qquad C\mid K \tag{3}
\]

单除子残数条件不能单独证明混合终端选择引理。特别地，后三个反例已经有
\(n=p-1\)，所以把失败归因于源距离也不成立；必须允许内部 \(B\) 状态切换。

## 边界

这是对 \(p\le500000000\)、\(m\le215\) 的精确有限反例基准。它不说明任意核心素数是否存在
\(B=1\) 桥，也不排除在更大缺口或其它 Type I 坐标中出现 \(B=1\) 见证。

可复现命令：

~~~bash
python3 reproductions/type_i_tail_reverse_b1_even_source_audit.py
python3 -m unittest tests/test_type_i_tail_reverse_b1_even_source_audit.py -q
~~~
