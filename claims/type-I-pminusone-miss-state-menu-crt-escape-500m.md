---
kind: claim
claim_id: type-I-pminusone-miss-state-menu-crt-escape-500m
title: p减一遗漏的127个上半区源状态菜单存在CRT逃逸
statement: 取五亿 p-1 桥遗漏的最短上半区源剖面所出现的127个不同(s,E)状态，其中s=p-n。令M为24与所有精确源平方模数Lambda(E)的最小公倍数，则p=1 modM是一条互素核心素数等差数列，且对每个菜单状态均不满足必要同余p=s modLambda(E)。故由Dirichlet定理，无穷多个核心素数不能通过这127个固定源状态中的任何一个获得 Type I 偶桥；该菜单不能成为全称混合终端选择器。
claim_status: established
proof_provenance: mixed
review_status: internal_review
topics:
- type-I
- p-minus-one
- upper-half-source
- source-state
- CRT
- Dirichlet-theorem
- obstruction
- selector-boundary
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-source-square-bridge-context
visibility: public
last_checked: '2026-07-28'
---

# p减一遗漏的127个上半区源状态菜单存在CRT逃逸

从 [p减一遗漏最短上半区源剖面](type-I-pminusone-miss-upper-half-profile-500m.md)取全部最短见证，
按源距离和桥因子去重：

\[
(s,E),\qquad s=p-n.
\]

得到 127 个不同状态。它们不是任意构造的模板，而是五亿 \(p-1\) 桥遗漏中实际出现的全部
最短上半区桥状态。

对每个偶桥因子 \(E\)，令 \(\Lambda(E)\) 为
[源平方桥的精确同余模数](type-I-source-square-congruence-modulus.md)。任何采用该固定状态的
Type I 桥都必须满足

\[
E\mid\frac{(p-s)^2}{\gcd(E,4)}
\quad\Longleftrightarrow\quad
p\equiv s\pmod {\Lambda(E)}. \tag{1}
\]

令

\[
M=\operatorname{lcm}\left(24,\{\Lambda(E):(s,E)\text{ 属于菜单}\}\right).
\tag{2}
\]

精确计算得到

\[
\begin{aligned}
M={}&2080306690880112911627043480372055466498254845814600878125160845151388442289457977201336185446412604853253476693259227259242633578576000.
\end{aligned}
\tag{3}
\]

对全部 127 个状态都直接验证

\[
1\not\equiv s\pmod {\Lambda(E)}. \tag{4}
\]

因此，任意

\[
p\equiv1\pmod M \tag{5}
\]

都满足 \(p\equiv1\pmod {24}\)，且不满足菜单中任何一个必要条件 (1)。由于 \(1\) 与 \(M\)
互素，Dirichlet 关于算术级数素数的定理给出无穷多个满足 (5) 的素数。对于充分大的这些
素数，各 \(p-s\) 都为正，但没有一个固定菜单状态通过源平方条件，因而更不可能继续通过
正规形的因子对实现条件。

## 含义与边界

这严格排除一个看似自然的收缩：把 p减一遗漏实际观测到的 127 个最短上半区状态固定为
全称 Type I 选择器。其失败发生在任何 \(BC\mid K\) 的正规形实现之前，故不能用换同一状态的
正规形补救。

它不排除 \((s,E)\) 随 \(p\) 自适应变化，不排除菜单外的 Type I 桥，也不排除普通 Type II
双尾。因此全称证明仍须给出状态依赖的、非固定菜单选择规律或真正的可提升递降。

重建命令：

~~~bash
python3 reproductions/type_i_pminusone_miss_state_menu_crt_escape.py
python3 -m unittest tests/test_type_i_pminusone_miss_state_menu_crt_escape.py -q
~~~
