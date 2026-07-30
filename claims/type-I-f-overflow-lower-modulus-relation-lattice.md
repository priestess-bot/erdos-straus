---
kind: claim
claim_id: type-I-f-overflow-lower-modulus-relation-lattice
title: 端点下降 F-box miss 的更小模数关系格证书
statement: 对冻结端点下降中 42 个 lower-modulus F-box miss，令 t=R/m。Smith/Hermite 整数变换为每个状态重建 K-支撑的满秩关系格、目标 -1 的仿射指数原像，并逐点验证原指数盒与该仿射格不相交；总计检查 13140 个盒点，最大单状态盒 1215 点。27 个状态还满足某个 2^j=-1 (mod t)，但其二进预算仍不足。该结果是 t=1 (mod 4) 的有限关系格证书，不是合法 Type I gap 或全称递降定理。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-balanced-lower-modulus-fiber-profile
  - type-I-f-relation-lattice-certificate-reconstruction
topics:
- type-I
- F-state
- relation-lattice
- smith-normal-form
- hermite-normal-form
- finite-box
- dyadic
- quotient
- proof-program
sources:
- claim: type-I-f-overflow-balanced-lower-modulus-fiber-profile
  role: F-box-miss-input
- claim: type-I-f-relation-lattice-certificate-reconstruction
  role: lattice-reconstruction-method
visibility: public
last_checked: '2026-07-30'
---

# 端点下降 F-box miss 的更小模数关系格证书

## 证书对象

对严格端点下降的更小模数 \(t=R/m\)，前一层分流已经证明目标 \(-1\) 属于
\(K\)-素因子支撑生成的子群，但不属于原有限指数盒。令

\[
K=\prod_iq_i^{\nu_i},\qquad
\Lambda_t=\{z\in\mathbb Z^r:A_tz\equiv0\pmod{D_t}\},
\]

其中 \(A_t\) 是各 \(q_i\) 在 \((\mathbb Z/t\mathbb Z)^\times\) 的离散对数矩阵，
\(D_t\) 是各单位群分量的阶。Smith 分解给出目标 \(-1\) 的一个整数原像 \(z_0\)，
Hermite 正规形给出 \(\Lambda_t\) 的规范满秩基，因此全部目标表示是仿射格

\[
z_0+\Lambda_t.
\]

证书验证四项：

1. \(A_t\Lambda_t\equiv0\pmod{D_t}\)；
2. \(A_tz_0\equiv b_t\pmod{D_t}\)，其中 \(b_t\) 是 \(-1\) 的对数向量；
3. 关系格行列式等于 \(K\)-支撑在模 \(t\) 中的像群阶；
4. 穷尽检查
   \[
   (z_0+\Lambda_t)\cap\prod_i[-\nu_i,\nu_i]=\varnothing.
   \]

第四项把前一层的“盒外 F 障碍”提升为规范整数格证书，而不是只记录一个残数布尔值。

## 冻结审计

复现脚本：

~~~text
reproductions/type_i_f_overflow_lower_modulus_relation_lattice.py
~~~

结果文件：

~~~text
reproductions/type-i-f-overflow-lower-modulus-relation-lattice-results.json
~~~

输入结果文件 SHA-256：

~~~text
c656c91ebb02a33e8d1f5c78db70ce14ac5fbc2decc0db99e05bcbcc1fbee22f
~~~

冻结输出：

~~~text
state_count: 42
total_box_points_checked: 13140
maximum_box_size: 1215
minimum_relation_index: 22
maximum_relation_index: 208576
order_two_target_count: 27
forward: 20 states, 5454 box points, 14 order-two targets
reverse: 22 states, 7686 box points, 13 order-two targets
~~~

所有 42 个状态都满足目标在生成子群内、目标不在有限盒内，且关系格行列式与独立子群
闭包阶一致。27 个状态虽然有 \(2^j\equiv-1\pmod t\)，但这不改变其盒外性质，也不
绕过 \(v_2(2K)=1\) 的预算缺口。

## 边界与下一桥

这里 \(t\equiv1\pmod4\)，所以 \(z_0+\Lambda_t\) 只是更小模数上的关系格接口。要把
它变成原素数 \(p\) 的选择器出口，还需证明以下至少一项：

- 关系格短向量能被提升到合法 \(3\bmod4\) 缺口并保留平方除子；
- 盒外的相位/格距离能按选择不变规则计入跨状态 \(q\)-进容量；
- 关系格的外部端点能构造 Type II 互素因子正规形；
- 不能收费的格缺口导致严格可提升的更小状态。

因此本卡完成的是 F-box miss 的规范化与可复核化，不把有限格证书误写成全称证明。

## 复现

~~~bash
python3 reproductions/type_i_f_overflow_lower_modulus_relation_lattice.py
~~~
