---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-negative-branch-bezout-reflection-terminal
title: 横向 stutter 负根的 Bezout 正规形、纯 T 分派与反射 Type II 终端
statement: >-
  对核心素数 p≡1 mod24 的 terminal-first 后 actual proper-root stutter receipt，取
  s∈{3,7,11,23}、奇素数 q|D*，并假设 q≡-1 mod2s、q|s(h-1)+1（低缺口负根）及
  q≡-1 mod4s(s-1)。令
  L=(q+1)/s-1、C=(L+1)/(4(s-1))、t=(Lp-1)/q、B=((s-1)p+s)/q。则
  p=st+B、LB-(s-1)t=1、B>=s、q=4sC(s-1)-1；因而
  mu=(s+B)/(s-1)、x=sBC、d=s^2C 是一张 Type II 除子证书，
  4/p=1/(sBC)+1/(psC(s-1))+1/(pBC(s-1))。此外，若 delta=v_q(D)，则
  q∤(p^2-1)(2p+1)m(m+2)(m-1)，且
  delta=v_q(D*)=v_q(D_T)、q^delta|gcd(T/u,m+2r)。故此反射子类的
  负根是直接 Type II terminal，并将其完整 q-adic receipt 容量定位到纯 T-side；
  它不保证任一 actual negative root 满足反射同余，也不提供未命中分支的递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-finite-curve-constraint
  - type-I-root-capacity-stutter-receipt-factor-split
  - type-I-root-capacity-stutter-transverse-residual-capacity-map
  - type-I-root-capacity-stutter-transverse-low-gap-m-polynomial-root-split
  - type-II-raw-ray-certificate
topics:
  - type-I
  - type-II
  - root-capacity
  - stutter
  - transverse-residual
  - negative-branch
  - bezout-normal-form
  - T-side-capacity
  - raw-ray
  - terminal-dispatch
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-transverse-low-gap-m-polynomial-root-split
    role: actual-low-gap-negative-root-interface
  - claim: type-I-root-capacity-stutter-transverse-residual-capacity-map
    role: actual-D-star-T-over-u-and-m-plus-two-r-allocation
  - claim: type-I-root-capacity-stutter-receipt-factor-split
    role: D-C-T-factor-split
  - claim: type-II-raw-ray-certificate
    role: raw-ray-Type-II-reconstruction
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_negative_branch_bezout_reflection_terminal.py
    role: q-local-Bezout-controls-and-reflection-terminal-certificate
visibility: public
last_checked: '2026-08-14'
---

# 横向 stutter 负根的 Bezout 正规形、纯 \(T\) 分派与反射 Type II 终端

## 1. 负根与反射子类

固定核心素数

\[
p\equiv1\pmod {24}.
\]

在 terminal-first 后，设一个 actual proper-root stutter receipt 仍存在，沿用

\[
D=mp+1-h,
\qquad D\mid ph+1,
\qquad
D_*=\frac{D}{(D,h^2-1)},
\tag{1}
\]

及根容量商记号 \(u,r,T,D_T\)。取

\[
s\in\mathcal G=\{3,7,11,23\},
\qquad
q\mid D_*,
\qquad
q\equiv-1\pmod {2s},
\tag{2}
\]

其中 \(q\) 是奇素数，并假设该 carrier 落在低缺口负根：

\[
q\mid s(h-1)+1.
\tag{3}
\]

前一张卡给出

\[
K=\frac{q+1}{s},
\qquad
L=K-1,
\qquad
Lp\equiv1\pmod q,
\qquad
m\equiv-L(L+1)\pmod q.
\tag{4}
\]

一般负根并不必然给出终端。本卡只关闭其中可由同一 carrier 读出的反射子类：

\[
\boxed{q\equiv-1\pmod {4s(s-1)}.}
\tag{5}
\]

这等价于

\[
4(s-1)\mid L+1.
\tag{6}
\]

令

\[
C=\frac{L+1}{4(s-1)}.
\tag{7}
\]

于是 \(C\) 是正整数，且 \(L=4(s-1)C-1>1\)。这个严格不等式来自 (6)，
而不是仅从 \(q\mid D_*\) 推出；一般地，\(D_*\) 仍可能与 \(h^2-1\) 有公共素因子。

## 2. Bezout 正规形

由 (4) 定义

\[
t=\frac{Lp-1}{q}.
\tag{8}
\]

它为正整数。再注意到

\[
L\bigl((s-1)p+s\bigr)
\equiv (s-1)+sL=q\equiv0\pmod q,
\]

而 \((L,q)=1\)，故

\[
B=\frac{(s-1)p+s}{q}\in\mathbb Z_{>0}.
\tag{9}
\]

两个定义之间有精确消元：

\[
\begin{aligned}
L\bigl((s-1)p+s\bigr)-(s-1)(Lp-1)&=q,\\
\boxed{LB-(s-1)t}&=1.
\end{aligned}
\tag{10}
\]

又由 \(q=s(L+1)-1\)，有

\[
L(p-st)=1+t\bigl(q-sL\bigr)=1+t(s-1)=LB,
\]

所以

\[
\boxed{p=st+B,\qquad LB-(s-1)t=1.}
\tag{11}
\]

这把负线性分支压成两个正整数 \((t,B)\) 的 Bezout 正规形，而不是一个任意的
\(p\)-加固定缺口门。

## 3. 反射条件强制 raw-ray 的序条件

由 (6)，\(L\equiv-1\pmod {s-1}\)。式 (10) 因而给出

\[
B\equiv-1\pmod {s-1}.
\tag{12}
\]

若 \(B<s\)，正性与 (12) 只允许 \(B=s-2\)。代入

\[
L=4(s-1)C-1
\]

及 (10)，得到

\[
t=4(s-2)C-1,
\qquad
p=st+B=4s(s-2)C-2,
\tag{13}
\]

这与 \(p\) 为奇素数矛盾。因此

\[
\boxed{B\ge 2s-3\ge s.}
\tag{14}
\]

另一方面，(7) 给出

\[
q=s(L+1)-1=4sC(s-1)-1.
\tag{15}
\]

再由 (9)--(10)，

\[
qB=(s-1)p+s.
\tag{16}
\]

故这正好是 `type-II-raw-ray-certificate` 的参数

\[
(A,C,K_{\rm ray})=(s,C,s-1),
\qquad
4ACK_{\rm ray}-1=q,
\qquad
B=\frac{K_{\rm ray}p+A}{q},
\tag{17}
\]

并且 (14) 给出其唯一序条件 \(A\le B\)。令

\[
\mu=\frac{s+B}{s-1},
\qquad
x=sBC,
\qquad d=s^2C.
\tag{18}
\]

由 raw-ray 证书引理，\((\mu,x,d)\) 是合法 Type II 除子证书，显式为

\[
\boxed{
\frac4p=
\frac1{sBC}+
\frac1{psC(s-1)}+
\frac1{pBC(s-1)}.}
\tag{19}
\]

这是终端证书；不需要先构造一个较小分母，也不应把它表述成负根的一般 lift。

## 4. 该终端的 q-adic 容量位置

反射条件给出 \(L>1\)，且

\[
0<L-1<L+1<L+2<q=s(L+1)-1.
\tag{20}
\]

由 \(Lp\equiv1\pmod q\)，若 \(q\mid p-1\)、\(q\mid p+1\) 或
\(q\mid2p+1\)，分别会给出 \(q\mid L-1\)、\(q\mid L+1\) 或
\(q\mid L+2\)，均与 (20) 矛盾。因此

\[
q\nmid(p^2-1)(2p+1).
\tag{21}
\]

同样由 (4)，

\[
m\equiv-L(L+1),
\qquad
m+2\equiv-(L-1)(L+2)\pmod q,
\tag{22}
\]

故 \(q\nmid m(m+2)\)。对 \(m-1\)，有

\[
(L+1)q-s(L^2+L+1)=(s-1)L-1,
\tag{23}
\]

而右端严格介于 \(0\) 与 \(q\) 之间，故 \(q\nmid m-1\)。最后，(3) 给出
\(h\equiv-L\pmod q\)，所以 (20) 也给出

\[
q\nmid h^2-1.
\tag{24}
\]

令 \(\delta=v_q(D)\)。由 (24) 及 \(q\mid D_*\)，有

\[
v_q(D_*)=\delta.
\tag{25}
\]

而 (21) 给出 \(q\nmid (p^2-1)/2\)，所以实际 \(C/T\) 因子分裂中

\[
v_q(D_T)=\delta.
\tag{26}
\]

现有横向残余容量定位给出 \(D_*\mid T/u\) 及 \(D_*\mid m+2r\)，故

\[
\boxed{
q^\delta\mid\gcd\!\left(\frac Tu,m+2r\right).}
\tag{27}
\]

所以反射负根的整个 \(q\)-primary receipt 高度都在 \(T\)-侧：它不是 \(p\pm1\)
overlap，也不是 \(m\)、\(m+2\) 的既有直接终端入口。

## 5. 固定 q-local 控制

一般 Bezout 正规形可由两个 q-local 负根控制检验：

\[
(p,q,h,m,s)=(313,17,12,4,3),
\qquad
(3313,41,36,11,7).
\tag{28}
\]

二者均给出 \(L=5\)，分别有

\[
(t,B)=(92,37),
\qquad
(t,B)=(404,485),
\]

并满足 (11) 与 (21)--(23)，但不满足反射同余，故不应被误报为 terminal。

反射控制为

\[
(p,q,h,m,s)=(769,23,39,13,3).
\tag{29}
\]

此时 \(L=7\)、\(C=1\)、\(t=234\)、\(B=67\)，而

\[
\mu=35,
\qquad x=201,
\qquad d=9,
\]

给出

\[
\frac4{769}=
\frac1{201}+
\frac1{4614}+
\frac1{103046}.
\tag{30}
\]

三个控制都只满足这里使用的 q-local 负根同余；其 \(D\) 都不整除 \(ph+1\)。
它们验证代数接口与证书恢复，绝不冒充 actual stutter receipt。

## 6. 边界

本卡仅关闭满足 (5) 的 actual negative-root carrier。它没有证明：

* 每个 actual negative root 都有这种反射载体；
* 一个未命中的 \(D_*\) 必有另一条 Type I/II terminal；
* 未命中负根可以递降到较小分母并带全域 lift；
* G/Type I global exit 的全局严格良基势。

所以 (19) 是负根的一个新的 terminal-first 分派，不是全称选择器的完成。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_negative_branch_bezout_reflection_terminal.py --verify
```

脚本只检查 (28)--(30) 的 q-local 恒等式、反射 raw-ray 证书和分母等式；它不扫描
素数、receipt、状态图或历史结果。
