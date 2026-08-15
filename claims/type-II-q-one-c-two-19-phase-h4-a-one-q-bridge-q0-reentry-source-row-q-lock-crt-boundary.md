---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-source-row-q-lock-crt-boundary
title: H4 q0 re-entry 的完整 source-row、unitary q-lock 与 p-residual CRT 边界
statement: >-
  在 actual H4 q0>1 p-free re-entry 的 source normal form 中，令
  p=2dq-1、h=2d、F=gamma+pt、xi=FD、D|K4、
  ell=(ph-q+1)/D，且 q=gamma q0。完整 source identity 与 4K4=pR4+1
  等价地强制 t 落在唯一的 source-row 剩余类
  t=t_src (mod 4(q-1))，其中
  t_src=p^(-1)[ell(p gamma q0^2)^(-1)-gamma] (mod 4(q-1)).
  若 rho||q 是任意 q-lock unitary allocation，则 t 也唯一落在一个类
  t=t_rho (mod q)。对任意 theta (mod p)，三条条件
  t=theta (mod p)、t=t_rho (mod q)、t=t_src (mod 4(q-1)) 由 CRT 唯一合并为
  一个模 4pq(q-1) 的正类。特别地，q-bridge 的 p-free 与 regeneration 的
  p-residual classes 不能与完整 source row 或 q-lock 发生纯同余矛盾。在 large-p
  minimal D=2d(4d^2-2d+1) 分支，q-lock 的第二根简化为
  t=gamma-(4d^2-2d+1)^(-1) (mod q/rho)；因此这张 CRT 边界不会继续删去
  pre-H3 的 17 条 necessary phase rays；独立的 H3 terminal-first 剪枝随后删去其中
  7 条，17-adic exact-carrier 剪枝再删去 3 条，complete-excess valuation 剪枝关闭余下 7 条。一个 p=12409,d=5,q=1241 的静态 source-row
  控制在 gamma in {1,17,73}、全部四个 unitary rho 与两条 raw residual
  class 下均给出正、primitive、p-free endpoint；17 条 ray 中三个首项素数亦有
  相同 gamma=1,rho=q 的静态控制。这些控制不构造 actual H4 predecessor、
  complete-excess maximality、top E_zeta 或 typed/atomic/persistent receipt。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-d-residue-gate
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-pfree-capacity-map
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-nonminimal-d-lift-finite-phase-exclusion
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-stutter-a-coordinate-transduction
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - q0-reentry
  - source-provenance
  - unitary-divisor
  - q-lock
  - chinese-remainder-theorem
  - capacity-transduction
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-d-residue-gate
    role: actual-source-normal-form-D-divisibility-and-h-equals-2d
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-pfree-capacity-map
    role: unitary-q-lock-signature-and-reentry-capacity-boundary
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-nonminimal-d-lift-finite-phase-exclusion
    role: minimal-D-identity-and-seventeen-phase-rays
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-stutter-a-coordinate-transduction
    role: raw-p-free-and-regeneration-t-residual-classes
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_source_row_q_lock_crt.py
    role: exact-source-row-crt-and-static-ray-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 \(q_0\) re-entry 的完整 source-row CRT 边界

## 1. 不能丢掉 \(D\mid K_4\) 的整行等式

保留 actual \(q_0>1\) p-free re-entry 的记号：

\[
p=2dq-1,
\qquad h=2d,
\qquad q=\gamma q_0,
\qquad F=\gamma+pt,
\qquad \xi=FD.
\tag{1}
\]

其中 \(D\mid K_4\)、\((D,q)=1\)，并且

\[
(q-1)R_4=\gamma q_0^2\xi-2d,
\qquad 4K_4=pR_4+1.
\tag{2}
\]

令

\[
A:=ph-q+1=2dp-q+1=\ell D.
\tag{3}
\]

此前只从 \(D\mid K_4\) 读取了 \(D\mid A\)。但将 (2) 的两式合并而不丢弃
商，得到完整恒等式

\[
\begin{aligned}
(q-1)(pR_4+1)
&=p\bigl(\gamma q_0^2FD-2d\bigr)+q-1\\
&=D\bigl(p\gamma q_0^2F-\ell\bigr),
\end{aligned}
\tag{4}
\]

故

\[
\boxed{
p\gamma q_0^2F-\ell
=4(q-1)\frac{K_4}{D}.
}
\tag{5}
\]

这一步使用 \(D\mid K_4\)，不是仅把 (3) 当作一个静态 divisor menu。

因为 \(q\) 为奇数，\(\gamma,q_0\mid q\)，而
\(0<q-1<p\)，故

\[
\bigl(p\gamma q_0^2,4(q-1)\bigr)=1.
\tag{6}
\]

代入 \(F=\gamma+pt\)，(5) 给出唯一的 source-row 类

\[
\boxed{
t\equiv t_{\rm src}:=
p^{-1}\left[\ell\bigl(p\gamma q_0^2\bigr)^{-1}-\gamma\right]
\pmod {4(q-1)}.
}
\tag{7}
\]

这里两个逆元都在模 \(4(q-1)\) 下取。反向地，取任意正的 (7) 代表并定义

\[
K_4=D\frac{p\gamma q_0^2F-\ell}{4(q-1)},
\qquad R_4=\frac{4K_4-1}{p},
\tag{8}
\]

则 (2) 的两个整数恒等式同时恢复。事实上，(7) 先保证 \(K_4\) 为整数。又模
\(p\) 有

\[
4K_4
\equiv-\frac{D\ell}{q-1}
=-\frac{A}{q-1}
\equiv1\pmod p,
\tag{8a}
\]

因为 \(A=2dp-q+1\equiv-(q-1)\pmod p\)，故 (8) 的 \(R_4\) 为整数。最后

\[
\begin{aligned}
(q-1)(4K_4-1)
&=D\bigl(p\gamma q_0^2F-\ell\bigr)-(q-1)\\
&=p\bigl(\gamma q_0^2FD-2d\bigr),
\end{aligned}
\]

除以 \(p\) 即恢复 (2)。

## 2. source row 与 q-lock 的精确 CRT 合并

令 \(\rho\parallel q\) 是 q-lock 的 unitary allocation。既有 q-lock signature 给出唯一
\(t_\rho\pmod q\)：

\[
t_\rho\equiv\gamma\pmod\rho,
\qquad
t_\rho\equiv\gamma-2dD^{-1}\pmod{q/\rho}.
\tag{9}
\]

又

\[
(p,q)=1,
\qquad (p,4(q-1))=1,
\qquad(q,4(q-1))=1.
\tag{10}
\]

因此对**任意** \(\theta\in\mathbb Z/p\mathbb Z\)，下列三条必要条件总有唯一共同解：

\[
\boxed{
\begin{aligned}
t&\equiv\theta&&\pmod p,\\
t&\equiv t_\rho&&\pmod q,\\
t&\equiv t_{\rm src}&&\pmod {4(q-1)}.
\end{aligned}
}
\tag{11}
\]

其模数为

\[
\boxed{4pq(q-1).}
\tag{12}
\]

特别地，原 q-bridge 中的两条正残余

\[
\theta\equiv\gamma(b+1)\pmod p,
\qquad
\theta\equiv\gamma(b+2)\pmod p
\tag{13}
\]

都不能仅因 (5) 或 q-lock 而被排除。这里并未声称所构造的 \(t\) 自动满足 endpoint
互素、maximal complete-excess、顶容量 \(E_\zeta\)、或任何 typed/atomic/persistent
合同；结论只是这些已知的 \(t\)-同余条件不存在矛盾。

## 3. 最小 \(D\) 射线没有额外的 q-lock 同余筛

在 large-\(p\) minimal 分支，置

\[
S_d=4d^2-2d+1,
\qquad D=2dS_d.
\tag{14}
\]

因为 \((D,q)=1\)，(9) 的第二根可化为

\[
\boxed{
t\equiv\gamma-S_d^{-1}\pmod{q/\rho}.
}
\tag{15}
\]

此外 (3) 还自动给出

\[
D\mid(2d-1)((2d+1)q-1),
\qquad (D,2d-1)=1,
\tag{16}
\]

所以 \(D\mid(2d+1)q-1\)。若一个素数同时整除 \(S_d\) 与 \(q-1\)，则它整除
\((2d+1)q-1\equiv2d\)；但 \((S_d,2d)=1\)，矛盾。故

\[
\boxed{(S_d,q-1)=1.}
\tag{17}
\]

这不是新的 phase pruning：它恰保证 (7)、(15) 中需要的逆元存在。因而对 pre-H3
17-ray supermenu 上任何通过此前 \(D\)-gate 的实际素数点，(11) 在 \(t\) 的同余层面
仍与每个 unitary allocation 和每条 \(p\)-residual class 兼容。后继的
[H3 terminal-first 剪枝](type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-minimal-d-ray-h3-terminal-pruning.md)
独立地删去其中 7 条；后继的
[17-adic exact-carrier 剪枝](type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-minimal-d-ray-17-adic-carrier-pruning.md)
再删去三条 \(d=17\) rays；后继的
[large-\(p\) complete-excess 关闭](type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-large-p-minimal-d-closure.md)
删除余下七条。继续只在 \(t\) 的同余层添加筛子不会产生这一 carrier 结论。

## 4. 静态控制与准确边界

回执构造一个完整的静态 source-row family：

\[
p=12409,\quad d=5,\quad q=1241=17\cdot73,\quad
D=910,\quad\ell=135.
\tag{18}
\]

取 \(\gamma\in\{1,17,73\}\)、\(b=2\gamma-1\)，以及每个
\(\rho\in\{1,17,73,1241\}\)，对 (13) 的两个 \(\theta\) 分别用 (11) 取正代表。
所得 24 个控制均精确满足：

\[
4K_4=pR_4+1,\quad D\mid K_4,\quad
(q-1)R_4=\gamma q_0^2\xi-2d,
\tag{19}
\]

并且端点 \(\xi,\zeta=R_4-\xi\) 为正、互素、p-free，且 q 的完整素数幂恰按
\(\rho,q/\rho\) 分配。另有 pre-H3 17 条 phase ray 中三个首项素数的
\(\gamma=1,\rho=q\) 控制，共六条（两条 \(\theta\)）满足相同的静态整数条件。

这些是对“source row + q-lock + raw terminal class 自身矛盾”这一设想的严格反例，
不是 actual H4 receipt：没有为它们构造 \(M_4,Q_x,\beta_x\) 的 maximal complete-excess
证书、top \(E_\zeta\)，也没有 H3-to-H4 prefix、terminal-first、typed、atomic 或 E1--E5
回执。事实上，exact-prefix 审计已表明这三个素数首项都不成为 actual re-entry：两条在
H3 terminal-first 截断，另一条有 \(\bigl((p+1)/2,M_4\bigr)\ne d\)。随后 exact carrier
equality 还全射线地关闭三条 \(d=17\) residual；complete-excess valuation 随后关闭全部
large-\(p\) rays。因此当前只剩有限 \(p\le\delta_d\) 区域的 payload 条件或 q-lock target
完整 root/solution-lift 合同，而不能来自新的 \(t\) 同余筛。

## 5. 定向复现

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_source_row_q_lock_crt.py --verify
```

回执只重建 (5)--(12) 的 CRT source row、(18) 的 24 个 composite-q 静态控制，以及
pre-H3 17 rays 中三个 prime first-point 的六个静态控制；不搜索 prime ranges、分母、
Reach graph 或 H4 predecessor history。
