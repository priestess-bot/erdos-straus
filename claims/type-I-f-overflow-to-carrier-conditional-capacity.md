---
kind: claim
claim_id: type-I-f-overflow-to-carrier-conditional-capacity
title: 分色 F 状态的盒溢出到载体高度的条件性容量接口
statement: 在冻结的 291 个分色 F 状态上，582 个双向载体组的基准需求/容量比全部为 1。若能证明目标仿射格的盒溢出半径 delta 至少在两个载体方向之一中产生 delta 层可比较的 q 进高度消耗，则单位层和最小乘积加权需求都会使 582 个组全部严格超载；该条件性接口把剩余缺口精确化为溢出到载体的算术映射。
claim_status: conditional
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-full-cross-color-pair-capacity-boundary
  - type-I-f-split-color-overflow-radius-boundary
  - type-I-f-square-obstruction-carrier-census
topics:
- type-I
- F-state
- relation-lattice
- overflow-radius
- q-adic
- colored-capacity
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-context
visibility: public
last_checked: '2026-07-30'
---

# 分色 F 状态的盒溢出到载体高度的条件性容量接口

## 已知基准

在冻结完整线性谱中，291 个不能在同一颜色承载两个活跃 Fourier 方向的 F 状态，
经双颜色交集选择产生 582 个定向载体组。对每个组按

\[
(p,q_a,q_s)
\]

聚合，需求为

\[
D_0=h_a h_s,
\]

容量为同一 (R) 窗口内全部线性源块的精确和

\[
C=\sum v_{q_a}(aR+1)v_{q_s}(sR+1).
\]

冻结结果是

\[
D_0=C
\]

对 582 个组全部成立；因此未经额外权重的双颜色容量只能达到饱和。

## 条件性溢出假设

令 (deltage1) 为目标仿射格首次进入扩张指数盒的溢出半径。需要证明一个新的
算术映射：若目标表示需要溢出 (delta)，则对应的载体高度增量 (x,yge0) 满足

\[
\max(x,y)\ge\delta.
\tag{A}
\]

这里 (x) 和 (y) 分别记在 (q_a) 与 (q_s) 方向上。条件 (A) 不是当前关系格
定义的直接推论；溢出是指数坐标的几何缺陷，载体高度是 (aR+1,sR+1) 的整数
整除性，二者之间的算术桥尚未证明。

## 条件性超载推论

若 (A) 成立，则

\[
(h_a+x)(h_s+y)
\ge
h_ah_s+\delta\min(h_a,h_s).
\tag{B}
\]

因此可以定义两个诊断需求：

\[
D_{\mathrm{unit}}=D_0+\delta,
\qquad
D_{\mathrm{min-prod}}=D_0+\delta\min(h_a,h_s).
\]

用溢出审计的截断半径（半径大于 4 的记录以 (delta=5) 作为下界）重算，结果为：

\[
\begin{array}{c|c|c|c}
\text{需求模型}&\text{组数}&\text{超载组}&\max(D/C)\\ \hline
\text{基准 }D_0&582&0&1\\
\text{单位层 }D_{\mathrm{unit}}&582&582&6\\
\text{最小乘积 }D_{\mathrm{min-prod}}&582&582&6
\end{array}
\]

所以只要把任意正的溢出成本严格拉回同一双颜色容量账本，就会立即得到跨状态
超载；不需要再增加载体种类。

## 逻辑边界

本卡的超载结论以 (A) 为条件，不能反向证明 (A)。当前尚未解决的关键问题是：

- 关系格坐标的最小溢出是否必然对应某个 (q)-进幂的增加；
- 溢出方向如何与规范的 (q_a,q_s) 颜色选择对齐；
- 多坐标溢出时，额外层数能否避免在不同素数方向间迁移；
- 溢出表示是否仍保持合法的 Type I/II 提升方向。

因此本卡是一个条件性研究接口和反例定位工具，不是选择器定理。下一步应尝试在
二维关系格的 Smith 坐标、同余链或标签—模数差刚性下证明 (A) 的某个受限版本。

## 复现

```bash
python3 reproductions/type_i_f_overflow_weighted_cross_capacity.py
```

结果文件：

```text
reproductions/type-i-f-overflow-weighted-cross-capacity-results.json
```
