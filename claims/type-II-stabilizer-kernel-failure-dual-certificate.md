---
kind: claim
claim_id: type-II-stabilizer-kernel-failure-dual-certificate
title: Type II 稳定子同余核失败的对偶 Fourier 二分
statement: 对源指数盒积集 P<=G 和候选核 K，若 K 不包含于 Stab(P)，则必有一个有限对偶证书。若 K 不包含于源子群 H=im(phi)，存在角色 chi 平凡于 H 而在某个 k in K 上非平凡；若 K<=H 但盒不具 K 不变性，则存在 k in K 和角色 chi 使 chi(k) != 1 且 P 的 Fourier 系数 hat(1_P)(chi) != 0。后者来自 1_P-1_{Pk} 的 Fourier 可逆性；若目标在商中伪命中，专门的目标陪集截面能量给出更强的 KERNEL_SPLIT_FOURIER。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-stabilizer-kernel-source-box-lattice-criterion
  - type-II-congruence-kernel-split-fourier-certificate
  - type-II-kernel-fourier-source-relation-compatibility
topics:
  - type-II
  - stabilizer
  - congruence-kernel
  - Fourier
  - annihilator
  - dual-certificate
  - source-lattice
  - quotient-descent
sources:
  - claim: type-II-stabilizer-kernel-source-box-lattice-criterion
    role: exact-kernel-failure-dichotomy
  - claim: type-II-congruence-kernel-split-fourier-certificate
    role: target-section-energy
  - claim: type-II-kernel-fourier-source-relation-compatibility
    role: lift-and-capacity-gate
visibility: public
last_checked: '2026-08-05'
---

# Type II 稳定子同余核失败的对偶 Fourier 二分

## 1. 设置

令 \(G\) 为有限阿贝尔群，真实源指数盒积集为
\[
P=\varphi(\mathcal B)\subseteq H=\operatorname{im}\varphi\le G,
\]
令 \(K\le G\) 是候选模数降阶同余核。要判断的是
\[
K\le\operatorname{Stab}_G(P).
\tag{1}
\]
源指数盒格判据把 (1) 的失败分成
\[
K\not\le H
\quad\text{或}\quad
K\le H\ \text{但}\ PK\ne P.
\tag{2}
\]

## 2. 源子群外置：annihilator 角色

若 \(K\not\le H\)，取 \(k_0\in K\setminus H\)。有限阿贝尔群
\(G/H\) 的对偶分离给出一个角色
\[
\chi\in\widehat G,\qquad
\chi|_H=1,\qquad
\chi(k_0)\ne1.
\tag{3}
\]
于是
\[
\chi(x)=1\quad(x\in P),
\]
而 \(\chi\) 对核方向 \(k_0\) 非平凡。记录
\[
\mathrm{KERNEL\_SOURCE\_ANNIHILATOR}
=(K,H,k_0,\chi).
\tag{4}
\]

### 证明

\(k_0H\) 是有限阿贝尔商 \(G/H\) 中的非单位元；有限阿贝尔群的角色分离
定理保证存在 \(\bar\chi\) 满足 \(\bar\chi(k_0H)\ne1\)。令
\(\chi=\bar\chi\circ(G\to G/H)\)，即得 (3)。证毕。

该角色的源和系数是纯单位相位；它不能被误报为目标命中，但若目标锚点或 F/G
载体也被分离，可进入环境 Fourier。若源关系格不包含该外置角色，则回执为
LIFT_OBSTRUCTED。

## 3. 源子群内但盒不饱和：平移差 Fourier

现在假设 \(K\le H\) 但 \(PK\ne P\)。存在 \(k\in K\) 使
\[
Pk\ne P.
\tag{5}
\]
令
\[
f_k=1_P-1_{Pk}.
\]
因平移是双射，\(f_k\ne0\)。有限阿贝尔 Fourier 变换可逆，故存在
\(\chi\in\widehat G\) 使
\[
\widehat f_k(\chi)\ne0.
\tag{6}
\]
而
\[
\widehat{1_{Pk}}(\chi)
=\overline{\chi(k)}\,\widehat{1_P}(\chi),
\]
所以
\[
\widehat f_k(\chi)
=(1-\overline{\chi(k)})\,\widehat{1_P}(\chi).
\tag{7}
\]
由 (6) 得到同时满足
\[
\boxed{
\chi(k)\ne1,\qquad
\widehat{1_P}(\chi)\ne0.
}
\tag{8}
\]
记录
\[
\mathrm{KERNEL\_BOX\_FOURIER}
=(K,k,\chi,\widehat{1_P}(\chi),\widehat f_k(\chi)).
\tag{9}
\]

### 规范选择

在固定的有限群坐标、核生成元排序和角色排序下，取使
\[
|\widehat f_k(\chi)|
\]
最大的最小 \((k,\chi)\)，即可把 (9) 变成与枚举路径无关的规范证书。

## 4. 与目标伪命中的关系

若目标 \(t\notin P\) 但 \(\pi(t)\in\pi(P)\)，目标陪集截面
\[
S_t=\{k\in K:tk\in P\}
\]
是非空真子集。此时
\[
\sum_{\chi\ne1}
\left|\sum_{k\in S_t}\overline{\chi(k)}\right|^2
=|S_t|(|K|-|S_t|)
\]
给出专门的 KERNEL_SPLIT_FOURIER，其系数直接测量目标陪集的非饱和程度；
它通常比 (9) 更强。若目标不在商中命中，则 (9) 仍是源盒不饱和的有限角色，
但不能单独声称 Type II。

## 5. 统一分派

稳定子核三分现在可按以下顺序回执：

1. KERNEL_STABILIZER_CERT：核被源盒稳定子吸收，进入饱和商；双重目标缺失时
   商阶严格下降；
2. KERNEL_SOURCE_ANNIHILATOR：核有源子群外置方向，角色平凡于所有源块；
3. KERNEL_BOX_FOURIER：核在源子群内但指数盒不饱和，角色同时看见源和核平移；
4. 目标商伪命中时优先输出 KERNEL_SPLIT_FOURIER；
5. 每个角色均须通过真实源关系格/SNF；通过者进入 F/G 或 q-height 容量，失败者
   记录 LIFT_OBSTRUCTED，不能把对偶角色直接写成递降。

这使同余核的三种失败都具有有限证书，但仍把“角色存在”与“整数解提升/严格
核心素数下降”严格分开。

## 6. \(p=97\) 的两类边界

对
\[
G=U(24),\quad H=\langle11\rangle=\{1,11\},\quad
K=\{1,5,13,17\},
\]
有 \(K\not\le H\)。商 \(G/H\) 的角色分离给出一个平凡于 \(\{1,11\}\)、
对某个 \(k\in K\) 非平凡的 KERNEL_SOURCE_ANNIHILATOR；这解释了为什么
模 \(4\) 的命中不能由该源盒回升。

若取一个 \(K\le H\) 但 \(P\) 只占据部分 \(K\)-纤维的抽象源盒，则 (7) 必给出
KERNEL_BOX_FOURIER；若目标也落在同一商陪集，则退化为前述目标截面证书。

## 研究边界

该二分证明稳定子核门失败时总有一个可复核的对偶角色，补上
KERNEL_NOT_IN_SOURCE/KERNEL_BOX_MISS 的 Fourier 出口。它仍不保证角色能通过源关系
格并产生 F/G 短证书或严格整数递降；这些仍是统一选择器的全局提升缺口。
