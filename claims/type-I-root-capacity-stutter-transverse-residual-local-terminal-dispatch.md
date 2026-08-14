---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-residual-local-terminal-dispatch
title: 横向 stutter 残余的 m 与 m 加二局部终端分流
statement: >-
  对核心素数 p≡1 mod24 的 terminal-first 后 actual proper-root stutter receipt，令
  D*=D/gcd(D,h^2-1)，m=(D+h-1)/p。对任一奇素数 q|D*：若 q|m，则
  q|p+1、q|h-1；若再有 q≡3 mod4，则 p 有显式 p+1 Type I 证书。若 q|m+2，则
  恰有 q|p-1、q|h+1 或 q|2p+1、q|h-2 两种情形；在第二种且 q≡5 mod8 时，
  s=(q+1)/2、C=(p+s)/(4q) 给出显式 Type II 证书
  4/p=1/(qC)+1/(2pC)+1/(2pqC)。因此未被这些直接终端关闭的残余在 m 分支
  必避开 3 mod4 素因子，在 m+2 的 2p+1 分支必避开 5 mod8 素因子；剩余的
  p-1 分支是 h+1 overlap，不是全局出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-transverse-residual-capacity-map
  - p-plus-one-sqrt-certificate
  - type-II-k2-adjacent-type-I-cross-chart-bridge
  - short-certificate-equivalence
topics:
  - type-I
  - type-II
  - root-capacity
  - stutter
  - transverse-residual
  - terminal-dispatch
  - local-congruence
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-transverse-residual-capacity-map
    role: actual-D-star-transverse-residual-input
  - claim: p-plus-one-sqrt-certificate
    role: p-plus-one-Type-I-terminal
  - claim: type-II-k2-adjacent-type-I-cross-chart-bridge
    role: two-p-plus-one-Type-II-specialization
  - claim: short-certificate-equivalence
    role: direct-Type-II-certificate-verifier
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_residual_local_terminal_dispatch.py
    role: fixed-Type-I-and-Type-II-terminal-controls
visibility: public
last_checked: '2026-08-14'
---

# 横向 stutter 残余的 \(m\) 与 \(m+2\) 局部终端分流

## 1. 设置

固定核心素数

\[
p\equiv1\pmod {24}.
\]

在 terminal-first 后，设一个 actual proper-root stutter receipt 仍存在，记

\[
M_0=\frac{p^2+p+1}{3},\qquad
u=(2r+1,M_0),\qquad h=3u,
\tag{1}
\]

\[
D=mp+1-h,\qquad D\mid ph+1,
\qquad D_*=\frac{D}{(D,h^2-1)}.
\tag{2}
\]

由 \(D\mid ph+1\) 及 \(h=3u\)，有 \((D_*,h)=1\)。此前的横向残余容量图还给出
\(D_*>1\) 以及

\[
\bigl(D_*,pM_0(2r+1)(m-1)\bigr)=1.
\tag{3}
\]

本卡只讨论一个奇素数 \(q\mid D_*\) 额外落入 \(m\) 或 \(m+2\) 时会发生什么。
它不声称每个 \(D_*\) 都有这种素因子：一般残余仍可能与 \(m(m+2)\) 互素。

## 2. \(q\mid m\) 时的 \(p+1\) 终端

若 \(q\mid m\)，将其代入 (2) 的第一式和第二式，分别得到

\[
h\equiv1\pmod q,
\qquad
p\equiv-1\pmod q.
\tag{4}
\]

也就是

\[
\boxed{q\mid m\Longrightarrow q\mid h-1\ \text{且}\ q\mid p+1.}
\tag{5}
\]

特别地，若 \(q\equiv3\pmod4\)，则 \(q\) 是 \((p+1)/2\) 的奇素因子。令

\[
x=\frac{p+q}{4},\qquad d=x.
\tag{6}
\]

因为 \(q\mid p+1\)，有

\[
d=x\mid x^2,\qquad q\mid px+d=x(p+1).
\tag{7}
\]

而 \(q\) 是 \(p+1\) 的奇真因子，故 \(3\le q\le p-2\)。于是 (6)--(7) 是一张
Type I 证书，显式分母为

\[
\boxed{
\frac4p=
\frac1x+
\frac1{x(p+1)/q}+
\frac1{px(p+1)/q}.}
\tag{8}
\]

无条件的终端蕴涵可写成

\[
\boxed{
q\mid(D_*,m),\ q\equiv3\pmod4
\Longrightarrow \text{(8) 是一张 Type I 证书}.}
\tag{9}
\]

因此若 terminal-first 已执行这个直接 verifier 而仍未关闭，则
\((D_*,m)\) 的每个奇素因子都必须是 \(1\pmod4\)。

式 (4) 还表明这个分支在 \(h-1\) overlap 上。由于 \(q\mid D_*\)，它只能由
\(D\) 超过该 \(h-1\) 重叠的赋值余量承载，不能被误称为全新的 root-capacity 因子。

## 3. \(q\mid m+2\) 的二分

若 \(q\mid m+2\)，(2) 的第一式给出

\[
h\equiv1-2p\pmod q.
\tag{10}
\]

把它代入 \(ph+1\equiv0\pmod q\)，得到

\[
(p-1)(2p+1)\equiv0\pmod q.
\tag{11}
\]

又 \(q\ne3\)，因为 \(3\mid h\) 而 \((D_*,h)=1\)。并且

\[
(p-1,2p+1)=(p-1,3)=3.
\tag{12}
\]

所以 (11) 中恰有一个因子被 \(q\) 整除，给出精确二分：

\[
\boxed{
q\mid m+2
\Longrightarrow
\begin{cases}
q\mid p-1, & q\mid h+1;\\
\text{或}\\[-6pt]
q\mid2p+1, & q\mid h-2.
\end{cases}}
\tag{13}
\]

第一行仍在 \(h+1\) overlap 上；因为 \(q\mid D_*\)，这里同样只留下高于该
overlap 的 \(q\)-进余量。第二行则满足 \(h\equiv2\pmod q\)，故对 \(q\ne3\)
完全不与 \(h^2-1\) 重合，是一个真正的横向 \(2p+1\) 分支。

## 4. \(2p+1\) 的五模八 Type II 终端

考虑 (13) 的第二行，并再假设

\[
q\equiv5\pmod8.
\tag{14}
\]

定义

\[
s=\frac{q+1}{2},\qquad
C=\frac{p+s}{4q}.
\tag{15}
\]

这两个整数都良定义。确实，\(s\equiv3\pmod4\)，而

\[
2(p+s)=2p+1+q
\tag{16}
\]

被 \(q\) 整除；\(p+s\) 又被 4 整除，故 \(C\in\mathbb N\)。此外
\(2p+1\equiv3\pmod8\)，所以 \(q\) 不可能等于 \(2p+1\)。作为奇数真因子，

\[
q\le\frac{2p+1}{3},\qquad
3\le s\le\frac{p+2}{3}<p-2.
\tag{17}
\]

令 Type II 的首分母和除子为

\[
x=qC=\frac{p+s}{4},\qquad d=C.
\tag{18}
\]

则

\[
d=C\mid x^2,\qquad d\le x,\qquad
s\mid x+d=C(q+1)=2sC.
\tag{19}
\]

所以 (18)--(19) 是自然范围的 Type II 证书，且直接恢复为

\[
\boxed{
\frac4p=
\frac1{qC}+
\frac1{2pC}+
\frac1{2pqC}.}
\tag{20}
\]

这也正是 \(K=2\) 相邻 Type I/II 桥在 \(L=q=2s-1\) 的一个专门化。

这里同样有无条件的终端蕴涵

\[
\boxed{
q\mid(D_*,m+2,2p+1),\ q\equiv5\pmod8
\Longrightarrow \text{(20) 是一张 Type II 证书}.}
\tag{21}
\]

因此若 terminal-first 已执行 (20) 而仍未关闭，
\((D_*,m+2,2p+1)\) 的每个奇素因子都必须避开 \(5\pmod8\)。

## 5. 边界

(9) 和 (21) 只处理 \(D_*\) 恰好碰到 \(m\) 或 \(m+2\) 的局部支撑；它们不证明
这种碰撞存在，也不关闭 (13) 的 \(p-1,h+1\) overlap 分支。特别地，不能从
\(D_*\mid m+2r\) 推出 \(D_*\mid m(m+2)\)。因此本卡提供的是两条可注册的
direct terminal 分支和一条剩余素因子筛，而不是全局证书或递降证明。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_residual_local_terminal_dispatch.py --verify
```

脚本固定重建一张 \(p+1\) Type I 控制及两张 \(2p+1\)、\(5\pmod8\) Type II
控制，逐项核对因子条件、自然缺口范围与三分母恒等式；它不扫描素数，也不把固定控制
冒充 actual stutter receipt。
