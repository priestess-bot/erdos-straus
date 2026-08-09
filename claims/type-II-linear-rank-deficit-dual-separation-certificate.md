---
kind: claim
claim_id: type-II-linear-rank-deficit-dual-separation-certificate
title: Type II 线性秩缺口的阶 ell 对偶分离证书
statement: 设固定源纤维的 ell 初等向量空间 V 中，目标 Fourier/关系需求方向张成 D，可用 Hall 邻域源槽向量张成 W。若 W 严格小于 D，则存在线性泛函 lambda 在 W 上为零而在 D 上非零；它提升为一个阶 ell 的真实有限群角色，平凡于所有可用源槽而分离至少一个未支付目标方向。该角色给出 SOURCE_RANK_FOURIER_SEPARATION 证书；若锚点也被分离则升级为环境锚点证书，否则进入关系 Fourier/容量分支。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-rado-linear-rank-hall-capacity-bridge
  - type-II-anchor-rank-fourier-dispatch
  - type-II-composition-kernel-role-rank-capacity-bridge
  - type-II-kernel-fourier-source-relation-compatibility
topics:
  - type-II
  - rank-deficit
  - dual-separation
  - Fourier
  - finite-abelian
  - source-relation
  - capacity
  - certificate
sources:
  - claim: type-II-rado-linear-rank-hall-capacity-bridge
    role: rank-deficient-neighborhood
  - claim: type-II-anchor-rank-fourier-dispatch
    role: anchor-versus-relation-branch
  - claim: type-II-composition-kernel-role-rank-capacity-bridge
    role: role-to-elementary-direction
  - claim: type-II-kernel-fourier-source-relation-compatibility
    role: finite-character-lift
visibility: public
last_checked: '2026-08-05'
---

# Type II 线性秩缺口的阶 \(\ell\) 对偶分离证书

## 1. 需求与源槽的两个子空间

固定参数纤维和素数 \(\ell\)，令
\[
V= A_\ell/\ell A_\ell
\]
是实际保持纤维源列的 \(\ell\)-初等商。对一个已经证明线性独立的角色请求子集
\(U\)，把其对应的目标方向写成
\[
w_r\in V,\qquad r\in U,
\]
并令
\[
D_U=\operatorname{span}_{\mathbb F_\ell}\{w_r:r\in U\}.
\]

这里 \(w_r\in V\) 是本卡的显式输入前提，不由
\(\chi_r\in\operatorname{Hom}(\Delta,\mu_\ell)\) 自动产生。调用者必须给出同一
source-SNF table 上的 common-space transport，或改用角色--源关系求值配对
\(\kappa(c)\in R^*\)。缺少两者时应输出
ROLE_TO_COLUMN_EVALUATION_UNPROVED，不能执行以下 \(D_U\) 与 \(W_U\) 的比较。

Hall 邻域 \(N(U)\) 中的每个合法 q 槽 \(c\) 带源列向量 \(v_c\in V\)，定义
\[
W_U=\operatorname{span}_{\mathbb F_\ell}\{v_c:c\in N(U)\}.
\]
Rado 线性 rank-Hall 失败意味着
\[
\dim W_U<|U|=\dim D_U.
\tag{1}
\]
这里最后一个等号要求 \(U\) 已经去除角色线性依赖；若角色不独立，应先取基。

## 2. 线性对偶分离定理

在 (1) 下，存在
\[
\lambda\in V^\*=\operatorname{Hom}_{\mathbb F_\ell}(V,\mathbb F_\ell)
\]
满足
\[
\lambda|_{W_U}=0,
\qquad
\lambda|_{D_U}\ne0.
\tag{2}
\]
因此存在某个 \(r_0\in U\) 使 \(\lambda(w_{r_0})\ne0\)。

### 证明

若所有 annihilate \(W_U\) 的泛函也 annihilate \(D_U\)，则有限维线性对偶的双正交
关系给出 \(D_U\subseteq W_U\)，与
\(\dim D_U>\dim W_U\) 矛盾。因此可取 \(\lambda\) 满足 (2)；再由
\(\lambda|_{D_U}\ne0\) 选取 \(r_0\)。在给定源列基下，\(\lambda\) 由一次高斯消元
直接构造。证毕。

## 3. 提升为真实阶 ell 角色

把 \(\lambda\) 视为 \(A_\ell\) 上的阶 \(\ell\) 角色
\[
\chi_\lambda(x)
=\exp\!\left(\frac{2\pi i}{\ell}\,
\lambda(x\bmod\ell A_\ell)\right).
\tag{3}
\]
则对所有可用邻域槽 \(c\in N(U)\)，
\[
\chi_\lambda(v_c)=1,
\]
而
\[
\chi_\lambda(w_{r_0})\ne1.
\tag{4}
\]
所以任何只使用 \(N(U)\) 中源槽的组合都保持单位相位，但目标需求方向
\(w_{r_0}\) 被分离。四元组
\[
\mathrm{SOURCE\_RANK\_FOURIER\_SEPARATION}
=(\ell,U,N(U),\lambda)
\tag{5}
\]
是一个有限、可复核的对偶证书；它不依赖把同一向量的重复槽当作独立容量。

## 4. 锚点与关系分派

若规范锚点 \(\alpha\) 的 \(\ell\)-初等坐标满足
\[
\lambda(\alpha\bmod\ell A_\ell)\ne0,
\]
则 \(\chi_\lambda\) 同时分离锚点，回执升级为
ANCHOR_SEPARATING_CHARACTER（若低商核和源关系相容则可成为 F/G 环境证书）。

若
\[
\lambda(\alpha\bmod\ell A_\ell)=0,
\]
则它是纯关系分离角色：锚点相位未被收费，但某个目标关系方向仍被源槽邻域
排除。该角色只能进入 SOURCE_RELATION_FOURIER、线性 rank 缺口或新的
q-height/递降分析，不能伪装成 Type II 命中。

若 \(\lambda\) 来自参数 CRT 或外部加法标签，仍须通过源关系格的仿射相容性；
(5) 是真实源列给出的角色时自动相容，外部候选失败则记录 LIFT_OBSTRUCTED。

## 5. 最小严格反例

取
\[
V=\mathbb F_2^2,\qquad
w_{r_1}=(1,0),\quad w_{r_2}=(0,1),
\]
而两个邻域槽都带同一向量
\[
v_{c_1}=v_{c_2}=(1,0).
\]
普通 Hall 数量条件有两个槽可匹配两个请求，但
\[
D_U=V,\qquad W_U=\operatorname{span}(1,0),
\]
故取 \(\lambda(x,y)=y\) 得
\[
\lambda(v_{c_1})=\lambda(v_{c_2})=0,\qquad
\lambda(w_{r_2})=1.
\]
这是一张显式的阶 2 SOURCE_RANK_FOURIER_SEPARATION，证明普通数量匹配
不能支付第二个独立角色。

## 6. 对统一选择器的作用

Rado 条件通过时，源槽可以支付独立角色，继续进入 q-height/Kneser 容量；Rado
条件失败时，在上述 common-space transport 前提下，(5) 把容量缺口转成阶
\(\ell\) 的对偶角色。于是跨状态 dispatch 不再
只有“FULL_MATCH/HALL_DEFICIT”两种粗粒度结果，而是：
\[
\text{线性独立容量匹配}
\quad\text{或}\quad
\text{SOURCE\_RANK\_FOURIER\_SEPARATION}.
\]
后者若能被固定层商或 F/G 载体承接，就成为规范 Fourier 证书；若不能承接，则
保留精确的关系格/提升障碍，转交良基递降，而不重复收费。

## 研究边界

该引理完成了 Rado 秩缺口到有限阶对偶角色的构造性转换，严格增强了普通 Hall
缺口回执。它仍不证明每个 SOURCE_RANK_FOURIER_SEPARATION 都自动产生核心素数
下降；下一步需要证明该角色在固定层商中有 F/G 载体，或把其 annihilator 商作为
严格变小的 source-fiber/参数状态。

当请求角色相关但物理义务不同，或角色空间与 source-column 空间没有预先识别时，
应使用[相关角色求值配对与广义 Rado 选择器](type-I-fg-dependent-role-evaluation-rado-tensor-selector.md)
中的不可见角色空间 \(Z_U\)，而不是虚构 \(w_r\in V\)。
