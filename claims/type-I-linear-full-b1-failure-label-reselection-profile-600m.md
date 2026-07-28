---
kind: claim
claim_id: type-I-linear-full-b1-failure-label-reselection-profile-600m
title: 六亿压力集中全谱 B 等于一失败点的三标签重选剖面
statement: 在200个首达B>1的完整线性压力谱中，18个素数没有任何B=1目标命中。对这18个真正全谱B=1失败点再次完整枚举所有线性源及一般B命中，并按完整谱标签层分解重选：3点一层、14点两层、1点三层，均不需四层；唯一三层点仍是p=26034649。这把三层重选的有限支持从三千万尾遗漏扩展到六亿压力集中最严格的B>1残余，但不证明全称选择器。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- b-equals-one
- reselection
- coordinate-label
- target-square-divisor
- exhaustive-computation
- terminal-bridge
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 六亿压力集中全谱 B 等于一失败点的三标签重选剖面

## 审计对象

[两百个首达 \(B>1\) 线性证书的完整谱重选剖面](type-I-linear-b-gt-one-full-spectrum-profile-600m.md)
已经把 200 个首达 \(B>1\) 记录分为 182 个可重选 \(B=1\) 的点和 18 个完整谱中没有任何
\(B=1\) 目标的点。本页只研究后者；它们是该六亿冻结压力集里一般 \(B\) 真正不可由 \(B=1\)
替代的部分。

对每个素数完整重建 (1)

\[
p=a+s+asR,
\qquad s\equiv1\pmod2,
\qquad R\equiv3\pmod4, \tag{1}
\]

并对每个一般 \(B\) 目标命中，把

\[
K=G_cG_pL_cL_p \tag{2}
\]

按这个**完整源谱**的坐标标签差分为源碰撞、源私有、仿射碰撞、仿射私有四层。对所有 15 个
非空子积直接检查中心化平方除子谱是否含 \(-1\)，再按层数与 \((R,a,s)\) 字典序重选。

## 结果

18 个严格 \(B=1\) 失败点全都保有一般 \(B\) 命中，重选层数为

| 最短层数 | 素数数 |
| ---: | ---: |
| 1 | 3 |
| 2 | 14 |
| 3 | 1 |
| 4 | 0 |

唯一三层点仍是

\[
p=26{,}034{,}649,
\qquad(R,a,s)=(187,15460,9), \tag{3}
\]

其唯一最短层子集为源私有、仿射碰撞、仿射私有。此前已知的四层固定状态边界没有在这些真正
\(B=1\) 残余的“存在一个源”量词下重现。

每张选中证书仍逐项满足

\[
E=sR+1,
\qquad 2\mid E,
\qquad E\mid4K^2,
\qquad E\equiv1\pmod R,
\qquad E\le4K-2R. \tag{4}
\]

故该剖面是混合终端选择引理的严格有限证据，而不只是标签支持统计。

## 含义与范围

这把三层重选候选的压力测试从三千万内 200 个普通双尾遗漏，推进到六亿闭合中最具对抗性的
18 个“全谱无 \(B=1\)”残余。它特别说明：在该有限集中，必须使用一般 \(B\) 并不意味着要
使用四个标签层。

然而完整有限谱仍不能限制未来核心素数。全称猜想可能在更大处出现“所有命中均需四层”或根本
没有线性一般 \(B\) 命中。证明仍需要跨源碰撞、角色和有限指数障碍的共同结构，而不是重复这个
有限统计。

## 复现

~~~bash
python3 reproductions/type_i_linear_full_b1_failure_label_reselection_profile_600m.py
python3 -m unittest tests.test_type_i_linear_full_b1_failure_label_reselection_profile_600m -v
~~~
