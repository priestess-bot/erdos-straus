---
kind: claim
claim_id: type-I-fixed-layer-cyclic-fourier-profile
title: 固定层循环商的精确 Fourier 频谱与 Parseval 证书
statement: 若固定层稳定子商 H/P 为循环群 C_m，则商表示计数可编码为整数系数向量 c；其 Fourier 能量由循环自相关在 m 次单位根处的精确群环求值给出，Parseval 恒等式可验证总非平凡能量，目标纤维缺失时必存在非平凡角色满足 |A(chi)| >= T/(m-1)。该 profile 不预选代数幅度最大角色，也不证明跨状态载体映射或递归边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fixed-layer-stabilizer-defect-reduction
  - type-I-f-g-fourier-obstruction-certificate
topics:
- type-I
- fixed-layer
- cyclic-quotient
- finite-fourier
- parseval
- exact-certificate
- phase-signature
- proof-boundary
sources:
  - reproduction: reproductions/fixed_layer_quotient_fourier.py
    role: generic cyclic quotient profile and exact group-ring autocorrelation
  - reproduction: reproductions/type_i_fixed_layer_stabilizer_fourier.py
    role: focused sixth-root backend and companion cyclic-order check
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: typed selector replay and stale-profile rejection
visibility: public
last_checked: '2026-08-03'
---

# 固定层循环商的精确 Fourier 频谱与 Parseval 证书

## 设置

令 `H` 为固定状态的有限单位子群，令 `J` 为含 `1` 的固定层，并设
`P = Stab_H(J)`。稳定子约化给出 `P` 包含于 `J` 和精确的固定目标计数恒等式。
本文只对商群 `H/P = C_m` 为循环群的情形增加一个可重放的频谱层；非循环商仍由
稳定子定理覆盖，但需要另一个字符分解后端。

取循环生成元，并将 `H/P` 坐标化为 `Z/mZ`。给定残余素数幂块 `(q_i,b_i)`，定义
商表示计数向量：

```text
c_t = # { (j,z) : j in image(J), -b_i <= z_i <= b_i,
            coord(j) + sum_i z_i * coord(q_i) = t mod m }
```

记 `T = sum_t c_t`，并令 `A_k = sum_t c_t * zeta_m^(k*t)`，其中 `zeta_m` 是
一个 m 次单位根。固定目标 `u in H` 的原群表示数等于
`c_coord(image(u))`；profile 首先重算逐目标计数，而不是只保存一个 Fourier 数值。

## 精确群环能量

定义循环自相关：

```text
C_d = sum_t c_t * c_(t-d)       (d mod m)
```

则 `|A_k|^2` 是整数群环 `Z[C_m]` 中的精确求值：

```text
|A_k|^2 = sum_d C_d * zeta_m^(k*d)
```

验证器保存整数系数向量 `C` 和角色索引 `k`，不使用浮点数比较一般阶数的代数
幅度。profile 同时核验：

```text
C_0 = sum_t c_t^2
sum_d C_d = T^2
sum_(k=1..m-1) |A_k|^2 = m * sum_t c_t^2 - T^2
```

最后一式是非平凡频率的 Parseval 账本。

## 目标缺失的存在性下界

若目标坐标计数为零且 `m > 1`，有限 Fourier 反演和三角不等式给出至少一个非平凡
角色满足：

```text
|A_k| >= T / (m - 1)
```

因此 profile 保存阈值 `T/(m-1)` 及其平方 `T^2/(m-1)^2`。它不声称已从整数群环
表达式中选出幅度最大的具体角色；需要具体角色时，必须使用相应阶数的精确代数
后端。当前一侧固定层 `C6` 切片回执继续使用六次单位根整基，额外给出
`amplitude_squared=12` 和规范角色 `k=1`。这不是中心化固定层的数值 profile；完整
中心化 \(C_6\) 控制的 target-odd 范数为 \(16,1,16\)，由
`type_i_f_target_involution_fourier.py` 单独验证。

## 规范相位签名

对每个非平凡角色 `k`，profile 保存：

```text
character_order = m / gcd(m,k)
gamma_(i,k) = k * coord(q_i) mod m
```

`gamma_(i,k)` 是可重算的有限相位分子，可作为后续 q 进相位桥的输入。当前合同
只证明它是状态内商群坐标；除非另有整数映射证明，不能把它解释为不同状态之间共享
的载体高度、缺陷单位或容量资源。

## 聚焦回执

验证器覆盖两个不同循环阶数：

| 状态 | 商群 | 目标计数 | 作用 |
|---|---:|---:|---|
| `(p,R,K)=(193,63,3040)` | `C6` | `0` | 与六次单位根精确回执交叉核验 |
| `(p,R,K)=(97,27,655)` | `C18` | `0` | 检验通用 profile 不依赖 `C6` |

两例均重算原群和商群的表示数恒等式、目标缺失、循环自相关和 Parseval 字段。
它们仍只是状态内对偶证据；选择器将 profile 纳入 `certificate_context`，并在
`carrier_mapping_status=unproved` 时保持 `analysis_evidence` 和
`recursive_edge_eligible=false`。

重放命令：

```bash
python3 reproductions/type_i_fixed_layer_stabilizer_fourier.py
python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
```

该主张推进了统一选择器的“表示—对偶”层，但没有关闭跨状态 q 进容量或良基递降；
下一步仍需证明某类规范相位签名能映射到真实 alternate/source-switch，或者把它直接
转成 Type I/II 终端或满足 E1--E5 的后继。
