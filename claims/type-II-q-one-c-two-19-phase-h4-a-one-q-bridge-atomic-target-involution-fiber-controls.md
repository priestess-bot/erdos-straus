---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-atomic-target-involution-fiber-controls
title: H4 atomic target 控制的单支撑 involution F 证书
statement: >-
  对两个既有 local H4 clean q-bridge atomic-split 控制，canonical target chart 的有限
  centered box 均不命中 -1，但一个 K-support prime 的显式幂恰为 -1 (mod R)，故两者都能
  以 provided_unbounded_modular 回执精确重分类为 F，而无需遍历由全部 support 生成的
  subgroup。具体地，p=73 控制有 R=4681587057373319、
  29^571589117469993=-1 (mod R)，盒大小 8019；p=241 控制有
  R=122496889878545062639、5323^2744808672054466815=-1 (mod R)，盒大小 22113。
  此回执是 target-local F classification，明确不是 canonical Fourier witness，两个控制也
  并未被断言为 actual 19-phase persistent H3 predecessor。因此它不证明 T1 的全称 typed
  serializer、terminal-first priority、source provenance、E1--E5 或全局出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-single-side-exclusion
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-atomic-owner-epoch-locality
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - q-bridge
  - atomic-split
  - target-fiber
  - F-classification
  - involution-witness
  - serializer
  - proof-boundary
sources:
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_atomic_target_involution_fiber_controls.py
    role: exact-target-reconstruction-box-exclusion-and-direct-F-witnesses
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: local-H4-clean-q-atomic-fixtures
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-single-side-exclusion
    role: actual-H4-atomic-endpoint-taxonomy
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-atomic-owner-epoch-locality
    role: canonical-atomic-target-support-and-owner-context
  - concept: denominator-escape-state-contract
    role: target-fiber-F-G-hit-and-signed-defect-contract
visibility: public
last_checked: '2026-08-17'
---

# H4 atomic target 控制的单支撑 involution F 证书

## 1. 这条结果解决的精确问题

H4 clean \(q\)-bridge 的 atomic target 必须独立重算 F/G/hit，不能复制 source 的标签。
通用 `overflow_chart_fiber_profile` 在 finite box 之后枚举整个由 support 生成的有限子群；
对本卡两个大 target chart，这不是合适的短回执。

这里使用一个更窄的充分证书。令


\[
K=\prod_{i=1}^r \ell_i^{\nu_i},\qquad
B_\nu=\prod_i[-\nu_i,\nu_i]\cap\mathbb Z^r,
\tag{1}
\]

且 \((K,R)=1\)。若某个 \(\ell_j\mid K\) 及整数 \(t>0\) 满足


\[
\ell_j^t\equiv-1\pmod R,
\qquad
-1\notin\left\{\prod_i\ell_i^{z_i}:z\in B_\nu\right\},
\tag{2}
\]

则向量 \(z=t e_j\) 证明 \(-1\) 在无限 support subgroup 内，第二个条件排除
`hit`，故 chart 的精确类型为 `F`。这个证书只需一次模幂和一个有限 centered-box
枚举；它不要求列举整个 subgroup。由于 \(t\) 可很大，signed defect 只保存素数--指数
分解，且该 witness 的 policy 是 `provided_unbounded_modular`，不是 canonical
minimum-\(\ell^1\) Fourier input。

## 2. 两个精确 target 回执

下表中的 \(M\) 是 atomic payload 的 lcm support，\(c\) 是其 canonical capacity，


\[
K_T=Mc,\qquad pR_T+1=4K_T.
\tag{3}
\]

| local H4 control | \(p\) | \(M\) | \(c\) | \(R_T\) | support factorization | direct F witness | \(|B_\nu|\) |
|---|---:|---:|---:|---:|---|---|---:|
| `prime_q37_atomic_split_strict` | 73 | 3559956824877628 | 24 | 4681587057373319 | \(2^5\cdot3\cdot7\cdot29\cdot229\cdot17077\cdot1121093\) | \(29^{571589117469993}\equiv-1\pmod {R_T}\) | 8019 |
| `composite_q121_atomic_split_strict` | 241 | 92255470189779250300 | 80 | 122496889878545062639 | \(2^6\cdot5^3\cdot89\cdot229\cdot2381\cdot5323\cdot3571501\) | \(5323^{2744808672054466815}\equiv-1\pmod {R_T}\) | 22113 |

复现器逐项重建 clean-q endpoint、\(Q_x,Q_y\)、\(M,c,R_T,K_T\)，重乘上表的完整
support factorization，枚举 (1) 的 centered box，并直接核验 (2)。两例都得到


\[
\operatorname{classification}=\texttt{F},\qquad
\operatorname{finite\_box\_hit}=\mathrm{false},\qquad
\operatorname{canonical\_fourier\_eligible}=\mathrm{false}.
\tag{4}
\]

因此，它们的 `target_fiber.status` 可取 `nonempty`，并带上显式 unbounded witness 与
全局定向 signed defect；没有伪造空纤维或继承 source label。

## 3. 为什么这不是 T1 的完成

这两个输入是已有的 **local arithmetic controls**。它们证明 target reclassification
在两个大 chart 上可由短、可复核证书完成，却没有证明每个 actual H4 source 都有 (2) 型
involution witness，也没有为没有该 witness 的 target 提供 G separator 或 canonical F
Fourier witness。

此外，两个控制不携带 actual persistent H3 predecessor、完整 terminal-first miss receipt、
state scope 或 E1--E5 edge serializer。因此本卡不能把 target-local classification 升格为
`verified_edge`。它只删除了一个具体的工程障碍：这两个 atomic 控制不再需要不可实用的
全子群 BFS 才能得到精确 F 标签。

## 4. 聚焦复现

```bash
PYTHONPATH=reproductions python3 \
  reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_atomic_target_involution_fiber_controls.py --verify
```

该回执只枚举两个明确的 centered box（8019 与 22113 个指数向量）并执行常数次模幂；不扫描
prime range、分母、state graph 或 generated subgroup。
