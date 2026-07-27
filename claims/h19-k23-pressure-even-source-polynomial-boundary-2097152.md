---
kind: claim
claim_id: h19-k23-pressure-even-source-polynomial-boundary-2097152
title: H19-k23 压力进程距离一偶源扇的多项式平方尾边界
statement: 对 H19-k23 压力进程 p(t)=748375048866405601+P*t，写 p(t)-1=165600*h(t)，其中h为本原一次多项式。距离一完整偶源扇的兼容移位恰为 d 或 d*h(t)，其中d|165600且d=1 mod4，共18条多项式射线。逐射线穷尽 M1(t)^2 的全部最终不超过M1(t)的整系数多项式因子，共104563项，均不满足 e1(t)=-M1(t) mod r(t)。故尽管种子可由实际非多项式因子递降，整个距离一偶源扇没有统一多项式平方尾。
claim_status: computationally_reproduced
topics:
- type-I
- even-source
- polynomial-factors
- strict-descent
- pressure-family
- h19
sources:
- paper: bradford2024
  locator: Proposition 1
  role: even-source-descent
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 压力进程距离一偶源扇的多项式平方尾边界

对压力进程写作

\[
p(t)-1=B h(t),\qquad B=165600, \tag{1}
\]

其中 (h(t)) 是内容为一且恒为 (1pmod4) 的一次整系数多项式。距离一偶源有

\[
p(t)-1=\operatorname{shift}\,(1+r). \tag{2}
\]

若希望 `shift` 本身是统一多项式因子，则唯一可能是

\[
\operatorname{shift}=d\quad\hbox{或}\quad d h(t),\qquad
d\mid B,quad d\equiv1\pmod4. \tag{3}
\]

这给出 18 条兼容射线。每条具有

\[
k(t)=\frac{\operatorname{shift}\,r(t)+1}{4},\qquad
M_1(t)=k(t)(1+r(t)), \tag{4}
\]

其完整平方尾要求

\[
e_1(t)\mid M_1(t)^2,\qquad e_1(t)\le M_1(t),\qquad
e_1(t)\equiv-M_1(t)pmod {r(t)}. \tag{5}
\]

将 (4) 的固定内容与本原一次因子分离后，\(\mathbb Z[t]\) 的唯一分解穷尽 (5) 中所有
最终有界的整系数多项式候选。18 条射线合计检查

\[
104563
\]

项，没有任何同余命中。

这与种子上的正向见证并不矛盾：该见证的 (e_1) 使用了 (M_1) 在单个参数值的实际
非多项式素因子。结论恰好区分了“某点有因子递降”与“该进程有统一多项式尾”这两件事。

本边界不排除无界自适应地选择 (p(t)-1) 的实际因子，不排除其它距离、其它源或 Type II
状态；它只排除距离一偶源扇最直接的统一多项式提升。

可复现命令：

~~~bash
python3 reproductions/h19_k23_pressure_even_source_polynomial_boundary.py \
  --input reproductions/h19-k23-global-tail-pressure-external-source-bridge-2097152.json \
  --output reproductions/h19-k23-pressure-even-source-polynomial-boundary-2097152.json
python3 -m unittest tests/test_h19_k23_pressure_even_source_polynomial_boundary.py -q
~~~
