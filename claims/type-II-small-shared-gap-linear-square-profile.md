---
kind: claim
claim_id: type-II-small-shared-gap-linear-square-profile
title: 小共享缺口扇的线性除子与平方专用证书分层
statement: 对核心素数的缺口 m=3,7,11，固定共享因子分别为 4,8,12。若 Type II 目标残数已由 x=(p+m)/4 的一个除子达到，则得到线性除子证书；若三个缺口均无此除子而某个缺口仍有 Type II 证书，则其每张目标证书都必须使用 d|x^2 但 d 不整除 x 的平方专用除子。精确审计至 10^7 将 82887 个核心素数分成线性 78808、平方专用 1354、三个缺口均未命中 2725。
claim_status: computationally_reproduced
topics:
- type-II
- shared-divisor
- divisor-lattice
- squarefull
- small-gap
- computation
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-24'
---

# 小共享缺口扇的线性除子与平方专用证书分层

## 定义与精确划分

对 \(m\in\{3,7,11\}\)，令

\[
x_m=\frac{p+m}{4},\qquad T_m=-x_m\pmod m. \tag{1}
\]

由 `type-II-small-shared-gap-explicit-fan`，这三个缺口的共享因子分别固定为

\[
D_3=4,\qquad D_7=8,\qquad D_{11}=12. \tag{2}
\]

因此只需考察 Type II 目标。把核心素数 \(p\) 分为三类：

1. **线性类**：某个 \(m\) 与某个 \(d\mid x_m\) 满足 \(d\equiv T_m\pmod m\)；
2. **平方专用类**：第一类失败，但某个 \(m\) 有 \(d\mid x_m^2\)、
   \(d\equiv T_m\pmod m\)；
3. **三缺口未命中类**：对三个 \(m\) 都没有上述 \(x_m^2\) 除子。

第一类直接给出 Type II 证书。第二类的任何目标证书都必满足

\[
d\mid x_m^2,\qquad d\nmid x_m. \tag{3}
\]

这是一个严格的逻辑结论：若某张目标证书的 \(d\) 整除 \(x_m\)，它已经把该素数
放入第一类。于是第二类准确隔离了必须重用某个素因子指数的证书机制。

## 精确审计

```bash
python3 reproductions/type_ii_small_shared_gap_linear_square_profile.py \
  --limit 10000000
```

对 \(p\le10^7\) 的 \(82{,}887\) 个核心素数，输出的完整互斥分割是

\[
\begin{array}{c|r|r}
\text{类别}&\text{个数}&\text{比例}\\
\hline
\text{线性}&78{,}808&95.079\%\\
\text{平方专用}&1{,}354&1.633\%\\
\text{三缺口未命中}&2{,}725&3.287\%
\end{array} \tag{4}
\]

线性命中按首次缺口进一步为

\[
47{,}137\ (m=3),\qquad26{,}621\ (m=7),\qquad5{,}050\ (m=11).
\]

平方专用的首次缺口为 \(910\) 个 \(m=7\) 与 \(444\) 个 \(m=11\)；
\(m=3\) 没有这一型，因为其目标 \(2\pmod3\) 一旦由 \(x_3^2\) 的除子达到，
必已有 \(x_3\) 的一个 \(2\pmod3\) 素因子。

## 研究含义

此前的单素因子扇把难点定位为多素因子乘积；本分层更精确：

- 大部分小缺口成功甚至不需要平方除子格，只需 \(d\mid x\)；
- 少量成功本质上依赖平方指数重用；
- 真正未命中的 \(2{,}725\) 个点才需要更大缺口或不同证书坐标。

所以一个可推进的证明子目标是：对线性类残余，利用不同 \(p+m\) 的固定差证明
不能同时维持“平方专用”或“未命中”型。这个目标保留了原选择器的跨缺口本质，
但避免把线性除子问题和平方指数问题混为一谈。
