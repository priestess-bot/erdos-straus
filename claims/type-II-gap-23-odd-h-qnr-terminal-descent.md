---
kind: claim
claim_id: type-II-gap-23-odd-h-qnr-terminal-descent
title: 奇 h 的 gap-23 二次非剩余 Type II 终端与两尾递降
statement: >-
  设 p=24h+1 为核心素数且 h 为奇数，令 x=(p+23)/4=6(h+1)。若 p 是模 23 的
  二次非剩余，则下表唯一指定的 d 属于 x^2、满足 d<=x 与 23|(x+d)，故给出 gap 23
  的显式 Type II 证书。该证书还规范地给出 n=(p+23)/24=h+1<p 的标记两尾解及
  显式 lift (ABC,ACK,BCK)->(ABC,pACK,pBCK)。因此这一分支既是原始 p 的
  terminal，也有不读取目标解的严格分母递降回执。p=2521 的双 G 控制点属于
  p=14 (mod 23)、d=8 这一行。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - short-certificate-equivalence
  - type-II-coprime-factor-normal-form
  - type-II-factor-pair-carrier-strict-descent
  - type-II-shared-gap-23-automatic-fan
  - type-I-type-II-mod-three-double-g-exit-obstruction
topics:
  - type-II
  - terminal-first
  - gap-23
  - quadratic-nonresidue
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
    role: strict-two-tail-descent
  - reproduction: reproductions/type_ii_gap_23_odd_h_qnr_terminal_descent.py
    role: residue-table-and-lift-controls
visibility: public
last_checked: '2026-08-12'
---

# 奇 \(h\) 的 gap-23 二次非剩余 Type II 终端与两尾递降

## 1. 定理

令

\[
p=24h+1,
\qquad h\ \text{为奇数},
\qquad x=\frac{p+23}{4}=6(h+1).
\tag{1}
\]

模 \(23\) 的二次非剩余恰为

\[
\operatorname{QNR}_{23}
=\{5,7,10,11,14,15,17,19,20,21,22\}.
\tag{2}
\]

对每个 \(r\in\operatorname{QNR}_{23}\)，下表给出唯一的 \(d\)：

| \(p\bmod23=r\) | 19 | 15 | 11 | 7 | 22 | 14 | 10 | 21 | 5 | 20 | 17 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(d\) | 1 | 2 | 3 | 4 | 6 | 8 | 9 | 12 | 16 | 18 | 36 |

**定理。** 若 \(p\bmod23\in\operatorname{QNR}_{23}\)，表中 \(d\) 满足

\[
d\mid x^2,
\qquad d\le x,
\qquad23\mid x+d.
\tag{3}
\]

故 \((m,d)=(23,d)\) 是 \(p\) 的 Type II 除子证书，分母为

\[
\boxed{
\frac4p
=\frac1x
+\frac1{p(x+d)/23}
+\frac1{p(x+x^2/d)/23}.
}
\tag{4}
\]

这条 terminal 同时带有严格的标记递降。令

\[
g=(d,x),\qquad A=\frac dg,\qquad B=\frac xg,
\qquad C=\frac gA,
\qquad K=\frac{A+B}{23},
\qquad n=\frac{p+23}{24}=h+1.
\tag{5}
\]

则 \(x=ABC\)、\((A,B)=1\)、\(d=A^2C\)、\(A+B=23K\)，并且

\[
\frac4n=\frac1{ABC}+\frac1{ACK}+\frac1{BCK},
\qquad
\frac4p=\frac1{ABC}+\frac1{pACK}+\frac1{pBCK}.
\tag{6}
\]

定义显式非空标记集

\[
W_{p,d}=\{(ABC,ACK,BCK)\}\subseteq\operatorname{Sol}(n).
\tag{7}
\]

则在 \(W_{p,d}\) 的全部元素上，

\[
\Phi_{p,d}(ABC,ACK,BCK)=(ABC,pACK,pBCK)
\tag{8}
\]

是不读取目标已知解的显式全域 lift，且 \(n=h+1<p\)。本卡不把 (8) 误称为
\(\operatorname{Sol}(n)\) 上的全域提升；它的域是明确的 factor-pair 标记状态，
而式 (4) 已足以作为原始 \(p\) 的 terminal。

## 2. 证明

由 \(h\) 为奇数，\(h+1\) 为偶数，从而

\[
12\mid x.
\tag{8}
\]

表中每一个 \(d\) 都整除 \(144\)，所以 (8) 给出 \(d\mid x^2\)。除
\(d=36\) 外，所有表中 \(d\) 至多 \(24\)，而核心域中 \(h\ge3\)、\(x\ge24\)。
若 \(d=36\)，表的剩余条件为 \(p\equiv17\pmod {23}\)，即
\(h\equiv16\pmod {23}\)；再用 \(h\) 为奇数得 \(h\ge39\)，故仍有 \(36\le x\)。

各列满足

\[
r\equiv-4d\pmod {23}.
\tag{9}
\]

这些 \(r\) 正好是 (2) 的十一项；也可由

\[
\operatorname{QR}_{23}
=\{1,2,3,4,6,8,9,12,13,16,18\}
\tag{10}
\]

直接验算。又 \(4x=p+23\)，所以由 (9)

\[
4(x+d)=p+23+4d\equiv0\pmod {23}.
\tag{11}
\]

由于 \((4,23)=1\)，这正是式 (3) 的第三项。于是 (3) 和 Type II
正规形立即给出 (4)。

对递降回执，Type II 互素因子正规形从任一 (3) 恢复式 (5) 中的
\(A,B,C\)，并给出 \(A+B=23K\)。又 \(24\mid p-1\)，故

\[
n=\frac{p+23}{23+1}=h+1<p.
\tag{12}
\]

将 \(x=ABC\) 与 \(A+B=23K\) 代入，式 (6) 分别化为

\[
\frac1x+\frac{A+B}{ABCK}
=\frac{24}{x}=\frac4n,
\qquad
\frac1x+\frac{A+B}{pABCK}
=\frac{p+23}{px}=\frac4p.
\]

这同时证明了 \(W_{p,d}\) 的非空性、提升恒等式与严格下降。

## 3. 与先前 gap-23 扇和双 G 控制的关系

在 \(h\) 不要求奇偶时，\(x\) 的固定 \(2,3\)-部分只保证
\(36\mid x^2\)，此前的 gap-23 自动扇因此覆盖 (2) 中除 \(5,14\) 外的九个
剩余类。奇 \(h\) 使 \(12\mid x\)，额外允许 \(d=8,16\)，恰补齐

\[
p\equiv14\pmod {23}quad(d=8),
\qquad
p\equiv5\pmod {23}quad(d=16).
\tag{13}
\]

这解释了双 G 严格控制点 \(p=2521\)：此时 \(h=105\) 为奇数，
\(p\equiv14\pmod {23}\)，取 \(d=8\) 得

\[
x=636,
\qquad
n=106,
\qquad
\frac4{106}=\frac1{636}+\frac1{28}+\frac1{2226},
\]

并经式 (8) 恢复已知的目标 terminal

\[
\frac4{2521}=\frac1{636}+\frac1{70588}+\frac1{5611746}.
\]

该定理仍只覆盖奇 \(h\) 且 \(p\) 为模 \(23\) 二次非剩余的子域；偶 \(h\)，以及
模 \(23\) 二次剩余的奇 \(h\)，都需要其它 terminal 或真正的 G/Type I 出口。

聚焦验证：

~~~bash
python3 reproductions/type_ii_gap_23_odd_h_qnr_terminal_descent.py --verify
~~~
