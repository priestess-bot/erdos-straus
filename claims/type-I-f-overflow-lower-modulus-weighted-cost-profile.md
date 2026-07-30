---
kind: claim
claim_id: type-I-f-overflow-lower-modulus-weighted-cost-profile
title: 低模数 F-box miss 的单位权溢出价格有限剖面
statement: 对冻结的 42 个低模数 F-box miss，令 Omega_1 为目标关系纤维中逐坐标盒外量之和的最小值。完整枚举溢出层 L<=6 得到精确值分布 Omega_1=1:12, 2:8, 3:2, 4:4, 5:2, 6:2；其余 12 个仅有 Omega_1>=7。将这 12 个再探测到 L<=9 后，6 个得到精确值 7:2, 8:3, 9:1，另 6 个仅有 Omega_1>=10。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-lower-modulus-weighted-cost-interface
  - type-I-f-overflow-lower-modulus-relation-lattice
topics:
- type-I
- F-state
- finite-box
- overflow
- weighted-capacity
- relation-lattice
- finite-audit
sources:
- claim: type-I-f-overflow-lower-modulus-weighted-cost-interface
  role: omega-definition
- claim: type-I-f-overflow-lower-modulus-relation-lattice
  role: frozen-42-state-input
visibility: public
last_checked: '2026-07-30'
---

# 低模数 F-box miss 的单位权溢出价格有限剖面

## 定义

对低模数 t=R/m 的冻结因子分解 K=prod_i q_i^nu_i，令

~~~text
Omega_1(t) = min { sum_i max(abs(z_i)-nu_i, 0)
                    : prod_i q_i^z_i = -1 (mod t) }.
~~~

输入的 42 个状态已由原 F 见证保证目标纤维非空；F_box_miss 分类则保证
Omega_1(t)>0。在同一溢出代价 L 内，脚本仅用字典序选择一个代表向量，
不把该向量本身当作选择不变对象。

## 冻结输入与复现

独立脚本：

~~~text
reproductions/type_i_f_overflow_lower_modulus_weighted_cost.py
~~~

结果 JSON：

~~~text
reproductions/type-i-f-overflow-lower-modulus-weighted-cost-results.json
~~~

输入结果及 SHA-256：

~~~text
type-i-f-overflow-r-modulus-repair-results.json
c656c91ebb02a33e8d1f5c78db70ce14ac5fbc2decc0db99e05bcbcc1fbee22f
~~~

因子分解输入及 SHA-256：

~~~text
type-i-f-overflow-support-boundary-results.json
93c571a0fdfe12d18028c21d10c1f8445b1e34ae979489c852478d0bce8ad9b1
~~~

本次结果 JSON SHA-256：

~~~text
e4bffc9727821fcfd83a5ae0bb02b8d5326ac58a024563e0a9acdfa355fded82
~~~

复现命令：

~~~bash
python3 reproductions/type_i_f_overflow_lower_modulus_weighted_cost.py
~~~

## 有限剖面

主剖面完整枚举每个 L=0,1,...,6 的整数向量层

~~~text
S_L = { z : sum_i max(abs(z_i)-nu_i, 0) = L }.
~~~

每一层中的盒内坐标逐一取值，盒外坐标按超出量和正负号逐一取值，因此每个
S_L 中的向量恰好出现一次。第一次命中
prod_i q_i^z_i = -1 (mod t) 即为 Omega_1 的精确值。统计如下：

~~~text
state_count: 42
primary_max_overflow: 6
primary_exact_count: 30
primary_unresolved_count: 12
primary_histogram: Omega_1=1:12, 2:8, 3:2, 4:4, 5:2, 6:2
~~~

对主剖面未解析的 12 个状态再完整探测到 L<=9：

~~~text
secondary_exact_count: 36
secondary_histogram: Omega_1=1:12, 2:8, 3:2, 4:4, 5:2, 6:2, 7:2, 8:3, 9:1
secondary_unresolved_count: 6
~~~

剩余 6 个状态为

~~~text
(p, t, orientation)
(62704849, 649, forward)
(75056809, 21113, reverse)
(310002289, 107977, reverse)
(312918169, 16649, forward)
(366108649, 11057, forward)
(373561609, 208577, forward)
~~~

它们目前仅能推出 Omega_1>=10。这不是“没有解”的结论；继续扩大层数仍是
开放的计算问题。

## 解释边界

这里的 Omega_1 是低模数乘法关系格上的单位权溢出价格。它不是
v_q 标签、载体高度或 q-height，也没有证明每个溢出层必须支付同一条
共同的 q-进容量链。因此本卡不能单独推出容量矛盾、Type I/II 证书或严格
递降。要把剖面提升为证明组件，仍需建立一个可复用的算术映射：溢出层（或其
Pareto 支持）要么注入受控的共同载体高度，要么产生更小且可提升的状态。
