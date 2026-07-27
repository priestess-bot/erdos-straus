---
kind: claim
claim_id: h19-k23-pressure-full-even-source-conditional-escape-2097152
title: H19-k23 压力进程完整距离一偶源扇的 Dickson 条件性逃逸
statement: 假定 Dickson 素数元组猜想，存在无穷多个 H19-k23 实际核心素数位于压力进程 p=748375048866405601+P*t，使其完整距离一偶源扇均无严格递降。写 p-1=165600*h，全部18条兼容移位为d或d*h。将p、h及每条射线中剩余本原一次因子合并后仅有19个正、本原、局部可采纳线性型。它们同时为充分大的素数时，所有实际因子都落入已枚举的平方尾模式；常数r状态点态避靶，线性r状态至多有有限多个异常参数，故整扇逃逸。
claim_status: conditional
topics:
- type-I
- even-source
- conditional
- dickson
- prime-tuples
- factorization
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

# H19-k23 压力进程完整距离一偶源扇的 Dickson 条件性逃逸

设

\[
p(t)-1=165600h(t). \tag{1}
\]

距离一偶源的全部兼容多项式移位是

\[
\operatorname{shift}=d\quad\hbox{或}\quad dh(t),\qquad
d\mid165600,quad d\equiv1\pmod4, \tag{2}

共 18 条射线。每条射线的

\[
M_1(t)=k(t)(1+r(t)) \tag{3}

由固定内容和有限个本原一次因子组成。

收集目标 (p(t))、(h(t)) 以及每条 (M_1) 中尚未出现的本原一次因子，重复项合并后得到
19 个正、本原线性型。有限域根检查显示该 19 元组局部可采纳。

假定 Dickson 猜想，存在无穷多个参数使这些型同时为素数。取充分大的这些参数，则每条
射线的所有实际素因子恰为固定内容中的素因子及所列线性素数。于是每个平方尾因子都属于
此前完整枚举的模式。

对 (r(t)) 为常数的射线，全部变量因子模 (r) 的残数固定，枚举的非命中即为逐参数
非命中。对 (r(t)) 为线性的射线，任何候选 (e_1(t)) 的同余条件给出一个非零常数余式；
当 (r(t)) 超过该常数的所有因子时，不可能再整除。因此各线性 (r) 射线至多保留有限个
异常参数，充分大时同样失败。

所以在 Dickson 条件下，该压力进程有无穷多个核心素数逃过**完整距离一偶源扇**。

这不反驳 Erdős--Straus 猜想，也不排除更大的奇数距离、非偶源 Type I、Type II 或其它状态。
它说明种子点的距离一见证依赖特殊的实际非多项式因子，不能被提升成覆盖整条进程的原则。

可复现命令：

~~~bash
python3 reproductions/h19_k23_pressure_full_even_source_conditional_escape.py \
  --input reproductions/h19-k23-global-tail-pressure-external-source-bridge-2097152.json \
  --output reproductions/h19-k23-pressure-full-even-source-conditional-escape-2097152.json
python3 -m unittest tests/test_h19_k23_pressure_full_even_source_conditional_escape.py -q
~~~
