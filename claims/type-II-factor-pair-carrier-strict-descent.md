---
kind: claim
claim_id: type-II-factor-pair-carrier-strict-descent
title: Type II 互素因子对的二次比值载体与严格递降
statement: 若一个合法 Type II gap m 的互素因子正规形 x=ABC、A+B=mK 同时满足 m+1|p-1，则它不仅给出 4/p 的直接 Type II 终端，而且给出严格且可提升的两尾递降到 n=(p+m)/(m+1)。当 m 是 3 (mod 4) 素数时，互素因子比值的二次剩余载体把该 Type II 选择问题化为 x 的非剩余素因子。特别地，gap 7 对全部核心素数有精确的非剩余因子判据；c=3 的 gap 11 在 3|q 时有精确的 11-二次非剩余判据，并在 3∤q 时缩为有限 signed-ratio box；gap 19 在 5|h 时缩为 n=(p+19)/20 的三残类 box；gap 23 在 q=3 (mod 4) 时有相应的 23-二次非剩余判据。p=12721 说明 3、7、11、23 的指定层可共同未命中而由 gap 19 关闭。结果只覆盖这些指定 gap 的 Type II factor-pair 层，不构成全称覆盖或 Erdos--Straus 证明。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-coprime-factor-normal-form
  - short-certificate-equivalence
  - type-II-c3-q-complementary-divisor-r7mod11-descent
  - type-II-p-plus-12-36-divisor-terminal-fan
  - denominator-escape-state-contract
topics:
  - type-II
  - terminal-first
  - strict-descent
  - factor-pair
  - quadratic-residue
  - c3
  - gap-seven
  - gap-eleven
  - gap-nineteen
  - gap-twenty-three
  - proof-boundary
sources:
  - claim: type-II-coprime-factor-normal-form
    role: complete-Type-II-factor-pair-normal-form
  - claim: short-certificate-equivalence
    role: Type-I-Type-II-divisor-reconstruction
  - claim: type-II-c3-q-complementary-divisor-r7mod11-descent
    role: original-r-equals-seven-gap-eleven-subfamily
  - concept: denominator-escape-state-contract
    role: terminal-first-and-strict-lift-boundary
visibility: public
last_checked: '2026-08-06'
---

# Type II 互素因子对的二次比值载体与严格递降

## 1. 因子对证书同时是严格两尾递降

令 \(p\equiv1\pmod4\) 为素数，\(m\equiv3\pmod4\) 为合法 gap，且

\[
x=\frac{p+m}{4}=ABC,\qquad
(A,B)=1,\qquad A\le B,\qquad A+B=mK.
\tag{1}
\]

再假设

\[
m+1\mid p-1,\qquad n=\frac{p+m}{m+1}.
\tag{2}
\]

**定理（factor-pair two-tail lift）。** (1)--(2) 给出一对精确恒等式

\[
\boxed{
\frac4n=\frac1{ABC}+\frac1{ACK}+\frac1{BCK},
}
\tag{3}
\]

\[
\boxed{
\frac4p=\frac1{ABC}+\frac1{pACK}+\frac1{pBCK}.
}
\tag{4}
\]

因此 (4) 是直接 Type II terminal，而 (3) 是严格较小实例 \(n<p\) 的解；
保留首分母并把后两尾乘以 \(p\) 可提升回 (4)。

**证明。** 由 \(A+B=mK\) 与 \(x=ABC\)，有

\[
\frac1{ACK}+\frac1{BCK}=\frac{A+B}{ABCK}=\frac m x.
\tag{5}
\]

故 (3) 的右端为 \((m+1)/x=4/n\)，而 (4) 的右端为

\[
\frac1x+\frac m{px}=\frac{p+m}{px}=\frac4p.
\tag{6}
\]

又 \(n=(p+m)/(m+1)<p\)。证毕。

这不是从任意 \(4/n\) 解得到 \(4/p\) 解的普遍提升：必须保留 (3) 的首分母
\(x=(p+m)/4\) 和两尾比值。它恰是 type-II-coprime-factor-normal-form 中
\(d=A^2C\) 的完整 Type II 层。

## 2. 二次比值载体

设 \(m\equiv3\pmod4\) 为素数，\(m\nmid x\)。对任意 \(N\) 定义 signed ratio box

\[
\mathcal R_m(N)=
\left\{ab^{-1}\pmod m:
a\mid N,\ b\mid N,\ (a,b)=1\right\}.
\tag{7}
\]

若 \(N=\prod_\ell\ell^{e_\ell}\)，则等价地

\[
\mathcal R_m(N)=
\left\{\prod_\ell \ell^{t_\ell}\pmod m:
-e_\ell\le t_\ell\le e_\ell\right\}.
\tag{8}
\]

记 \(\operatorname{QR}_m\) 为模 \(m\) 的非零二次剩余。

**引理（二次比值载体）。** 若 \(F\mid x\) 且

\[
\mathcal R_m(F)=\operatorname{QR}_m,
\tag{9}
\]

则当前 gap 的 Type II factor-pair certificate 存在，当且仅当 \(x\) 有一个
模 \(m\) 的二次非剩余素因子。

**证明。** 因 \(m\equiv3\pmod4\)，\(-1\) 是非剩余。若 \(\ell\mid x\) 是
非剩余，\(-\ell\in\operatorname{QR}_m\)。由 (9) 可取互素
\(a,b\mid F\) 使 \(a/b\equiv-\ell\pmod m\)。令

\[
(A,B,C)=(a,b\ell,x/(ab\ell)),
\tag{10}
\]

必要时交换 \(A,B\)，便得到 (1)。反过来，若 \(x\) 的全部素因子均为二次剩余，
任何 \(A/B\) 都是二次剩余，不可能等于 \(-1\)。证毕。

等价地，完整 Type II 命中条件就是

\[
\boxed{-1\in\mathcal R_m(x).}
\tag{11}
\]

(9) 只是把这个完整有限群条件压缩成一个单一非剩余因子选择器的充分且必要载体。

## 3. gap \(7\)：所有核心素数的完整因子对判据

对任意核心素数 \(p=24h+1\)，令

\[
x_7=\frac{p+7}{4}=2(3h+1),\qquad
n_7=\frac{p+7}{8}.
\tag{12}
\]

这里 \(8\mid p-1\)，且

\[
\mathcal R_7(2)=\{1,2,4\}=\operatorname{QR}_7.
\tag{13}
\]

所以有精确判据：

\[
\boxed{
\text{gap \(7\) Type II terminal 与严格 \(n_7\)-递降存在}
\Longleftrightarrow
x_7\ \text{有一个 \(7\)-二次非剩余素因子}.
}
\tag{14}
\]

例如 \(p=97\) 时 \(x_7=26\) 含 \(13\equiv6\pmod7\)。取

\[
(A,B,C,K)=(1,13,2,2),
\tag{15}
\]

便有

\[
\frac4{13}=\frac1{26}+\frac14+\frac1{52},
\qquad
\frac4{97}=\frac1{26}+\frac1{388}+\frac1{5044}.
\tag{16}
\]

## 4. c=3 的完整 gap \(11\) Type II 层

令

\[
q=\frac{p+11}{12}=2h+1,\qquad
x_{11}=3q,\qquad
p=12q-11.
\tag{17}
\]

因 \(p>11\) 为素数，有 \(11\nmid q\)。由 (11)，全部 gap \(11\) Type II
factor-pair certificate 的精确判据是

\[
\boxed{-1\in\mathcal R_{11}(3q).}
\tag{18}
\]

每一次命中都按 (3)--(4) 严格下降到 \(q<p\)，而不只是给一个直接 terminal。

若 \(3\mid q\)，则 \(9\mid x_{11}\)，而

\[
\mathcal R_{11}(9)=\{1,3,4,5,9\}=\operatorname{QR}_{11}.
\tag{19}
\]

故得到完全的因子选择器：

\[
\boxed{
3\mid q\Longrightarrow
\left[
\text{gap \(11\) Type II 命中}
\Longleftrightarrow
q\ \text{有一个 \(11\)-二次非剩余素因子}
\right].
}
\tag{20}
\]

若 \(3\nmid q\)，则不应错误外推 (20)。精确条件仍是有限盒

\[
\mathcal R_{11}(3q)=\{1,3,4\}\mathcal R_{11}(q),
\tag{21}
\]

即 \(\mathcal R_{11}(q)\) 必须命中 \(\{7,8,10\}\)。这已比只检查一个
\(r\equiv7\pmod{11}\) 因子严格更强。

例如

\[
p=457,\qquad q=39=3\cdot13,
\tag{22}
\]

没有 \(7\pmod{11}\) 的 \(q\)-因子，却可取

\[
(A,B,C,K)=(9,13,1,2),
\tag{23}
\]

从而

\[
\frac4{39}=\frac1{117}+\frac1{18}+\frac1{26},
\qquad
\frac4{457}=\frac1{117}+\frac1{8226}+\frac1{11882}.
\tag{24}
\]

完整因子对也严格超过三个低尺度互补因子射线。取

\[
p=24481,\qquad q=2041=13\cdot157,\qquad
(A,B,C,K)=(13,471,1,44),
\tag{25}
\]

给出

\[
\frac4{2041}=\frac1{6123}+\frac1{572}+\frac1{20724}.
\tag{26}
\]

这里对应 \(d=A^2C=13^2\)，不能由仅取
\(d\in\{q/r,3q/r,9q/r\}\) 的三尺度扇替代。

原 \(r\equiv7\pmod{11}\) 规则的正确扩张为：若 \(r\mid q\)、\(s=q/r\)，则

\[
\begin{array}{c|c|c|c}
r\pmod{11}&(A,B,C)&d&\text{(3) 的后二尾}\\ \hline
7&(1,3r,s)&s&\left((3r+1)s/11,\ 3(3r+1)q/11\right)\\
10&(1,r,3s)&3s&\left(3(r+1)s/11,\ 3(r+1)q/11\right)\\
8&(3,r,s)&9s&\left(3(r+3)s/11,\ (r+3)q/11\right)
\end{array}
\tag{27}
\]

每行都给 direct Type II terminal 和严格 \(q\)-递降。它们是 \(A\in\{1,3\}\)
的低尺度切片，而 (25) 展示 \(A>3\) 的 square-borrowing 分支确实存在。

gap \(11\) 也有明确的残余边界。若 \(q\) 的所有素因子都属于

\[
\operatorname{QR}_{11}=\{1,3,4,5,9\},
\tag{28}
\]

则 (18) 必失败。控制点

\[
p=313,\qquad q=27
\tag{29}
\]

满足 \(\mathcal R_{11}(81)=\operatorname{QR}_{11}\)，故整个 gap \(11\)
Type II 层未命中。另一个控制点

\[
p=937,\qquad q=79
\tag{30}
\]

含 \(11\)-非剩余因子，但 \(3\nmid q\)，且

\[
\mathcal R_{11}(237)=\{1,2,3,4,6,7,8\}
\not\ni-1.
\tag{31}
\]

所以它也未命中。这两点是指定 gap 的边界，不是 Erdős--Straus 反例。

## 5. gap \(11\) 的 Type I companion 切片

在 (17) 中，若一个 gap \(11\) 的候选除子写作 \(e=A^2C\)、\(x_{11}=ABC\)，
则 Type I 的标准条件 \(11\mid p x_{11}+e\) 等价于

\[
B^2C\equiv8\pmod{11}.
\tag{32}
\]

事实上 \(p\equiv4ABC\pmod{11}\)，故

\[
p x_{11}+e\equiv A^2C(4B^2C+1)\pmod{11},
\tag{32a}
\]

而 \(11\nmid AC\)。

另有一个把 Type II 递降与可能不同的 Type I 除子配对的精确子选择器：

\[
\eta\mid9q,\qquad \eta\equiv8\pmod{11}.
\tag{33}
\]

取

\[
d_{\mathrm{II}}=\frac{9q}{\eta},
\qquad
d_{\mathrm I}=q\,d_{\mathrm{II}}=\frac{x_{11}^2}{\eta}.
\tag{34}
\]

由于 \(q\) 与 \(\eta\) 都是奇数，\(\eta\equiv8\pmod{11}\) 蕴含
\(\eta\ge19\)，从而 \(d_{\mathrm{II}}<x_{11}\)。又

\[
d_{\mathrm{II}}\equiv-3q\pmod{11},
\qquad
p x_{11}+d_{\mathrm I}\equiv0\pmod{11},
\tag{35}
\]

这里 \(\eta^{-1}\equiv7\pmod{11}\)，所以
\(d_{\mathrm{II}}\equiv9q\eta^{-1}\equiv-3q\)，并且
\(p x_{11}+d_{\mathrm I}\equiv3q^2+8q^2\equiv0\pmod{11}\)。
所以前者给 (3)--(4)，后者给同一 gap 的直接 Type I certificate。
反过来，所有满足 \(d_{\mathrm{II}}\mid9q\) 的 gap \(11\) Type II 命中都
恰以 (33)--(34) 表示。这正是 (27) 三行的共同 Type I companion。

这张 companion 图仍非完整：例如 (25) 的 \(d_{\mathrm{II}}=13^2\) 不整除
\(9q\)，却给真实严格递降。

## 6. gap \(23\) 的相邻互补出口

仍以 (17) 的 \(q\) 记号。对 gap \(23\)，有

\[
x_{23}=\frac{p+23}{4}=3(q+1),
\qquad
n_{23}=\frac{p+23}{24}=\frac{q+1}{2}.
\tag{36}
\]

若 \(q\equiv3\pmod4\)，则 \(12\mid x_{23}\)，并且

\[
\mathcal R_{23}(12)
=\{1,2,3,4,6,8,9,12,13,16,18\}
=\operatorname{QR}_{23}.
\tag{37}
\]

因此

\[
\boxed{
q\equiv3\pmod4\Longrightarrow
\left[
\text{gap \(23\) Type II 命中}
\Longleftrightarrow
q+1\ \text{有一个 \(23\)-二次非剩余素因子}
\right].
}
\tag{38}
\]

控制点 (30) 恰由这个相邻出口关闭：取

\[
(A,B,C,K)=(3,20,4,1),
\tag{39}
\]

则

\[
\frac4{40}=\frac1{240}+\frac1{12}+\frac1{80},
\qquad
\frac4{937}=\frac1{240}+\frac1{11244}+\frac1{74960}.
\tag{40}
\]

容量门 \(4\mid(q+1)\) 不能删除：\(p=97,q=9\) 时 \(q+1\) 虽含
\(23\)-非剩余因子 \(5\)，但

\[
\mathcal R_{23}(30)\not\ni-1,
\tag{41}
\]

故 gap \(23\) 不命中。

## 7. gap \(19\) 的精确三残类盒

对核心素数 \(p=24h+1\)，gap \(19\) 的严格 source 条件恰为

\[
20\mid p-1
\Longleftrightarrow
5\mid h.
\tag{42}
\]

写 \(h=5t\)，并令

\[
n_{19}=\frac{p+19}{20}=6t+1,
\qquad
x_{19}=\frac{p+19}{4}=5n_{19}.
\tag{43}
\]

完整 Type II factor-pair 条件 (11) 在这里精确化为

\[
\boxed{
-1\in\mathcal R_{19}(5n_{19})
\Longleftrightarrow
\mathcal R_{19}(n_{19})\cap\{14,15,18\}\ne\varnothing.
}
\tag{44}
\]

事实上

\[
\mathcal R_{19}(5)=\{1,4,5\},
\tag{45}
\]

并且按 (8) 的指数区间有
\(\mathcal R_{19}(5n_{19})=\mathcal R_{19}(5)\mathcal R_{19}(n_{19})\)，即使
\(5\mid n_{19}\) 也成立：5 的两个指数区间相加恰给出
\([-(v_5(n_{19})+1),v_5(n_{19})+1]\)。将 \(-1=18\) 逐一除以 (45) 的三个元素
正好得到右侧的三残类。这是全 factor-pair 层的等价条件，不是单因子充分筛。

控制点

\[
p=12721,\qquad h=530,\qquad n_{19}=637=7^2\cdot13,
\qquad x_{19}=3185
\tag{46}
\]

落在该层。这里

\[
\mathcal R_{19}(35)=\operatorname{QR}_{19}
=\{1,4,5,6,7,9,11,16,17\},
\tag{47}
\]

而 \(13\) 是模 \(19\) 的非剩余。取

\[
(A,B,C,K)=(1,455,7,24)
\tag{48}
\]

得到

\[
\frac4{637}=\frac1{3185}+\frac1{168}+\frac1{76440},
\qquad
\frac4{12721}=\frac1{3185}+\frac1{2137128}+\frac1{972393240}.
\tag{49}
\]

它还位于一个显式 Dirichlet 射线。令 \(u\ge0\)、\(C_u=6u+1\)，则

\[
p_u=1801+10920u,
\qquad
n_u=91C_u,
\qquad
x_u=455C_u.
\tag{50}
\]

因为 \(\gcd(1801,10920)=1\)，每个使 \(p_u\) 为素数的参数都给出

\[
(A,B,C,K)=(1,455,C_u,24),
\tag{51}
\]

以及

\[
\frac4{91C_u}
=\frac1{455C_u}+\frac1{24C_u}+\frac1{10920C_u}.
\tag{52}
\]

Dirichlet 定理因此给出无穷多个这类核心素数；\(u=1\) 正是 (46)。容量不可删除：

\[
p=241,\qquad n_{19}=13,\qquad x_{19}=65,
\qquad -1\notin\mathcal R_{19}(65).
\tag{53}
\]

故仅有一个 \(19\)-非剩余因子不足以保证 gap \(19\) 命中。

## 8. 固定小 gap 的联合残余

令 \(t=h+1\)，则 \(p=24t-23\)。gap \(7,11,23\) 的严格较小 source 分别为

\[
n_7=3t-2,
\qquad
n_{11}=2t-1,
\qquad
n_{23}=t.
\tag{54}
\]

利用各自固定 carrier，三个完整 Type II 层共同未命中的精确条件为

\[
\mathcal R_7(3t-2)\cap\{3,5,6\}=\varnothing,
\tag{55}
\]

\[
\mathcal R_{11}(2t-1)\cap\{7,8,10\}=\varnothing,
\tag{56}
\]

\[
\mathcal R_{23}(t)\cap\{7,10,11,15,17,19,20,21,22\}=\varnothing.
\tag{57}
\]

例如 \(p=12721\) 对应 \(t=531\)。它还有 gap \(3\) 的 complete factor-pair miss，且

\[
\begin{aligned}
x_3&=3181,\\
x_7&=3182=2\cdot37\cdot43,\\
x_{11}&=3183=3\cdot1061,\\
x_{23}&=3186=2\cdot3^3\cdot59.
\end{aligned}
\tag{58}
\]

这些因子在相应 signed-ratio box 中都不能产生 \(-1\)，故 \(m=3,7,11,23\) 的
指定完整 Type II factor-pair/strict-descent 层均不命中。但 (48)--(49) 的 gap \(19\)
证书已经关闭该点。因此这只是有限 gap dispatch 的真实压力点，而非猜想反例。

## 9. 研究边界

本卡将四个指定 gap 的 Type II 选择问题压缩为可检验的因子残余或有限 signed-ratio
box，并把每个命中升级为可提升的严格递降。它没有证明这些 gap 的并集覆盖所有核心
素数：例如 gap \(11\) 的全二次剩余乘法半群仍是严格残余，且 gap \(7\)、\(19\)、\(23\)
也各有自己的盒条件。下一步应研究这些残余之间是否存在独立的 mark-transfer 或其它
gap 出口，不能把“较小 \(q\) 已可解”误当成自动可提升的资源。

复现：

    python3 reproductions/type_ii_factor_pair_carrier_strict_descent.py --verify
