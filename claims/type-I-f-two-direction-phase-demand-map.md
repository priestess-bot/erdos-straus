---
kind: claim
claim_id: type-I-f-two-direction-phase-demand-map
title: F 型关系格对偶的双方向相位需求映射
statement: 对冻结的 45 个 F 型状态，从目标仿射关系格选择一个系数盒 {-1,0,1}^r 中、目标相位非整数且至少有两个活跃坐标的对偶向量，并把目标相位方程投影到前两个活跃坐标，同时让其余坐标遍历完整指数盒。45 个状态均得到可验证的二维必要相位映射；其中 6 个二维投影为空，给出状态内的精确相位 F 证书，40 个最小选择为二维支撑、2 个为三维支撑、3 个为四维支撑。该结果不保证所选向量是最大 Fourier 系数，也不产生跨状态容量矛盾。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- F-state
- relation-lattice
- finite-fourier
- two-active
- phase-demand
- carrier
- q-adic
- cross-state
- certificate
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-context
visibility: public
last_checked: '2026-07-30'
---

# F 型关系格对偶的双方向相位需求映射

## 相位投影

设

\[
\Lambda=\ker\phi\subseteq\mathbb Z^r,
\qquad
\phi(z)=\prod_iq_i^{z_i},
\qquad
z_0+\Lambda=\phi^{-1}(-1).
\]

取 \(y\in\Lambda^*\) 并令

\[
\theta_i=y_i\pmod1,
\qquad
\tau=\langle y,z_0\rangle\pmod1.
\]

当 \(\tau\ne0\) 时，所有目标表示都必须满足

\[
\sum_i\theta_i z_i\equiv\tau\pmod1.
\tag{1}
\]

选两个活跃坐标 \(I=(i_1,i_2)\)，并令其余坐标在完整盒

\[
B_{\bar I}=\prod_{k\notin I}[-\nu_k,\nu_k]\cap\mathbb Z
\]

中变化。定义二维必要相位投影

\[
\mathcal P_I(\theta,\tau)=
\left\{(u_1,u_2):
\begin{array}{l}
u_j\in[-\nu_{i_j},\nu_{i_j}]\cap\mathbb Z,\\
\exists w\in B_{\bar I},\\
\theta_{i_1}u_1+\theta_{i_2}u_2+
\sum_{k\notin I}\theta_kw_k\equiv\tau\pmod1
\end{array}
\right\}.
\tag{2}
\]

若 \(\mathcal P_I=\varnothing\)，则指数盒内不存在任何满足该角色必要相位方程的点，
因此目标 \(-1\) 不可能命中；这是一张独立于完整平方除子枚举的状态内 F 证书。若
\(\mathcal P_I\ne\varnothing\)，它只给出必要投影，不能保证完整目标命中。

## 载体相位与颜色

在线性状态

\[
p=a+s+asR,
\qquad U=sR+1,
\qquad V=aR+1,
\qquad UV=4K,
\]

对 \(t\in\{s,a\}\) 定义载体高度

\[
\beta_t(q)=v_q(tR+1).
\]

若 \(2\not\mid K\)，相位只评价载体的奇部；若 \(2\mid K\)，则把 \(q=2\) 作为普通
支持坐标。载体的完整相位和所选二维部分分别为

\[
\Phi_t=\sum_{q\mid K}\theta_q\beta_t(q),
\qquad
\Phi_{t,I}=\theta_{i_1}\beta_t(q_{i_1})+
\theta_{i_2}\beta_t(q_{i_2})\pmod1.
\tag{3}
\]

因此每个状态可输出

\[
\bigl(q_{i_1},q_{i_2},t_{i_1},t_{i_2},
\beta_{t_{i_1}}(q_{i_1}),\beta_{t_{i_2}}(q_{i_2}),
\Phi_t,\Phi_{t,I}\bigr).
\tag{4}
\]

对每个方向取两个块中 \(q\)-进高度较大的块，平手时取 \(s\) 块，得到规范颜色对。
式 (3)--(4) 是相位到载体的精确记录；它没有把相位分母误当作 \(q\)-进高度下界。

## 冻结重建

输入为已经重建关系格的四个对抗核心中的 45 个 F 状态。对每个状态在
\(c\in\{-1,0,1\}^r\) 中按支撑大小、\(\ell_1\) 范数和字典序选取 \(y=\Lambda^{-*}c\)，
要求目标相位非整数且至少有两个活跃坐标；再取前两个活跃坐标作投影。结果为：

\[
\begin{array}{c|ccc}
\text{所选活跃支撑大小}&2&3&4\\ \hline
\text{状态数}&40&2&3
\end{array}
\]

规范高度优先颜色对为

\[
(a,a):29,\qquad(s,s):11,\qquad(s,a):4,\qquad(a,s):1.
\]

二维投影点数分布为

\[
\begin{array}{c|ccc}
|\mathcal P_I|&0&4&9\\ \hline
\text{状态数}&6&37&2.
\end{array}
\]

空投影的六个状态是

\[
\begin{array}{c|r|c}
p&R&(q_{i_1},q_{i_2})\\ \hline
878089&279&(73,601)\\
57399241&283&(331,172801)\\
57399241&7939&(5,19)\\
57399241&26947&(109,4831)\\
283319689&28107&(41,79)\\
283319689&2777643&(157,4423)
\end{array}
\]

这六条是有限状态内的相位空投影证书，不是新的素数范围结果。按
\((p,q_{i_1},q_{i_2},\text{颜色对},\tau_I)\) 分组后有 44 个需求组，仅
\((p,q_1,q_2,\text{颜色},\tau_I)=(26034649,379,941,(a,a),1/2)\) 重复两次；
规范高度优先二维联合高度乘积总和为 49。

完整相位、载体和投影载荷见
`reproductions/type-i-f-two-direction-phase-demand-results.json`。

## 逻辑边界

这张卡完成的是双方向关系格到相位/载体字段的精确映射。它仍没有证明：

- 选出的 \(y\) 是有限 Fourier 谱幅最大的规范角色；
- 不同状态必须重复使用同一个方向对、颜色对或相位需求；
- 非空二维投影一定产生目标表示或偶终端；
- 需求组超过双颜色交集容量，或能够构造严格可提升下降。

因此空投影分支可作为状态内 G/F 证书，非空分支必须继续进入双颜色交集容量或其它
算术下降证明。

## 复现

~~~bash
python3 reproductions/type_i_f_two_direction_phase_demand.py
~~~
