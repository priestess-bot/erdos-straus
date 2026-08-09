---
kind: claim
claim_id: type-I-stabilizer-aware-phase-owner-annihilator-relay
title: 稳定子感知 phase-owner 容量缺口的 source-column annihilator 与递降分派
statement: >-
  在 source-map 已闭合、仿射 q-primary 相位已完成 gcd/区间提升且所有相位标签通过固定层稳定子 P 投影到物理 owner 槽时，若请求数超过这些槽的总容量，则该物理 Hall 缺口精确分成两类：需求空间离开 owner source-column 张成空间时产生显式有限域分离泛函；若所有真实 source generators 也被该泛函湮灭，则得到目标相位分离的商 relay、子群 relay 或顶层 primary 终端，否则只能记为 source-column escape。需求空间若已包含于 owner source-column 空间，则严格输出 PHASE_OWNER_COLLISION_ONLY，当前缺口不能强制 annihilator。容量通过且无秩缺口时输出 PHASE_OWNER_RANK_PASS。该结论组合了 phase-lift、P-商去重、物理容量和 Rado 对偶，但不替代整数 source-SNF、范围、source-switch 与 E1--E5 提升门。
claim_status: conditional
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-stabilizer-aware-affine-phase-owner-capacity
  - type-I-fixed-fiber-affine-source-rank-cap-annihilator
  - type-II-owner-projection-physical-capacity-flow-gate
  - type-II-cross-state-qcapacity-deficit-annihilator-relay
topics:
  - type-I
  - F-state
  - G-state
  - q-primary
  - phase-lift
  - stabilizer
  - owner
  - Hall
  - source-column
  - annihilator
  - quotient-descent
  - subgroup-descent
  - collision
  - proof-program
sources:
  - claim: type-I-stabilizer-aware-affine-phase-owner-capacity
    role: affine-phase-and-P-owner-capacity-input
  - claim: type-I-fixed-fiber-affine-source-rank-cap-annihilator
    role: fixed-fiber-source-rank-and-relay-contract
  - claim: type-II-owner-projection-physical-capacity-flow-gate
    role: physical-owner-cut-and-collision-boundary
  - claim: type-II-cross-state-qcapacity-deficit-annihilator-relay
    role: finite-dual-target-relay
  - reproduction: reproductions/type_i_stabilizer_aware_phase_owner_annihilator.py
    role: finite-field-dispatch-controls
visibility: public
last_checked: '2026-08-09'
---

# 稳定子感知 phase-owner 容量缺口的 source-column annihilator 与递降分派

## 1. 输入与闭合条件

令 \(q\) 为素数、\(n=q^e\)，独立 source-map 给出

\[
\mathcal S=\{s_0+h t:t\in\mathbb Z\}\cap[L,U]\cap\mathbb Z,\qquad h>0,
\]

并要求 \(s=\gamma\pmod n\)。固定层的稳定子为 \(P\)，每个合法相位标签的 owner
为 \(\theta(s)\)，其可见 owner 槽为

\[
\rho_P(s)=\theta(s)P\in\mathcal C.
\]

本命题只处理一个相位进程的共同邻域。若不同请求有不同 owner 邻域，应先使用
已有的带容量 Hall 最小割，而不能把下面的总容量代替异构邻域条件。

相位 lift 后的标签集合记为 \(\mathcal L_\gamma\)。owner-map 闭合是指每个
\(s\in\mathcal L_\gamma\) 都有 \(\rho_P(s)\)，且每个出现的物理槽 \(c\) 都有
声明的整数容量 \(\mu(c)\) 和 source column
\[
v_c\in V,\qquad V=\mathbb F_\ell^m.
\]

对 \(R\) 个请求给出需求向量 \(d_1,\ldots,d_R\in V\)，令
\[
D=\operatorname{span}_{\mathbb F_\ell}\{d_1,\ldots,d_R\},\qquad
W=\operatorname{span}_{\mathbb F_\ell}\{v_c:c\in\Omega_\gamma\},
\]
其中
\[
\Omega_\gamma=\{\rho_P(s):s\in\mathcal L_\gamma\},\qquad
B_\gamma=\sum_{c\in\Omega_\gamma}\mu(c).
\]

最后，令 \(H\) 是 source/target 的有限目标商，\(\varphi:H\to V\) 是当前
\(\ell\)-初等 source quotient 的群同态。记真实 source generators 为 \(g_i\)，
并假设它们在当前 source-set 合同下生成全部声明的 source elements；目标为
\(\tau\)。称当前割为 source-dominating，当且仅当
\[
\varphi(g_i)\in W\quad\text{对每个真实 source generator }g_i.
\tag{1}
\]
这不是“当前 owner 槽已知”的同义词；(1) 要求所有真实源列都已被当前割支配。

## 2. 带标签的精确分派

按以下顺序处理，任何较早分支都禁止跳到较晚的递降结论。

1. 先对已经声明的仿射 source-map 求 phase lift。若 source-map 本身没有声明为
   完备，或相位 lift 中有标签没有 owner，或某个 owner 槽缺少 source column，
   输出 **PHASE_OWNER_SOURCE_UNCLOSED**。此时既不能把缺失标签当作相位无解，也
   不能从当前槽缺口构造 annihilator。

2. 在 source-map 声明完备后，输出 **PHASE_GCD_OBSTRUCTED / PHASE_INTERVAL_EMPTY**。
   若
   \(g=\gcd(h,n)\) 不整除 \(\gamma-s_0\)，相位无 lift；若同余可解但区间没有
   代表，则分别返回这两个精确的整数障碍。它们先于 owner 容量计算。

3. 假设相位 lift 和 owner/source-map 都闭合。若
   \[
   R>B_\gamma,
\tag{2}
\]
   则得到物理缺口
   \[
   \mathrm{PHASE\_OWNER\_PROJECTION\_HALL\_DEFICIT}
   =(R,B_\gamma,R-B_\gamma).
\tag{3}
   \]
   这一步按 P-商后的物理槽计数，标签碰撞不能增加 \(B_\gamma\)。

4. 在 (2) 成立时继续看线性需求：

   * 若 \(D\subseteq W\)，输出
     \[
     \boxed{\mathrm{PHASE\_OWNER\_COLLISION\_ONLY}}.
\tag{4}
     \]
     当前割中的任何线性泛函若湮灭所有 owner source columns，也必湮灭全部需求，
     因而此割不能强制出目标分离的 annihilator。应改查 alternate owner、q-prefix
     紧链或广义 \(2^j\) 终端。

   * 若 \(D\not\subseteq W\)，存在
     \[
     \lambda\in V^*,\qquad \lambda(W)=0,\qquad \lambda|_D\ne0.
\tag{5}
\]
     若割不是 source-dominating，输出
     \[
     \mathrm{PHASE\_OWNER\_SOURCE\_COLUMN\_ESCAPE}
\tag{6}
     \]
     并把未支配的真实源列加入后续 source-SNF/Hall 菜单；(5) 只能作为当前槽的
     局部分离见证。

   * 若割 source-dominating，把 \(\lambda\) 拉回 \(H\) 的角色
     \[
     \chi_\lambda(x)=
     \exp\!\left(\frac{2\pi i}{\ell}\lambda(\varphi(x))\right),
     \qquad K=\ker\chi_\lambda.
\tag{7}
     \]
     则所有真实源 generators 落在 \(K\)。按目标相位分三类：

     - \(\lambda(\varphi(\tau))\ne0\) 且 \(K\ne\{1\}\)：输出
       \[
       \mathrm{PHASE\_OWNER\_QUOTIENT\_RELAY}.
\tag{8}
       \]
       目标在严格较小商 \(H/K\) 中非平凡，而源列在商中被湮灭。它是有限群
       relay 候选，仍需整数提升。
     - \(\lambda(\varphi(\tau))\ne0\) 且 \(K=\{1\}\)：输出
       \[
       \mathrm{PHASE\_OWNER\_TOP\_PRIMARY\_TERMINAL}.
\tag{9}
       \]
       此时没有更小的 annihilator 商，必须转入顶层 primary 或广义 \(2^j\) 终端。
     - \(\lambda(\varphi(\tau))=0\)：目标落在 \(K\) 内。若目标尚未属于 source
       set，输出严格子群候选
       \[
       \mathrm{PHASE\_OWNER\_SUBGROUP\_RELAY};
\tag{10}
       \]
       若目标已经在 source set，则该角色只是
       \(\mathrm{PHASE\_OWNER\_RELATION\_ONLY}\)，不能伪造缺失。

5. 若 (2) 不成立且 \(D\subseteq W\)，输出
   \[
   \mathrm{PHASE\_OWNER\_RANK\_PASS}.
\tag{11}
   \]
   这只表示当前相位 owner 的物理容量和线性覆盖均通过，仍必须进入 source-SNF、
   Rado/Kneser、范围和 E1--E5。若容量通过但 \(D\not\subseteq W\)，则输出
   PHASE_OWNER_RANK_GAP 并把 (5) 交给 source-SNF；这不是由物理 Hall 缺口产生
   的结论。

## 3. 证明

相位部分是线性同余的标准解。令
\[
g=\gcd(h,n),\qquad \Delta=(\gamma-s_0)\bmod n.
\]
若 \(g\) 不整除 \(\Delta\)，没有标签；否则约去 \(g\)，得到唯一的
\(t=t_0\pmod{n/g}\)，再与区间相交，得到全部 \(\mathcal L_\gamma\)。因此前两类
回执互斥且完备。

owner 闭合后，每个请求至多使用 \(\mu(c)\) 次槽，所以共同邻域的任意 assignment
都满足 \(R\le B_\gamma\)。这证明 (2)--(3) 是严格的物理 Hall 缺口；不同标签
投影到同一 P-coset 时只能按同一个 \(\mu(c)\) 计数。

若 \(D\not\subseteq W\)，取 \(d\in D\setminus W\)。在有限维商空间 \(V/W\) 上取
一个在 \(d+W\) 上非零的线性泛函并拉回 \(V\)，即得 (5)。若
\(D\subseteq W\)，任何湮灭 \(W\) 的泛函都湮灭 \(D\)，所以 (4) 的
collision-only 结论是严格的，而不是启发式命名。

在 source-dominating 条件 (1) 下，(5) 使每个真实 source generator 的
\(\chi_\lambda\) 值为 \(1\)，故 source set 落在 \(K\)。若目标角色非平凡且
\(K\ne1\)，目标在 \(H/K\) 中仍非单位元，得到严格商 relay；若 \(K=1\)，没有
更小的核商。若目标角色平凡而目标尚未在 source set 中，则目标和源都在严格真
子群 \(K\) 中，得到子群 relay。source-dominating 不成立时，未知真实源列可能
不被 \(\lambda\) 湮灭，只能返回 (6)。所有分支均直接由有限维对偶性、核/商定义
和最大容量界推出。证毕。

## 4. 最小控制

取 \(q=5,e=2\)、标签进程 \(s=3+10t\)、区间 \([0,100]\)、相位
\(\gamma=13\)，得到标签 \((13,63)\)。取
\(P=\{0,4,8\}\subset\mathbb Z/12\mathbb Z\)，owner \(0\) 与 \(4\) 投影到同一
槽 \(c=\{0,4,8\}\)，且 \(\mu(c)=1\)。

在 \(V=\mathbb F_3^2\) 中令两个需求为 \((1,0),(0,1)\)，槽源列为 \((1,0)\)。
此时 \(R=2>B_\gamma=1\)，\(D\not\subseteq W\)，
\(\lambda(x,y)=y\)。真实 source generator 若只有 \((1,0)\)，目标取 \((0,1)\)，
则 \(\lambda(\tau)\ne0\)、\(|K|=3\)，得到非平凡 quotient relay。

同一槽、同一缺口下把目标改为 \((2,0)\)，并声明 source set 为
\(\{(0,0),(1,0)\}\)，则目标在 \(K\) 内但尚未在 source set 中，得到 subgroup
relay。把需求改为 \((1,0),(2,0)\) 时 \(D=W\)，严格得到 collision-only；再把
真实 source generator 增加为 \((0,1)\) 时，得到 source-column escape。将两个
owner 放到不同 P-coset、各给一个容量，则输出 rank pass。最后在一维
\(\mathbb F_3\) 中相同缺口给出 \(K=1\) 的 top-primary 控制。

聚焦复现命令：

    python3 reproductions/type_i_stabilizer_aware_phase_owner_annihilator.py --verify

## 5. 研究边界

该分派把当前工作的四个接口接成一条可计算状态机：仿射相位的整数可解性、
稳定子 owner 去重、物理 Hall 缺口和有限域 source-column 对偶。它证明了一个
重要的负边界：物理槽不足并不自动产生递降；当需求已被当前源列张成时，只能
记录 collision-only。

仍未完成的全局步骤是实际 F/G source-map 的 owner 闭合与 source-dominating 证明，
以及 (8)--(10) 中有限群 relay 到整数 source-switch、SNF、范围和 E1--E5 的
可提升性。因而本命题是统一选择器中的条件性桥，不是 Erdős--Straus 猜想的完整
证明。
