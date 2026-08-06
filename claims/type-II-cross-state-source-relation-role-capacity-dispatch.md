---
kind: claim
claim_id: type-II-cross-state-source-relation-role-capacity-dispatch
title: Type II 跨状态相容角色的锚点—初等秩—Hall 容量分派
statement: 对一个已通过共同环境、shared-q 和 SNF 提升门的跨状态 Fourier 角色，先在真实源关系商中取去重源相对支撑 R、目标锚点 alpha 与差分群 Delta=<R>。若角色在 Delta 上平凡且在目标锚点 alpha 上非平凡，则它是纯锚点 Fourier，不产生 q-height 需求，只能进入环境锚点/商 relay 或显式锚点提升障碍；若两者均平凡则删除恒等角色；若角色在 Delta 上非平凡，则某个 ell-primary 分量产生至少一个真实初等秩需求。对一组角色，若需求秩超过保持纤维的合法源列秩，则输出 SOURCE_RANK_INCONSISTENT；否则把独立需求接入 source-switch/SNF/重复-q 已验证的 Hall 图，Hall 缺口给出 HALL_DEFICIT_FOURIER，完整匹配在稳定子容量达到缺口时给出 Type II，否则进入稳定子吸收或商 relay。该分派不把“角色可提升”本身误称为 Type II。
claim_status: conditional
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-cross-state-full-match-realization-fourier-trichotomy
  - type-II-anchor-rank-fourier-dispatch
  - type-II-composition-kernel-role-rank-capacity-bridge
  - type-II-source-fiber-elementary-rank-qheight-injection
  - type-II-cross-state-source-demand-hall-capacity-bridge
  - type-II-hall-deficit-linear-dual-bridge
topics:
- type-II
- cross-state
- Fourier
- source-relation
- anchor
- elementary-rank
- Hall
- capacity
- source-switch
- descent
- proof-program
sources:
  - claim: type-II-cross-state-full-match-realization-fourier-trichotomy
    role: common-environment-role-input
  - claim: type-II-anchor-rank-fourier-dispatch
    role: anchor-relation-bisection
  - claim: type-II-composition-kernel-role-rank-capacity-bridge
    role: primary-demand-lower-bound
  - claim: type-II-source-fiber-elementary-rank-qheight-injection
    role: legal-source-column-rank
  - claim: type-II-cross-state-source-demand-hall-capacity-bridge
    role: typed-Hall-capacity
  - claim: type-II-hall-deficit-linear-dual-bridge
    role: Hall-dual-separation
visibility: public
last_checked: '2026-08-05'
---

# Type II 跨状态相容角色的锚点—初等秩—Hall 容量分派

## 1. 角色的真实源支撑

共同环境三分的 CROSS_STATE_SOURCE_RELATION_FOURIER 回执已经通过阶筛和
有限阿贝尔 SNF；仍需把它放回真实源关系商。去掉稳定子吸收和重复 q 后，设
\[
R\subseteq H,\qquad 1\in R,
\]
是匹配块在源关系商 \(H\) 中的去重相对支撑，目标写成锚点 \(\alpha\in H\)，并令
\[
\Delta=\langle R\rangle\le H.
\tag{1}
\]
对一个相容角色 \(\chi\in\widehat H\)，同时记录关系限制 \(\chi|_\Delta\) 和锚点相位
\(\chi(\alpha)\)；\(\chi(\alpha)\ne1\) 时它分离目标锚点，但即使锚点相位为 1，
关系限制仍可能给出非恒的目标差分方向。若有多条角色，按其在
\(\operatorname{Hom}(\Delta,\mu_\ell)\) 中的线性独立性去重。

这里的 \(R\) 必须来自同一保持来源标签的参数纤维或已证明的 source-switch
后继；共同单位群中的乘积集本身不能替代 \(R\)。否则应返回
\(\mathrm{UNREALIZED\_SOURCE\_COLUMN}\)，而不是建立秩需求。

## 2. 锚点—关系二分

定义角色的关系相位是否恒定：
\[
\mathrm{AnchorOnly}(\chi)
\iff
\chi|_\Delta=1.
\tag{2}
\]

若 (2) 成立且 \(\chi(\alpha)\ne1\)，则 \(\alpha\notin\Delta\)，并且
\[
\widehat{1_{\alpha R}}(\chi)
=\overline{\chi(\alpha)}\,|R|.
\tag{3}
\]
这只是纯锚点 Fourier：\(\chi\) 在所有真实源列上同相，所对应的 q-height/初等
关系需求为零。它的合法出口只有：

1. 若环境商 \(H/\Delta\) 或更小稳定子商仍保留目标相位并有可提升标签，则输出
   ANCHOR_ENVIRONMENT_RELAY，交给有限商递降；
2. 若锚点角色只能在抽象共同群中存在，记录
   ANCHOR_LIFT_OBSTRUCTED 或 TOP_PRIMARY_ANNIHILATOR，不得把式 (3) 的
   幅度当作 \(|R|\) 个容量单位。

若 \(\chi|_\Delta=1\) 且 \(\chi(\alpha)=1\)，则 \(\chi\) 在
\(\langle\Delta,\alpha\rangle\) 上恒等，是无信息的恒等角色，应从非平凡角色清单中
删除，不产生任何需求。

反之，若 \(\chi|_\Delta\ne1\)，取 \(\chi|_\Delta\) 的一个非平凡
\(\ell\)-primary 分量并降到阶 \(\ell\)，得到
\[
\dim_{\mathbb F_\ell}(\Delta/\ell\Delta)\ge1.
\tag{4}
\]
因此至少有一个真实 \(\ell\)-初等源关系需求
\(\mathrm{SOURCE\_RANK\_DEMAND}(\ell,1)\)。一组角色的需求数记为
\[
d_\ell=\dim_{\mathbb F_\ell}
\langle\chi|_\Delta:\chi\text{ 为当前角色族}\rangle.
\tag{5}
\]
只有独立限制才计入 \(d_\ell\)；同一角色的 Fourier pair-energy 或同一 q 的重复
来源不增加 \(d_\ell\)。

## 3. 源列秩门

设 \(W_\ell\) 是当前保持参数纤维的合法 source-relation 列在其
\(\ell\)-primary 商中的张成空间，并把目标差分群通过源列注入视为
\(W_\ell\) 的子空间。合法列必须同时满足真实 q 整除、来源标签、
source-switch/CRT、SNF 和 \(B'>A\) 范围条件；稳定子中的列和重复 q 账本已先
合并。令
\[
c_\ell=\dim_{\mathbb F_\ell}W_\ell.
\tag{6}
\]

源列注入给出必要不等式
\[
\boxed{d_\ell\le c_\ell.}
\tag{7}
\]
若实际回执出现 \(d_\ell>c_\ell\)，则得到
\(\mathrm{SOURCE\_RANK\_INCONSISTENT}\)：角色的关系相位与当前来源纤维不相容，
不能把缺少的方向记为“尚待匹配”的容量。若 \(d_\ell\le c_\ell\)，只说明存在
足够的线性源方向，尚未说明这些列在 q-height 层和整数参数上可同时实现。

## 4. Hall 与稳定子容量分派

将 \(d_\ell\) 个独立请求（以及其它已证明的 primary/数字层请求）接入合法边图：
请求到源槽的边必须保留同一参数纤维、真实 q 层和来源标签。对任意请求子集 \(U\)
记 \(N(U)\) 为其合法资源邻域。

* 若 \(|N(U)|<|U|\)，输出规范的
  \(\mathrm{HALL\_DEFICIT\_FOURIER}=(U,N(U))\)。在同一初等商的线性模型中，
  该缺口再由对偶角色给出 HALL_DEFICIT_FOURIER_SEPARATION；跨纤维缺边则保留
  UNREALIZED_SOURCE_COLUMN 或算术障碍。
* 若所有 \(U\) 满足 \(|N(U)|\ge|U|\)，取一个完整匹配，并令 \(T\) 为匹配后源
  积集在 \(H\) 中的稳定子。匹配后的 q-height 只有在稳定子商中累计活跃容量达到
  \[
\sum_i\kappa_i\ge |H/T|-1
\tag{8}
\]
  时才强制 \(-1\) 命中并回译为 Type II；若未达到 (8)，交给稳定子增长—吸收
  或商 relay，不能以 FULL_MATCH 结束。
* 若某条边的 SNF/CRT/范围条件失败，则记录 EDGE_OBSTRUCTED；该边既不计入
  \(N(U)\)，也不产生 SOURCE_RANK_INCONSISTENT。

这三项与纯锚点分支互斥：式 (3) 不进入 Hall q-height 账本，式 (4)--(8) 只对
关系相位非恒的角色生效。对固定 q 的请求子集，在上述 Rado/Hall 之前还应先应用
逐层移位上界；若
\(\sum_{j\le E_U}C_j(S_U,q)<|U|\)，直接记录
Q_ADIC_LAYER_CAPACITY_DEFICIT。完整切割见
[Type II 跨状态分层 Rado—q 进容量切割](type-II-cross-state-layered-rado-qcapacity-cut.md)。

## 5. 证明

若 \(\chi|_\Delta=1\)，生成性给出 \(\chi(r)=1\) 对所有 \(r\in R\)，目标非平凡
相位只能来自 \(\alpha\)，于是得到 (3)，且 \(\alpha\notin\Delta\)；这正是环境
锚点分支，不能制造关系列。

若 \(\chi|_\Delta\ne1\)，有限阿贝尔群的 primary 分解保证存在素数 \(\ell\) 使其
\(\ell\)-分量在 \(\Delta\) 上非平凡；取适当幂得到阶 \(\ell\) 角色，故 (4) 成立。
对角色族取独立限制得到 (5)。固定纤维源列注入定理把目标差分群嵌入
\(W_\ell\)，从而得到 (7)；不等时只能是来源相容性失败。等式成立后，有限 Hall
定理给出“完整匹配/严格缺口”二分；完整匹配再由 Kneser 稳定子容量判据给出
(8) 的 Type II 门，未达阈值时由稳定子吸收或商 relay 接续。证毕。

## 6. 边界例子

### \(p=97\) 的纯锚点回执

在 \(G=U(24)\) 中取单纤维源支撑 \(R=\{1\}\)、锚点
\(\alpha=13\)。则 \(\Delta=1\)，角色可在 \(\Delta\) 上平凡且在 \(\alpha\) 上非平凡，
式 (3) 的幅度为 \(1\)，但 \(d_\ell=0\)；这不是一个 q-height 请求，也不能与另一
纤维的 \(13\) 列合并。

### \(C_5\) 的关系需求

取 \(H=C_5=\langle g\rangle\)、\(R=\{1,g\}\)、\(\alpha=g^2\)。目标陪集
\(\alpha R=\{g^2,g^3\}\) 不含单位元，而 \(\Delta=H\)。角色
\(\chi(g)=e^{2\pi i/5}\) 在 \(R\) 上非恒相位，故
\(d_5=1\)。若合法源列空间 \(W_5\) 为零，输出
\(\mathrm{SOURCE\_RANK\_INCONSISTENT}\)；若有一个合法 q 槽，则进入 Hall 匹配，
但仍须满足 (8) 才能得 Type II。

## 研究边界

该引理把共同环境中“可提升 Fourier 角色”进一步分成不收费的纯锚点角色和至少
一个真实 primary 源需求，并把后者接到秩、Hall 和稳定子容量三重门。它没有声称
每个 SOURCE_RANK_DEMAND 都能达到 (8)，也没有把 Hall 缺口自动变成严格素数下降；
全局剩余仍是为每个缺口提供已证明的 LOWER_RELAY、算术障碍或闭合 F/G 终端。
