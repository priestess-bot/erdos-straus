---
kind: claim
claim_id: h19-k23-pressure-c3-even-source-conditional-escape-2097152
title: H19-k23 压力进程完整距离三偶源扇的 Dickson 条件性逃逸
statement: 假定 Dickson 素数元组猜想，存在无穷多个 H19-k23 实际核心素数位于压力进程 p=748375048866405601+P*t，使其完整距离三偶源扇均无严格递降。写 p-1=165600h、p-3=22ell；当 p,h,ell,q 同时为充分大的素数时，距离三的全部兼容移位恰为 d=1、ell。两条尾的实际平方除子模式均被逐一穷尽：d=ell 的常数模数 7 逐点避靶，而 d=1 的线性模数至多留下有限异常参数，故整扇逃逸。
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

# H19-k23 压力进程完整距离三偶源扇的 Dickson 条件性逃逸

设压力进程写成

\[
p(t)-1=165600h(t),\qquad p(t)-3=22\ell(t).
\]

在该进程上，\(\ell(t)\equiv1\pmod {12}\)。对距离 \(c=3\) 的偶源，兼容移位
\(d\mid p-3\) 还必须满足 \(12\mid p-d\)。若 \(\ell(t)\) 为素数，\(p-3=22\ell\)
的全部除子中恰有

\[
d=1,\qquad d=\ell(t)
\]

满足该条件，因此这两条射线就是完整距离三扇，不是预先截断的移位盒。

令 \(q(t)\) 由

\[
\frac{p(t)-\ell(t)}{12}=11q(t)
\]

定义。两条射线的尾积分别为

\[
M_1(t)=303600h(t)\ell(t)\quad(d=1),
\qquad
M_1(t)=242q(t)\quad(d=\ell).
\]

脚本逐一枚举 \(e_1\mid M_1^2\) 且 \(e_1\le M_1\) 的所有最终多项式因子模式：第一条有
5,468 个，第二条有 23 个。四个正、本原一次型 \(p,h,\ell,q\) 的局部根检查可采纳。

假定 Dickson 猜想，这四个型同时为充分大素数无穷次发生。于是每条射线的实际素因子只来自
固定内容及所列线性素数，故上述枚举覆盖全部实际平方尾因子。对 \(d=\ell\)，尾模数恒为
\(r=7\)，所有变量项已模 7 固定，23 个候选均逐点失败。对 \(d=1\)，\(r(t)\) 为线性；
每个候选的余式均为非零常数，因而整除只能在有限多个参数发生。取足够大的 Dickson 参数，
两条射线都没有严格递降。

所以在 Dickson 条件下，该压力进程有无穷多个核心素数逃过**完整距离三偶源扇**。
这不反驳 Erdős--Straus 猜想，也不排除距离一、其它奇数距离、非偶源 Type I、Type II
或其它递降状态。它把当前边界具体推进到：即使完整检查距离三，也需要跨距离或不同状态的
统一机制。

可复现命令：

~~~bash
python3 reproductions/h19_k23_pressure_c3_even_source_conditional_escape.py \
  --input reproductions/h19-k23-global-tail-pressure-external-source-bridge-2097152.json \
  --output reproductions/h19-k23-pressure-c3-even-source-conditional-escape-2097152.json
python3 -m unittest tests/test_h19_k23_pressure_c3_even_source_conditional_escape.py -q
~~~
