---
kind: claim
claim_id: type-II-a1-fixed-divisor-crt-terminal-descent-generator
title: A=1 固定除子的 Type II CRT 终端与两尾递降生成器
statement: >-
  令 m=4a-1>=3、(d,m)=1。若 h 同时满足 a|6h、d|6h+a、
  m|6h+a+d，且 p=24h+1 是 p>m+1 的素数，则 x=(p+m)/4=dB、
  K=(B+1)/m 给出 A=1,C=d 的互素因子对。因此 4/p 有直接 gap-m Type II
  终端，且 n=(p+m)/(m+1)=x/a<p 有显式两尾源解，其后两尾乘 p 即提升回 4/p。
  这三条条件是可由三元一次同余和广义 CRT 精确判定的单一 h 同余类；若所得
  p=24h+1 的剩余类与其模数互素，则 Dirichlet 定理给出无限素数射线。m=11,d=15
  产生 h=52 (mod 55) 的射线并包含双 G 控制 p=5209；m=59,d=21 恢复
  h=820 (mod 2065) 并包含 p=118801。该生成器只产生满足输入同余的子族，
  不构成固定或可变 gap 的全称覆盖。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - short-certificate-equivalence
  - type-II-coprime-factor-normal-form
  - type-II-factor-pair-carrier-strict-descent
  - type-I-type-II-double-g-external-source-preemption
  - type-II-gap-59-crt-factor-pair-terminal-descent
topics:
  - type-II
  - terminal-first
  - factor-pair
  - crt-ray
  - fixed-divisor
  - marked-descent
  - two-tail-lift
  - double-G
  - proof-program
sources:
  - claim: short-certificate-equivalence
    role: Type-II-certificate-reconstruction
  - claim: type-II-coprime-factor-normal-form
    role: A-one-factor-pair-normalization
  - claim: type-II-factor-pair-carrier-strict-descent
    role: strict-two-tail-descent-and-lift
  - claim: type-I-type-II-double-g-external-source-preemption
    role: gap-eleven-double-G-control
  - claim: type-II-gap-59-crt-factor-pair-terminal-descent
    role: gap-fifty-nine-control
  - reproduction: reproductions/type_ii_a1_fixed_divisor_crt_terminal_descent_generator.py
    role: exact-congruence-ray-and-identity-controls
visibility: public
last_checked: '2026-08-12'
---

# $A=1$ 固定除子的 Type II CRT 终端与两尾递降生成器

## 1. 定理

令

\[
m=4a-1\ge3,
\qquad (d,m)=1,
\tag{1}
\]

并考虑下列关于 $h$ 的三条整除条件：

\[
\boxed{
a\mid6h,
\qquad d\mid6h+a,
\qquad m\mid6h+a+d.
}
\tag{2}
\]

若 $p=24h+1$ 是满足 $p>m+1$ 的素数，置

\[
x=\frac{p+m}{4}=6h+a,
\qquad B=\frac{x}{d},
\qquad K=\frac{B+1}{m},
\qquad n=\frac{p+m}{m+1}=\frac{x}{a}.
\tag{3}
\]

**定理。** 式 (2) 使 (3) 的各量均为正整数，且

\[
(A,B,C,K)=(1,B,d,K)
\tag{4}
\]

是 gap $m$ 的互素因子对。因而

\[
\boxed{
\frac4p
=\frac1{dB}
+\frac1{pdK}
+\frac1{pdBK}
}
\tag{5}
\]

是直接 Type II terminal，而

\[
\boxed{
\frac4n
=\frac1{dB}
+\frac1{dK}
+\frac1{dBK}
}
\tag{6}
\]

满足 $n<p$。因此

\[
(dB,dK,dBK)\longmapsto(dB,pdK,pdBK)
\tag{7}
\]

是不读取目标解的严格两尾 lift。

## 2. 证明

第一条条件等价于

\[
m+1=4a\mid24h=p-1.
\tag{8}
\]

第二条给出 $x=dB$。第三条与 $x+d=d(B+1)$ 联合给出

\[
m\mid d(B+1).
\tag{9}
\]

由 $(d,m)=1$ 的互素性，$m$ 整除 $B+1$，所以 $K$ 为正整数，且

\[
x=ABC,qquad (A,B)=1,qquad A+B=1+B=mK.
\tag{10}
\]

这正是既有 Type II 互素因子对正规形。直接代入得到

\[
\frac1{dB}+\frac1{dK}+\frac1{dBK}
=\frac1x+\frac{B+1}{dBK}
=\frac{m+1}{x}
=\frac4n,
\tag{11}
\]

并将后两尾乘以 $p$ 得到

\[
\frac1x+\frac{m}{px}
=\frac{p+m}{px}
=\frac4p.
\tag{12}
\]

又 $n=(p+m)/(m+1)<p$，证毕。这里的 lift 只作用于 (6) 指定的源解，不能被误读为
从任意 $4/n$ 解到 $4/p$ 的一般提升。

## 3. CRT 与无限射线判据

式 (2) 等价于三条一次同余

\[
6h\equiv0\pmod a,
\qquad
6h\equiv-a\pmod d,
\qquad
6h\equiv-a-d\pmod m.
\tag{13}
\]

对一般 $6h\equiv b\pmod c$，可解当且仅当 $b$ 被 $(6,c)$ 整除；可解时它是一条模
$c/(6,c)$ 的同余类。对 (13) 的三个类运行广义 CRT，故其解集要么为空，要么精确为

\[
h\equiv h_0\pmod M.
\tag{14}
\]

这给出固定 $(m,d)$ 的完全、有限可判定入口，而不是启发式模板。若

\[
\bigl(24h_0+1,24M\bigr)=1,
\tag{15}
\]

则 Dirichlet 定理给出无穷多个素数

\[
p\equiv24h_0+1\pmod{24M}.
\tag{16}
\]

除去至多有限个不满足 $p>m+1$ 的起点，每个这样的素数都由 (5)--(7) 终止或严格递降。
若 (15) 失败，本定理仍对 (14) 中逐个恰为素数的参数有效，但不作无限性断言。

## 4. 两个控制

### 4.1 gap 11：包含双 G 控制 $p=5209$

取

\[
m=11,qquad a=3,qquad d=15.
\tag{17}
\]

式 (13) 化为

\[
h\equiv2\pmod5,
\qquad h\equiv8\pmod{11},
\]

即

\[
h\equiv52\pmod{55},
\qquad p\equiv1249\pmod{1320}.
\tag{18}
\]

剩余类与 $1320$ 互素。控制 $h=217$ 给出 $p=5209$、

\[
x=1305,qquad B=87,qquad K=8,qquad n=435,
\]

以及

\[
\frac4{435}=\frac1{1305}+\frac1{120}+\frac1{10440}
\longmapsto
\frac4{5209}=\frac1{1305}+\frac1{625080}+\frac1{54381960}.
\tag{19}
\]

这说明双 G 控制的 gap-11 terminal 是一条无限 CRT 终端/递降射线的成员，而非孤立因子分解。

### 4.2 gap 59：恢复 $p=118801$

取

\[
m=59,qquad a=15,qquad d=21.
\tag{20}
\]

式 (13) 恰为

\[
h\equiv0\pmod5,
\qquad h\equiv1\pmod7,
\qquad h\equiv-6\pmod{59},
\]

即 $h\equiv820\pmod{2065}$、$p\equiv19681\pmod{49560}$。代入 $h=4950$，
便恢复此前的

\[
(p,x,B,K,n)=(118801,29715,1415,24,1981)
\tag{21}
\]

和 gap-59 的两条精确等式。这个控制也验证 (15) 的无限素数条件。

## 5. 范围

该引理统一的是“$d$ 整除 $x$”的 $A=1$ 因子对射线。它不覆盖只满足“$d$ 整除 $x^2$”的
一般 $A>1$ 因子对，例如 gap-47 表中的若干二进除子；也不说明任何给定核心素数必会
落入某个可解的 $(m,d)$ 系统。因此它是扩展 terminal-first/marked-descent 菜单的生成器，
不是 G/Type I 全局出口的证明。
