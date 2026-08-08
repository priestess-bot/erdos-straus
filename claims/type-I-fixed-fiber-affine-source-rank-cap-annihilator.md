---
kind: claim
claim_id: type-I-fixed-fiber-affine-source-rank-cap-annihilator
title: 固定纤维仿射 source-map 的 q 秩上限与 annihilator relay
statement: 设固定 overflow 纤维 (p,A,d) 的所有实际 carrier 满足 M=M_0 (mod Ap)。若一个完整 source-map 的源列在 F_q 向量空间 V 中具有仿射形式 v(M)=v_0+w*(alpha M+beta mod q)，且 q^j|Ap，则该纤维全部源列至多张成一维空间。因而任何维数至少 2 的独立需求 D 都产生显式 Rado 对偶 lambda，湮灭所有实际源列并分离某个需求方向；若 source-map 完备、目标方向被 lambda 分离且 annihilator 核/整数提升门通过，则进入严格有限商 relay，否则分别输出 SOURCE_MAP_UNCLOSED、关系 Fourier 或精确 lift obstruction。该结论把固定纤维相位碰撞首次接到 source-rank/annihilator 分派，但不声称任意 Fourier 标签都是这种仿射载体标签。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fixed-fiber-affine-qprimary-phase-collapse
  - type-I-linear-block-escape-hall-annihilator-closure
  - type-II-hall-deficit-linear-dual-bridge
  - type-II-hall-source-column-closure-relay
topics:
  - type-I
  - overflow
  - fixed-fiber
  - affine-source-map
  - q-adic
  - rank-capacity
  - Rado
  - annihilator
  - quotient-descent
  - proof-boundary
sources:
  - claim: type-I-fixed-fiber-affine-qprimary-phase-collapse
    role: fixed-fiber-phase-collapse
  - claim: type-II-hall-deficit-linear-dual-bridge
    role: Hall-to-dual-character
  - claim: type-II-hall-source-column-closure-relay
    role: annihilator-relay
visibility: public
last_checked: '2026-08-09'
---

# 固定纤维仿射 source-map 的 (q) 秩上限与 annihilator relay

## 1. 算术输入

固定 (p)、(0<d<p)、(A>0)，并考虑实际 overflow 行

\[
A\mid M,
\qquad
pn=4dM+1.
\tag{1}
\]

上一引理给出：在同一个固定 \((p,A,d)\) 纤维中，所有 carrier 满足

\[
M\equiv M_0\pmod{Ap}
\tag{2}
\]

某个唯一的 (M_0)。取奇素数 (q)、层 (j\ge1)，满足

\[
q^j\mid Ap.
\tag{3}
\]

因此 (M\bmod q) 在整个纤维上恒定。

## 2. 仿射 source-map 的秩上限

设当前固定纤维的真实源列落在一个 (mathbb F_q) 向量空间 (V)，并且 source-map
已经声明为以下仿射载体形式：

\[
v(M)=v_0+w\,\overline{(\alpha M+\beta)}
\in V,
\qquad
\overline{(\alpha M+\beta)}\in\mathbb F_q.
\tag{4}
\]

这里 \(v_0,w\in V\) 与纤维固定，\(\alpha,\beta\in\mathbb Z\) 也固定；所有
实际 source 行都必须由 (4) 生成。这是一个明确的 source-map 假设，不是从 Fourier
角色阶自动推导的。

由 (2)--(3)，对任意同纤维 (M,M') 有

\[
\alpha M+\beta\equiv\alpha M'+\beta\pmod q.
\]

所以所有实际源列都相同：

\[
\boxed{v(M)=v(M')=:v_* .}
\tag{5}
\]

特别地，实际源列张成空间满足

\[
\boxed{\dim_{\mathbb F_q}\operatorname{span}\{v(M):M\in W\}\le1.}
\tag{6}
\]

这比只说相位槽数为一更强：在 source-map 真正由该标量仿射载体控制时，连源列的
初等秩也不能随着固定纤维行数增长。

### 证明

由 (2)，(M-M'=Ap\,t)。条件 (3) 特别蕴含 (q\mid Ap)，故

\[
\alpha M+\beta-(\alpha M'+\beta)=\alpha Ap\,t\equiv0\pmod q.
\]

代入 (4) 得 (5)，而单个向量的张成空间维数至多一，得到 (6)。证毕。

## 3. 独立需求的 Rado 对偶

令 (D\le V) 是已经由固定层 Fourier、目标纤维或 source relation 证明为独立的
需求空间，且

\[
\dim_{\mathbb F_q}D=r\ge2.
\tag{7}
\]

由 (6)，实际源列空间 (W_*:=\operatorname{span}\{v(M)\}) 的维数至多一，所以

\[
\dim W_*<\dim D.
\tag{8}
\]

有限维对偶性给出一个显式的泛函

\[
\boxed{
\lambda\in V^*,
\qquad
\lambda(W_*)=0,
\qquad
\lambda|_D\ne0 .
}
\tag{9}
\]

用阶 (q) 角色

\[
\chi_\lambda(x)=
\exp\!\left(\frac{2\pi i}{q}\lambda(x)\right)
\tag{10}
\]

记录后，得到

\[
\mathrm{FIXED\_FIBER\_AFFINE\_RANK\_DEFICIT}
=(q,j,D,W_*,\lambda).
\tag{11}
\]

式 (11) 不是单纯的 `FIXED_FIBER_PHASE_COLLISION`：它还提供一个分离需求方向的
有限对偶角色。

### 证明

若 (W_*=0)，任取在 (D) 上非零的泛函即可。若 (dim W_*=1)，因为
(dim D\ge2)，(D\not\subseteq W_*)，选取 (d_0\in D\setminus W_*)；将
(W_*+\langle d_0\rangle) 上的泛函取为在 (W_*) 上为零、在 (d_0) 上为一，
再延拓到 (V)，即得 (9)。角色 (10) 是其有限阶实现。证毕。

## 4. 选择器的四分

对 (11) 必须按 source-map 完备性和目标相位分派：

1. **SOURCE_MAP_UNCLOSED**：若 (4) 只覆盖已知行，未证明固定纤维的实际 source
   table 穷尽，则 (9) 不能湮灭未知源列；不能直接调用 annihilator relay。
2. **AFFINE_RANK_DEFICIT_RELATION**：若 source-map 完备但目标方向
   \(\tau\) 满足 \(\lambda(\tau)=0\)，角色只给出源关系 Fourier；它不产生目标
   容量，也不应重复收费同一 q 层。
3. **AFFINE_GLOBAL_ANNIHILATOR**：若 source-map 完备且
   \(\lambda(\tau)\ne0\)，则全部源列落入
   \(K=\ker\chi_\lambda\)，目标在 (K) 外。若 (K\ne1)，投影到 (H/K) 保持
   目标缺失，得到严格有限商 relay；若 (K=1)，这是顶层 primary 终端候选。
4. **AFFINE_LIFT_OBSTRUCTED**：若上述角色分离成立但整数 source-switch、SNF、
   范围或 E1--E5 提升门失败，保存最小失败行。抽象有限商仍是严格群论 relay，
   但不能登记为 Erdős--Straus 的整数递归边。

前三项互斥于 source-map 是否闭合和目标相位；第四项是第三项之后的整数提升结果。
这正是现有 Hall—annihilator 桥的一个可由固定纤维 CRT 自动触发的特殊入口。

## 5. 最小算术—线性控制

取

\[
(p,d,A)=(73,1,27),
\qquad
M\in\{675,2646,10530\}.
\]

这些 carrier 分别对应 (n=37,145,577)，且同余类为

\[
M\equiv675\pmod{Ap=1971},
\qquad
M\equiv0\pmod3.
\]

令 (V=\mathbb F_3^2)，并指定一个完整的仿射 source-map

\[
v(M)=
\bigl(1,\ M+1\bmod3\bigr)=(1,1).
\tag{12}
\]

令独立需求 (D=V)，取

\[
\lambda(x,y)=x-y.
\]

则

\[
\lambda(1,1)=0,
\qquad
\lambda(1,0)=1,
\qquad
\dim W_*=1<2=\dim D.
\]

若将目标方向取为 \(\tau=(1,0)\)，则 (lambda(\tau)=1)。在抽象群
(H=\mathbb F_3^2) 中，

\[
K=\ker\lambda=\{(x,x):x\in\mathbb F_3\},
\qquad
H/K\simeq C_3,
\]

所以这是一个严格的非平凡有限商 relay 控制。它只验证“完整仿射 source-map
\(\Rightarrow\) 秩缺口 \(\Rightarrow\) annihilator 商”的链条，不声称该抽象商已经
通过整数 E1--E5。

## 6. 研究边界

本引理完成了一个此前缺失的正向接口：固定纤维的 CRT 不仅合并物理相位，还在
**仿射 source-map 完备**时给出源列初等秩上限，并自动触发 Rado 对偶和有限 annihilator
relay。它仍不能解决全局存在性，因为还需要证明实际 F/G source-map 确实具有 (4) 的
完备性，或把非仿射/跨纤维列加入有限菜单。

因此下一决定性任务不是继续增加同纤维的重复行，而是：对每个线性 block escape，
证明 alternate-source 菜单要么被 (4) 覆盖并完成 E1--E5，要么出现可复核的非仿射/跨纤维
source 列，从而进入现有 Hall 扩张—annihilator 三分。
