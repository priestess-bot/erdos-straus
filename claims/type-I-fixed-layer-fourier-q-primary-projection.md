---
kind: claim
claim_id: type-I-fixed-layer-fourier-q-primary-projection
title: 固定层 Fourier 角色阶的 q-primary 精确投影
statement: 对循环商 C_m 的角色 chi_k，令 d=m/gcd(m,k)。若 q^h || d，则约化相位分子 u in Z/dZ 可经 rho_q(u)=(d/q^h)u mod q^h 投影到 q-primary 相位；该映射良定义且与更低 q 层相容。若 q 不整除 d，则从 C_d 到任何 q-primary 加法群的群同态只能平凡。该投影仍不是实际清分中心，必须另加整数坐标识别。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fixed-layer-cyclic-fourier-profile
  - type-I-fixed-layer-fourier-qadic-phase-bridge
topics:
- type-I
- fixed-layer
- finite-fourier
- q-primary
- q-adic
- phase-signature
- homomorphism
- proof-boundary
sources:
  - reproduction: reproductions/fixed_layer_quotient_fourier.py
    role: exact q-primary phase projection and q-not-dividing boundary
  - reproduction: reproductions/type_i_fixed_layer_stabilizer_fourier.py
    role: C6 and C18 focused verification
visibility: public
last_checked: '2026-08-03'
---

# 固定层 Fourier 角色阶的 q-primary 精确投影

## 角色相位

令固定层商为 `C_m`，角色索引为 `k`，并记

```text
g = gcd(m,k)
d = m/g
k_reduced = k/g
```

角色在坐标 `t in Z/mZ` 上的相位可以用约化分子
`u = k_reduced * t mod d` 表示；角色阶恰为 `d`。

## q-primary 投影

若 `q^h || d`，定义

```text
rho_(q,h)(u) = (d / q^h) * u mod q^h
```

这是从加法群 `Z/dZ` 到 `Z/q^h Z` 的良定义群同态：改变 `u` 一个 `d` 不会改变
右侧模 `q^h` 的结果，因为 `q^h` 整除 `d`。对任意 `r <= h`，再模 `q^r` 得到
相容的低层投影；因此它可以作为相位树的 q-primary 坐标。

若 `q` 不整除 `d`，则 `C_d` 的任意元素在 q-primary 加法群中的像的阶同时整除 `d`
和某个 q 的幂，只能为单位元。也就是说，任何此类群同态都平凡；选择器不能把
q 不整除角色阶的 Fourier 相位当作非零 q 进资源。

## 与清分中心的边界

该投影只处理角色阶的 q-primary 分量。真实清分合同中的中心是
`gamma = -A * R^(-1) mod q^e`。要把两者识别，必须额外提供一个整数坐标映射，使

```text
rho_(q,h)(u) = affine_map(A, R) mod q^h
```

并逐层验证嵌套同余。角色阶、Fourier 幅度或商群同构本身不提供这个识别，因此
`carrier_mapping_status` 仍为 `unproved`。

## 聚焦验证

当前 profile 对两个状态保存该投影：

| 状态 | 角色阶 | q-primary 检查 |
|---|---:|---|
| `(p,R,K)=(193,63,3040)` 的首个角色 | 6 | `q=3`, 模 3 投影为 2；`q=5` 明确不可用 |
| `(p,R,K)=(97,27,655)` 的首个角色 | 18 | `q=3`, 模 9 投影为 4 |

这两个结果只证明投影公式和不整除边界；没有声称产生跨状态容量超载或合法递归边。
统一选择器将 `q_primary_projection_rule` 与条件性 `qadic_phase_bridge` 一起保存。
