---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-pure-t-checkpoint-factorization-boundary
title: 横向 stutter 纯 T 侧 checkpoint 的因子继承与新容量阻断
statement: >-
  在 a=1,d=1 canonical checkpoint，令 E=1+p sigma、B0=2pr-1、
  B1=B0E-sigma、E1=(p-1)B1-1、T=p^2r-(p+1)/2。恒有
  pE1+1=2(p-1)ET。若 q|D* 是 actual L>1 low-gap negative-root pure-T-side
  carrier，令 tau=v_q(T)、epsilon=v_q(E)，则 q 不整除 2(p-1)，并有
  v_q(pE1+1)=epsilon+tau。特别地，q|E 时 actual maximal normalization 给出
  tau=delta=v_q(D)、epsilon=v_q(R-h)-delta，故
  v_q(pE1+1)=v_q(R-h)。因此从 q^epsilon|pE1+1 读到的 q-primary 因子完全是
  E 与 T 的既有因子继承，而不是独立的 checkpoint q-adic 条件；任何终端或 lift
  若只使用这条整除式，均未增加 actual receipt 之外的 q-primary 容量。该结论只阻断
  因子复用型 adapter，不排除使用额外状态合同的 Type I/II 证书或递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
  - type-I-root-capacity-stutter-transverse-pure-t-synchronization-boundary
  - type-I-root-capacity-stutter-transverse-pure-t-complete-excess-relay
topics:
  - type-I
  - root-capacity
  - stutter
  - transverse-residual
  - negative-branch
  - pure-T-side
  - complete-excess
  - checkpoint-relay
  - factorization
  - valuations
  - provenance
  - proof-boundary
sources:
  - claim: type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
    role: canonical-checkpoint-B-zero-B-one-and-E-one-formulas
  - claim: type-I-root-capacity-stutter-transverse-pure-t-complete-excess-relay
    role: actual-pure-T-normalization-and-q-primary-relay
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_pure_t_complete_excess_relay.py
    role: fixed-checkpoint-factorization-controls
visibility: public
last_checked: '2026-08-14'
---

# 横向 stutter 纯 \(T\) 侧 checkpoint 的因子继承与新容量阻断

## 1. canonical checkpoint 的精确因子式

在 \(a=1,d=1\) root interface，写

\[
E=1+p\sigma,
\qquad
T=p^2r-\frac{p+1}{2},
\tag{1}
\]

并定义 canonical checkpoint 参数

\[
B_0=2pr-1,
\qquad B_1=B_0E-\sigma,
\qquad E_1=(p-1)B_1-1.
\tag{2}
\]

这些恒等式本节不需要 actual root receipt。首先

\[
pB_0-1=2p^2r-p-1=2T.
\tag{3}
\]

又由 \(p\sigma=E-1\)，有

\[
\begin{aligned}
pB_1-1
&=p(B_0E-\sigma)-1\\
&=pB_0E-(E-1)-1\\
&=E(pB_0-1)\\
&=2ET.
\end{aligned}
\tag{4}
\]

最后

\[
\boxed{
pE_1+1
=(p-1)(pB_1-1)
=2(p-1)ET.}
\tag{5}
\]

因此 \(pE_1+1\) 不是一个新的独立 checkpoint 因子；它在整数层已经完全分解回
当前 multiplier \(E\) 与旧 \(T\)-容量。

## 2. pure \(T\)-side 的逐赋值后果

现设 \(q\mid D_*\) 是 actual \(L>1\) low-gap negative-root carrier，并继续令

\[
\tau=v_q(T),
\qquad \epsilon=v_q(E),
\qquad
\delta=v_q(D),
\qquad \zeta=v_q(R-h).
\tag{6}
\]

pure \(T\)-side 分派给出 \(q\nmid p^2-1\)，故 \(q\nmid2(p-1)\)。由 (5) 可得

\[
\boxed{v_q(pE_1+1)=\epsilon+\tau.}
\tag{7}
\]

若 \(q\mid E\)，actual maximal complete-excess 分型精确给出

\[
\tau=\delta,
\qquad \epsilon=\zeta-\delta.
\tag{8}
\]

代入 (7) 后得到更强的完整高度回收：

\[
\boxed{
q\mid E
\Longrightarrow
v_q(pE_1+1)=\zeta=v_q(R-h).}
\tag{9}
\]

所以此前的 \(q^\epsilon\mid pE_1+1\) 只是 (5) 中 \(E\) 的 q-primary 部分；
其余 \(q^\delta\) 来自 \(T\)。在 complete-excess 情形，checkpoint 端的总 q-height
恰是原始 \(z=R-h\) 的总 q-height，而不是新产生的高度。

若 \(q\nmid E\)，同样有

\[
v_q(pE_1+1)=\tau.
\tag{10}
\]

这也只读取现有 \(T\)-高度。

## 3. 因子复用型 adapter 的精确边界

等式 (5) 是一个可检验的阻断条件。若候选 terminal 或 lift 的唯一新增输入只是

\[
q^\epsilon\mid pE_1+1,
\tag{11}
\]

则 (5) 将其还原为已经给定的 \(q^\epsilon\mid E\)；在 pure \(T\)-side 上，剩余
q-height 也完全由 \(q^\tau\mid T\) 支付。故 (11) 不施加独立的 q-adic 条件，不能被
当作新的 owner、额外容量或严格势消耗重复登记。

这并不证明所有由 \(pE_1+1\) 触发的路径无效。一个有效的新 adapter 仍可能读取
其余因子 \(2(p-1)T\) 的具体除子、额外同余、checkpoint 的 terminal-first 分类、
persistent lineage 或全域 identity lift；只是它必须显式使用这些额外条件，不能仅把
(11) 重新命名为新的 q-primary source。

## 4. 聚焦复现

~~~bash
python3 reproductions/type_i_root_capacity_stutter_transverse_pure_t_complete_excess_relay.py --verify
~~~

该固定控制同时检查 (3)--(5)、(7)，并在 \(q\mid E\) 的控制上验证 (9)。控制只验证
q-primary normal form 和 checkpoint 整数恒等式，不冒充完整 actual root receipt，也不
扫描范围。
