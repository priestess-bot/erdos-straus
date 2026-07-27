---
kind: claim
claim_id: type-I-b4-prefix-boundary-21169
title: B不大于4最大尾偶源选择器的首个失败点
statement: 对全部p≤21169的281个核心素数，穷尽每个p的自然Type I缺口、B≤4正规形及p倍最大尾的严格反向桥。280个素数均有严格偶源边，唯一遗漏为p=21169。因此21169是该B≤4最大尾偶源选择器的首个失败点；结合其完整正规形审计，它的最小偶源参数为B=5。
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

# B 不大于 4 最大尾偶源选择器的首个失败点

对每个核心素数 \(p\le21169\)，穷尽

\[
3\le m\le p-2,\quad m\equiv3\pmod4,
\]

以及所有 \(B\le4\) 的 Type I 正规形；对每张正规形再穷尽 \(pK\) 最大尾的严格反向桥并要求
源分母为偶数。结果为：

| 项目 | 数值 |
|---|---:|
| 核心素数 | 281 |
| 有 \(B\le4\) 严格偶源边 | 280 |
| 遗漏 | \(21169\) |

因此 \(p=21169\) 是这个完整前缀中第一个、也是唯一一个逃过固定菜单
\(B\in\{1,2,3,4\}\) 的目标。由其[完整正规形偶源边界](type-I-full-normal-even-source-boundary-21169.md)，
该点并非没有 Type I 偶源递降，而是最小参数恰为 \(B=5\)。

这排除了“把最大尾严格偶源递降统一限制到 \(B\le4\)”的全局引理。它不证明后续点仍只需要
\(B=5\)，也不证明最小 \(B\) 无界；这正是下一步应当分析的因子残数复杂度。

可复现命令：

~~~bash
python3 reproductions/type_i_b4_prefix_boundary_21169.py
python3 -m unittest tests/test_type_i_b4_prefix_boundary_21169.py -q
~~~
