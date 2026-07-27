---
kind: claim
claim_id: odd-distance-even-source-half-factor-pair
title: 奇距离偶源的半因子对等价
statement: 设 p=1 mod24。偶源兼容射线 p-c=d(1+cr)、c 为奇数、d=1 mod4 必有 r=7 mod8，且恰等价于 M=(rp+1)/4 存在有向因子对 M=AB，A=B=(r+1)/2 mod r 且 B 为偶数；对应为 A=(cr+1)/2、B=(dr+1)/2。平方尾条件再只取决于 (r,M)。
claim_status: established
topics:
- type-I
- descent
- even-source
- factorization
- divisor-residues
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# 奇距离偶源的半因子对等价

设 \(p\equiv1\pmod{24}\)。任何兼容射线实际必有 \(r\equiv7\pmod8\)：因为
\(d\equiv1\pmod4\) 与 \(r\equiv3\pmod4\) 使
\(B=(dr+1)/2\) 为偶数，而 \(M=AB=(rp+1)/4\) 也必须为偶数。又
\(p\equiv1\pmod8\)，故 \(8\mid rp+1\)，即 \(r\equiv7\pmod8\)。以下固定这样的
\(r\)，并记

\[
M=\frac{rp+1}{4},\qquad u_r=\frac{r+1}{2}.
\]

则下列两类数据一一对应：

\[
p-c=d(1+cr),\qquad c\equiv1\pmod2,\qquad d\equiv1\pmod4, \tag{1}
\]

以及

\[
M=AB,\qquad A\equiv B\equiv u_r\pmod r,\qquad B\equiv0\pmod2. \tag{2}
\]

对应公式为

\[
A=\frac{cr+1}{2},\qquad B=\frac{dr+1}{2}; \tag{3}
\]

反向则为

\[
c=\frac{2A-1}{r},\qquad d=\frac{2B-1}{r}. \tag{4}
\]

的确，由 (1) 有

\[
rp+1=(cr+1)(dr+1)=4AB.
\]

又 \(A\equiv u_r\pmod r\) 可写成
\(A=u_r+rt\)，故 (4) 的 \(c=1+2t\) 为奇数。对 \(B\) 同理有整性；再因

\[
B\equiv0\pmod2,\qquad r\equiv3\pmod4,
\]

得到 \(2B-1\equiv3\pmod4\)，从而 \(d\equiv1\pmod4\)。反向代入即可恢复 (1)。

这把“在 \(rp+1\) 中寻找两个偶因子”的问题压缩为：在
\(M=(rp+1)/4\) 中寻找**同一剩余类** \(u_r\) 的有向因子对，且指定一端为偶数。
随后平方尾的条件仍为

\[
e_1\mid M^2,\qquad e_1\le M,\qquad e_1\equiv-M\pmod r. \tag{5}
\]

故完整选择器问题可分为两个相互独立的乘法问题：先得到 (2)，再在同一状态
\((r,M)\) 中得到 (5)。这比按距离逐条搜索更适合使用因子剩余类、零和积或筛法。

对十亿 H19 的四个压力点，首个命中状态均满足此等价；第四点
\(p=640775689,r=15\) 的一条射线给出

\[
M=2402908834=255683\cdot9398,
\]

其中两个半因子均为 \(8\pmod {15}\)，且 \(9398\) 为偶数。

这是一条代数等价，不是对一般 \(p\) 存在适当 \(r\) 或适当平方尾的证明。

## 重建

~~~bash
python3 reproductions/type_ii_h19_pressure_half_factor_pairs.py
python3 -m unittest tests/test_type_ii_h19_pressure_half_factor_pairs.py -q
~~~
