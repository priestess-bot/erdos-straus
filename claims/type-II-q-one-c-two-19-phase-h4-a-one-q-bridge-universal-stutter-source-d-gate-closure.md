---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-universal-stutter-source-d-gate-closure
title: H4 clean q-bridge 首层容量 stutter 的全域 source D-gate 关闭
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity a_alt=1 clean
  q bridge 中，对任意 carrier d=gcd((p+1)/2,M4)，不存在原 q-word 的 arithmetic
  capacity stutter E_x=q (mod p)。实际 source identity 强制
  D=(M4,Q_x) beta_x 同时满足 D=2d(4d^2-2d+1) (mod p) 和
  D divides ph-q+1，其中 h=2d、p=2dq-1、D divides K4。这个门不含 q0、gamma、
  t 或 payload 条件。p<=delta_d 时既有 finite low-p source screen 已穷尽其全部
  phase/D 菜单；p>delta_d 时，D>delta_d 的有限 nonminimal screen 为空，
  D=delta_d 的 17 条 phase rays 又由 H3 terminal-first、17-adic carrier 与
  complete-excess valuation 三分全部删除。故 q0=1 double-q/second/third carrier
  与 q0>1 re-entry 都没有 actual first-stutter parent；仍存的 nonterminal clean
  q endpoint 在算术容量上必有 c_q<=p-2，是否成为 strict macro 仍取决于既有
  terminal/typed/source/payload guards。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-complete-excess-stutter-reduction
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
  - type-II-q-one-c-two-19-phase-h4-p-primary-small-anchor-renewal
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-d-residue-gate
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-nonminimal-d-lift-finite-phase-exclusion
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-large-p-minimal-d-closure
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-finite-low-p-source-gate-closure
  - type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - q-bridge
  - capacity-stutter
  - source-provenance
  - divisor-gate
  - finite-sieve
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-complete-excess-stutter-reduction
    role: unique-first-stutter-gate-and-strict-capacity-complement
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: actual-q-word-and-support-normalized-D
  - claim: type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
    role: clean-carrier-forces-h-equals-two-d
  - claim: type-II-q-one-c-two-19-phase-h4-p-primary-small-anchor-renewal
    role: actual-H4-carry-and-phase-provenance
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-nonminimal-d-lift-finite-phase-exclusion
    role: source-only-nonminimal-D-screen
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-large-p-minimal-d-closure
    role: source-only-minimal-D-ray-closure
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-finite-low-p-source-gate-closure
    role: source-only-low-p-D-screen
visibility: public
last_checked: '2026-08-16'
---

# H4 clean \(q\)-bridge 首层 stutter 的全域 source \(D\)-gate

## 1. 需要关闭的实际首门

保留 actual \(q=1\) high \(C=2\) 19-phase H4 proper-overlap top-capacity
\(a_{\rm alt}=1\) clean \(q\)-bridge。记

\[
w=\frac{p+1}{2}=qd,
\qquad
h=(R_4-1,K_4)=2d,
\qquad
p=2dq-1.
\tag{1}
\]

这里 \(h=2d\) 是 actual H4 carry 与 clean-carrier 条件共同给出的结论。原
\(q\)-word 写为

\[
x_q=Q_x\beta_x=E_xD,
\qquad
D=(M_4,Q_x)\beta_x\mid K_4,
\tag{2}
\]

并满足

\[
q x_q=(q-1)R_4+h,
\qquad
R_4\equiv1\pmod p,
\qquad
pR_4+1=4K_4.
\tag{3}
\]

完整超额分解已证明：除 terminal 与已严格的容量分派外，唯一的首层算术
stutter 是

\[
E_x\equiv q\pmod p.
\tag{4}
\]

本卡的关键观察是，(1)--(4) 全都发生在**第一条** actual \(q\)-word 上；它们不
需要 \(q_0=q/(q,b+1)\) 的取值，更不需要把 endpoint 先重放为 \(q_0\)-re-entry。

## 2. 与 \(q_0\) 无关的 source \(D\)-gate

在 (4) 下，将 (2)--(3) 模 \(p\) 约化，得

\[
q^2D\equiv q+2d-1\pmod p.
\tag{5}
\]

由 \(2dq=p+1\)，有 \(q^{-1}\equiv2d\pmod p\)。于是

\[
\begin{aligned}
D
&\equiv4d^2(q+2d-1)\\
&\equiv2d(4d^2-2d+1)
=:\delta_d
\pmod p.
\end{aligned}
\tag{6}
\]

另一方面，以 \(p\) 乘 (3) 并使用 \(D\mid K_4\)，有

\[
pqE_xD=4(q-1)K_4-(q-1)+ph,
\]

故

\[
\boxed{
D\mid ph-q+1
=(2d-1)\bigl((2d+1)q-1\bigr)=:A_d.}
\tag{7}
\]

又 \(q>1\) 给

\[
0<D\le A_d<2dp.
\tag{8}
\]

所以每个 actual first stutter 都满足精确的 source-only 门

\[
\boxed{
D\equiv\delta_d\pmod p,
\qquad D\mid A_d,
\qquad0<D<2dp.}
\tag{9}
\]

这正是此前以 \(q_0>1\) re-entry 为入口时得到的 \(D\)-残数门，但其推导没有
使用 \(q_0>1\)：若形式地令 \(q_0=1\)、\(\gamma=q\)、\(\xi=x_q\)，此前的
source identity 就退化为 (3)。因此不能把 (9) 人为限制在 \(q_0>1\) 子域。

## 3. phase/D 菜单的全域闭合

actual 19-phase H4 provenance 还给

\[
d\mid\lvert1536-a(p)\rvert\le1535.
\tag{10}
\]

以下三个既有闭包的输入都仅为 (1)、(9)、(10)、31 条 phase progression 及
actual H3-to-H4 carrier equality \(d=(w,M_4)\)。它们的证明和复现脚本均未读取
\(q_0\)、\(\gamma\)、\(t\)、endpoint payload、typed guard 或 re-entry admission。
因而可直接作用于本卡的 first-stutter source gate。

| source 区域 | (9) 的有限分派 | 已闭合的原因 |
|---|---|---|
| \(p\le\delta_d\) | \(2\le q\le4d^2-2d+1\)，逐一枚举相容 phase/D 候选 | 2,204 个 \(q\) 值的 4,475,827 个 \(D\) 候选均不整除 \(A_d\) |
| \(p>\delta_d,\ D>\delta_d\) | \(D=\delta_d+kp,\ A_d=\ell D\)，\(k\ell\le2d-1\) | exact phase screen 的有限三元组菜单为空 |
| \(p>\delta_d,\ D=\delta_d\) | \(d\equiv1\pmod3\) 立即矛盾；其余给 17 条 phase rays | H3 terminal-first 删除 7 条、17-adic exact carrier 删除 3 条、complete-excess valuation 删除余下 7 条 |

第三行的最后七条使用的只是 actual carrier equality 和 H3 maximal completion：选取
\(\ell\mid d\) 后，\(\ell\) 在 \(w,c_3,q_3\) 的赋值均为一次、却不在 \(M_3\)
中，故 exact completion 必把 \(\ell\) 从 \(M_4\) 移出，与 \(\ell\mid d=(w,M_4)\)
矛盾。该论证同样没有 \(q_0\) 条件。

三行穷尽 (9)，从而 (4) 不可能：

\[
\boxed{
\text{actual clean }q\text{-bridge 不存在首层 }E_x\equiv q\pmod p
\text{ capacity stutter}.}
\tag{11}
\]

## 4. 对两类后继的影响

\(q_0=1\) double-\(q\) bridge、其 second/third carrier，和 \(q_0>1\) raw
re-entry，都是由首层 (4) 的不同分派产生。式 (11) 因而在它们的共同 parent 处关闭：

\[
\boxed{
q_0=1\text{ 与 }q_0>1\text{ 的上述 raw maps 在 actual 19-phase H4 域都无首层入口}.}
\tag{12}
\]

这不使那些条件性整数正规形失效；它们仍可用于核对蕴含或研究脱离本 actual H4
scope 的图表。它也不声称 every clean endpoint 已经形成递归边。由首层 complete-excess
分解，只能得到下列较窄的算术结论：每个 actual nonterminal endpoint 都落在

\[
c_q\le p-2.
\tag{13}
\]

要把 (13) 升格为 Type I/II 短证书或严格可提升宏，仍须逐项通过 terminal-first、typed
reclassification、source/path、single-side/atomic payload 与 serializer guards。
因此本卡关闭的是一个真实的 arithmetic source residual，不替代全局选择器的语义与提升义务。

## 5. 验证与范围

本卡没有重新运行历史的 4,475,827-candidate low-\(p\) screen。它复用三个已冻结的
有限 source receipts，并新增可人工检查的 scope audit：上面 (5)--(9) 在 first
\(q\)-word 内直接推得，三个分派所需的变量列表不含 \(q_0\)。相应的既有定向复现为：

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_nonminimal_d_lift_finite_phase_exclusion.py --verify
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_minimal_d_ray_complete_excess_valuation_pruning.py --verify
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_low_p_finite_source_gate.py --verify
```

这些命令分别验证三个冻结有限 receipt；它们不是对素数区间、分母或 Reach graph 的扫描。
