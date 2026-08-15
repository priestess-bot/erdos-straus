---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-s-zero-secondary-q-lock-exclusion
title: H4 q-bridge s=0 secondary p-free gate 的 a=1 q-lock 有限排除
statement: >-
  在满足 R4=1 (mod p) 的 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity
  a_alt=1 clean q bridge 中，取 s=0 q-block swap 的 p-free single-side secondary
  endpoint，并设其唯一容量 stutter 为 E_zeta=L0+p*sigma。则该 target 再次是完整乘积
  d=1 顶容量行，且其精确 a 坐标为 a_zeta=q/gcd(q,sigma)。若反设 a_zeta=1，则
  q|sigma；写 h=2e、d=gcd((p+1)/2,M4)、q=(p+1)/(2d)，actual q-swap identity
  唯一给 xi=h+(q-1)r，且 H4 高度界强迫 r>0。q-lock 等价于 q|r，故 r=q*t、t>=1，
  并由 xi|ph-q+1 得 q<=4de-1。于是所有反例落在有限菜单
  d<=1535、e|d、q<=4de-1、p=2dq-1、p=769 (mod 912)、u(p) in U_31、
  d|abs(1536-a(p))、以及 2e+q(q-1)t | 2ep-q+1。对该菜单作精确枚举，
  149977 个 residual-phase (d,q) 参数中 524 个通过 H4 provenance，而没有一个满足
  最后的整除式。因此 q 不整除 sigma，a_zeta>1，secondary p-free capacity stutter
  可接入既有 a>1 d=1 strict handoff。该结论不自动通过 terminal-first、typed、scope、
  serializer 或 persistent E1--E5 guards，也不单独证明 G/Type I 全局出口。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-s-zero-q-swap-p-primary-exclusion
  - type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
  - type-II-q-one-c-two-19-phase-h4-p-primary-small-anchor-renewal
  - type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
  - type-I-overflow-full-product-d-one-p-free-peeled-small-anchor
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
  - complete-excess-bundle
  - carry-stutter
  - p-free
  - finite-sieve
  - capacity-transduction
  - source-provenance
  - well-founded-rank
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-s-zero-q-swap-p-primary-exclusion
    role: actual-secondary-endpoint-p-free-receipt-and-xi-divisibility
  - claim: type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
    role: d-one-a-greater-than-one-strict-handoff-and-delta-provenance
  - claim: type-II-q-one-c-two-19-phase-h4-p-primary-small-anchor-renewal
    role: H4-height-bound-for-positive-secondary-parameter
  - claim: type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
    role: exact-residual-19-phase-menu-and-third-anchor-selector
  - claim: type-I-overflow-full-product-d-one-p-free-peeled-small-anchor
    role: p-free-d-one-a-greater-than-one-strict-suffix
  - concept: denominator-escape-state-contract
    role: terminal-typed-lift-and-potential-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_s_zero_secondary_q_lock_exclusion.py
    role: exact-secondary-q-lock-finite-menu-screen
visibility: public
last_checked: '2026-08-16'
---

# H4 \(q\)-bridge \(s=0\) secondary p-free gate 的 \(a=1\) q-lock 排除

## 1. 范围与带符号的顶容量 target

保留已建立的 actual q=1 high \(C=2\) 19-phase H4 proper-overlap
top-capacity \(a_{\rm alt}=1\) clean \(q\) bridge，及其 \(s=0\) q-block swap
的记号：

\[
w=\frac{p+1}{2}=qd,
\qquad d=(w,M_4),
\qquad (q,K_4)=(q,M_4)=1,
\tag{1}
\]

\[
h=2e,
\qquad e\mid d,
\qquad d\mid\Delta:=|1536-a(p)|,
\qquad 1\le\Delta\le1535.
\tag{2}
\]

先前的 q-block swap 已从原 H4 prefix 实际到达 primitive node

\[
\{\xi,\zeta\}=\left\{\frac{x_q}{q},R_4-\frac{x_q}{q}\right\},
\qquad
\xi\mid K_4,
\qquad
\xi\mid ph-q+1,
\tag{3}
\]

并排除了 \(Q_\zeta\) 的 \(p\)-block。若 \(Q_\zeta=1\)，这里已经是 Type I
terminal；故以下设 \(Q_\zeta>1\)，令

\[
E_\zeta=\frac{Q_\zeta}{(M_4,Q_\zeta)},
\qquad
L_0=\frac{\operatorname{lcm}(M_4,Q)}{M_4}.
\tag{4}
\]

唯一的容量 stutter 是 \(E_\zeta\equiv L_0\pmod p\)。写它的**带符号**差为

\[
\boxed{E_\zeta=L_0+p\sigma,\qquad \sigma\in\mathbb Z.}
\tag{5}
\]

这不假定 \(\sigma\ge0\)。原 top-capacity support 满足

\[
M_{\rm alt}=M_4L_0=\frac{pn-1}{4},
\qquad n=(p+1)b-1.
\tag{6}
\]

因此 secondary target 精确为另一条完整乘积顶容量行：

\[
M_\zeta=M_4E_\zeta=\frac{pn_\zeta-1}{4},
\qquad n_\zeta=n+4M_4\sigma.
\tag{7}
\]

写 \(M_4=dU\)。由 (1) 有 \((q,U)=1\)，而

\[
\frac{n_\zeta+1}{2}
=wb+2M_4\sigma
=d(qb+2U\sigma).
\tag{8}
\]

所以 secondary target 的精确 \(a\)-coordinate 是

\[
\boxed{a_\zeta=\frac{q}{(q,\sigma)}.}
\tag{9}
\]

若 \(q\nmid\sigma\)，则 \(a_\zeta>1\)，可在既有 target reclassification 与全部
guards 通过时接入 \(a>1\) d=1 strict handoff。本卡只排除唯一尚可能把 (9) 留在
\(a=1\) 的 q-lock。

## 2. q-lock 是 secondary raw endpoint 的正参数条件

在 q-block swap 的 first endpoint 中已有

\[
q^2\xi=(q-1)R_4+h.
\tag{10}
\]

模 \(q-1\) 约化，定义整数 \(r\) 为

\[
\boxed{\xi=h+(q-1)r.}
\tag{11}
\]

又 q-word 的另一坐标为 \(y_q=(R_4-h)/q\)。将 (11) 代入先前恒等式
\((q-1)y_q=q\xi-h\)，得到完整参数化

\[
y_q=h+qr,
\qquad
R_4=(q+1)h+q^2r,
\qquad
\zeta=qh+(q^2-q+1)r.
\tag{12}
\]

这里 \(r\) 不会为零或负。实际 H4 小锚 renewal 的高度界给

\[
z=R_4-h>
\frac{p^3}{2}-\frac1p-(p+1)
>\frac{(p+1)^2}{2}\ge qh,
\tag{13}
\]

其中末项使用 \(q\le w=(p+1)/2\)、\(h<p+1\)，且中间不等式对核心域
\(p\ge73\) 直接成立。故 \(y_q=z/q>h\)，由 (12) 得

\[
\boxed{r>0.}
\tag{14}
\]

另一方面，\(q\mid L_0\)，而 \(q\) 与 \(pM_4K_4\) 全部互素。结合 (5) 及
complete-excess 的逐素数定义，得到没有丢失合数 \(q\) 幂的等价链：

\[
\boxed{
q\mid\sigma
\Longleftrightarrow q\mid E_\zeta
\Longleftrightarrow q\mid Q_\zeta
\Longleftrightarrow q\mid\zeta
\Longleftrightarrow q\mid r.
}
\tag{15}
\]

最后一项来自 (12) 的 \(\zeta\equiv r\pmod q\)。因此 q-lock 会唯一给出

\[
\boxed{r=qt,\qquad t\ge1,\qquad
\xi=2e+q(q-1)t.}
\tag{16}
\]

这是 actual raw endpoint 的必要条件，而不是对抽象 d=1 target 另加的假设。

## 3. \(q\) 被压入有限 H4 菜单

由 (3)、(16) 和 \(p=2qd-1\)，q-lock 必满足

\[
2e+q(q-1)t
\mid
ph-q+1
=q(4de-1)-(2e-1).
\tag{17}
\]

特别地左端不超过右端。若 \(q\ge4de\)，以 \(t\ge1\) 估计差值给

\[
\begin{aligned}
(ph-q+1)-\xi
&\le q(4de-q)-4e+1\\
&\le-4e+1<0,
\end{aligned}
\tag{18}
\]

矛盾。因此每个 actual q-lock 只可能满足

\[
\boxed{1<q\le4de-1.}
\tag{19}
\]

这一步把此前无界的 signed capacity difference \(\sigma\) 转为一个由 H4 phase
data 决定的有限 \((d,e,q,t)\) 整数菜单。

## 4. 精确有限筛

实际 19-phase 中

\[
p=2dq-1\equiv769\pmod{912},
\qquad
u(p)=\frac{p-769}{912}\pmod{119}\in\mathcal U_{31},
\tag{20}
\]

并且 (2) 的 \(d\mid\Delta\) 是不可省略的 H3-to-H4 provenance 条件。由
(2)、(17)、(19)，每个 q-lock 都必须出现于下列精确菜单：

\[
\left.
\begin{gathered}
1\le d\le1535,\quad e\mid d,\quad1<q\le4de-1,\\
p=2dq-1\text{ 是素数},\quad u(p)\in\mathcal U_{31},\quad d\mid\Delta,\\
2e+q(q-1)t\mid2ep-q+1\quad(t\ge1).
\end{gathered}
\right\}
\tag{21}
\]

脚本对 (21) 作了整数级的穷尽。先只施加 \(p\equiv769\pmod{912}\) 与
\(q<4d^2\) 时有 3,345,232 个 \((d,q)\) 参数；其中精确 primality 检查保留
534,967 个，31 个 residual phase 保留 149,977 个，H4 provenance \(d\mid\Delta\)
保留 524 个。最后的 (17) 整除门给出：

\[
\boxed{\text{actual q-lock candidates}=\varnothing.}
\tag{22}
\]

为了显示筛选不是同余恒等式，residual phase 而未通过 provenance 的全部算术命中恰为：

| \(p\) | \(d\) | \(e\) | \(q\) | \(u\) | \(\Delta\) | \(t\) | \(\xi\) | \((ph-q+1)/\xi\) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 14,449 | 1,445 | 17 | 5 | 15 | 1,105 | 198 | 3,994 | 123 |
| 14,449 | 1,445 | 17 | 5 | 15 | 1,105 | 8,186 | 163,754 | 3 |
| 14,449 | 1,445 | 289 | 5 | 15 | 1,105 | 417,547 | 8,351,518 | 1 |

三行均有 \(1445\nmid1105\)。另有静态 \(p=409,d=41,e=1,q=5,t=1\) 控制，
以及 base phase 但 terminal-first 已移除的 \(p=769,d=35,e=5,q=11,t=1\) 控制。
故 terminal-first phase 与 actual H4 provenance 都在排除中实质发挥作用。

## 5. 后果与边界

(22) 排除 (15) 的首项，即

\[
\boxed{q\nmid\sigma,\qquad a_\zeta>1.}
\tag{23}
\]

所以 \(s=0\) q-block swap 的 secondary p-free branch 现在有完整的算术分派：

\[
Q_\zeta=1
\Longrightarrow\text{Type I terminal};
\qquad
Q_\zeta>1, c_\zeta\le p-2
\Longrightarrow\text{strict capacity};
\]

而唯一原先的 top-capacity case \(c_\zeta=p-1\) 也强制进入 \(a_\zeta>1\) d=1
strict handoff。于是这个 \(s=0\) branch 不再遗留 \(a=1\) q-lock 算术回返。

这里仍不把算术 target 自动登记为 global edge：每个 terminal-first、typed
reclassification、source/path、scope、serializer 和 persistent E1--E5 guard 必须逐个
通过。特别地，本卡没有单独证明整个 G/Type I 全局出口；它只关闭了该出口图中的一个
明确 secondary capacity gate。

## 6. 定向复现

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_s_zero_secondary_q_lock_exclusion.py --verify
```

回执检查三个静态 q-lock 控制，随后穷尽 (21) 的有限菜单并要求 (22) 的空输出。它不扫描
分母、历史 Reach、H4 predecessor 或任意外加 prime interval。
