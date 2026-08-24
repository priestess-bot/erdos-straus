---
kind: claim
claim_id: f2-post-g-c2-fused-h4-macro-reduction-v1
title: q=1 容量二的 19-phase 穷尽与 receiver-to-H4 融合宏
statement: >-
  对 ordinary q=1 full-carrier image 的 actual immediate d=1 receiver，若
  terminal-first miss 后的 nonregeneration complete-excess target 容量为 2，则奇 t
  分支为空，偶 t 分支被强制为 q_star=19、p=912u+769、g=1、j=8；所以当前 q=1
  image 中不存在 C2 non-19 residual。并且 C2 target H0、H1、H2、H3、H4 无需单独
  入队：将 d=1 relay、三 p-anchor、最大第四 anchor及 H4 residue/clean-q exit 组成
  一个以原 d=1 receiver P 为唯一 source 的确定、有限宏。H0--H4 只是 terminal-first 和
  arithmetic checkpoints，最终输出 terminal，或一个从 P 的 (0,p-1) 严格降到
  (0,c_T), c_T<=p-2 的 atomic/ordinary Type-I target。E1 保留整条 actual
  path，E2 target 确定，E4 为 Sol(p) identity，E5 比较 P 与最终 target；E3 和 re-entry
  仍须由共享 serializer/admission 或 Agent 3 atomic contract 完成。因此该结果消除
  C2 non-19 family 与 H3 standalone serializer 义务，但不把融合宏升级为 active
  VERIFIED_SUCCESSOR，也不关闭 H4 target 后的 F/G totality、F2 或 T6。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-d-one-capacity-one-exclusion
  - type-II-q-one-full-carrier-d-one-capacity-two-rigidity
  - type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
  - type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
  - f2-post-g-h4-arithmetic-totality-reduction-v1
  - type-I-t5-full-contract-level-global-well-foundedness
topics:
  - F2
  - post-G
  - C2
  - nineteen-phase
  - H4
  - macro-fusion
  - checkpoint
  - E1-E5
  - proof-boundary
sources:
  - data: data/t6-wave1/f2-post-g-c2-fused-macro-v1.json
    role: machine-readable-phase-and-macro-reduction
  - reproduction: reproductions/f2_post_g_c2_fused_macro.py
    role: focused-formula-composition-controls
visibility: public
last_checked: '2026-08-24'
---

# q=1 C2 的 19-phase 穷尽与融合宏

## 1. C2 入口没有 non-19 补集

设 P 是 q=1 full-carrier second-anchor/full-product prefix 产生的 actual immediate
(d=1) receiver：

\[
A=\frac{pn-1}{4},
\qquad
R=(p-1)n-1,
\qquad
K=A(p-1).
\tag{1}
\]

terminal-first miss 后，其 p-free complete-excess target 的 capacity 为

\[
c\equiv-E^{-1}\pmod p,
\qquad
E=(p-1)b-a,
\tag{2}
\]

其中 ((p+1)/2=ga)、((n+1)/2=gb)。现有 rigidity theorem 对整个 q=1 immediate
receiver domain 证明：

\[
c=2
\Longleftrightarrow
\text{even branch},\quad g=1,\quad j=8,\quad q_*=19,
\tag{3}
\]

并由 (q_*\mid6s-1)、(p=48s+1) 得

\[
\boxed{p=912u+769.}
\tag{4}
\]

奇 branch 的 (c=2) family 为空；偶 branch 的 every (c=2) target 都满足 (4)。
因此计划时保留的 `type_i_c2_non19_residual` 不需要创建：

```text
C2_NON19_RESIDUAL = FAMILY_EMPTY
```

同一 immediate (d=1) source domain 已有更低一层的全称排除：其 canonical residual
capacity 永不等于 (1)。因此本轨道向 A>1/high-support overflow 轨道交付的 immediate-image
nonterminal target 满足

\[
\boxed{c\ge2.}
\tag{5}
\]

其中 (c=2) 恰由 (3)--(4) 的 19-phase fused macro 接管。Agent 2 的抽象 (C=1)
boundary 不应再被计为本 post-G source image 的 live leaf。

## 2. 为什么 H0/H3 不应入队

在 (4) 的 phase 中，q=1 relay 从 P 到 capacity-two H0；随后三 p-anchor 给

\[
P\Longrightarrow H_0\Longrightarrow H_1\Longrightarrow H_2
\Longrightarrow H_3,
\tag{6}
\]

且最大第四 anchor 唯一产生 H4。H0--H2 的局部 capacity 允许上升；H3/H4 的
arithmetic fields 虽可重算，却没有必要成为 recursive source。T5 macro discipline 已允许
有限内部 checkpoints，只比较真实 parent 与最终 target。

于是定义 fused constructor

```text
q_one_d_one_c2_19_h4_fused_exit_v1
```

其唯一 persistent source 是 (1) 的 P；H0--H4 全部记录在 source/path receipt 中，
`queued=false`。每个 checkpoint 仍依序运行 terminal-first 与 typed checks：命中 terminal
立即结束，不能跳过。三 anchor 与第四 anchor 的前缀长度固定；其后的 d=1 regeneration
suffix 虽可依输入变化，但 p-adic rank 每步严格下降，故仍是确定的有限 macro，而非隐藏搜索。

## 3. H4 之后的完整算术分派

最大第四 anchor 已给 (1\le c_4\le p-2)。对 H4 的三个 residue branch：

1. (R_4\not\equiv0,1\pmod p)：第五 anchor/H5 d=1 suffix 给 terminal 或最终
   (c_T\le p-2)；
2. (R_4\equiv0\pmod p)：least-coprime same-anchor source repair 后进入同一分派；
3. (R_4\equiv1\pmod p)：full-overlap predecessor 为空，proper nontop 直接严格，
   top (a>1) 经 d=1 suffix 严格，top (a=1) 的 clean-q single-side branch 为空，
   唯一 nonterminal endpoint 是 p-free atomic target，且 (c_T\le p-2)。

所以在引用 claims 的 actual guards 下，fused macro 的算术输出只有

\[
\operatorname{TERMINAL}
\quad\dot\lor\quad
T\text{ with }1\le c_T\le p-2.
\tag{7}
\]

## 4. 融合 E1--E5

| 合同 | 融合回执 |
|---|---|
| E1 | P 的 persistent source、q=1 d=1 relay、H0--H4 所有实际 raw source/path、每个 terminal-first miss 与 maximal complete-excess occurrence。 |
| E2 | (2)--(4) 固定 phase；三 anchor、第四 anchor和 H4 final branch 的 tie-break 均确定，最终 target 从整数唯一重算。 |
| E3 | 中间 checkpoints 不入队；只给 final target 构造 target shape。common state envelope、owner digest 与 admission 仍是显式外部依赖。 |
| E4 | 所有 chart 共享 (4/p) 与 (W=\operatorname{Sol}(p))，组合 lift 是 identity。 |
| E5 | P 的真实 endpoint rank 为 ((0,p-1))，(6) 给最终 ((0,c_T))，故严格下降。 |

这里不使用 H0->H1 或 H3->H4 的局部 rank 作为 E5；只使用

\[
\boxed{(0,p-1)>(0,c_T).}
\tag{8}
\]

因此 missing H3 serializer 被删除，而不是“补一个 arithmetic state 并宣称 E3”。

## 5. 仍需共享接口完成的部分

若 (6) 的 nonterminal target 是 clean-q atomic output，必须交给 Agent 3 的共同
`AtomicPendingTargetV1` serializer；其它 ordinary output 必须投影到共享
PersistentSelectorState 并重新分类 owner。只有 final target 通过 common gate，融合宏才是
active verified successor。

准确状态为：

```text
C2_NON19_RESIDUAL = FAMILY_EMPTY
C2_H0_H3_STANDALONE_QUEUE_REQUIREMENT = ELIMINATED_BY_MACRO_FUSION
C2_FUSED_MACRO_ARITHMETIC_AND_E1_E2_E4_E5 = ESTABLISHED_RELATIVE
C2_FINAL_TARGET_E3_AND_REENTRY = OPEN_SHARED_INTERFACE
H4_F_G_DESCENDANT_TOTALITY = OPEN
F2 = OPEN
```

新增 producer、把 checkpoint 重新设为 queue item、或改变 T5 macro discipline 时，本结果必须重开。
