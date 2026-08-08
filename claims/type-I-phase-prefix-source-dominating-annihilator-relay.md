---
kind: claim
claim_id: type-I-phase-prefix-source-dominating-annihilator-relay
title: Fourier—q-prefix 槽缺口的 source-dominating annihilator relay
statement: 设一组 q-primary Fourier 请求的独立需求空间 D_U 维数为 r，真实相位—q-prefix 槽邻域 C 的源列张成空间 W_C 满足 |C|<r；若每个真实源列都有同纤维、同标签的合法槽支配，则存在阶 ell 对偶角色湮灭全部真实源列并分离 D_U。令 K 为其核，目标在 K 外时得到严格商 relay，目标在 K 内且不在源集时得到严格子群 relay；若源列不被槽邻域支配，只输出 PHASE_PREFIX_SOURCE_COLUMN_ESCAPE。对 Type II 目标 -1，非平凡素数阶 quotient relay 只能发生在 ell=2。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-qprimary-phase-prefix-intersection-capacity
  - type-II-cross-state-qcapacity-deficit-annihilator-relay
  - type-II-annihilator-two-sided-subgroup-quotient-descent
topics:
  - type-I
  - type-II
  - F-state
  - G-state
  - q-primary
  - q-prefix
  - Fourier
  - annihilator
  - source-dominating
  - quotient-descent
  - subgroup-descent
  - capacity
  - proof-program
sources:
  - claim: type-I-qprimary-phase-prefix-intersection-capacity
    role: phase-prefix-slot-neighborhood
  - claim: type-II-cross-state-qcapacity-deficit-annihilator-relay
    role: q-deficit-dual-character
  - claim: type-II-annihilator-two-sided-subgroup-quotient-descent
    role: target-phase-relay
  - reproduction: reproductions/type_i_phase_prefix_source_dominating_annihilator_relay.py
    role: quotient-subgroup-escape-controls
visibility: public
last_checked: '2026-08-09'
---

# Fourier—q-prefix 槽缺口的 source-dominating annihilator relay

## 输入

固定一个奇素数 q、一个 primary ell 和一个已经通过 Fourier 相位—q-prefix
交集门的请求子集 U。令

    V_ell = F_ell-vector space of real source columns,
    D_U <= V_ell,
    dim_Fell(D_U) = r.

D_U 是由过滤 Fourier 或 source-difference 分支证明为独立的需求方向空间。固定
一个 q-prefix 层 j，把该层所有通过整数、标签、SNF、source-switch 和范围门的
槽组成邻域

    C = C_j(U) = {(s,j): s is an admissible phase-prefix label}.

每个槽 c 带有真实源列向量 v_c in V_ell，并记

    W_C = span_Fell {v_c : c in C}.

假设层容量切割已经给出

    |C| < r.                                           (1)

定义 SOURCE_DOMINATING(C) 为：每个真实源生成列 g_i 都有一个同纤维、同标签
的合法槽 c_i in C，使

    v_(c_i) = g_i mod ell.

这是真实 source-map 闭合条件，不可用同余相似但来源不同的槽替代。

## source-dominating annihilator 定理

在 (1) 下，若 SOURCE_DOMINATING(C) 成立，则存在一个非零线性泛函

    lambda in V_ell^*,
    lambda(W_C)=0,
    lambda|D_U != 0.                                  (2)

对应的阶 ell 角色 chi_lambda 湮灭所有真实源列。令

    H = finite source target group,
    R = normalized real source set,
    1 in R,
    t not in R,
    K = ker(chi_lambda).

则 R subseteq K，并按目标相位分成：

1. 若 t notin K 且 K != 1，输出
   GLOBAL_PHASE_PREFIX_ANNIHILATOR_QUOTIENT_RELAY，目标投影到 H/K 后仍缺失，
   且群阶严格下降；
2. 若 t notin K 且 K = 1，输出 TOP_PRIMARY_ANNIHILATOR，不能伪造更小商；
3. 若 t in K，且 t notin R，输出
   GLOBAL_PHASE_PREFIX_ANNIHILATOR_SUBGROUP_RELAY，在真子群 K 中保留同一目标
   缺失，且 |K|<|H|；
4. 若 SOURCE_DOMINATING(C) 不成立，不能使用 (2)，输出
   PHASE_PREFIX_SOURCE_COLUMN_ESCAPE，并把未支配源列加入下一次 source-column
   扩张或记录 SNF/CRT/范围障碍。

若目标是 Type II 的 t=-1，且 H/K 的阶为素数 ell，则

    t notin K => ord(tK)=ell and ord(tK)|2,

故 ell=2。奇素数阶 annihilator 只能进入子群分支或源关系 Fourier，不产生
非平凡的 Type II 目标商。

## 证明

由 (1)，dim W_C <= |C| < r=dim D_U。有限维对偶性给出非零
lambda 湮灭 W_C 但不湮灭 D_U，得到 (2)。

若 SOURCE_DOMINATING(C) 成立，每个真实源生成列 g_i 都等于某个 v_(c_i)，
所以 lambda(g_i)=0。由源列生成性，chi_lambda 在 R 上恒等，故
R subseteq K。

若 t notin K，则 tK 是 H/K 中的非单位目标，而 R 的像为单位元，故商目标
仍缺失。K 非平凡时商阶严格小于 H；K=1 时只剩顶层 primary。若 t in K，
R,t 都落在 K，但 t not in R，所以同一缺失限制到真子群 K；K=1 将导致
t=1 in R，与假设矛盾。

最后，Type II 的 t=-1 满足 t^2=1。若 H/K 是阶为素数 ell 的商且 tK 非单位，
则 ord(tK)=ell，同时 ord(tK) divides 2，故 ell=2。源列不被支配时没有理由
断言 lambda 湮灭全源，故只能输出 escape。证毕。

## 可复核证书字段

完整回执至少保存：

    (ell, q, j, U, C, v_c, D_U, lambda,
     source_columns, dominated_columns, target t, K,
     SNF/CRT/source-switch/range status).

其中 (1) 是容量见证，(2) 是线性对偶见证，dominated_columns 是从槽到真实
源列的逐列映射。缺少最后一项时，即使 lambda 在已列出的槽上为零，也只能记录
局部 Hall/线性缺口，不能登记 relay。

## 三个控制

以下控制都使用二元向量，槽数小于独立需求数：

| 控制 | 真实源列 | 槽列 | 需求空间 | 目标 | 输出 |
|---|---|---|---|---|---|
| 商 relay | (1,0) | (1,0) | span((1,0),(0,1)) | (0,1) | quotient relay |
| 子群 relay | (1,0,0) | (1,0,0) | span((1,0,0),(0,0,1)) | (0,1,0) | subgroup relay |
| source escape | (1,0),(0,1) | (1,0) | span((1,0),(0,1)) | (0,1) | source-column escape |
| 顶层 primary | empty | empty | span((1,)) | (1,) | top primary |

商控制中 lambda(x,y)=y，K=span((1,0))，目标在核外。子群控制在
F_2^3 中取 lambda(x,y,z)=z，K=span((1,0,0),(0,1,0))，目标 (0,1,0)
在核内但不在源集 span((1,0,0))。source escape 控制缺少第二个真实源列的合法槽，
所以不允许构造全源 annihilator。顶层控制的核为零群，没有更小 relay。

## 研究边界

该定理把新得到的 phase-prefix layer deficit 接到 annihilator/递降链，但明确
保留 SOURCE_DOMINATING 作为算术完备性门。它不声称任意 q-prefix 槽表都支配
所有真实源列，也不把抽象 quotient/subgroup relay 自动升级为整数 Type I/II；
后者仍需 source-labelled SNF、CRT、范围和 E1--E5 提升。

## 聚焦复现

~~~bash
python3 reproductions/type_i_phase_prefix_source_dominating_annihilator_relay.py --verify
~~~

复现只验证维数缺口、线性 annihilator、目标相位三分和 source-column escape。
