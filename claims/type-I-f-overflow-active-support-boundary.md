---
kind: claim
claim_id: type-I-f-overflow-active-support-boundary
title: 分色 F 状态的盒溢出不局限于规范 Fourier 活跃支持
statement: 对冻结的 291 个分色 F 状态，在扩张指数盒半径不超过 6 的范围内找到 253 个目标仿射格见证；其中 32 个见证的溢出只落在规范活跃素因子、199 个同时落在活跃和非活跃素因子、22 个只落在非活跃素因子。788 个溢出坐标层中 342 个属于活跃支持、446 个不属于。因而溢出到载体的桥不能只在规范双活跃方向内建立。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-split-color-overflow-radius-boundary
  - type-I-f-overflow-to-carrier-conditional-capacity
topics:
- type-I
- F-state
- relation-lattice
- overflow-radius
- finite-fourier
- q-adic
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-context
visibility: public
last_checked: '2026-07-30'
---

# 分色 F 状态的盒溢出不局限于规范 Fourier 活跃支持

## 审计定义

对 291 个分色 F 状态，令 \(B_\nu\) 为原始指数盒，按每个坐标同时扩张的半径
\(\delta\) 搜索目标仿射格的一个见证。对找到的见证 \(z\)，将

\[
\operatorname{excess}_i=(|z_i|-\nu_i)_+
\]

非零坐标按其素因子是否属于该状态选定的规范 Fourier 活跃集合分类。扫描半径上限为
6；未找到见证的状态不被解释为目标不存在。

## 结果

\[
\begin{array}{c|r}
\text{字段}&\text{数量}\\ \hline
\text{状态总数}&291\\
\text{半径 }\le6\text{ 找到见证}&253\\
\text{半径 }\le6\text{ 未找到}&38\\
\text{仅活跃支持溢出}&32\\
\text{活跃与非活跃混合溢出}&199\\
\text{仅非活跃支持溢出}&22
\end{array}
\]

按溢出层计数，788 个非零坐标层中有 342 个落在规范活跃支持，446 个落在非活跃
素因子坐标。半径分布为

\[
87,73,36,27,17,13
\]

分别对应 \(\delta=1,2,3,4,5,6\)。

## 对容量桥的含义

此前的条件性接口假设溢出层数可以直接记到双颜色 Fourier 活跃对
\((q_a,q_s)\) 上。上述支持分流表明，这个假设不是一般的状态内事实：即使目标仿射格
在扩张盒中出现，最先出现的见证也可能需要非活跃素因子坐标。

因此可行的下一步必须允许至少三种需求：

1. 规范活跃方向的双颜色联合需求；
2. 非活跃但属于 \(K\) 的溢出支持需求；
3. 多坐标溢出在不同素因子之间迁移时的联合下界。

这不是对 Fourier 证书的否定。它说明“规范角色支撑”与“几何最短溢出支撑”是两个
不同对象，不能未经证明地使用同一容量键。

## 逻辑边界

该结果是半径六以内的有限见证审计。38 个未找到见证的状态仍可能在更大半径命中；
非活跃支持也不等于没有算术载体。当前唯一可靠结论是：二维活跃对的溢出—高度映射
不能覆盖全部分色状态，必须扩展到多活跃/多支持容量或构造递降势函数。

## 复现

```bash
python3 reproductions/type_i_f_overflow_support_boundary.py
```

结果文件：

```text
reproductions/type-i-f-overflow-support-boundary-results.json
```
