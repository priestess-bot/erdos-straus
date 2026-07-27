---
kind: claim
claim_id: type-I-b5-dyadic-terminal-ray
title: B等于5、E等于32的无穷Type I终端射线
statement: 令 p=757200t+21169，其中t>=0且p为素数。则p=1 mod24，且p具有以n=p-1为严格偶源的Type I最大尾反向边：其正规形为(A,B,C)=(30t+1,5,1262)，缺口m=4071，K=5*1262*(31A-5)，目标因子E=32。特别地，p在原始等差进程21169 mod757200中取素数值时给出无穷多个具有该固定终端证书的核心素数。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- normal-form
- even-source
- terminal-bridge
- dyadic
- affine-progressions
- dirichlet
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-terminal-bridge-context
visibility: public
last_checked: '2026-07-28'
---

# B 等于 5、E 等于 32 的无穷 Type I 终端射线

令 \(t\ge0\)，并定义

\[
A=30t+1,\quad p=757200t+21169,\quad H=31A-5,
\]

以及

\[
B=5,\quad C=1262,\quad R=31,\quad E=32,\quad m=4071.
\]

若 \(p\) 是素数，则 \(p\equiv1\pmod{24}\)。以下构造在每个这样的素数项上给出一条严格
Type I 终端反向边。

## 正规形与目标证书

置

\[
K=BCH=5\cdot1262\cdot(31A-5).
\]

由

\[
4B^2C+1=126201=31\cdot4071=mR \tag{1}
\]

及 \(p=4ABC-m\)，得到正规形 \((A,B,C)\) 的自然 Type I 证书。其相关的尾参数满足

\[
4K=pR+1. \tag{2}
\]

事实上，代入 \(H=AR-B\)，左端为

\[
4BCH=R(4ABC)-(4B^2C)=R(4ABC-m)+1=pR+1.
\]

于是目标端具有分解

\[
\frac4p=\frac1{ABC}+\frac1{ACH}+\frac1{pK}. \tag{3}
\]

## 严格偶源桥

取 \(n=p-1\)。由于

\[
p-1=16(47325t+1323), \tag{4}
\]

有

\[
E=32\mid\frac{n^2}{4}.
\]

同时

\[
E=32\equiv1\pmod {31}=1\pmod R, \tag{5}
\]

而 \(K=12620(465t+13)\)，故 \(E\mid4K^2\)。由最小点 \(t=0\) 已有

\[
E=32\le4K-2R,
\]

且右端随 \(t\) 增长。这验证了目标因子 \(E\) 的偶终端条件。把 (2) 减去 \(E\) 后除以
\(R\)，可得

\[
\frac{4K-E}{R}=p-1=n. \tag{6}
\]

因此源端的精确分解为

\[
\frac4n=\frac1{nK/E}+\frac1{ABC}+\frac1{ACH}. \tag{7}
\]

这里 \(2\le n<p\)，所以 (7) 是严格递降；(3) 和 (7) 共享后两个分母，正是该正规形
给出的最大尾严格反向边。

## 无穷性与边界

等差进程是原始的：

\[
\gcd(21169,757200)=1,\quad 24\mid757200,\quad21169\equiv1\pmod{24}.
\]

Dirichlet 关于算术级数中素数的定理遂保证 \(21169+757200t\) 含无穷多个素数项；每个
素数项都由上面的固定 \((B,C,E,m,R)=(5,1262,32,4071,31)\) 构造覆盖。

这是一条无限的正证书射线，也是点 \(p=21169\) 的 \(B=5,E=32\) 现象并非孤立的明确证据。
但它不证明所有核心素数属于这条进程，也不证明同一进程上的其它点没有 \(B\le4\) 证书；故它
既不是混合终端选择引理，也不是 \(B=5\) 的全局下界。

可复现命令：

~~~bash
python3 reproductions/type_i_b5_dyadic_terminal_ray.py
python3 -m unittest tests/test_type_i_b5_dyadic_terminal_ray.py -q
~~~
