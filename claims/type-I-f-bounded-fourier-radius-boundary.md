---
kind: claim
claim_id: type-I-f-bounded-fourier-radius-boundary
title: 冻结完整线性谱的 F 型 Fourier 系数盒半径边界
statement: 在 200 个冻结压力素数的完整线性谱中，2752 个 F 型状态均在系数盒 {-1,0,1}^r 中找到目标相位非整数的对偶候选；其中 2748 个候选达到 Fourier 缺失下界，4 个状态未达到。对这 4 个状态，将对偶系数盒扩大到 {-2,...,2}^r 仍未改善，但扩大到 {-3,...,3}^r 后全部达到下界，所需最小半径均为 3。这是有限复杂度边界，不是所有核心素数的统一半径定理。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- F-state
- finite-fourier
- relation-lattice
- bounded-certificate
- complexity-boundary
- cross-state
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-context
visibility: public
last_checked: '2026-07-30'
---

# 冻结完整线性谱的 F 型 Fourier 系数盒半径边界

## 完整谱结果

输入是 200 个压力素数的完整线性谱，其中有限指数 F 型状态共

\[
2752
\]

个。对每个状态重建关系格和 \(-1\) 的仿射原像，在
\(c\in\{-1,0,1\}^r\) 中保留目标相位非整数的候选，并按归一化 Fourier 乘积、
角色阶、支撑大小和系数字典序选取。

结果：

\[
\begin{array}{c|r}
\text{条件}&\text{状态数}\\ \hline
\text{有界候选达到 }1/(|H|-1)&2748\\
\text{有界候选未达到该下界}&4
\end{array}
\]

四个边界状态为

\[
\begin{array}{c|c|c}
p&R&\text{半径 1 的谱幅/下界比}\\ \hline
139224409&163&0.7054547936\\
247324009&19&2.7282\times10^{-16}\\
355341529&499&0.7584840915\\
405660649&19&3.3467\times10^{-16}
\end{array}
\]

因此，四个真实对抗核心上的“半径 1 全部通过”是局部事实，不能直接外推到完整
200 点谱。

## 半径修复

对四个边界状态扫描对称系数盒
\(\{-r,\ldots,r\}^d\)。半径 \(2\) 对四个状态都没有改善；半径 \(3\) 时四个状态
均达到 Fourier 缺失所需的

\[
\mathsf M(\theta)\ge\frac1{|H|-1}
\]

下界，且四个状态的最小充分半径都为 \(3\)。

这给出一个可操作的“短 Fourier 证书复杂度”字段：

\[
\rho_{\mathrm{Fourier}}(R,K)
=
\min\{r:\text{半径 }r\text{ 的对偶盒含有达标候选}\}.
\]

在当前冻结完整谱中，\(\rho_{\mathrm{Fourier}}\le3\) 对四个失败边界成立；但其余 2748
个状态的最小半径是否都为 1，尚未作为独立全量字段保存。

## 对统一选择器的意义

这项边界把“短证书”从固定的 \(\{-1,0,1\}\) 盒推广为一个可测复杂度，而不是无条件
宣称固定小盒足够。后续跨状态容量应把

- Fourier 系数盒半径；
- 角色阶和活跃支撑；
- 相位预算；
- 载体颜色与 \(q\)-进高度

作为联合证书字段。若半径增大导致活跃支撑或载体方向发生变化，不能继续使用半径 1
的容量分组。

本卡是冻结样本的边界复现，不证明存在一个适用于所有核心素数的绝对半径，也没有
证明 Fourier 复杂度可以直接转成算术下降。

## 复现

~~~bash
python3 reproductions/type_i_f_bounded_fourier_radius_boundary.py
~~~
