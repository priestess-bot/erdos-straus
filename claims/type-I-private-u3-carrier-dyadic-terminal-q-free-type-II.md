---
kind: claim
claim_id: type-I-private-u3-carrier-dyadic-terminal-q-free-type-II
title: 私有 u=3 载体族的二进终端与 Type II 支撑退出
statement: 设 p,q 为素数、p≡1 (mod 24)，且正整数 t>6、R>3 满足 p=t+3+3tR、tR+1=2q。令 h=(3R+1)/2，则 K=(pR+1)/4=qh，q 是完整有序线性源谱中唯一且高度为 1 的私有载体；全族无条件具有 E=4h^2、n=2h(t-3) 的广义 2^1 偶终端，同状态 Type I 命中等价于 h^2 的除子命中 -1 或 -h (mod R)。另一方面，任意 Type II 证书的首分母 x=(p+m)/4 都满足 q∤x，故任何 Type II 出口必须退出该私有 q 支撑。R=19、h=29、p=409 给出私有载体和偶终端同时存在但同状态 Type I 仍为 F miss 的显式边界；偶终端尚未构成可提升递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-linear-private-carrier-isolation-criterion
  - type-I-general-dyadic-terminal-transfer
  - type-I-general-b-centered-square-spectrum
  - type-II-coprime-factor-normal-form
topics:
  - type-I
  - type-II
  - private-carrier
  - linear-source
  - dyadic-terminal
  - support-exit
  - F-state
  - escape-lemma
  - proof-program
sources:
  - claim: type-I-linear-private-carrier-isolation-criterion
    role: complete-linear-source-private-carrier-criterion
  - claim: type-I-general-dyadic-terminal-transfer
    role: exact-dyadic-terminal-transfer
  - claim: type-I-general-b-centered-square-spectrum
    role: centered-Type-I-target-condition
  - claim: type-II-coprime-factor-normal-form
    role: exact-Type-II-divisor-condition
visibility: public
last_checked: '2026-07-31'
---

# 私有 \(u=3\) 载体族的二进终端与 Type II 支撑退出

## 设置

设 \(p,q\) 为素数，且正整数 \(t>6\)、\(R>3\) 满足

\[
p\equiv1\pmod{24},
\qquad
p=t+3+3tR,
\qquad
tR+1=2q.
\tag{1}
\]

定义

\[
h=\frac{3R+1}{2},
\qquad
K=\frac{pR+1}{4}.
\tag{2}
\]

由 (1) 立刻得到

\[
p=6q+t,
\qquad
4K=(tR+1)(3R+1),
\qquad
K=qh.
\tag{3}
\]

## 强制同余与私有性

因为 \(q\) 为奇素数，\(tR\equiv1\pmod4\)。又由 \(p=6q+t\) 及
\(p\equiv1\pmod{12}\)，有

\[
t\equiv7\pmod{12}.
\]

于是 \(R\equiv3\pmod4\)。若 \(R\equiv7\pmod8\)，则
\(p=t(3R+1)+3\equiv5\pmod8\)，矛盾；故

\[
R\equiv3\pmod8,
\qquad
h\equiv5\pmod{12}.
\tag{4}
\]

此外

\[
q-h=\frac{(t-3)R}{2}>0,
\qquad
q\equiv h\equiv2^{-1}\pmod R.
\tag{5}
\]

因为 \(q>h\) 且 \(q\) 为素数，\((q,h)=1\)，所以 \(v_q(K)=1\)。

现在把 (1) 视为完整有序线性源中的块

\[
tR+1=2q,
\qquad
p-t=6q.
\]

在[私有载体唯一性判据](type-I-linear-private-carrier-isolation-criterion.md)中取

\[
(t_0,u_0,d_0,n_0)=(t,3,2,6).
\]

条件 \(R+d_0>n_0-1\) 由 \(R>3\) 成立；而 \(t>6\) 时，\(6\) 的正因子中只有
\(D=2\) 同时满足 \(D\ge2\) 与 \(D\equiv2\pmod t\)。故 \(q\) 是完整有序线性源谱
中唯一出现于该块、且高度恰为 1 的私有载体。

## 无条件广义二进终端

令

\[
L=2K,
\qquad
a=2h,
\qquad
b=q,
\qquad
j=1.
\]

由 (3)、(5)，\(a,b\mid L\)、\((a,b)=1\)，并且

\[
a\equiv2b\pmod R,
\qquad
a<2b.
\]

一般二进传输因此给出

\[
\boxed{
E=4h^2,
\qquad
n=\frac{4K-E}{R}=2h(t-3).}
\tag{6}
\]

这里 \(n\) 是正的 \(8\) 的倍数，且

\[
p-n=6h+3>0.
\]

所以 (6) 是全族的严格更小偶终端。它仍只是满足
\(E\mid4K^2\)、\(E\equiv1\pmod R\) 的终端因子；本卡没有从 \(4/n\) 的任意解构造
\(4/p\) 解的提升映射，因而不把它称为算术递降。

## 同状态 Type I 条件消去私有 \(q\)

Type I 中心条件等价于存在严格除子 \(D\mid K^2\) 使

\[
4D\equiv-1\pmod R.
\]

把 \(D\) 写为

\[
\frac DK=q^e\frac dh,
\qquad
e\in\{-1,0,1\},
\qquad
d\mid h^2.
\]

由于 \(4K\equiv1\pmod R\) 且 \(q\equiv h\pmod R\)，目标条件化为

\[
q^e\frac dh\equiv-1\pmod R.
\]

当 \(e=0\) 时，这等价于 \(d\equiv-h\pmod R\)；当 \(e=1\) 时，等价于
\(d\equiv-1\pmod R\)；当 \(e=-1\) 时，对换 \(d\) 与 \(h^2/d\) 后仍等价于后一条件。
目标除子与 \(K^2/D\) 成反足对，且不可能等于 \(K\)，所以两者中总有一个满足严格
大小条件。综上，

\[
\boxed{
\text{同状态 Type I hit}
\Longleftrightarrow
\left(
\exists d\mid h^2:\ d\equiv-1\pmod R
\right)
\ \lor\
\left(
\exists d\mid h^2:\ d\equiv-h\pmod R
\right).}
\tag{7}
\]

右端只依赖 \((R,h)\)，与 \(t\) 及增长的私有素数 \(q\) 无关。

## 任意 Type II 必须退出 \(q\) 支撑

设 \(p\) 有任意 Type II 证书，记

\[
x=\frac{p+m}{4},
\qquad
d\mid x^2,
\qquad
d\le x,
\qquad
m\mid x+d.
\tag{8}
\]

自然范围 \(3\le m\le p-2\) 给出

\[
\frac p4<x<\frac p2.
\]

又因 \(R\ge11\)，有 \(q=(tR+1)/2>5t\)。若 \(q\mid x\)，再由
\(p=6q+t\) 可知只有

\[
x=2q
\quad\text{或}\quad
x=3q.
\tag{9}
\]

若 \(x=2q\)，则 \(m=2q-t\)，而 \(d\mid4q^2\)、\(d\le2q\) 迫使

\[
d\in\{1,2,4,q,2q\}.
\]

逐项将 \(x+d\) 除以 \(m\)，余数分别落在

\[
t+1,\ t+2,\ t+4,\ q+t,\ 2t,
\]

它们都严格介于 \(0\) 与 \(m\) 之间，违背 \(m\mid x+d\)。

若 \(x=3q\)，则 \(m=6q-t\) 且 \(5q<m<6q\)。由
\(x+d\le6q<2m\)，整除条件只能给 \(x+d=m\)，即

\[
d=3q-t.
\]

但 \(d\mid9q^2\)、\(d\le3q\) 只允许

\[
d\in\{1,3,9,q,3q\},
\]

与 \(q>5t\) 及 \(t>0\) 矛盾。因此

\[
\boxed{q\nmid x.}
\tag{10}
\]

又因 \(d\mid x^2\)，任何 Type II 中心除子也不含 \(q\)。这不是 Type II 存在性定理，
但它严格证明：该族若从 Type II 逃逸，必须离开当前私有载体支撑。

## \(R=19\) 的显式 F 边界

取

\[
R=19,
\qquad h=29,
\qquad(t,q,p)=(7,67,409).
\]

此时 \(q\equiv h\equiv10\pmod{19}\)，且 \(10\) 的乘法阶为 \(18\)。中心指数盒的像为

\[
\mathcal C_{19}(K)
=\{10^s:-2\le s\le2\}
=\{1,2,4,5,10\},
\]

不含 \(-1\equiv18\pmod{19}\)，而生成子群是整个单位群。因此该状态是 F miss 而非 G
障碍；目标离指数区间的循环距离为 \(9-2=7\)。与此同时，(6) 仍给出

\[
E=4\cdot29^2,
\qquad n=232.
\]

所以“完整私有载体加显式短关系终端必迫使同状态 Type I”已被无条件否定。剩余的真正
箭头是：把偶终端升级为带标记的可提升解，或证明必有一个退出 \(q\) 支撑的其它
Type I/II 状态；继续从私有 \(q\) 本身寻找 Type II 射线已由 (10) 排除。

该提升箭头现又得到一层严格压缩：自然 \(E\) 标记纤维非空当且仅当本状态已经 Type I
命中；平凡偶源的两坐标保留恒失败，而把 \(E=4h^2\) 用作保留 \(n/2\) 或 \(n\) 的
一分母提升因子也分别受模 4、模 3 障碍排除。剩余标准源条件全部落在不含 \(q\) 的
\(h^2,(n/2)^2,n^2\) 除子筛中。详见
[私有 u=3 偶终端的自然提升障碍与 q-free 因子三分](type-I-private-u3-terminal-natural-lift-obstruction.md)。
