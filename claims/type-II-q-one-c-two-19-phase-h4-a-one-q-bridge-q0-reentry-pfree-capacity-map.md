---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-pfree-capacity-map
title: H4 clean q-bridge 的 q0 p-free re-entry 完整超额容量图与 unitary q-lock 签名
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity a_alt=1 clean
  q bridge 中，设 q0=q/gamma>1、s=q0t、F=gamma+pt，且从 q-word 的 x-side
  实际剥离 q0 到 primitive p-free re-entry (xi,zeta)=(x_q/q0,R4-x_q/q0)。若
  Q_xi,Q_zeta 是相对 K4 的 maximal complete-excess blocks，令
  E_zeta=Q_zeta/gcd(M4,Q_zeta)（Q_zeta=1 时取 E_zeta=1），则
  Q_xi=Q_x/q0、E_xi=F；两块皆空恰为 Type I terminal，恰有一块非空时所选侧的
  single-side residual-divisibility gate 自动成立。否则 canonical support multiplier
  是 L_re=F E_zeta，且 c_re=-L0(F E_zeta)^(-1) (mod p)。因此
  c_re=p-1 恰当且仅当 E_zeta=L0 gamma^(-1) (mod p)。在此顶容量情形写
  F E_zeta=L0+p sigma，则 target 再次为 full-product d=1 行，
  n_re=n+4M4 sigma，且 a_re=q/gcd(q,sigma)。唯一不能算术进入既有 a>1 handoff
  的情形是 q|sigma；它等价于 q|xi zeta。令 D=gcd(M4,Q_x) beta_x、
  rho=gcd(q,xi)，则 q-lock 恰给出一个唯一 unitary divisor rho||q，并满足
  t=gamma (mod rho)、t=gamma-2dD^(-1) (mod q/rho)。反之每个这样的 unitary
  split 恰恢复 q-lock。写 M4=dU、sigma=qv，则 q-lock full-product target 的参数为
  b_re=b+2Uv；在 target 通过既有准入后，d=1 p-adic countdown 只在首个非零数字
  omega_re=-1 且其根容量 u 满足 9u^2>=p 时不由已知路由给出 terminal/strict macro。
  该结论不自动通过 typed、single-side 或 atomic adapter 的持久化 guards，也不排除
  这个最终 q-lock/root residual。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-p-primary-exclusion
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-stutter-a-coordinate-transduction
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-complete-excess-stutter-reduction
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
  - type-I-overflow-full-product-d-one-a-one-regeneration-return-digit-normal-form
  - type-I-overflow-full-product-d-one-a-one-root-coprime-capacity-fan-half-descent
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-d-residue-gate
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-nonminimal-d-lift-finite-phase-exclusion
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - a-one
  - fresh-carrier
  - raw-path
  - q0-reentry
  - p-free
  - complete-excess-bundle
  - capacity-transduction
  - unitary-divisor
  - q-lock
  - source-provenance
  - well-founded-rank
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-p-primary-exclusion
    role: actual-p-free-reentry-and-D-normal-form
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-stutter-a-coordinate-transduction
    role: q0-reentry-and-original-full-product-coordinate
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-complete-excess-stutter-reduction
    role: complete-excess-capacity-convention
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: clean-q-and-primitive-q-word
  - claim: type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
    role: original-d-one-top-capacity-and-a-greater-than-one-handoff
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: terminal-priority-and-single-side-bundle-contract
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: atomic-payload-and-conditional-E1-to-E5-contract
  - claim: type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
    role: d-one-regeneration-and-well-founded-countdown
  - claim: type-I-overflow-full-product-d-one-a-one-regeneration-return-digit-normal-form
    role: a-one-terminal-digit-classification-and-raw-source-repair
  - claim: type-I-overflow-full-product-d-one-a-one-root-coprime-capacity-fan-half-descent
    role: admitted-p-free-root-small-fan-terminal-or-strict-exit
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-d-residue-gate
    role: actual-H4-provenance-aware-D-divisor-gate
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-nonminimal-d-lift-finite-phase-exclusion
    role: nonminimal-lift-exclusion-and-minimal-D-phase-ray-map
  - concept: denominator-escape-state-contract
    role: terminal-typed-lift-and-potential-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_pfree_capacity_map.py
    role: exact-capacity-map-and-unitary-q-lock-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 clean \(q\)-bridge 的 \(q_0\) p-free re-entry 容量图

## 1. 范围与记号

保留 actual \(q=1\) high \(C=2\) 19-phase H4 proper-overlap top-capacity
\(a_{\rm alt}=1\) clean \(q\)-bridge 的记号。令

\[
w=\frac{p+1}{2}=qd,
\qquad
h=2d,
\qquad
(q,K_4)=(q,M_4)=1,
\tag{1}
\]

其中 \(h=2d\) 是 actual H4 carry 的结论。设唯一 q-bridge stutter 满足

\[
E_x=\frac{Q_x}{(M_4,Q_x)}=q_0F,
\qquad
q_0=\frac q\gamma>1,
\qquad
F=\gamma+pt,
\tag{2}
\]

其中 \(\gamma=(q,b+1)\)、\(s=q_0t\)。此前已实际到达 primitive raw word

\[
(x_q,y_q)\rightsquigarrow
(\xi,\zeta):=
\left(\frac{x_q}{q_0},R_4-\frac{x_q}{q_0}\right).
\tag{3}
\]

由前一张 p-primary 排除卡，\(p\nmid\xi\zeta\)。本卡只在这个已经 p-free 的
re-entry 上重新计算 complete-excess blocks 和 canonical capacity；不把它当作自动
accepted 的 Type I action。

令

\[
\xi=Q_\xi\beta_\xi,
\qquad
\zeta=Q_\zeta\beta_\zeta
\tag{4}
\]

为相对 \(K_4\) 的 maximal complete-excess 分解，并置

\[
E_\xi=\frac{Q_\xi}{(M_4,Q_\xi)},
\qquad
E_\zeta=\frac{Q_\zeta}{(M_4,Q_\zeta)}.
\tag{5}
\]

若相应 \(Q\) 为 \(1\)，约定其 \(E\) 也为 \(1\)。原 H4 top-capacity support
仍记为

\[
M_{\rm alt}=M_4L_0=\frac{pn-1}{4},
\qquad n=(p+1)b-1.
\tag{6}
\]

## 2. \(q_0\) 剥离后的精确 block

### 引理 1

\[
\boxed{
Q_\xi=\frac{Q_x}{q_0},
\qquad
\beta_\xi=\beta_x,
\qquad
E_\xi=F.
}
\tag{7}
\]

**证明。** \(q_0\mid Q_x\)，而 \(q_0\) 的每个素因子在 \(K_4\) 中的指数为零。
从 \(x_q=Q_x\beta_x\) 除去 \(q_0\) 因而只从相应的完整超额块移去这些素因子的
指定指数；其余素因子的 maximal complete-excess 判据不变。逐素数得到前两式。

又 \((q_0,M_4)=1\)，所以

\[
(M_4,Q_x/q_0)=(M_4,Q_x).
\]

将 (2) 代入即得第三式。\(\square\)

注意 (7) 不假定 \((q_0,F)=1\)：若同一素数在 \(F\) 中仍有剩余幂，它仍是
\(Q_\xi\) 的完整超额部分。

## 3. p-free terminal 与 canonical capacity

因为 \((x_q,y_q)=1\)，也有

\[
(\xi,\zeta)=(\xi,R_4)=1.
\tag{8}
\]

所以 \((Q_\xi,Q_\zeta)=1\)。两块皆空当且仅当 \(\xi\mid K_4\) 且
\(\zeta\mid K_4\)，这正是 terminal-first 的 Type I terminal。以下假设至少一块
非空。

由 (8) 的互素性，lcm 合并没有跨 endpoint 的重复计价：

\[
\begin{aligned}
L_{\rm re}
&:=\frac{\operatorname{lcm}(M_4,Q_\xi,Q_\zeta)}{M_4}\\
&=E_\xi E_\zeta
=\boxed{F E_\zeta}.
\end{aligned}
\tag{9}
\]

这里包含单侧与双色两种算术 support；后者是否构成 persistent atomic action 仍由独立
adapter 决定。

### 引理 2（单侧 residual gate 自动通过）

若恰有一块非空，则相应的 single-side complete-excess residual-divisibility gate
自动成立：

\[
\boxed{
Q_\xi=1<Q_\zeta\Longrightarrow \xi\beta_\zeta\mid K_4,
\qquad
Q_\zeta=1<Q_\xi\Longrightarrow \zeta\beta_\xi\mid K_4.
}
\tag{9a}
\]

**证明。** 第一种情形中 \(Q_\xi=1\) 给 \(\xi\mid K_4\)，而
\(\beta_\zeta\mid K_4\)。由 (8)，\((\xi,\beta_\zeta)=1\)，故乘积仍整除
\(K_4\)。第二种情形交换两侧即可。\(\square\)

因此 single-side branch 不再有独立的算术 residual gate；仍须独立重放
terminal-first、typed、source/path、serializer 和 persistent guards。只有
\(Q_\xi,Q_\zeta>1\) 才需要双色 atomic adapter。

p-free 保证 (9) 的 multiplier 在模 \(p\) 下可逆。原 top-capacity
同余 \(c_4L_0^{-1}\equiv-1\pmod p\) 因而给出

\[
\boxed{
c_{\rm re}\equiv-L_0(FE_\zeta)^{-1}\pmod p.
}
\tag{10}
\]

特别地，canonical representative 满足

\[
\boxed{
c_{\rm re}=p-1
\quad\Longleftrightarrow\quad
FE_\zeta\equiv L_0\pmod p
\quad\Longleftrightarrow\quad
E_\zeta\equiv L_0\gamma^{-1}\pmod p.
}
\tag{11}
\]

最后一个等价使用 \(F\equiv\gamma\not\equiv0\pmod p\)。故 (11) 以外的每个
nonterminal p-free re-entry 都有严格的**算术**容量 \(c_{\rm re}\le p-2\)；它只在
既有 terminal-first、typed 和 payload guards 成功时才可成为 strict macro。

## 4. 顶容量 re-entry 的 \(a\)-coordinate

现在设 (11) 成立，并唯一写成带符号的整数等式

\[
FE_\zeta=L_0+p\sigma.
\tag{12}
\]

由 (6)、(9) 有

\[
M_{\rm re}=M_4FE_\zeta
=M_{\rm alt}+pM_4\sigma
=\frac{p(n+4M_4\sigma)-1}{4}.
\tag{13}
\]

所以它再次落在 full-product \(d=1\) 行，且

\[
\boxed{n_{\rm re}=n+4M_4\sigma.}
\tag{14}
\]

写 \(M_4=dU\)。clean-q 给 \((q,U)=1\)，且 \(q\) 为奇数。对该行的坐标
\(a(r)=w/(w,(r+1)/2)\)，由 (6) 与 (14) 得

\[
\begin{aligned}
a_{\rm re}
&=\frac{qd}{\bigl(qd,d(qb+2U\sigma)\bigr)}\\
&=\boxed{\frac q{(q,\sigma)}}.
\end{aligned}
\tag{15}
\]

因此 \(q\nmid\sigma\) 时 \(a_{\rm re}>1\)，可在 target 重新分类和全部持久化
guards 通过后接入已有 \(a>1\) strict handoff。剩余的纯算术阻碍恰为

\[
\boxed{q\mid\sigma.}
\tag{16}
\]

## 5. \(q\)-lock 的 unitary 签名

原 clean bridge 有 \(q\mid Q\) 且 \((q,M_4)=1\)，故 \(q\mid L_0\)。又
\(p\equiv-1\pmod q\)。把 (12) 模 \(q\) 约化，得到

\[
\boxed{
q\mid\sigma
\quad\Longleftrightarrow\quad
q\mid FE_\zeta.
}
\tag{17}
\]

对任意 \(\ell\mid q\)，\(\ell\nmid K_4M_4\)。因此 (4)--(5) 在 \(q\)-部分
没有隐藏在 \(\beta\) 或 gcd 中的指数，故

\[
q\mid FE_\zeta
\quad\Longleftrightarrow\quad
q\mid\xi\zeta.
\tag{18}
\]

令

\[
D=(M_4,Q_x)\beta_x.
\tag{19}
\]

已有 actual re-entry normal form 给 \(D\mid K_4\)、\((D,q)=1\)、
\(\xi=FD\)。另外 q-word 恒等式给 \(R_4\equiv h=2d\pmod q\)。所以 (17)--(18)
等价于精确 root 条件

\[
\boxed{
q\mid(\gamma-t)D\,[2d-(\gamma-t)D].
}
\tag{20}
\]

这在 composite \(q\) 时不是“二选一”：不同素数幂可以分配到两个 endpoint。正确的
有限签名如下。

### 引理 3（unitary \(q\)-lock 签名）

在 (16) 下，令 \(\rho=(q,\xi)\)。则

\[
\boxed{
\rho\parallel q,
\qquad
t\equiv\gamma\pmod\rho,
\qquad
t\equiv\gamma-2dD^{-1}\pmod{q/\rho}.
}
\tag{21}
\]

反过来，任一 unitary divisor \(\rho\parallel q\) 满足 (21) 时，(16) 成立。

**证明。** 由 (8)，\(\xi\) 与 \(\zeta\) 互素。若 \(q\mid\xi\zeta\)，则对
\(q\) 的每个完整素数幂，它必须完整地落在恰一个 endpoint；因而
\(\rho=(q,\xi)\) 是 unitary divisor，且 \(q/\rho\mid\zeta\)。由
\(\xi\equiv(\gamma-t)D\) 与
\(\zeta\equiv2d-(\gamma-t)D\pmod q\)，再使用 \(D\) 在模 \(q\) 下可逆，
立即得到 (21)。反向乘回 \(\rho\mid\xi\)、\(q/\rho\mid\zeta\)，得
\(q\mid\xi\zeta\)，再由 (17)--(18) 得 (16)。\(\square\)

若 \(q\) 是素数，(21) 退化为两条根：\(t\equiv\gamma\pmod q\) 或
\(t\equiv\gamma-2dD^{-1}\pmod q\)。一般 \(q\) 只有
\(2^{\omega(q)}\) 种 unitary 分配，而不是一个未标记的容量回路。

## 6. q-lock 到 \(a=1\) 根扇的 relay

q-lock 并不意味着新的 full-product \(a=1\) 行必然静止。现在设 (16) 成立，写

\[
\sigma=qv,
\qquad M_4=dU.
\tag{23}
\]

由 (6)、(14) 与 \(p+1=2qd\)，re-entry target 的 \(a=1\) 参数是

\[
\begin{aligned}
b_{\rm re}
&=\frac{n_{\rm re}+1}{p+1}\\
&=\frac{(p+1)b+4dUqv}{2qd}
=\boxed{b+2Uv}.
\end{aligned}
\tag{24}
\]

当该 re-entry support 被重新分类为合法的正 full-product target 时，\(b_{\rm re}\)
仍为正奇数。令这个 full-product \(d=1\) 行的 ordinary complete-excess multiplier 为

\[
F_{\rm re}=(p-1)b_{\rm re}-1,
\qquad
\eta_{\rm re}=\nu_p(F_{\rm re}-1),
\qquad
\omega_{\rm re}\equiv
\frac{F_{\rm re}-1}{p^{\eta_{\rm re}}}\pmod p.
\tag{25}
\]

### 命题 4（q-lock root-fan relay）

若 (13) 的 canonical target 与随后每个 d=1 checkpoint 都通过既有的
terminal-first、typed、source/path、serializer 与 persistent guards，则：

\[
\boxed{
\omega_{\rm re}\not\equiv-1\pmod p
\Longrightarrow
\text{已有 d=1 countdown/source-repair 给出 strict macro};
}
\tag{26}
\]

若 \(\omega_{\rm re}\equiv-1\pmod p\)，经过恰 \(\eta_{\rm re}\) 次 canonical
regeneration 后到达 p-free root return，唯一写成

\[
b_\ast=2pr-1,
\qquad
u=\left(2r+1,\frac{p^2+p+1}{3}\right).
\tag{27}
\]

并且

\[
\boxed{
9u^2<p
\Longrightarrow
\text{bottom Type I terminal}\ \lor\ \text{p-free strict carry}.
}
\tag{28}
\]

**证明。** (24) 证明 q-lock target 确为 ordinary \(a=1,d=1\) full-product
input。d=1 regeneration countdown 保持 (25) 的首个非零 \(p\)-进数字：
\(\omega_{\rm re}=-2\) 由 raw-source repair 严格离开，其它非 \(-1\) 类给
\(c\le p-2\)，即得 (26)。\(\omega_{\rm re}=-1\) 时 countdown 的终类正是
\(b_\ast\equiv-1\pmod p\) 的 p-free root return；正奇性给 (27)。根容量扇的
\(9u^2<p\) 分支给出 (28)。\(\square\)

因此 q-lock 的**已知路由未关闭**部分被进一步压成

\[
\boxed{
\rho\parallel q,\quad\text{(22)},\quad
\omega_{\rm re}\equiv-1\pmod p,\quad 9u^2\ge p.
}
\tag{29}
\]

此外，actual H4 source receipt 还强制

\[
D\equiv2d(4d^2-2d+1)\pmod p,
\qquad
D\mid(2d-1)\bigl((2d+1)q-1\bigr).
\tag{29a}
\]

因此 original H4 carrier \(d=1\) 已被排除；对其余 \(d>1\)，(29a) 至多保留
\(2d\) 个 provenance-aware \(D\) 候选。式 (29) 仍不是不可能条件：它保留了
unitary endpoint allocation、p-adic terminal digit、根容量和这个有限 \(D\) gate；任何
忽略其中之一的“q-lock 自动下降”都不成立。

进一步地，actual 19-phase selector screen 已排除

\[
p>\delta_d:=2d(4d^2-2d+1),
\qquad D>\delta_d.
\tag{29b}
\]

在 \(p>\delta_d\) 的最小分支 \(D=\delta_d\) 中，\(d\equiv1\pmod3\) 也不可能。
所以 (29) 的 H4 provenance residual 还必须满足

\[
p\le\delta_d
\quad\text{或}\quad
\bigl(p>\delta_d,\ D=\delta_d,\ d\not\equiv1\pmod3\bigr).
\tag{29c}
\]

后一个 large-\(p\) minimal branch 在 31-selector 的必要条件 supermenu 中先有 17 条
CRT phase rays；H3 terminal-first 随后独立删去其中 7 条，留下 10 条。它们仍须与
unitary allocation、terminal digit 和 root capacity 联立，不代表已实现的 H4 receipt。

完整 source row 的 \(D\mid K_4\) 商会额外固定 \(t\pmod {4(q-1)}\)，但这与
unitary q-lock 的 \(t\pmod q\) 及任何 terminal \(t\pmod p\) 类两两 CRT 兼容。因此这
不是继续筛去剩余 10 rays 的工具；必须改用 actual H3-to-H4 carrier equality、\(E_\zeta\)、
maximality 或 guards 的信息。
该后继边界及定向控制见
[H4 \(q_0\) re-entry 的完整 source-row CRT 边界](type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-source-row-q-lock-crt-boundary.md)。

## 7. 精确分派与边界

| re-entry 情形 | 本卡给出的结果 | 仍需的独立条件 |
|---|---|---|
| \(Q_\xi=Q_\zeta=1\) | Type I terminal | terminal validator |
| 恰有一块非空 | single-side residual gate 由 (9a) 自动通过 | typed/source/path/serializer guards |
| \(FE_\zeta\not\equiv L_0\pmod p\) | \(c_{\rm re}\le p-2\) | typed/payload guards 后才是 strict edge |
| \(FE_\zeta\equiv L_0\pmod p,\ q\nmid\sigma\) | \(a_{\rm re}>1\) | existing \(a>1\) handoff guards |
| q-lock 且 \(\omega_{\rm re}\ne-1\) | existing d=1 strict dispatch | q-lock target/checkpoint guards |
| q-lock、\(\omega_{\rm re}=-1\)、\(9u^2<p\) | root-fan terminal 或 strict carry | root-return guards |
| q-lock、\(\omega_{\rm re}=-1\)、\(9u^2\ge p\) | residual (29) 加上 (29a)--(29c) 的 \(D\) provenance sieve | 必须另行排除、给证书或构造合法递降 |

这张卡关闭了“p-free re-entry 没有可计算 capacity”的缺口，并把所有仍留在
\(a=1\) 的顶容量情形转换为 endpoint 的有限因子分配和 root-fan 数值条件。它没有
声称 (29) 不可能；任何省略该 residual、或把 (15) 直接登记为全局递降的论证都是不正确的。

## 8. 定向算术回执

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_pfree_capacity_map.py --verify
```

回执只验证 (10)--(29) 的固定 capacity-map 整数控制，包括 strict、\(a>1\)
top-capacity、single-side gate、unitary q-lock 与 q-lock 后的 ordinary d=1 strict relay；
不构造 H4 predecessor，也不验证 actual-H4-only 的 (29a)。后者由独立的 \(D\) 残数门
回执验证；两类控制都不扫描 prime ranges 或历史 Reach。
