---
kind: claim
claim_id: h19-k23-pressure-odd-distance-primitive-form-growth
title: H19-k23 压力进程奇距离约化商型的必然增长
statement: 对压力进程 p(t)=p0+P*t 和每个 0<c<p0，令 B_c=gcd(p0-c,P)、ell_c(t)=(p(t)-c)/B_c。则每个 ell_c 是正、本原一次型，且不同距离给出不同的 ell_c。因此任何要求所有 ell_c 同时为素数来完整控制 p-c 因子的固定维 Dickson 编译，在距离上界趋于无穷时必需无界多的一次型。
claim_status: established
topics:
- even-source
- dickson
- prime-tuples
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

# H19-k23 压力进程奇距离约化商型的必然增长

设

\[
p(t)=p_0+Pt,\qquad
B_c=\gcd(p_0-c,P),\qquad
\ell_c(t)=\frac{p(t)-c}{B_c}.
\]

对任何 \(0<c<p_0\)，\(\ell_c\) 的系数与常数项分别为

\[
\left(\frac{P}{B_c},\frac{p_0-c}{B_c}\right).
\]

按 \(B_c\) 的定义，这两个整数互素，故 \(\ell_c\) 为正、本原一次型。

若 \(\ell_c=\ell_{c'}\)，先由一次系数相等得 \(B_c=B_{c'}\)；再由常数项相等得
\(p_0-c=p_0-c'\)，从而 \(c=c'\)。所以不同距离给出两两不同的约化商型。

这给出一个方法论上的严格限制。当前有界偶源逃逸把每个

\[
p-c=B_c\ell_c
\]

约化为“固定内容乘一个条件素数”，以便穷尽 \(p-c\) 的全部除子。若把这一**同一种一素数
商编译法**扩展到所有奇距离，则必须同时要求无界多个两两不同的 \(\ell_c\) 为素数；它不能由
一个固定有限维的 Dickson 元组承载。

这不是对任何无界距离递降定理的否定。它不排除使用更弱的因子分布、跨距离关联、非标准源或
其它方法。它只证明：要突破目前的有界条件性逃逸边界，不能把“所有距离的约化商均为一个
条件素数”继续作为固定维的统一框架。

可复现命令：

~~~bash
python3 reproductions/h19_k23_pressure_odd_distance_primitive_form_growth.py \
  --input reproductions/h19-k23-global-tail-pressure-external-source-bridge-2097152.json \
  --output reproductions/h19-k23-pressure-odd-distance-primitive-form-growth-2097152.json
python3 -m unittest tests/test_h19_k23_pressure_odd_distance_primitive_form_growth.py -q
~~~
