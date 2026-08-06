---
kind: claim
claim_id: type-II-source-column-escape-finite-expansion-relay
title: Type II 源列逃逸的有限独立请求扩张递降桥
statement: 在有限且已完成同纤维合法边枚举的 q 进容量缺口中，若当前独立请求集 U 的 Rado 对偶角色 lambda 分离某个真实源列，则沿该源列的合法外部边加入一个仍保持独立的请求。每次扩张至少带来一个新邻域槽，Hall 缺口不增加；有限请求集使过程终止于源列闭合、q 进容量释放、无合法源边的显式障碍，或一个外部请求方向落在当前需求张成空间内的具体依赖关系。该过程把 SOURCE-DOMINATING-CUT 从初始强假设降为有限可枚举的扩张分支，但不把关系回执或容量释放自动写成整数递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-cross-state-layered-rado-qcapacity-cut
  - type-II-hall-deficit-linear-dual-bridge
  - type-II-cross-state-source-relation-role-capacity-dispatch
  - type-II-rado-linear-rank-hall-capacity-bridge
  - type-II-annihilator-two-sided-subgroup-quotient-descent
topics:
- type-II
- source-column
- Hall
- q-adic
- finite-expansion
- Fourier
- dependency-relation
- source-switch
- proof-program
sources:
  - claim: type-II-cross-state-layered-rado-qcapacity-cut
    role: q-layer-capacity-deficit
  - claim: type-II-hall-deficit-linear-dual-bridge
    role: Rado-dual-source-separation
  - claim: type-II-cross-state-source-relation-role-capacity-dispatch
    role: dependent-request-relation-dispatch
visibility: public
last_checked: '2026-08-05'
---

# Type II 源列逃逸的有限独立请求扩张递降桥

## 1. 有限菜单与当前缺口

固定一个参数纤维、奇素数 \(q\) 和 primary \(\ell\)。令
\[
\Gamma^+=(\mathcal R,\mathcal C;E^+)
\]
是已经完成来源标签、SNF、CRT、真实 q 整除和范围门的有限同纤维请求图。每个
请求 \(r\in\mathcal R\) 带有真实需求向量
\[
d(r)\in D_\ell,
\]
每个槽 \(c\in\mathcal C\) 带有真实源列 \(v_c\in V_\ell\)。每个固定纤维的真实源生成元
\(g_i\) 记作 \(v_i\in V_\ell\)，并只允许使用 \(E^+\) 中携带 \(v_c=v_i\) 的同纤维
源边。

取一个请求集 \(U\subseteq\mathcal R\)，要求
\[
\{d(r):r\in U\}\quad\text{线性独立}.
\tag{1}
\]
记
\[
N(U)=\{c:\exists r\in U,\ (r,c)\in E^+\},\qquad
W(U)=\operatorname{span}_{\mathbb F_\ell}\{v_c:c\in N(U)\}.
\tag{2}
\]
若逐层 q 进上界给出
\[
\mathsf C_q(U)<|U|,
\tag{3}
\]
则 \(|N(U)|<|U|\)，并且 Rado 对偶桥构造
\[
\lambda_U\in V_\ell^\*,\qquad
\lambda_U|_{W(U)}=0,\qquad
\lambda_U|_{\operatorname{span}d(U)}\ne0.
\tag{4}
\]

称源生成元 \(i\) 在 \(U\) 上 **逃逸**，若
\[
\lambda_U(v_i)\ne0.
\tag{5}
\]
这比单纯“没有直接邻接边”更精确：若 \(v_i\in W(U)\)，即使当前没有标记为
source-dominating，也已经被 \(\lambda_U\) 湮灭，不需要重复扩张。

## 2. 一步扩张

设 \(i\) 在 \(U\) 上逃逸。因为 \(\lambda_U\) 在 \(W(U)\) 上为零，任何携带
\(v_c=v_i\) 的合法槽都不在 \(N(U)\)。考虑所有同纤维源边
\[
\mathcal E_i(U)=\{(r,c)\in E^+:\ v_c=v_i\}.
\tag{6}
\]

### 独立外部边

若存在 \((r,c)\in\mathcal E_i(U)\) 使 \(r\notin U\) 且
\[
d(r)\notin\operatorname{span}d(U),
\tag{7}
\]
令
\[
U'=U\cup\{r\},\qquad
k(r\mid U)=|N(U')\setminus N(U)|.
\tag{8}
\]
由于 \(c\in N(U')\setminus N(U)\)，有 \(k(r\mid U)\ge1\)。于是 Hall 缺口
\[
\delta(U)=|U|-|N(U)|
\]
满足精确恒等式
\[
\boxed{\delta(U')=\delta(U)-\bigl(k(r\mid U)-1\bigr)\le\delta(U).}
\tag{9}
\]
若 \(k(r\mid U)\ge2\)，则得到构造性的
\[
\mathrm{HALL\_ESCAPE\_EXPANSION\_SURPLUS}
\bigl(i,r,c,k(r\mid U)-1\bigr),
\tag{10}
\]
并且 Hall 缺口严格下降。若 \(k=1\)，缺口保持但独立请求数增加；这是有限扩张步骤，
不能把它误写成容量 surplus。

扩张后重新计算 \(\mathsf C_q(U')\) 和 Rado 对偶角色。若
\[
\mathsf C_q(U')\ge |U'|,
\tag{11}
\]
则原 q 进切割被释放，输出
\[
\mathrm{Q\_ADIC\_ESCAPE\_EXPANSION\_RELEASE}
(U,U',k,\mathsf C_q(U')-|U'|),
\tag{12}
\]
并转入线性秩/Hall 分派；不能继续沿用旧的 q 缺口角色。
若新增邻域槽还满足 Kneser-PRICE-INJECTION，则可进一步调用
[Type II Hall surplus 到 Kneser 活跃容量的价格注入桥](type-II-hall-surplus-kneser-price-injection.md)；
若所有 surplus 代表在最终稳定子中仍非平凡，还可直接使用
FINAL\_STABILIZER\_NONABSORBED\_PRICE 捷径；否则必须输出
HALL\_SURPLUS\_UNPRICED，并按重复 q、稳定子吸收、跨纤维或整数回译障碍分派。

### 依赖外部边

若所有 \((r,c)\in\mathcal E_i(U)\) 的外部请求都满足
\[
d(r)\in\operatorname{span}d(U),
\tag{13}
\]
则从任取一条外部边得到已知系数 \(a_s\in\mathbb F_\ell\)，使
\[
d(r)=\sum_{s\in U}a_s d(s).
\tag{14}
\]
记录具体依赖回执
\[
\mathrm{DEPENDENT\_SOURCE\_ESCAPE\_RELATION}
=\left(i,r,c,\ a_s\right).
\tag{15}
\]
该回执进入 SOURCE_RELATION_FOURIER 或关系角色分派；它不能作为一个新的独立
q-height 请求，也不能增加 Kneser 目标集合容量。

### 无合法边

若
\[
\mathcal E_i(U)=\varnothing,
\tag{16}
\]
则输出
\[
\mathrm{SOURCE\_COLUMN\_EDGE\_OBSTRUCTED}(i),
\tag{17}
\]
并附上该源列的完整 SNF/CRT/范围失败行。不能把它静默删除，也不能把 (3) 单独
解释成递降。

## 3. 有限终止三分

从 \(U_0=U\) 开始，只在 q 进缺口仍满足 (3) 且存在满足 (7) 的外部边时执行独立
扩张。每一步都加入一个此前不在 \(U_t\) 的请求，因此
\[
|U_{t+1}|=|U_t|+1.
\tag{18}
\]
请求集 \(\mathcal R\) 有限，故至多 \(|\mathcal R|-|U_0|\) 次后终止。终止时至少有
下列四种回执之一：

1. **SOURCE\_COLUMN\_CLOSED**：某个 Rado 角色 \(\lambda_t\) 满足
   \(\lambda_t(v_i)=0\) 对全部真实源列成立。此时可直接使用全源列
   annihilator 三分，不再要求每个源列都有一条直接邻接边；
2. **Q\_ADIC\_ESCAPE\_EXPANSION\_RELEASE**：式 (11) 成立，q 进缺口消失，转入
   线性秩、普通 Hall 或 Kneser 分支；
3. **DEPENDENT\_SOURCE\_ESCAPE\_RELATION**：式 (15) 给出关系 Fourier 输入；
4. **SOURCE\_COLUMN\_EDGE\_OBSTRUCTED**：式 (17) 给出有限算术负证书。

若所有真实源列均有至少一条合法边，且 q 缺口在每一步保持，则不可能无限停留在
SOURCE_COLUMN_ESCAPE：要么进入 (1) 的全源列闭合，要么加入新的独立请求，最终因
(18) 终止。这个有限扩张过程将初始的 SOURCE-DOMINATING-CUT 强假设替换成
可枚举的“扩张—重算—回执”程序。

## 4. 证明

式 (4) 由 (3) 和 Rado 线性对偶性得到。若 (5) 成立，而某个合法槽
\(c\in N(U)\) 满足 \(v_c=v_i\)，则
\(\lambda_U(v_i)=\lambda_U(v_c)=0\)，矛盾；所以逃逸源列的每条合法边都携带
\(N(U)\) 之外的新槽。满足 (7) 的外部请求加入后，至少有一个新邻域槽，故
\(k\ge1\)，直接计算得到 (9)。若 q 容量通过，则 (12) 是优先切割规则；若不通过，
新请求仍保持独立，因而可以重新应用 (4)。

若不存在独立外部边而存在外部边，则 (14) 是有限维坐标消元给出的显式关系；
若不存在任何边，则 (16)--(17) 是完整有限菜单上的穷尽。每次继续扩张严格增加
\(|U_t|\)，故 (18) 给出良基终止。终止分支的四项正好覆盖“新独立边、依赖边、无边、
角色已湮灭或 q 容量释放”，证毕。

## 5. 边界例子

### 严格 Hall 缺口下降

令 \(U=\{r_1\}\)、\(N(U)=\{c_1\}\)，另有
\[
N(r_2)=\{c_2,c_3\},\qquad v_{c_2}=v_{c_3}=v_i,
\]
且 \(v_i\) 被当前 \(\lambda_U\) 分离。加入独立请求 \(r_2\) 后
\(k=2\)，故 \(\delta\) 严格下降一个单位，得到 (10)。

### 依赖关系分支

在 \(D_\ell=\mathbb F_2 e_1\) 中，令
\(d(r_1)=d(r_2)=e_1\)，而逃逸源列 \(v_i\) 只有一条合法外部边接到 \(r_2\)。
该边不能扩大独立请求集；记录
\[
d(r_2)+d(r_1)=0
\]
作为 (15)，而不是伪造第二个独立容量单位。

### 无边障碍

若逃逸源列 \(v_i\) 在完整 SNF/CRT/范围菜单中没有任何合法边，则 (17) 是有限
可复核的算术障碍；当前 q 缺口仍未自动转成整数下降。

## 6. 两阶段良基闭包势

对当前独立请求集 \(U\) 定义扩张势
\[
\Psi_{\mathrm{esc}}(U)
=|\mathcal R|-|U|.
\tag{19}
\]
只要 q 进缺口仍满足 \(\mathsf C_q(U)<|U|\)，且当前 Rado 角色分离某个逃逸源列，
每加入一个满足 (7) 的独立外部请求 \(r\)，都有
\[
\Psi_{\mathrm{esc}}(U\cup\{r\})
=\Psi_{\mathrm{esc}}(U)-1.
\tag{20}
\]
因此独立扩张阶段不可能循环。与此同时，邻域增量 \(k(r\mid U)\) 给出
\[
\delta(U\cup\{r\})
=\delta(U)-(k(r\mid U)-1)\le\delta(U),
\tag{21}
\]
所以每一步同时保持 Hall 缺口不增。

扩张阶段终止后，按下列二级势/回执接续：

1. 若新角色湮灭全部真实源列，定义
   \[
   \Psi_{\mathrm{relay}}(\sigma)
   =\bigl(|H|,\ |H/T|,\ \delta(\sigma)\bigr),
   \tag{22}
   \]
   并调用全源列 annihilator 二分。目标在核外时商阶严格下降；目标在核内时
   真子群阶严格下降；整数 source-switch 通过后才登记可提升递降。
2. 若 \(\mathsf C_q(U')\ge|U'|\)，输出
   Q_ADIC_ESCAPE_EXPANSION_RELEASE，停止沿用旧的缺口角色，转入新的
   rank/Hall/Kneser 状态；不能把 (20) 当作 Type II 命中。
3. 若只有依赖外部边，输出
   DEPENDENT_SOURCE_ESCAPE_RELATION；该边给出关系 Fourier 输入，但不增加
   \(\Psi_{\mathrm{esc}}\) 的独立请求数。
4. 若无合法边，输出
   SOURCE_COLUMN_EDGE_OBSTRUCTED，并保存该源列的完整 SNF/CRT/范围失败账本。

于是，对有限输入图，扩张—闭包程序穷尽为
\[
\boxed{
\text{严格请求势下降}
\ \longrightarrow\
\text{群阶 relay}
\ \text{或 q 容量释放}
\ \text{或关系/算术障碍}.
}
\tag{23}
\]
只有第一类和第二类在相应整数提升门通过时才是统一选择器的递归边；后两类是
typed 非递归回执，不能被伪装成已经完成的下降。

### 证明

式 (20) 由 \(|U|\) 每次增加 1 直接得到，且 \(|\mathcal R|\) 固定有限，因此
独立扩张阶段至多进行 \(|\mathcal R|-|U_0|\) 次。式 (21) 是 (9) 的重写。
阶段终止时，若角色湮灭全部源列，有限阿贝尔核/商二分给出 (22) 的第一坐标严格
下降；若目标相位平凡则限制到真子群，仍降低 \(|H|\)。否则 q 容量已释放、边
依赖或边菜单为空，分别对应 2--4 的互斥回执。故 (23) 穷尽且无无限扩张，证毕。

## 研究边界

该引理把“q 缺口必须一开始就满足 SOURCE-DOMINATING-CUT”的条件降为有限扩张
检查，并新增了可计量的 HALL_ESCAPE_EXPANSION_SURPLUS 与依赖关系回执。它仍
不证明 q 容量释放分支必然命中 Type I/II，也不证明无边障碍在所有核心素数上必然
不存在；后两者仍需接入整数 source-switch、E1--E5 提升或广义 \(2^j\) 终端。
