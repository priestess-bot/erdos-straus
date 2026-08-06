---
kind: claim
claim_id: type-I-linear-escape-primary-hole-capacity
title: 线性 escaped source 的 primary 幂块—目标缺口容量
statement: 设 Type II 当前积集 P 的稳定子商为 Gbar=G/T，缺口陪集数为 c。若 r 个通过整数 source-switch 的 escaped source 在某个 ell-初等商 rho:Gbar->V_ell 中线性独立，并各自提供幂块 B_i={1,u_i,...,u_i^{d_i}}，则幂块积集在 Gbar 中至少含有 prod_i min(d_i+1,ell) 个不同元素。故 c < prod_i min(d_i+1,ell) 时目标必被命中；目标仍缺失时该乘积必须 <=c，违反者给出 PRIMARY_HOLE_CAPACITY_DEFICIT 并强制 Type II/稳定子终端。d_i=1 时退化为 2^r 门；ell=2 时任一非零 d_i 立即使本初等层达到二元饱和。该结论是 q-height 到目标纤维的严格容量映射，不自动证明 source-switch 或 E1--E5。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-linear-block-escape-rank-hole-terminal
  - type-I-linear-block-escape-quotient-rank
  - type-II-qadic-height-kneser-block-bridge
  - type-II-multiblock-kneser-active-capacity-dichotomy
  - type-II-kneser-saturated-one-coset-hole-certificate
topics:
- type-I
- linear-source
- escape
- primary
- q-height
- target-fiber
- hole-capacity
- Kneser
- Type-II
- source-switch
- E1-E5
- proof-program
sources:
  - claim: type-I-linear-block-escape-rank-hole-terminal
    role: two-point-special-case
  - claim: type-II-qadic-height-kneser-block-bridge
    role: q-height-source-block
  - claim: type-II-multiblock-kneser-active-capacity-dichotomy
    role: stabilizer-capacity
visibility: public
last_checked: '2026-08-05'
---

# 线性 escaped source 的 primary 幂块—目标缺口容量

## 1. 稳定子商和可用幂块

令 \(G\) 为当前 Type II 目标群，\(P\subseteq G\) 为已有源块积集，
\(T=\operatorname{Stab}_G(P)\)，并写

\[
\bar G=G/T,\qquad
\bar P=PT/T,\qquad
C=\bar G\setminus\bar P,\qquad
c=|C|.
\tag{1}
\]

目标陪集 \(\bar t=tT\) 属于 \(C\)。取一个 \(\ell\)-初等商

\[
\rho:\bar G\longrightarrow V_\ell,
\qquad V_\ell\ \text{为有限 }\mathbb F_\ell\text{-向量空间}.
\tag{2}
\]

令 \(u_1,\ldots,u_r\) 是已经通过参数纤维、整数 source-switch、SNF、CRT、范围和
互素性检查的 escaped source，并假设

\[
v_i=\rho(u_i),\qquad
v_1,\ldots,v_r\ \text{线性独立}.
\tag{3}
\]

第 \(i\) 个 source 提供的合法 primary 幂块为

\[
B_i=\{1,u_i,u_i^2,\ldots,u_i^{d_i}\},
\qquad d_i\ge1.
\tag{4}
\]

没有通过 E1--E5 或整数回译的候选不能计入 \(d_i\)；它们只能保留为
SOURCE_UNCLOSED/ARITHMETIC_OBSTRUCTED。

## 2. 幂块积集的严格大小

令

\[
\bar R=B_1\cdots B_r.
\tag{5}
\]

在 \(V_\ell\) 中，第 \(i\) 个指数 \(e_i\in\{0,\ldots,d_i\}\) 的像为
\(e_i v_i\)，其中系数按模 \(\ell\) 计算。因此该坐标至少有

\[
m_i=\min(d_i+1,\ell)
\tag{6}
\]

个不同值。由于 \(v_1,\ldots,v_r\) 线性独立，不同的 \(r\)-元坐标值给出不同的
\(V_\ell\) 元素，从而在原商群中也不同。于是得到

\[
\boxed{
|\bar R|
\ge
\prod_{i=1}^{r}\min(d_i+1,\ell).
}
\tag{7}
\]

这一步只把每个 source 的合法 q-height 转成有限 primary 数字层，不把不同 q 的
整数高度相乘；乘积来自独立初等商坐标的组合数。

## 3. 缺口填洞门

补集恒等式为

\[
\bar G\setminus(\bar P\,\bar R)
=\bigcap_{\bar v\in\bar R}C\bar v.
\tag{8}
\]

若 \(\bar P\bar R\) 仍缺失某个商元素 \(\bar x\)，则
\(\bar x\bar R^{-1}\subseteq C\)，因此

\[
|\bar R|\le c.
\tag{9}
\]

结合 (7) 得到严格容量门

\[
\boxed{
c<
\prod_{i=1}^{r}\min(d_i+1,\ell)
\quad\Longrightarrow\quad
\bar P\bar R=\bar G.
}
\tag{10}
\]

若目标仍缺失，则必须满足必要条件

\[
\boxed{
\prod_{i=1}^{r}\min(d_i+1,\ell)\le c.
}
\tag{11}
\]

如果真实回译数据违反 (11)，输出

\[
\mathrm{PRIMARY\_HOLE\_CAPACITY\_DEFICIT}
\left(\ell,(d_i),c,\prod_i\min(d_i+1,\ell)\right),
\tag{12}
\]

并直接进入 Type II 命中或稳定子/商终端。若 (10) 成立且所有 E1--E5 通过，则
\(\bar t\in\bar P\bar R\) 回译为一个 Type II 短证书；若某个 E 门失败，只保留
FIBER_TARGET_FILLED_BUT_LIFT_OBSTRUCTED。

## 4. 特殊情况和层析解释

当所有 \(d_i=1\) 时，(10) 退化为

\[
c<2^r\Longrightarrow\text{目标命中},
\]

即上一轮的二点块终端。若 \(\ell=2\)，则
\(\min(d_i+1,2)=2\) 对所有 \(d_i\ge1\)，二进方向只按独立方向计数；增加高度不能
制造更多二进商元素，但仍可能在更高的非初等层贡献 Kneser 活跃容量。

若某个 \(d_i\ge\ell-1\)，其坐标在 \(V_\ell\) 中已经饱和，继续增加该 source 的
高度不再提高本初等层的填洞数；此时应转查更高 \(\ell^2,\ell^3\) 商或稳定子容量，
但本初等层的证书并不因此失效。这给出一个层级停机规则：

\[
d_i\ge\ell-1
\quad\Longrightarrow\quad
\text{本 }\ell\text{-初等层不再增加容量，转查高层或稳定子。}
\tag{13}
\]

## 5. 证明

对每个 \(i\)，指数区间 \(0,\ldots,d_i\) 在 \(\mathbb F_\ell\) 中有
\(\min(d_i+1,\ell)\) 个不同剩余类。独立性 (3) 使这些坐标的笛卡尔积注入
\(V_\ell\)，得到 (7)。若 \(\bar P\bar R\ne\bar G\)，从 (8) 取一个剩余元素即得
\(x\bar R^{-1}\subseteq C\)，从而 (9)；代入 (7) 得 (10)--(11)。E1--E5 通过时，
商命中由真实源块回译为原参数 Type II 证书；否则保存 lift obstruction。式 (13)
是 \(\ell\)-初等坐标的饱和定义。证毕。

## 6. 边界例子

### 高度产生新填洞能力

取 \(V_3=\mathbb F_3^2\)，两个独立源方向，\(d_1=d_2=2\)。则
\[
\prod_i\min(d_i+1,3)=3^2=9.
\]
若稳定子商缺口 \(c=8\)，式 (10) 强制目标命中；仅使用二点块时大小只有
\(2^2=4\)，无法得到这个结论。

### 初等层饱和

取 \(\ell=2\)、\(r=1\)、\(d_1=7\)。本初等商仍只有
\(\min(8,2)=2\) 个元素；若 \(c=2\)，本引理不强制命中，必须检查四阶或更高
\(2^j\) 层。

### 等号边界

若 \(\ell=3\)、\(r=2\)、\(d_1=d_2=1\)，容量为 \(4\)。当 \(c=4\) 时只能得到
\( \bar R\) 与缺口集等势的 HOLE_LOCKED 候选，不能把等号误报为 Type II。

## 7. 研究边界

本卡把 escaped source 的 q-height、初等商独立性和目标缺口连接成严格的乘积容量
不等式，覆盖二点 \(2^r\) 终端之外的高层分支。它仍不证明实际 alternate source
菜单完备，也不自动处理 \(\ell^2\) 以上的数字层、多个 primary 混合或 E1--E5
失败；这些分支必须继续进入高阶 Kneser/广义 \(2^j\)/annihilator 递降。
