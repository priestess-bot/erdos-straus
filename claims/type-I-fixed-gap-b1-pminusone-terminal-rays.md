---
kind: claim
claim_id: type-I-fixed-gap-b1-pminusone-terminal-rays
title: 每个自然缺口都有无穷Type I/II双终端重叠射线
statement: 对任意q,s>=1，令m=4q-1、C=q(6ms-1)。原始等差进程p=24sCv+1-24qms（v>=1）中的每个素数项都满足p=1 mod24，并同时具有两条严格边：其正规形(A,B,C)=(6sv-1,1,C)给出源p-1、桥因子E=24qs的Type I最大尾偶终端边；同一缺口m以Type II除子d=qA给出普通双尾边。因进程原始，Dirichlet定理给出每个固定(q,s)有无穷多个这样的核心素数。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- normal-form
- terminal-bridge
- even-source
- p-minus-one
- fixed-gap
- affine-progressions
- dirichlet
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-terminal-bridge-context
visibility: public
last_checked: '2026-07-28'
---

# 每个自然缺口都有无穷 Type I/II 双终端重叠射线

取任意正整数 \(q,s,v\)，并定义

\[
m=4q-1,\quad C=q(6ms-1),\quad A=6sv-1,
\]

以及

\[
R=24qs-1,\quad E=24qs=R+1,\quad B=1.
\]

令

\[
p=4AC-m=24sCv+1-24qms. \tag{1}
\]

每个固定的 \((q,s)\) 都给出关于 \(v\) 的一条双终端重叠射线。

## 一般 B 等于 1 重叠判据

先给出本构造使用的普适充分条件。设一张 \(B=1\) Type I 正规形

\[
p=4AC-m,\qquad mR=4C+1
\]

有源 \(p-1\) 的最大尾终端边。写

\[
m=4q-1,\qquad R=4r-1. \tag{2}
\]

源为 \(p-1\) 强制桥因子为 \(E=R+1=4r\)。若

\[
q\mid r, \tag{3}
\]

则同一缺口 \(m\) 自动有普通 Type II 双尾证书。事实上，

\[
C=\frac{mR-1}{4}=mr-q,
\]

所以 (3) 给出 \(q\mid C\)。取

\[
x=AC,\qquad d=qA.
\]

便有 \(d\mid x\)，且 \(C\equiv-q\pmod m\)，所以

\[
d=qA\equiv-AC=-x\pmod m. \tag{4}
\]

此外

\[
m+1=4q\mid4(AC-q)=p-1. \tag{5}
\]

因此 \(d\) 是普通 Type II 尾的除子，并可将两条 \(p\)-尾严格去缩放。反过来，这里
没有断言 \(q\nmid r\) 时普通尾一定失败；但它给出一个必要条件：同一缺口上真正只由
\(B=1\) 的 \(p-1\) Type I 桥补上的状态，必须有 \(q\nmid r\)。

## 正规形与 p 减一桥

首先

\[
mR=(4q-1)(24qs-1)=4C+1. \tag{6}
\]

因此 \((A,B,C)=(A,1,C)\) 是 \(p\) 在缺口 \(m\) 的 Type I 正规形。令

\[
H=AR-1,\qquad K=CH. \tag{7}
\]

由 (1)、(6)、(7) 得

\[
4K=pR+1. \tag{8}
\]

设 \(n=p-1\)。因为

\[
AC-q
=q\bigl((6ms-1)(6sv-1)-1\bigr)
=6qs(6msv-m-v), \tag{9}
\]

有 \(6qs\mid AC-q\)。再由 \(p-1=4(AC-q)\)，得到

\[
E=24qs\mid\frac{(p-1)^2}{4}=\frac{n^2}{4}. \tag{10}
\]

并且

\[
E=R+1\equiv1\pmod R,\qquad
\frac{4K-E}{R}=p-1=n. \tag{11}
\]

这里 \(A\ge5\)、\(C\ge17\)、\(R\ge23\)，故 \(K=C(AR-1)\ge R\)。于是

\[
E=R+1\le4K-2R, \tag{12}
\]

且 \(E\mid4K^2\) 由 (6) 或 p 减一桥等价式给出。故每个素数项有精确的目标和源分解

\[
\frac4p=\frac1{AC}+\frac1{ACH}+\frac1{pK},
\]

\[
\frac4{p-1}=\frac1{(p-1)K/E}+\frac1{AC}+\frac1{ACH}. \tag{13}
\]

这是一条以 \(p-1<p\) 为源的严格偶终端边。

## 同一缺口的普通 Type II 双尾

同一参数还自动给出普通 Type II 尾。令

\[
x=AC,\qquad d=qA.
\]

因为 \(C=q(6ms-1)\)，有 \(d\mid x\)，且模 \(m\) 有

\[
C\equiv-q,\qquad x=AC\equiv-qA,\qquad
d=qA\equiv-x\pmod m. \tag{14}
\]

所以 \(d\mid x^2\)、\(d\le x\)，并且是缺口 \(m\) 的 Type II 除子证书。又

\[
m+1=4q\mid4(AC-q)=p-1. \tag{15}
\]

故这张证书可将两条 \(p\)-尾同时去缩放，严格降到

\[
n_{\mathrm{II}}=\frac{p+m}{m+1}=\frac{AC}{q}<p. \tag{16}
\]

因此 (13) 的 Type I \(p-1\) 源边和 (16) 的普通 Type II 双尾边在同一个素数射线上
同时存在。

## 无穷性

将 (1) 写作

\[
p=Dv+a,\qquad
D=24sC,\qquad
a=1-24qms. \tag{17}
\]

显然 \(p\equiv1\pmod {24}\)。此外

\[
\gcd(D,a)=1. \tag{18}
\]

事实上，\(a\) 分别与 \(2,3,q,s\) 互素；又模 \(6ms-1\) 有

\[
a=-4q(6ms-1)-m\equiv-m,
\]

而 \(\gcd(m,6ms-1)=1\)。所以 (18) 成立。Dirichlet 关于算术级数中素数的定理保证：
每个固定 \((q,s)\) 的进程 (17) 中有无穷多个素数项，且每个都是上述 Type I 终端证书
所覆盖的核心素数。

例如 \(q=s=1\) 时

\[
(m,C,R,E,p)=(3,17,23,24,408v-71),
\]

前三个素数项 \(337,1153,2377\) 都有 \(B=1\)、源 \(p-1\) 的终端桥。\(q=2,s=1\)
则给出缺口 \(m=7\)、进程 \(p=1968v-335\)。

## 边界

本定理为每个固定自然缺口构造无穷多个两分支同时成功的正例，但不对给定核心素数选择
\(q,s,v\)。因此它不证明混合终端选择引理；它说明固定缺口的失败不能由该缺口本身解释，
后续的全称问题仍是跨缺口的自适应因子选择。

可复现命令：

~~~bash
python3 reproductions/type_i_fixed_gap_b1_terminal_rays.py
python3 -m unittest tests/test_type_i_fixed_gap_b1_terminal_rays.py -q
~~~
