---
kind: claim
claim_id: type-I-f-relation-lattice-certificate-reconstruction
title: 冻结 F 状态的关系格规范证书重建
statement: 对冻结的四个对抗核心中 45 个有限指数 F 状态，单位群离散对数与 Smith/Hermite 整数变换可以重建满秩关系格基、目标 -1 的仿射指数原像，并逐点验证指数盒与该仿射格不相交；总共检查 57159 个盒点。该结果是有限计算证书重建，不是全称 F 型结构定理。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- F-state
- finite-fourier
- relation-lattice
- smith-normal-form
- certificate
- reproducibility
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-context
visibility: public
last_checked: '2026-07-30'
---

# 冻结 F 状态的关系格规范证书重建

## 证书对象

对 \(K=\prod_iq_i^{\nu_i}\) 的素因子对数坐标，利用单位群分量上的离散对数矩阵 \(A\)
和分量阶对角矩阵 \(D\)，构造整数同余矩阵

\[
[A\mid-D].
\]

其整数核投影给出关系格

\[
\Lambda=\{z\in\mathbb Z^r:Az\equiv0\pmod D\}.
\]

Smith 分解和 Hermite 正规形提供规范的满秩基矩阵。对目标 \(-1\) 的单位群对数向量
\(b\)，同一 Smith 变换给出一个整数原像 \(z_0\)，于是目标原像是仿射格

\[
z_0+\Lambda.
\]

证书验证包含：

1. \(A\Lambda\equiv0\pmod D\)；
2. \(Az_0\equiv b\pmod D\)；
3. \(|\det\Lambda|=|H|\)；
4. 逐点检查 \((z_0+\Lambda)\cap B_\nu=\varnothing\)。

最后一项直接在有限指数盒中枚举，避免把短对偶向量的充分条件误写成必要条件。

## 冻结重建结果

复现脚本为

reproductions/type_i_f_relation_lattice_certificate.py

在四个冻结对抗核心的 45 个 F 状态上重建全部证书，逐点检查总计 57,159 个盒点；
每个状态都满足目标在生成群中但不在指数盒中。该结果把现有 F 型分类记录升级为可独立
验证的关系格对象，并为后续短对偶向量、平坦性或加法结构提取提供统一输入。

## 边界

该卡没有声称：

- 关系格一定有满足 \(W_\nu(y)<\operatorname{dist}(\langle y,z_0\rangle,\mathbb Z)\)
  的短向量；
- 45 个状态覆盖所有核心素数或全部线性状态；
- 关系格证书已经给出跨状态 \(q\)-进容量矛盾或严格可提升下降。
