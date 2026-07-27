---
kind: claim
claim_id: type-I-b5-maximum-tail-even-source-closure-10m
title: 一千万核心素数的B不大于5最大尾偶源闭合
statement: 对所有p≤10000009的82887个核心素数，完整枚举自然Type I缺口、B≤4正规形和最大尾严格偶源反向边；82886个直接命中，唯一遗漏为21169。该点的完整正规形审计证明其最小偶源参数为B=5。因此在此范围每个核心素数均有B≤5的最大尾保留两项严格偶源Type I反向边，且B≤4仅在21169失败。
claim_status: computationally_reproduced
topics:
- type-I
- normal-form
- descent
- even-source
- overflow
- finite-audit
- closure
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 一千万核心素数的 B 不大于 5 最大尾偶源闭合

完整审计所有

\[
p\le10{,}000{,}009,\qquad p\equiv1\pmod{24}
\]

的 82,887 个核心素数。在每个目标上穷尽自然 Type I 缺口、所有 \(B\le4\) 正规形与
\(pK\) 最大尾的严格偶源反向桥，结果为

\[
82887=82886_{B\le4}+1_{p=21169}. \tag{1}
\]

唯一的 \(B\le4\) 遗漏为 \(p=21169\)。其[完整正规形偶源边界](type-I-full-normal-even-source-boundary-21169.md)
给出 \(m=4071,(A,B,C)=(1,5,1262)\) 的严格偶源边，并证明所有 \(B\le4\) 均失败。
因此合成得到

\[
\boxed{\text{对该一千万前缀，存在 }B\le5\text{ 的最大尾保留两项严格偶源 Type I 反向边。}} \tag{2}
\]

这是一个强的有限覆盖谱，而不是全称定理：它既不控制一千万之外所需的 \(B\)，也不提供从
\((p,m,A,B,C)\) 自适应选取证书的解析规则。它的价值在于把先前的“小 \(B\)”观察提升为一个
完整、带唯一低菜单异常的严格递降闭合。

可复现命令：

~~~bash
python3 reproductions/type_i_b4_prefix_profile_10m.py
python3 -m unittest tests/test_type_i_b4_prefix_profile_10m.py -q
~~~
