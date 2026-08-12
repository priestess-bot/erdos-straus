---
kind: claim
claim_id: type-II-gap-47-h6-qnr-terminal-descent
title: h 等于 6 模 8 时 gap-47 的 17 个二次非剩余终端与两尾递降
statement: >-
  设 p=24h+1 为核心素数且 h=6 (mod 8)，令 x=(p+47)/4=6(h+2)。若
  p (mod 47) 属于 R_47={5,10,11,13,15,22,23,26,30,31,35,39,41,43,44,45,46}，
  则表中指定 d 满足 d|x^2、d<=x 和 47|(x+d)，从而给出 gap 47 的显式 Type II
  短证书。又因 48|p-1，该同一 factor pair 规范地给出 n=(p+47)/48=(h+2)/2<p
  的非空两尾标记状态及不读取目标解的 lift (ABC,ACK,BCK)->(ABC,pACK,pBCK)。
  R_47 是模 47 二次非剩余集合中除去 {19,20,29,33,38,40} 的 17 项；本卡不对这
  六项、其它 h 同余类或全部 G 状态作覆盖声明。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - short-certificate-equivalence
  - type-II-coprime-factor-normal-form
  - type-II-factor-pair-carrier-strict-descent
  - type-II-gap-23-odd-h-qnr-terminal-descent
  - type-I-type-II-mod-three-double-g-exit-obstruction
topics:
  - type-II
  - terminal-first
  - gap-47
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
  - claim: type-II-gap-23-odd-h-qnr-terminal-descent
    role: forced-small-divisor-gap-template
  - reproduction: reproductions/type_ii_gap_47_h6_qnr_terminal_descent.py
    role: residue-table-factor-pair-and-lift-controls
visibility: public
last_checked: '2026-08-12'
---

# \(h\equiv6\pmod8\) 时 gap-47 的 17 个二次非剩余终端与两尾递降

## 1. 定理

令

\[
p=24h+1,
\qquad h\equiv6\pmod8,
\qquad x=\frac{p+47}{4}=6(h+2).
\tag{1}
\]

定义下表。第三列的 \(h_0\) 是同时满足
\(h\equiv6\pmod8\)、\(24h+1\equiv r\pmod{47}\) 的最小正整数。

| \(r=p\bmod47\) | \(d\) | \(h_0\) | \(x_0=6(h_0+2)\) |
|---:|---:|---:|---:|
| 5 | 128 | 102 | 624 |
| 10 | 256 | 206 | 1248 |
| 11 | 9 | 302 | 1824 |
| 13 | 32 | 118 | 720 |
| 15 | 8 | 310 | 1872 |
| 22 | 18 | 230 | 1392 |
| 23 | 6 | 326 | 1968 |
| 26 | 64 | 238 | 1440 |
| 30 | 16 | 246 | 1488 |
| 31 | 4 | 342 | 2064 |
| 35 | 3 | 350 | 2112 |
| 39 | 2 | 358 | 2160 |
| 41 | 72 | 174 | 1056 |
| 43 | 1 | 366 | 2208 |
| 44 | 36 | 86 | 528 |
| 45 | 24 | 182 | 1104 |
| 46 | 12 | 278 | 1680 |

记第一列的集合为

\[
\mathcal R_{47}=
\{5,10,11,13,15,22,23,26,30,31,35,39,41,43,44,45,46\}.
\tag{2}
\]

**定理。** 若 \(p\bmod47\in\mathcal R_{47}\)，表中的 \(d\) 满足

\[
d\mid x^2,
\qquad d\le x,
\qquad47\mid x+d.
\tag{3}
\]

所以 \((m,d)=(47,d)\) 给出 Type II 短证书

\[
\boxed{
\frac4p
=\frac1x
+\frac1{p(x+d)/47}
+\frac1{p(x+x^2/d)/47}.
}
\tag{4}
\]

这张 terminal 还带有严格标记递降。令

\[
g=(d,x),\qquad A=\frac dg,\qquad B=\frac xg,
\qquad C=\frac gA,
\qquad K=\frac{A+B}{47},
\qquad n=\frac{p+47}{48}=\frac{h+2}{2}.
\tag{5}
\]

则 \(x=ABC\)、\((A,B)=1\)、\(d=A^2C\)、\(A+B=47K\)，且

\[
\frac4n
=\frac1{ABC}+\frac1{ACK}+\frac1{BCK},
\qquad
\frac4p
=\frac1{ABC}+\frac1{pACK}+\frac1{pBCK}.
\tag{6}
\]

故

\[
W_{p,d}=\{(ABC,ACK,BCK)\}\subseteq\operatorname{Sol}(4,n)
\tag{7}
\]

非空，并且

\[
\Phi_{p,d}(ABC,ACK,BCK)=(ABC,pACK,pBCK)
\tag{8}
\]

是不读取目标解的显式 lift。因为 \(n=(h+2)/2<p\)，这也是一条严格的 marked
descent 回执；作为 (4) 的直接短证书时，它在 terminal-first 顺序中更早退出。

## 2. 强制 48 除子与残余覆盖

由 \(h\equiv6\pmod8\)，\(h+2\) 被 8 整除，故

\[
48\mid x.
\tag{9}
\]

表内每个 \(d\) 都是 \(2^a3^b\)（\(0\le a\le8\)、\(0\le b\le2\)）的一个因子，
因此

\[
d\mid48^2\mid x^2.
\tag{10}
\]

对每个固定的 \(r\)，前两个关于 \(h\) 的同余的解恰为

\[
h\equiv h_0\pmod{376}.
\tag{11}
\]

表中最后一列给出 \(d\le x_0\)。所以任意满足该行的 \(h\) 都有
\(x\ge x_0\ge d\)，证明 (3) 的前两项。

表的第二列按规则

\[
\boxed{r\equiv-4d\pmod{47}}
\tag{12}
\]

选取。由 \(4x=p+47\)，有

\[
4(x+d)=p+47+4d\equiv p+4d\equiv0\pmod{47},
\tag{13}
\]

从而得到 (3) 的第三项。

该覆盖的二次结构也完全显式。模 47 中 2 和 3 都是二次剩余，而
\(-1\) 是二次非剩余；所以每一个 \(-4d\) 都是二次非剩余。直接列出平方剩余可得

\[
\operatorname{QNR}_{47}
=\mathcal R_{47}\sqcup\{19,20,29,33,38,40\}.
\tag{14}
\]

这说明本卡是一个有意的 17 类覆盖，不是把 QNR 条件夸大为全覆盖。

## 3. 证书与下降的证明

式 (3) 是 Type II 除子证书的完整条件，故立即给出 (4)。又因

\[
48\mid24h=p-1,
\qquad x=12n,
\tag{15}
\]

可适用互素因子正规形。为完整起见，由 \(d\mid x^2\) 定义 (5) 后，逐素数赋值
给出

\[
x=ABC,\qquad d=A^2C,\qquad(A,B)=1.
\tag{16}
\]

这里 \(47\nmid x\)，因为 \(p\not\equiv0\pmod{47}\) 且 \(4x\equiv p\pmod{47}\)；
又 \(d\mid x^2\)，故 \(47\nmid AC\)。于是 (13) 与

\[
x+d=AC(A+B)
\tag{17}
\]

给出 \(47\mid A+B\)，所以 \(K\) 为正整数。最后

\[
\frac1{ABC}+\frac1{ACK}+\frac1{BCK}
=\frac1x+\frac{A+B}{ABCK}
=\frac{48}{x}=\frac4n,
\tag{18}
\]

而将后两项同时乘以 \(p\) 则得到

\[
\frac1x+\frac{A+B}{pABCK}
=\frac{p+47}{px}=\frac4p.
\tag{19}
\]

这证明 (6)--(8)。

## 4. 控制：\(p=2833\)

取 \(h=118\)，则

\[
p=2833,\qquad p\equiv13\pmod{47},\qquad x=720,\qquad d=32,\qquad n=60.
\tag{20}
\]

此时

\[
(A,B,C,K)=(2,45,8,1),
\tag{21}
\]

并且

\[
\frac4{60}=\frac1{720}+\frac1{16}+\frac1{360},
\tag{22}
\]

经 (8) 提升为

\[
\frac4{2833}=\frac1{720}+\frac1{45328}+\frac1{1019880}.
\tag{23}
\]

这个控制同时检查表项、Type II 恒等式、非空源标记和严格 \(60<2833\)；它不用于
宣称 gap 47 固定菜单已全称闭合。

## 聚焦验证

```bash
PYTHONPATH=reproductions python3 \
  reproductions/type_ii_gap_47_h6_qnr_terminal_descent.py --verify
```

验证器只重算表的 CRT 下界、二次剩余分解、指定除子条件与 \(p=2833\) 的 factor-pair
lift；不运行历史扫描或 gap 搜索。
