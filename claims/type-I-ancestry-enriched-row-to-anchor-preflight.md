---
kind: claim
claim_id: type-I-ancestry-enriched-row-to-anchor-preflight
title: 有序谱系到锚定相位的富集 row-to-anchor 准入门
statement: 对一个预先声明、保留 ancestry digest 的 actual raw 谱系树，若每条边的 raw 因子 r、实际 gcd reduction g 与被追踪坐标满足 rg z_w=z_v (mod R)，且归一化相位 Phi_v=-z_v^(-1) 全部落在同一 F 固定层群 H 中，那么只有在预先固定的 q-coprime anchor theta、固定层商 bar_J=pi(J) 与商投影 pi 下满足 pi(Phi_v)=theta bar_j_v^(-1)、bar_j_v in bar_J_theta 时，Phi 才给出合法的 q-primary row-to-anchor 相位。其相位增量是 log psi(pi(rg))，不是自动的 raw-factor log psi(pi(r))。tree 内该增量可积；若合并不同 history，必须在保留平行边的底层无向多重图上验证完整 pi-holonomy。只有在 factor-local 分支另验 r,g in H 且同一 raw 因子上的 psi(pi(g)) 恒定时，富集增量才可降为 factor-local action；每条 psi(pi(g))=1 时才回到 canonical raw-factor action。该门仅验证 row-to-anchor 的 raw provenance；共同整数 affine law、物理表到 ancestry occurrence 的覆盖、carry、representation-demand 到 q-height 的有界碰撞映射、E4 解提升和 E5 良基下降仍是独立前提。p=73,R=79 的 F-C78 raw-root control 满足 J cap 73J=empty，严格说明有 F Fourier 与 raw edge 并不产生这种 assignment。
claim_status: established
proof_provenance: repository_derivation
review_status: independent_review
depends_on:
  - type-I-ordered-raw-lineage-normalized-phase-rigidity
  - type-I-anchored-affine-phase-tree-capacity
  - type-I-raw-factor-action-affine-preflight
  - type-I-f-target-involution-fourier-phase-collapse
  - type-I-f-c78-raw-root-fixture-p73-r79
topics:
  - type-I
  - F-state
  - raw-transition
  - ancestry
  - row-to-anchor
  - anchored-phase
  - q-primary
  - factor-action
  - capacity
  - proof-boundary
sources:
  - claim: type-I-ordered-raw-lineage-normalized-phase-rigidity
    role: normalized-phase-and-gcd-enriched-transport
  - claim: type-I-anchored-affine-phase-tree-capacity
    role: anchored-phase-capacity-contract
  - claim: type-I-raw-factor-action-affine-preflight
    role: factor-local-integrability-boundary
  - claim: type-I-f-c78-raw-root-fixture-p73-r79
    role: canonical-assignment-negative-control
visibility: public
last_checked: '2026-08-07'
---

# 有序谱系到锚定相位的富集 row-to-anchor 准入门

## 1. 目的与输入

这一门只回答一个狭窄问题：actual raw transcript 是否能够为一个已经固定的
F 型锚定相位表提供 `row_to_anchor_map` 的**来源语义**。它不从 raw 路径
制造锚点、角色、整数标签、carry 或递归边。

固定一个 F 图表的有限群数据

\[
H\le U(R),\qquad P=\operatorname{Stab}_H(J),\qquad
\bar H=H/P,\qquad \pi:H\longrightarrow\bar H,\qquad
\bar J:=\pi(J)\subseteq\bar H,
\tag{1}
\]

一个奇素数 \(q\)、阶为 \(q^e\) 的角色

\[
\psi:\bar H\longrightarrow\mu_{q^e},
\tag{2}
\]

以及一个在实际商 \(\bar H\) 中阶与 \(q\) 互素的、预先固定的锚点
\(\theta\in\bar H\)。令

\[
\bar J_\theta=
\{\bar j\in\bar J:\theta\bar j^{-1}\in\operatorname{im}\bar\phi\}.
\tag{3}
\]

这里的 \(H,P,J,\bar J,\theta,\psi,\bar\phi\)、物理表 \(\mathcal W\)、\(\kappa\) 的
canonical occurrence 选择规则、duplicate bound 与 raw tree expansion policy 必须在查看任何
endpoint 或 potential hit **之前**固定并写入同一状态 digest。特别地，不能在某条
成功 raw word 之后才选择 \(J\)、\(\theta\)、\(\kappa\) 或逐顶点查表定义一个 \(\bar j\)。

令 \(\mathscr T\) 是保留 ancestry digest 的有根 actual raw 谱系树。每个顶点
\(v\) 保存一个有序坐标后代 \(z_v\)，根坐标 \(z_\circ\in U(R)\)。每条有向边
\(e:v\to w\) 保存：

\[
r(e)\in U(R),\qquad g(e)\in U(R),\qquad
r(e)g(e)z_w\equiv z_v\pmod R,
\tag{4}
\]

其中 \(r(e)\) 是 actual raw 因子，\(g(e)\) 是除法后实际发生的完整 gcd
reduction，而非任选的约数。式 (4) 由有序 raw 坐标输运给出；它要求保存
selected side、shift、pre/post-gcd 坐标和 orientation。

定义唯一的归一化相位

\[
\Phi_v=-z_v^{-1}
=-z_\circ^{-1}\prod_{e\in[\circ,v]}r(e)g(e)\pmod R.
\tag{5}
\]

本门的 native 分支要求每个 \(\Phi_v\in H\)，并要求下式中的 \(\bar j_v\) 是由
预先固定的数据强制出的元素：

\[
\boxed{
\pi(\Phi_v)=\theta\bar j_v^{-1},\qquad
\bar j_v=\theta\pi(\Phi_v)^{-1}\in\bar J_\theta.
}
\tag{6}
\]

若 \(\Phi_v\notin H\)，或 (6) 的 \(\bar j_v\) 不属于**已固定的** \(\bar J_\theta\)，
正确输出是 `ANCESTRY_ROW_TO_ANCHOR_UNCLOSED`。不能为了修复该失败而扩充
\(J\)，也不能把 \(\Phi_v\) 事后送到一个任意选择的商中。

一个不从 \(H\subseteq U(R)\) 导出的 source-to-F homomorphism 可以另行研究，
但它必须独立声明域、关系保持、目标对合语义及覆盖范围；它不是本门的免费替代品。

为使本门能够服务于一张物理 row 表而不是仅服务于 history clone，另固定一个
已声明的物理表 \(\mathcal W\) 及全定义 occurrence projection

\[
\kappa:\mathcal W\longrightarrow V(\mathscr T).
\tag{6a}
\]

每个 \(w\in\mathcal W\) 必须与 \(\kappa(w)\) 的完整 raw/physical 字段相容，
并使用 \(\bar j_w:=\bar j_{\kappa(w)}\)。若一个 physical row 有多个 ancestry
occurrence，\(\kappa\) 的 canonical 选择规则必须预先固定；若要保留多个 occurrence，
还必须给出 `duplicate_occurrence_bound`，且容量表仍按物理 row \(w\) 计数一次。
phase holonomy 只能授权相位元素合并，不能单独授权物理 row、carrier 或 selector state
合并。下文出现 \(\gamma_{w,k}\) 时，约定它是 \(\gamma_{\kappa(w),k}\)。

## 2. 富集相位输运定理

对 \(1\le k\le e\)，取

\[
\psi_k=\psi^{q^{e-k}},\qquad
\psi_k(\bar j_v)=\zeta_{q^k}^{-\gamma_{v,k}},
\qquad \gamma_{v,k}\in\mathbb Z/q^k\mathbb Z.
\tag{7}
\]

并写

\[
D_{\bar J_\theta,k}=|\psi_k(\bar J_\theta)|.
\tag{7a}
\]

由于 \(\operatorname{ord}(\theta)\) 与 \(q\) 互素，\(\psi_k(\theta)=1\)。由
(4)--(6)，每条谱系边满足

\[
\boxed{
\gamma_{w,k}-\gamma_{v,k}
=\log_{\zeta_{q^k}}\psi_k\!\left(\pi(r(e)g(e))\right).
}
\tag{8}
\]

**证明。** 由 (6)--(7)，

\[
\psi_k(\pi(\Phi_v))
=\psi_k(\theta)\psi_k(\bar j_v)^{-1}
=\zeta_{q^k}^{\gamma_{v,k}}.
\]

而 (5) 给出 \(\Phi_w\Phi_v^{-1}=r(e)g(e)\)。两式相除后取
\(\zeta_{q^k}\) 指数即得 (8)。证毕。

所以实际 source-lineage 的自然边标签是富集 token \((r(e),g(e))\)，或其
乘积 \(r(e)g(e)\)，而不是单独的 raw factor \(r(e)\)。式 (8) 是一个
**row-to-anchor provenance** 定理；它没有给出共同的整数标签
\(s_w\)，更没有给出 \(s_w\equiv c+u\gamma_{w,k}\)。

若当前 coordinate 带方向地是物理尾

\[
z_v\equiv\varepsilon C_v2^\ell\pmod R,
\qquad \varepsilon\in\{+1,-1\},
\qquad pR+1=4M_vC_v,
\qquad 4M_v-R=n_v,
\tag{9}
\]

则 (5) 的相位也可不读取 endpoint 地写成

\[
\Phi_v=-\varepsilon n_v2^{-\ell}
=-\varepsilon2^{2-\ell}M_v\pmod R,
\qquad
\bar j_v=\theta\pi\!\left(-\varepsilon2^{2-\ell}M_v\right)^{-1}.
\tag{10}
\]

这只给出 E3 normal-form verifier 的候选方向/相位输入。physical tail \(2^\ell C_v\) 与广义
\(2^j\) divisor-ratio 偶前驱是不同对象；(10) 不产生后者，也不绕过 F 态的自然
标记提升零分支。

## 3. History 合并与 holonomy

在 ancestry-digest 树中，每条 history occurrence 是不同顶点，所以 (5) 已是一个
顶点 potential。若要把多个 history 合并为同一个 anchor-phase occurrence，则必须额外验证：
在**保留平行边的底层无向多重图**的每个闭合游走
中，正向穿越边 \(e\) 取 \(\pi(r(e)g(e))\)，反向穿越取其逆，乘积均为 \(1\in\bar H\)：

\[
\boxed{
\prod_{e\text{ along }W}\pi(r(e)g(e))^{\operatorname{sgn}_W(e)}=1.
}
\tag{11}
\]

这等价于任意两个同端点 history 的 \(\pi(\Phi)\) 相同，因而等价于它们给出同一个
\(\bar j_v\)。若只需要某一个 \(q^k\)-phase 的一致性，(11) 可弱化为乘积落入
\(\ker\psi_k\)；但那不足以合并完整的 row-to-anchor group element。

即使 (11) 成立，physical row 的合并仍需要 (6a) 中的字段一致性、\(\kappa\) 的
覆盖性和 duplicate-occurrence bound；它不能仅由相位 holonomy 推出。

不能只检查有向闭路：一个有向无环菱形也可能有两条同端点路径，其 gcd 相位积不同。
树的无环性因此只证明 cloned history 内的可积性，不能自动证明原始 raw 图的
`raw_factor_action_compatibility`。

## 4. 与 factor-local 门的精确关系

本节额外要求每个待压缩的 \(r(e),g(e)\in H\)，使 \(\pi(r(e))\) 与
\(\pi(g(e))\) 分别有定义。以下量词只覆盖已声明的 raw-edge universe（及其已请求的
history merge），并要求对所有 \(1\le k\le e\) 成立；等价地，可只在顶层 \(k=e\)
检查。令
\(\lambda_k(u)=\log_{\zeta_{q^k}}\psi_k(\pi(u))\)。由 (8)，对于同一
raw factor \(r\)，富集增量只在以下条件下可压缩为一个只依赖 \(r\) 的 action：

\[
\boxed{
\lambda_k(g(e))=\lambda_k(g(f))
\quad\text{whenever }r(e)=r(f)=r.
}
\tag{12}
\]

此时可以取

\[
\alpha_k(r)=\lambda_k(r)+\lambda_k(g(e))
\tag{13}
\]

（右端因 (12) 与所选边无关）。只有更强的

\[
\boxed{\psi_k(\pi(g(e)))=1\quad\text{for every edge }e}
\tag{14}
\]

成立时，才恢复 canonical raw-factor 公式
\(\alpha_k(r)=\lambda_k(r)\)。

因此本卡的 `ancestry_enriched_row_to_anchor_preflight` 和既有的
`raw_factor_action_compatibility` 是不同字段：

```text
ancestry_enriched_row_to_anchor_preflight
  = a declared, ordered source tree satisfies (4)--(6)

factor_local_raw_action_verified
  = the requested merge holonomy, H-membership, and (12) hold

canonical_raw_factor_action_verified
  = factor_local_raw_action_verified plus (14)
```

没有 (12) 时，不能把 state-dependent gcd reduction 静默删去；有 (12) 也不能把
tree 内的 provenance 误称为全 raw graph 已 complete。

## 5. 从表示到容量仍需的两个独立门

令 \(c(x)\) 是固定层商上的表示数，\(\tau\) 是目标对合，定义 anti-target deficit

\[
D_\tau=\sum_{x\in\bar H}[c(x)-c(\tau x)]_+.
\tag{15}
\]

现在假设 \(\eta\ge1\)、每个物理 row 有 \(1\le h_w\le e\)，并另行给出一个由
实际物理 row 定义的 `demand_to_slot` 映射，把这 \(D_\tau\) 个需求单位送到

\[
\{(w,k):w\in\mathcal W,\ 1\le k\le h_w\},
\tag{16}
\]

且每个 slot 至多承载 \(\eta\) 个需求单位，则纯计数给出

\[
\frac{D_\tau}{\eta}\le\sum_{w\in\mathcal W}h_w.
\tag{17}
\]

若同一张**完整**物理 row 表还已经给出整数标签、共同 affine law、区间和物理 row
重复度上界 \(\mu\)，即对每个 \(w\in\mathcal W\) 与所有 \(1\le k\le h_w\) 有

\[
s_w\in[L,L+B],\qquad
s_w\equiv c+u\gamma_{w,k}\pmod {q^k},\qquad
u\in(\mathbb Z/q^e\mathbb Z)^\times,
\tag{18}
\]

则锚定容量定理才可追加上界

\[
\boxed{
\frac{D_\tau}{\eta}
\le\sum_{w\in\mathcal W}h_w
\le
\mu\sum_{k=1}^eD_{\bar J_\theta,k}
\left(\left\lfloor\frac{B}{q^k}\right\rfloor+1\right).
}
\tag{19}
\]

这是“表示--对偶--容量”之间可审计的条件接口：Fourier energy 或 target deficit
**不能**直接被当作 \(q\)-height。缺少 (16) 的实际、有界碰撞实现时，左侧不成立；
缺少 (18) 的物理标签表时，右侧不成立。history clone 也不能被无界重复计数。

E2 仍要求真实 cofactor-overflow transcript 与独立的 `CarryCore` 条件；E4 仍要求
全域解提升；E5 仍要求全局良基势。终端优先调度必须在任何 raw tree root-entry 或
enqueue 前执行，并在每个 successor chart 中重跑。

## 6. 三个定向控制

### (p=73,R=79)：Fourier 加 raw edge 仍不足

在 F-\(C_{78}\) control 中，取 \(H=U(79)\)、\(P=1\)，固定层为

\[
J=\{1,2,7,14,17,34,40,43,68\}.
\tag{20}

从 universal source 的第一坐标沿实际 \(73\)-edge，有

\[
z_\circ=73,\quad z_1=1,\quad
\Phi_\circ=66,\quad\Phi_1=78,\quad
\Phi_1\Phi_\circ^{-1}=73\pmod {79}.
\tag{21}
\]

但直接计算

\[
\boxed{J\cap73J=\varnothing.}
\tag{22}
\]

若 (6) 在这条边的两个端点同时成立，则
\(73=\Phi_1\Phi_\circ^{-1}=\bar j_\circ\bar j_1^{-1}\)。由于这里 \(P=1\)，
\(\bar j_\circ\) 就是 \(J\) 中的元素，故 \(\bar j_\circ\in J\cap73J\)，矛盾。故此已固定 F layer 不存在覆盖该 raw edge 的
canonical native assignment。它不排除别的 \(J\)、别的 chart 或不属于本卡 native
分支的独立 source-to-F map。

### (p=1009)：有正向谱系相位，但没有 F 桥

完整 source-bypass word 的 \(t=4,2,1\) 尾满足

\[
\Phi_{4C}=-M,\qquad\Phi_{2C}=-2M,\qquad\Phi_C=-13.
\tag{23}
\]

这验证 (4)--(5) 与带方向的 (10)，但没有提供 (6) 的 F anchor assignment、共同
整数标签或 carry/E4/E5。且该素数已有 terminal-first 叶，故只能作为局部正控制。

### (p=193)：gcd enrichment 不能省略

F/\(C_6\)/\(q=3\) control 的 actual p-edge 有 \(g=25\)。富集相位是
\(\Phi=25\)，而只按 raw factor 的相位是 \(1\)。在自然商角色下二者分别有指数
\(2\) 与 \(0\pmod3\)，故删除 \(g\) 会将一个 direct-F compatibility failure
错报为通过。该 parent 为 target-derived formal control，不是 source root，也不涉及
overflow E2。

## 7. 选择器边界

只有下列字段同时存在时，才允许输出
`ANCESTRY_ENRICHED_ROW_TO_ANCHOR_PREFLIGHT`：

```text
terminal_first_status = clear
declared_source_and_tree_expansion_policy = verified
ordered_coordinate_lineage = verified
actual_raw_factor_and_full_gcd_per_edge = verified
native_phase_domain Phi_v in H = verified
fixed (H, P, J, bar_phi, theta, psi) digest = verified
q_coprime_anchor_in_actual_quotient = verified
all forced bar_j_v lie in predeclared bar_J_theta = verified
physical_row_to_ancestry_coverage kappa = verified
occurrence_projection_and_duplicate_bound = verified
phase_merge_policy = distinct_occurrences | holonomy_verified
state_class = F rechecked in the current chart
recursive_edge_eligible = false
```

该输出仍只能是 `analysis_evidence`。它不等于
`raw_factor_action_compatibility=verified`，不等于 AAL capacity 已闭合，也绝不等于
`verified_edge`。若缺少完整物理标签/carry/demand lift/E4/E5 中任一项，状态必须保持
`ANCHORED_PHASE_MAP_UNCLOSED` 或其更早的精确失败码。

窄复现依赖三个常数大小的 receipt：

```bash
python3 reproductions/type_i_ordered_raw_lineage_normalized_phase_rigidity.py --verify
python3 reproductions/type_i_f_c78_raw_root_fixture_p73_r79.py --verify
python3 reproductions/type_i_f_c3_triple_tail_raw_affine_obstruction_p7129.py --verify
```
