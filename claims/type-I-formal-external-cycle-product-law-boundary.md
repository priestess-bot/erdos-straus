---
kind: claim
claim_id: type-I-formal-external-cycle-product-law-boundary
title: 外部一层周期的带符号乘积律与自动终端边界
statement: 任意 m=1 形式周期的边标号 q_i 与相邻选中坐标的换向符号 epsilon_i 满足 prod q_i=prod epsilon_i (mod R)，并有相应整数闭圈恒等式。把标号分成 K 内、外部分后，原 K 中心盒命中精确等价于外部乘积被一个平移后的内部指数盒吸收；整圈关系本身不保证吸收，也不自然控制模外部 Q 的 Type I、Type II 或 K_Q 中心谱。核心例 (p,R,K)=(241,19,1145) 有全外部三周期但上述三个周期内终端同时失败；此外 R=3(mod8) 时外部 2 周期普遍存在。因此任何全称外部逃逸引理必须加入全局终端优先、源可达性或合法 support switch，不能只使用周期乘积。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - type-I-formal-cycle-representation-lattice-capacity
  - type-I-general-b-centered-square-spectrum
  - type-I-coprime-factor-normal-form
  - type-II-coprime-factor-normal-form
topics:
  - type-I
  - type-II
  - formal-target-pair
  - external-support
  - cycle-product
  - shifted-capacity-box
  - cross-chart
  - counterexample-boundary
  - terminal-first
sources:
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: full-excess-cycle-interface
  - claim: type-I-formal-cycle-representation-lattice-capacity
    role: multi-node-exponent-elimination
  - claim: type-I-general-b-centered-square-spectrum
    role: centered-spectrum-equivalence
visibility: public
last_checked: '2026-07-31'
---

# 外部一层周期的带符号乘积律与自动终端边界

## 1. 带符号整圈乘积律

考虑一个长度为 \(\ell\) 的 \(m=1\) 形式周期。第 \(i\) 条边在当前无序对中选中坐标
\(c_i\)，用素数 \(q_i\mid c_i\) 作迁移。在下一节点，第 \(i+1\) 条边选中的坐标要么是
\(c_i/q_i\)，要么是它相对 \(R\) 的补数。定义

\[
\varepsilon_i=
\begin{cases}
+1,&c_{i+1}=c_i/q_i,\\
-1,&c_{i+1}=R-c_i/q_i.
\end{cases}
\tag{1}
\]

这里循环下标满足 \(c_\ell=c_0\)。逐边都有

\[
q_i c_{i+1}\equiv\varepsilon_i c_i\pmod R.
\tag{2}
\]

全部周期坐标都与 \(R\) 互素，所以把 (2) 相乘并消去 \(\prod_i c_i\)，得到

\[
\boxed{
P:=\prod_{i=0}^{\ell-1}q_i
\equiv
\varepsilon:=\prod_{i=0}^{\ell-1}\varepsilon_i
\pmod R.}
\tag{3}
\]

这还有整数加强。令 \(\delta_i=(1-\varepsilon_i)/2\)，逐边等式为

\[
q_i c_{i+1}=\varepsilon_i c_i+\delta_i q_iR.
\tag{4}
\]

依次代入后有

\[
Pc_0=\varepsilon c_0+RN,
\tag{5}
\]

其中

\[
N=
\sum_{i=0}^{\ell-1}
\delta_i
\left(\prod_{j=0}^{i}q_j\right)
\left(\prod_{j=i+1}^{\ell-1}\varepsilon_j\right)
\in\mathbb Z.
\tag{6}
\]

式 (3) 是周期必然提供的最强无条件乘积合同；它尚未限制乘积中哪些素数可由 \(K\)
吸收。

## 2. 外部乘积的精确移位盒条件

对每个 \(r\mid K\)，令 \(t_r\) 为边标号序列中 \(r\) 的出现次数，并把全部外部标号
连乘为

\[
E=\prod_{q_i\nmid K}q_i.
\tag{7}
\]

于是

\[
P=E\prod_{r\mid K}r^{t_r}.
\tag{8}
\]

写 \(\nu_r=v_r(K)\)，定义平移盒

\[
\mathcal B_{R,K,t}=
\left\{
\prod_{r\mid K}r^{w_r}\pmod R:
-\nu_r-t_r\le w_r\le\nu_r-t_r
\right\}.
\tag{9}
\]

由 (3)、(8) 及 \(\varepsilon^{-1}=\varepsilon\)，精确有

\[
\boxed{
-1\in\mathcal C_R(K)
\quad\Longleftrightarrow\quad
-\varepsilon E\in\mathcal B_{R,K,t}.}
\tag{10}
\]

确实，对中心指数 \(z_r\in[-\nu_r,\nu_r]\) 令 \(w_r=z_r-t_r\)，则

\[
\prod r^{w_r}
=\left(\prod r^{z_r}\right)
\left(\prod r^{t_r}\right)^{-1}
\equiv-\varepsilon E\pmod R.
\tag{11}
\]

所以周期只把原问题改写成一个**移位容量吸收**问题。外部乘积 \(E\) 的存在或
\(P\equiv-1\pmod R\) 都不自动使 (10) 成立。

## 3. 三类外部 \(Q\) 终端活在不同模数

令 \(Q\equiv3\pmod4\) 为与 \(p\) 互素的正整数，并写

\[
x_Q=\frac{p+Q}{4},
\qquad
K_Q=\frac{pQ+1}{4}.
\tag{12}
\]

对任意与 \(Q\) 互素的 \(X\)，记

\[
\mathcal C_Q(X)=
\{dX^{-1}\pmod Q:d\mid X^2\}.
\tag{13}
\]

则外部缺口的三个完整判据可统一写成

\[
\begin{array}{rcl}
Q\text{ 为 Type I 缺口}
&\Longleftrightarrow&-p\in\mathcal C_Q(x_Q),\\
Q\text{ 为 Type II 缺口}
&\Longleftrightarrow&-1\in\mathcal C_Q(x_Q),\\
Q\text{ 作为新模数中心命中}
&\Longleftrightarrow&-1\in\mathcal C_Q(K_Q).
\end{array}
\tag{14}
\]

第二行的大小条件 \(d\le x_Q\) 不增加障碍：若某个 \(d\mid x_Q^2\) 命中 \(-1\)，
互补因子 \(x_Q^2/d\) 也命中，而两者中恰有一个小于 \(x_Q\)。

式 (3) 和 (10) 位于模 \(R\) 的单位群，(14) 位于模 \(Q\) 的单位群。没有额外的群同态、
因子恒等式或状态构造时，不能从前者推出后者。

## 4. 全外部负号周期仍可三重失败

取核心素数与状态

\[
p=241,
\qquad R=19,
\qquad K=\frac{pR+1}{4}=1145=5\cdot229.
\tag{15}
\]

完整超高图中有周期

\[
\{1,18\}
\xrightarrow{,q=2,}
\{9,10\}
\xrightarrow{,q=3,}
\{3,16\}
\xrightarrow{,q=3,}
\{1,18\}.
\tag{16}
\]

三个标号都在 \(K\) 支撑外。依次选中 \(18,9,3\) 时，换向符号为
\((+1,+1,-1)\)，所以

\[
P=2\cdot3\cdot3=18\equiv-1\pmod {19},
\tag{17}
\]

并且 (5) 在这里是

\[
(18+1)\cdot18=19\cdot18.
\tag{18}
\]

然而原中心谱为

\[
\mathcal C_{19}(1145)=\{1,4,5\},
\tag{19}
\]

不含 \(-1\equiv18\)。周期坐标产生的、满足普通外部菜单条件的唯一
\(Q\equiv3\pmod4\) 除数是 \(Q=3\)。此时

\[
x_3=61,
\qquad K_3=181.
\tag{20}
\]

两数都模 3 同余 1，所以它们的全部平方除子中心谱都只有 \(1\)。于是 (14) 的 Type I、
Type II 和跨模数中心三项全部 miss。

这不是 Erdős--Straus 猜想的反例。周期外的

\[
h=7,
\qquad x=62,
\qquad d=1
\tag{21}
\]

满足 Type II 判据 \(7\mid x+d\)，并恢复解

\[
(x,y,z)=(62,2169,134478).
\tag{22}

因此 (15)--(22) 精确否定的是“外部周期本身必产生现有终端”，同时支持先做全局终端
扫描再进入形式图。周期、三个 miss 与独立 Type II 解由
`reproductions/type_i_formal_cycle_multiplier_boundary.py` 逐项核验。

## 5. 二进周期说明外部性本身没有稀缺性

对任意奇 \(R\)，总选 \(\{x,R-x\}\) 的偶坐标并除以 2，在
\((\mathbb Z/R\mathbb Z)^\times/\{\pm1\}\) 上是置换 \([x]\mapsto[2^{-1}x]\)，故
一层节点自动分解成二进周期。核心状态满足 \(R\equiv3\pmod8\) 时 \(K\) 为奇数，这些
边全部是外部超高边。

所以外部周期不是一种可按数量稀缺性收费的异常事件。下一条仍可能成立的全称命题必须
至少限定到 terminal-first 后的源可达 \(\Psi_0=1\) 余核，并要求每个可达外部强连通分量
满足以下之一：移位盒吸收、某个周期或一步坐标触发 (14)，或产生带完整 E1--E5 与解提升
回执的合法 support switch。
