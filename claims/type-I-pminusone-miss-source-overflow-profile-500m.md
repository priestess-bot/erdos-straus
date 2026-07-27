---
kind: claim
claim_id: type-I-pminusone-miss-source-overflow-profile-500m
title: 五亿p减一遗漏最短源状态的三级指数溢出边界
statement: 在五亿p减一桥遗漏的185个最短上半区源状态中，119个有B=1的Type I正规形实现；其余66个全部是B=1有限积集障碍而非子群障碍。对这66个状态完整枚举F|K^2的正规形实现后，最小指数溢出为1、2、3的个数分别为63、2、1；唯一三级溢出边界为p=229474249，其最小实现B=12。因此先前压力样本中“一或两次指数溢出足够”的现象不随源状态重选保持。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- p-minus-one
- upper-half-source
- source-state
- normal-form
- finite-product
- exponent-overflow
- selector-boundary
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-terminal-bridge-context
visibility: public
last_checked: '2026-07-28'
---

# 五亿 p减一遗漏最短源状态的三级指数溢出边界

输入为 [p减一遗漏最短上半区源剖面](type-I-pminusone-miss-upper-half-profile-500m.md) 的全部

\[
185
\]

个记录。它们是普通 Type II \(p-1\) 双尾遗漏中不能使用 \(p-1\) Type I 桥的点；每个记录
已在同一 \(p\le5\cdot10^8,m\le215\) 正规形盒内选为最短上半区偶源。

对每个已选源状态 \((p,n,E)\)，令

\[
s=p-n,\qquad R=\frac{E-1}{s},\qquad K=\frac{pR+1}{4}.
\]

先以 [源状态实现判据](type-I-normal-source-state-realization.md) 重枚举全部正常形。\(B=1\)
分支等价于 \(K\) 有一个除子属于 \(-1/4\pmod R\)。对该分支的每个遗漏，再完整枚举

\[
F\mid K^2,\qquad 4F\equiv-1\pmod R,
\]

并从 \(F\) 的超出 \(K\) 的指数部分恢复 \(B,C,A,m\)。指数溢出计数为

\[
\sum_q\max\{0,v_q(F)-v_q(K)\}.
\]

所有中间状态与目标、源两边的单位分数恒等式均以整数和有理数重建。

## 结果

| 项目 | 数值 |
| --- | ---: |
| 最短源状态 | 185 |
| \(B=1\) 实现 | 119 |
| \(B=1\) 遗漏 | 66 |
| 子群障碍 | 0 |
| 有限积集/指数障碍 | 66 |
| 最小溢出为 1 | 63 |
| 最小溢出为 2 | 2 |
| 最小溢出为 3 | 1 |

唯一的三级指数溢出边界是

\[
p=229\,474\,249,\qquad R=359,\qquad E=248\,788.
\]

它的最小正常形实现有 \(B=12\)。更精确地，

\[
K=2^3\cdot3\cdot37\cdot41\cdot67\cdot8443,
\qquad F=19296=2^5\cdot3^2\cdot67.
\]

故 \(F\) 相对 \(K\) 的指数缺额为 \(2+1=3\)。因此，先前两个固定压力集上“\(B=1\)
失败最多只需两次已有因子的指数溢出”并不是对动态最短源状态稳定的规律。

## 含义与边界

这不是混合终端选择引理的反例：185 个点均仍有 Type I 上半区桥。它排除的是一个更窄的
推进设想，即希望从任意自然选取的源状态出发，用至多两次指数溢出统一实现正规形。

因而下一步不能只控制“目标残数是否进入 \(K^2\) 的除子积集”；还必须解释如何重选源状态，
或在溢出超过固定阈值时强制不同的 Type I/II 出口。

重建命令：

~~~bash
python3 reproductions/type_i_pminusone_miss_source_overflow_profile.py
python3 -m unittest tests/test_type_i_pminusone_miss_source_overflow_profile.py -q
~~~
