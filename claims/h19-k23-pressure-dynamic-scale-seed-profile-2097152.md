---
kind: claim
claim_id: h19-k23-pressure-dynamic-scale-seed-profile-2097152
title: H19-k23 压力种子自然动态外部源的完整因子剖面
statement: 对压力种子 p=748375048866405601，取 G=41400 与自然动态尺度 h=(p-1)/(4G)=4519173000401，标准外部源为 p-G=748375048866364201。源乘积 M=h(p-G) 的完整分解为 7789*4519173000401*96081017956909。M^2 的27个除子仅给出15个模4h-1残数，目标 -M 不在其中，故此实际动态源不存在完整平方尾严格递降。
claim_status: computationally_reproduced
topics:
- type-I
- external-source
- dynamic-scale
- factorization
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

# H19-k23 压力种子自然动态外部源的完整因子剖面

在压力种子

\[
p=748375048866405601
\]

上，取 (G=41400) 及自然动态尺度

\[
h=\frac{p-1}{4G}=4519173000401. \tag{1}
\]

标准外部源为

\[
n=p-G=748375048866364201,\qquad M=hn. \tag{2}
\]

完整因子分解是

\[
M=7789\cdot4519173000401\cdot96081017956909. \tag{3}
\]

对应模数为 (q=4h-1)。程序穷尽 (M^2) 的所有 27 个除子，并按模 (q) 合并为 15 个
不同残数；目标

\[
-M\pmod q=13557519001202 \tag{4}
\]

不在该集合中。因此不存在

\[
e\mid M^2,\qquad e\le M,\qquad e\equiv-M\pmod q, \tag{5}
\]

从而该实际种子在这一自然动态外部源上没有完整平方尾严格递降。

这是一点上的完整因子结论，不能推出其它参数的同一动态源也失败；它也不排除其它增长尺度、
其它外部源、Type II 证书或不同递降状态。

可复现命令：

~~~bash
python3 reproductions/h19_k23_pressure_dynamic_scale_seed_profile.py \
  --input reproductions/h19-k23-global-tail-pressure-external-source-bridge-2097152.json \
  --output reproductions/h19-k23-pressure-dynamic-scale-seed-profile-2097152.json
python3 -m unittest tests/test_h19_k23_pressure_dynamic_scale_seed_profile.py -q
~~~
