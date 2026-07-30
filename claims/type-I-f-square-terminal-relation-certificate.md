---
kind: claim
claim_id: type-I-f-square-terminal-relation-certificate
title: 平方终端 F 状态的完整关系格短证书重建
statement: 对冻结的 253 个多支持平方终端 F 状态，Smith/Hermite 整数变换为每个状态重建满秩关系格基和目标 -1 的仿射指数原像，并逐点验证该仿射格与有限指数盒不相交；总计检查 133029 个盒点，最大单状态盒为 5103 点。该结果为有限、规范、可复查的 F 证书，不是所有核心素数的全称选择器。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- F-state
- square-terminal
- relation-lattice
- smith-normal-form
- hermite-normal-form
- finite-fourier
- bounded-certificate
- proof-program
sources:
- claim: type-I-linear-half-block-kneser-square-terminal-profile
  role: square-terminal-state-scope
- claim: type-I-f-relation-lattice-certificate-reconstruction
  role: relation-lattice-verifier-interface
visibility: public
last_checked: '2026-07-30'
---

# 平方终端 F 状态的完整关系格短证书重建

## 证书对象

输入是 253 个已经去重的平方终端候选
\((p,R,\operatorname{source},E)\)。令

\[
K=\frac{pR+1}{4}=\prod_iq_i^{\nu_i}.
\]

在每个单位群 CRT 分量上取 (K) 的素因子离散对数，构造同余矩阵

\[
[A\mid-D].
\]

Smith 分解给出目标 \(-1\) 的一个整数原像 (z_0)，Hermite 正规形给出关系格

\[
\Lambda=\{z\in\mathbb Z^r:Az\equiv0\pmod D\}.
\]

目标指数纤维因此被规范写成仿射格

\[
z_0+\Lambda.
\]

证书验证四件事：

1. (A\Lambda\equiv0\pmod D)；
2. (Az_0\equiv\log(-1)\pmod D)；
3. \(|\det\Lambda|=|\mathcal H_R(K)|\)；
4. 逐点验证 \((z_0+\Lambda)\cap\prod_i[-\nu_i,\nu_i]=\varnothing\)。

## 冻结结果

结果文件
`reproductions/type-i-f-square-terminal-relation-certificate-results.json` 的 SHA-256 为

```text
53119e9aaeadac7080811782f3a3eb07f3cd6674dfb9a18776a3c5e68d108297
```

摘要为：

```text
state_count: 253
total_box_points_checked: 133029
maximum_box_size: 5103
all_target_in_generated_subgroup: true
all_target_outside_box: true
full_support_rank_with_two_histogram: {"0": 87, "1": 138, "2": 26, "3": 2}
```

这把半块 Kneser 剖面中的每个状态都升级为一个独立的有限 F 证书：目标确实位于
支撑子群，但有限指数预算不足以达到目标。`full_support_rank_with_two` 记录了
用虚拟二进方向 2 加 (K) 的规范素因子生成整个支撑子群所需的最少附加素因子数；
它只作为支撑接口，不被误当作有限盒命中。

## 边界与下一步

该证书证明的是“目标仿射格与当前盒不交”，并没有证明盒外最近点能够产生合法偶终端，
也没有给出跨状态容量矛盾。下一步应从证书中的目标原像、关系格基和低秩支撑中提取：

- 可比较的最小盒外溢出坐标；
- 对应素因子的 (q)-进高度需求；
- 或能接入奇数距离/广义 (2^j) 源的严格下降方向。

## 复现

```text
python3 reproductions/type_i_f_square_terminal_relation_certificate.py
```

脚本锁定平方终端输入和半块支撑剖面哈希，并逐点重建关系格和有限盒空缺。
