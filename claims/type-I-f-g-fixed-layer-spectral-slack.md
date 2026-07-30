---
kind: claim
claim_id: type-I-f-g-fixed-layer-spectral-slack
title: F 型固定层的 Fourier 谱余量约束
statement: 对有限阿贝尔群 H 中的非空固定层 J 和指数盒，若目标 t 的表示数为零，则任何满足规范 Fourier 下界的角色 chi 都满足 g_J(chi) product_i f_nu_i(theta_i) >= 1/(|H|-1)，其中 g_J 是固定层归一化谱因子。因此其截断相位预算满足 sum_i min(1,nu_i^2 delta_i^2) <= 60 log((|H|-1)g_J(chi))，比忽略固定层得到的 60 log(|H|-1) 严格更强；相应有限阶分母预算也同步收紧。该约束仍是状态内对偶证书，不自动产生跨状态载体容量矛盾。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- finite-fourier
- fixed-layer
- F-state
- dual-certificate
- phase-budget
- relation-lattice
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

# F 型固定层的 Fourier 谱余量约束

## 表示数与固定层因子

令 \(H\) 为有限阿贝尔群，\(J\subseteq H\) 为非空固定层，生成元为
\(q_1,\ldots,q_r\)，预算为 \(\nu_i\)，目标为 \(t\)。设

\[
g_J(\chi)=\frac{1}{|J|}\left|\sum_{j\in J}\chi(j)\right|,\qquad
f_{\nu}(\theta)=\frac{|D_\nu(e^{2\pi i\theta})|}{2\nu+1}.
\]

若目标表示数 \(N_J(t)=0\)，有限 Fourier 展开给出一个非平凡角色 \(\chi\) 满足

\[
g_J(\chi)\prod_{i=1}^r f_{\nu_i}(\theta_i)\ge\frac1{|H|-1},
\qquad
\chi(q_i)=e^{2\pi i\theta_i}.
\tag{1}
\]

因为左侧不为零，\(g_J(\chi)>0\)，且 (1) 还强制

\[
(|H|-1)g_J(\chi)\ge1.
\tag{2}
\]

## 谱余量预算

对每个坐标使用初等 Dirichlet 核衰减

\[
f_{\nu_i}(\theta_i)\le
\exp\left(-\frac1{60}\min\{1,\nu_i^2\delta_i^2\}\right),\qquad
\delta_i=\|\theta_i\|_{\mathbb R/\mathbb Z}.
\tag{3}
\]

将 (3) 代入 (1)，得到

\[
\boxed{
\sum_i\min\{1,\nu_i^2\delta_i^2\}
\le
60\log\bigl((|H|-1)g_J(\chi)\bigr).
}
\tag{4}
\]

右侧非负由 (2) 保证。与不记录固定层时的
\(60\log(|H|-1)\) 相比，固定层贡献了精确的谱余量

\[
60\log\frac1{g_J(\chi)}
\]

的预算收缩。若 \(g_J(\chi)=1\)，恢复无固定层修正；若 \(g_J(\chi)\) 很小，角色必须
在更多有权坐标上更接近平凡。

## 有限阶分母形式

令 \(d_i=\operatorname{ord}(\chi(q_i))\)。对非平凡坐标有
\(\delta_i\ge1/d_i\)，故 (4) 进一步给出

\[
\boxed{
\sum_{\chi(q_i)\ne1}\min\left\{1,\left(\frac{\nu_i}{d_i}\right)^2\right\}
\le
60\log\bigl((|H|-1)g_J(\chi)\bigr).
}
\tag{5}
\]

## 用途与边界

式 (4)--(5) 给规范 F 型证书增加一个可计算的固定层负载字段：

- fixed_layer_spectral_factor = g_J(chi)
- phase_budget = 60*log((|H|-1)*g_J(chi))
- denominator_budget 使用同一右端

它可以用于三种后续分流：

1. 预算很小：进入低阶商、关系格短向量或加法临界结构；
2. 预算仍大但活跃支撑固定：进入高度优先载体和联合容量；
3. 两者均不成立：必须证明产生新的可提升状态。

本卡不声称 \(g_J\) 的小值必然导致目标命中，也不把状态内相位预算直接变成跨状态
共同 \(q\)、共同颜色或统一联合高度；这些仍是统一选择器的未闭合桥梁。
