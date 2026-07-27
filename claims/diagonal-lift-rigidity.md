---
kind: claim
claim_id: diagonal-lift-rigidity
title: 坐标对角缩放不能给出严格的全域解提升
statement: 设 2<=n<p 且 p 为素数。若三个正有理常数 lambda_1,lambda_2,lambda_3 所定义的坐标对角变换 (a,b,c)->(lambda_1 a,lambda_2 b,lambda_3 c) 将 4/n 的全部正实解恒等地送入 4/p 的解空间，则 lambda_1=lambda_2=lambda_3=p/n。该共同缩放不能把任一 4/n 的正整数解送为整数三元组。因此不存在这种对角比例型的严格全域整数提升。
claim_status: established
topics:
- descent
- solution-lift
- obstruction
- egyptian-fractions
- proof-program
sources:
- paper: elsholtz_tao2013
  locator: "Section 2"
  role: equation-and-parametrization-context
visibility: public
last_checked: '2026-07-24'
---

# 坐标对角缩放不能给出严格的全域解提升

## 定理

设

\[
2\le n<p,\qquad p\text{ 为素数},
\]

并令 \(\lambda_1,\lambda_2,\lambda_3\) 为与源解无关的正有理数。假设对每一组正实数
\((a,b,c)\) 满足

\[
\frac4n=\frac1a+\frac1b+\frac1c, \tag{1}
\]

都有恒等式

\[
\frac4p=
\frac1{\lambda_1a}+\frac1{\lambda_2b}+\frac1{\lambda_3c}. \tag{2}
\]

则必有

\[
\lambda_1=\lambda_2=\lambda_3=\frac pn. \tag{3}
\]

特别地，不存在把每个 \(4/n\) 的正整数解送到 \(4/p\) 的正整数解的此类坐标对角提升。

这里的“全域”是指式 (2) 是源解曲面上的恒等式，而非只在事先挑出的有限或带标记子集上成立。
所以结论不排除依赖源解因子结构的非线性提升，也不排除带标记状态图。

## 证明

写

\[
u=\frac1a,\qquad v=\frac1b,\qquad w=\frac1c.
\]

式 (1) 的正实解在开三角形

\[
u,v,w>0,\qquad u+v+w=\frac4n \tag{4}
\]

中连续变化。式 (2) 变为

\[
\frac{u}{\lambda_1}+\frac{v}{\lambda_2}+\frac{w}{\lambda_3}=\frac4p. \tag{5}
\]

一个线性函数若在 (4) 所给的二维开集上恒定，则它的三个系数相等。因此

\[
\frac1{\lambda_1}=\frac1{\lambda_2}=\frac1{\lambda_3}=\mu. \tag{6}
\]

将 (4) 代入 (5)，得到

\[
\mu\frac4n=\frac4p,
\]

故 \(\mu=n/p\)，即 (3)。

现取任一正整数源解 \((a,b,c)\)。若共同缩放 (3) 的三个目标分母仍都是整数，
因 \(p\) 为素数且 \(n<p\)，有 \(\gcd(p,n)=1\)，于是

\[
n\mid a,\qquad n\mid b,\qquad n\mid c. \tag{7}
\]

写 \(a=na_0,b=nb_0,c=nc_0\)。式 (1) 化为

\[
4=\frac1{a_0}+\frac1{b_0}+\frac1{c_0}, \tag{8}
\]

但右端至多为 \(3\)，矛盾。因此 (3) 从不把正整数源解送为正整数三元组。

## 与已有共同缩放障碍的区别

`short-certificate-descent` 中的共同缩放检查只排除了

\[
(a,b,c)\longmapsto(\lambda a,\lambda b,\lambda c).
\]

本定理说明：只要要求一个与源解无关的坐标对角公式在整个解曲面上成立，即使先允许
三个不同的比例 \(\lambda_i\)，它们仍被恒等式强制相同。故尝试把任意较小实例的每个
解“逐坐标放大”到目标实例，不会产生递降。

这条刚性不触及真正剩余的可能性：映射可以只定义在 \(W\subsetneq\operatorname{Sol}(n)\)
上，比例可以依赖于源解的因子数据，或三个输出分母可以耦合地重组。那些情形正是
`marked-solution-descent-closure` 所允许、而全称选择器尚未解决的部分。
