---
kind: claim
claim_id: h19-k23-unbridged-pressure-full-low-defect-rays
title: H19-k23 两条无固定桥原压力进程的全体低缺陷 Type II 尾定理
statement: H19-k23 两条没有固定因子外源桥的原始压力进程，其每个参数 n>=0 都有一个固定的 p-1 Type II 尾证书，而不必细化进程。第一条固定取 q=15、m=59、d=37845=3^2*5*29^2；第二条固定取 q=90、m=359、d=121014=2*3^6*83。两个固定见证相对 Supp(q) 都只新增1个素因子，故选择器最小缺陷满足 delta(p,q)<=1；这里不主张 delta 恰等于1。两条原进程均为本原的 1 mod 24 等差进程，故各含无穷多个素数值；每个这样的核心素数都满足动态选择器的低缺陷分支 T。
claim_status: established
proof_provenance: mixed
review_status: independent_review
topics:
- type-II
- support-defect
- selector
- affine-progressions
- dirichlet
- h19
- pressure-family
sources:
- paper: bradford2024
  locator: Proposition 2
  role: ordinary-Type-II-tail-context
visibility: public
last_checked: '2026-07-27'
---

# 两条原压力进程的全体低缺陷尾

令

\[
p_i(n)=p_i(0)+P_i n,\qquad n\ge0,
\]

其中 \(p_1(0)=2\,220\,549\,727\,681\,245\,601\)、
\(p_2(0)=748\,375\,048\,866\,405\,601\)，而 \(P_1,P_2\) 是
[固定因子桥产物](../reproductions/h19-k23-global-tail-pressure-external-source-bridge-2097152.json)
中相应两行的原始 `pressure_prime_coefficient`。下文没有把 \(P_i\) 乘上额外周期；
可复算结果把两条进程都显式标为 `full_original_pressure_ray` 和
`step_refinement_multiplier: 1`。这与此前只覆盖周期细化子族的
[低缺陷子射线定理](h19-k23-unbridged-pressure-low-defect-subrays.md)不同。

## 固定见证

置

\[
B_i(n)=\frac{p_i(n)-1}{4},\qquad
S_i=\frac{P_i}{4},\qquad x_i(n)=B_i(n)+q_i.
\]

两条原进程分别使用下列数据：

| 进程 | \(q_i\) | \(m_i=4q_i-1\) | \(d_i\) | 见证新增支持 | \(\delta(p,q_i)\) 上界 |
|---|---:|---:|---:|---|---:|
| \(p_1\) | 15 | 59 | \(37\,845=3^2\cdot5\cdot29^2\) | \(\{29\}\) | 1 |
| \(p_2\) | 90 | 359 | \(121\,014=2\cdot3^6\cdot83\) | \(\{83\}\) | 1 |

精确整数审计对 \(i=1,2\) 逐项验证

\[
P_i\equiv0\pmod{24},\qquad
\gcd(p_i(0),P_i)=1,
\]

\[
q_i\mid B_i(0),\quad q_i\mid S_i,
\quad d_i\mid x_i(0)^2,\quad d_i\mid S_i, \tag{1}
\]

以及

\[
m_i\mid x_i(0)+d_i,\qquad m_i\mid S_i,
\qquad d_i\le x_i(0),\qquad \gcd(d_i,m_i)=1. \tag{2}
\]

由于 \(B_i(n)=B_i(0)+S_i n\) 且 \(x_i(n)=x_i(0)+S_i n\)，式 (1)--(2)
对每个 \(n\ge0\) 推出

\[
q_i\mid B_i(n),\qquad d_i\mid x_i(n)^2,
\qquad d_i\equiv-x_i(n)\pmod{m_i},
\qquad d_i\le x_i(n). \tag{3}
\]

这正是
[普通 Type II 双尾选择器](type-II-tail-support-defect-criterion.md)的精确除子判据。
相对于 \(\operatorname{Supp}(q_i)\)，式 (3) 的两个固定除子都只引入一个新素数，
所以整条原进程上的选择器最小缺陷都至多为 1。这里没有穷尽所有 \(q,d\)，因而不把
这个上界写成等式。

特别地，第二条进程上的 \(q_2=90,d_2=121\,014\) 把此前
\(q=8,d=1\,508\,258\) 只在周期细化子射线上给出的缺陷上界 2 严格改进为：原进程
全体参数上的缺陷上界 1。此前固定见证本身仍然有效，但已不是当前最佳上界或最佳作用域。

## 证书恒等式与递降

对任意参数 \(n\ge0\)，令

\[
u_i(n)=\frac{B_i(n)}{q_i}+1,
\]

并定义普通 Type II 的两个尾分母

\[
y_i(n)=\frac{p_i(n)(x_i(n)+d_i)}{m_i},\qquad
z_i(n)=\frac{p_i(n)(x_i(n)+x_i(n)^2/d_i)}{m_i}.
\]

式 (3) 以及 \(\gcd(d_i,m_i)=1\) 保证这两个数都是整数，并给出

\[
\frac4{p_i(n)}
=\frac1{x_i(n)}+\frac1{y_i(n)}+\frac1{z_i(n)}, \tag{4}
\]

以及去掉两个尾中的 \(p_i(n)\) 后的源恒等式

\[
\frac4{u_i(n)}
=\frac1{x_i(n)}
+\frac1{y_i(n)/p_i(n)}
+\frac1{z_i(n)/p_i(n)}. \tag{5}
\]

这里 \(2\le u_i(n)<p_i(n)\)，所以 (5) 是严格递降。程序对两条进程的
\(n=0,1\) 分别重放 (4)--(5) 的精确有理数恒等式；全参数结论来自 (1)--(3)
的仿射不变量，而不是由两个样本外推。

## 无穷素数与作用域

两条原进程都满足 \(p_i(0)\equiv1\pmod{24}\)、\(24\mid P_i\) 且
\(\gcd(p_i(0),P_i)=1\)。Dirichlet 关于等差数列中素数的定理因此保证每条
原进程含无穷多个素数值。每个这样的值都是核心素数，并由同一个固定见证满足
[动态选择器](dynamic-low-defect-tail-or-external-exit-selector.md)的分支 T。

这个结论覆盖两条原压力进程的全部参数，严格强于此前的周期细化子射线结论；它仍只
处理 H19-k23 压力作用域，不是对所有核心素数的全称选择器定理。

可复现命令：

~~~bash
python3 reproductions/h19_k23_unbridged_pressure_full_low_defect_rays.py
python3 -m unittest tests/test_h19_k23_unbridged_pressure_full_low_defect_rays.py -q
~~~
