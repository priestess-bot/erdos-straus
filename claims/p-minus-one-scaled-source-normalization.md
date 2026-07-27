---
kind: claim
claim_id: p-minus-one-scaled-source-normalization
title: p-1 缩放提升与 p 可整除 Type I 首项的归一化
statement: 设 n=p-1。若保持两条尾分母不变，把 4/n 的首分母 A 提升为 pA/t 并得到 4/p，则 A=n(p-t)/4。反之，该公式和 t|A 使任一源解严格提升为目标解。等价地，若目标首项 z 被 p 整除，则 t=np/(4(z/p)+n) 是唯一可能的移位；它为整数时恰恢复该提升。
claim_status: established
topics:
- descent
- type-I
- normalization
- p-minus-one
- certificate
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# \(p-1\) 缩放提升与 \(p\) 可整除 Type I 首项的归一化

令 \(p\) 为奇素数、\(n=p-1\)。假设同一对正整数 \(u,v\) 同时出现于

\[
\frac4n=\frac1A+\frac1u+\frac1v,\qquad
\frac4p=\frac1{pA/t}+\frac1u+\frac1v, \tag{1}
\]

其中 \(t\) 为正整数且 \(t\mid A\)。两式相减得到

\[
\frac4{np}
=\frac1A-\frac{t}{pA}
=\frac{p-t}{pA},
\]

所以首项没有自由度：

\[
A=\frac{(p-1)(p-t)}4. \tag{2}
\]

反过来，若 \(A\) 由 (2) 给出、\(t\mid A\)，且左式有解，则

\[
\frac1{pA/t}+\frac1u+\frac1v
=\frac4{p-1}-\frac{p-t}{pA}
=\frac4p,
\]

故严格提升成立。

目标首项 \(z=pA/t\) 必被 \(p\) 整除。写 \(Z=z/p\)，由 (2) 可反解唯一移位

\[
t=\frac{(p-1)p}{4Z+p-1}. \tag{3}
\]

因此，\(p-1\) 缩放源不是与 Type I 证书空间无关的新存在性问题：它精确参数化了
首项被 \(p\) 整除、且 (3) 为整数的那部分 Type I 目标解。此前有限审计中的 15 条
代表见证均满足 (2)--(3)。

当 \(p\equiv1\pmod4\) 且 \(t\mid A\) 时，(2) 进一步把比例类别完全分开：
\[
\begin{array}{c|c|c}
t\text{ 的类别}&A/(p-1)&\text{缩放记号}\\ \hline
t\equiv1\pmod4&(p-t)/4&a(p-1)\\
t\equiv3\pmod4&(p-t)/4&a(p-1)/2\\
t\equiv0\pmod2&(p-t)/4&a(p-1)/4
\end{array}
\]
其中第一行正是旧的 \(c=1\) 标准偶源形；后两行是非倍数缩放。因为
\(\gcd(t,p-t)=1\)，\(t\mid A\) 对奇 \(t\) 等价于 \(t\mid p-1\)，对偶 \(t\)
等价于 \(t\mid(p-1)/4\)。故 \(b=1,2,4\) 已穷尽保持两条尾分母的 \(p-1\) 首项比例。

这个归一化不否定其作为严格提升的作用；它指出真正需要证明的是对每个目标存在满足
(3) 的可用 Type I 证书，而不是继续扩大同一平方尾枚举。

## 重建

~~~bash
python3 reproductions/type_ii_h19_p_minus_one_scaled_source_normalization.py
python3 -m unittest tests/test_type_ii_h19_p_minus_one_scaled_source_normalization.py -q
~~~
