---
kind: claim
claim_id: type-II-gap-59-crt-factor-pair-terminal-descent
title: gap-59 的 CRT 强制因子对终端与严格两尾递降射线
statement: >-
  设 p=24h+1 是素数，且 h=820 (mod 2065)，等价于
  h=0 (mod 5), h=1 (mod 7), h=-6 (mod 59)。令 x=(p+59)/4。
  则 d=21 满足 d|x、d<=x、59|(x+d)，故给出显式 gap-59 Type II 短证书。
  又 60|p-1，因子对 (A,B,C,K)=(1,x/21,21,(x/21+1)/59) 给出
  n=(p+59)/60<p 上的两尾解及不读取目标解的 lift。这一算术级数有无限多个素数
  p=19681 (mod 49560)，因而是一条无限的 terminal/marked-descent 射线；它包括
  先前固定 gap 55 反例 p=118801。本卡只覆盖该 CRT 子族，不构成 G 或 Type II 的
  全称出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - short-certificate-equivalence
  - type-II-coprime-factor-normal-form
  - type-II-factor-pair-carrier-strict-descent
  - type-I-type-II-mod-three-double-g-exit-obstruction
topics:
  - type-II
  - terminal-first
  - gap-59
  - crt-ray
  - factor-pair
  - marked-descent
  - two-tail-lift
  - double-G
  - proof-program
sources:
  - claim: short-certificate-equivalence
    role: Type-II-certificate-reconstruction
  - claim: type-II-coprime-factor-normal-form
    role: factor-pair-normalization
  - claim: type-II-factor-pair-carrier-strict-descent
    role: strict-two-tail-descent-and-lift
  - claim: type-I-type-II-mod-three-double-g-exit-obstruction
    role: p-118801-double-G-pressure-control
  - reproduction: reproductions/type_ii_gap_59_crt_factor_pair_terminal_descent.py
    role: CRT-ray-and-exact-identity-controls
visibility: public
last_checked: '2026-08-12'
---

# gap-59 的 CRT 强制因子对终端与严格两尾递降射线

## 1. 定理

令

\[
p=24h+1,
\qquad
h\equiv0\pmod5,
\qquad
h\equiv1\pmod7,
\qquad
h\equiv-6\pmod{59}.
\tag{1}
\]

由中国剩余定理，(1) 等价于

\[
h\equiv820\pmod{2065}.
\tag{2}
\]

特别地 $h\ge820$。令

\[
x=\frac{p+59}{4}=6h+15,
\qquad d=21,
\qquad n=\frac{p+59}{60}=\frac{2h}{5}+1.
\tag{3}
\]

**定理。** 每个满足 (1) 的素数 $p$ 都有 gap-59 的 Type II 证书

\[
\boxed{
\frac4p
=\frac1x
+\frac1{p\,21K}
+\frac1{p\,21BK},
\qquad
B=\frac{x}{21},\quad K=\frac{B+1}{59}.
}
\tag{4}
\]

同时，严格较小的 $n<p$ 有标记源解

\[
\boxed{
\frac4n
=\frac1x
+\frac1{21K}
+\frac1{21BK}.
}
\tag{5}
\]

因此保留首分母并将后两尾乘以 $p$ 的映射

\[
(x,21K,21BK)\longmapsto(x,p\,21K,p\,21BK)
\tag{6}
\]

是不读取目标解的显式 lift。式 (4) 在 terminal-first 顺序中已直接退出；式 (5)--(6)
额外提供同一证书的严格 marked descent 回执。

## 2. CRT 条件强制该证书

由 $h\equiv1\pmod7$，

\[
x=6h+15\equiv-h+1\equiv0\pmod7.
\tag{7}
\]

又 $3\mid x$，故 $d=21\mid x$，从而 $d\mid x^2$ 且 $d\le x$。由

\[
x+d=6h+36=6(h+6)
\tag{8}
\]

和 $h\equiv-6\pmod{59}$，得到 $59\mid x+d$。这正是 gap $59$ 的完整
Type II 除子条件，故已得到一个直接 terminal。

进一步，$h\equiv0\pmod5$ 蕴含

\[
60\mid24h=p-1,
\tag{9}
\]

且 $n$ 是正整数并严格小于 $p$。写 $x=21B$。由 (8) 以及

$59\nmid21$，有 $B\equiv-1\pmod{59}$，故 $K=(B+1)/59$ 为正整数。于是

\[
(A,B,C,K)=(1,B,21,K),
\qquad x=ABC,
\qquad A+B=59K.
\tag{10}
\]

这满足互素因子对正规形。将 (10) 代入既有的 factor-pair two-tail lift，便得到
(4)--(6)。这一步没有把任意 $4/n$ 的解错误提升为 $4/p$：它只作用于 (5) 指定的
两尾标记状态。

最后，(2) 给出

\[
p\equiv24\cdot820+1=19681\pmod{24\cdot2065=49560}.
\tag{11}
\]

而 $(19681,49560)=1$。Dirichlet 素数定理因此保证 (11) 中有无限多个素数；每一个
都属于本定理的核心素数射线。这是对无限 CRT 子族的结论，不能推出 gap 59 或有限
gap 菜单覆盖所有 G 状态。

## 3. 控制：双 G 压力点 $p=118801$

取 $h=4950$。它满足

\[
(h\bmod5,h\bmod7,h\bmod59)=(0,1,53)=(0,1,-6),
\tag{12}
\]

并给出

\[
p=118801,
\qquad x=29715,
\qquad d=21,
\qquad B=1415,
\qquad K=24,
\qquad n=1981.
\tag{13}
\]

故 (5) 与 (4) 分别为

\[
\frac4{1981}
=\frac1{29715}+\frac1{504}+\frac1{713160},
\tag{14}
\]

\[
\frac4{118801}
=\frac1{29715}+\frac1{59875704}+\frac1{84724121160}.
\tag{15}
\]

这解释了该双 G 反例为何在固定 gap 55 扇之后于 gap 59 首次命中；控制本身不声称
所有同类压力点都会命中这条 CRT 射线。
