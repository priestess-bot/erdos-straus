---
kind: claim
claim_id: t6-frozen-q-one-local-runtime-proper-root-relative-exclusion
title: 冻结 q=1 局部 runtime 的 proper-root 相对不可达
statement: >-
  固定 q=1 local runtime blob 5f4cc98be5e50925a7a6663132d96fcee2d1f222
  与 common classifier blob b03f4f8c24eeb0470b554756e78d1ba047e7fb17。对任一核心
  素数 p，令 Reach_local(p) 为该 module 自身 bootstrap 接受的非终止 initializer
  output 只沿 build_runtime() 登记 route 入队所生成的传递闭包，并在 terminal 或
  DEAD_END 停止。则其 owner 只可能属于 G endpoint、full-carrier post-G、A>1
  overflow、marked absorb 四类，且与 proper_root_stutter_k_gt_one predicate 的交为空。
  这是冻结局部图的相对排除，不是全局 actual-reachable 空域，不关闭 O1、F1、F3 或 T6。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-runtime-slice
  - t6-persistent-selector-state-v1
topics:
  - T6
  - q-one
  - local-runtime
  - reachability
  - proper-root
  - frozen-graph
  - proof-boundary
sources:
  - source: scripts/t6_q_one_full_carrier_runtime_slice_v1.py
    role: frozen initializer, dispatch map, facts, and DEAD_END
  - source: scripts/t6_persistent_selector_state_v1.py
    role: common proper-root owner predicate
  - data: data/t6-constructor-inventory-v1.json
    role: local-runtime and global-coverage boundary
visibility: public
last_checked: '2026-08-27'
---

# 冻结 q=1 局部 runtime 的 proper-root 相对不可达

## 1. Frozen scope

Fix the exact source blobs

```text
scripts/t6_q_one_full_carrier_runtime_slice_v1.py
  5f4cc98be5e50925a7a6663132d96fcee2d1f222

scripts/t6_persistent_selector_state_v1.py
  b03f4f8c24eeb0470b554756e78d1ba047e7fb17
```

For a core prime \(p\), define \(\operatorname{Reach}_{\rm local}(p)\) as
the persistent states obtained by:

1. taking the nonterminal initializer output accepted by this local module's
   own bootstrap;
2. repeatedly executing only the routes registered by its `build_runtime()`;
3. stopping at a verified terminal or `DEAD_END`.

This seed is not promoted to a globally authenticated q=1 source. The
definition is internal to the frozen local runtime.

## 2. Registered path induction

The initializer has one nonterminal target owner:

```text
type_ii_relation_g_endpoint
```

The dispatch registry has exactly two source-owner rows:

```text
type_ii_relation_g_endpoint
  -> type_i_full_carrier_post_g

type_i_full_carrier_post_g
  -> type_i_a_gt_one_overflow_residual
   | type_i_absorb_marked_residual
```

The two final owners have no outgoing route in this slice. Therefore induction
on the number of queue transitions gives

\[
\boxed{
\operatorname{owner}(\operatorname{Reach}_{\rm local}(p))
\subseteq
\left\{
\begin{array}{l}
\texttt{type_ii_relation_g_endpoint},\\
\texttt{type_i_full_carrier_post_g},\\
\texttt{type_i_a_gt_one_overflow_residual},\\
\texttt{type_i_absorb_marked_residual}
\end{array}
\right\}.}
\tag{1}

\]

## 3. Predicate exclusion

All states emitted by this slice begin with facts that fix

```text
proper_root_k = None
proper_root_height = None
proper_root_height_class = NONE
```

and their provenance is one of

```text
ORDINARY_ENDPOINT
FULL_CARRIER_POST_G
OVERFLOW
MARKED_ABSORB
```

The common `proper_root_stutter_k_gt_one` predicate instead requires

```text
provenance_kind = PROPER_ROOT
proper_root_height_class = LOW
proper_root_k is an integer greater than 1
```

Hence every state in (1) fails that predicate:

\[
\boxed{
\operatorname{Reach}_{\rm local}(p)
\cap
\{S:V_{\texttt{proper_root_stutter_k_gt_one}}(S)=1\}
=\varnothing.}
\tag{2}

\]

## 4. Boundary

`Reach_local` is not the global actual-reachable set. Its registered schedule
MISS is not a complete terminal-universe MISS. Other or future initializers,
producers, or dispatch rows may create a proper-root state, and any change to
either frozen blob reopens this relative claim.

Consequently (2) does not prove the semantic proper-root family empty, does
not establish F3 source absence in a future all-constructor runtime, and does
not change O1, F1, F3, T6, or the Erdős--Straus conjecture.
