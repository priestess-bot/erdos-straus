# 47fedc2 上游依赖清单

冻结点：`47fedc2` — `Archive H4 clean q relative closure`。

## 核心 concept

- `concepts/denominator-escape-state-contract.md`
  - E1--E5、fresh source scope、marked solution set、phase-relative edge 语义。
- `concepts/flagship-proof-program-2026-08-16.md`
  - T4 原始旗舰量词与 T1--T6 关系。

## 方向 3 的核心 claims

- `claims/type-I-type-II-mod-three-double-g-exit-obstruction.md`
  - q=1 G 精确判别；`p=241` 双 G 反例。
- `claims/type-II-q-one-canonical-root-slice-support-disjointness.md`
  - 旧 canonical root 与 `X`-support 的互素障碍。
- `claims/type-II-q-one-type-I-carrier-rail-dispatch.md`
  - carrier rail；唯一 low full-carrier root；首个 odd/even dispatch。
- `claims/type-I-universal-p-source-capacity-anchor-orbit.md`
  - 每个 low Type I chart 的 universal `p`-source。
- `claims/type-II-q-one-full-carrier-phase-root-entry.md`
  - ordinary fresh root-entry 的 E1--E5 与第一 strict segment。
- `claims/type-I-overflow-determinant-fixed-n-dual-support-conflict.md`
  - fixed-`n` quotient-fold 基础恒等式和 identity lift。

## q=1 专属下游 claims

- `claims/type-II-q-one-full-carrier-second-anchor-overflow.md`
- `claims/type-II-q-one-full-carrier-second-anchor-fixed-n-macro.md`
- `claims/type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay.md`
- `claims/type-II-q-one-full-carrier-d-one-regeneration-completion.md`

## 对应 upstream reproduction scripts

- `reproductions/type_ii_q_one_full_carrier_phase_root_entry.py`
- `reproductions/type_ii_q_one_type_i_carrier_rail_dispatch.py`
- `reproductions/type_i_type_ii_mod_three_double_g_exit_obstruction.py`
- `reproductions/type_ii_q_one_canonical_root_slice.py`
- `reproductions/type_ii_q_one_full_carrier_second_anchor_overflow.py`
- `reproductions/type_ii_q_one_full_carrier_second_anchor_fixed_n_macro.py`
- `reproductions/type_ii_q_one_full_carrier_d_one_p_free_gate_exclusion_relay.py`
- `reproductions/type_ii_q_one_full_carrier_d_one_regeneration_completion.py`

## 本包与 upstream reproduction 的关系

本包 `verification/` 下脚本是**独立重写**，不 import 上游 repository modules。这样做的目的不是替代上游 verifier，而是降低“同一个实现同时生成 claim 和验证 claim”的相关性。

## 本包内保存的上游快照

由于打包环境不能稳定获取整个 Git tree，本包 `upstream/` 保存了能够直接取得的关键原始 Markdown 快照；未复制的文件仍由以上 path + commit 唯一确定。
