---
kind: claim
claim_id: type-II-cross-state-full-match-realization-fourier-trichotomy
title: Type II 跨状态完整匹配的算术实现—Fourier 三分
statement: 对一个已合并重复 q 层且能嵌入共同有限阿贝尔单位群的跨状态完整匹配，设其源块束为 P_f、目标为 -1。若目标属于 P_f，则任选目标见证进入同模数、严格降模、raw 算术闭合三分：得到 Type II、保持标签的较小模数后继或 ALL_ARITHMETIC_LIFT_EMPTY 后的 RAW_DIVISOR_FOURIER。若目标不属于 P_f，则有限群 Parseval 给出非平凡角色；通过指数阶与有限阿贝尔 SNF 时输出 CROSS_STATE_SOURCE_RELATION_FOURIER，否则输出明确的 CROSS_STATE_ARITHMETIC_FOURIER_OBSTRUCTED。共同环境群或 shared-q 合并失败时输出 AMBIENT_SOURCE_OBSTRUCTED。该三分把 UNREALIZED_CROSS_STATE_MATCH 变成有类型的后继，但不把跨状态匹配本身误称为 Type II。
claim_status: conditional
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-hall-matching-fiber-realization-gate
  - type-II-hall-bundle-target-residue-fourier-gate
  - type-II-hall-fiber-arithmetic-closure-trichotomy
  - type-II-arithmetic-empty-raw-fourier-bridge
  - type-II-raw-finite-abelian-source-lift-snf
  - type-II-cross-state-same-modulus-pooling-counterexample
topics:
- type-II
- cross-state
- FULL_MATCH
- fiber-realization
- source-switch
- Fourier
- SNF
- arithmetic-obstruction
- proof-program
sources:
  - claim: type-II-hall-matching-fiber-realization-gate
    role: single-fiber-upgrade-boundary
  - claim: type-II-hall-bundle-target-residue-fourier-gate
    role: target-residue-Fourier
  - claim: type-II-hall-fiber-arithmetic-closure-trichotomy
    role: arithmetic-candidate-closure
  - claim: type-II-arithmetic-empty-raw-fourier-bridge
    role: raw-empty-Fourier-refinement
  - claim: type-II-raw-finite-abelian-source-lift-snf
    role: finite-abelian-frequency-lift
visibility: public
last_checked: '2026-08-05'
---

# Type II 跨状态完整匹配的算术实现—Fourier 三分

## 1. 共同环境和规范源块束

固定一个有限的共同环境单位群
\[
G_*=U(4D_*),
\tag{1}
\]
并设一个跨参数 Hall 完整匹配选择了带来源标签的 q 层
\[
(a_i,q_i,e_i),\qquad
q_i^{e_i}\mid p+4D_*a_i,\qquad q_i\nmid4D_*,
\tag{2}
\]
其中 \(q_i\) 是 shared-\(q\) 合并后两两不同的奇素数，\(e_i\) 是共同账本确认的
可用高度。
若无法把原始块分解为这类带来源 q 层，则输出
\(\mathrm{AMBIENT\_SOURCE\_OBSTRUCTED}\)。
先按 shared-\(q\) 账本合并同一素数的重复层；若同一 \(q\) 的总指数、来源标签或
环境嵌入尚未确定，则输出
\(\mathrm{AMBIENT\_SOURCE\_OBSTRUCTED}\)，不得构造乘积集。合并后设
\[
\mathcal P_f
=\prod_{i=1}^r\{1,q_i,q_i^2,\ldots,q_i^{e_i}\}
\subseteq G_*,
\tag{3}
\]
其中 \(q_i\) 两两互素，集合乘积按去重后的
群元素理解。
目标记为 \(t=-1\in G_*\)。

式 (3) 只表达跨状态匹配的有限源块束；它还没有给出单一整数参数 \(A\)，所以
\(\mathcal P_f\) 的命中不能直接称为 Type II。

## 2. 命中分支：算术实现三分

若
\[
t\in\mathcal P_f,
\tag{4}
\]
选取一个指数向量 \(z\) 并令
\[
h=\prod_i q_i^{z_i}.
\tag{5}
\]
去掉零指数后，选中的块 \(h_i=q_i^{z_i}\) 仍带有原来源标签，满足
\(h_i\mid p+4D_*a_i\)，且
\[
h\equiv-1\pmod{4D_*}.
\tag{6}
\]
由于选中块 \(h_i\) 两两互素，先由
\[
a_0\equiv a_i\pmod{h_i}
\]
取 CRT 类；于是 \(h\mid p+4D_*a_0\)。在三类候选全空时，raw Fourier 桥的目标残数
应取 \(t_0\equiv D_*a_0\pmod h\)，而不是共同单位群中的 \(t=-1\)。
对该 \(h\) 依次检查有限候选：

1. 同模数 admissible 参数 \(a\mid D_*\)；
2. 严格除子格参数 \(D'|D_*\)、\(D'<D_*\)、\(A|D'\)；
3. raw 正规形三元组 \((A,C,K)\)。

若第一类非空，得到 FIBER_REALIZED\((A)\) 和 Type II 短证书；若第一类为空而
第二类非空，得到保持来源标签的严格较小模数后继；若前两类为空而第三类非空，
得到 raw Type II 短证书；三类全空时输出
\[
\mathrm{ALL\_ARITHMETIC\_LIFT\_EMPTY}
\tag{7}
\]
并调用已有的 type-II-arithmetic-empty-raw-fourier-bridge，在 raw 除子残数集上
构造 RAW_DIVISOR_FOURIER，而不是把共同源块集 \(\mathcal P_f\) 的 Fourier
系数误作 raw 证书。该三分的候选完备性由 Hall 混合因子的同模数—降模—raw 算术
闭合引理保证。

## 3. 未命中分支：共同群 Fourier

若
\[
t\notin\mathcal P_f,
\tag{8}
\]
在 \(G_*\) 上令
\[
F=1_{\mathcal P_f}-\delta_t.
\tag{9}
\]
支持不相交，故未归一化 Fourier 满足
\[
\widehat F(1)=|\mathcal P_f|-1,
\qquad
\sum_{\chi\in\widehat{G_*}}|\widehat F(\chi)|^2
=|G_*|(|\mathcal P_f|+1).
\tag{10}
\]
于是
\[
\boxed{
\sum_{\chi\ne1}|\widehat F(\chi)|^2
=|G_*|(|\mathcal P_f|+1)-(|\mathcal P_f|-1)^2>0.
}
\tag{11}
\]
将非平凡角色按“幅度递减、群坐标的固定字典序递增”排列；首个角色给出规范的
\(\mathrm{CROSS\_STATE\_RESIDUE\_FOURIER}\) 候选，但不能因此停止枚举。对这列
角色逐一先通过阶筛
\[
\operatorname{ord}(\chi_*)\mid \operatorname{exp}(H_{\mathrm{src}}),
\tag{12}
\]
再用有限阿贝尔源关系与目标锚点的 SNF 仿射系统检查：

* 只要某个角色通过 (12) 和 SNF：输出
  \(\mathrm{CROSS\_STATE\_SOURCE\_RELATION\_FOURIER}\)，并把首个通过的角色交给
  F/G、rank-Hall 或其它已闭合容量接口；
* 若允许角色子集非空但全部角色的阶筛或 SNF 均失败：输出
  \(\mathrm{CROSS\_STATE\_ARITHMETIC\_FOURIER\_OBSTRUCTED}\)，保存全部失败关系行，
  不把外部加法角色计入 Kneser 容量；
* 若经过阶筛和 SNF 门后、允许的源相容角色子集的总能量为零，则当前源商对该
  匹配空洞不可见，转环境商、另一参数纤维或良基递降；这不否定共同群上未筛选
  的非平凡总能量 (11)。

## 4. 穷尽性和与 FIBER_REALIZED 的关系

在共同环境和 shared-\(q\) 已通过时，(4) 或 (8) 必居其一。命中分支中，有限
算术闭合三分穷尽所有同模数、除子格和 raw 正规形候选；未命中分支中，(11) 保证
存在非平凡共同群角色，阶筛/SNF 对每个规范角色给出成功或失败回执。因此
\[
\boxed{
\begin{array}{c}
\text{Type II / 严格降模 / raw Type II},\\
\text{ALL\_ARITHMETIC\_LIFT\_EMPTY}\to\text{RAW\_DIVISOR\_FOURIER},\\
\text{或可提升 SOURCE\_RELATION\_FOURIER / 明确算术障碍}
\end{array}}
\tag{13}
\]
是该有限匹配的完整 typed 分派。

若匹配本来就是 FIBER_REALIZED\((A)\)，则 (4) 的同模数候选已经由实现门确认，
命中可直接升级为 Type II；若只有跨状态匹配而无实现映射，(13) 仍然成立，但
不能跳过算术门。特别是 \(11\cdot13\equiv-1\pmod{24}\) 的 \(p=97\) 伪命中落在
命中但三类参数候选全空的分支，不是 Type II 证书。

## 5. 证明

共同环境或 shared-\(q\) 失败时，(3) 没有定义，故第一分支是必要的障碍回执。
否则指数向量的有限枚举给出 (4)/(8) 二分。若 (4) 成立，(5)--(6) 把命中指数
变成带来源的有限混合因子；算术闭合三分的每一类都由其正规形整除、范围和来源
合同直接验证，三类全空则由 raw 空集桥在其除子残数集上构造
RAW_DIVISOR_FOURIER，再按源关系门分派。

若 (8) 成立，(9) 的支持不相交，Parseval 给出 (10)--(11)；有限阿贝尔群的角色
阶筛是必要条件，SNF 是角色和锚点相容的充要整数判据。故每个规范角色只能成功
提升或留下明确失败行，不能出现未分类的“混合积容量”。证毕。

## 6. 边界例子

### \(p=97\) 的伪命中

取 \(D_*=6\)、\(G_*=U(24)\)，源块 \(11\) 和 \(13\) 分别来自
\(p+24=121\) 与 \(p+72=169\)。它们的匹配乘积 \(143\equiv-1\pmod{24}\)，
但同模数和除子格参数门均无候选，raw 三元组也为空；因此输出
\(\mathrm{ALL\_ARITHMETIC\_LIFT\_EMPTY}\) 后转 RAW_DIVISOR_FOURIER。

### 未命中角色

在 \(G=C_8\) 中取
\(\mathcal P_f=\{0,4\}\)（加法记号）和目标 \(1\)。目标未命中，奇角色
\(\chi(x)=(-1)^x\) 给出非零差分 Fourier；若源关系商允许该角色，则输出
\(\mathrm{CROSS\_STATE\_SOURCE\_RELATION\_FOURIER}\)，否则保存 SNF 障碍。

## 研究边界

该三分把跨状态 FULL_MATCH 从“容量已分配”推进为有限的整数实现或共同群对偶
分派，消除了把混合乘积直接写成 Type II 的逻辑跳步。它仍不证明未命中 Fourier
角色必有 F/G 载体，也不保证 ALL_ARITHMETIC_LIFT_EMPTY 必然产生严格核心素数
下降；这些仍是全局 HC 的后续条件。
