---
kind: claim
claim_id: f2-post-g-h4-arithmetic-totality-reduction-v1
title: F2 post-G/H4 的 H4 算术分支完备化与唯一语义接口
statement: >-
  设 P 是 q=1 high-C=2 19-phase 中已经通过 H3=>H4 actual
  source/path、terminal-first 和 typed 前置的 persistent parent，且 H4 chart 满足
  M4>B_p、1<=c4<=p-2。按 R4 mod p 的互斥分支，R4 不等于 0,1 时的第五 anchor、
  R4=0 的同锚 source repair、以及 R4=1 的 proper-overlap small-anchor renewal
  均可归约为 terminal 或与 P 比较严格下降的最终容量 c<=p-2；R4=1 的 full-overlap
  实际前驱为空，top-capacity a>1 由 d=1 handoff 严格离开，a=1 由 clean-q bridge
  的 y-block、p-primary 与首层 stutter source gates 归约为 c_q<=p-2 的 single-side
  或 atomic target-local dispatch。因此在这些 actual 前置与各引用定理的 checkpoint
  guards 下，H4 算术 guard partition 没有未分类的 capacity leaf；唯一未付的是把
  single-side/atomic target 接入共享 PersistentSelector admission、完成 target re-entry
  与其后的 selector。该结果是 track-local arithmetic reduction，不关闭 F2 或 T6。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
  - type-II-q-one-c-two-19-phase-h4-source-residue-finite-bound
  - type-II-q-one-c-two-19-phase-h4-full-overlap-predecessor-exclusion
  - type-II-q-one-c-two-19-phase-h4-raw-source-repair
  - type-II-q-one-c-two-19-phase-fifth-anchor-parent-macro-gate
  - type-II-q-one-c-two-19-phase-h5-top-capacity-d-one-handoff
  - type-II-q-one-c-two-19-phase-h5-a-one-full-overlap-sieve-completion
  - type-II-q-one-c-two-19-phase-h4-p-primary-small-anchor-renewal
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-y-block-nonempty
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-p-primary-endpoint-exclusion
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-universal-stutter-source-d-gate-closure
  - type-II-q-one-c-two-19-phase-h4-clean-q-e1-e5-relative-macro-closure
topics:
  - F2
  - post-G
  - H4
  - H5
  - arithmetic-partition
  - terminal-first
  - complete-excess
  - p-adic
  - clean-q
  - atomic-split
  - proof-boundary
sources:
  - data: data/t6-wave1/f2-post-g-h4-arithmetic-reduction-v1.json
    role: machine-readable-branch-receipt
  - reproduction: reproductions/f2_post_g_h4_arithmetic_reduction.py
    role: focused-algebraic-control-replay
  - document: docs/T6_F2_F3_HIGH_CONCURRENCY_EXECUTION_PLAN.md
    role: F2 quantified domain and E1-E5 acceptance contract
visibility: public
last_checked: '2026-08-24'
---

# F2 post-G/H4 的 H4 算术分支完备化

## 1. 作用域与不越界声明

本卡只处理一个已经存在的 H3=>H4 actual receipt。设

\[
P\Longrightarrow H_4=(p,R_4,K_4;M_4,c_4),
\qquad
4K_4=pR_4+1,
\qquad
M_4>B_p=\frac{(p-1)^2}{4},
\qquad
1\le c_4\le p-2,
\tag{1}
\]

并假定 P 到 H4 的 source/path、terminal-first miss、typed reclassification 和已有
parent receipt 均可重放。P 的固定 parent rank 是

\[
\Lambda_p^\sharp(P)=(0,p-1).
\tag{2}
\]

本卡证明的是 H4 算术 continuation 的分支约简；它不把 H4 checkpoint 自动变成共享
runtime 的 admitted state，也不声称 H4 之后的 F/G target 已有全局 selector。

## 2. 三个 residue 主分支

### 2.1 (R_4\not\equiv0,1\pmod p)

令

\[
Q_5=Q_{K_4}(R_4-1),
\qquad
M_5=\operatorname{lcm}(M_4,Q_5)=M_4L_5,
\qquad
c_5\equiv c_4L_5^{-1}\pmod p.
\tag{3}
\]

因为 (p\nmid R_4(R_4-1)K_4)，

\[
(p,R_4(p-1)-p,p-1)\longrightarrow(1,R_4-1,1)
\tag{4}
\]

是实际 primitive p-source，且 (Q_5) 是非平凡 p-free complete-excess block。这里

\[
R_4-1> (R_4-1,K_4)\le p+1
\tag{5}
\]

排除 (Q_5=1)。若 (c_5\le p-2)，把 (4) 与已有 P=>H4 prefix 作为一个宏，得到

\[
\Lambda_p^\sharp(P)=(0,p-1)>(0,c_5).
\tag{6}
\]

若 (c_5=p-1)，则 (3) 精确是 full-product (d=1) top-capacity normal form。其
\(a_5>1\) suffix 由 d=1 regeneration/source repair/small-anchor route 给出
最终 (c<p-1)；\(a_5=1\) 在 actual H3=>H4 receipt 域被 H5 finite-sieve completion
排除。因此该主分支没有算术容量残余。

### 2.2 (R_4\equiv0\pmod p)

原 universal p-source 的 primitive 性失效，但不需要删除 p-block。取

\[
q_*=\min\{q:q\text{ prime},\ q\nmid R_4K_4(R_4-1)\}
\tag{7}
\]

并令

\[
(U_*,V_*,m_*)=(q_*,R_4(q_*-1)-q_*,q_*-1).
\tag{8}
\]

则

\[
U_*+V_*=R_4m_* ,\quad (U_*,V_*)=1,
\quad
(U_*,V_*,m_*)\xrightarrow{q_*}(1,R_4-1,1).
\tag{9}
\]

由于 (q_*\nmid R_4-1)，该 source replacement 不改变
\(Q_5,M_5,c_5\)。于是同样的二分适用：(c_5\le p-2) 直接给 (6)，而 (c_5=p-1)
进入上一节的 H5 d=1 suffix；H5 (a=1) actual predecessor 仍为空。故 (R_4=0)
不是新的算术 dead end。

### 2.3 (R_4\equiv1\pmod p)

令

\[
h=(R_4-1,K_4),\qquad z=R_4-h.
\tag{10}
\]

H4 carry identity 给出 (2\le h\mid p+1)。实际 H3=>H4 full-overlap predecessor
exclusion 排除 (h=p+1)，所以必须有 (h<p+1)。先沿 H4 p-source 真实剥离
\(R_4-1\) 的 p-block，再到达 \(\{h,z\}\)，并相对 (K_4) 取

\[
Q=Q_{K_4}(z),\qquad
M_{\rm alt}=\operatorname{lcm}(M_4,Q),\qquad
c_{\rm alt}\equiv c_4(M_{\rm alt}/M_4)^{-1}\pmod p.
\tag{11}
\]

若 (c_{\rm alt}\le p-2)，则 parent macro 严格下降。若 (c_{\rm alt}=p-1)，目标
进入 full-product (d=1) 行。其 (a_{\rm alt}>1) suffix 严格离开顶容量；唯一剩余
的数字分支是 (a_{\rm alt}=1)。

在该分支，令 (w=(p+1)/2)、(d=(w,M_4))、(q=w/d)。clean q raw bridge 真实到达

\[
(x_q,y_q)=\left(R_4-\frac zq,\frac zq\right).
\tag{12}
\]

已有三个独立 source gates 给出：

1. (Q_y=Q_{K_4}(y_q)>1)，故 endpoint 不是 full-excess sink，也不是 x-side single
   side；
2. (p\nmid Q_xQ_y)，其中 (Q_x=Q_{K_4}(x_q))；
3. 首层 stutter (E_x\equiv q\pmod p) 不可能。

clean-carrier theorem 已从 actual (a_{\rm alt}=1) receipt 证明

\[
(q,K_4)=1.
\tag{13}
\]

所以 `non-clean-q` 不是此 actual branch 的独立补集，而是空分支。因此，若 endpoint
不是 terminal，则恰有两类算术 payload：

\[
Q_x=1<Q_y
\quad\text{或}\quad
Q_x,Q_y>1,
\tag{14}
\]

且统一目标支撑

\[
M_q=\operatorname{lcm}(M_4,Q_x,Q_y)
\tag{15}
\]

的 canonical capacity 满足 (1\le c_q\le p-2)。第一类是 p-free single-side，第二类
是 p-free atomic split。已有 clean-q relative macro 在 upstream H4 receipt、priority
prefix、target validator 和 serializer guards 全部通过时给出 E1--E5；其 E5 仍是
从 P 的 (2) 比较最终 (c_q)，不是比较 H4 内部 checkpoint。

## 3. 完备性与互斥性

三个 residue 条件

\[
R_4\equiv0,\qquad R_4\equiv1,\qquad
R_4\not\equiv0,1\pmod p
\tag{16}
\]

互斥且穷尽。每个主分支内部的 (c\le p-2) / (c=p-1)、以及
(a=1\) / (a>1) 都是整数或 gcd 定义产生的互斥二分。故在本卡假设域内，H4
**算术**分派无第四个 residue/capacity branch。

full-overlap exclusion 使 `nonproper` 补支为空；(c_{\rm alt}\le p-2) 与
(c_{\rm alt}=p-1) 是 nontop/top 二分；top 内 (a_{\rm alt}=1) 与
(a_{\rm alt}>1) 穷尽，而 (13) 又删除 non-clean-q。故计划要求的
proper/nonproper、top/nontop、a-coordinate 和 clean/non-clean 四层算术 guard 均已符号分派。

但“算术分派无第四分支”不等于 F2 closed：(Q_x=1<Q_y) 与双色 atomic 输出仍需
统一 target serializer、owner/admission、scope continuity 与 successor re-entry；
它们产生的 typed F/G descendants 也仍需 total continuation。数学 branch 已分派，语义 continuation
尚未闭合。

## 4. 精确剩余边界

本卡把 track 的数学残余从“未知 H4 算术出口”缩为：

```text
H4_ARITHMETIC_RESIDUAL = NONE under the stated actual-H3/H4 guards
H4_SEMANTIC_RESIDUAL = single-side/atomic target common-admission and re-entry
H4_F_G_DESCENDANT_TOTALITY = OPEN
F2_POST_G_H4 = OPEN
```

若共享 admission 尚未接入，`pending_dispatch` 仍不是 verified successor；不能因为
(6)、(9) 或 (14) 的严格容量而提前升级 F2。

## 5. 组成定理的证据边界

本卡组合的是已有 claims 的符号蕴含，不重新执行历史大规模筛选。定向复现器只检查：

- p-source / same-anchor replacement 的整数恒等式；
- full-product d=1 形式与 capacity transport；
- clean-q endpoint 的 (Q_y>1)、p-free 与 stutter-free arithmetic shape；
- parent-to-final-target 的 rank 比较。

它不把有限 controls、`recursive_edge_eligible`、`pending_dispatch` 或 registry name
当作 actual admission 证据。严格的 F2 验收仍要求每个 leaf 的 E1--E5、共同 gate 和
re-entry 全部通过。
