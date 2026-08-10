---
kind: claim
claim_id: type-I-fg-marked-source-menu-saturation
title: F/G 有限带标记 source 菜单的饱和与相位实现判据
statement: 对一个已经由独立算术命题证明穷尽、且满足 V(Gamma(A))=0 的有限同纤维 source table A，候选菜单 M 的 source 完备性不必保留为口头前提：把每条带标记行 (u,lambda) 放入 H x Z/eZ 后，M 与 A 施加完全相同的复角色约束当且仅当其生成的带标记子群相等。菜单与目标相位共同可由某个复角色实现当且仅当该联合子群没有非零纯标记元。若要求全局 mu_(q^a)-值且阶恰为 q^a 的角色，还必须通过额外的有限 SNF 同余和 exact-order 门；一般复角色的延拓不能替代该门。菜单不饱和时，SNF 给出一个实际遗漏 source 行的群方向逃逸或标记关系矛盾，而不是笼统的 F_SOURCE_MAP_UNCLOSED。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on: []
topics:
  - type-I
  - F-state
  - G-state
  - source-map
  - source-completeness
  - Fourier
  - phase-lift
  - finite-abelian
  - SNF
  - q-primary
  - proof-program
sources:
  - claim: type-II-raw-finite-abelian-source-lift-snf
    role: finite-abelian-labelled-character-SNF
visibility: public
last_checked: '2026-08-10'
---

# F/G 有限带标记 source 菜单的饱和与相位实现判据

## 1. 范围

固定有限阿贝尔群 \(H\)、标签根群

\[
E=\mathbb Z/e\mathbb Z,
\]

以及一个已经由独立算术命题证明穷尽的、同参数纤维的真实 source table

\[
\mathcal A\subseteq H\oplus E.
\tag{1}
\]

一行 \((u,\lambda)\) 表示该实际 source 的群像为 \(u\)，当前相位要求为

\[
\chi(u)=\zeta_e^\lambda.
\tag{2}
\]

令 \(\mathcal M\subseteq\mathcal A\) 是当前菜单，\(\mathcal T\subseteq H\oplus E\)
是有限目标锚点/目标纤维相位表。这里的“穷尽”只能来自例如线性两块或已声明
universe 的 canonical \(D\)-格菜单；没有这种外部 source-completeness 定理时，本卡
不能删除 'F_SOURCE_MAP_UNCLOSED'。

对任意行集 \(\mathcal B\)，定义

\[
\Gamma(\mathcal B)=\langle(u,\lambda):(u,\lambda)\in\mathcal B\rangle
\le H\oplus E,
\qquad
V(X)=X\cap(\{0\}\oplus E).
\tag{3}
\]

再记

\[
\mathcal X(\mathcal B)=
\{\chi\in\widehat H:
\chi(u)=\zeta_e^\lambda\text{ for every }(u,\lambda)\in\mathcal B\},
\tag{4}
\]

其中 \(\widehat H=\operatorname{Hom}(H,\mathbb C^\times)\) 是全部复角色群。第 5 节
单独处理固定 \(q\)-primary 阶；式 (4) 不预先要求角色在整个 \(H\) 上取值于
\(\mu_e\)。

## 2. 带标记饱和定理

假设完整 source table 本身相位相容：

\[
V(\Gamma(\mathcal A))=0.
\tag{5}
\]

则

\[
\boxed{
\Gamma(\mathcal M)=\Gamma(\mathcal A)
\quad\Longleftrightarrow\quad
\mathcal X(\mathcal M)=\mathcal X(\mathcal A).
}
\tag{6}
\]

左式定义当前菜单对完整实际 source table 的带标记饱和。它同时排除两种遗漏：

\[
\begin{array}{c|c}
\text{遗漏类型}&\text{最小回执}\\ \hline
u\notin\langle\pi_H\Gamma(\mathcal M)\rangle
&\mathrm{MARKED\_SOURCE\_MENU\_GROUP\_ESCAPE}\\
u\in\langle\pi_H\Gamma(\mathcal M)\rangle\text{ 但标签不相容}
&\mathrm{MARKED\_SOURCE\_MENU\_LABEL\_RELATION\_OBSTRUCTED}.
\end{array}
\tag{7}
\]

### 证明

若左式成立，任何 \(\mathcal A\) 行都是 \(\mathcal M\) 行的整数线性组合。将 (2)
相乘后，满足 \(\mathcal M\) 的角色自动满足 \(\mathcal A\)，反向包含由
\(\mathcal M\subseteq\mathcal A\) 给出。

反过来，取一条
\((u,\lambda)\in\mathcal A\setminus\Gamma(\mathcal M)\)。由 (5)，
\(V(\Gamma(\mathcal M))=0\)，所以

\[
\Gamma(\mathcal M)\longrightarrow
L_{\mathcal M}:=\pi_H\Gamma(\mathcal M)
\tag{8}
\]

单射，并且它是唯一标签同态
\(\theta_{\mathcal M}:L_{\mathcal M}\to E\) 的图像。把
\(\zeta_e^{\theta_{\mathcal M}}\) 延拓为 \(H\) 的复角色，得到
\(\chi_0\in\mathcal X(\mathcal M)\)。

若 \(u\notin L_{\mathcal M}\)，有限商 \(H/L_{\mathcal M}\) 有一个在 \(u\) 上非平凡的
角色 \(\psi\)。\(\chi_0\) 与 \(\chi_0\psi\) 都满足菜单，且至少一个违反遗漏行。
若 \(u\in L_{\mathcal M}\)，遗漏行不属于图像恰表示
\(\lambda\ne\theta_{\mathcal M}(u)\)，所以每个菜单角色都违反该行。两种情形均给出
\(\mathcal X(\mathcal M)\ne\mathcal X(\mathcal A)\)。证毕。

延拓只针对复角色；它不宣称延拓仍有固定的 \(q\)-primary 阶。这里使用
\(\mathbb C^\times\) 的可除性，等价地，限制映射
\(\widehat H\to\widehat{L_{\mathcal M}}\) 对有限阿贝尔子群 \(L_{\mathcal M}\) 满射。

## 3. 目标相位的无竖直元判据

在 (6) 的饱和已经通过后，

\[
\boxed{
\mathcal X(\mathcal A\cup\mathcal T)\ne\varnothing
\quad\Longleftrightarrow\quad
V\bigl(\Gamma(\mathcal M)+\Gamma(\mathcal T)\bigr)=0.
}
\tag{9}
\]

无竖直元表示投影到 \(H\) 后的每个群元素只有一个强制标签，从而定义同态

\[
\theta:\pi_H\bigl(\Gamma(\mathcal M)+\Gamma(\mathcal T)\bigr)\to E.
\tag{10}
\]

将其复角色值延拓到 \(H\) 得到正向；反向中，任何纯标签关系都必须被同一个角色
取到单位值。由 (6) 可将 \(\mathcal M\) 换回完整 \(\mathcal A\)。因此输出

\[
\begin{array}{c|c}
V\bigl(\Gamma(\mathcal M)+\Gamma(\mathcal T)\bigr)=0
&\mathrm{MARKED\_SOURCE\_TARGET\_PHASE\_REALIZED}\\
V\bigl(\Gamma(\mathcal M)+\Gamma(\mathcal T)\bigr)\ne0
&\mathrm{MARKED\_TARGET\_PHASE\_RELATION\_OBSTRUCTED}.
\end{array}
\tag{11}
\]

后一行只是 source--target 相位关系矛盾；它不是 Type II \(q\)-height，也不是已经
可提升的整数递降。

## 4. 有限 SNF 构造

写

\[
H\simeq\mathbb Z^d/D\mathbb Z^d,
\qquad D=\operatorname{diag}(m_1,\ldots,m_d).
\tag{12}
\]

令 \(U_{\mathcal M}\) 的列是菜单群坐标，\(\ell_{\mathcal M}\) 是对应标签行。
带标记行 \((u,\lambda)\) 属于 \(\Gamma(\mathcal M)\)，当且仅当

\[
\begin{pmatrix}
U_{\mathcal M}&-D&0\\
\ell_{\mathcal M}&0&-e
\end{pmatrix}
\begin{pmatrix}c\\z\\t\end{pmatrix}
=
\begin{pmatrix}\widetilde u\\\lambda\end{pmatrix}
\tag{13}
\]

有整数解。对 (13) 做一次 Smith 正规形，即可逐行检查完整 table 的 source
是否已由菜单蕴含；失败行就是 (7) 的构造性证书。

令 \(T\) 的列为目标群坐标、\(\tau\) 为目标标签行，取

\[
R=[\,U_{\mathcal M}\ \ T\ \ -D\,].
\tag{14}
\]

若 \(N\) 是 \(\ker_{\mathbb Z}R\) 的一个整数 SNF 基，则

\[
V\bigl(\Gamma(\mathcal M)+\Gamma(\mathcal T)\bigr)=0
\quad\Longleftrightarrow\quad
(\ell_{\mathcal M},\tau,0)N\equiv0\pmod e.
\tag{15}
\]

失败列 \(N_j=(c,\beta,z)\) 给出

\[
U_{\mathcal M}c+T\beta-Dz=0,
\qquad
\ell_{\mathcal M}c+\tau\beta\not\equiv0\pmod e,
\tag{16}
\]

即 (11) 的显式关系证书。

## 5. 固定 \(q\)-primary 阶的额外门

令 \(e=q^a\)。式 (9) 只构造某个复角色，不能自动保留全局
\(\mu_e\)-值性，更不能保证阶恰为 \(q^a\)。若分派需要一个新的全局
\(q\)-primary 角色，必须单独求解

\[
m_\nu y_\nu\equiv0\pmod e,
\qquad
\sum_\nu c_{j\nu}y_\nu\equiv\lambda_j\pmod e
\tag{17}
\]

对所有菜单和目标行 \(j\)。这里 \(y_\nu\) 是第 \(\nu\) 个 invariant-factor
生成元的 \(\mu_e\) 指数，\(c_{j\nu}\) 是该行的 \(H\) 坐标。要求角色阶恰为
\(q^a\) 时，还必须有

\[
\min_\nu v_q(y_\nu)=0.
\tag{18}
\]

否则输出 \(\mathrm{MARKED\_QPRIMARY\_ORDER\_OBSTRUCTED}\)，不能把 (9) 的复角色
延拓误登记为当前 F/G 的固定阶角色。若规范 \(\chi_q\) 已预先给定，则无需重建它：
逐行核对 \(\chi_q\) 在完整 table 和目标表上的标签即可。

式 (17) 的成功解还给出后续 elementary selector 所需的全部数据。把
\(y_\nu\) 模 \(q\)，并只保留 \(q\mid m_\nu\) 的 invariant-factor 坐标，
即得到 \(H/qH\) 上的初等角色。对 source span \(S\)，其真实可见空间是

\[
V_q=(S+qH)/qH\simeq S/(S\cap qH),
\]

而不是 \(S/qS\)。若只给定局部 \(S\to\mathbb F_q\) 标签而未运行 (17)，
它能延拓到 ambient \(H\) 当且仅当湮灭 \(S\cap qH\)。通过后，closed table
的标签矩阵模 \(q\) 就是规范 role-evaluation matrix；见
[F/G source-SNF 的规范初等角色求值商](type-I-fg-snf-canonical-role-evaluation-quotient.md)。

## 6. 选择器分派

对已经有 source-completeness 定理的 universe，先执行

\[
\begin{array}{rcl}
\Gamma(\mathcal M)\ne\Gamma(\mathcal A)
&\Rightarrow&\mathrm{MARKED\_SOURCE\_MENU\_ESCAPE}
\ \text{（即 (7) 的两种细回执之一）};\\
\Gamma(\mathcal M)=\Gamma(\mathcal A),\ V\ne0
&\Rightarrow&\mathrm{MARKED\_TARGET\_PHASE\_RELATION\_OBSTRUCTED};\\
\Gamma(\mathcal M)=\Gamma(\mathcal A),\ V=0,\ \text{且 (17)--(18) 通过}
&\Rightarrow&\mathrm{F\_FOURIER\_SOURCE\_TARGET\_LIFTED}.
\end{array}
\tag{19}
\]

只有第三行可进入已有单 \(q\) source-fiber、Hall/Kneser、CRT 和 E1--E5 分派。
相同 \(\Gamma\) 的物理 source 行仍可能有不同 multiplicity 或 \(q\)-height；本卡不把
带标记群饱和冒充 Hall 容量或 'FIBER_REALIZED'。

## 7. 小例子与边界

取 \(H=C_6=\langle g\rangle\)、\(e=3\)，

\[
\mathcal A=\{(2g,2),(4g,1)\},
\qquad
\mathcal M=\{(2g,2)\},
\qquad
\mathcal T=\{(g,1)\}.
\tag{20}
\]

因为 \(2(2g,2)=(4g,1)\)，有 \(\Gamma(\mathcal M)=\Gamma(\mathcal A)\)。任一关系
\(2c+n\equiv0\pmod6\) 也有 \(2c+n\equiv0\pmod3\)，故 (9) 通过，
\(\chi(g)=\zeta_3\) 实现所有行。

若完整 table 另含 \((g,1)\)，则该行不在 \(\Gamma(\mathcal M)\)。角色
\(\psi(g)=-1\) 在菜单生成子群上平凡，因而 \(\chi\) 与 \(\chi\psi\) 至少一者违反
遗漏行，给出 'MARKED_SOURCE_MENU_GROUP_ESCAPE'。

最后取 \(H=C_4=\langle g\rangle\)、\(E=C_2\)，并要求
\(\theta(2g)=1\pmod2\)，亦即 \(\zeta_2^{\theta(2g)}=-1\)。其带标记图没有纯标签元，且复角色 \(\chi(g)=i\) 可实现它；
但没有全局 \(\mu_2\)-值角色实现它，因为每个 \(H\to\mu_2\) 都在 \(2g\) 上取 \(1\)。
这说明第 5 节的 fixed-order SNF 门不能省略。

本卡只把已证明有限的 source universe 变成可判定的饱和/相位接口；它不证明全局
source-map 完备，也不把角色提升自动变成实际因子、Type I/II 短证书或整数递降。
但在 fixed-order 门通过后，初等角色到 closed source edges 的求值配对和秩容量已经
由上述规范商确定，不再保留为独立的 transport 黑箱。
