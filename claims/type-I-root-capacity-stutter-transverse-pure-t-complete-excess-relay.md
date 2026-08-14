---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-pure-t-complete-excess-relay
title: 横向 stutter 纯 T 侧负根的 complete-excess 分型与 checkpoint relay
statement: >-
  对核心素数 p≡1 mod24 的 actual nonterminal proper-root stutter receipt，令
  z=R-h=ED、E=1+p sigma、e=(ph+1)/D、A=(p+1)T/2、K=((p^2-1)/2)T。
  若奇素数 q|D* 是 L>1 low-gap negative-root carrier，置
  tau=v_q(T)、zeta=v_q(z)、delta=v_q(D)、epsilon=v_q(E)，则
  q 不整除 E 当且仅当 zeta=delta 且 tau≥delta；q|E 当且仅当
  tau=delta、zeta>delta，此时 epsilon=zeta-delta。恒有
  v_q(pE+e)=tau-delta。特别地，q|E 时 e 是 q-单位；tau>delta 时
  E,e 都是 q-单位且 q^(tau-delta) 恰整除 pE+e。在 a=1,d=1 checkpoint
  中令 B0=2pr-1、B1=B0E-sigma、E1=(p-1)B1-1。若 q|E，则
  sigma≡E1≡h≡-L、B0≡B1≡L mod q，且 q^epsilon|pE1+1。
  这是 pure T-side complete-excess 的 actual provenance/capacity relay，
  不单独构造 Type I/II 证书、可注册递降边或全局出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-general-endpoint-divisor-gate
  - type-I-root-capacity-stutter-receipt-factor-split
  - type-I-root-capacity-stutter-transverse-negative-branch-bezout-reflection-terminal
  - type-I-root-capacity-stutter-transverse-pure-t-synchronization-boundary
  - type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
topics:
  - type-I
  - root-capacity
  - stutter
  - transverse-residual
  - negative-branch
  - pure-T-side
  - complete-excess
  - receipt-quotient
  - checkpoint-relay
  - valuations
  - provenance
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-receipt-factor-split
    role: primewise-actual-maximal-complete-excess-normalization
  - claim: type-I-root-capacity-stutter-transverse-negative-branch-bezout-reflection-terminal
    role: L-greater-than-one-pure-T-side-negative-root-data
  - claim: type-I-root-capacity-stutter-transverse-pure-t-synchronization-boundary
    role: actual-T-side-synchronization-and-normalized-receipt-interface
  - claim: type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
    role: canonical-checkpoint-B-one-and-E-one-formulas
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_pure_t_complete_excess_relay.py
    role: fixed-q-primary-normalization-and-checkpoint-relay-controls
visibility: public
last_checked: '2026-08-14'
---

# 横向 stutter 纯 \(T\) 侧负根的 complete-excess 分型与 checkpoint relay

## 1. 设置

固定核心素数

\[
p\equiv1\pmod {24}.
\]

在 terminal-first 后，设仍有一个 actual nonterminal proper-root stutter receipt，写

\[
z=R-h=ED,
\qquad
e=\frac{ph+1}{D},
\qquad
A=\frac{p+1}{2}T,
\qquad
K=\frac{p^2-1}{2}T.
\tag{1}
\]

nonterminal 分支的 canonical complete-excess multiplier 满足

\[
E=1+p\sigma,
\qquad \sigma\in\mathbb Z_{>0}.
\tag{2}
\]

取一个 \(L>1\) 的 low-gap negative-root carrier

\[
s\in\{3,7,11,23\},
\qquad q\mid D_*,
\qquad q\equiv-1\pmod {2s},
\qquad q\mid s(h-1)+1,
\tag{3}
\]

其中 \(q\) 为奇素数。

并令

\[
L=\frac{q+1}{s}-1,
\qquad
\tau=v_q(T),
\quad \zeta=v_q(z),
\quad \delta=v_q(D),
\quad \epsilon=v_q(E).
\tag{4}
\]

已有 pure \(T\)-side 分派给出

\[
Lp\equiv1\pmod q,
\qquad h\equiv-L\pmod q,
\qquad m\equiv-L(L+1)\pmod q,
\tag{5}
\]

以及

\[
q\nmid\frac{p^2-1}{2},
\qquad q\nmid h^2-1,
\qquad
v_q(D_*)=v_q(D)=\delta.
\tag{6}
\]

因此 \(q\) 在 \(A\) 与 \(K\) 中的容量完全相同：

\[
v_q(A)=v_q(K)=\tau.
\tag{7}
\]

这正是与 \(p\pm1\) overlap 不同的 pure \(T\)-side 特征。

## 2. actual maximal normalization 的完整二分

actual maximal complete-excess 归一化逐素数给出

\[
v_q(D)=
\begin{cases}
\zeta,&\zeta\le v_q(K),\\
v_q(A),&\zeta>v_q(K),
\end{cases}
\qquad
v_q(E)=
\begin{cases}
0,&\zeta\le v_q(K),\\
\zeta-v_q(A),&\zeta>v_q(K).
\end{cases}
\tag{8}
\]

代入 (7)，得到不重叠且完全的分型：

\[
\boxed{
\begin{aligned}
q\nmid E
&\Longleftrightarrow
\zeta=\delta,\quad \tau\ge\delta,\quad\epsilon=0,\\
q\mid E
&\Longleftrightarrow
\tau=\delta,\quad\zeta>\delta,\quad
\epsilon=\zeta-\delta>0.
\end{aligned}}
\tag{9}
\]

这里使用了 \(q\mid D\)，故 \(\delta>0\)。第一行表示 \(z\) 的 \(q\)-高度尚未
超过 \(T\) 的完整容量；第二行则表示 \(D\) 恰耗尽该容量，超出的高度以 \(E\) 的
complete-excess 形式保留。故 pure \(T\)-side 上 \(q\) 进入 \(E\) 的条件不是又一条
局部同余，而是 actual maximality 的精确容量饱和条件。

## 3. receipt quotient 的精确赋值桥

由 \(4K=pR+1\)、\(z=ED\) 和 \(eD=ph+1\)，有

\[
\boxed{
D(pE+e)=4K=2(p^2-1)T.}
\tag{10}
\]

根据 (6)，\(q\) 不整除右端除 \(T\) 外的因子。因此

\[
\boxed{v_q(pE+e)=\tau-\delta.}
\tag{11}
\]

这给出两条可直接交给后续 provenance adapter 的分派：

\[
\begin{aligned}
q\mid E
&\Longrightarrow \tau=\delta,
\quad v_q(pE+e)=0,
\quad v_q(e)=0;\\
\tau>\delta
&\Longrightarrow q\nmid E,
\quad v_q(e)=0,
\quad v_q(pE+e)=\tau-\delta>0.
\end{aligned}
\tag{12}
\]

第二行中 \(q\nmid E\) 来自 (9)，而 \(e\) 必为 \(q\)-单位，因为 \(pE\) 已是
\(q\)-单位。若 \(\tau=\delta\) 且 \(q\nmid E\)，(11) 只说
\(pE+e\) 是 \(q\)-单位；本卡不额外断言 \(e\) 的赋值。

## 4. excess 向下一 checkpoint 的 relay

在当前 \(a=1,d=1\) root interface，令

\[
B_0=2pr-1,
\qquad B_1=B_0E-\sigma,
\qquad E_1=(p-1)B_1-1.
\tag{13}
\]

现在设 \(q\mid E\)。由 (9)，\(\epsilon>0\) 且

\[
p\sigma\equiv-1\pmod {q^\epsilon}.
\tag{14}
\]

因此 \(B_1\equiv-\sigma\pmod {q^\epsilon}\)，从而

\[
\begin{aligned}
pE_1+1
&=p(p-1)B_1-p+1\\
&\equiv-p(p-1)\sigma-p+1\\
&\equiv0\pmod {q^\epsilon}.
\end{aligned}
\]

即

\[
\boxed{q^\epsilon\mid pE_1+1.}
\tag{15}
\]

此高赋值 relay 并不依赖 \(B_0\) 的额外整除。负根余数则把它的模 \(q\) 形状完全定向。
由 (5) 与 pure \(T\)-side 同步 \(q\mid m+2r\)，有

\[
2r\equiv L(L+1)\pmod q,
\qquad
B_0=2pr-1\equiv L\pmod q.
\tag{16}
\]

又由 \(q\mid E\) 及 (2)，\(\sigma\equiv-L\pmod q\)，故

\[
B_1\equiv-\sigma\equiv L\pmod q,
\qquad
E_1\equiv(p-1)L-1\equiv-L\pmod q.
\tag{17}
\]

结合 \(h\equiv-L\pmod q\)，可写为

\[
\boxed{
\sigma\equiv E_1\equiv h\equiv-L\pmod q,
\qquad
B_0\equiv B_1\equiv L\pmod q.}
\tag{18}
\]

所以 pure \(T\)-side 的 complete-excess 并非在归一化后消失：它以
\(q^{v_q(E)}\mid pE_1+1\) 的明确 receipt/checkpoint 边携带到下一节点。该因子
随后可精确分解为 \(pE_1+1=2(p-1)ET\)，故其中的 q-primary 部分是 \(E\) 与
\(T\) 的继承，而不是自动生成的新 checkpoint 容量；详见
[纯 \(T\) 侧 checkpoint 的因子继承与新容量阻断](type-I-root-capacity-stutter-transverse-pure-t-checkpoint-factorization-boundary.md)。

## 5. 边界与聚焦控制

式 (9)--(18) 是 actual receipt 的必要容量映射，并不表示 \(E_1\) 已通过
terminal-first、persistent lineage、全域 identity lift 或 E1--E5 的注册合同。
尤其 \(q^\epsilon\mid pE_1+1\) 不是现有 ordinary multiplier terminal menu 的自动
命中，也没有给出严格势下降。尤其不能只把 \(q^\epsilon\mid pE_1+1\) 当作新输入：
它完整分解回 \(E\) 与 \(T\)。后续 adapter 必须使用该因子之外的具体除子、额外同余、
terminal-first 分类或 identity-lift 合同；在此之前不能把本 relay 记录为 global exit。

~~~bash
python3 reproductions/type_i_root_capacity_stutter_transverse_pure_t_complete_excess_relay.py --verify
~~~

脚本只回放 \((p,q,s,L,h,m)=(313,17,3,5,12,4)\) 上的两组固定 q-primary
normalization 控制：一组 \(q\)-excess 进入 \(E\)，另一组保留严格的 \(T\)-side
slack。它们验证 (8)、(10)--(18) 的整数算术，但明确不冒充完整 actual root receipt，
也不扫描素数、receipt 或状态图。
