---
kind: claim
claim_id: type-II-hall-surplus-kneser-price-injection
title: Type II Hall surplus 到 Kneser 活跃容量的价格注入桥
statement: 对同一已实现参数纤维中的有限 Hall 扩张序列，若每一步新增邻域槽中除一个锚槽外的 surplus 槽都能通过真实 source-switch、重复 q 去重和逐步稳定子非吸收条件注入一个独立可回译的 Kneser 源块，则这些槽按顺序产生的稳定子增长价格给出 Kneser 容量下界。若 |A_0|+sum_{c in E}|T_{iota(c)}|>|H|-|T_s|，目标纤维必命中 Type II；若价格注入失败，则输出 HALL_SURPLUS_UNPRICED，精确标明 q 重复、稳定子吸收、跨纤维或整数回译失败，不能把 Hall surplus 本身写成容量或递降。
claim_status: conditional
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-column-escape-finite-expansion-relay
  - type-II-multiblock-kneser-active-capacity-dichotomy
  - type-II-full-match-stabilizer-relay-certificate
  - type-II-source-fiber-qheight-kneser-bridge
  - type-II-q-layer-prefix-kneser-price-certificate
  - type-II-q-prefix-source-crt-fiber-concentration
topics:
- type-II
- Hall
- surplus
- Kneser
- active-capacity
- price-injection
- stabilizer
- q-adic
- source-switch
- proof-program
sources:
  - claim: type-II-source-column-escape-finite-expansion-relay
    role: finite-Hall-expansion-surplus
  - claim: type-II-multiblock-kneser-active-capacity-dichotomy
    role: Kneser-active-price
  - claim: type-II-full-match-stabilizer-relay-certificate
    role: stabilizer-growth-or-absorption
visibility: public
last_checked: '2026-08-05'
---

# Type II Hall surplus 到 Kneser 活跃容量的价格注入桥

## 1. Hall 扩张 surplus

固定一个已经通过 FIBER_REALIZED 的参数纤维，令 \(H\) 为目标有限阿贝尔群，
\(A_0\subseteq H\) 为非空初始积集。对一个有限独立请求扩张序列记
\[
U_0\subset U_1\subset\cdots\subset U_m,
\qquad U_t=U_{t-1}\cup\{r_t\}.
\tag{1}
\]
令
\[
C_t=N(U_t)\setminus N(U_{t-1}),\qquad
k_t=|C_t|\ge1.
\tag{2}
\]
从每个 \(C_t\) 选一个锚槽 \(a_t\)，把其余槽定义为
\[
E_t=C_t\setminus\{a_t\},\qquad
\eta=\sum_{t=1}^{m}|E_t|=\sum_{t=1}^{m}(k_t-1).
\tag{3}
\]
由有限源列逃逸扩张桥，\(\eta\) 是非负且可复核的 Hall surplus；它本身只表示
“额外邻域槽”，还不是目标集合容量。

## 2. 价格注入条件

称 \(E=\bigsqcup_tE_t\) 满足 **Kneser-PRICE-INJECTION**，若所有锚槽和 surplus 槽
都能放入同一个有序源块序列
\[
\mathcal D=(D_1,\ldots,D_s),\qquad
P_0=A_0,\quad P_j=P_{j-1}D_j,\quad T_j=\operatorname{Stab}_H(P_j),
\tag{4}
\]
且对每个 \(c\in E\) 都能给出一个实际源块
\[
B_c=\{1,g_c,g_c^2,\ldots,g_c^{e_c}\}\subseteq H
\tag{5}
\]
并验证：

1. **同纤维回译**：\(B_c\) 的每个可用指数都来自当前参数纤维的真实整数除子，
   source-switch、标签、SNF 和 \(B'>A\) 门全部通过；
2. **重复去重**：同一个 q 的共同账本、同一来源标签和已经吸收的重复层不在
   \(E\) 中重复出现；不同 \(c\) 的选择可以作为同一纤维中的独立块组合；
3. **逐步非吸收价格**：若 \(c\in E\) 在序列 \(\mathcal D\) 中占据位置
   \(\iota(c)\)，则要求 \(g_c\notin T_{\iota(c)}\)，从而该 surplus 块在当前
   稳定子下至少产生一个新 \(T_{\iota(c)}\)-陪集，且
   \(D_{\iota(c)}=B_c\)，价格为
   \(|T_{\iota(c)}|\)。锚槽对应的 \(D_j\) 可以被吸收，但必须仍有真实回译。
4. **规范 Fourier 见证**：对每个 surplus 位置 \(j=\iota(c)\)，保存一个商角色
   \[
   \chi_c\in\widehat{H/T_j},\qquad
   \chi_c(g_cT_j)\ne1.
   \tag{6}
   \]
   等价地，把 \(\chi_c\) 拉回 \(H\) 后有
   \(\chi_c|_{T_j}=1\) 且 \(\chi_c(g_c)\ne1\)。该角色由
   \(H/T_j\) 的 SNF 直接构造，作为 F/G 价格证书。

条件 (2) 是算术/标签检查，条件 (4) 的完整积集回译和逐步非吸收是稳定子检查；两者都不能由 Hall 图的
邻接关系自动推出。

## 3. Hall surplus 到 Kneser 容量

在 Kneser-PRICE-INJECTION 下，逐步 Kneser 增长给出
\[
|P_s|
\ge |A_0|+\sum_{c\in E}|T_{\iota(c)}|
\ge |A_0|+\eta.
\tag{7}
\]
因此若目标 \(t\in H\) 满足
\[
\boxed{
|A_0|+\sum_{c\in E}|T_{\iota(c)}|>|H|-|T_s|,
}
\tag{8}
\]
则
\[
t\in P_s,
\tag{9}
\]
从而由同纤维整数回译得到 Type II 短证书。

若 (8) 不成立但仍 \(t\notin P_s\)，保留精确的逐步稳定子缺口
\[
\delta_{\mathrm{price}}
 =|H|-|T_s|-|A_0|-\sum_{c\in E}|T_{\iota(c)}|\ge0
\tag{10}
\]
以及稳定子商 \(H/T_s\)。这条分支进入稳定子吸收、较小商 relay 或广义
\(2^j\) 终端，不能把 \(\eta\) 当作已经完成的整数下降。

## 4. 价格注入失败回执

若任一额外槽不能满足第 2 节条件，输出
\[
\mathrm{HALL\_SURPLUS\_UNPRICED}
\tag{12}
\]
并附第一失败原因：

* **Q\_DUPLICATE\_PRICE**：两个 surplus 槽只是同一 q 的重复来源，shared-q ledger
  合并后不能提供两个独立块；
* **STABILIZER\_ABSORBED\_PRICE**：在相应步骤 \(g_c\in T_{\iota(c)}\)，该块被吸收，
  不能计入 \(\sum_j|T_j|\)；
* **CROSS\_FIBER\_PRICE**：槽来自不同参数纤维，没有共同的完整积集 \(P_s\)；
* **INTEGER\_LIFT\_PRICE\_OBSTRUCTED**：SNF、source-switch、范围或 \(B'>A\)
  回译失败。

这些回执分别进入重复 q 账本、稳定子商、FIBER_REALIZED 或算术障碍分支。
只有所有额外槽都通过 (4)--(6) 后，才能使用 (8)；Hall surplus 单独不产生
Type II 证书。

## 5. 证明

对每个 surplus 位置 \(j=\iota(c)\)，有限阿贝尔群的角色分离性给出
\[
g_c\notin T_j
\iff
\exists\chi_c\in\widehat{H/T_j}:\chi_c(g_cT_j)\ne1.
\tag{11}
\]
因此 (6) 是逐步非吸收的规范 Fourier 见证。条件 \(g_c\notin T_j\) 给出单步 Kneser
不等式 \(|P_j|\ge|P_{j-1}|+|T_j|\)；锚槽和其它未定价块只使积集不减。
沿完整序列迭代得到 (7)。若目标缺失，则 \(P_sT_s=P_s\)，目标陪集 \(tT_s\)
与 \(P_s\) 不相交，所以 \(|P_s|\le|H|-|T_s|\)；这与 (8) 矛盾，故 (9) 成立。
若任一条件失败，逐步增长下界没有证明，按失败类型记录 (12)。
证毕。

## 6. 最终稳定子非吸收捷径

在价格注入的同一已实现纤维中，先按给定顺序完成全部源块插入，得到最终稳定子
\[
T_s=\operatorname{Stab}_H(P_s).
\tag{13}
\]
令 \(E\) 为 Hall surplus 槽中选定的代表，并假设每个代表都已经通过同纤维回译、
shared-q 去重和源块完整性门。若进一步满足
\[
\boxed{
g_c\notin T_s\quad\text{对所有 }c\in E,
}
\tag{14}
\]
则 (4)--(6) 的逐步非吸收条件自动成立：因为
\[
T_{\iota(c)}\le T_s,
\qquad
g_c\notin T_s\Longrightarrow g_c\notin T_{\iota(c)}.
\tag{15}
\]
因此可以直接输出构造性回执
\[
\mathrm{FINAL\_STABILIZER\_NONABSORBED\_PRICE}
=(T_s,E,\{T_{\iota(c)}\}_{c\in E}),
\tag{16}
\]
并得到
\[
|P_s|
\ge |A_0|+\sum_{c\in E}|T_{\iota(c)}|.
\tag{17}
\]
若 (8) 同时成立，(17) 立即给出 Type II 命中；若 (8) 不成立且目标仍缺失，则
直接转入 \(\bar H=H/T_s\) 的稳定子商 relay。

若存在 \(c\in E\) 使 \(g_c\in T_s\)，不能直接把它记为
STABILIZER_ABSORBED_PRICE：它可能在最终步骤之前曾经非吸收并贡献过合法价格。
此时必须回到实际插入时序，逐个检查 \(g_c\in T_{\iota(c)}\)：

* 若 \(g_c\in T_{\iota(c)}\)，该槽从价格账本删除并记为
  STABILIZER_ABSORBED_PRICE；
* 若 \(g_c\notin T_{\iota(c)}\)，仍可按其插入时稳定子收取
  \(|T_{\iota(c)}|\)，但不再使用 (14) 的捷径；
* 若同纤维或 shared-q 门失败，回执为 HALL_SURPLUS_UNPRICED 及其第一失败行。

### 证明

稳定子单调性给出 \(T_{\iota(c)}\le T_s\)。在 (14) 下，若
\(g_c\in T_{\iota(c)}\)，则 \(g_c\in T_s\)，矛盾，所以每个 surplus 代表在其插入
时都非吸收。逐步 Kneser 不等式逐项相加即得 (17)。若 (8) 成立，目标陪集与
\(P_s\) 不交会违反 (17)；若不成立，最终稳定子饱和恒等式把目标缺失传递到
\(H/T_s\)。最后一段是按插入时稳定子定义的穷尽，避免把最终吸收倒推为历史吸收。

## 7. q 层前缀的自动价格注入

PRICE-INJECTION 中的 q 进 surplus 不应按资源槽逐个复制源块。若 surplus 请求
带有固定来源标签，先用[Type II q 层请求的来源 CRT 纤维集中与唯一候选](type-II-q-prefix-source-crt-fiber-concentration.md)
筛选共同候选纤维；若一组请求都落在同一已实现纤维 \((D_*,A)\) 和同一 q 残数方向，
且每条边的可用层是 \(\{1,\ldots,h_r\}\)，则调用
[Type II q 层前缀匹配到纤维 Kneser 价格的规范压缩](type-II-q-layer-prefix-kneser-price-certificate.md)。
排序后的前缀 Hall 条件 \(h_{(k)}\ge k\) 给出一个规范层匹配
\(1,\ldots,n\)，并构造单个真实幂块
\[
B_q=\{1,\bar q,\ldots,\bar q^n\}.
\tag{18}
\]
若最终稳定子下 \(\operatorname{ord}_{H/T}(\bar qT)>1\)，则折叠塌缩引理强制
\(n+1<\operatorname{ord}_{H/T}(\bar qT)\)，该块自动支付恰 \(n\) 个活跃价格；
若 \(n+1\) 在插入时稳定子上达到有限阶，只登记 Q_PREFIX_ORDER_FOLD 并进入
稳定子塔；完成全部块后最终方向若被吸收则价格为零。相同商方向先合并，跨纤维请求只生成逐纤维账本，不能直接
相加。于是原条件中每个 surplus 槽的独立块要求可精化为：

* 同一纤维/同一 q 的槽只需通过一个前缀匹配和一个幂块回译；
* q 层前缀失败输出 Q_PREFIX_MATCHING_DEFICIT，不计入价格；
* 最终吸收、插入层有限阶、方向重复和跨纤维分别输出
  Q_PREFIX_FINAL_STABILIZER_ABSORBED、Q_PREFIX_ORDER_FOLD、
  Q_DIRECTION_DUPLICATE_OBSTRUCTED 或 Q_PREFIX_PRICE_FRAGMENTED。

在所有这些门通过后，所得幂块按 (4)--(6) 放入同一有序源块序列；式 (8) 的
Kneser 阈值才可使用。这个接口减少了重复 q 的未定价范围，但没有把不同候选
\((D_*,A)\) 自动合并为一个纤维。

## 8. 边界反例

### 稳定子吸收反例

取 \(H=C_4\)、\(A_0=\{0\}\)，两个额外槽都声称携带
\[
B_1=B_2=\{0,2\}.
\]
第一个块加入后 \(T_1=\{0,2\}\)，因此两个块都在相应步骤被吸收。即使 Hall
扩张账本记录 \(\eta=2\)，也不能把它们计入逐步价格；该情形必须输出
\(\mathrm{STABILIZER\_ABSORBED\_PRICE}\)。

### 重复 q 反例

若两个槽来自同一 q 的两条来源，但共同 q 账本只允许一个可回译层，则把它们
分别计入 \(\eta\) 会制造虚假的 surplus。合并后其中一个槽应删除，输出
\(\mathrm{Q\_DUPLICATE\_PRICE}\)。

### 真正可定价的边界

取 \(H=C_8\)、\(A_0=\{0\}\)，把三个 surplus 槽定价为
\(B_1=B_2=B_3=\{0,1\}\)，并把一个未计价锚槽取为 \(B_4=\{0,4\}\)。
前三步的稳定子均为平凡群，故逐步价格和为 \(1+1+1\)；第四步后
\(P_4=C_8\)、\(T_4=H\)。于是
\[
|A_0|+\sum_{j=1}^{3}|T_j|=4>|H|-|T_4|=0,
\]
式 (8) 给出目标命中。这说明价格必须按插入时的稳定子记录，不能用最终稳定子
回溯收费。

## 研究边界

该桥首次把有限源列扩张的 Hall surplus 转成有单位的 Kneser 活跃容量，并把
“surplus 不可收费”的三类结构性原因显式分开。它仍是条件性结论：当前全局缺口
是证明每个实际 q 释放分支都满足 PRICE-INJECTION，或在失败时把回执提升为
稳定子商、广义 \(2^j\) 终端、Type I/F/G 出口或保持标签的严格递降。
