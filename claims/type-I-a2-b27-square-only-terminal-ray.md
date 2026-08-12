---
kind: claim
claim_id: type-I-a2-b27-square-only-terminal-ray
title: (A,B)=(2,27) 的平方专用 Type I 终端射线
statement: 对核心素数 p=24h+1、合法 gap m=24c-1，置 s=h+c、x=6s。若 9|s 并令 C=s/9、d=4C，则 d|x^2，且 gap-m 的 Type I 证书条件等价于 m|27p+2；命中时正规形唯一为 (A,B,C)=(2,27,s/9)。该族通常不满足 d|x，因而严格位于完整 d|x 层之外。固定 m=1583 时，条件等价于 p=2521+341928a；该原始等差射线的每个素数项都给出直接 Type I terminal。其首项 p=2521 是双 G、七路 terminal dispatch 与完整 d|x 层的共同残差，却以 (m,d)=(1583,76) 终止。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - short-certificate-equivalence
  - type-I-coprime-factor-normal-form
  - type-I-complete-divisor-layer-normal-form
  - type-I-adaptive-d2r-global-family-boundary
topics:
  - type-I
  - square-divisor
  - square-only
  - terminal-first
  - internal-normal-form
  - dirichlet-ray
  - double-G
  - proof-boundary
sources:
  - claim: short-certificate-equivalence
    role: Type-I-divisor-reconstruction
  - claim: type-I-coprime-factor-normal-form
    role: exact-(A,B,C)-normal-form
  - claim: type-I-complete-divisor-layer-normal-form
    role: strict-d-divides-x-boundary
  - reproduction: reproductions/type_i_a2_b27_square_only_terminal_ray.py
    role: equivalence-and-control-verification
visibility: public
last_checked: '2026-08-12'
---

# \((A,B)=(2,27)\) 的平方专用 Type I 终端射线

## 1. 一个不在 \(d\mid x\) 层内的精确选择器

令

\[
p=24h+1,
\qquad 1\le c\le h,
\qquad m=24c-1,
\qquad s=h+c,
\qquad x=6s.
\tag{1}
\]

假设 \(9\mid s\)，写

\[
C=\frac{s}{9},
\qquad d=4C=\frac{4s}{9}.
\tag{2}
\]

**定理。** 此 \(d\) 是 gap \(m\) 的 Type I 除子证书，当且仅当

\[
\boxed{m\mid27p+2.}
\tag{3}
\]

命中时，证书的互素因子正规形精确为

\[
\boxed{(A,B,C)=(2,27,s/9).}
\tag{4}
\]

**证明。** 由 \(x=54C\)、\(d=4C\)，有

\[
\frac{x^2}{d}=729C=81s\in\mathbb N.
\tag{5}
\]

故 \(d\mid x^2\)。而

\[
px+d=54Cp+4C=2C(27p+2).
\tag{6}
\]

因为 \(p=24s-m\)，所以 \((s,m)=1\)；进而 \((2C,m)=1\)，因 \(m\) 为奇数且
\(C\mid s\)。因此 (6) 被 \(m\) 整除当且仅当 (3) 成立。

又

\[
x=2\cdot27\cdot C,
\qquad d=2^2C,
\qquad (2,27)=1,
\tag{7}
\]

所以 (4) 由 Type I 互素因子正规形给出，且其唯一性同样随之成立。证毕。

这是真正的**平方专用**分支：对每个 \(C\)，都有 \(d=4C\nmid54C=x\)，但仍由 (5)
给出 \(d\mid x^2\)。因此它不被完整 \(d\mid x\) 正规形覆盖，也不应把后者的空盒误读为
完整 Type I 的空盒。

该分支还可从单个移位整数直接检索。定义

\[
\mathscr D_{2,27}(p)=
\left\{
m\mid27p+2:
23\le m\le p-2,\quad m\equiv-p\pmod {216}
\right\}.
\tag{8}
\]

则 \(\mathscr D_{2,27}(p)\ne\varnothing\) 当且仅当本卡的
\((A,B)=(2,27)\) 分支在某个合法 gap 命中；对每个这样的 \(m\)，证书为

\[
x=\frac{p+m}{4},
\qquad d=\frac{p+m}{54}.
\tag{9}
\]

事实上 \(m\equiv-p\pmod{216}\) 等价于 \(9\mid(p+m)/24=s\)，而
\(m\equiv-p\pmod{24}\) 同时强制 \(m=24c-1\)。于是该有限因子盒与 (1)--(3)
双向等价；其输入只是 \(27p+2\) 的因子分解，不是对所有缺口的试探。

## 2. 一个直接穿过双 G 残差的无穷射线

固定

\[
m=1583=24\cdot66-1.
\tag{10}
\]

对 \(p=24h+1\)，条件 \(9\mid h+66\) 和 (3) 分别给出

\[
h\equiv6\pmod9,
\qquad
648h+29\equiv0\pmod{1583}.
\tag{11}
\]

第二式的解是 \(h\equiv105\pmod{1583}\)，且 \(105\equiv6\pmod9\)。故两者精确合并为

\[
\boxed{h=105+14247a,\qquad p=2521+341928a,\qquad a\ge0.}
\tag{12}
\]

对这个射线，

\[
C=19+1583a,
\qquad x=54C,
\qquad d=4C.
\tag{13}
\]

又 \(\gcd(2521,341928)=1\)，故 Dirichlet 定理保证 (10) 含无穷多个素数参数；每个这样的
核心素数由 (3) 直接终止。

首项是

\[
p=2521,\quad C=19,\quad (m,x,d)=(1583,1026,76),
\tag{14}
\]

从而

\[
\boxed{
\frac4{2521}
=\frac1{1026}+\frac1{1634}+\frac1{55610739}.}
\tag{15}
\]

这个点先前已被证明为完整 \(d\mid x\) Type I 层的空盒，也逃过七路 terminal dispatch。
它在 gap \(23\) 的 \((m,d)=(23,848)\) 证书则来自既有 \(3p+4\) 分支和外部递降桥；
(14) 是另一个 gap、另一个 \((A,B)\) 正规形的独立终端，并非该桥的重复表述。

更强地，对 \(p=2521\) 的每个合法 gap 和每个 \(d\mid x^2\) 完整枚举，恰得到

\[
(m,x,d)=(23,636,848),\qquad(1583,1026,76).
\tag{16}
\]

因此第一张已知桥和第二张本卡的 square-only certificate 一起耗尽了该控制点的完整 Type I
平方除子盒；该断言是具体控制点的有限容量事实，并不外推为任意 \(p\) 的分类。

## 3. 对全局出口目标的限度

本卡增加一个可由 \(27p+2\) 的因子和 \(p+m\equiv0\pmod{216}\) 检索的完整 terminal
分支，并明确关闭了双 G 代表点 \(2521\) 的一个原有 Type I 盲区。它仍只覆盖固定
\((A,B)=(2,27)\) 的射线，不构成全称 selector，也没有替代全局严格递降所需的势函数。
下一决定性问题是：把所有 \(d\nmid x\) 的正规形按 \((A,B)\) 的小因子结构分类后，能否证明
每个剩余 G 状态至少命中一个有限的 \((A,B)\) 菜单，或从其中构造可提升的严格递降。

定向复现：`python3 reproductions/type_i_a2_b27_square_only_terminal_ray.py --verify`
