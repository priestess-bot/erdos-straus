---
kind: claim
claim_id: gap-residue-reachability
title: 固定首分母缺口的精确除子残数判据
statement: 对 p=1 mod 4、m=3 mod 4、3<=m<=p-2，令 x=(p+m)/4 和 D_m(x)={d mod m:d|x^2}。则存在该缺口的 Type I 证书当且仅当 -4^{-1} 属于 D_m(x)，存在 Type II 证书当且仅当 -x 属于 D_m(x)；后者的 d<=x 条件自动可满足。
claim_status: established
topics:
- certificate
- divisors
- congruences
- type-I-II
sources:
- paper: bradford2024
  locator: "Propositions 1--2"
  role: primary-certificate-criterion
visibility: public
last_checked: '2026-07-23'
---

# 固定首分母缺口的精确除子残数判据

## 精确表述

令 \(p\equiv1\pmod4\) 为素数，\(m\equiv3\pmod4\)、\(3\le m\le p-2\)，并令

\[
x=\frac{p+m}{4},\qquad
D_m(x)=\{d\bmod m:d\mid x^2\}.
\]

则 \(\gcd(x,m)=1\)，而且：

\[
\begin{aligned}
\text{Type I at gap }m&\Longleftrightarrow -4^{-1}\in D_m(x),\\
\text{Type II at gap }m&\Longleftrightarrow -x\in D_m(x).
\end{aligned}
\]

## 证明

若公因子同时整除 \(x\) 和 \(m=4x-p\)，它也整除 \(p\)。但 \(0<x<p\)，故该公因子只能是 \(1\)。

Bradford 的 Type I 条件是某个 \(d\mid x^2\) 满足 \(d\equiv-4x^2\pmod m\)。令 \(e=x^2/d\)，则

\[
e\equiv \frac{x^2}{-4x^2}\equiv-4^{-1}\pmod m.
\]

该变换可逆，给出第一条。Type II 条件是 \(d\mid x^2\)、\(d\le x\)、\(d\equiv-x\pmod m\)。若一个除子 \(e\) 满足 \(e\equiv-x\pmod m\)，其配对除子 \(x^2/e\) 也满足同一同余，因为

\[
\frac{x^2}{-x}\equiv-x\pmod m.
\]

\(e\) 与 \(x^2/e\) 至少一个不超过 \(x\)，所以 \(d\le x\) 自动可强制。反向蕴含直接来自原条件。

## 作用与边界

该判据把固定缺口问题化为有限阿贝尔群 \((\mathbb Z/m\mathbb Z)^\times\) 中的除子残数可达性；它没有证明存在一个对所有 \(p\) 有效的小 \(m\)。

## 除子格的边界分类

对任意上述合法 \((p,m,x)\)，这些边界候选没有新的隐藏分支：

\[
\begin{array}{c|c}
\text{候选} & \text{结论}\\
\hline
\text{Type I},\ d=1 & \text{不可能}\\
\text{Type I},\ d=x & m\mid p+1\\
\text{Type I},\ d=x^2 & \text{不可能}\\
\text{Type II},\ d=1 & m\mid p+4\\
\text{Type II},\ d=x & \text{不可能}
\end{array}
\]

证明如下。Type I 的 \(d=1\) 条件等价于 \(m\mid p^2+4\)，因为

\[
4(px+1)=p^2+pm+4.
\]

但 \(m\equiv3\pmod4\) 含有一个 \(q\equiv3\pmod4\) 素因子。若
\(q\mid p^2+4\)，则 \((p/2)^2\equiv-1\pmod q\)，与 \(-1\) 在此类素数模下
不是平方矛盾。因此 Type I 的 \(d=1\) 不可能。

对于 \(d=x\)，利用 \(\gcd(x,m)=1\)，Type I 条件
\(m\mid x(p+1)\) 正好化为 \(m\mid p+1\)；Type II 条件
\(m\mid2x\) 会推出 \(m\mid p\)，与 \(m<p\) 矛盾。对于 Type I 的
\(d=x^2\)，条件 \(m\mid x(p+x)\) 化为 \(m\mid p+x\)，再乘以 \(4\) 得
\(m\mid5p\)。因 \(\gcd(m,p)=1\)，这将迫使 \(m\mid5\)，不可能
\(m\equiv3\pmod4\)。最后 Type II 的 \(d=1\) 条件 \(m\mid x+1\)
在乘以 \(4\) 后正好等价于 \(m\mid p+4\)。

所以在 `p-plus-one-sqrt-certificate` 和 `p-plus-four-sqrt-certificate` 都失败的残余集中，
任何证书都必须使用真正的内部除子：Type I 的 \(d\notin\{1,x,x^2\}\)，
Type II 的 \(1<d<x\)。
