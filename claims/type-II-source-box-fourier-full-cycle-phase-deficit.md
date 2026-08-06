---
kind: claim
claim_id: type-II-source-box-fourier-full-cycle-phase-deficit
title: Type II 源指数盒 Fourier 的整周期湮灭与相位深度缺口
statement: 对有限阿贝尔群中的带重数源指数盒，Fourier 系数逐源列精确分解为几何和。若某活跃列的角色像阶 d_i 整除 e_i+1，该角色系数严格为零；非零系数因此要求每个活跃列都有显式的相位深度缺口 r_i=(e_i+1) mod d_i 不为零。对 q-primary 角色 d_i=q^{a_i} 时，等价于 v_q(e_i+1)<a_i，并可输出 PHASE_DEPTH_DEFICIT。该证书只约束源侧相位，不把角色阶直接计为 q-height；只有通过源关系去重和真实 q-adic 载体提升后才可进入容量账本。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-kernel-fourier-source-relation-compatibility
  - type-II-source-fiber-qheight-kneser-bridge
  - type-I-fixed-layer-fourier-qadic-phase-bridge
topics:
- type-II
- source-box
- Fourier
- geometric-sum
- phase-depth
- q-adic
- collision-weight
- capacity-interface
- proof-boundary
sources:
  - claim: type-II-kernel-fourier-source-relation-compatibility
    role: source-relation-and-anchor-lift-gate
  - claim: type-II-source-fiber-qheight-kneser-bridge
    role: source-q-height-blocks
  - claim: type-I-fixed-layer-fourier-qadic-phase-bridge
    role: real-carrier-mapping-boundary
visibility: public
last_checked: '2026-08-05'
---

# Type II 源指数盒 Fourier 的整周期湮灭与相位深度缺口

## 1. 带来源的 Fourier 对象

令 \(G\) 为有限阿贝尔群，取源列 \(g_1,\ldots,g_r\in G\) 和指数盒

\[
\mathcal Z=\prod_{i=1}^r\{0,1,\ldots,e_i\},
\qquad
\phi(z)=\prod_i g_i^{z_i}.
\tag{1}
\]

因为指数盒可能有真实乘法碰撞，先使用源指数的带重数测度

\[
\mu_\phi(x)=\#\{z\in\mathcal Z:\phi(z)=x\}.
\tag{2}
\]

对角色 \(\chi\in\widehat G\)，定义源盒 Fourier 系数

\[
\widehat\mu_\phi(\chi)
=\sum_{z\in\mathcal Z}\overline{\chi(\phi(z))}.
\tag{3}
\]

这是带来源的指数证书；只有在 \(\phi\) 在盒上单射，或已经按真实碰撞商通过
源关系格仿射门之后，(3) 才能直接解释为无重数目标截面的 Fourier 系数。

## 2. 几何和分解

令

\[
\xi_i=\chi(g_i),
\qquad d_i=\operatorname{ord}(\xi_i),
\tag{4}
\]

约定 \(d_i=1\) 表示该列对角色不活跃。由乘积盒的独立坐标，

\[
\widehat\mu_\phi(\chi)
=\prod_{i=1}^r S_i(\chi),
\qquad
S_i(\chi)=\sum_{a=0}^{e_i}\overline{\xi_i}^{\,a}.
\tag{5}
\]

当 \(d_i>1\) 时写

\[
e_i+1=m_i d_i+r_i,
\qquad 0\le r_i<d_i.
\tag{6}
\]

将指数区间分成 \(m_i\) 个完整周期和一个余段，得到精确恒等式

\[
S_i(\chi)
=\sum_{a=0}^{r_i-1}\overline{\xi_i}^{\,a}
=
\begin{cases}
0,&r_i=0,\\[2mm]
\displaystyle\frac{1-\overline{\xi_i}^{\,r_i}}
{1-\overline{\xi_i}},&1\le r_i<d_i.
\end{cases}
\tag{7}
\]

因此，完整周期部分完全从该角色的源 Fourier 证书中消失；它不能再次被计作相位
需求。若 \(d_i=1\)，则 \(S_i=e_i+1\)。

## 3. 整周期湮灭定理

由 (5)--(7) 立即得到：

\[
\boxed{
\widehat\mu_\phi(\chi)\ne0
\quad\Longrightarrow\quad
r_i=(e_i+1)\bmod d_i\ne0
\text{ 对每个 }d_i>1\text{ 的列 }i.
}
\tag{8}
\]

等价地，若存在一个活跃列满足 \(d_i\mid e_i+1\)，则

\[
\widehat\mu_\phi(\chi)=0.
\tag{9}
\]

这不是幅度估计，而是一个逐列的零证书。若所有活跃列均通过 (8)，则源角色只
看见余段盒

\[
\mathcal Z_{\chi}^{\rm res}
=\prod_{d_i=1}\{0,\ldots,e_i\}
\times
\prod_{d_i>1}\{0,\ldots,r_i-1\},
\tag{10}
\]

并有

\[
\widehat\mu_\phi(\chi)
=\sum_{z\in\mathcal Z_{\chi}^{\rm res}}
\overline{\chi(\phi(z))}.
\tag{11}
\]

特别地，对每个 \(d_i>1\)，非零几何和满足

\[
\left|S_i(\chi)\right|
=\frac{\left|\sin(\pi r_i/d_i)\right|}
{\sin(\pi/d_i)}\ge1,
\tag{12}
\]

故

\[
\left|\widehat\mu_\phi(\chi)\right|
\ge\prod_{d_i=1}(e_i+1)
\quad\text{在 }\widehat\mu_\phi(\chi)\ne0\text{ 时成立}.
\tag{13}
\]

## 4. q-primary 相位深度回执

若 \(\chi\) 的相关像为 q-primary，且

\[
d_i=q^{a_i}\qquad(a_i>0),
\tag{14}
\]

则 (8) 等价于

\[
v_q(e_i+1)<a_i.
\tag{15}
\]

定义逐列相位缺口

\[
\delta_{i,q}(\chi)
=a_i-\min\{a_i,v_q(e_i+1)\}\ge1,
\tag{16}
\]

以及余段长度

\[
r_{i,q}(\chi)=(e_i+1)\bmod q^{a_i}
\in\{1,\ldots,q^{a_i}-1\}.
\tag{17}
\]

回执字段

    PHASE_DEPTH_DEFICIT = {
      character_order: q^a_i,
      column: i,
      height: e_i,
      residue_length: r_i,q,
      valuation_gap: delta_i,q
    }

是一个有限、可重算的源侧事实：该角色若要保持非零，必须避开
\(q^{a_i}\mid e_i+1\)。它把“角色阶与指数高度发生整周期相消”的边界显式化，
但不声称 \(\delta_{i,q}\) 本身就是清分高度或容量单位。

## 5. 与真实源关系和容量的接线

该引理的选择器接线固定为三步：

1. 先对带重数源盒计算 (5)。若某个活跃列满足 \(r_i=0\)，输出
   PHASE_FULL_CYCLE_ANNIHILATION，删除该候选 Fourier 角色，不进入容量账本；
2. 若所有活跃列 \(r_i>0\)，保存 (10)、(16) 的 PHASE_DEPTH_DEFICIT，再对指数
   碰撞商执行源关系格/锚点仿射相容性检查；
3. 只有角色已通过真实关系提升，并另有整数坐标
   \(\rho_i:\mathbb Z/d_i\mathbb Z\to\mathbb Z/q^{h_i}\mathbb Z\)、相位中心和
   嵌套同余时，才允许把 \(h_i\) 送入 F/G q 进容量合同。不能用 \(a_i\)、
   \(\delta_{i,q}\) 或 Fourier 幅度直接替代 \(h_i\)。

因此，该引理补的是“非零相位角色在源盒上实际留下了多少余段”的必要条件，和
现有的 source-relation lift gate、q-height bridge 是串联关系，而不是把抽象角色阶
直接升级为载体。

## 6. 小例子与边界

在 \(C_4\) 中令 \(g=1\)、\(e=3\)，取唯一非平凡角色 \(\chi(g)=i\)，则
\(d=4\)、\(e+1=4\)、\(r=0\)，所以几何和为零。若改为 \(e=2\)，则
\(r=3\)，几何和 \(1-i-1=-i\)，系数非零且 \(v_2(e+1)=0<2\)。

在 \(C_8\) 中取角色使 \(\chi(g)=-1\)，则 \(d=2\)。\(e=1\) 时
\(2\mid e+1\)，整周期湮灭；\(e=2\) 时余段长度为 1，角色只看到首项，
相位缺口为 \(a-v_2(3)=1\)。

若 \(\phi\) 在盒上有碰撞，(3) 是带来源测度的系数，不能未经处理地替换为
\(\widehat{1_P}\)。例如 \(g^2=1\)、\(e=3\) 时指数有重复；此时必须先按
\(L_G\) 去重，再使用源关系格判据。该限制防止把重复指数误计为额外容量。

## 7. 结论与未闭合边界

本引理给出了一个新的、完全代数的 Fourier 预筛：任何非零源盒角色都必须避开
每个活跃列的整周期条件，并携带明确的 q-primary 相位深度缺口。它可以立即删去
一批不可能进入容量账本的候选角色，也为后续真实载体映射提供有限的余段输入。

它没有证明以下更强结论：

* 相位缺口 \(\delta_{i,q}\) 自动对应某个 F/G 清分高度；
* 所有非零角色都可通过源关系商提升为无重数目标截面角色；
* 剩余余段需求跨状态必然超载，或失败必产生整数严格递降。

因此，PHASE_DEPTH_DEFICIT 是兼容 Fourier 到容量/递降桥的精确前置证书，
不是全局“短证书或递降”定理。
