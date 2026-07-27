---
kind: claim
claim_id: type-II-small-shared-gap-single-prime-fan
title: 缺口 3、7、11 共享因子扇的单素因子扩张
statement: 在缺口 3、7、11 的显式共享因子扇之外，令 x_7=(p+7)/4=2u_7、x_11=(p+11)/4=3u_11。若 p=1 mod7 且 u_7 有 5 mod7 素因子，或 p=2,4 mod7 且 u_7 有 3 mod7 素因子，则 m=7 有一张共享 Type II 证书。若 p 不等于 7,8,10 mod11，令 t=-3p mod11；若 u_11 有 t 或 4t mod11 素因子，则 m=11 有一张共享 Type II 证书。与前三缺口的常数分支合并后，未命中者必须同时避开这些指定单素因子残数。
claim_status: established
topics:
- type-II
- shared-divisor
- prime-factors
- congruences
- small-gap
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--2
  role: certificate-reconstruction
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-24'
---

# 缺口 \(3,7,11\) 共享因子扇的单素因子扩张

## 定理

沿用 `type-II-small-shared-gap-explicit-fan` 的记号。共享因子仍固定为

\[
D_3=4,\qquad D_7=8,\qquad D_{11}=12. \tag{1}
\]

写

\[
x_7=\frac{p+7}{4}=2u_7,\qquad
x_{11}=\frac{p+11}{4}=3u_{11}. \tag{2}
\]

在前一条显式扇未命中后，下面的条件仍足以给出共享 Type II 证书：

\[
\begin{array}{c|c|c|c}
\text{条件}&m&\text{选择的 }q&d\\
\hline
p\equiv1\pmod7&7&q\mid u_7,\ q\equiv5\pmod7&q\\
p\equiv2\pmod7&7&q\mid u_7,\ q\equiv3\pmod7&q\\
p\equiv4\pmod7&7&q\mid u_7,\ q\equiv3\pmod7&2q\\
\hline
p\not\equiv7,8,10\pmod {11}&11&q\mid u_{11},\ q\equiv t\pmod {11}&q\\
p\not\equiv7,8,10\pmod {11}&11&q\mid u_{11},\ q\equiv4t\pmod {11}&3q
\end{array} \tag{3}
\]

其中最后两行的

\[
t\equiv-3p\pmod {11}. \tag{4}
\]

## 证明

对 \(m=7\)，有 \(x_7\equiv2p\pmod7\)，故在余下的
\(p\equiv1,2,4\pmod7\) 三类中，Type II 目标 \(-x_7\) 分别为

\[
5,\quad3,\quad6\pmod7. \tag{5}
\]

表 (3) 的 \(d=q,q,2q\) 分别同余于这些目标；且 \(q\mid u_7\)，所以
\(d\mid x_7^2\)。最后一类 \(2q\le2u_7=x_7\)，其余两类更小。

对 \(m=11\)，由 (2) 得

\[
x_{11}\equiv3p\pmod {11},\qquad -x_{11}\equiv t\pmod {11}. \tag{6}
\]

若 \(q\equiv t\)，取 \(d=q\)。若 \(q\equiv4t\)，因 \(3^{-1}\equiv4\pmod {11}\)，
取 \(d=3q\)。两者都满足 \(d\equiv t\pmod {11}\)，且分别不超过
\(u_{11}\) 和 \(3u_{11}=x_{11}\)。它们又都整除 \(x_{11}^2\)。

因此每一行都满足 Type II 除子判据；(1) 同时给出共享因子条件。

## 可检验残余

前三缺口的“单素因子扇”遗漏时，除
`type-II-small-shared-gap-explicit-fan` 的残余条件外，进一步有：

\[
\begin{aligned}
p\equiv1\pmod7&\Longrightarrow
 \text{所有 }q\mid u_7\text{ 都不为 }5\pmod7,\\
p\equiv2,4\pmod7&\Longrightarrow
 \text{所有 }q\mid u_7\text{ 都不为 }3\pmod7,\\
\text{所有 }q\mid u_{11}&\Longrightarrow
 q\not\equiv t,4t\pmod {11}. \tag{7}
\end{aligned}
\]

这仍不是选择器失败：一个由两个或更多素因子组成的除子可以命中目标。

## 精确审计

```bash
python3 reproductions/type_ii_small_shared_gap_single_prime_fan.py --limit 10000000
```

对 \(p\le10^7\) 的 \(82{,}887\) 个核心素数，六个先后分支命中数为

\[
47{,}137,\ 17{,}731,\ 4{,}517,\ 4{,}037,\ 3{,}000,\ 6{,}465,
\]

最后一项是单素因子扇的残余。因此前五项共覆盖

\[
76{,}422/82{,}887=92.2000\%\text{（四舍五入）}. \tag{8}
\]

这比只使用常数除子的 \(83.1313\%\) 更强，但仍低于允许任意除子的
\(96.7124\%\)；两者的差正是下一层多素因子乘积结构。

以 \(d\mid x\) 与 \(d\mid x^2\) 的自然除子格层次重写这一差额，见
`type-II-small-shared-gap-linear-square-profile`：绝大多数额外命中已在线性
除子层完成，只有一小部分真正依赖平方指数重用。
