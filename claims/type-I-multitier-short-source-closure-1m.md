---
kind: claim
claim_id: type-I-multitier-short-source-closure-1m
title: 百万前缀的Type I多层短源闭合
statement: 对p不大于1000009的9732个核心素数，按四层选择器依次闭合：完整二幂p减一桥9149点、固定12项非二幂E菜单的B属于{1,2}的p减一桥555点、E不大于10^6的源平方允许全因子对p减一桥25点、以及三个B=1的短一般源边3点。故该前缀全部闭合；所选见证中E最大576，B最大435，源距离最大25。该结论严格限于此有限审计，不给出全称界。
claim_status: computationally_reproduced
topics:
- type-I
- normal-form
- descent
- even-source
- factorization
- dyadic
- selector
- finite-audit
- closure
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 百万前缀的 Type I 多层短源闭合

对每个

\[
p\le1{,}000{,}009,\qquad p\equiv1\pmod{24},
\]

按下列顺序应用精确因子对选择器：

| 层 | 机制 | 新闭合点数 |
|---|---|---:|
| 1 | 完整允许二幂 \(E=2^t\) 的 \(n=p-1\) 因子对 | 9,149 |
| 2 | 固定 \(E\) 菜单、\(B\in\{1,2\}\)、\(n=p-1\) | 555 |
| 3 | 所有 \(E\le10^6\) 且 \(E\mid(p-1)^2/4\) 的完整 \(BC\mid K\) 对、\(n=p-1\) | 25 |
| 4 | 最终三点的全部自然缺口、\(B\le4\) 一般源审计 | 3 |

总数为

\[
9149+555+25+3=9732. \tag{1}
\]

最后三点的按源距离最优边为

\[
\begin{array}{c|c|c|c|c}
p & n & p-n & E & B\\ \hline
297049 & 297024 & 25 & 476 & 1\\
513529 & 513520 & 9 & 280 & 1\\
710089 & 710080 & 9 & 280 & 1
\end{array}
\]

所有被选见证均有严格更小偶源；合成后的实际最大参数为

\[
E\le576,\qquad B\le435,\qquad p-n\le25. \tag{2}
\]

这不是关于所有素数的统一定理。第 3 层的扫描上界是 \(10^6\)，而第 4 层只对前述三点完整；
特别地，(2) 是对该百万前缀的观测到的、经逐条证书验证的上界，不可外推为全局界。它的价值在于：
此前彼此独立的二幂桥、低 \(B\) 非二幂菜单、较复杂 \(p-1\) 因子对与短外源边现在形成了一个
无重叠的有限闭合链。

可复现命令：

~~~bash
python3 reproductions/type_i_joint_residual_general_edge_profile_1m.py
python3 reproductions/type_i_multitier_short_source_closure_1m.py
python3 -m unittest \
  tests/test_type_i_joint_residual_general_edge_profile_1m.py \
  tests/test_type_i_multitier_short_source_closure_1m.py -q
~~~
