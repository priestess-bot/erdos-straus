---
kind: claim
claim_id: type-I-b1-pminusone-same-gap-dichotomy
title: B等于1的p减一终端桥与同缺口Type II的精确二分
statement: 设一张B=1的Type I正规形以源p-1具有最大尾偶终端桥。写m=4q-1、R=4r-1、C=mr-q、p=4AC-m。则该桥存在当且仅当r整除q^2(A+1)^2；同一缺口存在普通Type II双尾证书当且仅当q整除Ar。后一条件失败时，已存在的Type I桥不能由同一缺口的普通Type II双尾替代。特别地，原始进程p=7896t+913中的每个素数项都有该Type I桥而没有同缺口Type II双尾。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- type-II
- p-minus-one
- b1
- terminal-bridge
- same-gap
- divisor-residues
- affine-progressions
- dirichlet
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-and-Type-II-certificate-context
visibility: public
last_checked: '2026-07-28'
---

# B 等于 1 的 p 减一终端桥与同缺口 Type II 的精确二分

这张图表给出此前 (q\nmid r) 充分重叠判据的精确版本。它区分的是**同一缺口**上的普通
Type II 双尾；不排除同一素数在其他缺口拥有 Type II 证书。

## 定理

设 (p\equiv1\pmod {24}) 是素数，且有一张 (B=1) 的 Type I 正规形

\[
p=4AC-m,\qquad mR=4C+1.
\]

若其最大尾反向提升的源为 (p-1)，则桥因子必为 (E=R+1)。写

\[
m=4q-1,\qquad R=4r-1,\qquad C=mr-q. \tag{1}
\]

则该 (p-1) 偶终端桥存在当且仅当

\[
r\mid q^2(A+1)^2. \tag{2}
\]

并且，在这个相同缺口 (m) 上，存在可同时去除两条 (p)-尾的普通 Type II 证书当且仅当

\[
q\mid Ar. \tag{3}
\]

条件 (2) 与 (3) 可以同时成立，也可以仅有 (2)。后者是这一图表中真正由 Type I 分支提供、
而不能被**同缺口**普通 Type II 双尾替代的精确状态。

## p 减一桥的因子条件

源为 (p-1) 强制

\[
E=R+1=4r.
\]

令

\[
t=\frac{p-1}{4}=AC-q. \tag{4}
\]

由 (4K=pR+1) 得

\[
K=pr-t\equiv-t\pmod r.
\]

因此桥的平方因子条件等价于

\[
E\mid4K^2
\quad\Longleftrightarrow\quad
r\mid t^2. \tag{5}
\]

这里它也保证 (E\mid(p-1)K)：由 (K\equiv-t\pmod r) 可得 (r\mid tK)。其余桥条件
(E\equiv1\pmod R)、偶性以及自然范围由 (E=R+1) 和正规形自动满足。

从 (1) 得

\[
t=A(mr-q)-q\equiv-q(A+1)\pmod r.
\]

代入 (5) 正好给出 (2)。反过来同样逐步逆推，故 (2) 是充要而非仅充分条件。

## 同缺口普通 Type II 的充要条件

普通双尾去缩放必须满足

\[
m+1=4q\mid p-1=4(AC-q),
\]

即 (q\mid AC)。又由 (C=mr-q\equiv-r\pmod q)，这等价于 (3)。这是必要性。

反过来，若 (q\mid Ar)，则 (q\mid AC)。令

\[
x=AC,\qquad d=qA.
\]

由于 (C\ge q)，有 (d\le x)；又 (q\mid AC) 给出 (d\mid x^2)。并且

\[
d=qA\equiv-AC=-x\pmod m. \tag{6}
\]

所以 (d) 是 Type II 除子证书，而 (4q\mid p-1) 使其两条 (p)-尾严格去缩放到

\[
n=\frac{p+m}{m+1}=\frac{AC}{q}<p.
\]

这证明 (3) 的充分性和定理。

## 无穷个同缺口非重叠的 Type I 点

取

\[
q=7,\quad r=2,\quad m=27,\quad C=47,\quad R=7,
\]

并令

\[
A=42t+5,\qquad p=4AC-m=7896t+913. \tag{7}
\]

这里 (p\equiv1\pmod {24})，且

\[
\gcd(7896,913)=1.
\]

故 Dirichlet 定理给出 (7) 中无穷多个素数项。对每个此类项，(A) 为奇数，故

\[
2\mid7^2(A+1)^2,
\]

于是 (2) 给出因子 (E=8) 的 (p-1) Type I 终端桥；另一方面

\[
Ar=2(42t+5)\equiv3\pmod7,
\]

所以 (3) 失败，普通 Type II 双尾不可能在缺口 (27) 出现。前三个素数项为

\[
32497,\quad64081,\quad79873.
\]

这只说明 Type I 机制在该**同缺口**图表中确有无穷独立作用；它并不排除这些素数的其他 Type II
证书，也不构成全局选择引理的证明。

## 五亿残余核验

在完整五亿普通 Type II 尾遗漏集所选的 1,400 条 (p-1,B=1) 桥中，逐条重建均满足 (2)，
并且全部违反 (3)。因此此前观察到的 (q\nmid r) 实际上可强化为精确的

\[
q\nmid Ar.
\]

这把下一阶段的因子问题固定为：如何利用

\[
r\mid q^2(A+1)^2,\qquad q\nmid Ar
\]

产生另一缺口的证书、另一 Type I 桥，或可下降的替代状态。

可复现命令：

~~~bash
python3 reproductions/type_i_b1_pminusone_same_gap_dichotomy.py
python3 -m unittest tests/test_type_i_b1_pminusone_same_gap_dichotomy.py -q
~~~
