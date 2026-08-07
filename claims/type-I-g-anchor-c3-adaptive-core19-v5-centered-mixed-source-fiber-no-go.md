---
kind: claim
claim_id: type-I-g-anchor-c3-adaptive-core19-v5-centered-mixed-source-fiber-no-go
title: v=5 C0/C1 的 centered mixed-source fiber no-go 与相对 q=19 边界
statement: 对 adaptive core-19 的 v=5 控制，C0=p-3 与 C1=19 的两条 raw receipt 共享 universal source orbit，但 q=5 move 需要 coordinate-frame swap，故不构成共同 ordered prefix。令 Phi0=13=C0^{-1}、Phi1=-C1^{-1} (mod R) 及 delta=Phi1 Phi0^{-1}=-C0C1^{-1}。delta 不属于 C_R(K)C_R(K)^{-1}，因而不可能存在任何 native centered fixed layer J=C_R(N), N|K，将两叶放入同一 row-to-anchor/source fiber。一个独立的 signed marked-tail finite nonnative groupoid 可以闭合两条声明 raw path 的 phase 并给出抽象非零 19-初等 relation；它不是完整参数纤维，故不产生可收费 source-rank demand、整数 q-height、容量、Type II 命中或递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-adaptive-core19-v5-dual-leaf-f19-control
  - type-I-g-anchor-c3-adaptive-core19-v5-signed-marked-source-groupoid
  - type-I-g-anchor-c3-adaptive-core19-c19-atomic-reset
  - type-I-fg-fourier-to-type-II-role-demand-bridge
  - type-II-source-fiber-elementary-rank-qheight-injection
topics:
  - type-I
  - c3
  - core19
  - raw-source
  - coordinate-frame
  - signed-tail
  - source-groupoid
  - fixed-layer
  - source-fiber
  - no-go
  - q-primary
  - source-rank
  - terminal-first
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_c3_adaptive_core19_v5_centered_mixed_source_fiber_no_go.py
    role: exact cyclic-component difference-box exclusion
visibility: public
last_checked: '2026-08-07'
---

# v=5 centered mixed-source fiber no-go

这张卡修正一个重要的 provenance 细节，并把“尚未构造 adapter”加强为一个针对
native centered-F adapter 的严格 no-go。

## 1. raw orbit 不是共同 ordered prefix

两条 leaf 有相同 universal \(p\)-edge，均到达 \((1,R-1,1)\)。但 C0 路径随后先将
坐标 frame 交换为 \((R-1,1,1)\)，在左侧执行 \(q=5\)；C1 路径则在原 frame 的
右侧执行 \(q=5\)。两步到达同一 destination，却不是同一个 ordered raw edge。

因此它们可以组成同一 **raw-orbit source** 控制，但任何试图把它们当作同一完整
ordered lineage 或不记录 frame morphism 的 adapter 都已经不合格。frame swap 必须在
`source_orbit_tree_digest` 中作为显式、非 raw 的 morphism 保存。

## 2. native centered adapter 的必要条件

在 v=5 写

\[
\Phi_0=13=C_0^{-1},\qquad
\Phi_1=4387621028405=-C_1^{-1}\pmod R,
\]

并令

\[
\delta=\Phi_1\Phi_0^{-1}
=-C_0C_1^{-1}
=5147016975629\pmod R.
\tag{1}
\]

假设存在一个 native row-to-anchor adapter，具有某个 centered layer
\(J=\mathcal C_R(N)\)、\(N\mid K\)、稳定子 \(P\)、锚点 \(\theta\)，并在商中满足

\[
\Phi_iP=\theta j_i^{-1}P,\qquad j_i\in J.\tag{2}
\]

因为 \(1\in J\)，有 \(P\subseteq J\)；又 \(JP=J\)。将 (2) 相除便得到

\[
\delta\in JJ^{-1}.
\tag{3}
\]

此外 \(N\mid K\) 意味着 \(J\subseteq\mathcal C_R(K)\)，所以 (3) 的必要条件为

\[
\delta\in\mathcal C_R(K)\mathcal C_R(K)^{-1}.
\tag{4}
\]

## 3. 一个常数规模的 exact exclusion

取素数分量

\[
q=171566399\mid R,\qquad g=7,\qquad \operatorname{ord}_q(g)=171566398.
\]

按 \(K\)-support 顺序

\[
(2,19,193,5351,66383,31641497801)
\]

的 \(g\)-离散对数为

\[
(34001298,46258077,7372596,134674827,6933472,171198251),
\]

而

\[
\log_g\delta=119416350\pmod {171566398}.
\tag{5}
\]

中心 box 的指数预算是 \((1,2,1,1,1,1)\)，故差 box 是

\[
[-2,2]\times[-4,4]\times[-2,2]^4.
\tag{6}
\]

它有 \(28125\) 个向量、\(24541\) 个不同的循环分量值，并且不含 (5)。于是 (4)
不成立；模 \(q\) 的反证立即推出模 \(R\) 的反证。

**定理。** v=5 的 C0/C1 pair 不可能进入任意 native centered fixed layer 的同一
row-to-anchor/source fiber。改变 \(N\)、\(P\) 或 \(\theta\) 都不能修复它。

## 4. 相对 q=19 合同与 nonnative 边界

令 \(\zeta=150\in U(191)\)，\(\eta(a)=a^{10}\pmod {191}\)。该点有

\[
\eta(-1)=1,\qquad
\eta(C_0)=\zeta^3,\qquad
\eta(C_1)=\zeta^{11},
\]

因此 \(\eta(\delta)=\zeta^{11}\ne1\)。
[signed marked-tail groupoid](type-I-g-anchor-c3-adaptive-core19-v5-signed-marked-source-groupoid.md)
已经在两条**声明的** raw path 上闭合了这个相对 phase，并构造了使两叶相等的抽象商。
它刻意没有完整 source universe、参数纤维或整数 lift，因而不能代入下面的容量合同。

为说明一个真正的 **non-native capacity adapter** 还必须满足什么，假设它给出有限
Abelian 商 \(\bar H=H/T\)、参数纤维映射 \(\pi\)、源映射
\(\phi:\mathbb Z^r\to\bar H\)，以及同一完整纤维内的坐标 \(z_0,z_1\)，满足

\[
\pi\phi(z_0)=\pi\phi(z_1),\qquad
\chi(\phi(z_0-z_1))=\zeta^{11},
\tag{7}
\]

其中 \(\chi\) 是在 \(\bar H\) 上存活的精确 \(19\)-阶角色。令

\[
L_\pi=\ker(\pi\circ\phi),\qquad A_\pi=\phi(L_\pi).
\]

则 \(v=\phi(z_0-z_1)\in A_\pi\)，且 \(\chi|_{A_\pi}\) 满射到
\(\mu_{19}\)。由于 \(19A_\pi\subseteq\ker\chi\)，有

\[
v\notin19A_\pi,\qquad
\boxed{\dim_{\mathbb F_{19}}(A_\pi/19A_\pi)\ge1.}
\tag{8}
\]

如果完整 source fiber 支撑包含两点，(8) 同时给
\(r_{19}(\Delta_Q)\ge1\)，所以只可产生最小的一项
`SOURCE_RANK_DEMAND(19,1)`。它并不证明这个秩恰为一，也不产生整数
\(19\)-height 或 Type II capacity。

有限 groupoid 已经提供两条 full raw lineage、frame morphism 和抽象 \(19\)-relation；
但它没有把它们放入同一**完整** source fiber。一个合格 capacity adapter 仍须提供
\(T,\pi,\phi,z_0,z_1\)、角色存活性、有限像的 SNF 行与
\(\sum_j a_jx_j\equiv11\pmod {19}\)、完整 source-table closure，以及随后独立的
整数 source-map 和 physical slot 回执。v=5 当前还被两个独立条件截断：F witness 为
`provided_unbounded_modular` 而非 canonical Fourier input，且已有 \((m,d)=(3,11)\)
terminal-first。
