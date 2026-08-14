---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-pure-t-cross-mod-valuation-staircase
title: 横向 stutter 纯 T 侧的跨模 multiplier-quotient 赋值阶梯
statement: >-
  对 actual nonterminal proper-root stutter receipt，令
  D=mp+1-h、eD=ph+1、E=1+p sigma、T=p^2r-(p+1)/2，则恒有
  sigma D=2T-(m+2r)，以及 (p+e+sigma)D=(p^2-1)(m+2r)。由于 2<=h<p，
  sigma(1-h)=-(m+2r+1) mod p；于是 sigma=0、1、-1 mod p 分别精确等价于
  p|(m+2r+1)、p|(m+2r+2-h)、p|(m+2r+h)。若 q|D* 是 L>1 pure-T-side
  negative-root carrier，delta=v_q(D)，则
  v_q(m+2r)=delta+v_q(p+e+sigma)。若再有 q|E，则 v_q(T)=delta，故所有
  超过强制 q^delta 层的 m+2r 高度恰由 p+e+sigma 的 q-adic 赋值支付。
  这是把 multiplier/checkpoint p-suffix 与 actual receipt quotient 的下一 q 层连接的
  capacity map；它本身不构造 Type I/II 证书、identity lift 或全局出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-general-endpoint-divisor-gate
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
  - receipt-quotient
  - checkpoint-relay
  - p-adic
  - q-adic
  - valuations
  - provenance
  - proof-boundary
sources:
  - claim: type-I-root-capacity-general-endpoint-divisor-gate
    role: actual-stutter-R-D-E-e-identities
  - claim: type-I-root-capacity-stutter-transverse-pure-t-synchronization-boundary
    role: pure-T-forced-q-layer-and-normalized-receipt-identity
  - claim: type-I-root-capacity-stutter-transverse-pure-t-complete-excess-relay
    role: q-excess-implies-T-height-exactly-delta
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_pure_t_complete_excess_relay.py
    role: actual-stutter-cross-mod-identity-and-q-primary-controls
visibility: public
last_checked: '2026-08-14'
---

# 横向 stutter 纯 \(T\) 侧的跨模 multiplier-quotient 赋值阶梯

## 1. actual stutter 的 multiplier 消元

固定核心素数 \(p\equiv1\pmod {24}\) 的 actual nonterminal proper-root stutter
receipt。写

\[
D=mp+1-h,
\qquad eD=ph+1,
\qquad E=1+p\sigma,
\tag{1}
\]

以及

\[
T=p^2r-\frac{p+1}{2},
\qquad
R=2p^3r-p^2-2pr-p+1,
\qquad R-h=ED.
\tag{2}
\]

从 \(ED=R-h\) 中减去 \(D=mp+1-h\)，并使用 \(E-1=p\sigma\)，得到

\[
\begin{aligned}
p\sigma D
&=R-mp-1\\
&=p\bigl(2p^2r-p-2r-1-m\bigr).
\end{aligned}
\]

故有第一条精确整数恒等式

\[
\boxed{\sigma D=2T-(m+2r).}
\tag{3}
\]

另一方面，actual stutter 还有

\[
2T=p^2(m+2r)-(p+e)D.
\tag{4}
\]

将 (3) 代入 (4)，消去 \(T\)，得到第二条更适合赋值的恒等式

\[
\boxed{(p+e+\sigma)D=(p^2-1)(m+2r).}
\tag{5}
\]

式 (3)--(5) 不是抽象 divisor gate：它们同时使用了 actual \(R-h=ED\)、
actual \(eD=ph+1\) 与 nonterminal multiplier 参数 \(\sigma\)。

## 2. checkpoint \(p\)-suffix 的 actual 判据

proper-root 条件 \(2\le h<p\) 使 \(1-h\) 成为模 \(p\) 的单位。将 (3) 模 \(p\)
化简，得到

\[
\boxed{\sigma(1-h)\equiv-(m+2r+1)\pmod p.}
\tag{6}
\]

所以 \(\sigma\bmod p\) 不再只是一个未经来源约束的 checkpoint 标签；它由 actual
\(m+2r\) 与 root height \(h\) 唯一确定。特别地，canonical checkpoint 的三条
non-strict suffix 分别等价于

\[
\boxed{
\begin{aligned}
\sigma\equiv0\pmod p
&\Longleftrightarrow p\mid m+2r+1,\\
\sigma\equiv1\pmod p
&\Longleftrightarrow p\mid m+2r+2-h,\\
\sigma\equiv-1\pmod p
&\Longleftrightarrow p\mid m+2r+h.
\end{aligned}}
\tag{7}
\]

其余剩余类才进入 strict carry 行。与 CRT 边界并不矛盾：CRT 说明 q-local data
本身不能限制这些 p 条件；(6) 指出真正需要读取的跨模 actual 数据正是
\(m+2r\) 的 \(p\)-剩余。

## 3. pure \(T\)-side 的下一 q 层

现在取一个 \(L>1\) low-gap negative-root pure \(T\)-side carrier

\[
q\mid D_*,
\qquad \delta=v_q(D).
\tag{8}
\]

已有分派给出 \(q\nmid p^2-1\)，且强制 \(q^\delta\mid m+2r\)。因此由 (5)
逐赋值得

\[
\boxed{
v_q(m+2r)=\delta+v_q(p+e+\sigma).}
\tag{9}
\]

等价地，定义

\[
\widehat D=\frac{D}{q^\delta},
\qquad
\widehat M=\frac{m+2r}{q^\delta},
\tag{10}
\]

则

\[
\boxed{(p+e+\sigma)\widehat D=(p^2-1)\widehat M.}
\tag{11}
\]

所以 \(\widehat M\) 的每一个额外 q-primary 层恰由 actual receipt quantity
\(p+e+\sigma\) 检测，而不是由已经塌缩的 \(T/u\) 与 \(m+2r\) 双重整除重新计数。

若进一步 \(q\mid E\)，此前 complete-excess 分型给出

\[
v_q(T)=\delta.
\tag{12}
\]

故 (9) 将 pure \(T\)-side 的完整层图精确分成：\(T\) 停在被 \(D\) 强制的
\(q^\delta\) 层，而 \(m+2r\) 的任何额外层完全由 \(p+e+\sigma\) 记录。

## 4. 边界与下一输入

式 (6) 与 (9) 产生 actual cross-mod capacity map，但尚未证明 (7) 的任意一条
bad suffix 必然触发 terminal，也没有排除它们。它也不保证
\(p+e+\sigma\) 在 \(q\) 上非零或必有额外高度。

下一条有希望的 adapter 必须把 (7) 的三个明确 \(p\)-整除条件，或 (9) 的
\(p+e+\sigma\) q-adic 阶梯，接到已有 Type I/II terminal menu 或带 identity lift
的严格边；不能再只使用 \(q\mid E\)、\(q\mid D_*\) 或 \(pE_1+1\) 的因子继承。

## 5. 聚焦复现

~~~bash
python3 reproductions/type_i_root_capacity_stutter_transverse_pure_t_complete_excess_relay.py --verify
~~~

脚本保留 pure \(T\) q-primary 控制，并额外重放固定的 actual stutter receipt
\((p,r,h,m,D,e,\sigma)=(97,6618,58,4,331,17,376206)\)，逐项检查
\(R-h=ED\)、\(eD=ph+1\)、(3)、(5)、(6) 与 capacity receipt 条件。它不做范围扫描。
