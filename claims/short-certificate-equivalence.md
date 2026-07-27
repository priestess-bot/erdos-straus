---
kind: claim
claim_id: short-certificate-equivalence
title: 首分母缺口除子证书与素数实例等价
statement: 对任意素数 p=1 mod 4，4/p 的有序三项单位分数分解存在，当且仅当存在 m=3 mod 4、3<=m<=p-2 与 d|((p+m)/4)^2，使得 Type I 的 m|p(p+m)/4+d 或 Type II 的 d<=(p+m)/4 且 m|(p+m)/4+d 成立；两种情形均可显式恢复分母。
claim_status: established
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
last_checked: '2026-07-24'
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
Elsholtz--Tao 的整除型分类先将其归入 I 或 II；将相应的两分母因子分解代入，
便得到上述 \(d\mid x^2\) 与同余条件，令 \(m=4x-p\) 即得到证书。
Bradford 的 Propositions 3--4 陈述同一必要条件；其出版文本只展开证明了
Proposition 3，故这里不把 Proposition 4 当作未经复核的证明来源。

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
