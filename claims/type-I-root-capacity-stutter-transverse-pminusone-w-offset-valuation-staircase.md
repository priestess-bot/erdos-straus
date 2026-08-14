---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-pminusone-w-offset-valuation-staircase
title: p 减一 complete-excess 横向素因子的 w 加九赋值阶梯
statement: >-
  对核心素数 p≡1 mod24 的 actual proper-root stutter receipt，令
  u=h/3、w=(2r+1)/u。若 q|(E,D*,m+2,p-1) 是 p-1,h+1 complete-excess
  overlap 素数，b=v_q(p-1)、t=v_q(D)-b>0，则
  p^2u(w+9)=2T+(p-1)^2+3p(ph+1)，并且
  v_q(w+9)=b+t 当 0<t<b，等于 2b 当 t>b，且至少为 2b 当 t=b。
  在共振 t=b 时，v_q(w+9)>2b 当且仅当
  2T/q^(2b)+((p-1)/q^b)^2≡0 mod q。故 w+9 的额外 q 容量由 t 相对 b 的
  精确阶梯与一个显式共振门给出；该容量描述尚不构造短证书、解提升或全局出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-transverse-residual-capacity-map
  - type-I-root-capacity-stutter-transverse-overlap-receipt-relay
  - type-I-root-capacity-stutter-transverse-pminusone-root-quotient-orientation
topics:
  - type-I
  - root-capacity
  - stutter
  - transverse-residual
  - complete-excess
  - p-minus-one
  - root-quotient
  - valuations
  - capacity-map
  - resonance
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-transverse-residual-capacity-map
    role: proper-root-quotient-and-q-coprimality
  - claim: type-I-root-capacity-stutter-transverse-overlap-receipt-relay
    role: exact-T-and-ph-plus-one-valuations
  - claim: type-I-root-capacity-stutter-transverse-pminusone-root-quotient-orientation
    role: prior-one-extra-q-orientation
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_pminusone_w_offset_valuation_staircase.py
    role: fixed-q-primary-valuation-staircase-controls
visibility: public
last_checked: '2026-08-14'
---

# \(p-1\) complete-excess 横向素因子的 \(w+9\) 赋值阶梯

## 1. 输入

固定核心素数 \(p\equiv1\pmod {24}\) 的 actual proper-root stutter receipt，记

\[
u=\frac h3,\qquad
w=\frac{2r+1}{u},\qquad
T=p^2r-\frac{p+1}{2}.
\tag{1}
\]

设 \(q\) 是 \(p-1,h+1\) overlap 中的 complete-excess 奇素数：

\[
q\mid(E,D_*,m+2,p-1),
\qquad
b=v_q(p-1),
\qquad
t=v_q(D)-b>0.
\tag{2}
\]

横向残余容量图给出 \(q\nmid u\)。receipt relay 则给出精确赋值

\[
v_q(T)=b+t,
\qquad
v_q(ph+1)=2b+t.
\tag{3}
\]

因为 \(q\ne3\) 且 \(q\nmid p\)，\(2,3,p,u\) 都是 \(q\)-单位。

## 2. \(w+9\) 的精确恒等式

由 \(u(w+9)=2r+1+3h\) 以及 \(2T=2p^2r-(p+1)\)，直接有

\[
\begin{aligned}
p^2u(w+9)
&=p^2(2r+1+3h)\\
&=2T+(p+1)+p^2+3p^2h\\
&=\boxed{2T+(p-1)^2+3p(ph+1)}.
\end{aligned}
\tag{4}
\]

这条恒等式把此前只有下界的 root-index offset 直接接到 actual receipt 的
\(T\)-side excess 与 \(ph+1\) receipt quotient。

## 3. 非共振阶梯

由 (3)--(4)，右侧三项的 \(q\)-赋值依次为

\[
b+t,\qquad 2b,\qquad 2b+t.
\tag{5}
\]

若 \(0<t<b\)，第一个数严格最小；若 \(t>b\)，第二个数严格最小。由于
\(p^2u\) 是 \(q\)-单位，非阿基米德比较给出

\[
\boxed{
v_q(w+9)=
\begin{cases}
b+t, & 0<t<b,\\[3pt]
2b, & t>b.
\end{cases}}
\tag{6}
\]

因此此前只知的 \(q^{b+1}\mid w+9\) 可在所有非共振 complete-excess state
中升级为精确可计数的 \(q\)-容量。

## 4. 共振门

若 \(t=b\)，(5) 的前两项同为 \(2b\)，所以 (4) 先给出

\[
\boxed{v_q(w+9)\ge2b.}
\tag{7}
\]

将 (4) 除以 \(q^{2b}\) 并模 \(q\) 化简。第三项的赋值为 \(3b\)，故消失；于是

\[
p^2u\frac{w+9}{q^{2b}}
\equiv
2\frac{T}{q^{2b}}+
\left(\frac{p-1}{q^b}\right)^2
\pmod q.
\tag{8}
\]

左侧的系数仍是 \(q\)-单位，因此更高一层容量有精确充要判据：

\[
\boxed{
v_q(w+9)>2b
\Longleftrightarrow
2\frac{T}{q^{2b}}+
\left(\frac{p-1}{q^b}\right)^2
\equiv0\pmod q.}
\tag{9}
\]

式 (9) 不是一个自动终端；它只把唯一的 valuation resonance 变成可直接计算的
q-primary gate。

## 5. 与现有定向的关系和边界

因为 \(b,t\ge1\)，(6)--(7) 蕴涵 \(v_q(w+9)\ge b+1\)，严格加强已有的
\(w+9\) 一层额外 \(q\) 定向。它仍不能让 \(q\) 进入旧的 \(q\mid u\)
external-source 菜单：这里始终有 \(q\nmid u\)。因此该结果提供的是 future
transverse-residual adapter 可调用的精确 offset capacity，而不是 Type I/II
证书、\(p-1\) source-tail witness、identity lift 或 global exit。

## 聚焦复现

~~~bash
python3 reproductions/type_i_root_capacity_stutter_transverse_pminusone_w_offset_valuation_staircase.py --verify
~~~

脚本重放四个固定 q-primary 控制：两个 proper-root 输入分别覆盖共振和 \(t>b\)，
另两个局部整数控制覆盖 \(t<b\) 与共振门命中。后两者明确不被冒充为 root receipt；
脚本不扫描素数、根层或状态图。
