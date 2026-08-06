---
kind: claim
claim_id: type-II-hall-source-column-closure-relay
title: Type II 固定纤维 Hall 缺口的全源列闭包—商递降三分
statement: 在一个已通过 source-switch/SNF 的有限固定纤维中，若 Hall 缺口的线性对偶角色已经提升为真实阶 ell 角色，并且该角色在该纤维的全部规范源列上平凡，则源集落入核 K。目标相位非平凡且 |K|>1 时给出严格商缺失和可提升的全局 annihilator relay；K=1 时给出顶层 primary 终端候选。目标相位平凡时，目标与源集同落在真核子群中，先输出可计算的 annihilator subgroup relay，并通过 SNF/source-switch 提升门；提升失败才保留关系 Fourier 与精确 lift obstruction。若存在源列被角色分离，输出 SOURCE_COLUMN_ESCAPE，并要求将该列加入完整 Hall 菜单或记录其有限算术边障碍。由此，source-column-closed 的 Hall 缺口不再是未分类的 UNRELAYABLE_HALL_DEFICIT。
claim_status: conditional
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-hall-deficit-linear-dual-bridge
  - type-II-anchor-rank-fourier-dispatch
  - type-II-source-fiber-finite-abelian-composition-relay
  - type-II-stabilizer-kernel-quotient-descent-trichotomy
  - type-II-source-column-escape-finite-expansion-relay
  - type-II-annihilator-two-sided-subgroup-quotient-descent
topics:
- type-II
- Hall
- source-column
- annihilator
- quotient-descent
- Fourier
- fixed-fiber
- source-switch
- proof-program
sources:
  - claim: type-II-hall-deficit-linear-dual-bridge
    role: hall-to-character
  - claim: type-II-anchor-rank-fourier-dispatch
    role: target-phase-dispatch
  - claim: type-II-source-fiber-finite-abelian-composition-relay
    role: finite-abelian-quotient-relay
visibility: public
last_checked: '2026-08-06'
---

# Type II 固定纤维 Hall 缺口的全源列闭包—商递降三分

## 1. 固定纤维和规范源列

固定一个已经通过来源标签、source-switch、SNF 和范围门的有限参数纤维。将其
源和集乘以一个基点的逆元规范化为

\[
R=\{1\}\,B_1\cdots B_s\subseteq H,\qquad
\tau\in H\setminus R,
\tag{1}
\]

其中 \(H\) 是有限阿贝尔目标商，\(\tau\) 是规范目标。令
\(g_1,\ldots,g_s\) 为所有实际源块的单位生成元；指数盒的每个元素都是这些
\(g_i\) 的乘积。固定一个 \(\ell\)-初等源商 \(V_\ell\)，并把每个源列记为
\(v_i\in V_\ell\)。

Hall 图中的请求 \(U\) 已经去除线性依赖，且其合法邻域 \(N(U)\) 的源列张成
\[
W_U=\operatorname{span}_{\mathbb F_\ell}\{v_c:c\in N(U)\}.
\tag{2}
\]
若 \(|N(U)|<|U|\)，固定纤维线性桥给出
\[
\lambda\in V_\ell^\*,\qquad
\lambda|_{W_U}=0,\qquad
\lambda|_{D_U}\ne0.
\tag{3}
\]
把 \(\lambda\) 提升为真实阶 \(\ell\) 角色
\[
\chi_\lambda:H\longrightarrow\mu_\ell .
\tag{4}
\]

定义 **全源列闭包** 条件
\[
\mathrm{SCClosed}(U,\lambda)
\iff
\lambda(v_i)=0\quad(1\le i\le s).
\tag{5}
\]
式 (5) 是有限矩阵检查，不要求把不同源列重复计入容量；它检查的是当前固定
纤维中所有实际源生成元，而不只是 Hall 缺口的邻域槽。

## 2. 全源列闭包定理

若 \(\mathrm{SCClosed}(U,\lambda)\) 成立，令
\[
K=\ker\chi_\lambda.
\tag{6}
\]
由 (5)，每个 \(B_i\subseteq K\)，从而
\[
\boxed{R\subseteq K.}
\tag{7}
\]
因此目标相位给出完备三分：

### A. 目标被分离且核非平凡

若
\[
\chi_\lambda(\tau)\ne1,\qquad |K|>1,
\tag{8}
\]
则自然商
\[
\pi_\lambda:H\to H/K\simeq C_\ell
\tag{9}
\]
满足
\[
\pi_\lambda(R)=\{1\},\qquad
\pi_\lambda(\tau)\ne1.
\tag{10}
\]
所以目标在严格较小商中缺失，记录
\[
\mathrm{GLOBAL\_ANNIHILATOR\_LOWER\_RELAY}
=(\ell,K,\pi_\lambda,\pi_\lambda(R),\pi_\lambda(\tau)).
\tag{11}
\]
若商的来源参数纤维门、标签回译和 E1--E5 通过，(11) 是保持来源的严格递降；
否则保留 \(\mathrm{GLOBAL\_ANNIHILATOR\_LIFT\_OBSTRUCTED}\)，不能把抽象商
自动写成原猜想的递降。

### B. 目标被分离但没有可降核

若 \(\chi_\lambda(\tau)\ne1\) 而 \(|K|=1\)，则 \(H\simeq C_\ell\) 是当前
primary 的顶层商，(10) 没有严格更小的群。记录
\[
\mathrm{TOP\_PRIMARY\_ANNIHILATOR}
=(\ell,\chi_\lambda,\tau),
\tag{12}
\]
并转入广义 \(2^j\)/顶层 F/G 或有限算术终端；不能虚构一个同阶递降。若当前
源列已按二点关系块分组，则 \(K=1\) 与 (5) 还强制所有非零
\(\ell\)-primary 关系块数为 \(c_0=0\)，可同时输出
\[
\mathrm{CYCLIC\_PRIMARY\_DIGIT\_DEFICIT}(\ell,0),
\tag{12a}
\]
这是已有循环进位终端的精确层缺口，而不是未分类的角色存在。

### C. 目标相位未被分离

若
\[
\chi_\lambda(\tau)=1,
\tag{13}
\]
则 \(\tau\in K\)，而 (7) 已给出 \(R\subseteq K\)。因此原目标缺失保留在真子群
\(K\) 中；调用
[Type II 全源列闭合的 annihilator 子群—商双向严格递降](type-II-annihilator-two-sided-subgroup-quotient-descent.md)
输出
\(\mathrm{ANNIHILATOR\_SUBGROUP\_LOWER\_RELAY}\)。若其整数
SNF/source-switch/标签提升门通过，升级为
\(\mathrm{SUBGROUP\_SOURCE\_SWITCH\_DESCENT}\)；若提升失败，角色仍可因
\(\lambda|_{D_U}\ne0\) 而分离一个请求关系方向，但不能伪称原问题已经下降，此时回执为
\[
\mathrm{RELATION\_FOURIER\_NO\_TARGET\_SEPARATION}.
\tag{14}
\]
同时附上 \(\mathrm{ANNIHILATOR\_SUBGROUP\_LIFT\_OBSTRUCTED}\) 的具体 SNF/CRT
失败行。该角色不能作为新的目标容量单位重复收费；后继应走已闭合的关系 Fourier、
F/G 出口或另一条保持标签的递降。

## 3. 未闭合源列的精确回执

若 (5) 不成立，取一个确定的源列 \(v_i\) 使
\[
\lambda(v_i)\ne0.
\tag{15}
\]
记录
\[
\mathrm{SOURCE\_COLUMN\_ESCAPE}=(i,v_i,\lambda(v_i)).
\tag{16}
\]
这不是容量缺口的证明，而是说明当前 Hall 图没有包含该源列对本固定纤维的全部
影响。随后只有两种合法处理：

1. 若 \(g_i\) 对某个当前需求有已证明的 source-switch/SNF 边，则把该边加入
  完整 Hall 菜单，重新计算最大匹配和最小割；
2. 若所有候选边均失败，则保存失败行作为
   \(\mathrm{SOURCE\_COLUMN\_EDGE\_OBSTRUCTED}\)，不能把该列从源集合中静默删除。

固定纤维的源列菜单是有限的，所以对固定的 \((U,\lambda)\) 检查 (15) 必然终止；
若加入合法边导致 Hall 状态改变，则将其作为新的有限状态重新计算，不能把一次
检查自动宣称为全局闭合。只有在同一状态的全部源列均已纳入、或其失败行均已保存
时，才回到 (5) 的 A--C 三分。跨纤维列没有合法回译时，输出
\(\mathrm{UNREALIZED\_SOURCE\_COLUMN}\)，而不是套用固定纤维商递降。

若逃逸源列只有连接当前请求集之外的合法同纤维边，则调用
[Type II 源列逃逸的有限独立请求扩张递降桥](type-II-source-column-escape-finite-expansion-relay.md)：
外部请求方向独立时扩张 \(U\) 并重算 q 容量和 Rado 角色；方向依赖时记录具体
DEPENDENT\_SOURCE\_ESCAPE\_RELATION；若 q 容量释放则回到秩/Hall 分派。该扩张
每次至少加入一个新请求，因而是有限过程；只有得到 SOURCE\_COLUMN\_CLOSED、
显式边障碍或后继出口时，才可继续 A--C 三分。

## 4. 支配割的自动闭包

若对每个实际源生成元 \(g_i\)，都能在同一固定纤维中找到一个请求
\(r_i\in U\) 及其合法邻域槽 \(c_i\in N(U)\)，且该槽携带的源列正是 \(v_i\)，则称
\(U\) 为 **SOURCE-DOMINATING-CUT**。此时
\[
v_i\in W_U\quad\text{对所有 }i,
\tag{17}
\]
而 (3) 立即给出 \(\lambda(v_i)=0\)，所以
\[
\mathrm{SOURCE\text{-}DOMINATING\text{-}CUT}
\Longrightarrow
\mathrm{SCClosed}(U,\lambda).
\tag{18}
\]
这是一组有限的边成员检查；它把逐列闭包从额外假设降为当前最小割的可计算性质。
若同时 \(\chi_\lambda(\tau)\ne1\) 且 \(|K|>1\)，则直接进入 (11) 的
\(\mathrm{GLOBAL\_ANNIHILATOR\_LOWER\_RELAY}\)；否则按 B/C 分支处理。

## 5. 证明

由 (5)，每个源生成元 \(g_i\) 都在 \(\ker\chi_\lambda=K\) 中；由于 \(K\) 是子群，
指数盒的任意乘积都在 \(K\)，得到 (7)。若 (8) 成立，\(\pi_\lambda\) 是非平凡
有限商，且 (10) 说明目标不在投影源集，故得到商缺失；\(|K|>1\) 使商阶
\(|H/K|=\ell<|H|\)，第一坐标严格下降。若 \(|K|=1\)，则
\(|H|=\ell\)，只能记录顶层分支。若 (13) 成立，则 \(\tau\in K\)，而 (7) 与
规范化的 \(1\in R\)、\(\tau\notin R\) 给出 \(R,\tau\subseteq K\)、\(K\ne1\)。
因此同一目标缺失严格限制到真子群 \(K\)；关系 Fourier 只在该子群的
SNF/source-switch/标签提升失败后作为不收费障碍保留。若 (5) 失败，(15) 是有限源列
成员检查的反证；合法边存在时必须将其纳入完整图，边不存在时其 SNF/CRT/范围失败行
正是算术障碍。固定 \((U,\lambda)\) 的源列成员检查是有限的；若选择加入合法边，新增
状态必须重新验证 Hall 条件和势，故本引理只保证每个已闭合状态的 A--C 三分，不把
有限菜单误写成跨状态自动终止。证毕。

## 6. 边界例子

### 严格商 relay

用加法记号取 \(H=C_8\)、\(R=\{0,4\}\)、\(\tau=1\)，
\(\chi(x)=(-1)^x\)。源列 \(4\) 被 \(\chi\) 湮灭，故
\(K=\{0,2,4,6\}\)、\(|K|=4\)，而
\(\tau\notin K\)。商为 \(C_2\)，目标严格缺失，满足 A。

### 顶层无下降

取 \(H=C_2\)、\(R=\{0\}\)、\(\tau=1\)。非平凡角色的核为零，
\(|K|=1\)，只能记录 TOP_PRIMARY_ANNIHILATOR。

### 源列逃逸

取 \(H=C_8\)、\(R=\{0,1\}\)、\(\tau=3\)，仍取
\(\chi(x)=(-1)^x\)。源列 \(1\) 满足 \(\chi(1)=-1\)，故 (5) 失败；它必须作为
\(\mathrm{SOURCE\_COLUMN\_ESCAPE}\) 加回 Hall 菜单，不能把 \(R\) 错写成落在
\(\ker\chi\) 中。

## 研究边界

该引理把固定纤维 Hall 对偶角色的适用范围精确分开：全源列闭合时，目标相位非平凡
给出严格商 relay，目标相位平凡则先给出严格的核子群状态，再由整数提升门决定是否
成为可提升递降；源列未闭合时产生可枚举的
\(\mathrm{SOURCE\_COLUMN\_ESCAPE}\) 或算术障碍。它仍不证明每个跨纤维 Hall 缺口
都能通过 FIBER_REALIZED，也不保证顶层或提升失败分支自动产生 Type I/F/G；但它
消除了“只对当前邻域槽平凡就可递降”和“目标相位平凡即无下一步”的两个逻辑跳步。
