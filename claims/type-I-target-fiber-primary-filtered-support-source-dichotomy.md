---
kind: claim
claim_id: type-I-target-fiber-primary-filtered-support-source-dichotomy
title: q-primary 过滤 Fourier 缺口的支撑对偶—源差分二分
statement: 在目标纤维 q-primary 过滤密度桥的 Fourier 缺口分支中，令 S 为盒像、D_B 为 S 的差分子群，并选择规范 q-primary 角色 chi。若 chi 在 D_B 上平凡，则 chi 因而湮灭盒支撑差分，给出目标与支撑陪集之间的显式对偶分离；若 chi 在 D_B 上非平凡，则 D_B/qD_B 有非零初等 q 商，真实源差分格必须支付至少一个 SOURCE_DIFFERENCE_Q_DEMAND(q) 方向。两支互斥且均可计算；该二分不把 q 角色阶自动升级为整数 q-height。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-target-fiber-primary-filtered-density-fourier-relay
  - type-I-fg-fourier-to-type-II-role-demand-bridge
  - type-I-fourier-qprimary-phase-lift-capacity-dichotomy
topics:
  - type-I
  - F-state
  - G-state
  - target-fiber
  - q-primary
  - Fourier
  - support
  - source-difference
  - source-rank
  - dual-separation
  - lift-boundary
  - proof-program
sources:
  - claim: type-I-target-fiber-primary-filtered-density-fourier-relay
    role: filtered-Fourier-character-input
  - claim: type-I-fg-fourier-to-type-II-role-demand-bridge
    role: source-rank-routing
  - claim: type-I-fourier-qprimary-phase-lift-capacity-dichotomy
    role: independent-integer-lift-gate
  - reproduction: reproductions/type_i_target_fiber_primary_filtered_support_source_dichotomy.py
    role: support-annihilator-and-source-demand-controls
visibility: public
last_checked: '2026-08-09'
---

# q-primary 过滤 Fourier 缺口的支撑对偶—源差分二分

## 输入

令 H 为有限阿贝尔群，令

    phi: Z^r -> H,
    B = product_i [-nu_i,nu_i] intersect Z^r,
    S = phi(B),
    D_B = <s s'^(-1) : s,s' in S>.

令 y in H 是目标，X <= widehat(H) 是一个 q-primary 角色子群，K=X^perp，
m=|X|，T=2^r，V=|B|。假设目标纤维 q-primary 过滤密度桥已经进入 Fourier
缺口分支：

    N_y <= T,
    C_(y,K) <= T,
    V > m T.

从 X 中按既定规范选出非平凡角色 chi，使

    -Re(conj(chi(y)) Bhat(chi))
    >= (V - m C_(y,K))/(m - 1)
    > 0.                                                   (1)

定义盒指数差分格

    L_B = <z - z' : z,z' in B> <= Z^r,
    Lambda = ker(phi).

显然 D_B=phi(L_B)。记 D_(B,q) 为 D_B 的 q-Sylow 子群，并定义

    r_q(B) = dim_Fq(D_(B,q) / q D_(B,q)).

## 二分定理

在上述输入下，以下两个分支互斥且穷尽：

### A. 支撑湮灭与对偶分离

若 chi 在 D_B 上平凡，则存在 c in the unit circle，使

    chi(phi(z)) = c  for every z in B.

因此 chi 因子化为 H/D_B 上的角色，并且盒支撑落在单一陪集

    S subseteq {h in H : chi(h)=c}.

式 (1) 进一步给出

    V Re(conj(chi(y)) c)
    <= -(V - m C_(y,K))/(m - 1).                           (2)

右端严格为负，所以 chi(y) != c，目标不在支撑陪集中。选择器输出

    SUPPORT_ANNIHILATOR_SEPARATION
    (q, ord(chi), chi mod D_B, c, y, score).

这是一条有限群的 G 型支撑—目标对偶分离证书；它不产生源 q 秩需求。

### B. 源差分 q 初等需求

若 chi 在 D_B 上非平凡，则

    r_q(B) >= 1.                                           (3)

并且

    L_B / (L_B intersect Lambda + q L_B)
        isomorphic to D_B / q D_B

含有非零 F_q 商。因此任何保持盒像差分的真实 source relation 或源差分载体，
至少必须支付一个独立 q 方向。选择器输出

    SOURCE_DIFFERENCE_Q_DEMAND(q, r_q(B) >= 1,
                               chi restricted to D_B).

该请求可以送入已有的 F/G 角色—源秩桥、q-primary 相位提升和跨状态容量账本；
但在独立 source-map、CRT/SNF 和范围条件通过之前，不能把它写成整数 Type II
高度或完整短证书。

## 证明

若 chi 在 D_B 上平凡，对任意 z,z' in B 都有

    chi(phi(z)) chi(phi(z'))^(-1)
    = chi(phi(z-z')) = 1.

故 chi(phi(z)) 是与 z 无关的常数 c，且 chi 对 D_B 平凡，所以它因子化到
H/D_B。另一方面，盒 Fourier 和为

    Bhat(chi) = V c.

将它代入 (1) 得 (2)。右端严格为负，故 chi(y) 与 c 不同；由于整个支撑
陪集的 chi 值都等于 c，得到目标—支撑对偶分离。

若 chi 在 D_B 上非平凡，则 chi(D_B) 是一个非平凡有限 q 群。因而 D_B 的
q-Sylow 子群非平凡，有限 q 群的 Frattini 商 D_(B,q)/qD_(B,q) 非零，得到
(3)。

映射 phi 限制到 L_B 后满射到 D_B。由 phi(q L_B)=q D_B，第一同构定理给出

    L_B / (L_B intersect Lambda + q L_B)
    isomorphic to D_B / q D_B.

所以源差分格确实包含至少一个独立 q 方向。两支分别由 chi|D_B 是否恒等
唯一决定，故互斥且穷尽。证毕。

## 为什么这是过滤缺口的必要下一门

上一条过滤密度桥只保证存在一个 X 内的负实 Fourier 缺口；若直接把角色阶
q^e 当作整数 q-height，会混淆固定层锚点相位、支撑分离和真实源关系。本二分
先检查整个盒像的差分群：

* A 支把缺口解释为支撑陪集与目标的有限对偶分离，不虚构 Type II 源需求；
* B 支把缺口压缩成至少一个独立 q 源差分请求，再交给 source-label 相位提升和
  跨状态容量，而不是按角色阶重复收费。

这里使用整个盒像 S，而不是仅使用精确目标纤维的去重支撑。原因是 Fourier
缺口的和遍历整个盒；若只检查目标纤维差分，可能错误地把一个由盒外部支撑
变化产生的 q 方向标成锚点相位。

## 精确控制

| 控制 | H、生成元 | 盒预算 | y | V、T、m | 盒奇偶支撑 | 输出 |
|---|---|---:|---:|---:|---|---|
| 支撑湮灭 | C_4, (2,1) | (4,0) | 1 | (9,4,2) | 全为偶 | SUPPORT_ANNIHILATOR_SEPARATION |
| 源差分请求 | C_6, (1) | (2) | 1 | (5,2,2) | 奇偶均有 | SOURCE_DIFFERENCE_Q_DEMAND |

第一个控制中盒像只由 2 的倍数组成，q=2 角色 chi(x)=(-1)^x 在 D_B
上平凡，目标 1 的角色值与支撑的角色值相反，故 Fourier 分数为 -9。第二个
控制中盒像含有相邻 residue，D_B 的 q-Sylow 为 C_2，故 r_2(B)=1；其
规范角色分数为 -1，恰为 (1) 的下界。

## 研究边界

本二分证明了过滤 Fourier 缺口要么是支撑对偶分离，要么至少产生一个真实的
有限源差分 q 请求；它仍不证明该请求有整数标签提升，也不保证跨 F/G 状态
容量超载。后续必须对 B 支的请求运行 phase-lift / Hall / CRT-SNF 门：

    local lift -> assignment capacity -> E1--E5
                  or strict liftable descent.

若 source-map 未封闭，合法回执是 SOURCE_DIFFERENCE_SOURCE_UNCLOSED，而不是
“无解”或自动递降。

后续的活动坐标精化证明
\[
L_B=\bigoplus_{\nu_i>0}\mathbb Ze_i,\qquad
D_B=\langle g_i:\nu_i>0\rangle.
\]
所以规范 Type I 素因子盒的所有 \(\nu_i\ge1\) 时 \(D_B=H\)，本卡 A 支为空；
B 支若通过 elementary ambient extension，则活动源列已经 source-dominate
整个规范求值商。保留这些源的 filter-only 候选在 realization 前只得到候选饱和；
若它 independently realized 为 exact successor，剩余容量才精确为零。完整
no-go 见
[primary filter 的活动源差分饱和与 source-preserving successor 零容量](type-I-primary-filter-active-source-saturation-zero-successor-capacity.md)。

## 聚焦复现

~~~bash
python3 reproductions/type_i_target_fiber_primary_filtered_support_source_dichotomy.py --verify
~~~

脚本只验证两个控制的过滤缺口条件、实际 Fourier 分数、支撑奇偶湮灭和 q 初等
差分分支，不做历史扫描。
