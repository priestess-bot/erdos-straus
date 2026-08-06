---
kind: claim
claim_id: type-II-annihilator-two-sided-subgroup-quotient-descent
title: Type II 全源列闭合的 annihilator 子群—商双向严格递降
statement: 设规范化有限阿贝尔目标状态为 (H,R,t)，其中 1 属于 R 且 t 不属于 R。若固定纤维的阶 ell 非平凡角色 chi 湮灭全部真实源列，从而 R 落在 K=ker(chi) 中，则按 t 是否属于 K 完成双向严格二分：t 不属于 K 时投影到 H/K 得到目标缺失的严格商 relay，t 属于 K 时直接把目标缺失限制到真子群 K 得到严格子群 relay；当 Type II 目标 t=-1 时，商中非平凡的分支必有 ell=2，奇素数阶角色只能进入子群分支；当 K=1 时只剩顶层 ell-primary 终端。两个 relay 均附有可计算的 SNF、source-switch、标签和 B'>A 提升门，门失败时输出精确的 lift-obstructed 证书。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-hall-deficit-linear-dual-bridge
  - type-II-linear-rank-deficit-dual-separation-certificate
  - type-II-source-fiber-finite-abelian-composition-relay
  - type-II-stabilizer-kernel-quotient-descent-trichotomy
topics:
- type-II
- annihilator
- subgroup-descent
- quotient-descent
- Fourier
- Hall
- source-column
- source-switch
- SNF
- well-founded-potential
- proof-program
sources:
  - claim: type-II-hall-deficit-linear-dual-bridge
    role: full-source-closure-dual-character
  - claim: type-II-linear-rank-deficit-dual-separation-certificate
    role: explicit-order-ell-character
  - claim: type-II-source-fiber-finite-abelian-composition-relay
    role: finite-abelian-target-state
  - claim: type-II-stabilizer-kernel-quotient-descent-trichotomy
    role: integer-lift-and-lower-modulus-gate
visibility: public
last_checked: '2026-08-05'
---

# Type II 全源列闭合的 annihilator 子群—商双向严格递降

## 1. 规范化的全源列闭合

固定一个已经通过来源标签、SNF、source-switch 和范围门的有限纤维。把一个源
基点除去后，写成

\[
1\in R\subset H,\qquad t\in H\setminus R,
\tag{1}
\]

其中 \(H\) 是有限阿贝尔目标商，\(R\) 是真实源块的和集，\(t\) 是规范目标。
令 \(\mathcal G=\{g_1,\ldots,g_s\}\) 是所有实际源列和规范基点产生元；源块账本
要求

\[
R\subseteq\langle\mathcal G\rangle .
\tag{2}
\]

设 \(\chi:H\to\mu_\ell\) 是一个非平凡、阶为素数 \(\ell\) 的真实角色，并令

\[
K=\ker\chi,\qquad Q=H/K.
\tag{3}
\]

全源列闭合不是“当前 Hall 邻域上的角色为零”，而是下面的有限成员条件：

\[
\mathrm{SCClosed}(\chi)
\iff
\chi(g_i)=1\quad(1\le i\le s)
\quad\text{且所有源块成员均通过 (2) 回译。}
\tag{4}
\]

由 (2)--(4) 有

\[
\boxed{R\subseteq K,\qquad |Q|=\ell,\qquad |K|=|H|/\ell<|H|.}
\tag{5}
\]

若 \(\chi\) 来自 q 进 Rado 缺口，则 (4) 可由逐列检查、有限逃逸扩张后的
SOURCE_COLUMN_CLOSED 或 SOURCE-DOMINATING-CUT 得到；未闭合时不能使用本引理。

## 2. 两侧严格二分

在 (4) 成立时，目标只有两种位置。

### A. 目标在核外：商递降

若

\[
t\notin K,
\tag{6}
\]

则 \(\bar t=tK\ne K\)，而由 \(R\subseteq K\)

\[
\pi(R)=\{K\},\qquad \pi(t)=\bar t\ne K,
\qquad \pi:H\to Q=H/K.
\tag{7}
\]

所以

\[
\boxed{\bar t\notin\pi(R)}
\tag{8}
\]

是一个阶为 \(\ell\) 的目标缺失。若 \(|H|>\ell\)，则
\(|Q|=\ell<|H|\)，输出

\[
\mathrm{ANNIHILATOR\_QUOTIENT\_LOWER\_RELAY}
=(H,R,t,\chi,\pi,Q,\bar t).
\tag{9}
\]

若 \(|H|=\ell\)，则 \(K=1\)，没有更小的非平凡商；(9) 改记为

\[
\mathrm{TOP\_PRIMARY\_ANNIHILATOR}(\ell,\chi,t).
\tag{10}
\]

### B. 目标在核内：子群递降

若

\[
t\in K,
\tag{11}
\]

则 \(R\subseteq K\) 且 \(t\notin R\)，从而同一个目标缺失在真子群中保留：

\[
\boxed{t\notin R\quad\text{且}\quad R,t\subseteq K,\qquad |K|<|H|.}
\tag{12}
\]

输出

\[
\mathrm{ANNIHILATOR\_SUBGROUP\_LOWER\_RELAY}
=(K,R,t,\chi,\iota_K),
\tag{13}
\]

其中 \(\iota_K:K\hookrightarrow H\) 是保持源标签的嵌入。注意 \(K=1\) 与
(11) 不相容：此时 \(t=1\in R\)，会违背 \(t\notin R\)。所以目标在核内的分支
自动是严格的非平凡子群递降，而不是顶层终端。

式 (12) 是对原先“目标相位平凡、只能保留关系 Fourier”回执的加强：在全源列
闭合时，关系角色同时给出一个更小的目标状态；只有整数参数提升门失败时，才
退回为带障碍的关系 Fourier。

### C. Type II 目标的阶二塌缩

现在专门恢复 Type II 的规范目标
\[
t=-1\in H.
\tag{13a}
\]
因为 \((-1)^2=1\)，对任意群同态 \(\pi:H\to H/K\) 都有
\[
\operatorname{ord}(\pi(t))\mid2.
\tag{14b}
\]
若 \(Q=H/K\) 的阶为素数 \(\ell\)，则
\[
t\notin K
\quad\Longrightarrow\quad
\operatorname{ord}(\pi(t))=\ell
\quad\Longrightarrow\quad
\ell=2.
\tag{15b}
\]
换言之，奇素数阶 annihilator 角色不能产生一个把 Type II 目标
\(-1\) 分离到非平凡商中的 quotient relay。对奇素数 \(\ell\)，必有
\(\pi(t)=1_Q\)；而 \(1\in R\) 且 \(R\subseteq K\)，所以 \(t\notin K\) 分支
在规范化目标状态中不可能发生，只能进入 \(t\in K\) 的严格子群递降。

这也与[单位群—目标带像满射 SNF 判据](type-II-annihilator-unit-group-target-map-snf-criterion.md)
的 G1 条件一致：若候选映射满足
\(\eta:U(4D')\twoheadrightarrow J\) 和 \(\eta(-1)=t_J\)，则
\[
\operatorname{ord}(t_J)\mid2.
\tag{16b}
\]
当 \(J\simeq C_\ell\) 且 \(t_J\ne1\) 时，(16) 立即排除所有奇素数
\(\ell\)。因此 quotient 端的直接目标 relay 只需在二阶目标或其迭代
\(2^j\) primary 塔中搜索；奇 primary 角色仍可用于源关系 Fourier、源列秩或
子群 relay，但不能被误记为非平凡 \(-1\) 商命中。

## 3. 子群/商的格级精确回译

令源群取为真实源列像

\[
H=\operatorname{im}\varphi,\qquad
\Lambda=\ker\varphi,\qquad
\varphi:L\longrightarrow H,
\tag{14a}
\]

并令 \(\mathcal B\subset L\) 是源指数盒。由 \(R=\varphi(\mathcal B)\subseteq K\)，
有 \(\mathcal B\subseteq\widetilde K\)，其中

\[
\widetilde K=\varphi^{-1}(K).
\tag{15a}
\]

因为 \(K\le H=\operatorname{im}\varphi\)，第一同构定理给出

\[
\boxed{\widetilde K/\Lambda\simeq K.}
\tag{16a}
\]

若 \(t\in K\)，任取目标代表 \(t_L\in L\)；它自动属于 \(\widetilde K\)，且
\(t_L\notin\mathcal B+\Lambda\)，否则 \(t\in R\)。因此
\[
(\widetilde K/\Lambda,\mathcal B+\Lambda,t_L+\Lambda)
\]
是子群分支的完整格级目标状态，而不是只在抽象有限群中存在的占位符。

若 \(t\notin K\)，把 \(\varphi\) 与商映射复合，得到

\[
\overline\varphi:L\longrightarrow H/K,\qquad
\ker\overline\varphi=\widetilde K,\qquad
L/\widetilde K\simeq H/K.
\tag{17a}
\]

源盒的像是单位元，而 \(t_L\) 的像非单位元；这是商 relay 的完整格级状态。
式 (16a)--(17a) 说明群论二分不会丢失来源指数或目标缺失，剩余问题只在于新
格状态能否满足 Type II 的整数正规形。

## 4. 整数 source-switch 与提升门

群论二分 (9)/(13) 不自动等于原素数参数的整数递降。为使回执成为可提升后继，
保存源指数映射

\[
\varphi:L\longrightarrow H,\qquad
\Lambda=\ker\varphi,
\tag{14}
\]

以及真实源盒 \(\mathcal B\subset L\)。对子群分支定义

\[
L_K=\varphi^{-1}(K),
\qquad
\Lambda_K=\Lambda\cap L_K.
\tag{15}
\]

用 SNF 计算 \(L_K/\Lambda_K\) 的一组基，并检查：

1. 每个源块的指数在 \(L_K\) 中仍有来源标签和范围代表；
2. 目标指数 \(t_L\) 落在 \(L_K\)，且 \(t_L\notin\mathcal B+\Lambda_K\)；
3. 规范正规形的整数参数满足 source-switch 合同、\(B'>A\) 和 E1--E5；
4. 新状态的 modulus/目标纤维确实对应 \(K\)，没有只在抽象群中存在的伪提升。

四项通过时，把 (13) 升级为

\[
\mathrm{SUBGROUP\_SOURCE\_SWITCH\_DESCENT}
=(p,L_K,\mathcal B,t_L,\mathrm{SNF},B'>A).
\tag{16}
\]

四项任一失败时，输出完整失败行

\[
\mathrm{ANNIHILATOR\_SUBGROUP\_LIFT\_OBSTRUCTED}
=(\chi,K,L_K,\text{failed\_gate},\text{SNF/CRT\ witness}),
\tag{17}
\]

并保留 (13) 作为抽象有限群下降证书；不能把 (17) 误写成已经完成的核心素数
递降。商分支同样保存 \(Q\) 的源标签回译和 \(B'>A\) 检查，失败时记
\(\mathrm{ANNIHILATOR\_QUOTIENT\_LIFT\_OBSTRUCTED}\)。

四项门的有限充要菜单和直接 Type II 子列表终端见
[Type II annihilator relay 的带来源同余纤维提升判据](type-II-annihilator-congruence-fiber-lift-criterion.md)；
该判据把 G1--G4 的失败逐项记录，避免把抽象 relay 或 Fourier 角色重复计入容量。

## 5. 证明

由全源列闭合，\(\chi\) 在每个 \(g_i\) 上取单位相位。按 (2) 的生成性，所有
源块成员及其乘积都在 \(K\)，故 \(R\subseteq K\)。

若 \(t\notin K\)，则其陪集 \(tK\) 在 \(H/K\) 中不是单位陪集，而 \(\pi(R)\)
只有单位元，得到 (7)--(8)。因为 \(\chi\) 非平凡且阶为 \(\ell\)，
\(|H/K|=\ell\)；当 \(|H|>\ell\) 时商阶严格变小，当 \(|H|=\ell\) 时
\(K=1\) 且只能进入 (10)。

若 \(t\in K\)，则 \(R,t\) 都是 \(K\) 的元素，且原缺失关系
\(t\notin R\) 不会因限制到 \(K\) 而改变，得到 (12)。非平凡 \(\chi\) 使
\(|K|<|H|\)，而 \(K=1\) 会迫使 \(t=1\in R\)，故该分支不可能退化。

最后，(14a)--(17) 只是把两个有限群状态的包含关系写回整数源格：第一同构定理给出
\(\widetilde K/\Lambda\) 的精确格状态，四项门逐一保证源块、目标、参数合同和严格
大小均可回译。
因此它们决定的是“可提升递降”还是“带精确障碍的抽象递降”，证毕。

## 6. 构造性边界例子

### 子群递降

取 \(H=C_2\oplus C_2\)，
\[
R=\{(0,0)\},\qquad t=(0,1),\qquad
\chi(x,y)=(-1)^x.
\]
则 \(K=\{(0,0),(0,1)\}\)，源与目标都在 \(K\) 中，且
\(t\notin R\)。因此目标直接递降到真子群 \(K\simeq C_2\)；这是目标相位
\(\chi(t)=1\) 时不能再被称为“只有关系 Fourier”的最小反例。

### 商递降

在同一 \(H\) 和 \(\chi\) 下取 \(t=(1,0)\)。此时 \(t\notin K\)，
\(H/K\simeq C_2\) 中目标非单位而源投影为单位，得到商 relay。

### 顶层终端

取 \(H=C_\ell\)、\(R=\{0\}\)、\(t=1\)，令 \(\chi\) 为忠实阶 \(\ell\) 角色。
则 \(K=1\)，目标在核外但没有严格非平凡商，只能输出
\(\mathrm{TOP\_PRIMARY\_ANNIHILATOR}\)。

## 7. 与统一选择器的接线和边界

对 SIMULTANEOUS_ROLE 失败产生的 Rado 对偶角色，先执行有限源列逃逸扩张；只有
得到 SCClosed 后才调用本引理。于是固定纤维的角色缺口现在有如下顺序：

\[
\text{source-column escape}
\ \longrightarrow\
\text{SCClosed}
\ \longrightarrow\
\begin{cases}
\text{annihilator quotient relay},&t\notin K,\\
\text{annihilator subgroup relay},&t\in K,\\
\text{top primary},&K=1.
\end{cases}
\tag{18}
\]

当需要同时处理多个奇素数阶 annihilator 时，可直接先调用
[奇主部分 annihilator 压缩与 2-primary 终端接口](type-II-odd-primary-annihilator-compression-two-primary-terminal.md)：
它把所有奇主方向一次性压到 \(O=\pi^{-1}((H/\langle R\rangle)_{(2)})\)，并把剩余
对偶障碍精确交给 2-primary/广义 \(2^j\) 菜单，避免在同一个奇主商中重复收费。

该链在有限群层面消除了“目标相位平凡但没有下一步”的空分支；仍未消除两个
全局条件：跨纤维角色必须先通过 FIBER_REALIZED，且 (16) 的整数 source-switch
提升门尚未对所有核心素数证明。若 (17) 发生，下一步应研究其 SNF 障碍是否
强制 Type I/F/G 证书或另一条保持标签的严格下降，而不是继续增加 Fourier 支撑
计数。
