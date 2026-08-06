---
kind: claim
claim_id: type-II-rado-linear-rank-hall-capacity-bridge
title: Type II 顶层角色的 Rado 线性 rank-Hall 容量桥
statement: 对固定源纤维的 ell 初等商向量空间 V，给每个独立顶层 Fourier/关系角色一个允许 q 进槽集合，并给每个槽标记其真实源列向量 v_c。存在把所有角色分配到不同槽且所选源列线性独立的容量映射，当且仅当每个请求子集 U 的邻域源列秩至少为 |U|。秩条件失败时给出 LINEAR_RANK_DEFICIT(ell,U)；普通 Hall 数量匹配通过但线性秩失败的情形不能计入容量。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-anchor-rank-fourier-dispatch
  - type-II-composition-kernel-role-rank-capacity-bridge
  - type-II-source-fiber-elementary-rank-qheight-injection
  - type-II-cross-state-source-demand-hall-capacity-bridge
topics:
  - type-II
  - Rado
  - matroid
  - linear-rank
  - Hall
  - Fourier
  - q-adic
  - capacity
  - source-relation
sources:
  - claim: type-II-anchor-rank-fourier-dispatch
    role: independent-role-demand
  - claim: type-II-composition-kernel-role-rank-capacity-bridge
    role: top-kernel-rank-lower-bound
  - claim: type-II-source-fiber-elementary-rank-qheight-injection
    role: source-column-vector-map
  - claim: type-II-cross-state-source-demand-hall-capacity-bridge
    role: slot-compatibility-and-arithmetic-edges
visibility: public
last_checked: '2026-08-05'
---

# Type II 顶层角色的 Rado 线性 rank-Hall 容量桥

## 1. 角色请求和源列向量

固定一个参数纤维和素数 \(\ell\)，令
\[
V_\ell=A_{\ell}/\ell A_{\ell}
\]
是保持该纤维的真实源关系列在 \(\ell\)-primary 商中的初等向量空间。顶层
Fourier dispatch 或 composition-kernel bridge 已经给出一组线性独立的角色需求
\[
\mathcal R_\ell=\{r_1,\ldots,r_m\}.
\]
每个实际 q 进资源槽 \(c\in\mathcal C_\ell\) 带有一个源列向量
\[
v_c\in V_\ell,
\]
它由该槽对应的单位源列在 \(A_\ell/\ell A_\ell\) 中的像确定。相同 q 的重复来源、
稳定子吸收列和不保持参数纤维的列先删除或合并；克隆槽不会克隆同一个线性向量的
秩。

对每个角色请求 \(r\)，定义允许槽集合
\[
\mathcal C(r)\subseteq\mathcal C_\ell
\]
为所有通过 source-switch、SNF、真实 q-height、标签合同和范围门的槽。一个
**线性 rank-realizing matching** 是一个注入
\[
f:\mathcal R_\ell\hookrightarrow\mathcal C_\ell
\]
满足
\[
f(r)\in\mathcal C(r),
\qquad
\{v_{f(r)}:r\in\mathcal R_\ell\}
\text{ 线性独立}.
\tag{1}
\]

这里的“独立”是源关系容量的真实含义；只计槽数量而不看 \(v_c\) 会重复支付同一
初等方向。

## 2. Rado 秩—Hall 定理

对任意请求子集 \(U\subseteq\mathcal R_\ell\)，令
\[
N(U)=\bigcup_{r\in U}\mathcal C(r),
\qquad
\rho(U)=\operatorname{rank}_{V_\ell}\{v_c:c\in N(U)\}.
\]
则存在线性 rank-realizing matching，当且仅当
\[
\boxed{
\rho(U)\ge |U|
\qquad\text{对所有 }U\subseteq\mathcal R_\ell.
}
\tag{2}
\]

这是把 Hall 婚配定理应用到槽集上的线性拟阵；也称 Rado 的独立代表定理。

### 证明

必要性显然：\(U\) 中的请求必须由 \(N(U)\) 中不同槽实现，且对应源列独立，
所以 \(|U|\le\rho(U)\)。

充分性是 Rado 独立代表定理。为使回执可构造，可在向量拟阵上运行增广路径算法：
从空选择开始，每一步尝试把一个未代表请求接到其允许槽；若新增向量落在当前
张成空间中，则沿交替路径替换已选槽，直到得到独立增广，或得到一个无法扩张的
交替闭包 \(U\)。无法扩张时，闭包中的所有允许槽都在已选源列张成空间内，且
\(\rho(U)<|U|\)，给出秩缺口；若算法覆盖全部请求，则得到 (1)。这正是 Rado
定理的拟阵增广证明。证毕。

对固定有限输入，增广过程同时输出一个显式匹配或一个最小/规范秩缺口子集；无需
把重复向量复制成新的容量。

## 3. 与普通 Hall 和 q-height 的区别

普通 Hall 只检查
\[
|N(U)|\ge|U|.
\]
线性 rank-Hall 检查的是
\[
\operatorname{rank}\{v_c:c\in N(U)\}\ge|U|.
\]
因此普通 Hall 通过并不意味着真实源容量通过。例如在
\(V_{\ell}=\mathbb F_2^2\) 中，两个请求都允许两个槽，但
\[
v_{c_1}=v_{c_2}=(1,0).
\]
普通 Hall 有完整匹配，而
\[
\rho(\{r_1,r_2\})=1<2
\]
给出
\[
\mathrm{LINEAR\_RANK\_DEFICIT}(\ell=2,\{r_1,r_2\}).
\]
这两个槽只是同一源方向的重复层，不能支付两个独立顶层角色。

相反，若
\[
v_{c_1}=(1,0),\qquad v_{c_2}=(0,1),
\]
则所有请求子集的秩条件通过，显式选择 \(c_1,c_2\) 给出两个独立容量方向。

## 4. 对统一选择器的分派

对 \(\mathcal R_\ell\) 由锚点—秩 dispatch 产生的独立角色请求，计算 Rado 秩条件：

1. 若 (2) 通过，输出每个角色对应的真实 q 进槽和独立源列基；这些请求才可
   进入 Hall q-height/Kneser 容量；
2. 若某个 \(U\) 满足 \(\rho(U)<|U|\)，输出
   \[
   \mathrm{LINEAR\_RANK\_DEFICIT}(\ell,U,\rho(U),|U|),
   \tag{3}
   \]
   并由线性对偶构造一个在邻域源列上平凡、在至少一个需求方向上非平凡的阶
   \(\ell\) 角色，记录
   \(\mathrm{SOURCE\_RANK\_FOURIER\_SEPARATION}\)；
3. 若槽的允许集合因 SNF/CRT/范围为空，先输出 EDGE_OBSTRUCTED；不能把
   空邻域误报成线性秩缺口；
4. 若角色请求本身并非线性独立，先在请求空间取基；pair-energy 边数不等于
   \(|\mathcal R_\ell|\)。

当 \(\rho(U)<|U|\) 且 \(U\) 已由非恒相位 Fourier 证明为独立需求时，这是一条
固定纤维的 SOURCE_RANK_INCONSISTENT/容量不足证书；若只是在跨纤维合并后出现
秩缺口，则必须保留来源标签，并转入 FIBER_REALIZED 或严格递降检查。

## 5. 与顶层核 Fourier 的接线

锚点在差分群内时，anchor-rank dispatch 至少产生一个 \(\ell\)-初等角色方向。
把多个独立顶层角色作为 \(\mathcal R_\ell\)，Rado 条件精确回答它们能否由实际
保持纤维的 q 进源列支付。若通过，得到的独立源列基可送入
type-II-cross-state-source-demand-hall-capacity-bridge；若失败，秩缺口本身就是
该纤维不能支持声称角色数量的严格回执。

这一步还修正一个潜在误用：同一 q 的不同高度层可以增加有限阶 Kneser 活跃容量，
但若它们在 \(V_\ell\) 中是同一向量，不能增加独立角色数。只有不同 q 或不同来源列
在初等商中产生独立向量，才可提高 Rado 秩。

## 研究边界

该桥把顶层 Fourier 的“独立角色需求”与 q 进槽的实际源列秩连接成一个可构造的
线性拟阵证书，严格补上普通 Hall 数量容量遗漏的重复方向问题。它仍不证明
LINEAR_RANK_DEFICIT 一定给出核心素数下降；下一步需要把秩缺口与稳定子商的
composition relay、Type I/F/G 出口或带标签的 source-switch 递降连接起来。

秩缺口到阶 \(\ell\) 对偶角色的具体消元公式、以及该角色的锚点—关系分派，见
[Type II 线性秩缺口的阶 \(\ell\) 对偶分离证书](type-II-linear-rank-deficit-dual-separation-certificate.md)。
