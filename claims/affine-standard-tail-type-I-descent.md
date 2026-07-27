---
kind: claim
claim_id: affine-standard-tail-type-I-descent
title: 共享尺度标准大尾的仿射 Type I 递降射线
statement: 令 p=1 mod24 为素数。若正整数 a<b、h、t 满足 p(a+b)=4abt-h、h|a^2t，并令 x=at、y=bt、d=ht、m=(4a^2t+h)/(a+b)，则只要 m 在自然范围，(m,d) 是 Type I 证书且其第二分母为 y。若 y 本身是 p/2<n<p 内偶数标准源的 n，或 y=2n 且 n 是该范围内 3 的倍数，则该证书分别给出从 (n/2,n,n) 或 (n/3,2n,2n) 保留大尾并重组另外两项的严格提升。反之，满足 gcd(x,y)|d 的这两类 Type I 提升都唯一归入该坐标。
claim_status: established
topics:
- descent
- certificate
- type-I
- affine-parameterization
- even-source
- three-divisible-source
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1 and 3"
  role: Type-I-certificate-context
- paper: elsholtz_tao2013
  locator: "Section 2, Proposition 2.3"
  role: Type-I-parameterization-context
visibility: public
last_checked: '2026-07-24'
---

# 共享尺度标准大尾的仿射 Type I 递降射线

## 定理

令 \(p\equiv1\pmod{24}\) 为素数。取正整数

\[
a<b,\qquad h>0,\qquad t>0, \tag{1}
\]

满足

\[
p(a+b)=4abt-h,\qquad h\mid a^2t. \tag{2}
\]

定义

\[
x=at,\qquad y=bt,\qquad d=ht,
\qquad m=\frac{4a^2t+h}{a+b}. \tag{3}
\]

若 \(3\le m\le p-2\)，则 \((m,d)\) 是 \(p\) 的 Type I 除子证书；其恢复出的
第二分母正好是 \(y\)。

进一步有两个标准源切片。

1. 若 \(y\) 为偶数且 \(p/2<y<p\)，令 \(n=y\)。则
   \[
   \frac4n=\frac1{n/2}+\frac1n+\frac1n
   \quad\Longrightarrow\quad
   \frac4p=\frac1y+\frac1x+\frac1z. \tag{4}
   \]
2. 若 \(y\) 为偶数、\(n=y/2\) 满足 \(p/2<n<p\) 且 \(3\mid n\)，则
   \[
   \frac4n=\frac1{n/3}+\frac1{2n}+\frac1{2n}
   \quad\Longrightarrow\quad
   \frac4p=\frac1y+\frac1x+\frac1z. \tag{5}
   \]

其中 \(z\) 是 Type I 恢复公式给出的正整数。两条边都严格降低源分母秩。

反过来，考虑 even-standard-two-tail-descent 或
three-divisible-standard-two-tail-descent 中任一个因子见证。若其有序重组尾的首项
严格小于被保留大尾，记该项和大尾为 \(x<y\)，则该因子自动就是 Type I 除子 \(d\)。令

\[
t=\gcd(x,y). \tag{6}
\]

则 \(t\mid d\) 自动成立，令 \(a=x/t,b=y/t,h=d/t\) 后唯一恢复 (1)--(3)。
所以这个仿射模型恰好穷尽这两个标准大尾构造中 \(x<y\) 的因子见证。

## 证明

由 (2)，\(m\) 是整数；代入 (3) 得

\[
4x-p
=4at-\frac{4abt-h}{a+b}
=\frac{4a^2t+h}{a+b}=m. \tag{7}
\]

又 \(d=ht\mid a^2t^2=x^2\)，并且

\[
\begin{aligned}
my
 &=\frac{4a^2t+h}{a+b}\,bt\\
 &=\frac{4a^2bt^2+hbt}{a+b}\\
 &=\frac{(4abt-h)at+h t(a+b)}{a+b}\\
 &=px+d.
\end{aligned} \tag{8}
\]

故 \(m\mid px+d\)，这正是 Type I 条件。Bradford 的恢复公式给出

\[
y=\frac{px+d}{m},\qquad
z=\frac{p(x+px^2/d)}m. \tag{9}
\]

第一式与 (8) 一致。把 \(y=n\) 代入偶数标准恒等式，或把 \(y=2n\) 代入
三倍数标准恒等式，和 (9) 一起即给出 (4)--(5)。源分母 (n<p)，故递降严格。

反向部分由 \(a=x/t,b=y/t,h=d/t\) 直接给出。恒等式 \(my=px+d\) 和
\(m=4x-p\) 反解为 (2) 与 (3)，而 \(t=\gcd(x,y)\) 固定后坐标唯一。

还须说明上述反向的 Type I 性并非额外假设。两种标准大尾都满足

\[
R=4y-p,\qquad S=py,\qquad \gcd(R,S)=1.
\]

其因子构造给出 \(e=Ru-S\mid S^2\)。故模 \(e\) 有 \(Ru\equiv S\)；平方后利用
\(e\mid S^2\) 和 \(\gcd(R,e)=1\)，得到 \(e\mid u^2\)。又令 \(m=4u-p\)，则

\[
e=Ru-S=(4u-p)y-pu=my-pu.
\]

所以 \(e\) 正是 Type I 证书除子。最后 \(t=\gcd(u,y)\) 同时整除 \(my\) 与
\(pu\)，从而 \(t\mid e\)。这补全了反向的全部条件。

## 参数区间的含义

偶数标准源的秩为 \(n=bt\)。其严格范围 \(p/2<n<p\) 的非平凡端点化为

\[
bt(3a-b)>h, \tag{10}
\]

所以常见的可行区间是 \(a<b<3a\)。相对地，三倍数标准源的秩为 \(n=bt/2\)。
当 \(3a<b<7a\) 并满足

\[
bt(7a-b)>2h, \tag{11}
\]

它落在 \(p/2<n<p\)；这正解释了三倍数大尾分支可以进入小于 \(p/3\) 的缺口区间。
两类都还须检查 \(x\le p/2\)，等价于

\[
2at(b-a)>h. \tag{12}
\]

这些不等式只是把源秩、自然首分母和严格性显式化，并不保证对任意 \(p\) 存在
\((a,b,h,t)\)。

## 两个切片

偶数切片取

\[
(p,a,b,h,t)=(21169,82,107,3,114),
\]

给出 \((m,d)=(16223,342)\) 与

\[
(6099,12198,12198)\longmapsto(12198,9348,7057998628). \tag{13}
\]

三倍数切片取

\[
(p,a,b,h,t)=(8329,16,55,1,168),
\]

给出 \((m,d)=(2423,168)\) 与

\[
(1540,9240,9240)\longmapsto(9240,2688,1231359360). \tag{14}
\]

## 边界

该射线把两种已知的无条件标准源提升压缩到较小的 \((a,b,h,t)\) 参数空间，但并没有
为所有核心素数选择这些参数。若存在一个能覆盖全体 \(p\) 的参数选择规则，它才会成为
目标引理所需的全称递降分支；当前定理只给出精确、可核验的候选结构。
