---
kind: claim
claim_id: odd-distance-even-source-descent
title: 奇数距离偶源的完整平移平方因子递降扇
statement: 对每个 p=1 mod24 的素数，任意满足参数条件的奇数距离 c 都给出一个严格较小的偶数源 p-c；该源上的全部可恢复 Type I 平移平方尾，精确等价于一个 M1^2 因子的单同余条件。
claim_status: established
topics:
- descent
- certificate
- type-I
- external-source
- factorization
- even-source
- proof-program
sources:
- paper: bradford2024
  locator: "Proposition 1"
  role: Type-I-certificate-reconstruction
- paper: ventas2026
  locator: "Theorem 2.3"
  role: external-source-context
visibility: public
last_checked: '2026-07-24'
---

# 奇数距离偶源的完整平移平方因子递降扇

## 定理

设 p 是满足下式的素数，c 是小于 p 的正奇数：

\[
p\equiv1\pmod{24},\qquad 1\le c<p.
\]

取 p-c 的正因子 d。假设存在正整数 r，使得

\[
s=\frac{p-c}{d}=1+cr>1,\qquad dr\equiv-1\pmod4.\tag{1}
\]

令

\[
k=\frac{dr+1}{4},\qquad M_1=ks.\tag{2}
\]

则 d 是 1 mod 4，r 是 7 mod 8，且

\[
4M_1=rp+1,\qquad (r,M_1)=1.\tag{3}
\]

若正整数 e1 满足

\[
e_1\mid M_1^2,\qquad e_1\le M_1,\qquad
e_1\equiv-M_1\pmod r,\tag{4}
\]

定义

\[
u=\frac{M_1+e_1}{r},\qquad v=\frac{M_1u}{e_1},\qquad
m=\frac{4e_1+1}{r},\qquad D=\frac{u^2}{e_1}.\tag{5}
\]

这些量均为正整数，且

\[
3\le m\le p-2.
\]

以下是严格的标记提升：

\[
\frac4{p-c}
=\frac1{dM_1}+\frac1u+\frac1v
\quad\Longrightarrow\quad
\frac4p
=\frac1{pM_1}+\frac1u+\frac1v.\tag{6}
\]

同时，(m,D) 是 p 的 Type I 除子证书，首分母是 u。源分母 p-c 严格小于 p，
且因为 c 是奇数而为偶数。此定理只在 (1)、(4) 成立时构造带标记的可提升源解；
它没有断言每个 p 都可以选到 c、d、e1。

反过来，完整平移平方因子外部源递降中，凡源分母为 p-c（其中 c 为正奇数）的
见证，都唯一来自 (1)--(4)。故 (4) 是该偶源切片的精确单同余参数化，并非额外的
充分条件。

## 证明

由 (1)、(2)，

\[
p=ds+c=d(1+cr)+c=d+c(dr+1)=d+4kc.\tag{7}
\]

所以 d 是 1 mod 4。再由 dr 是 -1 mod 4，r 是 3 mod 4，故 r 为大于 1 的
奇数。事实上，\(d\equiv1\pmod4\) 给出 \((dr+1)/2\) 为偶数；由下面的恒等式
\(M_1=((cr+1)/2)((dr+1)/2)\)，\(M_1\) 也为偶数。因为 \(p\equiv1\pmod8\) 且
\(4M_1=rp+1\)，可知 \(8\mid rp+1\)，即 \(r\equiv7\pmod8\)。直接计算得

\[
4M_1=s(dr+1)=drs+s=r(ds+c)+1=rp+1.
\]

r 与 s 互素，而 4k=dr+1 蕴含 r 与 k 互素，所以 (3) 成立。

由 (4) 及 (3) 中的互素性，互补因子自动满足

\[
\frac{M_1^2}{e_1}\equiv-M_1\pmod r.\tag{8}
\]

因而 u、v 均为整数；e1 整除 u 平方，所以 D 也为整数，并且

\[
\frac1u+\frac1v=\frac r{M_1}.
\]

结合 p-c=ds、4k=dr+1 及 (3)，有

\[
\frac1{dM_1}+\frac r{M_1}=\frac{dr+1}{dM_1}=\frac4{p-c},
\qquad
\frac1{pM_1}+\frac r{M_1}=\frac4p.
\]

这给出 (6)。

进一步，

\[
4u-p=\frac{4e_1+1}{r}=m.\tag{9}
\]

若 e1=M1，(4) 会迫使 r 整除 2M1，这与 (3) 矛盾。又

\[
M_1-e_1\equiv2M_1\equiv\frac{r+1}{2}\pmod r,
\]

所以

\[
p-m=\frac{4(M_1-e_1)-2}{r}\ge2.\tag{10}
\]

式 (9) 给出 m 是 3 mod 4，故 m 落在所述自然范围。

最后，

\[
mv-pu
=u\left(\frac{M_1(4e_1+1)}{re_1}-p\right)
=\frac{u(M_1+e_1)}{re_1}=D,
\]

以及

\[
u+pe_1
=\frac{M_1+e_1+(4M_1-1)e_1}{r}
=\frac{M_1(4e_1+1)}r=mM_1.\tag{11}
\]

Bradford 的两条 Type I 恢复式分别恢复 v 与 pM1，正是 (6) 的目标三元组。

为证明反向完整性，设完整平移平方因子见证的源是 n=p-c，平移参数为 d，并令
q=4k-1、M=kn。原条件 d 整除 M，连同 4M=qp+d，给出 d 整除 qp。由于 d 严格
小于素数 p，d 整除 q。写 q=dr，再代入 (q+1)n=qp+d，得到

\[
n=d(1+cr)=ds,\qquad 4k=dr+1.
\]

这恢复 (1)--(2)。原因子可写为 e=de1；第二尾项同余强迫 e1 整除 M1 平方，
第一个同余化为 (4) 的末项，而 (3) 自动给出互补同余。d、e1 唯一决定原参数。

## 例子与边界

取

\[
p=73,\qquad c=3,\qquad d=1,\qquad s=70,\qquad r=23,\qquad
k=6,\qquad M_1=420,\qquad e_1=40.
\]

此时 (m,D)=(7,10)，而

\[
\frac4{70}=\frac1{420}+\frac1{20}+\frac1{210}
\quad\Longrightarrow\quad
\frac4{73}=\frac1{30660}+\frac1{20}+\frac1{210}.
\]

这补充 p-1 源：p=73 在距离一扇中未命中，却在 c=3 时命中。奇数距离偶源递降测试
在 p 不超过 10000 的 143 个核心素数上，逐项核对了 c=1、3、7 与完整平移族的等价；
允许所有 c 不超过 31 的正奇数时命中 93 个。两项数字都是有限审计，不能代替
对 (4) 的全称选择器。更强的同一范围诊断允许每个素数使用所有小于 p 的正奇数
距离，仍只命中 112 个，并漏掉 97、193、241、577 等 31 个核心素数。因此仅扩大
这一完整偶源扇不足以证明目标引理。
