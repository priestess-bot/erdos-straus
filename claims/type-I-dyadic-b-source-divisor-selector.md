---
kind: claim
claim_id: type-I-dyadic-b-source-divisor-selector
title: Type I 二进 B 源状态的奇部除子选择判据
statement: 设偶源状态满足 E=1+sR、K=(pR+1)/4、E|n^2/gcd(E,4)，其中 n=p-s。令 K=2^v K_0 且 K_0 为奇数。对 t>=1，存在 B=2^t 的自然 Type I 正规形最大尾反向边，当且仅当 t<=v 且存在 d|K_0，使 2^(v+t+2)d=-1 mod R 且 K_0/d>2^t；此时 C=2^(v-t)d、H=K_0/d、A=(H+2^t)/R 和 m=(2^(v+t+2)d+1)/R。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- normal-form
- even-source
- source-state
- divisor-residues
- dyadic
- selector
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I normal-form context
visibility: public
last_checked: '2026-07-28'
---

# Type I 二进 \(B\) 源状态的奇部除子选择判据

设 \(p\equiv1\pmod4\)，\(s\) 是正奇数，\(n=p-s\) 是严格更小的偶数。给定偶源桥状态

\[
E=1+sR,\qquad K=\frac{pR+1}{4},\qquad
E\mid\frac{n^2}{\gcd(E,4)}, \tag{1}
\]

其中 \(R\ge3\) 为奇数。写

\[
K=2^vK_0,\qquad K_0\text{ 为奇数}. \tag{2}
\]

## 定理

对任意 \(t\ge1\)，存在以该状态为桥、且

\[
B=2^t \tag{3}
\]

的自然 Type I 正规形最大尾反向边，当且仅当 \(t\le v\)，且存在正除子
\(d\mid K_0\)，满足

\[
2^{v+t+2}d\equiv-1\pmod R,\qquad
\frac{K_0}{d}>2^t. \tag{4}
\]

此时显式恢复

\[
C=2^{v-t}d,\qquad
H=\frac{K_0}{d},\qquad
A=\frac{H+2^t}{R},\qquad
m=\frac{2^{v+t+2}d+1}{R}. \tag{5}
\]

式 (5) 给出 \(K=BCH\)、\(p=4ABC-m\)，以及由 (1) 导出的严格偶源反向边。

## 证明

若边存在，令 \(D=BC\)、\(H=K/D\)。因为 \(B=2^t\) 且
\(\gcd(A,B)=1\)，\(A\) 为奇数。又 \(R\) 为奇数、\(B\) 为偶数且
\(H=AR-B\)，所以 \(H\) 也为奇数。因此 \(D\) 吸收 \(K\) 的全部二进因子：

\[
D=2^vd,\qquad d\mid K_0.
\]

故 \(t\le v\) 且 \(C=2^{v-t}d\)。正规形同余

\[
4B^2C+1\equiv0\pmod R
\]

正是 (4) 的第一个条件。另一方面，

\[
R(p-m)=4BC(H-B)-2,
\]

故自然缺口 \(m<p\) 等价于 \(H>B=2^t\)，即 (4) 的第二个条件。

反过来，取 (5)。第一个同余给出 \(R\mid4B^2C+1\)。又
\(4K\equiv1\pmod R\)，故

\[
4BCH=(4B^2C)\frac HB\equiv1\pmod R
\]

推出 \(H\equiv-B\pmod R\)，所以 \(A\) 为整数。这里 \(H\) 是奇数、\(B\) 为偶数，
故 \(A\) 为奇数，从而 \(\gcd(A,B)=1\)。第二个不等式保证 \(m<p\)；其余自然范围及
两边单位分数恒等式由一般源状态实现判据和 (1) 立即恢复。

## 两个边界状态

\[
\begin{array}{c|c|c|c|c|c}
p & (s,E) & (v,t) & d & (A,B,C) & m\\ \hline
63332329 & (1,48) & (1,1) & 91 & (86995,2,91) & 31\\
172657489 & (1,144) & (4,3) & 31 & (87025,8,62) & 111
\end{array}
\]

第二行正是五亿有限盒中 \(B\le7\) 的唯一偶源遗漏在 \(B=8\) 的恢复。对同一
\((p,s,E)=(172657489,1,144)\)，\(t=2\) 没有满足 (4) 的除子，故不能把该状态降为
\(B=4\)。

## 边界

本判据只在已经给定源状态 \((s,E)\) 后选择二进 \(B\)。它没有保证某个 \(E\) 或某个
\(t\) 对所有核心素数存在，因此不是混合终端选择引理的证明。

可复现命令：

~~~bash
python3 reproductions/type_i_dyadic_b_source_selector.py
python3 -m unittest tests/test_type_i_dyadic_b_source_selector.py -q
~~~
