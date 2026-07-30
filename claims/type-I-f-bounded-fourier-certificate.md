---
kind: claim
claim_id: type-I-f-bounded-fourier-certificate
title: 冻结 F 状态的有界规范 Fourier 证书
statement: 对冻结的 45 个 F 型关系格状态，在对偶系数盒 {-1,0,1}^r 中保留目标相位非整数的候选，并按归一化 Dirichlet 乘积、角色阶、活跃支撑和系数字典序规范选择。45 个状态均得到可验证的非平凡 Fourier 证书，其归一化谱幅均达到 F 型目标缺失所需的 1/(|H|-1) 下界；最小幅度余量为 6.333... 倍。该结果是有界候选盒内的规范证书，不声称全角色最大值，也不产生跨状态容量矛盾。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- F-state
- finite-fourier
- relation-lattice
- bounded-certificate
- phase-budget
- q-adic
- capacity
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-context
visibility: public
last_checked: '2026-07-30'
---

# 冻结 F 状态的有界规范 Fourier 证书

## 证书规则

对关系格基 \(L\) 和目标仿射原像 \(z_0\)，令

\[
\Lambda=L\mathbb Z^r,
\qquad
\theta=L^{-T}c,
\qquad
c\in\{-1,0,1\}^r.
\]

保留非零 \(c\) 且

\[
\langle\theta,z_0\rangle\notin\mathbb Z.
\]

对每个预算 \(\nu_i\) 定义归一化 Dirichlet 因子

\[
f_{\nu_i}(\theta_i)
=
\frac{\left|\sum_{k=-\nu_i}^{\nu_i}
e^{2\pi i k\theta_i}\right|}{2\nu_i+1}.
\]

候选的谱质量为

\[
\mathsf M(\theta)=\prod_i f_{\nu_i}(\theta_i).
\]

在该有限候选集内按

\[
(-\mathsf M,\ \operatorname{ord}(\theta),\
|\operatorname{supp}\theta|,\ \|c\|_1,c)
\]

字典序选取首个候选。这里的第一项按高精度实数比较，角色相位和载体指数均保留为
有理数；因此证书的离散部分不依赖浮点离散对数或枚举顺序。

## F 型下界验证

若 \(H\) 是支撑素因子生成的有限群，纯指数盒的目标表示数为零，则有限 Fourier 展开
给出某个非平凡角色满足

\[
\mathsf M(\theta)\ge\frac1{|H|-1}.
\]

本次冻结重建并非枚举全部 \(|H|\) 个角色，而是验证上述有界候选中所选角色已经满足
这个必要下界。结果为：

\[
\begin{array}{c|c}
\text{字段}&\text{结果}\\ \hline
\text{状态数}&45\\
\text{对偶系数盒}&\{-1,0,1\}^r\\
\text{最小 }\mathsf M/(|H|-1)^{-1}&6.3333333333\\
\text{中位 }\mathsf M/(|H|-1)^{-1}&4057.0490167
\end{array}
\]

所选角色的活跃支撑大小分布为

\[
1:2,\quad2:24,\quad3:2,\quad4:7,\quad5:5,\quad6:3,\quad7:2.
\]

这给出一个重要的结构修正：稳定子商的活跃方向数与有界 Fourier 规范角色的实际
活跃支撑不必相同。冻结样本中有两个角色只含一个活跃素因子，故单活跃
Fourier—载体桥不能只被视为抽象特例；但它仍只闭合这两个已冻结状态的证书接口。

## 载体与相位预算

对线性状态的两个块

\[
U=sR+1,\qquad V=aR+1,
\]

对每个活跃 \(q_i\) 按 \(q_i\)-进高度较大者选择颜色，并记录

\[
\bigl(q_i,\ \theta_i,\ \operatorname{color},\
v_{q_i}(U),\ v_{q_i}(V)\bigr).
\]

同时保存角色阶、目标相位、归一化谱质量和截断相位预算

\[
W(\theta)=
\sum_i\min\{1,\nu_i^2\|\theta_i\|_{\mathbb R/\mathbb Z}^2\}.
\]

这样每一张 F 证书都同时拥有：

1. 关系格中的有理对偶向量；
2. 可验证的 Fourier 下界余量；
3. 活跃素因子—颜色—\(q\)-进高度载荷；
4. 可输入跨状态容量的相位预算。

对两个单活跃角色进一步直接计算 \(\mathcal A_R(K)\) 的稳定子。它们的固定层稳定子
均为平凡群，因而商群阶仍分别为 \(7456\) 和 \(47022136\)；所选 \(qT\) 的阶分别为
\(1864\) 和 \(11755534\)，均不生成整个商群。这说明“某个 Fourier 角色只在一个
\(q\) 上非平凡”不等于“稳定子商只有一个活跃方向”，现有单活跃循环商桥不能仅凭
角色支撑大小直接套用。

## 逻辑边界

本卡没有证明：

- 所选角色是全部有限角色中的全局 Fourier 最大角色；
- 有界系数盒对所有核心素数都一定找到满足下界的角色；
- 不同状态的角色必须共享同一个素数、颜色或相位键；
- 相位预算可以直接转成同一标签差上的整数高度需求；
- 因而尚未得到跨状态容量矛盾、算术下降或全称 Type I/II 选择器。

它把“规范 F 角色”从抽象存在性推进为可重复的有限证书，并揭示稳定子活跃方向与
Fourier 活跃支撑之间的差异；下一步仍是把该证书的相位质量严格拉回共同载体容量或
可提升势函数。

## 复现

~~~bash
python3 reproductions/type_i_f_bounded_fourier_certificate.py
~~~
