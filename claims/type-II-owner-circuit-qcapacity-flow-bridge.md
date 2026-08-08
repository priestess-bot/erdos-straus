---
kind: claim
claim_id: type-II-owner-circuit-qcapacity-flow-bridge
title: Type II owner 相容回路族的 q 进需求—物理容量流桥
statement: 对一族已通过 SNF/CRT/power-closed 门的 owner 依赖回路，把每个回路系数展开为带来源的 q 层需求 token，并把 token 的可用 q 槽和实际复用预算放入有限流网络。最大流不足时给出精确 CIRCUIT_Q_CAPACITY_DEFICIT；满流后再检查独立 Fourier 角色的源列秩，秩不足给出对偶见证，秩通过则得到可进入 F/G/Kneser 的 source-complete 容量证书。该桥用实际流取代未经证明的 pair-energy reuse 常数。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-owner-joint-circuit-arithmetic-lift-trichotomy
  - type-II-kernel-fourier-pair-energy-qheight-demand
  - type-II-owner-projection-physical-capacity-flow-gate
  - type-II-rado-linear-rank-hall-capacity-bridge
  - type-I-fg-fourier-phase-owner-capacity-bridge
topics:
  - type-II
  - owner-weight
  - source-circuit
  - q-adic
  - physical-capacity
  - max-flow
  - min-cut
  - Fourier
  - F/G
  - Rado
  - constructive-certificate
  - proof-program
sources:
  - claim: type-II-owner-joint-circuit-arithmetic-lift-trichotomy
    role: compatible-circuit-input
  - claim: type-II-kernel-fourier-pair-energy-qheight-demand
    role: Fourier-pair-demand-lower-bound
  - claim: type-II-owner-projection-physical-capacity-flow-gate
    role: physical-q-slot-flow
  - claim: type-II-rado-linear-rank-hall-capacity-bridge
    role: post-flow-source-rank
  - claim: type-I-fg-fourier-phase-owner-capacity-bridge
    role: F-G-owner-interface
  - reproduction: reproductions/type_ii_owner_circuit_qcapacity_flow.py
    role: reuse-collision-and-source-rank-controls
visibility: public
last_checked: '2026-08-09'
---

# Type II owner 相容回路族的 q 进需求—物理容量流桥

## 1. 回路需求载荷

固定一族已经通过回路—SNF—算术三分的相容回路
\[
\mathcal C=\{C_1,\ldots,C_m\}.
\]
每个回路的系数和来源 q-height 只允许产生 power-closed 需求 token：
\[
\mathcal Q(C_a)=
\{(a,q,j,\sigma):1\le j\le d_{a,q},\;
\text{该层由回路 }C_a\text{ 的合法来源支付}\}.
\tag{1}
\]
\(d_{a,q}\) 不由 Fourier 幅度直接赋值，而由整数来源合同和 shared-q ledger
核验。对回路子族 \(U\subseteq\mathcal C\)，总需求为
\[
D_q(U)=\sum_{C_a\in U}|\mathcal Q(C_a)|.
\tag{2}
\]
若同一回路的多个相位边只产生同一独立 primary 方向，先在角色空间去重；(2)
只统计真实 q 层需求，不统计 pair-energy 的重复边数。

每个需求 token \(x\in\mathcal Q(C_a)\) 有一个合法物理 q 槽邻域
\(\mathcal S(x)\)，槽 \(s=(q,j,\text{physical occurrence})\) 有复用容量 \(b(s)\)。
来源标签、owner 和 source-SNF 失败的 token 不进入 \(\mathcal S(x)\)。

## 2. 精确 q 流

在网络
\[
\text{source}\to x\to s\to\text{sink}
\tag{3}
\]
中，source—token 容量为 1，token—槽边只在
\(s\in\mathcal S(x)\) 时存在，槽—sink 容量为 \(b(s)\)。令
\(\mathsf F_q(U)\) 为该网络最大整数流。

定义
\[
\boxed{\mathrm{CIRCUIT\_Q\_FLOW\_PASS}(U)
\iff
\mathsf F_q(U)=D_q(U).}
\tag{4}
\]

最大流—最小割给出精确分派：

* 若
  \[
  \boxed{\mathsf F_q(U)<D_q(U),}
  \tag{5}
  \]
  输出
  \[
  \mathrm{CIRCUIT\_Q\_CAPACITY\_DEFICIT}
  =(U,\mathsf F_q(U),D_q(U),\text{minimum cut}).
  \tag{6}
  \]
  这是真实 q 槽/owner 复用缺口；不能把同一 q 层在不同回路下重复收费。
* 若所有 \(U\) 均满流，保存每个 token 的实际槽分配和来源标签；这才允许把
  回路族送入 F/G q-prefix、Kneser 或下一层 source-rank 检查。

(6) 不依赖一个预先假设的 \(R_{\rm reuse}\)；所有复用冲突都在当前有限图中由最小割
显示。

## 3. 满流后的角色秩门

令每个相容回路或其 Fourier 角色在当前 \(\ell\)-初等商中的独立需求向量为
\(d_a\)，去掉线性重复后取独立子集 \(U_\ell\)。满流分配产生的 q 槽 source
columns 记为 \(v_s\)。对请求子集 \(W\subseteq U_\ell\)，定义
\[
\rho_q(W)=\operatorname{rank}_{\mathbb F_\ell}
\{v_s:s\text{ 可服务 }W\}.
\tag{7}
\]

若某个 \(W\) 满足
\[
\rho_q(W)<|W|,
\tag{8}
\]
输出
\[
\mathrm{CIRCUIT\_SOURCE\_RANK\_DEFICIT}
=(W,\rho_q(W),|W|,\lambda_W),
\tag{9}
\]
其中 \(\lambda_W\) 是湮灭可用 source columns 的规范对偶。若所有 Rado 条件通过，
则得到
\[
\mathrm{CIRCUIT\_SOURCE\_COMPLETE\_CAPACITY\_CERT}
=(\mathcal C,\text{q-token assignment},\text{independent source basis}).
\tag{10}
\]
(10) 只证明回路族已经支付了真实 q 层和独立 source 方向；随后仍须检查
E4 Type II、F/G owner 相位或稳定子/Kneser 终端。

## 4. 与 Fourier 能量的严格接口

相容角色的 pair-energy 恒等式可以提供候选关系边数量下界，但不能直接替代
\(\mathcal Q(C_a)\)。正确顺序是：

1. 用回路—SNF 三分确认哪些 Fourier 回路真实相容；
2. 用来源 q-height 产生每个回路的有限 token 载荷 \(\mathcal Q(C_a)\)；
3. 用 (3) 的最大流检查 q 槽复用；
4. 用 (7)--(10) 检查独立角色秩；
5. 通过后才把分配送入 F/G 紧链、Kneser 活跃容量或 Type II 目标纤维。

若相容回路族的流缺口释放一个已验证的 \(D'<D\) source-switch，则沿回路三分
输出严格递降；若没有该映射，(6) 只作为 q 容量负证书，不能自动写成递降。

## 5. 穷尽性证明

网络 (3) 是有限整数容量网络，故 (4) 与满分配等价；最大流—最小割定理给出
(5)--(6)。满流后，所有 q token 已由真实物理槽和预算支付；在固定 \(\ell\)-商中，
Rado 独立代表定理给出 (8)--(10) 的秩二分。pair-energy 仅用于生成候选回路，不参与
流的容量计数，因此重复边不会改变证明。最后按算术三分的直接、严格 source-switch
和 Fourier 后继检查，得到完整的固定回路族 typed 出口。证毕。

## 6. 构造性控制

### \(p=5113\)：不同 q 槽满流并直接终端

两个需求 token 分别允许槽 \(q=17\) 和 \(q=7\)，每槽容量为 1；最大流和需求
均为 2，source columns 独立，且回路算术因子 \(17\cdot7\equiv-1\pmod4\)，
输出 Type II 短证书。

### 重复 q 的真实缺口

两个相容回路 token 都只能使用同一个物理 \(q=5\) 槽，容量为 1。虽然 pair-energy
可能给出两个关系边，网络最大流只有 1，输出 (6)，不把两个回路重复收费。

### 满流但源秩不足

两个 token 使用不同物理槽且最大流为 2，但两槽在 \(\ell\)-初等商给出同一个
source column；(8) 输出 source-rank deficit，而不是 Fourier 容量通过。

## 研究边界

该桥把相容回路族的 q-height 需求和真实物理槽复用精确连接起来，消除了
\(R_{\rm reuse}\) 未知时从 pair-energy 到全局容量的跳步。它仍不证明任意核心素数的
相容回路族一定产生满流或严格递降；下一步必须把 (6)、(9) 的负证书接入
source-column escape、Type I/F/G 终端或可提升良基下降。
