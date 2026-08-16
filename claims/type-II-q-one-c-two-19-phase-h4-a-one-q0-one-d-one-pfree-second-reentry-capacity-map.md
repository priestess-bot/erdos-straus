---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-d-one-pfree-second-reentry-capacity-map
title: H4 q0=1 d=1 p-free 第二 re-entry 的完整超额容量图与 unitary q-lock
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity a_alt=1 clean
  q bridge 的 q0=1 second-stutter 中，设 d4=gcd((p+1)/2,M4)=1、a2=1、
  rho||q、qhat=q/rho>1，且 actual x-side re-entry
  (xi,zeta)=(x2/qhat,R4-x2/qhat) 已由 rho=1 或 proper-unitary d=1
  p-primary 排除而 p-free。写 E_x2=qhat F、F=q rho+p t；令 E_zeta 为 zeta
  的 maximal complete-excess multiplier。则 Q_xi=Q_x2/qhat、E_xi=F，
  nonterminal re-entry 的 canonical multiplier 为 L_re=F E_zeta，容量为
  c_re=-L0(F E_zeta)^(-1) (mod p)。顶容量恰为
  F E_zeta=L0+p sigma；此时 target 是 full-product d=1 行，
  n_re=n+4M4 sigma，a_re=q/gcd(q,sigma)。并且
  q|sigma 当且仅当 q|t E_zeta。令 lambda=gcd(q,t)（t=0 时取 lambda=q），
  则这个 q-lock 当且仅当 lambda||q 且 q/lambda divides E_zeta；它给出
  lambda|xi、q/lambda|zeta 的实际 endpoint allocation。非 q-lock 自动进入
  a_re>1 strict handoff；q-lock 写 sigma=qv 后有 b_re=b+2M4v，并由 ordinary
  d=1 countdown/root-fan 路由。故尚未被已有 strict macro 关闭的必要条件精确缩为
  lambda||q、q/lambda|E_zeta、omega_re=-1、9u^2>=p，外加 target 的
  terminal/typed/source/path/serializer/persistent guards。该结论不证明这最终
  residual 不可达，也不把静态容量图自动升级为 global edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q0-one-second-stutter-unitary-transduction
  - type-II-q-one-c-two-19-phase-h4-a-one-q0-one-second-reentry-rho-one-p-primary-exclusion
  - type-II-q-one-c-two-19-phase-h4-a-one-q0-one-proper-unitary-reentry-p-primary-d-gate
  - type-II-q-one-c-two-19-phase-h4-a-one-q0-one-double-q-bridge
  - type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
  - type-I-overflow-full-product-d-one-a-one-root-coprime-capacity-fan-half-descent
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - a-one
  - q0-one
  - double-q-carrier
  - raw-path
  - p-free
  - complete-excess-bundle
  - capacity-map
  - unitary-divisor
  - q-lock
  - p-adic-regeneration
  - root-capacity-fan
  - solution-lift
  - well-founded-rank
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-second-stutter-unitary-transduction
    role: second-stutter-normal-form-and-actual-x-side-reentry
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-second-reentry-rho-one-p-primary-exclusion
    role: rho-one-p-free-reentry
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-proper-unitary-reentry-p-primary-d-gate
    role: proper-unitary-d-one-p-primary-closure
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-double-q-bridge
    role: double-q-endpoint-and-second-capacity-normalization
  - claim: type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
    role: ordinary-d-one-countdown-and-strict-rank
  - claim: type-I-overflow-full-product-d-one-a-one-root-coprime-capacity-fan-half-descent
    role: root-fan-terminal-or-strict-carry
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: one-side-and-atomic-payload-guard-boundary
  - concept: denominator-escape-state-contract
    role: typed-E1-to-E5-and-global-lift-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q0_one_d_one_pfree_reentry_capacity_map.py
    role: focused-capacity-map-and-q-lock-normal-form-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 \(q_0=1\) \(d_4=1\) p-free 第二 re-entry 的容量图

## 1. 范围

保留 actual H4 \(q_0=1\) double-\(q\) bridge 的第二 stutter。为避免与 full-product
行的 \(d=1\) 混淆，先把 H4 载体记为

\[
w=\frac{p+1}{2},\qquad d_4=(w,M_4),\qquad q=\frac{w}{d_4}.
\tag{1}
\]

本卡只处理

\[
\boxed{d_4=1,\qquad w=q,\qquad p=2q-1,\qquad h=2,\qquad (q,M_4)=1.}
\tag{2}
\]

在第二 stutter 的 \(a_2=1\) 分派中，已有 unitary-carrier transduction 给

\[
\rho\parallel q,\qquad \widehat q=\frac q\rho>1,\qquad
s=\widehat q t,
\tag{3}
\]

\[
E_{x,2}=\widehat q F,\qquad F=q\rho+pt.
\tag{4}
\]

因此同一 actual H4 prefix 上有 x-side primitive raw re-entry

\[
\boxed{
(\xi,\zeta)=\left(\frac{x_2}{\widehat q},
R_4-\frac{x_2}{\widehat q}\right).
}
\tag{5}
\]

若 \(\rho=1\)，既有因式排除已证明 (5) p-free；若 \(1<\rho<q\)，则
\(d_4=1\) 的 proper-unitary \(D\)-gate 为空，也已证明 (5) p-free。故在本卡的
\(\widehat q>1\) 范围内，

\[
\boxed{p\nmid\xi\zeta.}
\tag{6}
\]

第三 \(q\)-carrier \(\widehat q=1\) 是另一条 y-side raw word，不在本卡的 x-side
re-entry 范围内。

将两侧相对 \(K_4\) 的 maximal complete-excess 分解写为

\[
\xi=Q_\xi\beta_\xi,\qquad
\zeta=Q_\zeta\beta_\zeta,
\tag{7}
\]

\[
E_\xi=\frac{Q_\xi}{(M_4,Q_\xi)},\qquad
E_\zeta=\frac{Q_\zeta}{(M_4,Q_\zeta)}.
\tag{8}
\]

若 \(Q_\zeta=1\)，约定 \(E_\zeta=1\)。原 H4 top-capacity multiplier 仍记为

\[
M_{\rm alt}=M_4L_0=\frac{pn-1}{4},
\qquad n=(p+1)b-1=2qb-1.
\tag{9}
\]

这里 \(q_0=1\) 已给出 \(q^2\mid L_0\)，但本卡**不**把它错误强化为
\(L_0=q^2\)。

## 2. x-side 剥离后的精确 complete-excess block

把第二 endpoint 的 selected block 写为

\[
x_2=Q_{x,2}\beta_{x,2},\qquad
g=(M_4,Q_{x,2}),\qquad
D=g\beta_{x,2}.
\tag{10}
\]

由 (4) 有 \(Q_{x,2}=g\widehat qF\)。由于
\((\widehat q,M_4)=1\)，从 \(x_2\) 实际除去 \(\widehat q\) 只剥去该完整超额
block 的对应因子，逐素数得到

\[
\boxed{
Q_\xi=\frac{Q_{x,2}}{\widehat q}=gF,\qquad
\beta_\xi=\beta_{x,2},\qquad
E_\xi=F.
}
\tag{11}
\]

特别地，

\[
\xi=FD.
\tag{12}
\]

这里不需要 \((F,\widehat q)=1\)：若 \(F\) 仍含 \(\widehat q\) 的某个素因子，
它正确地保留在 \(Q_\xi\) 中。

由 primitive raw re-entry 有 \((\xi,\zeta)=1\)，所以

\[
(Q_\xi,Q_\zeta)=1.
\tag{13}
\]

若两块都为空，(5) 已是 Type I terminal。若恰有一块非空，则对应的 single-side
residual-divisibility gate 与普通 p-free re-entry 一样自动通过；两块都非空时仍须
调用 atomic adapter。以下只计算二者共享的算术容量，不跳过这些语义 guards。

## 3. canonical capacity 与顶容量 re-entry

由 (11)、(13)，nonterminal re-entry 的 complete-excess multiplier 是

\[
\boxed{
L_{\rm re}
=\frac{\operatorname{lcm}(M_4,Q_\xi,Q_\zeta)}{M_4}
=E_\xi E_\zeta
=F E_\zeta.
}
\tag{14}
\]

式 (6) 使 \(F E_\zeta\) 在模 \(p\) 下可逆。原 H4 top-capacity relation
\(c_4L_0^{-1}\equiv-1\pmod p\) 因而给

\[
\boxed{
c_{\rm re}\equiv-L_0(FE_\zeta)^{-1}\pmod p.
}
\tag{15}
\]

所以

\[
\boxed{
c_{\rm re}=p-1
\quad\Longleftrightarrow\quad
FE_\zeta\equiv L_0\pmod p.
}
\tag{16}
\]

在这个唯一的顶容量情形，唯一写为

\[
FE_\zeta=L_0+p\sigma,\qquad \sigma\in\mathbb Z.
\tag{17}
\]

于是

\[
\begin{aligned}
M_{\rm re}
&=M_4FE_\zeta
=M_{\rm alt}+pM_4\sigma,\\
\boxed{n_{\rm re}}&=\boxed{n+4M_4\sigma},
\qquad
M_{\rm re}=\frac{pn_{\rm re}-1}{4}.
\end{aligned}
\tag{18}
\]

该 target 的 \(a\)-coordinate 直接由 (2)、(9)、(18) 给出：

\[
\begin{aligned}
a_{\rm re}
&=\frac{q}{\left(q,(n_{\rm re}+1)/2\right)}\\
&=\frac{q}{(q,qb+2M_4\sigma)}
=\boxed{\frac q{(q,\sigma)}}.
\end{aligned}
\tag{19}
\]

故

\[
q\nmid\sigma
\quad\Longrightarrow\quad
a_{\rm re}>1.
\tag{20}
\]

在 re-entry payload、target reclassification 和所有已有 guards 通过时，(20) 接入
既有 \(a>1\) \(d=1\) strict handoff。它以同一 \(4/p\) 的
\(\operatorname{Sol}(p)\) identity map 支付 E4，并由既有容量秩严格下降支付 E5。

## 4. q-lock 的 exact unitary endpoint allocation

把 (17) 模 \(q\) 约化。由于 \(q\mid L_0\)、\(p\equiv-1\pmod q\) 和
\(F=q\rho+pt\)，有

\[
-tE_\zeta\equiv-\sigma\pmod q.
\tag{21}
\]

因此 (19) 中唯一的 \(a=1\) 算术回返恰为

\[
\boxed{
q\mid\sigma
\quad\Longleftrightarrow\quad
q\mid tE_\zeta.
}
\tag{22}
\]

这不是一个没有 endpoint 语义的同余。令

\[
\lambda=(q,t),
\tag{23}
\]

其中 \(t=0\) 时 \(\lambda=q\)。则有以下精确签名。

### 引理 1（second re-entry q-lock 签名）

\[
\boxed{
q\mid\sigma
\quad\Longleftrightarrow\quad
\lambda\parallel q
\ \text{且}\
\frac q\lambda\mid E_\zeta.
}
\tag{24}
\]

在 (24) 成立时还有

\[
\boxed{
\lambda\mid F\mid\xi,
\qquad
\frac q\lambda\mid E_\zeta\mid\zeta.
}
\tag{25}
\]

**证明。** 因为 \((p,q)=1\)，若 \(\ell^e\parallel q\) 且
\(0\le v_\ell(t)<e\)，则

\[
v_\ell(F)
=v_\ell(q\rho+pt)
=v_\ell(t).
\tag{26}
\]

另一方面 \(E_\zeta\mid\zeta\)、\(F\mid\xi\) 且 \((\xi,\zeta)=1\)，故
\((F,E_\zeta)=1\)。若 (22) 成立且 \(0<v_\ell(t)<e\)，则
\(v_\ell(E_\zeta)\ge e-v_\ell(t)>0\)，与此互素性矛盾。故对每个
\(\ell^e\parallel q\)，要么 \(v_\ell(t)=0\)，要么 \(v_\ell(t)\ge e\)。

于是 \(\lambda=(q,t)\) 逐素数要么含完整的 \(\ell^e\)、要么不含，亦即
\(\lambda\parallel q\)。在后者中，(22) 强制 \(\ell^e\mid E_\zeta\)，所以
\(q/\lambda\mid E_\zeta\)。反向只要 \(\lambda\mid t\) 及
\(q/\lambda\mid E_\zeta\)，便立即有 \(q\mid tE_\zeta\)。最后，
\(\lambda\mid q,t\) 使 \(\lambda\mid q\rho+pt=F\)，并与
\(q/\lambda\mid E_\zeta\mid\zeta\) 一起给 (25)。\(\square\)

因此 composite \(q\) 的 q-lock 不是二选一或任意部分幂分配；它至多有
\(2^{\omega(q)}\) 个完整素数幂的 endpoint allocation。

## 5. q-lock 到 ordinary d=1 root-fan 的 relay

现在设 q-lock 成立，写

\[
\sigma=qv.
\tag{27}
\]

由 (9)、(18) 得 target 的 \(a_{\rm re}=1\) 参数

\[
\boxed{
b_{\rm re}
=\frac{n_{\rm re}+1}{p+1}
=b+2M_4v.
}
\tag{28}
\]

在 target 经 terminal-first、typed、source/path、serializer 和 persistent guards
准入后，它正是 ordinary full-product \(d=1\) 行。令

\[
G_{\rm re}=(p-1)b_{\rm re}-1,
\qquad
\eta_{\rm re}=v_p(G_{\rm re}-1),
\qquad
\omega_{\rm re}\equiv
\frac{G_{\rm re}-1}{p^{\eta_{\rm re}}}\pmod p.
\tag{29}
\]

既有 ordinary \(d=1\) countdown、raw-source repair 与 p-free root-return
classification 给出：

\[
\omega_{\rm re}\not\equiv-1\pmod p
\quad\Longrightarrow\quad
\text{已有 strict macro};
\tag{30}
\]

\[
\omega_{\rm re}\equiv-1\pmod p
\quad\Longrightarrow\quad
b_\ast=2pr-1
\tag{31}
\]

在恰 \(\eta_{\rm re}\) 次 canonical regeneration 之后。令

\[
u=\left(2r+1,\frac{p^2+p+1}{3}\right).
\tag{32}
\]

root-coprime capacity fan 进一步给出

\[
9u^2<p
\quad\Longrightarrow\quad
\text{bottom Type I terminal}\ \lor\ \text{p-free strict carry}.
\tag{33}
\]

所以本卡范围内尚未被已有算术路由关闭的必要条件是

\[
\boxed{
\lambda\parallel q,\qquad
\frac q\lambda\mid E_\zeta,\qquad
\omega_{\rm re}\equiv-1\pmod p,\qquad
9u^2\ge p.
}
\tag{34}
\]

式 (34) 还必须与 actual H4 source provenance、single-side 或 atomic payload 的
准入、以及全部 state-contract guards 同时满足。它不是“剩余状态存在”的断言，更不是
全局出口定理。

## 6. 静态边界控制

存在只满足本卡整数 normal form 的静态 q-lock/root residual 控制；因此不能仅由
\(q\mid tE_\zeta\)、\(\omega_{\rm re}=-1\) 或 \(9u^2\ge p\) 中任一条件推出矛盾。
反过来，也有 q-lock 立即进入 \(u=1\) root-fan 出口的控制。两者都不构造 actual H4
predecessor、不声称 \(E_\zeta\) 是某个实际 endpoint 的 maximal block，只防止把
算术必要条件误写成充分的 global closure。

    python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q0_one_d_one_pfree_reentry_capacity_map.py --verify

回执仅核对 (14)--(34) 的整数 identity、non-lock \(a>1\) control、unitary allocation、
root-fan exit control 与 residual normal-form control；不扫描素数、分母、历史 Reach
或 H4 predecessor。
