---
kind: claim
claim_id: type-I-linear-adversarial-core-f-block-alignment-profile-600m
title: 四个对抗核心全部 F 状态的块级鸽巢余量
statement: 对线性源分解 K=gamma*L，令 D_R(X)=A_R(X)A_R(X)^(-1)、H_L=<D_R(L)>、T_gamma={-x^(-1):x属于D_R(gamma)}。若 |D_R(L)|+|T_gamma∩H_L|>|H_L|，则一般B目标必命中；F型失败必满足相反的不等式。四个真实对抗核心的45个F状态、69个有向源全部满足该必要不等式，最小余量为0，正余量最小值为11；只有两个等号方向，其中一个为非平凡尖锐边界(p,R,a,s)=(57399241,455,150,841)，另一个因H_L={1}且T_gamma∩H_L为空而是空性等号。该结果是完整有限边界，不证明跨源选择器。
claim_status: computationally_reproduced
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- finite-exponent
- centered-spectrum
- divisor-lattice
- difference-set
- block-alignment
- pigeonhole-bound
- adversarial-core
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-29'
---

# 四个对抗核心全部 F 状态的块级鸽巢余量

## 块级充分条件

设 \(\gcd(K,R)=1\)，在线性源正规化中写

\[
K=\gamma L,
\qquad
\mathcal D_R(X)=\mathcal A_R(X)\mathcal A_R(X)^{-1},
\qquad
\mathcal A_R(X)=\{d\bmod R:d\mid X\}.
\]

由素数指数区间相加和单位群交换性，有

\[
\mathcal D_R(K)=\mathcal D_R(\gamma)\mathcal D_R(L).
\]

定义

\[
H_L=\langle\mathcal D_R(L)\rangle,
\qquad
T_\gamma=\{-x^{-1}:x\in\mathcal D_R(\gamma)\}.
\]

若

\[
\mathcal D_R(L)\cap T_\gamma\ne\varnothing,
\]

则 \(-1\in\mathcal D_R(K)\)，即一般 \(B\) 目标命中。另一方面，若状态是 F 型并且
目标仍未命中，则 \(\mathcal D_R(L)\) 与 \(T_\gamma\cap H_L\) 是 \(H_L\) 中的两个不交
集合，因此必有

\[
\boxed{
|\mathcal D_R(L)|+|T_\gamma\cap H_L|\le |H_L|.
}
\tag{1}
\]

所以严格违反 (1) 是一个块级的充分命中条件。它比只比较整个
\(\mathcal D_R(K)\) 与 \(\mathcal H_R(K)\) 的半密度更定向：只统计当前仿射块子群中真正
需要的目标拉回类。

## 全部四核心审计

输入为四个一般 \(B\) 唯一命中且全谱无 \(B=1\) 的真实对抗核心。此前已知共有 45 个 F 型
状态；恢复所有线性源方向后共有 69 个有向源。对每个块差集直接按素因子指数层构造，对
\(H_L\) 的阶和成员性使用单位群离散对数格证书，避免枚举大模数的整个单位群。

| \(p\) | F 状态数 | 有向源数 | 最小余量 | 等号方向数 |
| ---: | ---: | ---: | ---: | ---: |
| 878,089 | 2 | 4 | 21 | 0 |
| 26,034,649 | 6 | 8 | 49 | 0 |
| 57,399,241 | 24 | 36 | 0 | 2 |
| 283,319,689 | 13 | 21 | 100 | 0 |
| **合计** | **45** | **69** | **0** | **2** |

全体 69 个方向的目标对齐交集均为空。全局正余量中的最小值为 11，因此除了两个等号
方向外，没有接近违反必要不等式的方向。

## 两个等号边界

第一个等号方向为

\[
(p,R,a,s)=(57{,}399{,}241,455,150,841).
\]

其块数据为

\[
|H_L|=6,
\qquad
|\mathcal D_R(L)|=5,
\qquad
T_\gamma\cap H_L=\{391\}.
\]

右块差集恰好覆盖 \(H_L\) 中除 391 外的全部五类，而 391 正是唯一所需却未覆盖的类。
因此 (1) 取等号但目标仍不命中，这是该鸽巢条件的非平凡尖锐边界。

第二个等号方向为

\[
(p,R,a,s)=(57{,}399{,}241,7939,30,241).
\]

这里 \(|H_L|=1\)、\(|\mathcal D_R(L)|=1\)，且
\(T_\gamma\cap H_L=\varnothing\)。这是没有可用目标拉回类的空性等号，不提供新的
命中机制。

## 研究边界

该审计把 F 型状态的块级必要条件从全局半密度细化为定向拉回余量，但它没有排除所有
状态同时达到等号或保持正余量。因此不能把

\[
\text{块级鸽巢余量非负}
\]

升级为跨模数选择器定理。下一步应研究碰撞/过剩指数层是否能强制某个方向的余量变为负，
或者证明同一核心的另一 \(R\) 状态可以拉回当前缺失类；单纯提高
\(|\mathcal D_R(K)|\) 的全局密度仍不足够。

## 复现

~~~bash
python3 reproductions/type_i_linear_adversarial_core_f_block_alignment_profile_600m.py
python3 -m unittest tests/test_type_i_linear_adversarial_core_f_block_alignment_profile_600m.py -v
~~~
