---
kind: claim
claim_id: type-I-formal-reach-odd-combination-box-rigidity
title: 形式可达节点的奇组合不能返回 F 态容量盒
statement: 固定线性 F 状态 (p,R,K)，把任一形式可达节点 (A,B,m) 写成扩展素数支撑上的指数向量 z，使 A/B=prod q^z_q。任意整数系数组合 z=sum c_v z_v 的相位只由系数和奇偶决定：prod q^z_q=(-1)^(sum c_v) mod R。若系数和为奇数、全部外部坐标消去且内部坐标落回 |z_q|<=v_q(K)，便得到原中心目标盒中的 Type I 命中，与 F 定义矛盾。因此 Smith 或关系格组合不能把 F 态修回 K 盒；外部消元成功后必留下内部容量超限，或必须保留外部支撑并另行构造直接终端或合法换支撑。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-formal-ranked-pruning-and-external-gap-selector
  - type-I-formal-single-external-smith-parity-selector
  - type-I-f-g-fourier-obstruction-certificate
topics:
  - type-I
  - F-state
  - formal-target-pair
  - representation-lattice
  - Smith-normal-form
  - capacity
  - rigidity
  - proof-boundary
sources:
  - claim: type-I-formal-single-external-smith-parity-selector
    role: external-row-cancellation-interface
  - claim: type-I-f-g-fourier-obstruction-certificate
    role: F-state-target-box-definition
visibility: public
last_checked: '2026-07-31'
---

# 形式可达节点的奇组合不能返回 F 态容量盒

## 定理

固定一个线性 F 状态

\[
4K=pR+1,
\qquad
K=\prod_{q\in\mathcal Q}q^{\nu_q}.
\tag{1}
\]

设 \(v=(A_v,B_v,m_v)\) 是从缺陷见证经形式迁移得到的任一可达节点，因而

\[
A_v+B_v=Rm_v,
\qquad
(A_v,B_v)=1.
\tag{2}
\]

在包含 \(\mathcal Q\) 及全部节点素因子的有限扩展支撑 \(\mathcal Q^*\) 上，唯一写成

\[
\frac{A_v}{B_v}=\prod_{q\in\mathcal Q^*}q^{z_{v,q}}.
\tag{3}
\]

对有限个节点和任意整数系数 \(c_v\)，令

\[
z=\sum_vc_vz_v,
\qquad
C=\sum_vc_v.
\tag{4}
\]

则

\[
\boxed{
\prod_{q\in\mathcal Q^*}q^{z_q}\equiv(-1)^C\pmod R.
}
\tag{5}
\]

特别地，不存在同时满足下列三项的组合：

1. \(C\) 为奇数；
2. 对每个 \(q\in\mathcal Q^*\setminus\mathcal Q\)，有 \(z_q=0\)；
3. 对每个 \(q\in\mathcal Q\)，有 \(|z_q|\le\nu_q\)。

## 证明

由 (2) 可知 \(A_v\equiv-B_v\pmod R\)。若某素数同时整除 \(B_v\) 与 \(R\)，它也
整除 \(A_v\)，与互素性矛盾；所以 \(B_v\) 在模 \(R\) 下可逆。于是每个节点都满足

\[
\prod_q q^{z_{v,q}}
=A_vB_v^{-1}
\equiv-1\pmod R.
\tag{6}
\]

将 (6) 取整数幂并相乘，立即得到 (5)。若上述三项同时成立，则 (5) 的左端只使用
\(K\) 的素数支撑，且指数落在原盒

\[
\mathcal B_K=\prod_{q\mid K}[-\nu_q,\nu_q].
\]

因为 \(C\) 为奇数，它又表示目标相位 \(-1\)。这正是一张原图表中心 Type I 盒命中，
与状态为 F 的定义矛盾。

若 \(C\) 为偶数，组合相位为 \(+1\)，也不能表示目标 \(-1\)。故整数线性组合没有第三种
奇偶选择可以绕过结论。

## 对 Smith 与容量路线的含义

单外部行或多外部行的 Smith 消元仍有价值，但它只能区分两类失败：

- 没有奇系数和的外部消元关系时，得到 `MISS_EXTERNAL`；
- 存在这种关系时，内部结果必越出 \(\mathcal B_K\)，得到 `MISS_CAPACITY`。

因此“组合多个 Reach 节点后回到原 \(K\) 盒”不能成为 F 态的新出口；若真回到盒中，
它只是在反证状态并非 F。组合路线要产生证明增量，必须保留某个外部 slab 并独立恢复
Type I/II 或跨图表终端，或者构造满足状态合同、能引入或移除外部支撑的可提升边。

本定理不排除这些外部输出，也不声称某个直接 gap 或合法 support switch 必然存在。
