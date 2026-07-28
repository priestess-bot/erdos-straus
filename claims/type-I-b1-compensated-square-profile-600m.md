---
kind: claim
claim_id: type-I-b1-compensated-square-profile-600m
title: 六亿 B 等于一自平方残余的补偿平方剖面
statement: 对m<=999的B=1自平方重选后留下的57个冻结压力点，完整枚举同一B=1目标盒和每个补因子H的平方除子T；补偿平方桥闭合36点，余21点。累计该有限流程闭合1964点中的1943点；21点仍不是全称反例或其他终端机制的失败证明。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- b1
- compensated-square
- terminal-bridge
- pressure-set
- computational-profile
- residual
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 六亿 \(B=1\) 自平方残余的补偿平方剖面

输入为 [\(m\le999\) 自平方正规形重选](type-I-b1-self-square-reselection-profile-600m.md) 留下的
57 个点。对每个点，完整枚举相同 \(m\le999\) 目标盒中的 \(B=1\) 正规形；再对每张形式的
\(H^2\) 的每个除子 \(T\)，检查

\[
T\equiv4\pmod R,
\qquad q=(H-CT)/R>0,
\qquad T\mid qH. \tag{1}
\]

命中后以 \(E=4C^2T\) 重放目标和源的单位分数恒等式。

| 项目 | 数量 |
| --- | ---: |
| 输入自平方残余 | 57 |
| 补偿平方闭合 | 36 |
| 补偿平方残余 | 21 |
| 已检 \(B=1\) 正规形 | 447 |
| 已检 \(H^2\) 除子 | 19,465 |
| 合格候选 | 151 |
| 所选源位于上半区 | 20 |
| 最大所选缺口 | 991 |

因此，按“\(m\le999\) 自平方重选，再在其 57 个残余上作补偿平方重选”的固定有限流程，共有

\[
1{,}907+36=1{,}943
\]

个压力点闭合，留下 21 个。这 21 个点只与仓库中另一条“全正规形 \(p-1\) 桥失败”清单交叠
两个素数；相同计数不代表相同障碍，故不能把这两条有限结果合并为全称结论。

本剖面没有枚举 \(m>999\)、一般 \(B\)、不同线性源或 Type II 结构。其作用是把 \(B=1\)
补因子平方路线的下一残余明确缩小到 21 点，而不是证明它们没有其他证书。

复现：

~~~bash
python3 reproductions/type_i_b1_compensated_square_profile_600m.py
python3 -m unittest tests.test_type_i_b1_compensated_square_profile_600m -q
~~~
