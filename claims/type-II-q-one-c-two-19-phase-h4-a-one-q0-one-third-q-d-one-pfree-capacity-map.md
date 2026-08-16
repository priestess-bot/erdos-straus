---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-third-q-d-one-pfree-capacity-map
title: H4 q0=1 第三 q carrier 的 d=1 p-free 容量图与 source D-gate
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity a_alt=1 clean
  q bridge 的 q0=1 second-stutter 中，若 d4=gcd((p+1)/2,M4)=1、rho=q、
  qhat=1，则 q^3 divides L0 divides Q_K4(z)。令 U=L0/q^3，并在第三 actual
  q word (x3,y3)=(R4-z/q^3,z/q^3) 处写 x3=Q_x3 beta_x3、
  E=Q_x3/gcd(M4,Q_x3)、D=gcd(M4,Q_x3) beta_x3。则 p-free third endpoint 的
  complete-excess multiplier 和 capacity 精确为 L3=UE、c3=-q^3 E^{-1} (mod p)。
  raw identity 强制 ED=9 (mod p)、D divides q^3-4q+1；因此唯一非严格 capacity
  E=q^3 (mod p) 强制 D=72 (mod p)。若写 E=q^3+ps，则相应 full-product chart 有
  n3=n+4M4Us，且其 a-coordinate 为 a3=q/gcd(q,Us)。a3=1 恰给出 q 在
  U|y3 与 E|x3 两端之间的 unitary prime-power allocation；它仍须经过 typed/payload
  guards，且本卡不证明该 source-D residual 全称为空或一般 G/Type I selector。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q0-one-third-q-d-one-p-primary-exclusion
  - type-II-q-one-c-two-19-phase-h4-a-one-q0-one-second-stutter-unitary-transduction
  - type-II-q-one-c-two-19-phase-h4-a-one-q0-one-double-q-bridge
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
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
  - triple-q-carrier
  - raw-path
  - p-free
  - complete-excess-bundle
  - residual-capacity
  - source-provenance
  - divisor-gate
  - unitary-divisor
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-third-q-d-one-p-primary-exclusion
    role: actual-third-carrier-and-p-free-endpoint
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-second-stutter-unitary-transduction
    role: rho-equals-q-triple-carrier-receipt
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-double-q-bridge
    role: q-squared-base-capacity-and-p-free-bundle
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: actual-clean-raw-word-and-p-free-payload-taxonomy
  - concept: denominator-escape-state-contract
    role: capacity-edge-versus-admitted-macro-boundary
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q0_one_third_q_d_one_pfree_capacity_map.py
    role: focused-third-carrier-capacity-and-source-D-gate-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 \(q_0=1\) 第三 \(q\) carrier 的 \(d=1\) p-free 容量图

## 1. 第三实际端点与完整超额分解

保留 actual H4 \(q_0=1\) second-stutter 的 \(d_4=1\) 分支，并设

\[
q=\frac{p+1}{2},\qquad p=2q-1,\qquad h=2,
\qquad \rho=q,\qquad\widehat q=1.
\tag{1}
\]

已有 unitary transduction 给出

\[
q^3\mid L_0\mid Q:=Q_{K_4}(z)\mid z,
\qquad (q,K_4)=1,
\tag{2}
\]

故第三条 actual primitive raw word 的端点是

\[
(x_3,y_3)=\left(R_4-\frac z{q^3},\frac z{q^3}\right).
\tag{3}
\]

令

\[
U=\frac{L_0}{q^3},\qquad
x_3=Q_{x,3}\beta_{x,3},\qquad
g=(M_4,Q_{x,3}),
\tag{4}
\]

\[
E=\frac{Q_{x,3}}{g},\qquad D=g\beta_{x,3}.
\tag{5}
\]

由最大 complete-excess 分解，\(g\) 与 \(\beta_{x,3}\) 是 \(K_4\) 的互素因子，
因此

\[
\boxed{x_3=ED,\qquad D\mid K_4.}
\tag{6}
\]

另一方面，\(q\) 与 \(M_4\) 互素，且从 \(z\) 侧除去 \(q^3\) 只移去这条
clean carrier 的相应完整素数幂。因此

\[
Q_{y,3}=\frac Q{q^3},\qquad
\frac{Q_{y,3}}{(M_4,Q_{y,3})}=U.
\tag{7}
\]

端点 primitive 性给 \((x_3,y_3)=1\)，所以 \(E\) 与 \(U\) 互素。

## 2. raw identity、p-free 复核与 source \(D\)-gate

由 \(q^3y_3=z=R_4-2\) 及 \(x_3+y_3=R_4\)，有

\[
q^3x_3=(q^3-1)R_4+2.
\tag{8}
\]

代入 (6)，并用 actual H4 receipt \(R_4\equiv1\pmod p\)、
\(q\equiv\tfrac12\pmod p\)，得到

\[
q^3ED\equiv q^3+1\pmod p,
\qquad
\boxed{ED\equiv9\pmod p.}
\tag{9}
\]

这也给出比单独因式分解更直接的 p-free 复核：\(p\ge73\) 时右端非零，
故 \(p\nmid x_3\)；而原 p-free bundle 给 \(p\nmid y_3\)。

将 \(pR_4+1=4K_4\) 代入 (8)，得到

\[
4(q^3-1)K_4-pq^3ED=q^3-1-2p=q^3-4q+1.
\tag{10}
\]

结合 \(D\mid K_4\) 与 \(D\mid ED\)，有第二个 source gate：

\[
\boxed{D\mid q^3-4q+1.}
\tag{11}
\]

式 (9)、(11) 在本卡范围内来自 actual raw path，不是静态 endpoint 的额外假设。

## 3. p-free complete-excess capacity

若 \(Q_{x,3}=Q_{y,3}=1\)，(3) 是 terminal-first 的 Type I terminal。以下设
至少一块非平凡。由于两块互素，单侧情形自动满足既有 residual-divisibility gate，
双侧情形仍须 atomic adapter。两类共同的算术 multiplier 是

\[
L_3=
\frac{\operatorname{lcm}(M_4,Q_{x,3},Q_{y,3})}{M_4}
=\boxed{UE}.
\tag{12}
\]

原 H4 top-capacity receipt 为 \(c_4L_0^{-1}\equiv-1\pmod p\)。于是唯一
canonical capacity 满足

\[
\boxed{c_3\equiv-q^3E^{-1}\pmod p.}
\tag{13}
\]

所以所有 nonterminal p-free endpoint 中，非严格容量恰为

\[
\boxed{
c_3=p-1
\quad\Longleftrightarrow\quad
E\equiv q^3\pmod p.
}
\tag{14}
\]

若 (14) 不成立，则 \(c_3\le p-2\)；在已有 terminal-first、typed、payload、
serializer 与 persistent guards 成功时，这正是从同一 persistent parent 出发的严格
capacity edge。

## 4. 顶容量的 \(D\)-gate 与 \(a\)-坐标

现在只设 (14)，并唯一写成

\[
E=q^3+ps,\qquad s\in\mathbb Z.
\tag{15}
\]

把 (15) 代入 (9)，得到第三 carrier 顶容量的必要 source congruence

\[
\boxed{D\equiv72\pmod p.}
\tag{16}
\]

因此未被严格容量关闭的 actual third endpoint 必同时满足

\[
\boxed{
D\equiv72\pmod p,
\qquad
D\mid q^3-4q+1.
}
\tag{17}
\]

这是一条 provenance-aware sieve；本卡不把它误称为全称矛盾。

另一方面，由 (12)、(15) 有

\[
\begin{aligned}
M_3&=M_4UE=M_4L_0+pM_4Us,\\
\boxed{n_3}&=\boxed{n+4M_4Us},
\qquad
M_3=\frac{pn_3-1}{4}.
\end{aligned}
\tag{18}
\]

若该 full-product target 通过重分类而成为正 \(d=1\) chart，则其 \(a\)-coordinate
精确为

\[
\boxed{
a_3=
\frac q{\left(q,(n_3+1)/2\right)}
=\frac q{(q,Us)}.
}
\tag{19}
\]

因此 \(q\nmid Us\) 时有 \(a_3>1\)，可在所有既有 guards 通过后交给现有
\(a>1\) strict handoff。

## 5. \(a_3=1\) 的 unitary endpoint allocation

剩余的纯算术回返条件是 \(q\mid Us\)。因为 \((U,E)=1\) 且
\(E\equiv ps\pmod q\)，令

\[
\lambda=(q,U)
\tag{20}
\]

便有精确等价：

\[
\boxed{
q\mid Us
\quad\Longleftrightarrow\quad
\lambda\parallel q,
\qquad \frac q\lambda\mid s.
}
\tag{21}
\]

在 (21) 中，\(\lambda\mid U\mid y_3\)，而
\(q/\lambda\mid E\mid x_3\)。这些 prime-power 都相对于 \(K_4\) clean，
所以它们指出第三 endpoint 上实际可选的 raw prime edges；复合 \(q\) 的完整幂
不能被误写成单一的二选一分支。

**证明。** 若 \(q\mid Us\)，取 \(\ell^e\parallel q\)。若 \(U\) 含有
\(\ell\) 的非完整正幂，则 \(s\) 必含 \(\ell\)，而
\(E=q^3+ps\) 也含 \(\ell\)，与 \((U,E)=1\) 矛盾。因此 \(U\) 对 \(q\) 的
每个素数幂要么全含、要么不含，故 \(\lambda\parallel q\)。未含在 \(U\) 中的
完整幂必须整除 \(s\)。反向由 \(\lambda\mid U\)、\(q/\lambda\mid s\) 立即
给 \(q\mid Us\)。最后 \(E\equiv ps\pmod{q/\lambda}\) 且 \((p,q)=1\) 给
\(q/\lambda\mid E\)。\(\square\)

这不是全局 exit：mixed allocation 仍要经过 terminal/typed/payload/serializer 和
persistent guards；如果它被登记为 \(a=1\) target，后续 ordinary \(d=1\) countdown
或 root-fan 也必须按各自 contract 单独支付。

**范围更新。** 后继的
[original q-bridge source \(D\)-gate 全称排除](type-II-q-one-c-two-19-phase-h4-a-one-d-one-q-bridge-stutter-source-d-gate-closure.md)
已在 first stutter 层排除 actual \(d_4=1\) parent。因此本卡的 \(D\equiv72\pmod p\)
map 不再是 actual \(d_4=1\) residual，而是被排除 antecedent 的完整 capacity normal
form；它仍避免未来重新引入错误的 third-carrier 论证。

## 6. 定向回执与边界

    python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q0_one_third_q_d_one_pfree_capacity_map.py --verify

回执核对 \(p=73\) 时 (16)--(17) 的 divisor control、第三 carrier 的 capacity
同余，以及复合 \(q=205\) 的 unitary allocation 算术。它不搜索素数范围、H4
predecessor、denominator 或 Reach history；全称结论来自上面的代数推导。
