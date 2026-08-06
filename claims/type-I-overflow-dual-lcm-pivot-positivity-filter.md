---
kind: claim
claim_id: type-I-overflow-dual-lcm-pivot-positivity-filter
title: overflow 对偶 lcm pivot 的精确正性与局部 trap 判据
statement: 对 overflow 行列式 pn=4Md+1、M=kp+r 与 charged support A|M，fixed-n 的规范 lcm pivot L_n=lcm(A,d) 在 g=gcd(A,d)、u=M/A 下满足 R_{L_n}>0 当且仅当 p>gu，且它严格增长 carrier 当且仅当 d 不整除 A。fixed-s 的规范 lcm pivot L_s=lcm(A,r) 在 a=A/gcd(A,r) 整除 d 时恰通过 fixed-s 的整除门；此时 R_{L_s}>0 自动成立，且它严格增长 carrier 当且仅当 r 不整除 A。故 d|A、r|A 和 A/gcd(A,p-d) 不整除 r 严格阻断 fixed-n lcm、fixed-s lcm 与 cofactor r-chart 三条规范 pivot；这只是局部 selector trap，不排除其它 fixed-n/fixed-s 除子、support reset、terminal 或递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-fixed-n-overflow-rank-descent
  - type-I-overflow-fixed-s-dual-outer-rank-descent
  - type-I-overflow-cofactor-r-chart-support
  - type-I-overflow-fixed-n-bounded-divisor-saturation
topics:
  - type-I
  - overflow
  - fixed-n
  - fixed-s
  - lcm
  - positivity
  - cofactor
  - support
  - selector
  - proof-boundary
sources:
  - claim: type-I-overflow-fixed-n-overflow-rank-descent
    role: fixed-n-edge-interface
  - claim: type-I-overflow-fixed-s-dual-outer-rank-descent
    role: fixed-s-edge-interface
  - claim: type-I-overflow-cofactor-r-chart-support
    role: cofactor-edge-interface
  - claim: type-I-overflow-fixed-n-bounded-divisor-saturation
    role: wider-atlas-boundary
visibility: public
last_checked: '2026-08-06'
---

# overflow 对偶 \(\operatorname{lcm}\) pivot 的精确正性与局部 trap 判据

## 1. 设置

令 \(p\equiv1\pmod {24}\) 为素数。考虑一个已经通过其来源/路径门的 overflow
行列式

\[
pn=4Md+1,
\qquad
M=kp+r,
\qquad
1\le r<p,
\qquad
0<d<p,
\qquad
A\mid M.
\tag{1}
\]

记

\[
s=\frac{4rd+1}{p}=n-4kd>0,
\qquad
C=p-d.
\tag{2}
\]

由 (1) 模 \(p\) 可知 \(p\nmid M\)，因而

\[
p\nmid A,
\qquad
p\nmid \frac MA.
\tag{3}
\]

本卡只精化两个固定的 \(\operatorname{lcm}\) pivot 的正性和 carrier 增长门；
来源、标记集、E1--E5、其他除子和 terminal-first 检查仍由下游分派负责。

## 2. fixed-\(n\) pivot 的精确正性

令

\[
g=(A,d),
\qquad
u=\frac MA,
\qquad
L_n=[A,d]=\frac{Ad}{g}.
\tag{4}
\]

则

\[
\frac{Md}{L_n}=gu,
\tag{5}
\]

从而 fixed-\(n\) 图表的参数可化为

\[
K_n=L_n\left(p-\frac{Md}{L_n}\right)=L_n(p-gu),
\tag{6}
\]

\[
pR_n+1=4L_n(p-gu)=4K_n,
\qquad R_n=4L_n-n.
\tag{7}
\]

由 (3) 和 \(g\mid A\)，有 \(p\nmid gu\)，所以 \(gu\ne p\)。因此

\[
\boxed{
R_n>0
\quad\Longleftrightarrow\quad
K_n>0
\quad\Longleftrightarrow\quad
p>gu.
}
\tag{8}
\]

此外

\[
\frac{L_n}{A}=\frac d{(A,d)},
\qquad
\boxed{L_n>A\quad\Longleftrightarrow\quad d\nmid A.}
\tag{9}
\]

特别地，\(A\mid d\) 只给出 \(L_n=d\)；要有 \(L_n=A\)，正确的方向是
\(d\mid A\)。

## 3. fixed-\(s\) pivot 的自动正性

令

\[
h=(A,r),
\qquad
a=\frac Ah,
\qquad
L_s=[A,r]=ar.
\tag{10}
\]

则

\[
\boxed{L_s\mid rd\quad\Longleftrightarrow\quad a\mid d.}
\tag{11}
\]

事实上 \(A=ah\)、\(r=hr'\) 且 \((a,r')=1\)，故
\(ar\mid rd\) 等价于 \(a\mid d\)。在此条件下写 \(d=ac\)。因为
\(0<d<p\)，有 \(0<c<p\)，并且

\[
K_s=L_s\left(p-\frac{rd}{L_s}\right)=L_s(p-c),
\tag{12}
\]

\[
pR_s+1=4L_s(p-c)=4K_s,
\qquad R_s=4L_s-s.
\tag{13}
\]

所以

\[
\boxed{L_s\mid rd\quad\Longrightarrow\quad R_s>0.}
\tag{14}
\]

在 (11) 已经通过时，单列的 \(R_s>0\) 算术门是冗余的。carrier 增长由

\[
\frac{L_s}{A}=\frac r{(A,r)},
\qquad
\boxed{L_s>A\quad\Longleftrightarrow\quad r\nmid A}
\tag{15}
\]

精确决定。

## 4. 三个规范 pivot 的局部 trap

余因子 \(r\)-chart 的 carrier 门为

\[
[A,C]\mid rC
\quad\Longleftrightarrow\quad
\frac{A}{(A,C)}\mid r.
\tag{16}
\]

因此

\[
\boxed{
d\mid A,
\qquad r\mid A,
\qquad
\frac{A}{(A,p-d)}\nmid r
}
\tag{17}
\]

分别阻断 fixed-\(n\) lcm 的 carrier 增长、fixed-\(s\) lcm 的 carrier 增长和
cofactor \(r\)-chart 的 carrier 门。一个方便的充分特例为

\[
d=A,
\qquad r\mid A,
\qquad 0<r<A.
\tag{18}
\]

此时 \((A,p-d)=(A,p)=1\)，故 (16) 要求 \(A\mid r\)，与 \(r<A\) 矛盾。

式 (17) 只是三条特定规范 pivot 的严格局部 trap。它不排除 fixed-\(n\) 的其他
\(L\mid Md\)、fixed-\(s\) 的其他 \(L\mid rd\)、以外层势支付的 support reset，
也不排除直接 Type I/II、容量或另一条可提升递降。

## 5. 为什么不能把局部 trap 当作全 atlas 障碍

取

\[
(p,A,M,d,n,r)=(73,18,1242,18,1225,1).
\tag{19}
\]

有

\[
73\cdot1225=4\cdot1242\cdot18+1,
\qquad
R_M=3743>73.
\tag{20}
\]

这里 \(d=A\)、\(r\mid A\)、\((A,p-d)=(18,55)=1\)，故 (17) 成立。两个
lcm pivot 分别给出

\[
L_n=L_s=18,
\qquad
R_n=-1153,
\qquad
(R_s,K_s)=(71,1296),
\tag{21}
\]

而 cofactor 门要求 \(18\mid1\)，失败。

但固定-\(n\) 的另一个实际除子

\[
L=414\mid Md,
\qquad
(R_L,K_L)=(431,7866),
\tag{22}
\]

仍满足

\[
18<L\le B_{73}=1296,
\qquad
\left\lfloor\frac{1296}{18}\right\rfloor=72
>3=
\left\lfloor\frac{1296}{414}\right\rfloor.
\tag{23}
\]

所以它通过完整 fixed-\(n\) 有界除子 atlas 的算术和外层势门。该例只说明局部
trap 不能被升级为 `FULL_ATLAS_NO_EDGE`；它本身没有声明来源/路径回放，因而不是
E1--E5 已验证边，更不是 Erdős--Straus 反例。
