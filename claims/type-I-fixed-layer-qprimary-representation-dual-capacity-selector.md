---
kind: claim
claim_id: type-I-fixed-layer-qprimary-representation-dual-capacity-selector
title: 固定层稳定子商的 q-primary 表示—对偶—容量选择器
statement: 设 \(J\subset H\) 含单位元，\(P=\operatorname{Stab}_H(J)\)，\(X\le P^\perp\) 是非平凡 q-primary 角色子群。对 \(r\) 个残余生成元的有限指数盒，令 \(N_y\) 为目标 \(y\) 的精确 \(J\)-表示数，\(C_{y,X}\) 为目标陪集 \(yX^\perp\) 的表示数，\(T_J=|J|2^r\)、\(V=|J|\prod_i(2\nu_i+1)\)。按近邻、商陪集饱和、q-primary Fourier 缺口、低密度容量的顺序，四个条件互斥且穷尽；Fourier 分支存在非平凡 \(\chi\in X\) 使 \(-\operatorname{Re}(\overline{\chi(y)}F_J(\chi))\ge(V-|X|C_{y,X})/(|X|-1)\)，且稳定子商系数精确乘以 \(|P|\)。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fixed-layer-stabilizer-defect-reduction
  - type-I-target-fiber-primary-filtered-density-fourier-relay
  - type-I-target-fiber-neighbor-terminal
  - type-I-target-fiber-neighbor-dyadic-normalization
topics:
- type-I
- F-state
- G-state
- fixed-layer
- stabilizer
- q-primary
- representation
- Fourier
- capacity
- selector
- generalized-dyadic
- proof-program
sources:
  - claim: type-I-fixed-layer-stabilizer-defect-reduction
    role: stabilizer-quotient-and-coefficient-lift
  - claim: type-I-target-fiber-primary-filtered-density-fourier-relay
    role: q-primary-filtered-density-identity
  - claim: type-I-target-fiber-neighbor-terminal
    role: same-fixed-layer-neighbor-terminal
  - reproduction: reproductions/type_i_fixed_layer_qprimary_selector.py
    role: four-branch-and-stabilizer-controls
visibility: public
last_checked: '2026-08-09'
---

# 固定层稳定子商的 q-primary 表示—对偶—容量选择器

## 1. 设置

用乘法记号令 \(H\) 为有限阿贝尔群，\(1\in J\subseteq H\)，并令
\[
P=\operatorname{Stab}_H(J)=\{h:hJ=J\},\qquad \pi:H\longrightarrow\bar H=H/P.
\]
给定 \(g_i\in H\)、指数盒
\[
\mathcal B_\nu=\prod_{i=1}^r[-\nu_i,\nu_i]\cap\mathbb Z^r,\qquad
\Phi(z)=\prod_i g_i^{z_i},\qquad
V=|J|\prod_i(2\nu_i+1),\qquad T_J=|J|2^r.
\]
取 \(X\le P^\perp\cong\widehat{\bar H}\) 为非平凡 q-primary 角色子群，记
\(m=|X|>1\)、\(K_X=X^\perp\)，并定义
\[
N_y=\#\{(j,z)\in J\times\mathcal B_\nu:j\Phi(z)=y\},\qquad
C_{y,X}=\#\{(j,z):j\Phi(z)\in yK_X\},
\]
\[
F_J(\chi)=\sum_{j\in J}\sum_{z\in\mathcal B_\nu}\chi(j\Phi(z)).
\tag{1}
\]
阈值 \(T_J\) 而不是 \(2^r\) 是必要的：近邻终端要求两条表示共享同一个固定层元素 \(j\)。

## 2. 四分支

在目标支撑非空的前提下，按下列顺序输出唯一分支：

1. **NEIGHBOR_TERMINAL**：若 \(N_y>T_J\)，则存在同一个 \(j\) 和不同的
   \(z,w\in\mathcal B_\nu\)，它们位于同一符号盒，故 \(|z_i-w_i|\le\nu_i\)。
   在 Type I 单位群模型中 \(j\Phi(z)=j\Phi(w)=y\)，所以它们是同一目标指数
   纤维的近邻对，可调用近邻终端及其广义 \(2^j\) 归一化。

2. **Q_PRIMARY_QUOTIENT_SATURATED**：若 \(N_y\le T_J\) 且
   \(C_{y,X}>T_J\)，则 q-primary 商 \(H/K_X\) 的目标陪集饱和。该回执不把
   固定层碰撞直接写成整数命中。

3. **Q_PRIMARY_FIXED_LAYER_FOURIER_DEFICIT**：若
   \(N_y\le T_J\)、\(C_{y,X}\le T_J\) 且 \(V>mT_J\)，则存在
   \(\chi\in X\setminus\{1\}\) 使
\[
\boxed{
-\operatorname{Re}\bigl(\overline{\chi(y)}F_J(\chi)\bigr)\ge
\frac{V-mC_{y,X}}{m-1}>0.}
\tag{2}
\]

4. **Q_PRIMARY_FIXED_LAYER_BOX_CAPACITY**：若前三个数量条件中的最后一个反向，
   即 \(V\le mT_J\)，则记录
\[
\boxed{V\le |X|\,|J|\,2^r.}
\tag{3}
\]

若 \(y\notin J\langle g_1,\ldots,g_r\rangle\)，先输出固定层支撑分离；当该支撑是
子群或陪集时，这就是通常的 G 型商分离，否则只承诺精确的空支撑证书。

## 3. 证明

由 \(1\in J\)，对 \(x\in P\) 有 \(x=x\cdot1\in xJ=J\)，故 \(P\subseteq J\) 且
\(JP=J\)。因为 \(X\le P^\perp\)，有 \(P\subseteq K_X\)，而 \(X\) 是
\(\widehat{H/P}\) 的角色子群。角色正交关系给出
\[
\sum_{\chi\in X}\overline{\chi(y)}\chi(t)=m\,\mathbf1_{t\in yK_X}.
\tag{4}
\]
对 \(t=j\Phi(z)\) 求和，得到
\[
\sum_{\chi\in X}\overline{\chi(y)}F_J(\chi)=mC_{y,X},
\qquad F_J(1)=V.
\tag{5}
\]
因此非平凡角色的实部总和为 \(mC_{y,X}-V\)。在分支 3 中它至多
\(mT_J-V<0\)，除以 \(m-1\) 即得 (2)；分支 4 是互补容量不等式。
若 \(N_y>T_J\) 而没有同一 \(j\) 的近邻对，则每个 \(j\) 的 \(2^r\) 个符号盒至多
包含一个 \(z\)，从而 \(N_y\le|J|2^r=T_J\)，矛盾。证毕。

## 4. 稳定子商缩放

令 \(\bar J=\pi(J)\)，\(\bar F_{\bar J}\) 为商群 Fourier 和。对
\(\chi=\bar\chi\circ\pi\in X\)，\(J\) 是 \(P\)-周期集，所以
\[
\boxed{F_J(\chi)=|P|\,\bar F_{\bar J}(\bar\chi).}
\tag{6}
\]
过滤计数同样满足 \(C_{y,X}=|P|\,\bar C_{\pi(y),X}\)，但固定目标的精确计数在商化
时不乘 \(|P|\)：每个商表示对固定 \(y\) 恰有一个 \(j\in J\) 的提升。因此 Fourier
缺口在商群中等价于
\[
-\operatorname{Re}\bigl(\overline{\bar\chi(\pi(y))}
\bar F_{\bar J}(\bar\chi)\bigr)\ge
\frac{V/|P|-mC_{y,X}/|P|}{m-1}.
\tag{7}
\]
这正是固定层无周期化后 q-primary 对偶的精确系数，不把 \(|P|\) 重复计入单点目标。

## 5. typed 边界与验证

| 分支 | certificate_type | recursive_edge_eligible |
|---|---|---|
| 近邻 | target_fiber_neighbor | 仅 E1--E5 适配器通过时为真 |
| 商饱和 | q_primary_quotient_saturated | false |
| Fourier | fixed_layer_qprimary_fourier_deficit | false |
| 低密度 | fixed_layer_qprimary_capacity | false |

复现器 reproductions/type_i_fixed_layer_qprimary_selector.py 在加法循环群中验证四个
分支、Fourier 下界和非平凡稳定子下的 \(|P|\) 缩放。该选择器补上固定层与 q-primary
过滤之间的表示—对偶—容量接口，但 Fourier source-map、整数提升、跨状态容量和
良基递降仍需单独证明；因此它不是猜想的全称证明。
