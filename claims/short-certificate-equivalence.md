---
kind: claim
claim_id: short-certificate-equivalence
title: 首分母缺口除子证书与素数实例等价
statement: 对任意素数 p=1 mod 4，4/p 的有序三项单位分数分解存在，当且仅当存在 m=3 mod 4、3<=m<=p-2 与 d|((p+m)/4)^2，使得 Type I 的 m|p(p+m)/4+d 或 Type II 的 d<=(p+m)/4 且 m|(p+m)/4+d 成立；两种情形均可显式恢复分母。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- divisor-parametrization
- certificate
- type-I-II
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1--4 (Propositions 2 and 4 are stated but their proofs are left to the reader)"
  role: statement-and-reconstruction-context
- paper: elsholtz_tao2013
  locator: "Section 2"
  role: type-classification
- paper: bello2026
  locator: "Proposition 2 and Theorem 5"
  role: fab-completeness
visibility: public
last_checked: '2026-08-26'
---

# 首分母缺口除子证书与素数实例等价

## 精确表述

令 \(p\equiv1\pmod4\) 为素数，\(m=4x-p\)。则

\[
\left\lceil\frac p4\right\rceil\le x\le\frac p2
\quad\Longleftrightarrow\quad
3\le m\le p-2,\quad m\equiv3\pmod4,\quad x=\frac{p+m}{4}.
\]

在此变量替换下，Bradford 的两类证书变成：

\[
\begin{aligned}
\mathrm{I}:&\quad d\mid x^2,\qquad m\mid px+d;\\
\mathrm{II}:&\quad d\mid x^2,\quad d\le x,\qquad m\mid x+d.
\end{aligned}
\]

第一条中的 \(px\equiv4x^2\pmod m\)，故也可写作 \(m\mid4x^2+d\)。

若 I 成立，取

\[
y=\frac{px+d}{m},\qquad
z=\frac{p(x+px^2/d)}m;
\]

若 II 成立，取

\[
y=\frac{p(x+d)}m,\qquad
z=\frac{p(x+x^2/d)}m.
\]

所得 \((x,y,z)\) 分别是 Type I、Type II 解。反向地，对任一有序素数解，
下面给出仓库内的完整代数推导，而不把 Bradford 未展开的 Proposition 4 当作证明。

## 反向完备性的独立证明

设

\[
\frac4p=\frac1x+\frac1y+\frac1z,
\quad x\le y\le z,
\quad m=4x-p.
\]

由正性和 \(4/p\le3/x\) 得 \(p/4<x\le3p/4<p\)，所以 \(m>0\)、
\(p\nmid x\)。又

\[
\gcd(p,m)=\gcd(p,4x-p)=\gcd(p,4x)=1.
\]

把剩余两项通分可得

\[
myz=px(y+z),
\]

进而有关键因子恒等式

\[
(my-px)(mz-px)=p^2x^2. \tag{1}
\]

两个因子都为正，因为
\(m/(px)=1/y+1/z>1/y,1/z\)。将
\(myz=px(y+z)\) 模 \(p\) 化简，并使用 \(p\nmid m\)，得到
\(p\mid yz\)。必要时交换 \(y,z\)，可固定 \(p\mid z\)。
若只有这一项被 \(p\) 整除，交换后虽然未必仍有 \(y\le z\)，但仍保留
\(y,z\ge x\)，这正是下面 Type I 上界所需的全部顺序信息。若两项都被
\(p\) 整除，则不必交换，并保留 \(y\le z\)。

### Type I

若 \(p\nmid y\)，令

\[
d=my-px.
\]

由上面已经证明的 \(p\nmid m\)，有

\[
d\equiv my\not\equiv0\pmod p,
\]

即 \(\gcd(d,p)=1\)。式 (1) 给出 \(d\mid p^2x^2\)，故可消去
\(p^2\) 而得到 \(d\mid x^2\)。又
\(\gcd(x,m)=\gcd(x,p)=1\)，所以 \(\gcd(d,m)=1\)。
定义 \(e=x^2/d\)，则

\[
y=\frac{px+d}{m},
\quad
z=\frac{p(x+px^2/d)}m.
\]

同时 \(d\equiv-px\pmod m\)。利用 \(p\equiv4x\pmod m\) 和
\(\gcd(d,m)=1\)，从 \(d\equiv-4x^2=-4de\pmod m\) 还得到

\[
4e\equiv-1\pmod m. \tag{2}
\]

下面证明该情形不会越过自然首分母上界。若
\(h=2x-p>0\)，由 \(y\ge x\) 得

\[
d\ge x(m-p)=2xh,
\quad
e\le\frac{x}{2h}.
\]

又由 (2) 的正整数整除关系，

\[
m=p+2h\le4e+1\le\frac{2x}{h}+1=\frac ph+2.
\]

乘以 \(h\) 后化为

\[
(h-1)(p+2h)\le0.
\]

所以正整数 \(h\) 只能等于 \(1\)，即唯一待排除边界是
\(x=(p+1)/2\)、\(m=p+2=2x+1\)。此时 Type I 同余给出
\(d\equiv-1\pmod m\)，故 \(d\ge2x\)。因为 \(x\) 为奇数且
\(d\mid x^2\)，实际上 \(d>2x\)，从而

\[
0<4e+1<m,
\]

这与 (2) 矛盾。因此 Type I 必有 \(x\le(p-1)/2\)。

### Type II

若 \(p\mid y,z\)，写 \(y=pY,z=pZ\)。原方程化为

\[
mYZ=x(Y+Z),
\]

并给出

\[
(mY-x)(mZ-x)=x^2. \tag{3}
\]

令 \(d=mY-x\)。两个因子为正，且 \(Y\le Z\)，所以由 (3)
得到

\[
d\mid x^2,
\quad
d\le x,
\quad
m\mid x+d.
\]

相应恢复式正是

\[
y=\frac{p(x+d)}m,
\quad
z=\frac{p(x+x^2/d)}m.
\]

又因 \(m\) 整除正整数 \(x+d\)，

\[
m\le x+d\le2x.
\]

代入 \(m=4x-p\) 得 \(x\le p/2\)，而 \(p\) 为奇数，所以
\(x\le(p-1)/2\)。

两种情形均得到

\[
3\le m=4x-p\le p-2,
\quad
m\equiv3\pmod4.
\]

这证明自然范围内的 Type I/II 除子枚举对所有有序素数解反向完备。

## 可验证性

证书只含一个类型位与 \((m,d)\)（\(x=(p+m)/4\) 可重建）。其二进制长度至多

\[
1+\lceil\log_2 p\rceil+\lceil2\log_2p\rceil,
\]

因为 \(m<p\)、\(d\le x^2<p^2/4\)。所有整除检查和分母恢复都使用 \(O(\log p)\) 位整数。因此这是关于给定 \(p\) 的短可核验证书；它不是对所有 \(p\) 都能找到证书的证明。

## 边界条件

将 \(m\) 限制为 \(m\le H(p)\) 会产生一个更强的“短缺口”命题。已知等价定理只允许 \(H(p)=p-2\)；任何固定、对数或幂次上界都须单独证明。有限范围内找到小 \(m\) 只能构成实验事实。

## 与 fab 参数的最小化等价

令 \(g(p)\) 是上述所有 I/II 证书中的最小缺口 \(m\)，令

\[
h(p)=\min\{\operatorname{fab}(p,a,b)>0:a,b\in\mathbb N\}.
\]

在 \(4/p\) 可解时，\(g(p)=h(p)\)。`fab` 的 Proposition 2 给出一个解，其中一个分母是 \((p+k)/4\)；把三个分母重排后，最小分母不大于它，故对应缺口不大于 \(k\)，于是 \(g(p)\le h(p)\)。反过来，最小缺口的解乘以 \(4\) 后成为 \(1/p\) 且三个分母均为 \(4\) 的倍数，Theorem 5 产生一个可采纳的 \(k\le g(p)\)，故 \(h(p)\le g(p)\)。

这只是两个优化语言的严格对应。它把有限 `fab` 筛的记录与首分母缺口实验连接起来，并不证明 \(g(p)\) 有统一上界。
