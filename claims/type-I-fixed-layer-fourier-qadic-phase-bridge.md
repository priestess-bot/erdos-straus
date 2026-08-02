---
kind: claim
claim_id: type-I-fixed-layer-fourier-qadic-phase-bridge
title: 固定层 Fourier 相位到 q 进容量的条件桥
statement: 若循环商 Fourier 角色的相位签名带有显式仿射映射到 q^h 的载体相位，并且跨状态相位中心在每个最低共同层满足嵌套同余，则这些签名可进入已有相位树容量账本；未给出该映射和同余时，Fourier 角色阶不能被解释为共享 q 进资源。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fixed-layer-cyclic-fourier-profile
  - type-I-phase-clearing-cell-capacity-contract
  - type-I-overflow-defect-unit-phase-capacity
topics:
- type-I
- fixed-layer
- finite-fourier
- q-adic
- phase-bridge
- capacity
- conditional-interface
- proof-boundary
sources:
  - reproduction: reproductions/fixed_layer_quotient_fourier.py
    role: exact Fourier phase signatures and typed bridge requirements
  - claim: type-I-phase-clearing-cell-capacity-contract
    role: nested q-adic phase-cell capacity
visibility: public
last_checked: '2026-08-03'
---

# 固定层 Fourier 相位到 q 进容量的条件桥

## 输入

固定状态的循环商记为 `C_m`，选定一个非平凡角色索引 `k`。对残余块 `q_i`，profile
给出有限相位分子：

```text
gamma_i = k * coord(q_i) mod m
```

这些 `gamma_i` 只属于商群坐标。要把它们送入某个素数 `q` 的容量账本，必须额外提供：

1. 一个明确记录的仿射映射 `rho_i: Z/mZ -> Z/q^h_i Z`，以及相位中心
   `c_i = rho_i(gamma_i)`；
2. 每个高度 `h_i > 0` 和有限标签区间宽度 `M`；
3. 重复度上界 `mu`；
4. 任意两条兼容记录 `i,j` 的嵌套同余
   `c_i = c_j (mod q^min(h_i,h_j))`。

映射可以来自显式 alternate/source-switch 恒等式、清分移位或其它已证明的整数
坐标拉回；不能由角色阶、Fourier 幅度或模群同构自动推定。

## 条件性容量结论

在上述输入成立时，令 `D_t` 为满足 `h_i >= t` 的相位中心 `c_i mod q^t` 的不同值
数量。相同相位胞内的高度记录满足已有相位树账本：

```text
sum_i h_i <= mu * sum_{t >= 1} D_t * (floor(M / q^t) + 1)
```

其中每个 `D_t` 都由明确的相位中心重算。若另有证明把超出右端的高度需求注入某个
实际载体集合，则可以得到容量矛盾；若没有该注入，账本只是条件性上界。

## 类型边界

该桥的状态类型固定为：

```text
phase_source = quotient_fourier_character
qadic_phase_bridge = conditional_contract_only
carrier_mapping_status = unproved
selector_status = analysis_evidence
recursive_edge_eligible = false
```

只有在额外证明相位映射、嵌套同余、标签非空和完整 E1--E5 后，才可以把容量结论
升级为 `verified_edge` 或 `terminal_leaf`。因此它补齐了 Fourier 到容量的接口语义，
但没有声称当前两个聚焦状态已经产生跨状态超载。

## 聚焦实现

`fixed_layer_quotient_fourier.py` 在每个 profile 中保存角色相位签名和上述四类
`required_inputs`，并显式标记 `carrier_mapping_status=unproved`。统一选择器重算
profile 后将 `qadic_phase_bridge` 原样放入 `certificate_context`，所以缺失桥接数据
不会被误认为容量证书。

这条主张的作用是把下一步真正需要证明的对象限定为“显式相位映射 + 嵌套同余 + 实际
载体注入”，而不是继续累加状态内 Fourier 幅度或角色阶统计。
