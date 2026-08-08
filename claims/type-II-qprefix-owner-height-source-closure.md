---
kind: claim
claim_id: type-II-qprefix-owner-height-source-closure
title: q-prefix owner 高度到 source-dominating 闭合的有限判据
statement: 对固定核心素数 p、奇素数 q 和一个 source-complete 的有限 owner map，将每个真实源列 g_i 绑定到唯一移位 s_i，并令 e_i=v_q(p+4s_i)。在保持标签和 source-switch 合同的前提下，第 j 层合法槽支配全部源列当且仅当每个 e_i>=j；若某个 e_i<j，则该 owner 给出规范 OWNER_QPREFIX_SOURCE_ESCAPE。因而 phase-prefix 槽容量缺口只有在所有 owner 通过该高度门时才可进入 source-dominating annihilator relay；p=433、q=7、移位 {16,100} 的高度 (1,2) 给出第 1 层闭合、第 2 层对 16 的严格逃逸。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-shared-factor-q-adic-difference-bound
  - type-I-phase-prefix-source-dominating-annihilator-relay
  - type-II-source-fiber-qheight-kneser-bridge
topics:
  - type-II
  - q-prefix
  - owner-map
  - source-completeness
  - source-dominating
  - q-adic
  - capacity
  - escape
  - annihilator
  - proof-program
sources:
  - claim: type-II-shared-factor-q-adic-difference-bound
    role: owner-height-and-layer-capacity
  - claim: type-I-phase-prefix-source-dominating-annihilator-relay
    role: domination-to-annihilator-relay
  - claim: type-II-source-fiber-qheight-kneser-bridge
    role: source-fiber-integer-gate
  - reproduction: reproductions/type_ii_qprefix_owner_height_source_closure.py
    role: p433-owner-height-control
visibility: public
last_checked: '2026-08-09'
---

# q-prefix owner 高度到 source-dominating 闭合的有限判据

## Owner map 合同

固定奇素数 q、核心素数 p 和一个有限 source-complete owner map

    O = {(g_i,s_i): 1 <= i <= m}.

其中 g_i 是当前参数纤维的真实源列，s_i 是唯一的整数移位 owner。要求：

1. owner 标签 s_i 两两可区分，且每个真实源列恰有一个 owner；
2. owner 行已通过来源整除、source-switch、SNF、标签和范围门；
3. 在第 j 个 q-prefix 层，owner i 的槽存在当且仅当

       q^j | p + 4 s_i.                              (1)

   也就是 e_i=v_q(p+4s_i) >= j；
4. 不允许用另一个来源的同余相似槽替代 owner i。

这些是有限 source-map 完备性条件；若 owner 表未穷尽，输出
OWNER_SOURCE_MAP_UNCLOSED，不使用下面的等价式。

## owner 高度闭合定理

令

    e_i = v_q(p+4s_i),
    O_j = {i:e_i >= j},
    C_j = {(s_i,j):i in O_j}.

则第 j 层满足 SOURCE_DOMINATING(C_j) 当且仅当

    O_j = {1,...,m}.                               (2)

若 (2) 成立，owner-to-slot 映射

    g_i -> (s_i,j)                                  (3)

是一个显式的同纤维、同标签 source-dominating 证书；任何 phase-prefix 槽容量
缺口都可以交给 source-dominating annihilator relay。

若 (2) 不成立，取字典序最小的 i_* 使 e_i* < j，则

    OWNER_QPREFIX_SOURCE_ESCAPE
    = (i_*,g_i*,s_i*,e_i*,j)                         (4)

是一个严格的 owner 逃逸见证：第 j 层没有合法槽能支配 g_i*，所以不能从该层
构造湮灭全部真实源列的递降角色。该请求只能转入 source-column 扩张、另一 q
层、其它 Type I/II 射线或明确算术障碍。

## 容量和 relay 后果

在 owner map 合同下，真实 owner 槽数精确为

    |C_j| = #O_j = #{i:e_i >= j}.                    (5)

它满足已有的移位集上界

    |C_j| <= C_j({s_i},q),                           (6)

并且逐层需求 R_j 必须满足

    R_j <= mu |C_j|                                  (7)

才能通过 owner 标签的局部 Hall 门。若 R_j > mu|C_j|，输出
OWNER_QPREFIX_LAYER_DEFICIT；若同时 (2) 成立，再由 phase-prefix
source-dominating relay 给出 annihilator/商/子群分派。若 (2) 失败，优先输出
式 (4)，不能把容量缺口直接升级为 relay。

因此“q 层槽数不足”和“真实源列不被支配”是两个不同回执：

    all owners pass -> capacity deficit may yield annihilator;
    an owner fails  -> source escape, no full-source annihilator.

## 证明

由 owner 合同，第 j 层的合法槽存在当且仅当 (1) 成立。因此所有真实源列都有
同纤维、同标签槽，当且仅当每个 i 都满足 e_i>=j，这正是 (2)；映射 (3) 逐列
给出 SOURCE_DOMINATING。

若存在 i_* 使 e_i*<j，则 (1) 对该 owner 不成立，任何保持 owner 标签的
合法槽都不能代表 g_i*。source-complete 假设排除了未登记的替代 owner，所以
(4) 是不可省略的 source-column escape。式 (5) 是定义，式 (6) 由同一 q 层
移位残类上界得到，式 (7) 是每个槽重复度至多 mu 的普通容量必要条件。
最后，只有在 (2) 成立时，phase-prefix 槽邻域才湮灭全部真实源列，才能调用
source-dominating annihilator relay。证毕。

## 精确控制：p=433

取已有两条 q=7 owner 移位

    p=433,
    S={16,100},
    p+4*16=497=7*71,
    p+4*100=833=7^2*17.

所以

    e_16=1,
    e_100=2,
    C_1=2,
    C_2=1.

第 1 层的 owner 集 O_1={16,100}，映射
16 -> (16,1)、100 -> (100,1) 支配全部两列。第 2 层的 owner 集
O_2={100}；移位 16 的记录

    (16, e_16=1, required_layer=2)

是规范 OWNER_QPREFIX_SOURCE_ESCAPE。若反事实要求两个独立请求都支付第 2 层，
则 R_2=2、mu=1、|C_2|=1，同时有一个层容量缺口和一个 owner 逃逸；选择器
必须保留逃逸优先级，不能把缺口错误升级为全源 annihilator。

该控制还达到共享 q 进界：

    min(v_7(497),v_7(833)) = v_7(4*(100-16)) = 1,

而总高度 1+2=C_1+C_2=3。故它不是松的估计，而是一个真实的 owner-height
闭合/逃逸分界。

## 研究边界

本判据把抽象 SOURCE_DOMINATING 条件化为一个有限、逐 owner 可检查的 q-height
条件，并给出第一个失败 owner 的整数见证。它不保证 owner map 本身对所有核心
素数 source-complete，也不把第 1 层闭合自动推广到更高层；每个层都必须重新
检查 (2)。通过 owner 门后，仍需 source-labelled SNF、Kneser 目标容量和
E1--E5/严格递降门。

## 聚焦复现

~~~bash
python3 reproductions/type_ii_qprefix_owner_height_source_closure.py --verify
~~~

复现只检查 p=433 的实际 q-adic owner 高度、逐层 owner 集、容量等式和第 2 层
逃逸见证。
