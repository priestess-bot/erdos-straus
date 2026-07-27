---
kind: claim
claim_id: h19-k23-pressure-even-source-seed-profile-2097152
title: H19-k23 压力种子距离一偶源扇的严格递降
statement: 压力种子 p=748375048866405601 虽在自然动态标准源 p-41400 上没有完整平方尾，但其距离一偶源 p-1 有严格递降。完整枚举距离一偶源的兼容因子射线至第11条命中：shift=22595865002005、r=33119、k=187088113250350899、平方尾因子 e1=574459478468352。相应源/目标三分式恒等式与 Type I 证书均精确核验，源分母 p-1 严格小于p。
claim_status: computationally_reproduced
topics:
- type-I
- even-source
- strict-descent
- factorization
- pressure-family
- h19
sources:
- paper: bradford2024
  locator: Proposition 1
  role: even-source-descent
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 压力种子距离一偶源扇的严格递降

对压力种子

\[
p=748375048866405601,
\]

取距离 (c=1)，源分母为严格更小的偶数 (p-1)。完整偶源参数化在一个因子
`shift` 上要求

\[
s=\frac{p-1}{\operatorname{shift}}=1+r,\qquad
k=\frac{\operatorname{shift}\,r+1}{4},\qquad M_1=ks. \tag{1}
\]

对每条兼容射线，完整平方尾条件是

\[
e_1\mid M_1^2,\qquad e_1\le M_1,\qquad e_1\equiv-M_1\pmod r. \tag{2}
\]

按 `shift` 递增穷尽兼容射线，在第 11 条得到

\[
\begin{aligned}
\operatorname{shift}&=22595865002005,\\
r&=33119,\\
k&=187088113250350899,\\
M_1&=6196358310851621774880,\\
e_1&=574459478468352.
\end{aligned} \tag{3}
\]

由此得到

\[
u=187093779561916128,\qquad
v=2018071142264194029458820. \tag{4}
\]

程序直接以有理数验证

\[
\frac4{p-1}
=\frac1{\operatorname{shift}M_1}+\frac1u+\frac1v,
\qquad
\frac4p
=\frac1{pM_1}+\frac1u+\frac1v. \tag{5}
\]

恢复的 Type I 证书具有

\[
m=69381258911,\qquad
D=60933945148041112092. \tag{6}
\]

因此此前自然动态标准源的失败并不使该种子接近反例：切换到 (p-1) 的偶源状态后，
已有明确的严格递降。此结论只针对一个种子，未证明距离一偶源扇对整条压力进程全称覆盖。

可复现命令：

~~~bash
python3 reproductions/h19_k23_pressure_even_source_seed_profile.py \
  --input reproductions/h19-k23-global-tail-pressure-external-source-bridge-2097152.json \
  --output reproductions/h19-k23-pressure-even-source-seed-profile-2097152.json
python3 -m unittest tests/test_h19_k23_pressure_even_source_seed_profile.py -q
~~~
