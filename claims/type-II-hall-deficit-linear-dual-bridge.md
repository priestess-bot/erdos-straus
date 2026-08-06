---
kind: claim
claim_id: type-II-hall-deficit-linear-dual-bridge
title: Type II 固定纤维 Hall 缺口到线性对偶分离桥
statement: 在同一固定来源纤维和同一 ell 初等源商中，若已取线性独立的需求方向 U 满足普通 Hall 缺口 |N(U)|<|U|，则邻域源列空间的秩严格小于需求空间，因而可构造一个阶 ell 角色，平凡于所有可用源槽而分离至少一个需求方向。该回执把固定纤维的 HALL_DEFICIT 精化为 HALL_DEFICIT_FOURIER_SEPARATION；跨纤维或未实现来源标签时不适用，必须保留单纤维实现门。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-cross-state-source-demand-hall-capacity-bridge
  - type-II-rado-linear-rank-hall-capacity-bridge
  - type-II-linear-rank-deficit-dual-separation-certificate
topics:
  - type-II
  - Hall
  - rank-deficit
  - dual-separation
  - Fourier
  - fixed-fiber
  - finite-abelian
  - capacity
sources:
  - claim: type-II-cross-state-source-demand-hall-capacity-bridge
    role: ordinary-Hall-deficit
  - claim: type-II-rado-linear-rank-hall-capacity-bridge
    role: independent-demand-linearization
  - claim: type-II-linear-rank-deficit-dual-separation-certificate
    role: finite-character-separation
visibility: public
last_checked: '2026-08-05'
---

# Type II 固定纤维 Hall 缺口到线性对偶分离桥

## 1. 固定纤维的线性化输入

固定一个保持来源标签的参数纤维，以及一个素数 \(\ell\)。令
\[
V_\ell=A_\ell/\ell A_\ell
\]
为该纤维真实源关系列在 \(\ell\)-primary 商中的初等向量空间。设
\[
U=\{r_1,\ldots,r_m\}
\]
是一组已经去除线性依赖的需求，需求方向为
\[
w_{r_i}\in V_\ell,\qquad
D_U=\operatorname{span}\{w_{r_i}:1\le i\le m\},
\qquad
\dim D_U=m.
\]
令 \(N(U)\) 是普通 Hall 兼容图中 U 的合法 q 槽邻域；每个
\(c\in N(U)\) 带有真实源列向量 \(v_c\in V_\ell\)，并设
\[
W_U=\operatorname{span}\{v_c:c\in N(U)\}.
\]

这里的“固定纤维”要求所有 \(w_{r_i}\)、\(v_c\) 都来自同一个参数回译和同一个
source-switch 状态。因 SNF、CRT、范围或 \(B'>A\) 失败而不存在的候选边，先记
EDGE_OBSTRUCTED，不伪造为源槽。

## 2. Hall 缺口的线性对偶定理

若
\[
|N(U)|<|U|=m,
\tag{1}
\]
则
\[
\dim W_U\le |N(U)|<m=\dim D_U.
\tag{2}
\]
因此存在 \(\lambda\in V_\ell^*\) 使
\[
\lambda|_{W_U}=0,\qquad \lambda|_{D_U}\ne0.
\tag{3}
\]
对应角色
\[
\chi_\lambda(x)=
\exp\!\left(\frac{2\pi i}{\ell}
\lambda(x\bmod \ell A_\ell)\right)
\tag{4}
\]
满足
\[
\chi_\lambda(v_c)=1\quad(c\in N(U)),
\qquad
\chi_\lambda(w_{r_0})\ne1
\tag{5}
\]
对某个 \(r_0\in U\) 成立。于是可记录有限证书
\[
\mathrm{HALL\_DEFICIT\_FOURIER\_SEPARATION}
=(\ell,U,N(U),\lambda).
\tag{6}
\]

### 证明

(1) 中邻域至多有 \(|N(U)|\) 个源列，故其张成空间维数不超过
\(|N(U)|\)，得到 (2)。需求已经取成独立方向，所以
\(\dim D_U=m\)。由有限维线性对偶的双正交关系，(2) 蕴含存在一个在
\(W_U\) 上为零、在 \(D_U\) 上不为零的泛函 \(\lambda\)，即 (3)。把
\(\lambda\) 按 (4) 提升为真实阶 \(\ell\) 角色，(5) 随即成立。证毕。

## 3. 与 Rado 和普通 Hall 的关系

Rado rank-Hall 的条件是
\[
\operatorname{rank}(W_U)\ge |U|
\]
对所有请求子集成立。固定纤维中普通 Hall 缺口 (1) 更强地给出
\[
\operatorname{rank}(W_U)
\le |N(U)|
< |U|,
\]
所以一定落入 Rado 的秩缺口分支。普通 Hall 与线性 Hall 的差别在这里不是
两个独立的失败记录：前者可以直接精化为 (6)，而不是只保留请求—槽数量差。

若某个槽向量重复，(2) 仍只按其张成空间计数；若邻域为空，则得到分离角色
平凡于空的源空间，并同时保留造成空邻域的 EDGE_OBSTRUCTED 记录。后者说明
算术边界，前者说明可用源关系在该纤维中无法分离需求，二者不可互相替代。

## 4. 分派和适用边界

对 (6) 的角色按锚点—秩 dispatch 分派：

1. 若规范锚点被 \(\lambda\) 分离，记录环境锚点/F/G 候选；
2. 若锚点不被分离，记录 SOURCE_RELATION_FOURIER 或
   SOURCE_RANK_FOURIER_SEPARATION，并继续检查 F/G 载体、source-switch 或
   annihilator 商的严格势下降；
3. 若需求来自多个 primary 分量，可在固定纤维的直和
   \(V=\bigoplus_\ell V_\ell\) 中先取总需求基；同一证明适用于总维数与邻域源列
   数的比较；
4. 若需求来自不同参数纤维且没有 FIBER_REALIZED 映射，不能把它们强行放进同一
   \(V_\ell\)。此时只能保留 HALL_DEFICIT、UNREALIZED_CROSS_STATE_MATCH
   或各纤维的独立分离证书。

因此该桥闭合的是“固定纤维 Hall 缺口”的线性对偶出口，而不是任意跨状态 Hall
缺口的整数回译。跨纤维的 Kneser surplus 仍必须先通过单纤维实现门。

## 5. 最小例子

在
\[
V=\mathbb F_2^2,\qquad
w_{r_1}=(1,0),\quad w_{r_2}=(0,1)
\]
中，若两个请求都只有同一合法槽 \(c\)，且
\[
v_c=(1,0),
\]
则
\[
|N(U)|=1<2=|U|,
\qquad
W_U=\operatorname{span}(1,0).
\]
取 \(\lambda(x,y)=y\)，便有
\[
\lambda(v_c)=0,\qquad \lambda(w_{r_2})=1.
\]
这同时是普通 Hall 缺口、Rado 秩缺口和
\(\mathrm{HALL\_DEFICIT\_FOURIER\_SEPARATION}\)，而不是两个请求共享一份
q 层的“可接受匹配”。

## 研究边界

该桥把固定纤维内的数量 Hall 缺口严格精化为有限阶对偶角色，减少了
UNRELAYABLE_HALL_DEFICIT 的适用范围。它仍不证明该角色自动产生 Type II 或核心
素数下降；剩余问题是证明锚点/F/G 承接，或把角色的 annihilator 商构造成保持标签、
严格降低势的整数后继。
