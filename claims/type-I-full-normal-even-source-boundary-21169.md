---
kind: claim
claim_id: type-I-full-normal-even-source-boundary-21169
title: p等于21169的完整Type I正规形偶源边界
statement: 对核心素数p=21169穷尽所有3≤m≤21167、m=3 mod4的Type I正规形及其p倍最大尾的全部严格反向桥。共得19张正规形、20条严格反向边、19条偶源边；偶源边的最小正规形参数为B=5，首次由m=4071、(A,B,C)=(1,5,1262)给出。故该点没有任何B≤4的最大尾严格偶源Type I反向边。
claim_status: computationally_reproduced
topics:
- type-I
- normal-form
- descent
- even-source
- overflow
- finite-audit
- boundary
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# p 等于 21169 的完整 Type I 正规形偶源边界

令 \(p=21169\)。对全部自然缺口

\[
3\le m\le p-2=21167,\qquad m\equiv3\pmod4,
\]

枚举 \(x=(p+m)/4\) 的每个平方除子，按 Type I 条件归一化为所有 \((A,B,C)\)，并对每张
正规形的 \(pK\) 最大尾穷尽 \(E\mid4K^2\) 所给的严格反向边。

| 项目 | 数值 |
|---|---:|
| Type I 正规形 | 19 |
| 严格最大尾反向边 | 20 |
| 严格偶源边 | 19 |
| 偶源边最小 \(B\) | 5 |

所有正规形的 \(B\) 分布为

\[
1,5,6,7,9,14,17,19,20,26,45,59,71,82,136
\]

（按出现次数计数见结果档案）；其中没有 \(B=2,3,4\)。最小 \(B\) 的两条偶源边共同来自

\[
m=4071,\qquad(A,B,C)=(1,5,1262),
\]

且源分母分别为 \(21060\) 与 \(21168\)。因此

\[
\text{不存在 }B\le4\text{ 的最大尾保留两项严格偶源 Type I 反向边。} \tag{1}
\]

这把先前的 \(B=1\) 边界提升为对固定小菜单 \(B\le4\) 的精确单点反例。它并未说明最小
\(B\) 无界，也没有排除改坐标、Type II 或非最大尾的递降；其作用是排除将全局引理建立在固定
低 \(B\) 最大尾选择器上的路线。

可复现命令：

~~~bash
python3 reproductions/type_i_full_normal_even_source_boundary_21169.py
python3 -m unittest tests/test_type_i_full_normal_even_source_boundary_21169.py -q
~~~
