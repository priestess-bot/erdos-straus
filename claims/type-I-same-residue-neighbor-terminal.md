---
kind: claim
claim_id: type-I-same-residue-neighbor-terminal
title: 任意同余纤维近邻终端引理
statement: 设 K=prod_i q_i^{nu_i} 且 R 为奇数。若同一指数盒中的两个不同向量 z,w 满足逐坐标距离 |z_i-w_i|<=nu_i，并且 prod_i q_i^{z_i}=prod_i q_i^{w_i} (mod R)，则定向后的比值产生 E=4K prod_i q_i^{z_i-w_i}，满足 E|4K^2、E=1 mod R、E<=4K-4R，并给出正的 4 的倍数终端 n=(4K-E)/R。若全盒大小 prod_i(2nu_i+1)>2^{omega(K)}|H_R(K)|，则必有某个任意剩余类纤维包含这样的近邻对。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- same-residue
- target-fiber
- representation
- near-pair
- even-terminal
- finite-abelian-groups
- packing
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-terminal-selector-context
visibility: public
last_checked: '2026-07-29'
---

# 任意同余纤维近邻终端引理

## 定理

设 \(R\) 为奇数，\(K=\prod_{i=1}^r q_i^{\nu_i}\)，并令

\[
B_\nu=\prod_{i=1}^r[-\nu_i,\nu_i]\cap\mathbb Z^r.
\]

对 \(t\in\mathcal H_R(K)\) 定义任意剩余类纤维

\[
\mathcal Z_t
=
\left\{
z\in B_\nu:
\prod_iq_i^{z_i}\equiv t\pmod R
\right\}.
\]

若不同的 \(z,w\in\mathcal Z_t\) 满足

\[
|z_i-w_i|\le\nu_i\qquad(1\le i\le r),
\]

则交换 \(z,w\) 后可令

\[
\rho=\prod_iq_i^{z_i-w_i}\in(0,1).
\]

令 \(U=K\rho\)、\(E=4U\)。则

\[
U\in\mathbb Z,\qquad U\mid K^2,\qquad U\equiv K\pmod R,
\]

并且

\[
E\mid4K^2,\qquad E\equiv1\pmod R,\qquad E\le4K-4R.
\]

因此

\[
n=\frac{4K-E}{R}
\]

是正的 \(4\) 的倍数，且在 \(4K=pR+1\) 时满足 \(0<n<p\)。

### 证明

逐坐标距离给出
\(0\le\nu_i+z_i-w_i\le2\nu_i\)，所以

\[
U=\prod_iq_i^{\nu_i+z_i-w_i}
\]

是整数且整除 \(K^2\)。同一剩余类纤维给出
\(\rho\equiv1\pmod R\)，故 \(U\equiv K\pmod R\)。方向选择给出
\(0<U<K\)；二者同余于 \(R\)，于是 \(K-U\ge R\)，从而
\(E\le4K-4R\)。最后
\[
n=\frac{4(K-U)}R
\]

是正整数和 \(4\) 的倍数。与目标纤维引理相同的端点奇偶性论证给出 \(n<p\)。证毕。

## 全盒装箱推论

把每个坐标区间 \([-\nu_i,\nu_i]\) 划分成两个直径不超过 \(\nu_i\) 的子区间，
例如 \([-\nu_i,0]\) 与 \([1,\nu_i]\)（零归入前一块）。指数盒因而被分成
\(2^r\) 个小盒。

若某个纤维 \(\mathcal Z_t\) 的大小超过 \(2^r\)，则同一小盒中有两个不同表示，
定理立即给出偶终端。进一步，所有纤维总数为
\[
\prod_i(2\nu_i+1),
\]
而纤维的索引群大小为 \(|\mathcal H_R(K)|\)。所以

\[
\boxed{
\prod_i(2\nu_i+1)>2^r|\mathcal H_R(K)|
\Longrightarrow
\text{存在任意同余纤维近邻对，进而存在偶终端}.
}
\]

## 逻辑边界

该引理推广了目标纤维近邻终端：目标纤维只是 \(t=-1\) 的一个特殊纤维。
全盒装箱只保证某个剩余类有近邻，不保证该类是 \(-1\)，因此它不能单独构造
核心素数的 Type I 目标证书。它适合用作终端接口和表示重数分支，目标命中仍需
另外的支撑逃逸、有限盒饱和或 Type II 出口。
