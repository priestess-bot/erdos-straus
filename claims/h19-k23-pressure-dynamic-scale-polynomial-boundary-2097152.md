---
kind: claim
claim_id: h19-k23-pressure-dynamic-scale-polynomial-boundary-2097152
title: H19-k23 压力进程自然增长尺度的多项式平方尾边界
statement: 对 H19-k23 压力进程 p(t)=748375048866405601+P*t，令 G=41400、h(t)=(p(t)-1)/(4G)，取参数增长的标准外部源尺度 k=h(t)。源精确为 p(t)-G，且 M(t)=h(t)(p(t)-G)。h 与 p-G 均为本原且互异的一次整系数多项式。穷尽 M(t)^2 的全部最终不超过M(t)的整系数多项式因子后，仅有5个候选，均不满足 e(t)=-M(t) mod(4h(t)-1)。故这个自然动态尺度没有统一多项式平方尾严格递降。
claim_status: computationally_reproduced
topics:
- type-I
- external-source
- dynamic-scale
- polynomial-factors
- strict-descent
- pressure-family
- h19
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: external-source-descent
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 压力进程自然增长尺度的多项式平方尾边界

取压力进程

\[
p(t)=748375048866405601+Pt,\qquad G=41400, \tag{1}
\]

并定义随参数增长的尺度

\[
h(t)=\frac{p(t)-1}{4G},\qquad k(t)=h(t). \tag{2}
\]

因为 (p=4Gh+1)，相应标准外部源精确化简为

\[
\frac{(4h-1)p+1}{4h}=p-G. \tag{3}
\]

令

\[
M(t)=h(t)(p(t)-G),\qquad q(t)=4h(t)-1. \tag{4}
\]

完整平方尾递降需要

\[
e(t)\mid M(t)^2,\qquad e(t)\le M(t),\qquad e(t)\equiv-M(t)\pmod {q(t)}. \tag{5}
\]

这里 (h) 与 (p-G) 都是内容为一、彼此不伴随的一次整系数多项式。因此在
\(\mathbb Z[t]\) 的唯一分解中，任意多项式因子都形如

\[
h(t)^a(p(t)-G)^b,\qquad 0\le a,b\le2. \tag{6}
\]

最终大小条件排除次数大于二的项，也排除 ((p-G)^2)，后者的二次主系数严格大于
\(M\) 的主系数。剩下恰好五项：

\[
1,quad h,quad p-G,quad h^2,quad h(p-G). \tag{7}
\]

将每一项代入 (5)，以 (q) 的有理根直接计算余式，五项均非零。故没有统一整系数
多项式平方尾。

这条边界仅针对这个自然增长尺度及多项式因子。它不排除从 (p-G) 选择非多项式的实际
因子，不排除其它参数增长尺度，也不排除平移、Type II 或不同递降状态。

可复现命令：

~~~bash
python3 reproductions/h19_k23_pressure_dynamic_scale_polynomial_boundary.py \
  --input reproductions/h19-k23-global-tail-pressure-external-source-bridge-2097152.json \
  --output reproductions/h19-k23-pressure-dynamic-scale-polynomial-boundary-2097152.json
python3 -m unittest tests/test_h19_k23_pressure_dynamic_scale_polynomial_boundary.py -q
~~~
