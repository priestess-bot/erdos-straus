---
kind: claim
claim_id: type-I-stabilizer-aware-affine-phase-owner-capacity
title: 稳定子感知的仿射 q-primary phase-lift 与 owner 容量门
statement: 设 q^e 为 F/G Fourier 角色的 q-primary 阶，独立 source-map 将候选整数标签限制为 S={s0+h t:t∈Z}∩[L,U]，并给出相位条件 s=gamma (mod q^e)。若固定层稳定子为 P，source-map 还给出每个标签的物理 owner coset rho_P(s) in H/P 及槽容量 mu(c)，则 phase-lift 的 gcd/区间三分与 P-商 owner 容量三分可串联：无解时给出 PHASE_GCD_OBSTRUCTED 或 PHASE_INTERVAL_EMPTY；有解时容量至多 B_gamma=sum_{c in rho_P(L_gamma)} mu(c)，请求超过 B_gamma 给出严格 PHASE_OWNER_PROJECTION_HALL_DEFICIT；请求不超过该容量才允许继续 source-SNF、Rado/Kneser 或 E1--E5。若 rho_P 非单射，标签碰撞债务必须显式记录，不能按原始标签数收费。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-qprimary-phase-affine-label-gcd-lift
  - type-I-fixed-layer-stabilizer-defect-reduction
  - type-II-owner-projection-physical-capacity-flow-gate
  - type-I-fixed-layer-qprimary-representation-dual-capacity-selector
topics:
- type-I
- F-state
- G-state
- fixed-layer
- stabilizer
- q-primary
- phase-lift
- affine-source-map
- owner
- physical-capacity
- Hall
- SNF
- proof-program
sources:
  - claim: type-I-qprimary-phase-affine-label-gcd-lift
    role: gcd-interval-phase-lift
  - claim: type-I-fixed-layer-stabilizer-defect-reduction
    role: P-quotient
  - claim: type-II-owner-projection-physical-capacity-flow-gate
    role: physical-owner-flow
  - reproduction: reproductions/type_i_stabilizer_aware_affine_phase_owner_capacity.py
    role: phase-and-P-collision-controls
visibility: public
last_checked: '2026-08-09'
---

# 稳定子感知的仿射 q-primary phase-lift 与 owner 容量门

## 1. 输入

令 \(q\) 为素数、\(e\ge1\)、\(n=q^e\)，并令独立 source-map 给出候选标签进程

\[
\mathcal S=\{s_0+h t:t\in\mathbb Z\}\cap [L,U]\cap\mathbb Z,\qquad h>0.
\]

固定 Fourier q-primary 相位 \(\gamma\in\mathbb Z/n\mathbb Z\)，要求

\[
s\equiv\gamma\pmod n.
\tag{1}
\]

设固定层 \(J\) 的稳定子为 \(P\)，且 source-map 对每个 \(s\in\mathcal S\) 提供一个
物理 owner \(\theta(s)\in H\)。q-primary 角色在 \(P\) 上平凡，因此真正可见的 owner
是

\[
\rho_P(s)=\theta(s)P\in H/P.
\tag{2}
\]

允许进一步把 \(H/P\) 的 coset 投影到有限物理槽集 \(\mathcal C\)；下面把这一投影
仍记作 \(\rho_P\)。每个槽 \(c\) 有已经声明的整数容量 \(\mu(c)\)。

source-map 完备性是本门的输入。若某个合法标签没有 owner，必须输出
PHASE_OWNER_MAP_UNCLOSED，而不能由标签缺失反推相位无解。

## 2. 相位 lift 的精确三分

记

\[
g_0=\gcd(h,n),\qquad \Delta=(\gamma-s_0)\bmod n,\qquad
h_1=h/g_0,\qquad n_1=n/g_0.
\]

则：

1. 若 \(g_0\nmid\Delta\)，(1) 无解，输出
   PHASE_GCD_OBSTRUCTED；
2. 若 \(g_0\mid\Delta\)，当 \(n_1>1\) 时令
   \[
t_0\equiv(\Delta/g_0)h_1^{-1}\pmod{n_1},
\tag{3}
\]
   当 \(n_1=1\) 时令 \(t_0=0\)。所有整数解恰为 \(t=t_0+n_1 k\)；
3. 令
   \[
t_{\min}=\left\lceil\frac{L-s_0}{h}\right\rceil,\qquad
t_{\max}=\left\lfloor\frac{U-s_0}{h}\right\rfloor.
\]
   若不存在 \(k\) 使 \(t_{\min}\le t_0+n_1k\le t_{\max}\)，输出
   PHASE_INTERVAL_EMPTY；否则
   \[
\mathcal L_\gamma=\{s_0+h(t_0+n_1 k):
\lceil(t_{\min}-t_0)/n_1\rceil\le k\le
\lfloor(t_{\max}-t_0)/n_1\rfloor\}
\tag{4}
\]
   是全部 phase-lift 标签。

这一步是线性同余的必要充分判据，不使用 Fourier 幅度或物理容量假设。

## 3. P-商 owner 容量门

在 phase-lift 集非空且 owner map 完备时定义

\[
\Omega_\gamma=\{\rho_P(s):s\in\mathcal L_\gamma\},\qquad
B_\gamma=\sum_{c\in\Omega_\gamma}\mu(c),
\tag{5}
\]

以及标签碰撞债务

\[
D_\gamma=|\mathcal L_\gamma|-|\Omega_\gamma|.
\tag{6}
\]

对一组共享该相位进程、每条请求都允许使用 \(\Omega_\gamma\) 的 \(R\) 个独立 q
请求，有严格二分：

* 若 \(R>B_\gamma\)，输出
  \[
  \boxed{\mathrm{PHASE\_OWNER\_PROJECTION\_HALL\_DEFICIT}
  =(R,B_\gamma,R-B_\gamma,D_\gamma).}
  \tag{7}
  \]
  这是物理 owner 槽的真实容量缺口；即使 \(|\mathcal L_\gamma|\ge R\)，也不能
  用标签重数支付它。
* 若 \(R\le B_\gamma\)，输出 PHASE_OWNER_CAPACITY_PASS，并把具体槽表送入
  source-label SNF、Rado/Kneser 或 E1--E5。容量通过不是整数解提升本身。

更一般地，若请求 \(r\) 只有邻域 \(N(r)\subseteq\Omega_\gamma\)，则可行 owner 分配
当且仅当所有请求子集 \(U\) 满足带容量 Hall 条件

\[
\boxed{
|U|\le\sum_{c\in\bigcup_{r\in U}N(r)}\mu(c).}
\tag{8}
\]

因此 (7) 是全同邻域时的规范最小割；异构请求必须保存真正的最小 Hall 集，不能用
总标签数代替。

## 4. 证明

式 (3)--(4) 是线性同余 \(h t\equiv\Delta\pmod n\) 的标准解：可解当且仅当
\(g_0\mid\Delta\)，约去 \(g_0\) 后 \(h_1\) 在 \(\mathbb Z/n_1\mathbb Z\) 中可逆，
区间条件再给出 \(k\) 的整数范围。

若所有请求使用同一邻域 \(\Omega_\gamma\)，任意 assignment 至多使用每个物理槽
\(\mu(c)\) 次，所以请求数至多为 \(B_\gamma\)，得到 (7)；当 \(R\le B_\gamma\) 时，
把请求逐个连到所有槽，按槽容量发送流即可构造满流。一般邻域情形构造网络

\[
s\longrightarrow r\longrightarrow c\longrightarrow t,
\]

边容量分别为 \(1,1,\mu(c)\)。最大流—最小割定理给出 (8)。若两个不同标签满足
\(\rho_P(s)=\rho_P(s')\)，它们经过固定层稳定子后是同一个可见 owner 槽，故只能按
该槽的 \(\mu(c)\) 计数；这证明 \(D_\gamma\) 不能被当作额外容量。证毕。

## 5. 与统一选择器的分派

该门应接在固定层 q-primary Fourier 角色之后：

\[
\text{Fourier }(q^e,\gamma)
\longrightarrow
\text{gcd/interval phase lift}
\longrightarrow
\text{P-quotient owner projection}
\longrightarrow
\text{Hall/Rado or arithmetic lift}.
\]

回执顺序为：

1. source-map 未闭合：PHASE_OWNER_MAP_UNCLOSED；
2. \(g_0\nmid\Delta\)：PHASE_GCD_OBSTRUCTED；
3. 区间无解：PHASE_INTERVAL_EMPTY；
4. 有 lift 但 (7) 成立：PHASE_OWNER_PROJECTION_HALL_DEFICIT；
5. owner 容量通过：PHASE_OWNER_CAPACITY_PASS，继续 source-SNF/整数门。

前两类是相位/载体障碍，不是 Type II 容量；第四类是物理槽容量证书，不自动是
整数递降；只有后续 source-column annihilator、Type I/II 终端或 E1--E5 严格边通过，
才能升级统一选择器状态。

## 6. 研究边界

该定理首次把仿射 q-primary phase-lift 的精确 gcd/区间判据与固定层稳定子的物理
owner 去重接成同一条可计算门。它不假设所有 Fourier 角色都有 source-map，也不把
标签碰撞当成全局反例；未闭合 source-map 必须保留为独立状态。要推进全称选择器，
下一步是证明实际 F/G source-map 的完备性，或把 (7) 的物理最小割接到已闭合的
source-column annihilator、广义 \(2^j\) 终端或可提升良基递降。

聚焦复现命令：

    python3 reproductions/type_i_stabilizer_aware_affine_phase_owner_capacity.py --verify

