---
kind: claim
claim_id: type-II-dyadic-target-fiber-top-class-packing-short-relation
title: Type II 二进顶位源类的二^r 装箱—短关系引理
statement: 在固定状态的有界指数盒中，若最大二进深度目标类去重后的不同源像数超过 2^r，则两个表示落在同一符号盒，因而在原预算内产生一个进入最大深度子群 L_d=2^{d+1}K 的非零源关系；若不超过 2^r，则该层只能输出至多 2^r 个源标签的有限边界菜单，不能从装箱本身强制关系。两种分支都必须把最大深度类在 H/L_d 中记为一个容量单位。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-dyadic-target-fiber-max-depth-relay
  - type-II-dyadic-target-fiber-maximal-quotient-dedup
  - type-I-target-fiber-density-neighbor-fourier-trichotomy
  - type-II-kernel-fourier-source-relation-compatibility
topics:
  - type-II
  - dyadic
  - target-fiber
  - packing
  - short-relation
  - source-relation
  - capacity
  - SNF
  - proof-program
sources:
  - claim: type-II-dyadic-target-fiber-max-depth-relay
    role: maximum-depth-layer-and-antipodal-relay
  - claim: type-II-dyadic-target-fiber-maximal-quotient-dedup
    role: unique-top-class-and-capacity-deduplication
  - claim: type-I-target-fiber-density-neighbor-fourier-trichotomy
    role: sign-cell-packing-pattern
  - claim: type-II-kernel-fourier-source-relation-compatibility
    role: source-relation-lattice-and-lift-interface
  - reproduction: reproductions/dyadic_target_fiber_max_depth.py
    role: packing-control-and-relation-receipt
visibility: public
last_checked: '2026-08-09'
---

# Type II 二进顶位源类的二^r 装箱—短关系引理

## 设置

令 \(H\) 为有限阿贝尔群，\(K=\langle\kappa\rangle\simeq C_{2^a}\) 为核，
\(\phi:\mathbb Z^r\to H\) 为由 \(r\) 个源生成元给出的同态，并令

\[
\mathcal B_\nu=\prod_{i=1}^r[-\nu_i,\nu_i]\cap\mathbb Z^r.
\]

固定目标 \(t\) 和源像集 \(S=\phi(\mathcal B_\nu)\)，假设

\[
t\notin S,
\qquad
F_t=\{k\in K:t+k\in S\}\ne\varnothing,
\qquad
0\notin F_t.
\]

按二进深度令

\[
d=\max_{k\in F_t}\operatorname{dep}_2(k),
\qquad
L_d=2^{d+1}K,
\qquad
F_t^{(d)}=\{k\in F_t:\operatorname{dep}_2(k)=d\}.
\]

定义最大深度表示集

\[
\mathcal Z_d=\{z\in\mathcal B_\nu:\phi(z)-t\in F_t^{(d)}\}.
\]

从 \(\mathcal Z_d\) 中对每个不同源像 \(\phi(z)\) 只保留一个指数代表，得到

\[
\mathcal Z_d^{\mathrm{red}}.
\]

这一步是必要的：指数碰撞 \(\phi(z)=\phi(z')\) 只能说明源关系格中的零元，不能重复向目标纤维或 Hall/q 容量收费。

## 装箱—短关系二分

把每个坐标区间分为两个符号区间

\[
I_i^-=[-\nu_i,0],
\qquad
I_i^+=[1,\nu_i].
\]

空的 \(I_i^+\) 不产生新格子，故总符号盒数至多为

\[
T_r=2^r.
\]

则有以下严格二分：

\[
\boxed{
|\mathcal Z_d^{\mathrm{red}}|>2^r
\Longrightarrow
\texttt{SHORT_DYADIC_LAYER_RELATION}.
}
\tag{1}
\]

更具体地，存在不同的 \(z,z'\in\mathcal Z_d^{\mathrm{red}}\)，它们属于同一符号盒，
满足

\[
|z_i-z_i'|\le\nu_i\quad(1\le i\le r),
\qquad
\Delta=z-z'\ne0,
\tag{2}
\]

并且

\[
\phi(\Delta)=\phi(z)-\phi(z')
\in L_d\setminus\{0\}.
\tag{3}
\]

因此 \(\Delta\) 是原指数预算内的非零源关系，其核坐标二进深度至少为
\(d+1\)。若 \(\mathcal L_G=\ker\phi\) 是源关系格，则它给出

\[
\Delta\in\phi^{-1}(L_d)\setminus\mathcal L_G,
\qquad
[\Delta]\ne0
\text{ in }\phi^{-1}(L_d)/\mathcal L_G.
\tag{4}
\]

这个商类可直接交给已有 SNF、CRT 或核 Fourier lift 判据；关系可能比 \(d+1\)
更深，但不会回到 \(L_d\) 之外。

反之，若

\[
|\mathcal Z_d^{\mathrm{red}}|\le2^r,
\tag{5}
\]

装箱只输出有限回执

\[
\texttt{TOP_CLASS_PACKING_BOUNDARY}
\]

以及不超过 \(2^r\) 个代表和源标签。此分支并不声称不存在别的短关系；它只说明
“最大深度顶位类的去重表示”本身不足以由符号装箱强制出关系，必须转向边界菜单、
其它深度、跨状态容量或整数提升检查。

## 证明

将 \(\mathcal Z_d^{\mathrm{red}}\) 按每个坐标的 \(I_i^-\) 或 \(I_i^+\) 归类。
这些类至多有 \(2^r\) 个。若表示数超过 \(2^r\)，抽屉原理给出同一类中的
\(z\ne z'\)。由于同一符号区间的直径不超过 \(\nu_i\)，得到 (2)。

由 \(z,z'\in\mathcal Z_d\)，存在 \(k,k'\in F_t^{(d)}\) 使

\[
\phi(z)=t+k,
\qquad
\phi(z')=t+k'.
\]

最大深度去重引理给出 \(k-k'\in2^{d+1}K=L_d\)。又因保留的是不同源像，
\(\phi(z)\ne\phi(z')\)，故 \(k-k'\ne0\)，从而得到 (3) 和 (4)。若表示数不超过
\(2^r\)，则直接得到 (5) 的有限边界菜单。证毕。

## 与商容量和 Type II 提升的接口

最大深度层在 \(H/L_d\) 中只有一个源类

\[
\omega_d=2^d\kappa+L_d.
\]

所以无论 (1) 还是 (5) 分支，规范商容量都只能记为

\[
\kappa_{\mathrm{top}}(s,d)=1
\quad\text{(固定状态和固定层)}.
\tag{6}
\]

在 (1) 分支，关系回执可以有三种后续用途：

1. 若 \(\Delta\) 满足已有 Type II 正规化和整数可提升条件，则生成短证书；
2. 若只满足有限群关系而不满足 E1--E5，则输出带明确标签的
   \texttt{LIFT_OBSTRUCTED}，不能把它误记为整数解；
3. 若关系进入更深的 \(2^{d+2}K\) 层，则把它作为新的 q-adic 进位或严格递降候选，
   但仍需证明状态量严格下降。

在 (5) 分支，所有代表必须保留来源标签、SNF 类和参数纤维；不能因同一个商类的
多次表示而复制 Hall/q 容量。若不同状态或不同参数纤维各自实现了顶位类，只有在
source-CRT 和 FIBER_REALIZED 检查通过后才可合并。

## 控制实例

取

\[
H=C_2\times C_{16},
\quad
g_1=(1,1),\quad g_2=(0,2),
\quad
\mathcal B=[-2,2]^2,
\quad
t=(1,0).
\]

最大深度为 \(d=0\)，最大深度层有 6 个不同源像，而
\(2^r=2^2=4\)。例如

\[
z=(-1,-2),
\qquad
z'=(-1,-1),
\qquad
\Delta=(0,-1),
\]

且

\[
\phi(\Delta)=(0,14)\in2K\setminus\{0\}.
\]

这正是预算内的 \texttt{SHORT_DYADIC_LAYER_RELATION}。同一复现器还保留了严格商、
普通短关系、顶层终端和 \(t\in K\) 固定点四个控制分支。

## 边界

本引理只解决“顶位源类过密时必有预算内二进关系”的有限群组合门；它没有证明
每个核心素数的顶位去重表示都超过 \(2^r\)，也没有自动完成从 (4) 到整数
E1--E5 的提升。因此全局证明仍需一个覆盖所有 \texttt{TOP_CLASS_PACKING_BOUNDARY} 的
跨状态容量或良基递降定理。

## 复现

~~~bash
python3 -m py_compile reproductions/dyadic_target_fiber_max_depth.py
python3 reproductions/dyadic_target_fiber_max_depth.py --verify
~~~

复现器会报告 \texttt{top_representative_count}、\texttt{packing_bound}、同符号盒碰撞、
非零层关系和关系深度；没有超过 \(2^r\) 时则将 \texttt{packing_pair} 留空。

