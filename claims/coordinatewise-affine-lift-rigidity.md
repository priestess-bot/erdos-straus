---
kind: claim
claim_id: coordinatewise-affine-lift-rigidity
title: 逐坐标仿射全域提升仍退化为共同缩放
statement: 设 2<=n<p 且 p 为素数。若正斜率的逐坐标仿射公式 (a,b,c)->(alpha_1 a+beta_1, alpha_2 b+beta_2, alpha_3 c+beta_3) 将 4/n 的全部正实解恒等地送入 4/p 的解空间，则 beta_1=beta_2=beta_3=0 且 alpha_1=alpha_2=alpha_3=p/n。因此它不能把任何正整数源解送成正整数目标解。
claim_status: established
topics:
- descent
- solution-lift
- obstruction
- affine-rigidity
- egyptian-fractions
- proof-program
sources:
- paper: elsholtz_tao2013
  locator: "Section 2"
  role: equation-and-parametrization-context
visibility: public
last_checked: '2026-07-24'
---

# 逐坐标仿射全域提升仍退化为共同缩放

## 定理

设

\[
2\le n<p,\qquad p\text{ 为素数}.
\]

令 \(\alpha_i>0\)、\(\beta_i\in\mathbb R\) 不依赖于源解，并假设对每个正实源解

\[
\frac4n=\frac1a+\frac1b+\frac1c \tag{1}
\]

三个仿射输出分母均为正，且恒有

\[
\frac4p=
\frac1{\alpha_1a+\beta_1}
+\frac1{\alpha_2b+\beta_2}
+\frac1{\alpha_3c+\beta_3}. \tag{2}
\]

则

\[
\beta_1=\beta_2=\beta_3=0,\qquad
\alpha_1=\alpha_2=\alpha_3=\frac pn. \tag{3}
\]

于是这类全域公式不能把 \(4/n\) 的任何正整数解送为 \(4/p\) 的正整数解。

## 证明

改用倒数坐标

\[
t_i=\frac1{a_i},\qquad S=\frac4n,
\qquad \phi_i(t)=\frac{t}{\alpha_i+\beta_i t}. \tag{4}
\]

由输出分母在全部正实源解上为正，\(\phi_i\) 在 \((0,S)\) 上有定义。假设 (2)
恰等价于：在开单纯形 \(t_1,t_2,t_3>0\)、\(t_1+t_2+t_3=S\) 上恒有

\[
\phi_1(t_1)+\phi_2(t_2)+\phi_3(t_3)=\frac4p. \tag{5}
\]

写 \(t_3=S-t_1-t_2\)。对 (5) 先对 \(t_1\) 求导、再对 \(t_2\) 求导，得到

\[
\phi_3''(t_3)=0. \tag{6}
\]

由于 \(t_3\) 可遍历 \((0,S)\)，\(\phi_3''\) 在该区间恒为零。循环交换三个坐标，
每个 \(\phi_i\) 都满足同一结论。另一方面，直接计算给出

\[
\phi_i''(t)=-\frac{2\alpha_i\beta_i}
{(\alpha_i+\beta_i t)^3}. \tag{7}
\]

由 \(\alpha_i>0\)，故 \(\beta_i=0\) 对所有 \(i\) 成立。此时 (5) 化为

\[
\frac{t_1}{\alpha_1}+\frac{t_2}{\alpha_2}+\frac{t_3}{\alpha_3}=\frac4p
\quad(t_1+t_2+t_3=S). \tag{8}
\]

左侧要在开单纯形上恒定，三个系数必须相等。因此

\[
\alpha_1=\alpha_2=\alpha_3=\alpha. \tag{9}
\]

将 \(t_1+t_2+t_3=S=4/n\) 代入 (8)，得到

\[
\frac4p=\frac1\alpha\frac4n,
\]

从而 \(\alpha=p/n\)，证明 (3)。

最后，若对某个正整数源解三个输出分母都是整数，则 (3) 与
\(\gcd(p,n)=1\) 强制 \(n\mid a,b,c\)。把 (1) 除以 \(n\) 后得到

\[
4=\frac1{a/n}+\frac1{b/n}+\frac1{c/n},
\]

右侧至多为 \(3\)，矛盾。

## 边界

这严格包含 `diagonal-lift-rigidity` 所排除的纯缩放：允许不同的斜率和常数
平移也不会产生全域提升。假设“对全部正实源解恒等成立”是关键；本定理不排除只在
带标记子集上定义、系数依赖源解因子，或耦合多个输入坐标的非线性映射。后者仍是
“短证书或递降”目标真正需要探索的空间。
