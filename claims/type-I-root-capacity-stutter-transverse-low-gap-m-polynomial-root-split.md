---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-low-gap-m-polynomial-root-split
title: 横向 stutter 低缺口 m 多项式的正负根分派
statement: >-
  对核心素数 p≡1 mod24 的 terminal-first 后 actual proper-root stutter receipt，
  令 D=mp+1-h、Da=m+h(h-1)、D*=D/gcd(D,h^2-1)，取
  s∈{3,7,11,23} 和奇素数 q|D*，并假设 q≡-1 mod2s。令
  Delta_s=ms^2-s+1、F_s^+=sh-1、F_s^-=s(h-1)+1，则精确有
  Delta_s+F_s^+F_s^-=s^2Da。故若 q|Delta_s，恰有一个 F_s^+、F_s^-
  被 q 整除。正根 F_s^+ 给出 A=1 的 source-factor Type II terminal 与
  n=(p+s)/(s+1)<p 的显式两尾 lift；负根 F_s^- 令 K=(q+1)/s 为偶数并精确强制
  q|((K-1)p-1)，即一般二次扇的未解决负支，而 q 不整除 Kp+1。因而
  gcd(D*,Delta_s) 的该剩余类碰撞不是自动 terminal，而是 terminal/negative-branch
  的完整容量分派。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-finite-curve-constraint
  - type-I-root-capacity-stutter-transverse-residual-capacity-map
  - type-I-root-capacity-stutter-transverse-root-residue-low-gap-descent
  - type-I-root-capacity-stutter-transverse-quadratic-shift-type-II-fan
topics:
  - type-I
  - type-II
  - root-capacity
  - stutter
  - transverse-residual
  - bounded-gap
  - source-factor-gate
  - capacity-map
  - negative-branch
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-finite-curve-constraint
    role: actual-stutter-curve-identity
  - claim: type-I-root-capacity-stutter-transverse-residual-capacity-map
    role: transverse-residual-provenance-and-coprimality
  - claim: type-I-root-capacity-stutter-transverse-root-residue-low-gap-descent
    role: positive-root-terminal-and-strict-two-tail-lift
  - claim: type-I-root-capacity-stutter-transverse-quadratic-type-II-fan
    role: negative-linear-factor-branch
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_root_residue_low_gap_descent.py
    role: q-local-positive-and-negative-root-split-controls
visibility: public
last_checked: '2026-08-14'
---

# 横向 stutter 低缺口 \(m\) 多项式的正负根分派

## 1. 设置

固定核心素数

\[
p\equiv1\pmod {24}.
\]

terminal-first 后，设一个 actual proper-root stutter receipt 存在。沿用

\[
D=mp+1-h,
\qquad
D\mid ph+1,
\qquad
(D,h)=1,
\qquad
D_*=\frac{D}{(D,h^2-1)},
\tag{1}
\]

以及有限曲线恒等式

\[
Da=m+h(h-1).
\tag{2}
\]

固定一个低缺口

\[
s\in\mathcal G=\{3,7,11,23\},
\tag{3}
\]

并取一个奇素数 \(q\mid D_*\)，满足

\[
q\equiv-1\pmod {2s}.
\tag{4}
\]

因此 \(q>s\)。定义三个只含 actual stutter 参数的整数

\[
\Delta_s=ms^2-s+1,
\qquad
F_s^+=sh-1,
\qquad
F_s^-=s(h-1)+1.
\tag{5}
\]

已有的 \(A=1\) root-residue low-gap adapter 表明：若 \(q\mid F_s^+\)，
则 \(q\) 直接给出 Type II terminal 与严格两尾递降。本卡刻画同一个
\(q\mid\Delta_s\) 碰撞何时落在该正根，何时则必定进入尚未闭合的负支。

## 2. 精确二根恒等式

直接展开得到

\[
\begin{aligned}
F_s^+F_s^-
&=(sh-1)(sh-s+1)\\
&=s^2h(h-1)+s-1.
\end{aligned}
\tag{6}
\]

与 (2) 相加，给出整数恒等式

\[
\boxed{
\Delta_s+F_s^+F_s^-
=s^2\bigl(m+h(h-1)\bigr)
=s^2Da.}
\tag{7}
\]

由于 \(q\mid D\) 且 \(q\nmid s\)，有

\[
\boxed{
q\mid\Delta_s
\Longleftrightarrow
q\mid F_s^+F_s^-.}
\tag{8}
\]

而 (4) 蕴涵 \(q>s>s-2\)。若 \(q\) 同时整除两个根因子，则它整除

\[
F_s^+-F_s^-=s-2,
\tag{9}
\]

矛盾。因此得到精确互斥分派

\[
\boxed{
q\mid\Delta_s
\Longrightarrow
\left[
q\mid F_s^+
\quad\mathbin{\dot\lor}\quad
q\mid F_s^-
\right].}
\tag{10}
\]

这里的 \(\dot\lor\) 表示恰有一个分支成立。

## 3. 正根是已知的严格递降

若 \(q\mid F_s^+\)，则

\[
q\mid(D_*,sh-1),
\qquad
q\equiv-1\pmod {2s}.
\tag{11}
\]

这正是已有 \(A=1\) source-factor gate。令

\[
K=\frac{q+1}{s},
\qquad
C=\frac{p+s}{4q},
\qquad
n=\frac{p+s}{s+1}.
\tag{12}
\]

则 \(K\) 为偶数、\(K=\langle h\rangle_q\)，并且

\[
\frac4n=\frac1{qC}+\frac1{CK}+\frac1{qCK},
\qquad
\frac4p=\frac1{qC}+\frac1{pCK}+\frac1{pqCK},
\qquad
n<p.
\tag{13}
\]

所以正根是一个直接 terminal，同时给出明确的 singleton marked two-tail lift。

## 4. 负根精确选择一般二次扇的负支

若 \(q\mid F_s^-\)，仍令

\[
K=\frac{q+1}{s}.
\tag{14}
\]

由 (4)，\(K\) 是偶数；由 \(q>s\)，有 \(1<K<q\)。现在

\[
s(1-h)\equiv1\equiv sK\pmod q,
\]

故

\[
K\equiv1-h\pmod q.
\tag{15}
\]

利用 (2)，得到已有二次移位的精确剩余

\[
m+K(K-1)
\equiv m+(1-h)(-h)
\equiv0\pmod q.
\tag{16}
\]

并且

\[
(K-1)p-1\equiv-hp-1\equiv0\pmod q.
\tag{17}
\]

另一方面，\(q\nmid Kp+1\)：若它也成立，则通用正支反推
\(K\equiv h\pmod q\)，与 (15) 合并得到 \(2h\equiv1\pmod q\)。再和
\(sh\equiv s-1\pmod q\) 联立会给出 \(s\equiv2\pmod q\)，这与 \(q>s\) 矛盾。

所以负根并不产生第 3 节的 terminal；它精确落在

\[
\boxed{
q\mid((K-1)p-1),
\qquad
q\nmid Kp+1,}
\tag{18}
\]

即一般偶 \(K\) 二次扇此前保留的负线性因子。这个结论把
\(\gcd(D_*,\Delta_s)\) 的同余碰撞从一个模糊的潜在命中，压缩为已关闭的正根或
需要新 adapter 的负支。

## 5. q-local 正负控制

正根控制

\[
(p,q,h,m,s)=(337,17,6,4,3)
\tag{19}
\]

满足 \(17\mid F_3^+=17\)，并按 (13) 下降到 \(n=85\)。

负根控制

\[
(p,q,h,m,s)=(433,11,30,10,3)
\tag{20}
\]

满足

\[
11\mid D=4301,
\qquad
11\mid ph+1,
\qquad
11\nmid h^2-1,
\tag{21}
\]

并有

\[
\Delta_3=88,
\qquad
F_3^+=89,
\qquad
F_3^-=88.
\tag{22}
\]

这里 \(K=(11+1)/3=4\)，所以

\[
11\mid(4-1)\cdot433-1,
\qquad
11\nmid4\cdot433+1.
\tag{23}
\]

这个控制具有核心素数和 transverse \(q\)-local 算术，但不声称
\((20)\) 是 actual root receipt。它严格表明：只用这里列出的局部 stutter、
\(m\)-多项式和剩余类条件，不能把 \(\Delta_s\) 的碰撞错误升级为正根 terminal。

## 6. 边界与下一缺口

本卡没有证明任何 actual \(\gcd(D_*,\Delta_s)\) 非平凡，也没有关闭 (18) 的负支。
它得到的是一个 exact capacity map：

\[
\gcd(D_*,\Delta_s)
\quad\longrightarrow\quad
\begin{cases}
\gcd(D_*,F_s^+) & \text{直接 Type II terminal 与严格递降},\\
\gcd(D_*,F_s^-) & \text{一般二次扇的负支}.
\end{cases}
\tag{24}
\]

所以后续若从 \(m\)-side 容量、\(D_*\mid m+2r\) 或固定系数因子入手，唯一有机会
推进全称出口的新增目标是：将 (18) 的 actual negative branch 转化为另一张短证书、
一个带完整 state contract 的递降，或由 actual maximality/provenance 排除。不能再把
\(\Delta_s\) 的单一素因子命中误记为已经关闭。

## 聚焦复现

~~~bash
python3 reproductions/type_i_root_capacity_stutter_transverse_root_residue_low_gap_descent.py --verify
~~~

脚本只重放 (19)--(23) 与已知正根 two-tail lift，不扫描素数、根层、分母或
selector 历史。
