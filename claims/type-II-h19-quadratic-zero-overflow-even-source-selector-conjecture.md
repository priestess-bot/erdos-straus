---
kind: claim
claim_id: type-II-h19-quadratic-zero-overflow-even-source-selector-conjecture
title: H19 后二次外部源或零溢出偶源选择器猜想
statement: 对每个未被 H19 直接 Type II 射线捕获的素数 p=1 mod24，猜想至少有一个出口成立：(A) 存在完整平方因子外部源严格递降；或 (B0) 存在正奇数 c、d|p-c、r,e，使 (p-c)/d=1+cr、dr=-1 mod4、M=((rp+1)/4)、e|M^2、e=-M mod r，且 e|(M+e)/r。条件 (B0) 等价于尾诱导 Type I 目标除子溢出 B=1，并给出严格递降。该猜想若成立则蕴含 Erdős--Straus 猜想。
claim_status: open
topics:
- type-I
- even-source
- external-source
- overflow
- selector
- induction
- proof-program
- h19
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: even-source-and-external-source-descent
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization
visibility: public
last_checked: '2026-07-26'
---

# H19 后二次外部源或零溢出偶源选择器猜想

令 \(p\equiv1\pmod {24}\) 未被已知 H19 直接 Type II 射线捕获。提出如下析取。

**(A) 二次外部源分支。** 存在完整平方因子外部源严格递降，即已有标准分支的全部
因子同余条件成立。

**(B0) 零溢出偶源分支。** 存在正奇数 \(c<p\)、\(d\mid p-c\)、正整数 \(r,e\)，使

\[
\frac{p-c}{d}=1+cr>1,\qquad dr\equiv-1pmod4,
\]

并令

\[
k=\frac{dr+1}{4},\qquad M=k(1+cr)=\frac{rp+1}{4}.
\]

要求

\[
emid M^2,\qquad ele M,\qquad eequiv-Mpmod r,\qquad
emid\frac{M+e}{r}. \tag{B0}
\]

前 3 条是完整偶源平方尾条件。由尾归一化，令

\[
g=\frac{4e+1}{r},\qquad x=\frac{M+e}{r}=\frac{p+g}{4}.
\]

则 \(e\mid x^2\)，且 Type I 正规形的溢出为 \(B=e/(e,x)\)。因此 (B0) 最后一条
等价于 \(B=1\)。它不是随意附加的“小参数”要求，而是尾目标除子完全不超出其首分母
素因子指数的精确条件。

任一分支都给出严格更小源分母的显式提升，故该析取若对所有 H19 残余成立，则结合已知
H19 射线与强归纳蕴含 Erdős--Straus 猜想。

## 当前证据和风险

在存储的 \(p\le10^9\) H19 剖面中，660 个点满足 (A)，余下 4 个点均满足 (B0)，其
尾参数 \(r\) 为 \(103,31,31,15\)。同时，直接扫描所有残余会看到 91 个首个 \(r\) 命中
需要 \(B>1\)；但这些点都已经满足 (A)。这正是提出析取、而不是单独零溢出偶源选择器的
理由。

这仍只是有限支持，尤其没有解释为什么一般的二次外部源失败会强制一个 \(B=1\) 的偶源尾。
高溢出与标准源成功的有限相关性可能在更大范围破裂。证明必须使用两类因子状态的共同失败、
碰撞--私有分解或新的标记递降，而不能从统计相关直接推演。
