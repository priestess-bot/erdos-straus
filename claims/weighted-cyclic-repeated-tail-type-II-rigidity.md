---
kind: claim
claim_id: weighted-cyclic-repeated-tail-type-II-rigidity
title: 小权重加权循环重复尾提升必退化为 Type II 证书
statement: 令 p=1 mod24 为素数，0<r<s<p 且 gcd(r,s)=1。若严格更小的重复尾源 4/n=1/a+2/b 经 r/s 加权循环传输得到整数目标三元组，则目标至少两项被 p 整除；其余项 x 满足 p/4<x<=p/2，故该提升必恢复自然范围的 Type II 证书。因而权重分母 s<p 的重复尾路线不能给出独立于直接 Type II 证书的无标记递降。
claim_status: established
topics:
- descent
- type-II
- weighted-transport
- repeated-tail
- rigidity
- marked-solution
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II certificate reconstruction
- paper: elsholtz_tao2013
  locator: Section 2
  role: Egyptian-fraction equation context
visibility: public
last_checked: '2026-07-25'
---

# 小权重加权循环重复尾提升必退化为 Type II 证书

## 定理

令

\[
p\equiv1\pmod {24},\qquad
0<r<s<p,\qquad \gcd(r,s)=1. \tag{1}
\]

设有严格更小的重复尾源

\[
\frac4n=\frac1a+\frac1b+\frac1b,\qquad 2\le n<p, \tag{2}
\]

并用加权循环传输

\[
\begin{aligned}
\frac1A&=\frac n{ps}\left(\frac r a+\frac{s-r}b\right),\\
\frac1B&=\frac n{ps}\left(\frac r b+\frac{s-r}b\right),\\
\frac1C&=\frac n{ps}\left(\frac r b+\frac{s-r}a\right). \tag{3}
\end{aligned}
\]

若 \(A,B,C\) 都是正整数，则其中至少两项被 \(p\) 整除；把剩余项记为 \(x\)，
目标解是自然范围的 Type II 解，因而有一张直接 Type II 除子证书。

## 证明

由 (3) 的中间项，

\[
B=\frac{pb}{n}. \tag{4}
\]

整性及 \(\gcd(n,p)=1\) 给出 \(b=nk\)。由 (2)，

\[
a=\frac{nk}{4k-2},\qquad
n_k=\frac{4k-2}{\gcd(k,4k-2)}\mid n. \tag{5}
\]

特别地 \(n_k<p\)。若 \(k\) 奇，则 \(n_k=4k-2\)；若 \(k\) 偶，
\(n_k=2k-1\)。两种情形都给出

\[
0<4k-1<2p. \tag{6}
\]

将 (5) 代入 (3)，得到

\[
A=\frac{psk}{D_A},\qquad B=pk,\qquad C=\frac{psk}{D_C}, \tag{7}
\]

其中

\[
D_A=4rk+s-3r,\qquad
D_C=4(s-r)k-2s+3r. \tag{8}
\]

因为 \(s<p\)，\(p\nmid sk\)。若 \(p\nmid A\)，由 (7) 的整性必须有
\(p\mid D_A\)；同理，若 \(p\nmid C\)，则 \(p\mid D_C\)。若两者都不被 \(p\)
整除，则

\[
p\mid D_A+D_C=s(4k-1). \tag{9}
\]

由 \(p\nmid s\) 得 \(p\mid4k-1\)。式 (6) 表明唯一可能的正奇数倍数是

\[
p=4k-1, \tag{10}
\]

但右端 \(3\pmod4\)，与 \(p\equiv1\pmod4\) 矛盾。因此 \(A,C\) 至少一项被
\(p\) 整除；再结合 \(B=pk\)，目标至少有两条 \(p\) 倍分母。三项不可能都被
\(p\) 整除，否则把目标等式乘以 \(p\) 后，右端至多为 \(3\)，而左端为 \(4\)。
故恰有一项不被 \(p\) 整除。

设其余项为 \(x\)，并写目标为

\[
\frac4p=\frac1x+\frac1{pU}+\frac1{pV}. \tag{11}
\]

正性给出 \(x>p/4\)。又 \(1/U+1/V\le2\)，所以将 (11) 乘以 \(p\) 后有

\[
4-\frac px\le2,
\]

即 \(x\le p/2\)。于是 \(m=4x-p\) 是 \(3\pmod4\) 的正整数，且
\(3\le m\le p-2\)。这正是自然 Type II 范围；Bradford 的 Type II 除子对应恢复
直接证书，定理得证。

## 对有限审计的解释

weighted-cyclic-complete-repeated-tail-audit 的 \(s\le50\)、\(p\le5000\) 盒满足
\(s<p\)。其唯一无向命中 \(p=2161,r/s=1/49\) 的两条 \(p\) 倍尾分母，正是本定理
所强制；审计记录的 Type II \((m,d)=(47,12)\) 是独立实现核对，而不是从有限数据
归纳出的规律。

## 研究边界

该刚性排除所有 \(s<p\) 的重复尾加权循环作为独立递降机制。要绕开它，必须至少满足
下列之一：

1. 权重分母与 \(p\) 同量级或更大；
2. 源的三项分母彼此不同；
3. 传输不是零偏移循环形式。

第一种选择会失去“固定或缓增有限模板”的可控性；第二种才是当前较有潜力的因子标记
方向。
