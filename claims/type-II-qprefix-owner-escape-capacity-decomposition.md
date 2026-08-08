---
kind: claim
claim_id: type-II-qprefix-owner-escape-capacity-decomposition
title: q-prefix owner 逃逸的紧链—容量松弛分解
statement: 对固定奇素数 q、核心素数 p 和 source-complete 的有限 owner map，令 e_i=v_q(p+4s_i)、O_j={i:e_i>=j}，C_j 为所有 owner 移位在模 q^j 下的最大残类占用，Delta_j=C_j-|O_j|。则 O_j 是唯一目标残类中的 owner 集；若 i 的高度 k=e_i<j 且 O_j 非空，任取 a in O_j 都有 v_q(s_i-s_a)=k，给出严格 q-prefix 边界。对层需求 R_j 和每槽重数 mu，owner 缺口、可用残类松弛和全局 q 进缺口满足 (R_j-mu C_j)_+=((R_j-mu|O_j|)_+-mu Delta_j)_+。因此 Delta_j=0 时 owner 逃逸是紧链边界，不能由容量松弛吸收；Delta_j>0 时至多 mu Delta_j 个 owner 缺口可由非 owner 标签的额外残类吸收，必须另过 source-switch；超出该松弛的部分是严格 Q_ADIC_LAYER_CAPACITY_DEFICIT。p=433,q=7 给出紧链，扩展移位集给出松弛链。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-qprefix-owner-height-source-closure
  - type-II-shared-factor-q-adic-difference-bound
  - type-II-cross-state-layered-rado-qcapacity-cut
topics:
  - type-II
  - q-prefix
  - owner-map
  - source-escape
  - q-adic-boundary
  - capacity
  - slack
  - Hall
  - source-switch
  - proof-program
sources:
  - claim: type-II-qprefix-owner-height-source-closure
    role: owner-layer-closure-and-escape
  - claim: type-II-shared-factor-q-adic-difference-bound
    role: q-adic-residue-capacity
  - claim: type-II-cross-state-layered-rado-qcapacity-cut
    role: layered-demand-interface
  - reproduction: reproductions/type_ii_qprefix_owner_escape_capacity_decomposition.py
    role: tight-and-slack-controls
visibility: public
last_checked: '2026-08-09'
---

# q-prefix owner 逃逸的紧链—容量松弛分解

## 1. 设置与目标残类

固定奇素数 (q)、奇素数 (p) 和一个已经通过 source-complete、SNF、CRT、范围及
source-switch 标签门的有限 owner map

\[
  O=\{(g_i,s_i):1\le i\le m\}.
\]

令

\[
  e_i=v_q(p+4s_i),\qquad
  O_j=\{i:e_i\ge j\},\qquad
  A_j=\{s_i:i\in O_j\}.
\]

记

\[
  C_j=\max_{a\bmod q^j}\#\{s_i:s_i\equiv a\pmod {q^j}\},
  \qquad
  \Delta_j=C_j-|O_j|.
\tag{1}
\]

因为 (4) 在模 (q^j) 上可逆，存在唯一目标残类

\[
  \beta_j\equiv-p4^{-1}\pmod {q^j}
\tag{2}
\]

使得

\[
  A_j=\{s_i:s_i\equiv\beta_j\pmod {q^j}\}.
\tag{3}
\]

所以 (|O_j|\le C_j)，即 (Delta_j\ge0)。这里的 (C_j) 仍由完整 owner
移位集计算，而不是只由已经通过第 (j) 层的 owner 计算。

## 2. 逃逸 owner 的精确 q-adic 边界

若 (i\notin O_j)，令 (k=e_i<j)。假设 (O_j\ne\varnothing)，取任意
(a\in O_j)，于是 (e_a\ge j>k)。写

\[
  p+4s_i=q^ku_i,
  \qquad p+4s_a=q^{e_a}u_a,
  \qquad q\nmid u_i u_a.
\]

相减得到

\[
  4(s_i-s_a)
  =q^k\bigl(q^{e_a-k}u_a-u_i\bigr).
\]

括号中的量模 (q) 等于 (-u_i)，是单位；又 (q\nmid4)，因而

\[
\boxed{v_q(s_i-s_a)=k=e_i.}
\tag{4}
\]

这给出规范边界回执

```text
OWNER_QPREFIX_BOUNDARY = (i, a, e_i, j, s_i, s_a)
```

它比“第 (j) 层没有 owner 槽”更强：逃逸 owner 与任意仍活跃的高层 owner
在第 (e_i) 层相同、在第 (e_i+1) 层分叉。因此它不能被同一个第 (j) 层目标
残类中的匿名槽替代。

若 (O_j=\varnothing)，则第 (j) 层没有目标 owner，回执改为
`OWNER_QPREFIX_TOP_EMPTY`；此时不能伪造式 (4) 的比较 owner。

## 3. owner 缺口与全局容量的精确分解

令 (R_j\ge0) 是第 (j) 层独立请求数，(mu\ge1) 是每个合法槽允许支付的
最大重复度。owner 标签本身只允许使用 (O_j) 中的槽，因此 owner 层容量为

\[
  \mu|O_j|.
\]

完整移位残类的 q 进上界可支付 (mu C_j)。定义

\[
  G_j=(R_j-\mu|O_j|)_+,\qquad
  S_j=\mu\Delta_j,\qquad
  D_j=(R_j-\mu C_j)_+.
\tag{5}
\]

则有精确恒等式

\[
\boxed{
  D_j=(G_j-S_j)_+
  =\bigl((R_j-\mu|O_j|)_+-\mu\Delta_j\bigr)_+.
}
\tag{6}
\]

证明只需分三段：若 (R_j\le\mu|O_j|)，三项的正部均为零；若
(mu|O_j|<R_j\le\mu C_j)，则 (G_j=R_j-mu|O_j|\lemuDelta_j=S_j)，而
(D_j=0)；若 (R_j>mu C_j)，则 (G_j-S_j=R_j-mu C_j=D_j)。

式 (6) 的选择器含义是：

1. (G_j) 是保持 owner 标签时真实暴露的层缺口；
2. (S_j) 是完整移位集仍可提供的、但必须通过非 owner source-switch 才能使用的
   容量松弛；
3. (D_j>0) 是连完整残类容量也无法支付的严格
   `Q_ADIC_LAYER_CAPACITY_DEFICIT`。

因此 (Delta_j>0) 不能自动修复 owner 缺口；它只把缺口转成一个有上界的
alternate-owner 搜索任务。反之，(Delta_j=0) 时 (S_j=0)，任何 (G_j>0)
都同时是全局 q 进缺口，且式 (4) 给出每个失败 owner 的紧链边界。

## 4. 紧链—松弛二分

对任意层 (j)，选择器按以下顺序回执：

### A. 紧链

若 (Delta_j=0)，则目标残类是完整 owner 集的一个最大占用残类。任何
(i\notin O_j) 都产生 `OWNER_QPREFIX_TIGHT_BOUNDARY`；若 (R_j>mu|O_j|)，
由 (6) 立即得到严格 q 进容量缺口。此时不能把一个外部残类的槽偷偷标成同 owner
槽，也不能调用 source-dominating annihilator relay。

### B. 容量松弛

若 (Delta_j>0)，则最多 (muDelta_j) 个 owner 缺口可由完整移位菜单中的
额外残类支付。每一个这样的支付都必须产生一个新的 source-switch/alternate-owner
边，并重新通过 SNF、CRT、标签和整数提升门；若外部边不独立，转为已有的
`DEPENDENT_SOURCE_ESCAPE_RELATION`，若不存在则保留算术障碍。超过
(muDelta_j) 的剩余需求由 (6) 严格切出。

这把 owner-height 逃逸接到已有的有限源列扩张：松弛分支允许有限扩张尝试，紧链
分支直接产生 q-adic 边界，而不是重复调用一个不满足 source-dominating 的全源
湮灭器。

## 5. 精确控制：(p=433,q=7)

先取已有紧链移位集

\[
  S_0=\{16,100\},
  \quad e_{16}=1,\quad e_{100}=2.
\]

于是

\[
  (|O_1|,C_1,\Delta_1)=(2,2,0),
  \qquad
  (|O_2|,C_2,\Delta_2)=(1,1,0).
\]

在第 (2) 层，16 是逃逸 owner，100 是比较 owner，且

\[
  v_7(16-100)=1=e_{16}.
\]

若 (mu=1,R_2=2)，则

\[
  G_2=1,\qquad S_2=0,\qquad D_2=1.
\]

这是紧链上的真实 q 进超载，而不是单纯 owner 标签不匹配。

再加入已有严格缺口控制中的移位

\[
  S_1=\{16,100,3,10,17\}.
\]

第 1 层目标 owner 仍为 16、100，但三个额外移位落在另一个最大残类，故

\[
  (|O_1|,C_1,\Delta_1)=(2,3,1).
\]

取 (mu=1,R_1=3)，有

\[
  G_1=1,\qquad S_1=1,\qquad D_1=0.
\]

所以完整 q 残类容量足够，但 owner 标签仍暴露一个必须通过 source-switch 的
缺口。第 2 层仍有 ((|O_2|,C_2,\Delta_2)=(1,1,0))，故 (R_2=2) 依然产生
紧链超载和 16 相对 100 的边界见证。

## 6. 研究边界

本引理新增了 owner 逃逸的 q-adic 边界式 (4) 和容量缺口恒等式 (6)。它严格
区分：

* 紧最大残类中的 owner escape，可直接进入 q 进缺口/关系分派；
* 非最大残类造成的容量松弛，只能支持有限 alternate-owner/source-switch 搜索；
* 完整容量仍不足的部分，才是可进入 Rado/Kneser 切割的严格 q 进缺口。

它不声称松弛分支必然存在合法整数提升，也不把式 (4) 单独升级为 Type I/II
短证书。后续仍需把松弛分支的 alternate-owner 边接入 source-column 扩张，并在
紧链分支验证广义 (2^j)、Fourier 或稳定子 relay 的整数提升门。

## 聚焦复现

```bash
python3 reproductions/type_ii_qprefix_owner_escape_capacity_decomposition.py --verify
```

