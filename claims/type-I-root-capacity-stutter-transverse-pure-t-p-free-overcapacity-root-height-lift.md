---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-pure-t-p-free-overcapacity-root-height-lift
title: 横向 pure-T p-free p-block q-过容量的实际根高度 Hensel 桥
statement: >-
  对 actual L>1 low-gap negative-root pure-T-side complete-excess，令
  delta=v_q(D)>0、epsilon=v_q(E)>0、E=1+p^2t、eD=ph+1，及 p-block
  数据 lambda=v_p(F_1)、P_lambda=p^(lambda+1)-p-1、K_1=EK。若互补侧
  x 真有 q-过容量 v_q(x)>delta+epsilon，则 v_q(P_lambda)=delta+epsilon，且
  q^delta 恰整除 p^lambda+h-1。更精确地，令 D_hat=D/q^delta，则
  (p^lambda+h-1)/q^delta = e p^(-1) D_hat mod q^epsilon；并有
  q^delta|(p^(lambda-1)+m) 及
  (p^(lambda-1)+m)/q^delta = (p+e)p^(-2)D_hat mod q^epsilon。
  再由 2T-P_lambda=p^2(2r-p^(lambda-1))，可得 q^delta 恰整除 2r-p^(lambda-1)，且其
  q^delta 单位商等于 (pE+e)D_hat/(p^2(p^2-1)) mod q^epsilon。若 h=3u 是
  canonical root endpoint、2r+1=uw，则这给出 u 与 w 的两条精确 q-adic
  Hensel 约束。
  因而 overcapacity 不只是 p-block capacity polynomial 的 Hensel 条件：它强制
  p^lambda 在 actual root height h 的 q^delta 层精确命中、在下一 q 层必失败，
  同时给出 m/e/D 的高层残数；其中 r 坐标是 T 与 p-block 容量的依赖投影，不能
  单独计作新的 local exclusion。这是一个必要 capacity/provenance map，不构造
  Type I/II terminal、identity lift 或全局势。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-transverse-pure-t-complete-excess-relay
  - type-I-root-capacity-stutter-transverse-pure-t-p-free-pblock-reentry-gate
  - type-I-overflow-full-product-d-one-a-one-endpoint-s-zero-p-free-return
topics:
  - type-I
  - root-capacity
  - stutter
  - transverse-residual
  - negative-branch
  - pure-T-side
  - complete-excess
  - p-free-return
  - p-adic
  - q-adic
  - Hensel-lifting
  - root-height
  - capacity-map
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-transverse-pure-t-complete-excess-relay
    role: q-excess-implies-e-is-a-q-unit-and-vq-ph-plus-one-equals-delta
  - claim: type-I-root-capacity-stutter-transverse-pure-t-p-free-pblock-reentry-gate
    role: overcapacity-forces-exact-p-block-capacity-polynomial-height
  - claim: type-I-overflow-full-product-d-one-a-one-endpoint-s-zero-p-free-return
    role: p-free-p-block-pair-and-exact-gcd-capacity-identity
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_pure_t_complete_excess_relay.py
    role: synthetic-high-overcapacity-root-height-control
visibility: public
last_checked: '2026-08-14'
---

# 横向 pure-\(T\) p-free p-block \(q\)-过容量的实际根高度 Hensel 桥

## 1. 设置

固定一个 actual \(L>1\) low-gap negative-root pure-\(T\)-side
complete-excess receipt。沿用

\[
D=mp+1-h,
\qquad eD=ph+1,
\qquad
\delta=v_q(D)>0,
\qquad \epsilon=v_q(E)>0.
\tag{1}
\]

complete-excess relay 给出 \(q\nmid e\)，故

\[
v_q(eD)=v_q(ph+1)=\delta.
\tag{2}
\]

再取 p-free suffix

\[
E=1+p^2t.
\tag{3}
\]

令 p-block 剥离后的数据为

\[
\lambda=v_p(F_1),
\qquad
P_\lambda=p^{\lambda+1}-p-1,
\qquad
K_1=EK.
\tag{4}
\]

此前的 p-free capacity identity 给出

\[
(x,K_1)=(x,P_\lambda),
\qquad v_q(K_1)=\delta+\epsilon.
\tag{5}
\]

以下只讨论真正越过当前 q-capacity 的分支：

\[
v_q(x)>\delta+\epsilon.
\tag{6}
\]

这不是 first-layer discrete-log 命中；它是 q-primary 的 complete-excess
重新出现。特别地，(6) 蕴含 \(q\mid x\)。既有 discrete-log gate 遂给出
\(L^\lambda\equiv s\pmod q\)，而 \(s\ne1\)，所以

\[
\lambda\ge1.
\tag{6a}
\]

因此下文的 \(p^{\lambda-1}\) 始终是整数。

## 2. 过容量首先固定 p-block polynomial 的精确高度

由 (5)--(6)，左侧 gcd 的 q-赋值恰为 \(\delta+\epsilon\)。因为 \(x\) 的
赋值严格更大，右侧 gcd 只能在 \(P_\lambda\) 上于该层停止。因此

\[
\boxed{v_q(P_\lambda)=\delta+\epsilon.}
\tag{7}
\]

记 \(k=\delta+\epsilon\)。因 \(q\nmid p\)，(7) 等价于完整的
\(q\)-进离散对数 lift

\[
\boxed{
p^\lambda\equiv1+p^{-1}\pmod {q^k},
\qquad
p^\lambda\not\equiv1+p^{-1}\pmod {q^{k+1}}.}
\tag{7a}
\]

这里的逆元在相应的 \(q\)-进模数中理解；它直接来自

\[
P_\lambda=p\bigl(p^\lambda-(1+p^{-1})\bigr).
\]

模 \(q\) 时，\(p\equiv L^{-1}\) 及 \(s(L+1)\equiv1\) 给出

\[
p^\lambda\equiv1+p^{-1}
\quad\Longleftrightarrow\quad
L^\lambda\equiv s\pmod q.
\]

所以既有 gate 正是 (7a) 的 first layer；真正 overcapacity 还要求它 lift 到
\(q^k\) 而不 lift 到下一层。特别地，若
\(1+p^{-1}\notin\langle p\rangle\subset(\mathbb Z/q^k\mathbb Z)^\times\)，
该分支为空；否则 \(\lambda\) 落在模
\(\operatorname{ord}_{q^k}(p)\) 的唯一剩余类中，并仍须满足 (7a) 的 exact
non-lift 条件。下面的重点是：(7) 与 actual root receipt 并不独立。

## 3. 根高度的精确 Hensel 层

由 (1) 和 (4) 有恒等式

\[
\begin{aligned}
p\bigl(p^\lambda+h-1\bigr)
&=p^{\lambda+1}+ph-p\\
&=\bigl(p^{\lambda+1}-p-1\bigr)+(ph+1)\\
&=P_\lambda+eD.
\end{aligned}
\tag{8}
\]

右侧两项的 q-赋值分别为 \(\delta+\epsilon\) 与 \(\delta\)。它们不相等，且
\(q\nmid p\)，所以 (8) 给出

\[
\boxed{v_q\bigl(p^\lambda+h-1\bigr)=\delta.}
\tag{9}
\]

等价地，过容量强制 root-height signature

\[
\boxed{
p^\lambda\equiv1-h\pmod {q^\delta},
\qquad
p^\lambda\not\equiv1-h\pmod {q^{\delta+1}}.}
\tag{10}
\]

令 \(\widehat D=D/q^\delta\)。将 (8) 除以 \(p q^\delta\)，再使用 (7)，得到
更强的单位商关系

\[
\boxed{
\frac{p^\lambda+h-1}{q^\delta}
\equiv e p^{-1}\widehat D
\pmod {q^\epsilon}.}
\tag{11}
\]

这里的逆元均在 \(\mathbb Z/q^\epsilon\mathbb Z\) 中理解。故 \(h\) 不是仅在
mod \(q\) 上携带负根角色；其 \(q^\delta\) lift 的首个非零单位商被 actual
receipt quotient \(e\) 固定。

## 4. \(m\) 与 \(r\) 坐标的同一高层桥

由 \(h=mp+1-D\)，(8) 还可改写为

\[
\boxed{
p^2\bigl(p^{\lambda-1}+m\bigr)=P_\lambda+(p+e)D.}
\tag{12}
\]

先模 \(q^\delta\) 化简，得到

\[
q^\delta\mid p^{\lambda-1}+m.
\tag{13}
\]

将 (12) 除以 \(q^\delta\)，并再次使用 \(q^\epsilon\mid P_\lambda/q^\delta\)，
得到精确 residual congruence

\[
\boxed{
\frac{p^{\lambda-1}+m}{q^\delta}
\equiv (p+e)p^{-2}\widehat D
\pmod {q^\epsilon}.}
\tag{14}
\]

式 (11)、(14) 是同一 overcapacity 事件在 root-height 与 gap/receipt 坐标中的
两张高层投影。它们不是可任意指定的 q-local CRT 标签。

还可把 \(r\) 本身写到同一 q-adic 层，但这不是另一个独立的 q-local gate。由
\(T=p^2r-(p+1)/2\) 及 \(P_\lambda=p^{\lambda+1}-p-1\)，有精确恒等式

\[
\boxed{2T-P_\lambda=p^2\bigl(2r-p^{\lambda-1}\bigr).}
\tag{15}
\]

pure-\(T\) complete-excess relay 给出 \(v_q(T)=\delta\)，而 (7) 给出
\(v_q(P_\lambda)=\delta+\epsilon\)。将 (15) 除以 \(p^2q^\delta\)，并用
\(D(pE+e)=2(p^2-1)T\)，得到

\[
\begin{aligned}
\frac{2r-p^{\lambda-1}}{q^\delta}
&\equiv2p^{-2}\frac{T}{q^\delta}\\
&\equiv
\frac{(pE+e)\widehat D}{p^2(p^2-1)}
\pmod {q^\epsilon}.
\end{aligned}
\tag{16}
\]

故 (16) 的右侧是 q-单位，得到第三条 exact signature：

\[
\boxed{v_q\bigl(2r-p^{\lambda-1}\bigr)=\delta.}
\tag{17}
\]

用 actual cross-mod identity 与 (14) 相减也会得到同一 (16)，但 (15) 表明其
来源已完全被 \(T\) 的既有 \(q^\delta\) 容量和 \(P_\lambda\) 的 \(q^k\) Hensel
条件决定。因此 (17) 是把这两个输入投影到 actual \(r\) 坐标的精确记录，不应被
重复计作独立排除条件。

## 5. Canonical root realization filter

若该 receipt 还来自 canonical root-capacity endpoint，则

\[
u=\gcd\!\left(2r+1,\frac{p^2+p+1}{3}\right),
\qquad h=3u,
\qquad 2r+1=uw.
\tag{18}
\]

式 (10) 与 (17) 遂给出两条同时必须成立的 divisor-coordinate Hensel 条件：

\[
\boxed{
\begin{aligned}
3u&\equiv1-p^\lambda\pmod {q^\delta},
&3u&\not\equiv1-p^\lambda\pmod {q^{\delta+1}},\\
uw&\equiv1+p^{\lambda-1}\pmod {q^\delta},
&uw&\not\equiv1+p^{\lambda-1}\pmod {q^{\delta+1}}.
\end{aligned}}
\tag{19}
\]

这里 \(u\) 是 \((p^2+p+1)/3\) 的实际除子，而不是可自由选择的 local root
residue；\(w\) 还须满足 \(u=\gcd(2r+1,(p^2+p+1)/3)\)。因此 (19) 是将
p-block overcapacity 写成 canonical root coordinates 的 exact capacity map。
它不是额外独立的 q-local no-go：第一行的 mod-\(q\) 部分已与 low-gap negative root
一致，第二行则是 (15) 的坐标重写。其价值在于后续若使用 actual divisor/quotient
structure 或构造 strict descent，必须处理这两条 non-lift 条件，而不能只检查
q 的 first-layer discrete log。

## 6. 局部兼容边界

不能把 (7) 单独解释为与核心素数或局部 stutter 方程矛盾。取如下合成控制：

\[
\begin{gathered}
p=1489,\qquad q=11,\qquad s=L=3,\\
m=373,\qquad h=745,\qquad D=554653,\qquad e=2,\\
r=1594864619896145076,\qquad
t=8563019934725181,\qquad E=1+p^2t.
\end{gathered}
\tag{20}
\]

它满足低缺口负根的全部 q-local 关系、\(D=mp+1-h\)、\(eD=ph+1\)、
\(R-h=ED\)、p-free stutter 的两条 actual 整数恒等式及 p-block gcd capacity
identity。并且

\[
\delta=\epsilon=1,
\qquad
\lambda=1,
\qquad
v_{11}(K_1)=2,
\qquad
v_{11}(x)=3,
\qquad
v_{11}(P_\lambda)=2,
\tag{21}
\]

而 (9)、(11)、(14) 分别给出

\[
v_{11}(p^\lambda+h-1)=1,
\qquad
\frac{p^\lambda+h-1}{11}\equiv5\pmod {11},
\qquad
\frac{p^{\lambda-1}+m}{11}\equiv1\pmod {11}.
\tag{22}
\]

并且 (17) 给出

\[
v_{11}(2r-p^{\lambda-1})=1,
\qquad
\frac{2r-p^{\lambda-1}}{11}\equiv1\pmod {11}.
\tag{23}
\]

不过它**不是** canonical root-capacity endpoint：

\[
\gcd\!\left(2r+1,\frac{p^2+p+1}{3}\right)=1,
\qquad h\ne3,
\qquad h\nmid p^2+p+1.
\tag{24}
\]

所以该控制不是 actual endpoint receipt，更不是 Erdős--Straus 反例。它严格说明：
若要排除 high overcapacity，不能只用本卡消耗的局部 p-free、q-primary 与 receipt
代数；必须额外使用 canonical root realization、raw path provenance 或一个新的
terminal/lift adapter。

## 7. 对全局出口目标的意义

该引理将 p-block high-capacity branch 的真正强化固定为 (7a) 的
\(q^{\delta+\epsilon}\)-进离散对数 non-lift，并把它投影到 actual root-height、gap
和 canonical divisor coordinates。后续可尝试把 (7a)、(10) 或 (14) 与
\(h=3\gcd(2r+1,M)\)、\(D\mid K\) 的实际实现性联立，证明它们触发已有 Type I/II
terminal，或构造满足 E1--E5 的严格递降。当前它只是一张必要容量/来源图：没有
terminal、没有全域解提升，也没有全局势下降。

## 8. 聚焦复现

~~~bash
python3 reproductions/type_i_root_capacity_stutter_transverse_pure_t_complete_excess_relay.py --verify
~~~

该 verifier 重放 (20)--(24) 的局部高过容量控制，逐项检查 (7)、(7a)、(9)、(11)、(14)、(17)，
并显式检查其不满足 canonical root endpoint 条件。
