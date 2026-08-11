---
kind: claim
claim_id: type-II-p-minus-one-jacobi-source-snf-rank-one-anchor-dichotomy
title: p-1 因子 Type II 的 Jacobi 源关系 SNF 秩一压缩与锚点二分
statement: >-
  对 p=4U+1=4qr+1、m=4q-1、x=U+q 的 p-1 因子 Type II 状态，把 x 的不同
  素因子作为指数源列。Jacobi 符号给出一行规范的 F2 源关系评价矩阵
  beta=(beta_ell)，它恒 annihilate 全部乘法关系格；其源商像的 F2 秩恰为
  0（负源集为空）或 1（负源集非空），与负素因子数量无关。负源为空时
  -1 不在源支撑群内并给出 G 分离；负源非空时若 -1 在源支撑群内，则
  Jacobi 源—目标 SNF 系统显式相容，若有界 signed box 仍 miss，缺口不在
  C2 投影而在 ker(Jacobi) 的奇阶/完整关系几何中。若 -1 不在源支撑群内，
  则输出锚点外置而不伪造 F 或递降。这为 p=67369 的五张 G、三张 F 提供
  一个 rank-one source-SNF 解释，并证明不能按多个负因子重复收费。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-p-minus-one-jacobi-source-localization-collision-capacity
  - type-II-raw-finite-abelian-source-lift-snf
  - type-II-source-label-snf-failure-anchor-relation-dichotomy
  - type-II-kernel-fourier-source-relation-compatibility
  - type-II-source-fiber-cyclic-primary-digit-terminal
topics:
  - type-II
  - p-minus-one
  - Jacobi-character
  - source-relation
  - SNF
  - F2-rank
  - anchor-dichotomy
  - odd-primary-residual
  - capacity
  - F-G-state
  - selector
sources:
  - claim: type-II-p-minus-one-jacobi-source-localization-collision-capacity
    role: negative-source-factor-localization-and-cross-q-incidence
  - claim: type-II-raw-finite-abelian-source-lift-snf
    role: finite-source-label-SNF-realization
  - claim: type-II-source-label-snf-failure-anchor-relation-dichotomy
    role: target-in-source-versus-anchor-outside-dispatch
  - claim: type-II-kernel-fourier-source-relation-compatibility
    role: relation-lattice-and-anchor-phase-compatibility
  - reproduction: reproductions/type_ii_p_minus_one_jacobi_source_snf_rank_one.py
    role: focused-rank-one-anchor-and-control-verifier
visibility: public
last_checked: '2026-08-11'
---

# \(p-1\) 因子 Type II 的 Jacobi 源关系 SNF 秩一压缩与锚点二分

## 1. 指数源与规范评价行

设

\[
p=4U+1=4qr+1
\tag{1}
\]

为素数，并令

\[
m=4q-1,\qquad
x=U+q=q(r+1).
\tag{2}
\]

取 \(x\) 的不同素因子集合

\[
\mathcal P_q=\{\ell_1,\ldots,\ell_t\},
\qquad
e_i=v_{\ell_i}(x),
\tag{3}
\]

定义指数映射

\[
\phi_q:\mathbb Z^t\longrightarrow
H_q:=\langle\ell_1,\ldots,\ell_t\rangle
\le(\mathbb Z/m\mathbb Z)^\times,
\qquad
\phi_q(z)=\prod_{i=1}^t\ell_i^{z_i}\pmod m.
\tag{4}
\]

其乘法关系格为

\[
L_q=\ker\phi_q.
\tag{5}
\]

令 \(\chi_m(a)=(a/m)\) 为 Jacobi 角色，并定义

\[
\beta_i=
\begin{cases}
0,&\chi_m(\ell_i)=1,\\
1,&\chi_m(\ell_i)=-1,
\end{cases}
\qquad
\boldsymbol\beta_q=(\beta_1,\ldots,\beta_t)\in\mathbb F_2^t.
\tag{6}
\]

把这一行视为 \(C_2\) 的源关系评价矩阵

\[
E_q=[\,\boldsymbol\beta_q\,].
\tag{7}
\]

前一引理已经证明

\[
\chi_m(\ell_i)=-1
\iff
\ell_i\in\mathcal N_q(p)
\subseteq\{\ell:\ell\mid r+1\}.
\tag{8}
\]

因此 \(\boldsymbol\beta_q\) 不是任意标签，而是由真实整数源因子唯一确定的规范行。

## 2. 源关系 SNF 秩一引理

对任意 \(z\in L_q\)，有 \(\phi_q(z)=1\)，从而

\[
1=\chi_m(\phi_q(z))
=(-1)^{\boldsymbol\beta_q\cdot z}.
\]

故

\[
\boxed{
\boldsymbol\beta_q\cdot z=0\pmod2
\qquad(z\in L_q).}
\tag{9}
\]

这说明 \(\boldsymbol\beta_q\) annihilate 全部源关系格，并下降为一个由 Jacobi
角色规范诱导的群同态

\[
\overline\chi_q:H_q\longrightarrow C_2,
\qquad
\overline\chi_q(\phi_q(z))
=\boldsymbol\beta_q\cdot z.
\tag{10}
\]

下降良定义正是 (9) 的含义。其像和秩精确为

\[
\boxed{
\operatorname{rank}_{\mathbb F_2}
\operatorname{im}E_q
=
\begin{cases}
0,&\mathcal N_q(p)=\varnothing,\\
1,&\mathcal N_q(p)\ne\varnothing.
\end{cases}}
\tag{11}
\]

证明如下：负源为空时 \(\boldsymbol\beta_q=0\)。负源非空时至少一个坐标
\(\beta_i=1\)，故行 \(E_q\) 非零，而目标群 \(C_2\) 只有一维。于是即使
\(\mathcal N_q(p)\) 含有许多素因子，Jacobi 源关系商也只产生一个二进制方向，
不能把 \(|\mathcal N_q(p)|\) 当作独立 SNF 秩。

在已有有限阿贝尔 SNF 合同中，取源标签群 \(e=2\)、频率 \(k=1\)，
\(\lambda_i=\beta_i\)。式 (9) 正是所有源关系行的可解性条件；而
\(\chi_m|_{H_q}\) 本身给出显式角色解。因此：

\[
\boxed{
\text{Jacobi 源标签系统永不因源关系而 LIFT\_OBSTRUCTED；}
\quad
\text{其源像只可能是秩 \(0\) 或秩 \(1\).}}
\tag{12}
\]

这里的“永不失败”只针对已给出的真实因子标签 \(\beta_i\)，不声称任意外部
Fourier 标签都能通过 SNF。

## 3. 目标 \(-1\) 的锚点二分

记目标锚点

\[
a_q=-1\pmod m.
\tag{13}
\]

因为 \(m=4q-1\equiv3\pmod4\)，有

\[
\chi_m(a_q)=-1.
\tag{14}
\]

### 3.1 负源为空：规范 G 分离

若 \(\mathcal N_q(p)=\varnothing\)，则
\(\overline\chi_q\) 在 \(H_q\) 上恒为 \(+1\)，而 (14) 给出
\(\chi_m(a_q)=-1\)。因此

\[
\boxed{
\mathcal N_q(p)=\varnothing
\Longrightarrow
a_q\notin H_q.}
\tag{15}
\]

同一个 Jacobi 角色在源支撑上恒等、在目标上非恒等，故给出

\[
\operatorname{JACOBI\_G\_SOURCE\_TRIVIAL}.
\tag{16}
\]

这不是 source-rank 需求，也不是待补的 Type II 容量；它是目标锚点位于源支撑群
外部的完整分离证书。

### 3.2 负源非空且目标在源群内：源—目标 SNF 相容

若 \(\mathcal N_q(p)\ne\varnothing\) 且 \(a_q\in H_q\)，取
\(z^\ast\in\mathbb Z^t\) 使

\[
\phi_q(z^\ast)=a_q.
\tag{17}
\]

则

\[
(-1)^{\boldsymbol\beta_q\cdot z^\ast}
=\chi_m(a_q)=-1,
\]

从而

\[
\boxed{
\boldsymbol\beta_q\cdot z^\ast=1\pmod2.}
\tag{18}
\]

所以把目标标签 \(\lambda_0=1\) 加入源标签系统时，目标行与源关系格完全相容；
\(\chi_m|_{H_q}\) 是显式 SOURCE\_TARGET\_LABEL\_REALIZED 角色。若有界指数盒
没有给出这样的 \(z^\ast\)，失败来自盒的范围或其它群坐标，而不是 Jacobi 源
关系 SNF。

### 3.3 负源非空但目标在源群外：锚点外置

若 \(\mathcal N_q(p)\ne\varnothing\) 而 \(a_q\notin H_q\)，则源标签行仍然通过
(9)--(12)，但目标行无法加入。此时应输出

\[
\operatorname{JACOBI\_RANK\_ONE\_ANCHOR\_OUTSIDE},
\tag{19}
\]

并转交商 \( (\mathbb Z/m\mathbb Z)^\times/H_q\) 的锚点角色或其它终端；不能把
该状态直接称为 F，也不能把源行通过误写成 Type II 命中。

### 3.4 循环奇阶余商时的精确二分

若 \(H_q\) 本身为循环群，且 \(|H_q|=2s\)、\(s\) 为奇数，则其唯一二阶元是
\(a_q=-1\)。于是任一 \(\chi_m(\ell_i)=-1\) 的源因子生成的子群必包含
\(a_q\)。因此

\[
\boxed{
\begin{array}{c}
\mathcal N_q(p)=\varnothing
\Longleftrightarrow a_q\notin H_q,\\
\mathcal N_q(p)\ne\varnothing
\Longleftrightarrow a_q\in H_q.
\end{array}}
\tag{20}
\]

这覆盖 \(m\) 为素数的全部状态，也覆盖 \(m=27\) 这类单位群阶为
\(2\times\) 奇数的循环素数幂状态。

## 4. signed box 的二进制投影已经饱和

Type II signed box 为

\[
\mathcal Z_q=
\prod_{i=1}^t[-e_i,e_i]\cap\mathbb Z^t,
\qquad
e_i=v_{\ell_i}(x).
\tag{21}
\]

记其 Jacobi \(C_2\) 投影为

\[
\Pi_{2,q}
=\{\boldsymbol\beta_q\cdot z:z\in\mathcal Z_q\}
\subseteq\mathbb F_2.
\tag{22}
\]

若负源为空，显然

\[
\Pi_{2,q}=\{0\},
\qquad
\text{目标标签 }1\notin\Pi_{2,q}.
\tag{23}
\]

若负源非空，取任意 \(\ell_i\in\mathcal N_q(p)\)。因为
\(e_i=v_{\ell_i}(x)\ge1\)，向量 \(z=0\) 和 \(z=e_i\) 都属于 signed box，且
\[
\boldsymbol\beta_q\cdot0=0,\qquad
\boldsymbol\beta_q\cdot e_i=1.
\]

所以

\[
\boxed{
\mathcal N_q(p)\ne\varnothing
\Longrightarrow
\Pi_{2,q}=\{0,1\}.}
\tag{24}
\]

这给出一个严格的 no-go：

\[
\boxed{
\text{Jacobi 可见状态的 \(C_2\) 投影永远没有二进制容量缺口。}}
\tag{25}
\]

若同时 \(a_q\in H_q\) 而完整 signed box 仍 miss，则 miss 必定位在
\(\ker\overline\chi_q\) 内的剩余坐标（包括奇阶及可能的其它二进制方向）、源关系
几何或有限范围门；不能继续增加
Jacobi 二进制 request，也不能按负因子数重复收费。

## 5. 跨状态容量接口

对每个状态 \(q\)，定义一个 Jacobi role request

\[
\mathfrak j_q=
\begin{cases}
0,&\mathcal N_q(p)=\varnothing,\\
1,&\mathcal N_q(p)\ne\varnothing.
\end{cases}
\tag{26}
\]

候选整数因子 owner 集仍为 \(\mathcal N_q(p)\)，但

\[
\boxed{
\operatorname{rank}_{\mathbb F_2}(\mathfrak j_q)
\le1,
\qquad
\#\text{candidate factor owners}=|\mathcal N_q(p)|}
\tag{27}
\]

是两个不同账本。前者是源关系角色维数，后者是物理因子候选数。跨状态选择器若
要把某个因子 \(\ell\) 池化为共享物理槽，必须对候选图

\[
q\longleftrightarrow\ell
\quad\Longleftrightarrow\quad
\ell\in\mathcal N_q(p)
\tag{28}
\]

运行实际 owner/物理槽流；此前的入射公式给出

\[
\deg_{\mathcal D}(\ell)
\le\left\lfloor\frac{B-A}{\ell}\right\rfloor+1
\tag{29}
\]

的 occurrence 上界。式 (29) 不会把 rank-one 角色错误扩张成
\(|\mathcal N_q(p)|\) 个独立需求，也不允许反过来把一个角色方向当成已经实现了
多个 physical source columns。

## 6. 三个控制族

### 6.1 \(p=73\)

\[
\begin{array}{c|c|c|c}
q&\mathcal N_q(73)&\operatorname{rank}E_q&a_q\in H_q\\ \hline
1&\varnothing&0&\text{否}\\
2&\{5\}&1&\text{是}\\
3&\{7\}&1&\text{是}\\
6&\varnothing&0&\text{否}
\end{array}
\tag{30}
\]

对 \(q=2\)，\(m=7,x=20,d=1\) 是已有 Type II 命中；其负源因子 \(5\) 的指数
奇偶为 \(-1\)，而源—目标 Jacobi 行只有一个二进制方向。

### 6.2 \(p=337\)

取 \(U=84\)。两个允许状态 \(q=1,6\) 的负源分别为

\[
\mathcal N_1(337)=\{5,17\},
\qquad
\mathcal N_6(337)=\{5\}.
\tag{31}
\]

两张评价行的秩都为 \(1\)，不是 \(2\) 与 \(1\) 的因子数之和；同时同一因子
\(5\) 的跨状态 occurrence 达到前一引理的碰撞上界。\(q=6\) 还有 \(d=2\) 的
实际 Type II 命中。

### 6.3 \(p=67369\)

在端点下闭允许域 \(q\mid42\) 上，

\[
\begin{array}{c|c|c|c}
q&\mathcal N_q(67369)&\operatorname{rank}E_q&a_q\in H_q\\ \hline
1&\varnothing&0&\text{否}\\
2&\varnothing&0&\text{否}\\
3&\varnothing&0&\text{否}\\
6&\varnothing&0&\text{否}\\
7&\{29,83\}&1&\text{是}\\
14&\varnothing&0&\text{否}\\
21&\{73\}&1&\text{是}\\
42&\{67\}&1&\text{是}
\end{array}
\tag{32}
\]

五个 G 状态的评价行全零，三张 F 状态的评价行全为 rank one。特别是
\(q=7\) 虽有两个负素因子 \(29,83\)，其 Jacobi source-SNF 仍只有一个
\(C_2\) 方向。由于 \(m=27,83,167\) 的单位群分别为阶 \(18,82,166\) 的循环群，
(20) 保证三张 F 的目标锚点均在源支撑群内；已有 bounded-box miss 因而不是
Jacobi SNF 或 C2 投影失败。

## 7. 对统一选择器的严格含义

在端点允许域中，选择器应按以下顺序记录：

\[
\boxed{
\begin{array}{ll}
\mathcal N_q(p)=\varnothing
&\longrightarrow
\operatorname{JACOBI\_G\_SOURCE\_TRIVIAL},\\[2mm]
\mathcal N_q(p)\ne\varnothing,\ a_q\notin H_q
&\longrightarrow
\operatorname{JACOBI\_RANK\_ONE\_ANCHOR\_OUTSIDE},\\[2mm]
\mathcal N_q(p)\ne\varnothing,\ a_q\in H_q
&\longrightarrow
\operatorname{JACOBI\_RANK\_ONE\_SOURCE\_TARGET\_REALIZED}.
\end{array}}
\tag{33}
\]

第三支若完整 box 命中，进入 Type II terminal；若 box miss，必须转交
\(\ker\overline\chi_q\) 的 odd-primary/完整关系分析、其它源列、Type I terminal
或严格递降。它不能再次生成一个新的 Jacobi \(C_2\) request，也不能把
\(\mathcal N_q(p)\) 的每个元素当成独立 SNF 方向。

本引理的边界是明确的：它实现了 Jacobi 标签的 source-SNF 与锚点相容性，但没有
证明 \(\ell\) 因子候选已经成为 physical source column，也没有关闭 Jacobi 核剩余
方向的 F box miss。后续必须在 \(\ker\overline\chi_q\) 的剩余方向中构造源关系评价矩阵、
执行 owner/物理槽流，或给出 Type I/II 的严格可提升出口。

聚焦验证：

~~~bash
python3 reproductions/type_ii_p_minus_one_jacobi_source_snf_rank_one.py --verify
~~~

验证器只检查评价行秩、源关系奇偶、目标支撑成员关系和 \(p=73,337,67369\) 控制；
不重复运行历史范围或已有 F/G 有界盒测试。
