---
kind: claim
claim_id: h19-k23-pressure-c5-even-source-conditional-escape-2097152
title: H19-k23 压力进程完整距离五偶源扇的 Dickson 条件性逃逸
statement: 假定 Dickson 素数元组猜想，存在无穷多个 H19-k23 实际核心素数位于压力进程 p=748375048866405601+P*t，使其完整距离五偶源扇均无严格递降。写 p-5=10004ell；当 p、ell 及四条尾的 k 共因子同时为充分大的素数时，距离五的全部兼容移位恰为 d=1,41,61,2501。四条尾的实际平方除子模式均被逐一穷尽，线性尾模数只留下有限异常参数，故整扇逃逸。
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

# H19-k23 压力进程完整距离五偶源扇的 Dickson 条件性逃逸

在同一压力进程中有

\[
p(t)-5=10004\ell(t).
\]

对距离 \(c=5\) 的偶源，移位 \(d\mid p-5\) 必须同时使

\[
20\mid p-d,
\qquad
5d\mid p-d-5.
\]

假定 \(\ell(t)\) 为素数后，逐一枚举 \(10004\ell\) 的全部除子并检查这两个整除条件，
完整兼容扇恰为

\[
d\in\{1,41,61,2501\}.
\]

每条射线均有 \(M_1=k(p-5)/d\)。将四个 \(k\) 中的固定内容剥离，得到 \(p,\ell\)
及四个正、本原一次共因子 \(q_d\)，共六个一次型。它们的局部根检查可采纳。假定 Dickson
猜想，这六型同时为充分大素数无穷次发生，于是每条尾的所有实际素因子都由固定内容和其两个
指定的一次素因子构成。

在该条件下，脚本逐条枚举 \(e_1\mid M_1^2\)、\(e_1\le M_1\) 的所有最终因子模式。
对应 \(d=1,41,61,2501\) 的候选数依次为

\[
20048,\quad95,\quad203,\quad68.
\]

它们对各自线性尾模数的多项式余式均非零。因此每条射线至多保留有限个参数异常；取足够大的
Dickson 参数，整条距离五扇均无严格递降。

所以在 Dickson 条件下，该压力进程有无穷多个核心素数逃过**完整距离五偶源扇**。
这不反驳 Erdős--Straus 猜想，也不排除其它距离、非偶源 Type I、Type II 或其它递降状态。
与距离一、三的结果合在一起，它表明按单个固定奇距离扩展偶源扇不足以形成统一选择器；有效
推进必须利用不同距离之间的共同因子状态或不同类型的源状态。

可复现命令：

~~~bash
python3 reproductions/h19_k23_pressure_c5_even_source_conditional_escape.py \
  --input reproductions/h19-k23-global-tail-pressure-external-source-bridge-2097152.json \
  --output reproductions/h19-k23-pressure-c5-even-source-conditional-escape-2097152.json
python3 -m unittest tests/test_h19_k23_pressure_c5_even_source_conditional_escape.py -q
~~~
