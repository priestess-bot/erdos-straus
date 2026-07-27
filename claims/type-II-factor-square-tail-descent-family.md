---
kind: claim
claim_id: type-II-factor-square-tail-descent-family
title: q 平方因子给出的 Type II 双尾递降同余族
statement: 设 m=4q-1，且 d|q^2。若 t>=1 满足 t=-4d-1 (mod m)、6|qt、d<=q(t+1)，并且 p=4qt+1 为素数，则 p=1 (mod24)，x=(p+m)/4=q(t+1) 与 d 构成 Type II 证书，且 m+1|p-1，所以双尾去 p 严格递降到 n=t+1。6|q 是使核心同余自动成立的充分条件；更一般地，只要 t 的两条同余条件相容，就得到一个互素的核心素数算术进程。
claim_status: established
topics:
- type-II
- descent
- congruence-certificate
- explicit-family
- dirichlet-progressions
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-26'
---

# \(q^2\) 因子给出的 Type II 双尾递降同余族

这是一族可显式验证的正例，不是跨缺口选择器的全称证明。令

\[
m=4q-1,\qquad d\mid q^2. \tag{1}
\]

取任意整数 \(t\ge1\)，满足

\[
t\equiv-4d-1\pmod m,\qquad 6\mid qt,\qquad d\le q(t+1), \tag{2}
\]

并设

\[
p=4qt+1 \tag{3}
\]

为素数。由 \(6\mid qt\) 得 \(p\equiv1\pmod {24}\)，并且 \(4/p\) 有一张 Type II
证书；更强地，它是由两条 \(p\)-尾同时去 \(p\) 所给出的严格递降，源分母为

\[
n=t+1<p. \tag{4}
\]

## 证书与递降

令

\[
x=\frac{p+m}{4}=q(t+1). \tag{5}
\]

由 \(d\mid q^2\) 得 \(d\mid x^2\)。又 \(4q=m+1\)，故
\(q\equiv4^{-1}\pmod m\)。从 (2) 得

\[
x\equiv q(-4d)\equiv-d\pmod m. \tag{6}
\]

而 \(\gcd(q,m)=1\)，故 \(\gcd(d,m)=1\)。因此 (6) 与 \(d\mid x^2\)
正是 Type II 除子判据；特别地，\(d\le x\) 已由 (2) 保证。显式地，

\[
\frac4p=
\frac1x+
\frac1{p(x+d)/m}+
\frac1{p(x+x^2/d)/m}. \tag{7}
\]

两条后尾均含 \(p\)。又 \(m+1=4q\mid p-1\)，所以双尾去 \(p\) 引理给出

\[
\frac4{t+1}=
\frac1x+
\frac1{(x+d)/m}+
\frac1{(x+x^2/d)/m}. \tag{8}
\]

这正是 (4) 的严格源解。

## 无穷性与例子

若 \(6\mid q\)，核心同余无需再限制 \(t\)，这正是此前采用的简单充分条件。更一般地，
令 \(L=6/\gcd(q,6)\)，并把 (2) 的核心条件写作 \(t\equiv0\pmod L\)。只要它与
\(t\equiv-4d-1\pmod m\) 相容，\(p\) 便落在一个模 \(4qmL\) 的互素算术进程：它模
\(4q\) 为 \(1\)，模 \(m\) 为 \(-4d\)，模 \(L\) 为 \(1\)。Dirichlet 的算术进程
素数定理因而给出无穷多个素数，且充分靠后的项自动满足其余不等式。

例如：

| \(q\) | \(m\) | \(d\) | 一个 \(t\) | \(p\) | 源 \(n\) |
|---:|---:|---:|---:|---:|---:|
| 6 | 23 | 1 | 18 | 433 | 19 |
| 12 | 47 | 4 | 77 | 3,697 | 78 |
| 18 | 71 | 36 | 139 | 10,009 | 140 |

该一般化也覆盖 H19-k23 残余中出现的 \(m=31\) 小除子机制。取
\(q=8,d=8\)，则 \(m=31\)，并要求

\[
t\equiv29\pmod{31},\qquad 3\mid t.
\]

在 \(p=57\,671\,384\,918\,508\,001\) 时，\(t=(p-1)/32\) 满足这些条件；
\(d=8\) 给出 \(m=31\) 的 Type II 证书和严格双尾递降。它对应 262,144 层中一条
原最小共享缺口 \(m=27\) 而以 \(m=31\) 闭合的记录。

最后一行正是此前 \(m=71\)、\(d=36\) 族的一个实例。该定理构造无穷多条
可递降进程，但没有说明任意给定核心素数应落在哪一条进程，故不能替代待证的因子选择器。
