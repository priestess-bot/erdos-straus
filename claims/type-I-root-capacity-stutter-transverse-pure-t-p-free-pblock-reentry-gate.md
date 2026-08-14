---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-pure-t-p-free-pblock-reentry-gate
title: 横向 pure-T excess 的 p-free p-block q-重入离散对数门
statement: >-
  对 actual L>1 low-gap negative-root pure-T-side complete-excess，令
  q=s(L+1)-1、Lp=1 mod q、epsilon=v_q(E)>0、delta=v_q(D)，并处于
  p-free suffix E=1+p^2 t。令 r_1=r+tT、F_1=2(p-1)r_1-1、
  lambda=v_p(F_1)、F_1=p^lambda u；p-block 剥离后的实际两侧为
  y=(p+1)u、x=1+(p^(lambda+1)-1)y。则 q 不整除 F_1 和 y，且
  x=L((L+1)L^lambda-1) mod q。因此 q|x 当且仅当 L^lambda=s mod q；
  若离散对数无解则 q 在该 p-block pair 两侧均不存在，若有解则 lambda 落在一个
  mod ord_q(L) 的类。又 v_q(K_1)=delta+epsilon，因此 q 只会在 x-side 形成新的
  complete-excess，当且仅当 v_q(x)>delta+epsilon；第一层离散对数命中本身不够。
  若真的越过该高度，则 p-free capacity identity 进一步强制
  v_q(p^(lambda+1)-p-1)=delta+epsilon，即 q^(delta+epsilon) 恰整除这个
  p-block capacity polynomial。
  更强地，actual cross-mod identity 强制任何 q|x 都有 t+m=0 mod p，等价于
  E=1-p^2m mod p^3。于是 q-entry 同时需要一个 q 的离散对数类和 actual multiplier 的
  特定 p-adic digit；但这个一阶门不能升格为 v_p(F_1)=v_p(t+m)：actual p=97
  p-free family 有 v_p(t+m)=2、v_p(F_1)=1 的严格控制。这是 p-free return 内 q 的
  精确 reentry capacity map，不构造 terminal、lift 或全局势。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-transverse-negative-branch-bezout-reflection-terminal
  - type-I-root-capacity-stutter-transverse-pure-t-complete-excess-relay
  - type-I-overflow-full-product-d-one-a-one-endpoint-s-zero-p-free-return
  - type-I-root-capacity-stutter-transverse-pure-t-p-free-root-expulsion
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
  - discrete-log
  - capacity-map
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-transverse-negative-branch-bezout-reflection-terminal
    role: low-gap-negative-root-L-data-and-pure-T-q-capacity
  - claim: type-I-root-capacity-stutter-transverse-pure-t-complete-excess-relay
    role: q-excess-height-and-T-side-synchronization
  - claim: type-I-overflow-full-product-d-one-a-one-endpoint-s-zero-p-free-return
    role: p-free-return-and-p-block-peeled-pair
  - claim: type-I-root-capacity-stutter-transverse-pure-t-p-free-root-expulsion
    role: q-capacity-retained-in-K-one-but-absent-from-root-anchor
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_pure_t_complete_excess_relay.py
    role: p-block-gate-miss-and-gate-hit-without-overcapacity-controls
visibility: public
last_checked: '2026-08-14'
---

# 横向 pure-\(T\) excess 的 \(p\)-free \(p\)-block \(q\)-重入离散对数门

## 1. 设置与 p-block pair

固定一个 actual \(L>1\) low-gap negative-root pure-\(T\)-side complete-excess
receipt。沿用

\[
q=s(L+1)-1,
\qquad
Lp\equiv1\pmod q,
\qquad
s\in\{3,7,11,23\},
\tag{1}
\]

以及

\[
2r\equiv L(L+1)\pmod q,
\qquad
q\mid T,
\qquad
\delta=v_q(D),
\qquad
\epsilon=v_q(E)>0.
\tag{2}
\]

考虑 p-free suffix

\[
E=1+p^2t,
\qquad
r_1=r+tT,
\qquad
F_1=2(p-1)r_1-1.
\tag{3}
\]

写

\[
\lambda=v_p(F_1),
\qquad
F_1=p^\lambda u,
\qquad
p\nmid u.
\tag{4}
\]

既有 p-free return 在 canonical anchor 剥尽完整 \(p^{\lambda+1}\) 后，给出一条
actual raw p-block path 到达的 pair

\[
y=(p+1)u,
\qquad
x=1+\bigl(p^{\lambda+1}-1\bigr)y.
\tag{5}
\]

同一 return 保持

\[
K_1=EK,
\qquad
v_q(K_1)=\delta+\epsilon.
\tag{6}
\]

这里的 \(\lambda\) 是 p-block 的高度；不要与 receipt quotient \(e\) 或
low-gap parameter \(L\) 混同。

## 2. \(q\) 在 p-block pair 中的唯一入口

由于 \(q\mid T\)，(3) 给出 \(r_1\equiv r\pmod q\)。再由
\(p\equiv L^{-1}\pmod q\) 和 (2)，有

\[
\begin{aligned}
F_1
&\equiv2(p-1)r-1\\
&\equiv(L^{-1}-1)L(L+1)-1\\
&\equiv-L^2\pmod q.
\end{aligned}
\tag{7}
\]

所以 \(q\nmid F_1\)。由 (4) 又有

\[
u\equiv-L^{\lambda+2}\pmod q.
\tag{8}
\]

注意 (1) 给出 \(s(L+1)\equiv1\pmod q\)，故 \(q\) 不整除 \(L+1\)。由 (5)、(8)
可得

\[
\boxed{
y\equiv-(L+1)L^{\lambda+1}\not\equiv0\pmod q,}
\tag{9}
\]

以及

\[
\begin{aligned}
x
&\equiv1+\bigl(L^{-(\lambda+1)}-1\bigr)
\bigl(-(L+1)L^{\lambda+1}\bigr)\\
&\equiv L\bigl((L+1)L^\lambda-1\bigr)\pmod q.
\end{aligned}
\tag{10}
\]

因为 \(L\) 为模 \(q\) 的单位，得到精确的 first-layer gate：

\[
\boxed{
q\mid x
\quad\Longleftrightarrow\quad
L^\lambda\equiv s\pmod q.}
\tag{11}
\]

若 \(s\notin\langle L\rangle\subset(\mathbb Z/q\mathbb Z)^\times\)，则这个 \(q\)
在整个 p-block pair 上没有出现。若 \(s\in\langle L\rangle\)，任取一个
\(\lambda_0\) 满足 \(L^{\lambda_0}\equiv s\)，则 (11) 等价于

\[
\lambda\equiv\lambda_0\pmod{\operatorname{ord}_q(L)}.
\tag{12}
\]

所以 p-free return 不把原 pure-\(T\) carrier 任意地送回 root-capacity：它只能经由
\(x\)-side 的一个明确 p-adic height class 重现；\(y\)-side 被 (9) 无条件排除。

## 3. actual \(p\)-adic digit 的额外入口门

现在使用 actual stutter 的 cross-mod identity。p-free 条件意味着
\(\sigma=pt\)。此前的 p-suffix 判据因此给出

\[
p\mid m+2r+1,
\qquad
2r\equiv-m-1\pmod p.
\tag{13}
\]

又 \(T\equiv-1/2\pmod p\)，所以由 (3) 有

\[
r_1\equiv r-\frac t2\pmod p.
\tag{14}
\]

将 (13)--(14) 代回 \(F_1=2(p-1)r_1-1\)，得到

\[
\boxed{F_1\equiv m+t\pmod p.}
\tag{15}
\]

若 (11) 命中，\(\lambda\) 不可能为零：否则它会要求
\(1=L^0\equiv s\pmod q\)，但 \(1<s<q\)。于是 \(q\mid x\) 强制
\(\lambda\ge1\)，由 (15) 得到额外的 actual p-adic 条件

\[
\boxed{
q\mid x
\Longrightarrow
t\equiv-m\pmod p
\Longleftrightarrow
E=1+p^2t\equiv1-p^2m\pmod {p^3}.}
\tag{16}
\]

这条门不来自 q-local CRT：它使用了 actual \(m+2r\) 的 p-suffix 以及 p-free
return 的 \(F_1\)。因此它是 pure-\(T\) q-entry 首次获得的 genuinely cross-mod
provenance 条件。

## 4. q-overcapacity 的精确 Hensel 饱和门

既有 p-free p-block capacity formula 精确给出

\[
\boxed{
(x,K_1)=\bigl(x,\ p^{\lambda+1}-p-1\bigr).}
\tag{17}
\]

记 \(k_q=\delta+\epsilon=v_q(K_1)\)。若 \(q\) 真正越过现有容量，即

\[
v_q(x)>k_q,
\tag{18}
\]

则 (17) 左端的 q-adic 阶为 \(k_q\)。右端的 q-adic 阶则为

\[
\min\!\left(v_q(x),\ v_q\!\left(p^{\lambda+1}-p-1\right)\right).
\]

由于第一项严格大于 \(k_q\)，两端相等强制

\[
\boxed{
v_q(x)>\delta+\epsilon
\Longrightarrow
v_q\!\left(p^{\lambda+1}-p-1\right)=\delta+\epsilon.}
\tag{19}
\]

换言之，新的 q-primary complete-excess 不仅要通过 first-layer 离散对数门 (11)，
还要使 p-block capacity polynomial 恰好达到已有的 q-capacity：

\[
q^{\delta+\epsilon}\parallel p^{\lambda+1}-p-1.
\tag{20}
\]

这是必要条件而非充分条件；即使 (20) 成立，仍须直接检查 \(v_q(x)\) 是否真的超过
\(\delta+\epsilon\)。

## 5. 一层命中并不等于新的 complete-excess

在 (5) 的实际 raw pair 上，完整超额定义直接给出：\(q\) 能作为新的 \(x\)-side
complete-excess block 的素因子，当且仅当

\[
\boxed{v_q(x)>v_q(K_1)=\delta+\epsilon.}
\tag{21}
\]

式 (9) 表明 \(q\) 不可能从 \(y\)-side 产生该 block；式 (11) 只决定
\(v_q(x)\ge1\)，并不控制 (21) 所需的高层高度。因此，任何把
\(L^\lambda\equiv s\pmod q\) 直接称作新的 q-primary payload、terminal 或势消耗的
论证都是不充分的。

## 6. 两个聚焦控制

脚本使用两个 q-primary/p-free 兼容控制。

* \((p,q,s,L,h,m,r,t)=(313,17,3,5,12,4,15,9)\) 有 \(\lambda=0\)，所以
  \(L^\lambda=1\ne s\)，并且 \(q\nmid x\)。
* \((433,11,3,3,30,10,6,13)\) 有 \(\lambda=1\) 且 \(L^\lambda=s\)，所以
  \(11\mid x\)；但精确值为
  \(v_{11}(x)=1<v_{11}(K_1)=2\)，且
  \(v_{11}(p^{\lambda+1}-p-1)=1<2\)，仍没有新的 complete-excess block。

两个控制都验证 low-gap negative-root、pure-\(T\) 同步、p-free 公式和 (7)--(12)，
但都明确不是完整 actual root receipt。第二个控制是第一层 gate 命中却不能升级为
overcapacity 的严格边界，而不是猜想反例。

脚本另从已有 \(p=97,h=58,D=331,m=4\) 的 actual p-free receipt 家族取
family index \(79\)。它直接重放 \(R-h=ED\)、\(D\mid K\)、
\(p\mid m+2r+1\)、\(v_p(F_1)=1\) 及
\(F_1\equiv t+m\equiv0\pmod p\)，从而核对 (15)--(16) 的 actual p-adic
部分；该控制不声称带有 low-gap \(q\)-carrier。

同一家族的 family index \(2213\) 保留全部 actual receipt 与 p-free identity，但有

\[
\boxed{v_{97}(t+m)=2,\qquad v_{97}(F_1)=1.}
\tag{22}
\]

所以 (15) 只能作为 first p-adic digit 门使用，不能错误加强为
\(v_p(F_1)=v_p(t+m)\)，更不能仅由 \(E\) 的高阶 p-adic digit 决定离散对数 gate
所需的完整 \(\lambda\)。这是一条来自 actual p-free family 的严格 counterexample，
而不是对 (16) 的反例。

## 7. 边界

这条离散对数门没有给出 \(\lambda\) 的统一上界，也没有证明 (21) 必命中或必失败；
现有 p-free return 还允许很长的 raw/capacity 轨道。因此它不是 Type I/II 证书、
identity lift 或 global potential。

它把下一步缩小为一个实际、单侧的 q-primary 问题：对于已通过 (11) 的 \(x\)-side，
能否将 \(v_q(x)>\delta+\epsilon\) 接到既有 Type I/II menu、可收费的 support upgrade，
或一个严格可提升的递降；而对于未通过 (11) 的状态，如何利用 q 在该 p-block pair
完全缺席这一事实限制后续 source/path provenance。

## 8. 聚焦复现

~~~bash
python3 reproductions/type_i_root_capacity_stutter_transverse_pure_t_complete_excess_relay.py --verify
~~~
