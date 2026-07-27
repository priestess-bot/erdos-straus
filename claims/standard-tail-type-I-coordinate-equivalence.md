---
kind: claim
claim_id: standard-tail-type-I-coordinate-equivalence
title: 标准大尾提升恰为 Type I 证书的第二分母窗口
statement: 对核心素数 p，自然范围内从偶数标准源保留大尾的提升，恰等价于重构第二分母 y 为偶数且 p/2<y<p 的 Type I 证书；从三倍数标准源保留大尾的非冗余提升，恰等价于 y 被 6 整除且 p<y<2p 的 Type I 证书。两种对应中，尾项因子正是 Type I 除子 d。因此这些提升提供证书搜索坐标，但不消除目标因子选择问题。
claim_status: established
topics:
- descent
- certificate
- type-I
- coordinate-equivalence
- even-source
- three-divisible-source
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1 and 3"
  role: Type-I-certificate-statement-and-reconstruction
- paper: elsholtz_tao2013
  locator: "Section 2"
  role: ordered-solution-context
visibility: public
last_checked: '2026-07-24'
---

# 标准大尾提升恰为 Type I 证书的第二分母窗口

## 定理

令 \(p\equiv1\pmod {24}\) 为素数。一个自然范围的 Type I 证书写为

\[
m=4x-p,\qquad d\mid x^2,\qquad m\mid px+d, \tag{1}
\]

并以 Bradford 公式恢复

\[
y=\frac{px+d}{m},\qquad
z=\frac{p(x+px^2/d)}m. \tag{2}
\]

则有两条精确等价。

1. 下列两件事等价：

   - 存在偶数 \(n\) 满足 \(p/2<n<p\)，从
     \[
     \frac4n=\frac1{n/2}+\frac1n+\frac1n \tag{3}
     \]
     保留一个 \(n\)、重组另外两项，得到自然范围的目标解；
   - 存在满足 (1) 的 Type I 证书，且其 (2) 中的第二分母满足
     \[
     y\equiv0\pmod2,\qquad \frac p2<y<p. \tag{4}
     \]

   在对应中 \(n=y\)，尾项因子等于 \(d\)，目标三元组为 \((x,y,z)\)。

2. 下列两件事等价：

   - 存在 \(n\) 满足 \(3\mid n\)、\(p/2<n<p\)，从
     \[
     \frac4n=\frac1{n/3}+\frac1{2n}+\frac1{2n} \tag{5}
     \]
     保留一个 \(2n\)、重组另外两项，得到自然范围的目标解；
   - 存在满足 (1) 的 Type I 证书，且其第二分母满足
     \[
     y\equiv0\pmod6,\qquad p<y<2p. \tag{6}
     \]

   在对应中 \(2n=y\)，尾项因子仍等于 \(d\)，目标三元组为 \((x,y,z)\)。

## 证明

先从 Type I 证书出发。由 (1)--(2)，

\[
\frac4p=\frac1x+\frac1y+\frac1z. \tag{7}
\]

在 (4) 下令 \(n=y\)。则 \(n\) 是 \(p/2<n<p\) 的偶数，(3) 是显式源解；
(7) 保留该源中的一个大分母 \(n\)，所以给出偶数标准大尾提升。

在 (6) 下令 \(n=y/2\)。则 \(p/2<n<p\) 且 \(3\mid n\)，而

\[
\frac4n=\frac1{n/3}+\frac1{2n}+\frac1{2n}
=\frac1{y/6}+\frac1y+\frac1y. \tag{8}
\]

故 (7) 同样保留一个大分母 \(y=2n\)，给出三倍数标准大尾提升。

反过来，设 \(Y\) 是任一上述保留的大分母，目标解的另外两个分母按
\(x\le z\) 排列。自然范围保证 \(x\le p/2<Y\)，所以 \(x\) 是目标首分母。
令

\[
m=4x-p,\qquad R=4Y-p,\qquad S=pY. \tag{9}
\]

二项尾的因子式为

\[
(Rx-S)(Rz-S)=S^2. \tag{10}
\]

记 \(d=Rx-S\)。由 \(x\le z\)，可选 \(d\le S\)。又

\[
\begin{aligned}
d
&=(4Y-p)x-pY\\
&=(4x-p)Y-px\\
&=mY-px. \tag{11}
\end{aligned}
\]

所以

\[
Y=\frac{px+d}{m}. \tag{12}
\]

由 (10) 有 \(d\mid S^2\)，而 \(S\equiv Rx\pmod d\)。又
\(\gcd(R,S)=1\) 蕴含 \(\gcd(d,R)=1\)，故

\[
d\mid (Rx)^2\quad\Longrightarrow\quad d\mid x^2. \tag{13}
\]

由 (11) 有 \(d+px=mY\)，故 Type I 的候选恢复值满足

\[
\frac{p(x+px^2/d)}m=\frac{pxY}{d}. \tag{14}
\]

另一方面 \(d=Rx-S\) 蕴含

\[
R(pxY)-Sd=S(Rx-d)=S^2, \tag{15}
\]

所以 \((pxY/d)\) 正是 (10) 的另一因子所恢复的 \(z\)。也即

\[
z=\frac{p(x+px^2/d)}m. \tag{16}
\]

于是 (11)--(16) 正是 Type I 证书的恢复式。具体地，若
\(t=\gcd(x,Y)\)，则 (11) 同时表明 \(t\mid d\)；这也与
`affine-standard-tail-type-I-descent` 中给出的完整反向论证一致。

偶数源时 \(Y=n\)，自动得到 (4)；三倍数源时 \(Y=2n\)，自动得到 (6)。
反向对应遂全部成立。

## 含义

这两类提升确实有较小且显式可解的源分母，但其成功条件等价于目标 \(p\) 已具有一个
落在指定第二分母窗口的 Type I 证书。它们因此是有价值的 Type I 因子搜索坐标和标记
状态标签，却不能在该目标因子条件失败时提供额外的归纳杠杆。完成“短证书或递降”引理
仍需要强制这些窗口中的因子，或寻找不等价于既有证书的新型提升。
