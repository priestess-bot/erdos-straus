---
kind: claim
claim_id: type-II-owner-exact-flow-negative-certificate-relay
title: Type II owner 精确 q 流与 Rado 负证书的 typed 后继分派
statement: 在 source-preserving canonicalization 已通过的有限 owner 回路族中，把物理槽按真实复用容量展开为槽副本。若精确最大流有缺口，或满流后的独立 source-rank 有缺口，则存在一个独立请求子集及阶 ell 对偶角色；该角色按全源列闭合、源列逃逸、依赖回路或算术边障碍分派到 annihilator relay、有限扩张、关系 Fourier 或显式 obstruction。全源列闭合时目标核外/核内/顶层三分完整；只有带来源 SNF/CRT、范围和 E1--E5 门通过时才登记可提升递降。source-preserving 失败则先输出联合匹配 obstruction，不得从物理槽并集直接构造角色。
claim_status: conditional
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-owner-circuit-qcapacity-flow-bridge
  - type-II-owner-source-preserving-fiber-uniformity-criterion
  - type-II-owner-joint-matching-finite-obstruction-closure
  - type-II-cross-state-qcapacity-deficit-annihilator-relay
  - type-II-hall-source-column-closure-relay
  - type-II-source-column-escape-finite-expansion-relay
  - type-II-owner-projection-source-column-expansion-relay
  - type-II-owner-joint-circuit-arithmetic-lift-trichotomy
topics:
  - type-II
  - owner-weight
  - q-adic
  - max-flow
  - Rado
  - annihilator
  - source-column
  - finite-expansion
  - relation-Fourier
  - arithmetic-obstruction
  - strict-descent
  - proof-program
sources:
  - claim: type-II-owner-circuit-qcapacity-flow-bridge
    role: exact-token-physical-slot-flow
  - claim: type-II-owner-source-preserving-fiber-uniformity-criterion
    role: canonicalization-gate
  - claim: type-II-owner-joint-matching-finite-obstruction-closure
    role: nonuniform-joint-obstruction
  - claim: type-II-cross-state-qcapacity-deficit-annihilator-relay
    role: q-deficit-dual-relay
  - claim: type-II-hall-source-column-closure-relay
    role: all-source-column-closure
  - claim: type-II-source-column-escape-finite-expansion-relay
    role: escape-expansion-terminal
  - claim: type-II-owner-joint-circuit-arithmetic-lift-trichotomy
    role: dependency-circuit-arithmetic-lift
  - reproduction: reproductions/type_ii_owner_exact_flow_negative_certificate_relay.py
    role: finite-dispatch-controls
visibility: public
last_checked: '2026-08-09'
---

# Type II owner 精确 q 流与 Rado 负证书的 typed 后继分派

## 1. 规范化输入和两个真正的缺口

固定一个核心素数的有限 source-labelled 参数纤维。需求 token 集记为

\[
X=\{x_1,\ldots,x_n\},
\]

每个 token 有一个在同一 \(\ell\)-初等商中的独立方向
\(d_x\in V_\ell\)，物理 q 槽 \(s\) 有容量 \(b(s)\) 和 source column
\(v_s\in V_\ell\)。source-preserving canonicalization 的条件是：同一物理槽的
所有合法 token 边共享同一个三元签名
\[
(q\text{-layer},\text{source record},v_s).
\tag{1}
\]
因此槽 \(s\) 可以无损地展开为 \(b(s)\) 个副本；每个副本仍带同一个 source
column。若 (1) 不成立，token 依赖的 source vector 不能由物理槽并集表示，直接
应用 Hall 或 Rado 会把不同请求的资源错误合并，必须先输出
\[
\mathrm{OWNER\_TOKEN\_SOURCE\_CANONICALIZATION\_OBSTRUCTED}
\tag{2}
\]
并调用联合物理匹配穷尽和依赖回路算术三分。

在 (1) 通过后，令 \(\widehat S\) 是带容量展开的槽副本集，\(N(U)\) 是请求集
\(U\subseteq X\) 的副本邻域。精确流定义为
\[
F(U)=\max\{\text{把 }U\text{ 分配到 }\widehat S\text{ 的整数流}\}.
\tag{3}
\]
这里的流使用真实 token—槽边，而不是 pair-energy 的重复边数。

有两类、且只有两类需要本引理处理的负证书：

* **流缺口：** 对某个独立请求集 \(U\)，\(F(U)<|U|\)；
* **秩缺口：** 全体相关 token 已满流，但某个独立请求集 \(U\) 的可用 source
  columns 张成空间满足
  \[
  \rho(U)=\dim\operatorname{span}\{v_s:s\in N(U)\}<|U|.
  \tag{4}
  \]

流缺口中的容量副本比物理槽数多时，(4) 仍按副本计数；重复副本不会制造新的
线性方向。

## 2. 负证书到对偶角色

对流缺口，有限 Hall 定理在展开图上给出一个独立请求集（或其最小割）满足
\[
|N(U)|<|U|.
\tag{5}
\]
对秩缺口，(4) 已经给出同一不等式。于是
\[
W_U=\operatorname{span}\{v_s:s\in N(U)\}
\]
的维数小于独立需求空间
\(D_U=\operatorname{span}\{d_x:x\in U\}\)。有限维对偶性给出可计算的
\[
\lambda_U\in V_\ell^*,
\qquad
\lambda_U|_{W_U}=0,
\qquad
\lambda_U|_{D_U}\ne0.
\tag{6}
\]
记录 \((U,N(U),\lambda_U)\) 就是一个规范的
\(\mathrm{SOURCE\_RANK\_FOURIER\_SEPARATION}\) 证书。这里的“独立请求集”是
必要条件：若最小割请求方向本身线性相关，应先取一个最小依赖回路，输出
\[
\mathrm{DEPENDENT\_SOURCE\_ESCAPE\_RELATION}
\quad\text{或}\quad
\mathrm{CIRCUIT\_SOURCE\_RELATION\_FOURIER},
\tag{7}
\]
再交给 source-relation SNF/CRT/power-closed 算术三分；不得把相关方向当成新的
容量单位。

## 3. 全源闭合、逃逸和算术障碍的穷尽分派

设规范化源集由真实 source columns \(g_1,\ldots,g_r\) 生成，目标为
\(\tau\notin R\)。逐个检查 \(\lambda_U(g_i)\)：

### A. 全源列闭合

若
\[
\lambda_U(g_i)=0\quad(1\le i\le r),
\tag{8}
\]
则 \(R\subseteq K=\ker\chi_{\lambda_U}\)。按目标相位得到互斥三分：

1. \(\chi_{\lambda_U}(\tau)\ne1\) 且 \(|K|>1\)：输出
   \(\mathrm{GLOBAL\_ANNIHILATOR\_LOWER\_RELAY}\)。商 \(H/K\) 中源集压到
   单位元、目标仍非单位元；只有其 source-labelled SNF/CRT、范围、\(B'>A\) 和
   E1--E5 通过，才升级为严格可提升递降。
2. \(\chi_{\lambda_U}(\tau)\ne1\) 且 \(K=1\)：输出
   \(\mathrm{TOP\_PRIMARY\_ANNIHILATOR}\)，转入广义 \(2^j\) 或已有 F/G
   顶层终端；不能制造同阶递降。
3. \(\chi_{\lambda_U}(\tau)=1\)：目标和源集同落在真核子群 \(K\) 中，输出
   \(\mathrm{ANNIHILATOR\_SUBGROUP\_LOWER\_RELAY}\)。由于 \(1\in R\) 且
   \(\tau\notin R\)，此处 \(K\ne1\)，所以有限群势严格下降；整数提升失败时
   只记录 \(\mathrm{ANNIHILATOR\_SUBGROUP\_LIFT\_OBSTRUCTED}\)，不把关系
   Fourier 重复收费。

### B. 源列逃逸

若存在 \(g_i\) 使 \(\lambda_U(g_i)\ne0\)，输出
\[
\mathrm{SOURCE\_COLUMN\_ESCAPE}.
\tag{9}
\]
完整同纤维菜单随后只有以下回执：

* 有携带 \(g_i\) 的独立外部请求时，按源列逃逸扩张桥加入该请求；新增槽副本使
  Hall 缺口不增，若 q 流被释放则输出
  \(\mathrm{Q\_ADIC\_ESCAPE\_EXPANSION\_RELEASE}\)；
* 外部请求方向依赖时，输出 (7)，并把最小 circuit 送入本仓库的算术 lift
  trichotomy；
* 没有合法边时，保存完整 SNF/CRT/范围失败行，输出
  \(\mathrm{SOURCE\_COLUMN\_EDGE\_OBSTRUCTED}\)。

该分派不把一次扩张本身称为下降；只有后续通过来源标签和 E1--E5 的严格
\(D' < D\) 映射才是可提升递降。

### C. source-preserving 失败

若 (1) 失败，先执行联合物理满匹配穷尽：物理流通过但 source vector 依赖时，
输出规范最小依赖 circuit；所有满匹配均依赖时，输出
\(\mathrm{OWNER\_JOINT\_SOURCE\_SLOT\_OBSTRUCTION}\)。每个 circuit 依次
进入 Type II 直接命中、严格 source-switch、同模数 Fourier 或
\(\mathrm{CIRCUIT\_SOURCE\_RELATION\_LIFT\_OBSTRUCTED}\)。在该分支完成前，
不能声称存在 (6) 的物理 source column 对偶。

## 4. 目标为 \(-1\) 时的 primary 限制

Type II 的目标满足 \(\tau^2=1\)。若 \(\chi\) 的阶为奇素数 \(\ell\)，则
\[
\chi(\tau)^2=1,
\qquad
\chi(\tau)\in\mu_\ell,
\]
从而 \(\chi(\tau)=1\)。因此奇 primary 的全源闭合缺口只能走子群 relay 或
关系/算术分支；核外顶层分支只可能发生在 \(\ell=2\)，正好与广义 \(2^j\)
终端对接。这一限制减少了把奇 primary 负证书误写成目标商缺失的风险。

## 5. 证明

容量展开把每个物理槽替换为 \(b(s)\) 个同源副本，故整数最大流等于原物理
容量网络的最大流。若某独立请求集流不满，Hall 定理给出 (5)；若流满而 (4)
成立，则 (4) 本身给出邻域维数严格不足。两种情况下，\(W_U\) 是严格小于
\(D_U\) 的有限维子空间，取商 \(D_U/W_U\) 的非零线性泛函并延拓到
\(V_\ell\) 即得 (6)。若请求方向相关，最小依赖关系给出 (7)，而非 (6)。

当 (8) 成立时，每个真实源生成元位于 \(K\)，因此其所有带来源乘积都在
\(K\)；目标相位非平凡时投影到 \(H/K\) 仍缺失，\(|K|>1\) 给出严格商阶
下降，\(K=1\) 是顶层 primary；目标相位平凡时目标也位于真核子群中，因
\(1\in R\) 且 \(\tau\notin R\)，该子群非平凡且阶严格小于 \(|H|\)。

当 (8) 失败时，(9) 是具体线性分离列；已有有限扩张引理保证独立外部边、依赖
外部边和无边障碍穷尽所有同纤维处理。source-preserving 失败时，物理槽没有
请求无关的 source column，故只能使用联合匹配的回路枚举；这正是 (2) 的前提
失败，不允许套用物理 Hall 对偶。最后，\(\tau^2=1\) 与奇阶角色值的阶互素给出
第 4 节的 primary 限制。证毕。

## 6. 研究边界

该引理完成了一个真实接口：最新精确 token—槽流的两个负出口（流缺口和满流秩
缺口）现在都能生成带源列的对偶，并接入已有的闭合/逃逸/回路三分；非均匀 owner
资源不会被并集合并。它仍是条件性结果：尚未证明每个核心素数都有一个通过
source-preserving canonicalization 的有限相容回路族，也尚未证明所有顶层 primary
或算术障碍都会给出 Type I/F/G 证书。全局选择器的决定性缺口因此被精确收缩为
这些入口覆盖与整数提升条件，而不是未分类的 q 容量负证书。
