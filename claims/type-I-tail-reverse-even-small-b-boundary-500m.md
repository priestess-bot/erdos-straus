---
kind: claim
claim_id: type-I-tail-reverse-even-small-b-boundary-500m
title: 五亿普通双尾遗漏的偶源 B=8 精确低溢出边界
statement: 对 p<=500000000 的 1,717 个普通 Type II 双尾遗漏，完整枚举 m<=215、B<=8 的 Type I 正规形及严格最大尾反向提升，并显式验证偶桥 E 的整除、同余和大小条件；全部命中。B<=7 时恰遗漏 p=172657489，故 B=8 是该有限盒中此偶源选择器的最小全覆盖上界。
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

# 五亿普通双尾遗漏的偶源 \(B=8\) 精确低溢出边界

对每个普通 Type II 双尾遗漏，完整枚举

\[
3\le m\le215,\qquad m\equiv3\pmod4,\qquad B\le B_0,
\]

的 Type I 正规形及其所有严格最大尾反向提升。只接受偶源，并对每条候选显式核对

\[
E\mid4K^2,\qquad E\equiv1\pmod R,\qquad E\le4K-2R,\qquad2\mid E. \tag{1}
\]

## 精确边界

| \(B_0\) | 偶源命中 | 遗漏 |
|---:|---:|---|
| 7 | 1,716 | \(172657489\) |
| 8 | 1,717 | 无 |

因此 \(B=8\) 是这个有限盒内的最小全覆盖上界。阈值点 \(p=172657489\) 在

\[
(m,A,B,C)=(111,87025,8,62) \tag{2}
\]

有偶源桥，但在同一缺口盒的所有 \(B\le7\) 正规形中都没有偶源桥。

在 \(B\le8\) 的第一次命中顺序中，各 \(B\) 的记录数为

\[
1455,147,31,8,23,7,41,5
\quad(B=1,2,\ldots,8). \tag{3}
\]

这说明低溢出状态在有限压力集上极其有效，但
[B=1 边界](type-I-tail-reverse-b1-even-source-boundary-500m.md) 已表明它不能退化为单一
除子残数条件；状态切换至少要允许到 \(B=8\)。

## 边界

这是 \(p\le500000000,m\le215\) 内的精确计算结论，不提供对所有核心素数的 \(B\) 上界。
特别地，它不排除 \(B\) 或 \(m\) 在更大目标上增长，也没有给出从 \(p\) 的因子数据选择
\(B\) 的全称规则。

可复现命令：

~~~bash
python3 reproductions/type_i_tail_reverse_small_b_profile.py \
  --gap-cap 215 --b-cap 7 --even-source-only \
  --output reproductions/type-i-tail-reverse-even-small-b7-500m-results.json
python3 reproductions/type_i_tail_reverse_small_b_profile.py \
  --gap-cap 215 --b-cap 8 --even-source-only \
  --output reproductions/type-i-tail-reverse-even-small-b8-500m-results.json
python3 -m unittest tests/test_type_i_tail_reverse_small_b_profile.py -q
~~~
