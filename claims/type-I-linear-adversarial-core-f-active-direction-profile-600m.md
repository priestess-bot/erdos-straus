---
kind: claim
claim_id: type-I-linear-adversarial-core-f-active-direction-profile-600m
title: 四个真实对抗核心的 F 型活跃方向下界
statement: 对四个一般 B 唯一命中且全谱无 B=1 的真实对抗核心，45 个有限指数 F 状态按精确稳定子 T=Stab_H(A_R(K)) 计算活跃素因子方向 qA_R(K) != A_R(K)。活跃方向数分布为 3 个状态有 3 个、9 个有 4 个、13 个有 5 个、12 个有 6 个、8 个有 7 个；因此该压力集没有单一活跃素因子 F 状态。这是有限负边界，不是全称结论。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- F-state
- finite-exponent
- stabilizer
- active-prime
- multi-active
- cross-state
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-spectrum-context
visibility: public
last_checked: '2026-07-29'
---

# 四个真实对抗核心的 F 型活跃方向下界

## 定义

对每个有限指数 F 状态，令

\[
\mathcal A_R(K)=\{d\bmod R:d\mid K\},
\qquad
\mathcal H_R(K)=\langle q\bmod R:q\mid K\rangle,
\qquad
T=\operatorname{Stab}_{\mathcal H_R(K)}(\mathcal A_R(K)).
\]

一个素因子 \(q\mid K\) 称为活跃方向，当且仅当

\[
q\mathcal A_R(K)\ne\mathcal A_R(K).
\]

由于 \(q\in\mathcal H_R(K)\)，这等价于 \(q\notin T\)；活跃方向数正是商群
\(\mathcal H_R(K)/T\) 中非平凡素因子方向的数量。

## 冻结压力集结果

输入为四个真实对抗核心

\[
p\in\{878089,26034649,57399241,283319689\},
\]

完整谱中共有 45 个 F 型状态。逐状态从 \(K\) 的全部除子构造
\(\mathcal A_R(K)\)，再对每个素因子直接测试左乘是否保持该集合；结果为

\[
\begin{array}{c|ccccc}
\text{活跃方向数}&3&4&5&6&7\\ \hline
\text{状态数}&3&9&13&12&8
\end{array}
\]

特别地，45 个状态均至少有三个活跃方向；单一活跃素因子模型在该压力集上没有实例。
全部状态共有 238 次活跃方向出现、99 个不同活跃素因子；990 对状态中有 599 对共享
至少一个活跃方向。出现次数最多的三个方向是 \(q=2,3,5\)，分别出现 24、23、16 次。
这些数值仍是冻结压力集的结构剖面，不是对所有核心素数的统计定理。

## 研究含义

这项结果把已有的单活跃素因子跨状态容量界定位为排除性工具，而不是当前对抗核心的
主模型。若要在这些状态上建立统一选择器，证书必须至少处理三个同时非平凡的方向，
例如：

1. 用多维关系格控制三个方向的指数盒缺口；
2. 用多层 Kneser/Kemperman 结构把三方向缺口转成目标纤维近邻；
3. 将不同活跃素因子的共享幂分别拉回标签差和模数差，再证明联合容量不足。

因此，继续只证明“一奇素因子 F 障碍不能重复”不能覆盖这 45 个真实压力状态；下一步
需要一个至少三方向的联合证书或严格可提升转移。

## 证据范围

这是四个有限对抗核心的完整审计，不推出所有核心素数都具有三个活跃方向，也不证明
多活跃 F 状态必然命中。它只说明统一选择器的下一个数学对象应从单方向容量升级为
多方向容量。

## 复现

~~~bash
python3 reproductions/type_i_linear_adversarial_core_f_active_direction_profile.py
~~~

结果文件：
[type-i-linear-adversarial-core-f-active-direction-profile-600m-results.json](../reproductions/type-i-linear-adversarial-core-f-active-direction-profile-600m-results.json)
