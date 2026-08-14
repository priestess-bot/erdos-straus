---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-negative-branch-bezout-reflection-terminal
title: 横向 stutter 负根的 Bezout 正规形、纯 T 分派与反射 Type II 终端
statement: >-
  对核心素数 p≡1 mod24 的 terminal-first 后 actual proper-root stutter receipt，取
  s∈{3,7,11,23}、奇素数 q|D*，并假设 q≡-1 mod2s、q|s(h-1)+1（低缺口负根）及
  L=(q+1)/s-1、t=(Lp-1)/q、B=((s-1)p+s)/q。则 p=st+B、
  LB-(s-1)t=1。L=1 当且仅当 (s,q) 为 (3,5) 或 (7,13)，且此时 q|p-1,h+1,m+2，
  是已有 p-1 overlap；若 L>1，则 q∤(p^2-1)(2p+1)m(m+2)(m-1)，且若
  delta=v_q(D)，则 delta=v_q(D*)=v_q(D_T)、q^delta|gcd(T/u,m+2r)，即为纯
  T-side q-adic 分派。若再有 q≡-1 mod4s(s-1)，令 C=(L+1)/(4(s-1))，则 B>=s、
  q=4sC(s-1)-1，mu=(s+B)/(s-1)、x=sBC、d=s^2C 是一张 Type II 除子证书，
  4/p=1/(sBC)+1/(psC(s-1))+1/(pBC(s-1))。故反射子类直接终止；该命题不保证
  任一 actual negative root 满足反射同余，也不提供其余 pure-T 分支的递降。
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

一般负根并不必然给出终端。以下先把所有负根按其真实 carrier 的 \(L\) 值分类；
反射子类只会在第 4 节引入。特别地，不能仅从 \(q\mid D_*\) 推出
\(q\nmid h^2-1\)：一般的 \(D_*\) 仍可能与 \(h^2-1\) 有公共素因子。

## 2. Bezout 正规形

由 (4) 定义

\[
t=\frac{Lp-1}{q}.
\tag{5}
\]

它为正整数。再注意到

\[
L\bigl((s-1)p+s\bigr)
\equiv (s-1)+sL=q\equiv0\pmod q,
\]

而 \((L,q)=1\)，故

\[
B=\frac{(s-1)p+s}{q}\in\mathbb Z_{>0}.
\tag{6}
\]

两个定义之间有精确消元：

\[
\begin{aligned}
L\bigl((s-1)p+s\bigr)-(s-1)(Lp-1)&=q,\\
\boxed{LB-(s-1)t}&=1.
\end{aligned}
\tag{7}
\]

又由 \(q=s(L+1)-1\)，有

\[
L(p-st)=1+t\bigl(q-sL\bigr)=1+t(s-1)=LB,
\]

所以

\[
\boxed{p=st+B,\qquad LB-(s-1)t=1.}
\tag{8}
\]

这把负线性分支压成两个正整数 \((t,B)\) 的 Bezout 正规形，而不是一个任意的
\(p\)-加固定缺口门。

## 3. \(L=1\) overlap 与 \(L>1\) 纯 \(T\)-side 的精确二分

负根不应一概被称为横向 carrier。首先，若 \(L=1\)，则

\[
q=s(L+1)-1=2s-1.
\tag{12}
\]

在 \(s\in\{3,7,11,23\}\) 中，右端为奇素数只可能是

\[
\boxed{(s,q)=(3,5)\quad\text{或}\quad(7,13).}
\tag{13}
\]

而 (3)--(4) 此时精确给出

\[
q\mid p-1,
\qquad q\mid h+1,
\qquad q\mid m+2.
\tag{14}
\]

所以 \(L=1\) 不是新的 pure-transverse 分支，而是已有的
\(p-1,h+1,m+2\) overlap。更精确地，令

\[
b=v_q(m+2)=v_q(p-1)=v_q(h+1),
\qquad \delta=v_q(D).
\tag{15}
\]

已有 overlap 赋值对齐给出 \(b<\delta\)，并令 \(t_0=\delta-b\) 后有

\[
v_q(D_*)=v_q(D_T)=t_0,
\qquad q^{t_0}\mid T.
\tag{16}
\]

因此这两个小 carrier 应送入已有的 \(p-1\) receipt/relay checkpoint，不能误投递到
本卡的纯 \(T\)-side 分派。

以下设

\[
L>1.
\tag{17}
\]

由 \(q=s(L+1)-1\) 和 \(s\ge3\)，有

\[
0<L-1<L+1<L+2<q.
\tag{18}
\]

由 \(Lp\equiv1\pmod q\)，若 \(q\mid p-1\)、\(q\mid p+1\) 或
\(q\mid2p+1\)，分别会给出 \(q\mid L-1\)、\(q\mid L+1\) 或
\(q\mid L+2\)，均与 (18) 矛盾。因此

\[
q\nmid(p^2-1)(2p+1).
\tag{19}
\]

同样由 (4)，

\[
m\equiv-L(L+1),
\qquad
m+2\equiv-(L-1)(L+2),
\qquad
m-1\equiv-(L^2+L+1)\pmod q.
\tag{20}
\]

前两个余数与 (18) 立即给出 \(q\nmid m(m+2)\)。对第三个，恒等式

\[
(L+1)q-s(L^2+L+1)=(s-1)L-1
\tag{21}
\]

的右端严格介于 \(0\) 与 \(q\) 之间，所以 \(q\nmid m-1\)。又由 (3)，
\(h\equiv-L\pmod q\)，故 (18) 也给出

\[
q\nmid h^2-1.
\tag{22}
\]

令 \(\delta=v_q(D)\)。由 (22) 与 (19)，actual \(C/T\) 因子分裂和横向 residual
容量图给出

\[
\boxed{
v_q(D_*)=v_q(D_T)=\delta,
\qquad
q^\delta\mid\gcd\!\left(\frac Tu,m+2r\right).}
\tag{23}
\]

所以 \(L>1\) 恰是负根的 pure \(T\)-side 情形：它避开 \(p\pm1\) overlap、
\(2p+1\) terminal 和 \(m,m+2\) 的局部入口，但保留完整 \(q\)-进高度供后续
\(T\)-provenance 或递降适配器使用。

## 4. 反射条件强制 raw-ray 的序条件

现在再额外假设反射剩余类

\[
\boxed{q\equiv-1\pmod {4s(s-1)}.}
\tag{24}
\]

由于 \(q+1=s(L+1)\)，这等价于

\[
4(s-1)\mid L+1.
\tag{25}
\]

令

\[
C=\frac{L+1}{4(s-1)}.
\tag{26}
\]

则 \(L=4(s-1)C-1>1\)，所以反射分支自动属于第 3 节的 pure \(T\)-side
情形。又 \(L\equiv-1\pmod {s-1}\)，式 (7) 因而给出

\[
B\equiv-1\pmod {s-1}.
\tag{27}
\]

若 \(B<s\)，正性与 (27) 只允许 \(B=s-2\)。代入

\[
L=4(s-1)C-1
\]

及 (7)--(8)，得到

\[
t=4(s-2)C-1,
\qquad
p=st+B=4s(s-2)C-2,
\tag{28}
\]

这与 \(p\) 为奇素数矛盾。因此

\[
\boxed{B\ge 2s-3\ge s.}
\tag{29}
\]

另一方面，由 (4) 给出

\[
q=s(L+1)-1=4sC(s-1)-1.
\tag{30}
\]

再由 (6)，

\[
qB=(s-1)p+s.
\tag{31}
\]

故这正好是 `type-II-raw-ray-certificate` 的参数

\[
(A,C,K_{\rm ray})=(s,C,s-1),
\qquad
4ACK_{\rm ray}-1=q,
\qquad
B=\frac{K_{\rm ray}p+A}{q},
\tag{32}
\]

并且 (29) 给出其唯一序条件 \(A\le B\)。令

\[
\mu=\frac{s+B}{s-1},
\qquad
x=sBC,
\qquad d=s^2C.
\tag{33}
\]

由 raw-ray 证书引理，\((\mu,x,d)\) 是合法 Type II 除子证书，显式为

\[
\boxed{
\frac4p=
\frac1{sBC}+
\frac1{psC(s-1)}+
\frac1{pBC(s-1)}.}
\tag{34}
\]

这是终端证书；不需要先构造一个较小分母，也不应把它表述成负根的一般 lift。

## 5. 固定 q-local 控制

\(L=1\) overlap 可由固定 q-local 控制

\[
(p,q,h,m,s)=(241,5,39,18,3)
\tag{35}
\]

检验。它给出

\[
(L,t,B)=(1,48,97),
\qquad
v_5(D)=2,
\qquad
v_5(p-1)=v_5(h+1)=v_5(m+2)=v_5(D_*)=1.
\tag{36}
\]

一般 \(L>1\) Bezout 正规形可由两个 q-local 负根控制检验：

\[
(p,q,h,m,s)=(313,17,12,4,3),
\qquad
(3313,41,36,11,7).
\tag{37}
\]

二者均给出 \(L=5\)，分别有

\[
(t,B)=(92,37),
\qquad
(t,B)=(404,485),
\]

并满足 (8)、(18)--(22) 所用的 q-local 同余，但不满足反射同余，故不应被误报为
terminal。式 (23) 只在 actual receipt 上由既有容量图提供，并非这两个控制所声称的
性质。

反射控制为

\[
(p,q,h,m,s)=(769,23,39,13,3).
\tag{38}
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
\tag{39}
\]

四个控制都只满足这里使用的 q-local 负根同余；其 \(D\) 都不整除 \(ph+1\)。
它们验证代数接口与证书恢复，绝不冒充 actual stutter receipt。

## 6. 边界

本卡只关闭满足反射条件 (24) 的 actual negative-root carrier。它没有证明：

* 每个 actual negative root 都有这种反射载体；
* 一个未命中的 \(D_*\) 必有另一条 Type I/II terminal；
* 未命中负根可以递降到较小分母并带全域 lift；
* G/Type I global exit 的全局严格良基势。

所以上述分派是负根的一个新的 terminal-first 组织方式，不是全称选择器的完成。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_negative_branch_bezout_reflection_terminal.py --verify
```

脚本只检查 (35)--(39) 的 q-local 恒等式、反射 raw-ray 证书和分母等式；它不扫描
素数、receipt、状态图或历史结果。
