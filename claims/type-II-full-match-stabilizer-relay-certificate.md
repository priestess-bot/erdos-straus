---
kind: claim
claim_id: type-II-full-match-stabilizer-relay-certificate
title: Type II 单纤维完整匹配的稳定子增长或商 relay 证书
statement: 设同一固定来源纤维中的完整匹配给出有限阿贝尔群 H 内的源块 B_i={1,g_i,...,g_i^{e_i}}。按顺序令 P_k=A_0 B_1...B_k、T_k=Stab_H(P_k)。每步稳定子单调增大；若 g_k 不属于 T_k，则 Kneser 给出 |P_k|>=|P_{k-1}|+|T_k|，若 g_k 属于 T_k 则该块被最终稳定子吸收。若 |A_0|+sum_{g_k notin T_k}|T_k|>|H|-|T_m|，任意未命中目标都矛盾，故直接命中；否则得到显式目标缺口和被吸收源块的 H/T_m 商 relay。该证书把 FIBER_REALIZED 的 FULL_MATCH 分支精化为增长终端或稳定子商，而不把匹配本身误作 Type II。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-hall-matching-fiber-realization-gate
  - type-II-private-factor-kneser-growth-stabilizer-bridge
  - type-II-source-fiber-finite-abelian-composition-relay
  - type-II-source-fiber-qheight-kneser-bridge
topics:
  - type-II
  - FULL_MATCH
  - stabilizer
  - Kneser
  - relay
  - finite-abelian
  - fixed-fiber
  - capacity
sources:
  - claim: type-II-hall-matching-fiber-realization-gate
    role: same-fiber-integer-realization
  - claim: type-II-private-factor-kneser-growth-stabilizer-bridge
    role: one-block-growth-or-absorption
  - claim: type-II-source-fiber-finite-abelian-composition-relay
    role: quotient-relay
  - claim: type-II-source-fiber-qheight-kneser-bridge
    role: q-height-to-product-set
visibility: public
last_checked: '2026-08-05'
---

# Type II 单纤维完整匹配的稳定子增长或商 relay 证书

## 1. 顺序积集和稳定子

固定一个已经通过 FIBER_REALIZED 的参数纤维，令 \(H\) 为其有限阿贝尔单位群，
\(A_0\subseteq H\) 为非空初始源积集。完整匹配选出的真实源块写成
\[
B_k=\{1,g_k,g_k^2,\ldots,g_k^{e_k}\},
\qquad 1\le k\le m.
\]
按匹配的规范顺序定义
\[
P_0=A_0,\qquad
P_k=P_{k-1}B_k,\qquad
T_k=\operatorname{Stab}_H(P_k).
\tag{1}
\]

若 \(x\in T_{k-1}\)，则 \(P_kx=P_k\)，所以
\[
T_{k-1}\le T_k.
\tag{2}
\]
稳定子沿顺序单调增大，最终得到 \(T_m\)。

## 2. 单步增长—吸收二分

对第 \(k\) 个块：

- 若 \(g_k\in T_k\)，则整个 \(B_k\subseteq T_k\)，称该块为
  ABSORBED；由 (2) 它也落入最终 \(T_m\)；
- 若 \(g_k\notin T_k\)，则 \(B_kT_k/T_k\) 至少有两个陪集。Kneser 不等式给出
  \[
  |P_k|
  \ge |P_{k-1}T_k|+|B_kT_k|-|T_k|
  \ge |P_{k-1}|+|T_k|.
  \tag{3}
  \]

记
\[
I=\{k:g_k\notin T_k\},
\qquad
J=\{k:g_k\in T_k\}.
\tag{4}
\]
迭代 (3) 得到
\[
|P_m|\ge |A_0|+\sum_{k\in I}|T_k|.
\tag{5}
\]

## 3. 目标命中或稳定子商 relay

令目标 \(t\in H\)。若
\[
|A_0|+\sum_{k\in I}|T_k|>|H|-|T_m|,
\tag{6}
\]
则必有
\[
t\in P_m.
\tag{7}
\]

### 证明

若反之 \(t\notin P_m\)，因为 \(P_mT_m=P_m\)，目标陪集
\(tT_m\) 与 \(P_m\) 不相交，从而
\[
|P_m|\le |H|-|T_m|.
\]
这与 (5)、(6) 矛盾。故 (7) 成立。证毕。

若 (6) 不成立且仍有 \(t\notin P_m\)，则得到可复核的缺口
\[
\delta_{\mathrm{stab}}
=
|H|-|T_m|-|A_0|-\sum_{k\in I}|T_k|
\ge0,
\tag{8}
\]
以及稳定子商
\[
\bar H=H/T_m,\qquad
\bar P_m=P_m/T_m,\qquad
\bar t=tT_m.
\tag{9}
\]
所有 \(k\in J\) 的源块在 \(\bar H\) 中变成单位块；它们不能再次计入商容量。
这给出
\[
\mathrm{STABILIZER\_ABSORPTION\_RELAY}
=(T_m,J,\delta_{\mathrm{stab}},\bar H,\bar P_m,\bar t).
\tag{10}
\]

## 4. 与完整匹配和 q-height 的接线

FULL_MATCH 只有在 FIBER_REALIZED 后才可调用本证书。q-height 账本把每个真实
匹配槽注入一个 \(B_k\)；同一 q 的重复层先合并，稳定子吸收块不产生新的独立
容量。于是：

1. (6) 成立时，Kneser 直接给出该纤维的 Type II 命中；
2. (6) 不成立时，(10) 把所有已吸收来源显式送入更小的稳定子商，未吸收块的
   累计增长和剩余缺口同时保存；
3. 若 \(\bar H\) 的目标缺失沿有限阿贝尔合成列落入较小商，且 source-switch/整数
   标签可提升，则 (10) 变成严格 relay；若落在顶层核，则进入 Fourier/锚点—秩
   分派；
4. 若来源来自不同纤维而没有 FIBER_REALIZED，不能构造共同的 \(P_k,T_k\)，只能
   记录 UNREALIZED_CROSS_STATE_MATCH。

因此本证书把 HC5 的“已匹配请求仍需终端”具体化为一个有限增长或商 relay 检查。

## 5. 最小例子

### 增长终端

若 \(H=C_5\)、\(A_0=\{1\}\)，取生成元 \(g\)，匹配块为
\(B_i=\{1,g^i\}\)（\(1\le i\le4\)），规范顺序的稳定子均为平凡群，
故
\[
|A_0|+\sum_{k=1}^4|T_k|=1+4>5-1.
\]
目标任意非单位元都被积集命中，得到 Type II。

### 吸收 relay

若 \(H=C_6\)、\(A_0=\{1,-1\}\)，而 \(g=-1\)，则第一步即
\(g\in T_1\)，块被吸收；最终 \(T_1\) 含该二方向，商中该源块为单位，
剩余目标缺口由 \(H/T_1\) 的 Fourier/合成列 relay 处理。该块不能按独立 q 层再次
收费。

## 研究边界

本证书严格处理同一参数纤维的 FULL_MATCH：它保证“累计非吸收增长超过缺口”
时直接命中，并在否则时给出稳定子商和精确缺口。它仍不证明每个稳定子商都有
可提升整数后继，也不把跨纤维完整匹配自动变成共同积集；这些仍由
FIBER_REALIZED 和 source-switch/严格势下降条件承担。
