---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-overlap-complete-excess-valuation-classification
title: 横向 stutter overlap 的 actual complete-excess 赋值分型
statement: >-
  对核心素数 p≡1 mod24 的 actual proper-root stutter receipt，令
  z=R-h=ED、A=(p+1)T/2、K=((p^2-1)/2)T，并取横向 overlap 素数 q|D*。
  若 q|m，令 b=v_q(m)=v_q(p+1)=v_q(h-1)、t=v_q(D)-b、
  tau=v_q(T)、zeta=v_q(z)，则 q 不整除 E 当且仅当
  zeta=b+t、tau≥t；而 q|E 当且仅当 tau=t、zeta>b+t，此时
  v_q(E)=zeta-b-t。若 q|m+2、q|p-1，令
  b=v_q(m+2)=v_q(p-1)=v_q(h+1)，则 q 不整除 E 当且仅当
  zeta=b+t、tau≥t；而 q|E 当且仅当 tau=b+t、zeta>2b+t，此时
  v_q(E)=zeta-b-t>b。另有 v_q(T)>b 时，前一支强制
  v_q(r)=b，后一支强制 v_q(r-1)=b。该分型是 actual maximal
  complete-excess 的必要 provenance 过滤器，不构造证书、解提升或全局递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-general-endpoint-divisor-gate
  - type-I-root-capacity-stutter-receipt-factor-split
  - type-I-root-capacity-stutter-transverse-overlap-valuation-alignment
topics:
  - type-I
  - root-capacity
  - stutter
  - transverse-residual
  - complete-excess
  - valuations
  - provenance
  - overlap
  - proof-boundary
sources:
  - claim: type-I-root-capacity-general-endpoint-divisor-gate
    role: canonical-maximal-complete-excess-normalization
  - claim: type-I-root-capacity-stutter-receipt-factor-split
    role: primewise-D-and-E-valuation-formula
  - claim: type-I-root-capacity-stutter-transverse-overlap-valuation-alignment
    role: overlap-base-valuation-and-T-excess
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_overlap_complete_excess_valuation.py
    role: fixed-q-primary-normalization-and-T-residue-controls
visibility: public
last_checked: '2026-08-14'
---

# 横向 stutter overlap 的 actual complete-excess 赋值分型

## 1. 设置

固定核心素数 \(p\equiv1\pmod {24}\) 的 actual proper-root stutter receipt。沿用

\[
z=R-h=ED,\qquad
A=\frac{p+1}{2}T,\qquad
C=\frac{p^2-1}{2},\qquad K=CT.
\tag{1}
\]

取一个奇素数 \(q\mid D_*\)，并置

\[
\tau=v_q(T),\qquad
\zeta=v_q(z),\qquad
\epsilon=v_q(E),\qquad
\delta=v_q(D).
\tag{2}
\]

上一张 overlap 对齐卡给出两种本卡讨论的支路：

\[
\begin{aligned}
q\mid m&:
&b&=v_q(m)=v_q(p+1)=v_q(h-1),\\
q\mid m+2,\ q\mid p-1&:
&b&=v_q(m+2)=v_q(p-1)=v_q(h+1),
\end{aligned}
\tag{3}
\]

并且在两种情形中

\[
\delta=b+t,\qquad t>0.
\tag{4}
\]

由于 \((D_*,h)=1\) 而 \(3\mid h\)，始终有 \(q\ne3\)。本卡只分析 (3) 的
\(p\pm1\) overlap，不把 \(q\mid m+2,2p+1\) 的真正横向支路混入。

## 2. actual maximal normalization 的逐素数公式

对 \(a_q=v_q(A)\)、\(k_q=v_q(K)\)，actual maximal complete-excess 归一化给出

\[
(\delta,\epsilon)=
\begin{cases}
(\zeta,0),&\zeta\le k_q,\\
(a_q,\zeta-a_q),&\zeta>k_q.
\end{cases}
\tag{5}
\]

第二行正是 \(q\) 进入 complete-excess 乘子 \(E\) 的情形。式 (5) 不能由
抽象的 \(D\mid K\)、\(D\mid z\) 替代；它使用的是 canonical actual receipt 的
\(Q,\beta,(A,Q)\) 归一化。

## 3. \(p+1,h-1,m\) overlap

先设 \(q\mid m\)。由于 \(q\mid p+1\)、\(q\nmid p-1\)，由 (1) 有

\[
a_q=b+\tau,\qquad k_q=b+\tau.
\tag{6}
\]

将 (4) 代入 (5)，得到互斥且完全的两种情形：

\[
\boxed{
\begin{aligned}
q\nmid E
&\Longleftrightarrow
\zeta=b+t,\quad \tau\ge t,\quad\epsilon=0,\\
q\mid E
&\Longleftrightarrow
\tau=t,\quad\zeta>b+t,\quad
\epsilon=\zeta-b-t>0.
\end{aligned}}
\tag{7}
\]

确实，\(\zeta\le b+\tau\) 时 (5) 的第一行给出
\(\zeta=\delta=b+t\)，这等价于 \(\tau\ge t\)；而
\(\zeta>b+\tau\) 时第二行给出
\(\delta=a_q=b+\tau=b+t\)，故 \(\tau=t\)。

因此在这个 overlap 中，若 \(q\) 真正进入 \(E\)，则 \(T\) 的全部 \(q\)-容量恰好
等于 \(D\) 超过 \(h-1\) 基准的余量 \(t\)；不能额外保留 \(T\)-side slack。

## 4. \(p-1,h+1,m+2\) overlap

现在设 \(q\mid m+2\) 且 \(q\mid p-1\)。此时 \(q\nmid p+1\)，所以

\[
a_q=\tau,\qquad k_q=b+\tau.
\tag{8}
\]

代入 (4)--(5) 得

\[
\boxed{
\begin{aligned}
q\nmid E
&\Longleftrightarrow
\zeta=b+t,\quad \tau\ge t,\quad\epsilon=0,\\
q\mid E
&\Longleftrightarrow
\tau=b+t,\quad\zeta>2b+t,\quad
\epsilon=\zeta-b-t>b.
\end{aligned}}
\tag{9}
\]

这里 \(\zeta\le b+\tau\) 时仍有 \(\zeta=\delta=b+t\)；若
\(\zeta>b+\tau\)，则 (5) 给出
\(\delta=a_q=\tau=b+t\)，从而完整 \(K\)-门变为
\(b+\tau=2b+t\)。

这里的非对称性来自 \(p-1\) 的 \(q^b\) 容量属于 \(K=A(p-1)\) 却不属于 \(A\)。
所以若 \(q\) 进入 \(E\)，原始 \(z\) 的赋值不仅要超过 \(\delta=b+t\)，还必须越过
完整 \(K\)-门 \(k_q=2b+t\)；而进入 \(E\) 后留下的指数严格大于整个 overlap
基准 \(b\)。

## 5. \(T\)-high residual 对 \(r\) 的锁定

无论 \(q\) 是否进入 \(E\)，两个 \(p\pm1\) 支路还分别有恒等式

\[
2T=2p^2r-(p+1),
\tag{10}
\]

\[
2T=2p^2(r-1)+(p-1)(2p+1).
\tag{11}
\]

在 (10) 的 \(p+1\) 支路，若 \(\tau>b\)，第二项恰有 \(q\)-赋值 \(b\)。两项
赋值的非阿基米德比较强制

\[
\boxed{\tau>b,\ q\mid p+1\Longrightarrow v_q(r)=b.}
\tag{12}
\]

在 (11) 的 \(p-1\) 支路，因 \(q\ne3\) 而
\(v_q(2p+1)=0\)。同理，

\[
\boxed{\tau>b,\ q\mid p-1\Longrightarrow v_q(r-1)=b.}
\tag{13}
\]

特别地，(9) 的 \(q\mid E\) 自动有 \(\tau=b+t>b\)，所以

\[
q\mid(E,m+2,p-1)
\Longrightarrow v_q(r-1)=b.
\tag{14}
\]

而 (7) 的 \(q\mid E\) 若再有 \(t>b\)，则 \(\tau=t>b\) 并有
\(v_q(r)=b\)。

## 6. 边界

这是一条来源分型，而不是 global exit。它没有排除 (7) 的 non-excess 情形，也没有
排除 (9) 中要求更高 \(\zeta\) 的 complete-excess 情形；它更不能从
\(v_q(r)=b\) 或 \(v_q(r-1)=b\) 直接推出已有 root-capacity external source、
Type I/II 证书、严格递降或全域解提升。

不过，任何后续 transverse_residual_provenance_adapter 现在必须通过 (7)--(9)：
它不能把两个 overlap 都当成普通的 \(D_*\mid T\) 素因子，也不能把 \(p-1\) 支路的
小 \(q\)-excess 写成合法 complete-excess provenance。

## 聚焦复现

~~~bash
python3 reproductions/type_i_root_capacity_stutter_transverse_overlap_complete_excess_valuation.py --verify
~~~

脚本只重放四个固定 \(q\)-primary canonical-normalization 控制，以及两个固定的
\(T\)-high 余数控制。它们明确不冒充 actual root receipt，也不扫描素数、根层或
完整状态图。
