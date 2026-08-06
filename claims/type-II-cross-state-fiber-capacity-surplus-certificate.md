---
kind: claim
claim_id: type-II-cross-state-fiber-capacity-surplus-certificate
title: Type II 跨参数纤维 q-height 容量 surplus 证书
statement: 固定 D_* 与有限 admissible 参数纤维 A。对每个 A 取已合并重复 q 来源的幂块 P_A、最终稳定子 T_A 和精确活跃容量 kappa_{i,A}=min(d_i(A),ord(u_iT_A)-1)。若所有纤维都遗漏目标 -1，则逐纤维有 sum_i kappa_{i,A}<=|G_*/T_A|-2；因此任意正权重 w_A 都满足加权总需求不超过加权总缺口预算。反之若一个可验证的 q-height 下界使加权总需求超过该预算，则至少一个参数纤维命中 -1，从而给出 Type II 短证书。该聚合不假设不同纤维源块独立，容量只在各自纤维内计费。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-lattice-fibered-kneser-selector
  - type-II-source-fiber-qheight-kneser-bridge
  - type-II-multiblock-kneser-active-capacity-dichotomy
  - type-II-source-fiber-cyclic-digit-deficit-quotient-kernel-relay
  - type-II-q-layer-prefix-kneser-price-certificate
  - type-II-q-prefix-source-crt-fiber-concentration
  - type-II-cross-state-tower-weighted-surplus-selector
topics:
- type-II
- cross-state
- parameter-fiber
- q-height
- capacity
- surplus
- kneser
- source-switch
- constructive-certificate
- proof-program
sources:
  - claim: type-II-source-lattice-fibered-kneser-selector
    role: parameter-fiber-target-and-stabilizer
  - claim: type-II-source-fiber-qheight-kneser-bridge
    role: exact-q-height-blocks
  - claim: type-II-multiblock-kneser-active-capacity-dichotomy
    role: per-fiber-kneser-deficit
  - claim: type-II-source-fiber-cyclic-digit-deficit-quotient-kernel-relay
    role: deficit-to-quotient-or-kernel-routing
  - claim: type-II-q-layer-prefix-kneser-price-certificate
    role: prefix-matching-to-certified-q-price
  - claim: type-II-q-prefix-source-crt-fiber-concentration
    role: source-label-to-fiber-concentration
visibility: public
last_checked: '2026-08-05'
---

# Type II 跨参数纤维 q-height 容量 surplus 证书

## 纤维数据

固定原始 \(D\)、核心素数 \(p\) 和一个候选 \(D_*\mid D\)。令

\[
\mathcal A=\mathcal A_{D_*}(p)
\]

为满足 \(A\mid D_*\)、\(D_*/A\) 平方自由和 \(4AD_*<p\) 的参数纤维。对每个
\(A\in\mathcal A\)，把重复 q 来源先按共同 q 进账本合并，得到幂块

\[
B_{i,A}=\{1,u_i,u_i^2,\ldots,u_i^{d_i(A)}\}
\subseteq G_*=(\mathbb Z/4D_*\mathbb Z)^\times,
\tag{1}
\]

\[
P_A=\prod_i B_{i,A},\qquad
T_A=\operatorname{Stab}_{G_*}(P_A).
\tag{2}
\]

令

\[
\kappa_{i,A}
=\left|B_{i,A}T_A/T_A\right|-1
=\min\{d_i(A),\operatorname{ord}_{G_*/T_A}(u_iT_A)-1\}.
\tag{3}
\]

只有满足 source-switch 合同的来源块才进入 (1)；改变参数纤维的块、被共同 q
账本合并的重复来源和被 \(T_A\) 吸收的列不能重复计费。

## 聚合 surplus 定理

若同一纤维的 q 请求需要经过多级稳定子塔，逐级加权价格的更强版本见
[Type II 跨参数纤维稳定子塔的加权 surplus 选择器](type-II-cross-state-tower-weighted-surplus-selector.md)。
本节的最终稳定子公式是该版本在单层/最终块情形下的投影；两者不能对同一 q 方向
叠加计费。

对每个纤维取任意正权重 \(w_A>0\)，定义加权需求和缺口预算

\[
\mathcal Q_w
=\sum_{A\in\mathcal A}w_A\sum_i\kappa_{i,A},
\qquad
\mathcal B_w
=\sum_{A\in\mathcal A}w_A\bigl(|G_*/T_A|-2\bigr),
\tag{4}
\]

以及 surplus

\[
\operatorname{Surplus}_w=\mathcal Q_w-\mathcal B_w.
\tag{5}
\]

若所有参数纤维都遗漏 \(-1\)，则

\[
\boxed{\operatorname{Surplus}_w\le0.}
\tag{6}
\]

反之，若通过 q-height 账本得到

\[
\boxed{\operatorname{Surplus}_w>0,}
\tag{7}
\]

则至少存在一个 \(A\in\mathcal A\) 满足
\(-1\in P_A\)，因而给出 Type II 短证书。

### 证明

固定 \(A\)。若 \(-1\notin P_A\)，源纤维 Kneser 缺口给出

\[
\sum_i\kappa_{i,A}\le |G_*/T_A|-2.
\tag{8}
\]

乘以 \(w_A>0\) 后对所有 \(A\) 求和得到 (6)。若 (7) 成立，则 (8) 不可能对所有
\(A\) 同时成立；对违反 (8) 的纤维，整数性给出
\(\sum_i\kappa_{i,A}\ge|G_*/T_A|-1\)，Kneser 选择器遂强制
\(P_A=G_*\)，特别命中 \(-1\)。证毕。

## 为什么跨纤维重复不破坏定理

同一个来源块可以同时属于多个 \(I_{D_*}(A)\)。式 (4) 仍然安全，因为它不是把
这些来源块合并成一个全局乘积，而是在每个独立候选纤维上分别应用 (8) 后再求和。
因此本定理允许跨纤维复用，但禁止在同一纤维内把重复 q 或稳定子吸收列重复收费。
这正是 pair-energy 不能直接当独立容量、而 q-height/Kneser 账本可以聚合的区别。

可以用任何可证明的下界 \(\underline\kappa_{i,A}\le\kappa_{i,A}\) 代替精确
\(\kappa_{i,A}\)。若

\[
\sum_Aw_A\sum_i\underline\kappa_{i,A}
>
\sum_Aw_A(|G_*/T_A|-2),
\tag{9}
\]

则同样得到 Type II 命中；(9) 是适合跨状态 q 进容量证明的可计算入口。

## 前缀/CRT 下界注入

式 (9) 的关键不是把 Hall 请求数直接当作价格，而是先把请求变成同一参数纤维中
真实存在的 q 幂块。若一个请求有多个候选来源标签，先调用
[Type II q 前缀来源标签与候选纤维的有限穷尽闭包](type-II-q-prefix-source-label-finite-closure.md)；
只有其有限分支给出固定标签和按纤维不交的分割时，才进入下面的价格计算。标签表
未有限化时保留 LABEL_SOURCE_ENUMERATION_UNCLOSED，不得把它写入 (9)。设
\(\mathcal R\) 是带固定来源标签的 q 层请求族，并选择一个
按纤维不交的分派

\[
\mathcal R=\bigsqcup_{A\in\mathcal A}\mathcal R_A,
\qquad
\mathcal R_{A,q}=\{r\in\mathcal R_A:q_r=q\}.
\tag{10}
\]

对该分派定义 \(s_A=AD_*\)，并令

\[
Q_A=\operatorname{lcm}_{r\in\mathcal R_A}q_r^{h_r}.
\tag{11}
\]

对每个非空 \(\mathcal R_A\)，先运行[Type II q 层请求的来源 CRT 纤维集中与唯一候选](type-II-q-prefix-source-crt-fiber-concentration.md)。若
\(Q_A>D^2\)，CRT/范围门至多留下一个候选纤维；CRT 本身不相容时输出
\(\mathrm{Q\_PREFIX\_SOURCE\_CRT\_INCONSISTENT}\)，唯一候选不是当前 \(A\) 或
来源、SNF、范围门失败时输出
\(\mathrm{Q\_PREFIX\_SOURCE\_FIBER\_EMPTY}\) 或相应的
\(\mathrm{EDGE\_OBSTRUCTED}\)，均不产生下界。若 \(Q_A\le D^2\)，
则必须从有限候选表中为请求选择一个实际纤维；同一请求不能同时计入两个候选，
否则不得形成 (10) 的分派。

固定一个已通过这些门的 \((A,q)\)。令 \(h_{(1)}\le\cdots\le h_{(n_{A,q})}\) 为
该 q 请求的高度。如果

\[
h_{(k)}\ge k\qquad(1\le k\le n_{A,q}),
\tag{12}
\]

则[Type II q 层前缀匹配到纤维 Kneser 价格的规范压缩](type-II-q-layer-prefix-kneser-price-certificate.md)构造一个真实的连续 q 幂块。把它与该纤维此前已经通过回译的同 q 块取共同账本后，记总共得到的、尚未超过精确源高度的深度为
\(\widehat d_{A,q}\)，其中

\[
n_{A,q}\le \widehat d_{A,q}\le d_q(s_A).
\tag{13}
\]

若同一 q 方向已经存在，(13) 是合并后的总深度，不是把两个请求数相加；最终
稳定子 \(T_A\) 固定后才计算价格

\[
\underline\kappa_{A,q}
 =\min\left\{\widehat d_{A,q},
 \operatorname{ord}_{G_*/T_A}(u_qT_A)-1\right\}.
\tag{14}
\]

因该幂块是精确块 \(B_{q,A}\) 的子块，且每个 q 商方向只出现一次（若
\(u_qT_A\) 相同则先合并），\(\underline\kappa_{A,q}\le\kappa_{q,A}\)，其中
\(\kappa_{q,A}\) 表示 (3) 中对应 q 方向的精确价格；它可以作为 (9) 的逐纤维可验证
下界。
如果 \(\widehat d_{A,q}+1\) 达到最终商阶，则最终稳定子折叠塌缩给出
\(\operatorname{ord}_{G_*/T_A}(u_qT_A)=1\)，式 (14) 只记录最终吸收价格
\(0\)，不能继续增加 \(\mathcal Q_w\)。若相同 q 族是在插入时稳定子上达到商阶，
才记录 \(\mathrm{Q\_PREFIX\_ORDER\_FOLD}\)，转交稳定子塔、primary 或 Fourier。
若 (12) 失败，则输出
\(\mathrm{Q\_PREFIX\_MATCHING\_DEFICIT}\)，该 q 族的下界为零。

在所有纤维都完成上述门、且 (10) 保持来源标签和候选纤维不交后，定义

\[
\underline{\mathcal Q}_w
 =\sum_{A\in\mathcal A}w_A\sum_q\underline\kappa_{A,q}.
\tag{15}
\]

于是只要

\[
\boxed{
\underline{\mathcal Q}_w
 >\sum_{A\in\mathcal A}w_A\bigl(|G_*/T_A|-2\bigr),
}
\tag{16}
\]

就得到显式的 Type II 短证书。证明是：每个 (14) 都来自同一纤维的真实幂块，
故不超过精确价格；把它们代入 (9) 即得 (16) 的命中结论。该构造只在纤维内
计价；当 CRT 候选仍有多个且没有不交分派时，回执必须是
\(\mathrm{Q\_PREFIX\_PRICE\_FRAGMENTED}\)，而不是把同一来源请求复制到多个
\(A\) 后求和。

## 与数字缺口和算术提升门的分派

若 (7) 不成立而某个纤维缺失，则该纤维保留精确缺口

\[
\delta_A=|G_*/T_A|-2-\sum_i\kappa_{i,A}\ge0.
\tag{17}
\]

对循环 \(\ell\)-primary 分量，数字缺口二分把 \(\delta_A\) 送入严格较小商、
顶层核 Fourier 或锚点分离角色；若尝试把商解释为实际 Type II 模数，还必须通过
\(\mathscr L_{D_0}(h,a_0;p)\) 算术提升门。候选集为空时，账本记录
ARITHMETIC_LIFT_EMPTY，而不是把 \(\delta_A\) 误称为已完成递降。

因此跨状态记录至少有三种严格回执：

1. \(\operatorname{Surplus}_w>0\)：某个纤维直接 Type II 命中；
2. \(\operatorname{Surplus}_w\le0\) 且存在非空算术提升候选：保留可验证的低模后继；
3. 所有相关候选为空或角色不可提升：保留逐纤维缺口、核 Fourier 或
   ARITHMETIC_LIFT_EMPTY，转交另一条 Type I/II 射线或新的良基势。

## 边界例子

在 \(p=97,D=6,D_*=6\) 的三个参数纤维中，\(P_1=\{1,11\}\)、
\(P_2=\{1\}\)、\(P_3=\{1,13\}\)，目标 \(23\) 均缺失。最终稳定子吸收各自的
单列，三项需求均为零，而预算为非负数，所以没有跨纤维 surplus；把
\(11\) 与 \(13\) 直接相乘不属于本定理允许的聚合。

在抽象 \(G_*=C_5\) 中，若一个纤维有四个保持纤维且独立的二点块，最终稳定子为
平凡群，则 \(\sum\kappa=4>|G_*/T|-2=3\)，(7) 立即给出全群覆盖和目标命中。
这说明 surplus 阈值正好对应 Kneser 的“缺一层”边界。

## 研究边界

本定理现在给出了从来源 CRT、前缀 Hall 和 shared-q 账本到 (9) 的可计算下界注入
规则；但仍没有证明对所有核心素数都能选出满足 (10)--(14) 的来源标签分派，或使
式 (15) 严格为正。真正的全称缺口仍是：证明这种分派必产生正 surplus，或证明
剩余 \(\delta_A\) 必沿算术提升门、核 Fourier 或 Type I/F/G 势函数严格下降。
