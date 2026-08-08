---
kind: claim
claim_id: type-I-raw-certified-q-layer-charge-key-nonreuse
title: raw 认证 q 层到唯一 charge key 的不重计合同
statement: 设一个 state-local raw-to-cofactor receipt 保留 raw digest、候选纤维 f、endpoint H 及 H|N_f=p+4s_f，并令 q^e||H、q 不整除 M_f=4D_*。同模数 self-binding b=s_f 或一个已经验证的 source-switch 先把它绑定为 candidate-fiber q 块；只有经独立 typed demand 和显式 owner map 注入 canonical (f,q,j) token，才可参与 Q-PREFIX。对同一 fiber realization、q 残数方向和 block lineage 的所有 provenance，token 并集只形成一个连续 q 幂块、至多一个初等 q 列及一次互斥的 Kneser/tower 价格；跨状态价格或 Type II 命中还须完整 FIBER_REALIZED。raw 深度、列秩和价格不可相加。v=5 的 actual H=7、f=(6303,11)、q=7 收据给 raw 深度 1，而 N_f 的候选高度为 2；block-only 模型中 {1,7} 的价格为 1，候选扩张 {1,7,49} 的价格为 2，后者替换前者而不产生第二个 q 方向或 1+1+2 的容量。该合同建立 provenance 到既有 q 账本的条件接口，不产生 Fourier demand、FIBER_REALIZED、slot 注入、Type II 命中或 selector edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-raw-factor-block-local-cofactor-provenance
  - type-I-g-anchor-c3-adaptive-core19-v5-carrier-subset-q19-prefix-obstruction
  - type-II-source-fiber-shared-q-ledger
  - type-II-source-fiber-elementary-rank-qheight-injection
  - type-II-q-layer-prefix-kneser-price-certificate
  - type-II-stabilizer-tower-weighted-defect-conservation
topics:
  - type-I
  - type-II
  - raw-source
  - factor-provenance
  - q-adic
  - source-fiber
  - charge-key
  - Kneser
  - stabilizer
  - nonreuse
  - capacity
  - terminal-preempted
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_raw_certified_q_layer_charge_key_nonreuse.py
    role: v=5 H=7 raw-source binding, q-block nesting, and one-charge-key accounting
visibility: public
last_checked: '2026-08-08'
---

# raw 认证 \(q\) 层到唯一 charge key 的不重计合同

已有的 shared-q、初等秩、前缀和稳定子塔卡都已禁止把同一 \(q\) 的深度、秩、
Kneser 价格彼此叠加。尚未显式写出的连接点是：一个 **actual raw endpoint** 的
因子 provenance 应如何进入这一套账本，而不把同一整数证据复制成多个容量来源。

本卡给出这个连接的最小条件合同。它不是 raw occurrence 到 Type II request 的完整
functor；在 owner map 和 source-map 未闭合时，结果仍只是一份 raw-certified incidence。

## 1. 两种标识和 raw q 原子

固定一个 state-local raw-to-cofactor receipt

\[
\mathcal I=(\mathsf S,\omega,H;f,N_f),
\qquad
f=(D_*,A),\quad s_f=AD_*,\quad M_f=4D_*,\quad N_f=p+4s_f,
\tag{1}
\]

其中 \(\mathsf S\) 是 state identity，\(\omega\) 是逐边 raw digest，且

\[
H\mid N_f,\qquad (H,M_f)=1.
\tag{2}
\]

令 \(q\) 为 \(H\) 的奇素因子，写

\[
e_{\rm raw}=v_q(H)\ge1,
\qquad q\nmid M_f.
\tag{3}
\]

raw 证据的身份与最终容量账本的身份必须分开：

\[
\begin{aligned}
\mathsf{prov}(\mathcal I,q)
  &=(\mathsf S,\omega,f,q),\\
\mathsf{direction}(f,q)
  &=(\mathsf{fiber\_realization\_digest},q\bmod M_f,
       \mathsf{block\_lineage\_id}),\\
\mathsf{charge}(f,q)
  &=(\mathsf{direction}(f,q),\mathsf{stabilizer\_snapshot}).
\end{aligned}
\tag{4}
\]

`price_mode` 是附在同一 `block_lineage_id` 上的互斥账本选择，只能是最终稳定子价格或
tower-insertion 关系之一，不能作为新的 charge key。不同 raw word 可以有不同的
\(\mathsf{prov}\)，却可以有同一个 \(\mathsf{direction}\)；不能因此把它们当成不同的
\(q\) 方向。

receipt 自身只给 occurrence-addressed raw 原子链

\[
\mathcal A_{\mathcal I,q}
=\{(\mathsf{prov}(\mathcal I,q),j):1\le j\le e_{\rm raw}\}.
\tag{5}
\]

它不自动是 request、slot 或 Kneser 块。

## 2. 三层准入门

首先是 **candidate-block binding**。它只需要 admissible \(f\)、(2)--(3)，以及同模数
self-binding \(D=D_*\)、\(b=s_f=DA\)，或一个已验证的 source-switch/CRT 等式。它证明
\(q^{e_{\rm raw}}\mid N_f\)，所以可以在 \(U(M_f)\) 中保留一个带 raw provenance 的候选
q 块；这一步不需要 target residue、\(B'>A\) 或 `FIBER_REALIZED`。

其次才是 **typed Q-PREFIX admission**。它要求一个独立生成的 typed demand、所需的
source-map/SNF/范围门，以及一个 owner map
   \[
   \alpha:\bigcup\mathcal A_{\mathcal I,q}
   \longrightarrow\{(\mathsf{charge}(f,q),j):j\ge1\},
   \tag{6}
   \]
   它在已使用原子上单射，且其像闭成前缀 \(\{1,\ldots,n_q\}\)。

最后，只有一个完整匹配或积块束要把价格计入跨状态 surplus、或要从目标残数回译
Type II 时，才要求 source label、\(B'>A\)、target residue 和 `FIBER_REALIZED`。这三层
不能倒置：block binding 不是 typed request，typed request 也不是 Type II hit。

若 (6) 缺失或其像有洞，输出 `RAW_Q_OWNER_UNCLOSED` 或
`Q_PREFIX_EDGE_OBSTRUCTED`；不得把 (5) 直接计为 source rank 或容量价格。
重叠的 raw factor subset 取 \(\operatorname{im}\alpha\) 的并集，绝不把各 receipt 的
指数相加。

## 3. 唯一 charge-key 不重计定理

**定理。** 假设 candidate-block binding 已闭合；若另有 typed Q-PREFIX admission，则
\(\alpha\) 满足 (6)。令

\[
n_q=\left|\operatorname{im}\alpha\right|.
\tag{7}
\]

则对一个固定 \(\mathsf{charge}(f,q)\)：

\[
\boxed{
 n_q\le d_f(q),\qquad
 \epsilon_{\ell,q}\le1,\qquad
 B_{f,q}(n_q)=\{1,u_q,\ldots,u_q^{n_q}\}
 \text{ 只出现一次},
}
\tag{8}

其中 \(u_q=q\bmod M_f\)，\(d_f(q)\) 是 shared-q ledger 的连续深度，
\(\epsilon_{\ell,q}\) 是这一个 q 残数方向在任一 \(\ell\)-初等关系商中所贡献的
边际列数。若该 q 块已进入一个有明确 \(H_f,T_f\) 的 realized product ledger，则最终
稳定子模式下唯一可记入群容量的 q 价格是

\[
\boxed{
 \kappa_{f,q}=\min\!\left(n_q,
     \operatorname{ord}_{H_f/T_f}(u_qT_f)-1\right),
 \qquad
 \rho_{f,q}=\kappa_{f,q}|T_f|.
}
\tag{9}

若同一 `block_lineage_id` 取 `price_mode=tower-insertion`，则记录插入时有限阶/fold
并进入稳定子塔；同一块不得在最终模式下再加 (9)。跨状态价格或 Type II 命中还须完整
`FIBER_REALIZED`。因此下面两个量都没有“额外 q 容量”的意义：

\[
e_{\rm raw}+\epsilon_{\ell,q}+\kappa_{f,q},
\qquad
e_{\rm raw}|T_f|+\epsilon_{\ell,q}|T_f|+\rho_{f,q}.
\tag{10}
\]

**证明。** 先考虑同模数 self-binding。由 (2)--(3)，
\(q^{e_{\rm raw}}\mid p+4b\)；又 \(s_f-b=0\)，所以 shared-q ledger 中该来源的
\(\ell_q(s_f)=e_{\rm raw}\)。因此 raw 原子只能提供已声明高度以内的来源层；若还
有别的来源，全部层仍先由共同账本压至 \(d_f(q)\)，给出 (8) 的第一项。

owner map 的单射和前缀闭合使已注册的层恰为 \(1,\ldots,n_q\)，所以它们压缩为一个
\(B_{f,q}(n_q)\)，而不是若干相同 q 的块。重复 q 无论有多少 provenance，都只保留
一个 \(u_qT\) 初等列，故 \(\epsilon_{\ell,q}\le1\)。最后，前缀—Kneser 定理和
稳定子塔定理分别给出 realized product ledger 中的 (9) 及 insertion/final 的互斥性；
若此账本或 `FIBER_REALIZED` 缺失，价格根本不能登记。故深度、列秩和价格是同一
charge key 的三个不同投影，不能相加。证毕。

一般的 source-switch 情形只需把 self-binding 的 \(s_f-b=0\) 替换为已经通过的
带来源 CRT/SNF 等式；没有这份等式时，本定理不允许注册任何 token。

## 4. v=5 的 actual raw 校准

使用唯一的一首边 raw-to-cofactor 正控制：

\[
\begin{aligned}
p&=1202376916441,&D_*=6303,&A&=11,\\
s_f&=69333,&M_f&=25212,\\
N_f&=1202377193773=7^2\cdot347\cdot70715591.
\end{aligned}
\tag{11}

actual raw word

\[
(0,p),(1,5),(1,5),(0,119092570771)
\tag{12}

到达 \(H=7\)。raw 首标签是 \(\lambda=5\)，但 charge prime 是

\[
q=7,\qquad e_{\rm raw}=v_7(H)=1,\qquad v_7(N_f)=2.
\tag{13}

所以 self-binding \(b=s_f\) 的来源高度应封顶为一层：

\[
\ell_7(s_f)=1,\qquad d^{\rm raw}_f(7)=1.
\tag{14}

在只放入这个 q 块的模型里，\(\operatorname{ord}_{U(25212)}(7)=10\)，而

\[
B^{\rm raw}=\{1,7\},\qquad
\operatorname{Stab}_{U(25212)}(B^{\rm raw})=\{1\},\qquad
\kappa^{\rm raw}=1.
\tag{15}

若另有一个独立、可审计的 amplification/source receipt 认证 candidate 的第二个
\(7\)-层，正确更新是

\[
B^{\rm cand}=\{1,7,7^2\}=\{1,7,49\},
\qquad
\operatorname{Stab}_{U(25212)}(B^{\rm cand})=\{1\},
\qquad
\kappa^{\rm cand}=2.
\tag{16}

这是同一 \(q\) 方向的扩长和替换：\(B^{\rm raw}\subset B^{\rm cand}\)，不是两个
独立 q 块，更不是 \(1+1+2\) 的三份可收费容量。两者都不含 \(-1\pmod {25212}\)。

## 5. 适用边界

这个正控制只完成了 raw provenance 到 single-q charge-key 的**条件性**接线：

* 它没有产生 F/G Fourier demand；因此 \(\epsilon_{\ell,7}\le1\) 是列数上界，
  不是已经存在的 rank demand；
* 它没有构造完整 `FIBER_REALIZED`、source-switch/SNF、request-to-token 或
  demand-to-slot 注入；
* v=5 本身已有 \((m,d)=(3,11)\) 的直接 Type II terminal，故这个 fixture 只作
  terminal-preempted accounting control；
* 真正推进选择器的下一项工作，是在一个未被 terminal-first 抢占的 F/G state 上构造
  (6)，或证明任何这类 owner map 必进入可提升的 source-switch/商递降分支。

窄复现：

~~~
python3 reproductions/type_i_raw_certified_q_layer_charge_key_nonreuse.py --verify
~~~
