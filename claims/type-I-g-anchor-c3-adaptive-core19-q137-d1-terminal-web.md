---
kind: claim
claim_id: type-I-g-anchor-c3-adaptive-core19-q137-d1-terminal-web
title: q=137 实际 raw 族的 d=1 Type II moving-terminal 网
statement: 在 q=137 actual raw family p(w)=193+772716168w 的 w>=0 prime parameter 上，给定任意 m>0、m=3 (mod 4)，标准 d=1 Type II factor-pair terminal 在参数 w 处成立，当且仅当 gcd(m,772716168)=1 且 w= -197*772716168^(-1) (mod m)。对每个这样的 m，取最小非负代表 w_m 并写 w=w_m+mt，则 p=p0+772716168*m*t、gcd(p0,772716168*m)=1、p=1 (mod 24)；Dirichlet 给出无穷多个 prime parameter，且每个都有 explicit d=1 Type II identity 4/p=1/x+1/(pK)+1/(pKx)，其中 K=((p+4)/m+1)/4、x=mK-1。已有 q=137 raw receipt 在这些 prime 点仍实际成立，但必须 terminal-first 关闭。该网只精确分类 d=1 factor-pair terminal，不覆盖 d>1 或全部参数。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-adaptive-core19-q137-first-entry-family
topics:
  - type-I
  - Type-II
  - c3
  - core19
  - raw-source
  - q137
  - affine-family
  - moving-terminal
  - d-one
  - terminal-first
  - Dirichlet
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_c3_adaptive_core19_q137_first_entry_family.py
    role: exact d=1 terminal-web congruence, affine identities, and controls
visibility: public
last_checked: '2026-08-07'
---

# q=137 实际 raw 族的 d=1 moving-terminal 网

这张卡把此前 \(m=1319\) 的 terminal 子射线推广为 q=137 actual raw family 中所有
可能的 \(d=1\) factor-pair gap 的精确同余分类。它不是全覆盖定理，但它说明这条 raw
family 不是仅在一个偶然子射线上被 terminal 抢占。

## 1. Family 与唯一同余类

已有 actual raw family 的参数为

\[
p(w)=P+Dw,\qquad
P=193,\qquad
D=772716168=2^3 3^2\cdot7\cdot19^2\cdot31\cdot137.
\tag{1}
\]

固定 \(m>0\)、\(m\equiv3\pmod4\)。若 \((m,D)=1\)，定义唯一代表

\[
w_m\equiv-(P+4)D^{-1}=-197D^{-1}\pmod m,
\qquad0\le w_m<m.
\tag{2}
\]

于是

\[
w=w_m+mt
\Longleftrightarrow
m\mid p(w)+4.
\tag{3}
\]

反过来，若某个 \(w\) 满足 \(m\mid p(w)+4\)，则

\[
(m,D)\mid(P+4)=197.
\tag{4}
\]

而 \((D,197)=1\)，所以 \((m,D)=1\)。故 (2)--(3) 精确分类该 affine family
中所有的 \(d=1\) gap，而没有遗漏与 \(D\) 不互素的情形。

## 2. Direct Type II identity

在 (3) 的参数线上写

\[
\begin{aligned}
p_t&=P+D(w_m+mt),\\
L_t&=\frac{p_t+4}{m},\\
K_t&=\frac{L_t+1}{4},\\
x_t&=mK_t-1.
\end{aligned}
\tag{5}
\]

因 \(p_t\equiv1\pmod4\)、\(m\equiv3\pmod4\)，有 \(L_t\equiv3\pmod4\)，所以
\(K_t\) 为正整数。并且

\[
p_t+4=m(4K_t-1),\qquad
4x_t=p_t+m.
\tag{6}
\]

于是

\[
\boxed{
\frac4{p_t}
=\frac1{x_t}+\frac1{p_tK_t}+\frac1{p_tK_tx_t}.}
\tag{7}
\]

这正是标准 factor-pair 的 \(d=1\) 情形：

\[
1\mid x_t^2,\qquad
m\mid x_t+1.
\tag{8}
\]

因为 \(m\ne3\)（\(3\mid D\)），又 \(L_t\ge3\)，可得 \(p_t\ge3m-4>m+2\)；
所以 \(0<x_t<p_t\)，分母为正且严格有序。对 prime \(p_t\)，(7) 是直接 Type II
证书。

## 3. 无限 prime subray 与 raw admission

由 (5) 有

\[
p_t=p_0+Dm\,t.
\tag{9}
\]

又

\[
(p_0,D)=(P,D)=1,\qquad
(p_0,m)=(-4,m)=1,
\tag{10}
\]

故 \((p_0,Dm)=1\)。由于 \(24\mid D\)，初项为 \(1\pmod {24}\)、步长为
\(0\pmod {24}\)。Dirichlet 定理给出每个固定 \(m\) 的无穷多个 prime parameter。

同时 \(0\le w_m<m\)、\(t\ge0\) 保证 \(w\ge0\)，所以已有
\(v=12369w\) 的 actual \(137;\operatorname{Fac}(Q)\) raw receipt 在每个 prime
parameter 上仍然成立。可是 (7) 必须在任何 raw RESET 或 selector dispatch 前由
terminal-first 使用。

## 4. Controls 与边界

复现器用三个代表性 gap 验证完整 affine identity：

\[
(m,w_m)=(11,3),\qquad(55,36),\qquad(1319,1).
\tag{11}
\]

其中 \(m=55\) 表明 gap 无需为素数；\(m=1319\) 恰为此前已登记 terminal 子射线。
\(w=0,p=193\) 不属于这张 \(d=1\) 网，因为 \(p+4=197\equiv1\pmod4\)，但它另有
\((m,d)=(7,20)\) terminal。

本卡只分类 \(d=1\) factor-pair terminal。它既不排除同一参数的 \(d>1\) terminal，
也不声称每个 raw parameter 都落在某条 moving-terminal 子射线上。

窄复现：

    python3 reproductions/type_i_c3_adaptive_core19_q137_first_entry_family.py --verify
