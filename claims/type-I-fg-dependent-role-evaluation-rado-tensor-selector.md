---
kind: claim
claim_id: type-I-fg-dependent-role-evaluation-rado-tensor-selector
title: F/G 相关角色物理义务的求值配对、广义 Rado 与张量和选择器
statement: >-
  固定一个 ell 初等角色空间 R 和同一 source-SNF 表给出的源关系空间 L。只有每条
  带请求标签的 column edge 都携带可复核关系向量 u_e in L，且角色限制与源关系之间
  的双线性求值来自同一 provenance 时，才能定义实现向量
  kappa(e)(rho)=<rho,u_e> in R*。保留全部 n 个物理请求而令 k=dim R；存在每请求
  恰选一个 column 且所选实现向量张成 R*，当且仅当对每个请求子集 U，
  rank kappa(A(U))+n-|U|>=k。该广义 Rado 条件允许相关角色共享代数秩而不删除其
  不同 occurrence/target 义务；失败时不可见角色空间的维数严格大于补集请求数。
  在 fixed-target residual deep--shallow--column 候选严格三维矩形时，该条件与
  target 预收费、deep Hall、shallow Hall 联合成为完整 assignment 的充要条件。
  若调用者要求所选实现向量生成一个较大空间中的规定真子空间 D，则所有子空间 Hall
  割一般不充分；精确判据是需求基矩阵 B_D 属于 rank-one tensor sets
  {kappa(e)c^T} 的 Minkowski 和，等价于一个有限 projective-dual hitting cover，
  并有精确 Fourier 卷积表示数。F_2^2 的单请求菜单 {e1,e2}、需求
  <e1+e2> 是最小严格假阳性。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fg-fourier-to-type-II-role-demand-bridge
  - type-I-fg-role-snf-terminal-dispatch
  - type-II-rado-linear-rank-hall-capacity-bridge
  - type-II-linear-rank-deficit-dual-separation-certificate
  - type-II-owner-source-preserving-fiber-uniformity-criterion
  - type-I-prescribed-target-occurrence-rado-contraction
topics:
  - type-I
  - type-II
  - F-state
  - G-state
  - dependent-role
  - evaluation-pairing
  - Rado
  - matroid
  - tensor-sumset
  - Fourier
  - physical-capacity
  - strict-obstruction
  - proof-program
sources:
  - claim: type-I-fg-fourier-to-type-II-role-demand-bridge
    role: common-elementary-role-space
  - claim: type-I-fg-role-snf-terminal-dispatch
    role: joint-role-source-label-provenance
  - claim: type-II-rado-linear-rank-hall-capacity-bridge
    role: independent-representative-theorem
  - claim: type-II-linear-rank-deficit-dual-separation-certificate
    role: source-role-common-space-boundary
  - claim: type-II-owner-source-preserving-fiber-uniformity-criterion
    role: physical-column-canonicalization
  - claim: type-I-prescribed-target-occurrence-rado-contraction
    role: fixed-target-residual-physical-product
  - reproduction: reproductions/type_i_fg_dependent_role_evaluation_rado_tensor_selector.py
    role: focused-generalized-rado-tensor-dual-and-minimal-controls
visibility: public
last_checked: '2026-08-10'
---

# F/G 相关角色物理义务的求值配对、广义 Rado 与张量和选择器

## 1. 先构造角色--源列求值，而不是直接比较两个秩

固定初等素数 \(\ell\)。令 \(R\) 是实际 F/G Fourier restrictions 张成的有限维
\(\mathbb F_\ell\)-角色空间，令 \(L\) 是同一个已封闭 source-SNF table 中的源关系
空间。角色原本属于 \(\operatorname{Hom}(\Delta,\mu_\ell)\)，源列原本属于 source
relation quotient；两者不能仅因维数相同就直接识别。进入本卡必须先给出双线性配对

\[
\langle\ ,\ \rangle:R\times L\longrightarrow\mathbb F_\ell
\tag{1}
\]

以及如下 typed 回执：

~~~text
ROLE_EVALUATION_PAIRING_CERT
  elementary_prime: ell
  role_basis: a basis of R
  source_relation_basis: a basis of L
  pairing_matrix: evaluations from the same closed SNF/source table
  edge_relation_vector: e |-> u_e in L
  provenance: the complete witness that produced e and u_e
~~~

这里已固定 \(\mu_\ell\simeq\mathbb F_\ell\) 的加法坐标；改变 primitive root 只对
整个配对乘一个非零标量，不改变秩。每个带请求标签的 column edge \(e=(p,a)\)
必须携带由同一完整 witness、role-SNF 和 provenance 得到的
\(u_e\in L\)。定义它的**角色实现向量**

\[
\kappa(e)\in R^*,\qquad
\kappa(e)(\rho)=\langle\rho,u_e\rangle.
\tag{2}
\]

相同 source relation 必须给出相同 \(\kappa\)；请求标签不能凭空克隆角色秩。
若 column 自身还有未被 occurrence/shallow ledger 吸收的排他容量，必须先拆成
true-twin 物理副本，不能把 \(\kappa\) 当作容量副本。

取全部物理请求集合

\[
P=\{p_1,\ldots,p_n\},\qquad
R=\operatorname{span}\{\rho_p:p\in P\},\qquad
k=\dim R.
\tag{3}
\]

相关角色可以有不同 source/target occurrence 义务，所以 \(n\) 可以严格大于
\(k\)，且不能删除任何 \(p\)。对每个请求，令 \(A(p)\) 是通过全部局部门后的
非空带标签 column menu。

给定选择 \(\sigma(p)\in A(p)\)，定义联合求值映射

\[
\operatorname{ev}_\sigma:
R\longrightarrow\mathbb F_\ell^P,\qquad
\rho\longmapsto
\bigl(\kappa(\sigma(p))(\rho)\bigr)_{p\in P}.
\tag{4}
\]

称该选择**支付全部角色空间**，若 \(\operatorname{ev}_\sigma\) 单射。有限维对偶
立即给出求值配对引理

\[
\boxed{
\operatorname{ev}_\sigma\text{ 单射}
\iff
\operatorname{span}\{\kappa(\sigma(p)):p\in P\}=R^*
\iff
\bigcap_{p\in P}\ker\kappa(\sigma(p))=\{0\}.}
\tag{5}
\]

因此正确的 column 对象是 \(\kappa(e)\)，不是未经角色配对的裸 source vector。
在 finite-abelian source table 已由 exact contract 封闭、每条 edge 保存 ambient
群坐标、且 fixed-order SNF 已提升实际角色的分支，(1)--(2) 不是额外假设：取

\[
V_\ell=(S+\ell H)/\ell H,
\qquad
K_R=V_\ell/R^\perp\simeq R^*,
\]

并把 SNF 强制标签模 \(\ell\)，其标签矩阵的 edge 列正是 \(\kappa(e)\)。完整构造与
ambient-extension 边界见
[source-SNF 的规范初等角色求值商](type-I-fg-snf-canonical-role-evaluation-quotient.md)。
只有 source contract、ambient extension 或 edge provenance 尚未证明时，合法回执才是

~~~text
ROLE_TO_COLUMN_EVALUATION_UNPROVED
~~~

不能用 source rank 等于 role rank 代替。

## 2. 相关角色的广义 Rado 阈值定理

先证明一个纯线性选择定理。令 \(K\) 是有限维 \(\mathbb F_\ell\)-空间，
\(\mathcal A(p)\subseteq K\) 是 \(n\) 个非空有限 menus。定义

\[
\nu(\mathcal A)
=\max_{a_p\in\mathcal A(p)}
\operatorname{rank}\{a_p:p\in P\}.
\tag{6}
\]

**广义 Rado 阈值定理。** 对 \(0\le s\le n\)，存在每个请求恰选一个向量且
所选秩至少为 \(s\)，当且仅当

\[
\boxed{
\operatorname{rank}
\left(\bigcup_{p\in U}\mathcal A(p)\right)
+n-|U|\ge s
\qquad\text{对每个 }U\subseteq P.}
\tag{7}
\]

特别地，

\[
\boxed{
\nu(\mathcal A)
=\min_{U\subseteq P}
\left[
\operatorname{rank}
\left(\bigcup_{p\in U}\mathcal A(p)\right)
+n-|U|
\right].}
\tag{8}
\]

**证明。** 任一完整选择在 \(U\) 内至多贡献
\(\operatorname{rank}(\bigcup_{p\in U}\mathcal A(p))\) 个方向，在补集至多贡献
\(n-|U|\) 个方向，所以 (7) 必要。

反过来，取与 \(K\) 直和的 \(n-s\) 维空间

\[
Z=\langle z_1,\ldots,z_{n-s}\rangle
\tag{9}
\]

并把每个 menu 扩成

\[
\mathcal A'(p)=\mathcal A(p)\cup\{z_1,\ldots,z_{n-s}\}.
\]

对任意 \(U\)，式 (7) 等价于

\[
\operatorname{rank}
\left(\bigcup_{p\in U}\mathcal A'(p)\right)
=
\operatorname{rank}
\left(\bigcup_{p\in U}\mathcal A(p)\right)+n-s
\ge |U|.
\]

普通 Rado 独立代表定理遂给每个请求一个独立代表。独立选择中至多有 \(n-s\)
个 dummy \(z_i\)，所以至少 \(s\) 个代表来自原 menus 且线性独立。给其余请求
任取一个原 menu 向量，所得完整原选择的秩至少为 \(s\)。这证明 (7)，再对最大
可行 \(s\) 取值即得 (8)。证毕。

把 \(K=R^*\)、\(\mathcal A(p)=\kappa(A(p))\) 和 \(s=k\) 代入，(5)--(8) 得到
相关角色求值选择器：

\[
\boxed{
\exists\sigma:\operatorname{ev}_\sigma\text{ 单射}
\iff
\operatorname{rank}\kappa(A(U))+n-|U|\ge k
\quad(\forall U\subseteq P).}
\tag{10}
\]

当 \(n=k\) 时，(10) 正好退化为普通 Rado 条件，但它作用在已认证的 evaluation
vectors \(\kappa(e)\) 上。只有另有一个 rank-preserving identification
\(u_e\mapsto\kappa(e)\)，才能把 (10) 写成裸 source-column Rado。

### 缺口的不可见角色空间

对 \(U\subseteq P\) 定义

\[
Z_U
=\{\rho\in R:
\langle\rho,u_e\rangle=0
\text{ 对每个 }e\in\bigcup_{p\in U}A(p)\}.
\tag{11}
\]

则

\[
\dim Z_U
=k-\operatorname{rank}\kappa(A(U)).
\tag{12}
\]

若 (10) 对 \(U\) 失败，便有

\[
\boxed{\dim Z_U>n-|U|.}
\tag{13}
\]

补集的任一选择至多再施加 \(n-|U|\) 个线性条件，所以 \(Z_U\) 中仍有一个非零
角色湮灭整个完整选择。因此 (13) 是严格的

~~~text
ROLE_EVALUATION_GENERALIZED_RADO_DEFICIT
~~~

而不只是“候选数不足”。该非零角色一般依赖补集如何选择，但亏损仍有一个不依赖
该选择的规范对象：

\[
Q_U
=R^*/\operatorname{span}\kappa(A(U)),
\qquad
Q_U^*\simeq Z_U.
\tag{13a}
\]

令 \(m_U=\dim Q_U\)、\(r_U=n-|U|\)，则任一完成在 \(Q_U\) 中只能生成至多
\(r_U\) 维，且至少留下 \(m_U-r_U\) 维角色 kernel。更强地，最佳完整选择的精确
缺秩为

\[
k-\nu
=\max_{U\subseteq P}
\bigl(m_U-r_U\bigr).
\tag{13b}
\]

若全部菜单已经生成 \(R^*\)，则不存在对所有完成统一有效的非零标量角色；正亏损割
也不可能同时支配 closed source universe 的全部真实生成元。因此 (13a) 是固定线性
容量商，不是当前饱和 source state 的单角色 quotient descent。完整证明、最小严格
反例与后继门见
[广义 Rado 亏损的规范固定割商](type-I-fg-generalized-rado-fixed-quotient-defect.md)。

## 3. fixed-target 矩形系统的完整收缩

沿指定 target occurrence 的先验割，先处理 exact replay/history，并对 fresh
请求固定

\[
t(p),\qquad
m_T(o)=\#\{p:t(p)=o\},\qquad
b_D^T(o)=b_O(o)-m_T(o).
\tag{14}
\]

自身 deep key 等于 target key 时仍使用请求私有的 \(\star_p\)，容量为一且不增加
真实 ledger。记增量 deep、shallow 与 column 的投影 menus 为

\[
\mathcal D(p),\qquad
\mathcal S(p),\qquad
A(p),
\]

并假设全部局部门后有完整三维矩形

\[
\boxed{
\widehat{\mathcal E}_{\rm src}(p)
=\mathcal D(p)\times\mathcal S(p)\times A(p).}
\tag{15}
\]

**相关角色矩形收缩定理。** 在 (1)--(5)、fixed-target 合同和 (15) 下，存在满足
全部 \(n\) 个物理请求、共享 occurrence 容量、shallow 容量并支付整个角色空间
\(R\) 的完整 assignment，当且仅当：

\[
m_T(o)\le b_O(o)\qquad(\forall o),
\tag{16}
\]

\[
\sum_{d\in\bigcup_{p\in U}\mathcal D(p)}b_D(d)\ge |U|,
\qquad
\sum_{h\in\bigcup_{p\in U}\mathcal S(p)}b_S(h)\ge |U|
\qquad(\forall U\subseteq P),
\tag{17}
\]

以及

\[
\operatorname{rank}\kappa(A(U))+n-|U|\ge k
\qquad(\forall U\subseteq P).
\tag{18}
\]

这里真实 deep 的 \(b_D=b_D^T\)，私有 \(b_D(\star_p)=1\)。

**证明。** 必要性分别来自 fixed-target 收费、两组 capacitated Hall 和 (7)。
反向地，(17) 给每个物理请求选择合法 deep 与 shallow 副本；(18) 先选择 \(k\)
个具有独立 evaluation vectors 的请求--column edges，再给其余请求任取 filler
column。(15) 把三组按同一请求索引重组为完整 witness，(16) 再与 residual
deep 收费合并。式 (5) 保证所选 columns 支付整个 \(R\)。证毕。

这正面处理“相关角色但物理义务不同”：全部物理请求仍分别占用 deep/shallow/
target，只有代数收费从错误的 \(n\) 降为真实角色秩 \(k\)。若 (15) 失败，必须
保留完整带标签 hypergraph 并输出

~~~text
DEPENDENT_ROLE_COUPLED_HYPERGRAPH_REQUIRED
~~~

不能把 (17)--(18) 的分离投影当作充分条件。

## 4. 规定真子空间需要 rank-one tensor 和，而不是秩影子

求值接口的自然目标是整个 \(R^*\)，所以 (10) 已精确。但更一般的调用者可能给出
实现空间 \(K\simeq\mathbb F_\ell^r\) 及一个规定子空间
\(D\le K\)，要求

\[
D\subseteq
\operatorname{span}\{\kappa(\sigma(p)):p\in P\}.
\tag{19}
\]

设 \(d=\dim D\)，固定 \(D\) 的有序基矩阵
\(B_D\in\operatorname{Mat}_{r\times d}(\mathbb F_\ell)\)。对每个请求定义
rank-one tensor support

\[
\mathcal T_p
=
\{\kappa(e)c^T:
e\in A(p),\ c\in\mathbb F_\ell^d\}
\subseteq
G:=\operatorname{Mat}_{r\times d}(\mathbb F_\ell).
\tag{20}
\]

**张量和定理。** 在每个 \(A(p)\) 是请求局部标签、column 排他容量已另行支付的
前提下，

\[
\boxed{
\exists\sigma\text{ 满足 (19)}
\iff
B_D\in\mathcal T_{p_1}+\cdots+\mathcal T_{p_n}.}
\tag{21}
\]

**证明。** 对一个选择令

\[
M_\sigma=
[\kappa(\sigma(p_1))\ \cdots\ \kappa(\sigma(p_n))].
\]

式 (19) 等价于存在 \(C\in\operatorname{Mat}_{n\times d}(\mathbb F_\ell)\) 使

\[
M_\sigma C=B_D.
\tag{22}
\]

把 \(C\) 的第 \(p\) 行记为 \(c_p^T\)，则 (22) 正是

\[
B_D=\sum_{p\in P}\kappa(\sigma(p))c_p^T.
\tag{23}
\]

这给出 (21) 两个方向。若 \(c_p=0\)，对应请求仍可从非空 \(A(p)\) 任取 filler，
所以“至多选”与“每请求恰选”在局部标签模型下等价。证毕。

改变 \(D\) 的基把 \(B_D\) 右乘 \(Q\in\operatorname{GL}_d\)，而
\(\mathcal T_pQ=\mathcal T_p\)，故 (21) 与需求基无关。改变 \(K\) 的坐标则同时
左乘所有矩阵，也不改变 membership。

### 精确 projective-dual hitting cover

令

\[
\Omega_D
=\{[\lambda]\in\mathbf P(K^*):\lambda|_D\ne0\},
\qquad
C_e
=\{[\lambda]\in\Omega_D:\lambda(\kappa(e))\ne0\}.
\tag{24}
\]

有限维双正交关系给出第二个精确等价：

\[
\boxed{
\exists\sigma\text{ 满足 (19)}
\iff
\exists\sigma:\quad
\Omega_D=\bigcup_{p\in P}C_{\sigma(p)}.}
\tag{25}
\]

也就是存在 \(0\)-\(1\) 变量 \(x_{p,e}\) 满足

\[
\sum_{e\in A(p)}x_{p,e}=1\quad(\forall p),
\tag{26}
\]

\[
\sum_{\substack{p,e\\\lambda(\kappa(e))\ne0}}
x_{p,e}\ge1
\quad(\forall[\lambda]\in\Omega_D).
\tag{27}
\]

式 (25) 说明正确量词是先固定一组 columns，再同时击中全部非平凡需求对偶方向。

### 精确 Fourier 表示数与 tensor coset capacity

在加法群 \(G\) 上定义带 multiplicity 的函数

\[
f_p(X)
=\#\{(e,c)\in A(p)\times\mathbb F_\ell^d:
\kappa(e)c^T=X\}.
\tag{28}
\]

则张量表示数

\[
N_D=(f_{p_1}*\cdots*f_{p_n})(B_D)
\tag{29}
\]

满足

\[
\boxed{N_D>0\iff\text{(19) 有解}.}
\tag{30}
\]

取

\[
\chi_\Lambda(X)
=\exp\!\left(
\frac{2\pi i}{\ell}
\operatorname{tr}(\Lambda^TX)
\right),
\qquad
\widehat f_p(\Lambda)
=\sum_{X\in G}f_p(X)\overline{\chi_\Lambda(X)},
\]

Fourier inversion给出

\[
\boxed{
N_D
=\frac1{|G|}
\sum_{\Lambda\in G}
\left(\prod_{p\in P}\widehat f_p(\Lambda)\right)
\chi_\Lambda(B_D).}
\tag{31}
\]

所以失败分支有规范回执

~~~text
COLORED_ROLE_TENSOR_SUMSET_OBSTRUCTION
  target_matrix: B_D
  tensor_supports: T_p
  convolution_value: 0
  Fourier_spectrum: product of the local transforms
~~~

这不是自动的单角色 annihilator。令

\[
\mathcal T=\sum_{p\in P}\mathcal T_p,\qquad
H_T=\{Y\in G:\mathcal T+Y=\mathcal T\},
\qquad
\operatorname{cap}_T=\frac{|\mathcal T|}{|H_T|}.
\tag{32}
\]

\(\operatorname{cap}_T\) 是可达 tensor cosets 的精确容量；若
\(\operatorname{cap}_T=|G/H_T|\)，则 \(\mathcal T=G\)，所有同维需求矩阵都可达。
若 \(B_D\notin\mathcal T\)，缺失的是 \(G/H_T\) 中的一个具体 coset；把该商接成
整数后继仍须另证 E1--E5。

## 5. 所有子空间割的严格假阳性

式 (19) 的任一成功选择必满足

\[
\boxed{
\dim D-\dim(D\cap W)
\le
\#\{p:\kappa(A(p))\nsubseteq W\}
\qquad(\forall W\le K).}
\tag{33}
\]

因为 \(D\) 在 \(K/W\) 中的像由已选且不在 \(W\) 中的向量生成，每个请求至多
贡献一个方向。但 (33) 一般不充分。

对任意有限域取

\[
K=\mathbb F_\ell^2,\qquad
D=\langle e_1+e_2\rangle,\qquad
P=\{p\},\qquad
\kappa(A(p))=\{e_1,e_2\}.
\tag{34}
\]

若 \(D\le W\)，(33) 左端为零。若 \(D\nleq W\)，左端为一；此时
\(\{e_1,e_2\}\subseteq W\) 会强制 \(W=K\)，矛盾，所以右端也为一。全部
subspace cuts 均通过，但唯一选择只能生成 \(\langle e_1\rangle\) 或
\(\langle e_2\rangle\)，均不含 \(D\)。在 tensor 语言中，
\(B_D=e_1+e_2\notin\mathcal T_p\)。

这是最小反例：一维环境没有规定真非零子空间；单请求 singleton menu 若 (33)
通过，取其 span 即强制它生成 \(D\)。而且 \(\{e_1,e_2\}\) 张成整个 \(K\)，不存在
一个湮灭全部候选而分离 \(D\) 的单一线性泛函；失败来自

\[
\forall W\ \exists e(W)
\quad\not\Longrightarrow\quad
\exists e\ \forall W,
\]

所以必须保留 (21)、(25) 或 (31) 的联合选择对象。

有三个精确退化边界：

1. \(D=0\) 时自动成功；
2. \(D=K\) 或全部 eligible vectors 已落在 \(D\) 中时，问题退化为 (7) 的
   generalized Rado full-rank 条件；
3. \(n=\dim D\) 时，成功选择的 span 必须恰为 \(D\)，故可把每个 menu 限制到
   \(A(p)\cap D\) 后应用普通 Rado。

## 6. 三个严格控制

### 裸 source rank 不能替代角色求值

取 \(L=\mathbb F_2^2\)、\(R=\langle\rho_x\rangle\)，其中
\(\rho_x(x,y)=x\)。一个请求只有 relation column \(u=e_2\)。裸 column rank 为一，
与 \(k=1\) 相等；但

\[
\kappa(e_2)(\rho_x)=0,
\]

所以求值秩为零，角色完全未支付。这给出

~~~text
RAW_SOURCE_RANK_ROLE_PAYMENT_FALSE_POSITIVE
~~~

并证明 (1)--(2) 不是记账格式。

### 三个物理请求、两个相关角色方向

仍用标准配对，取

\[
\rho_{p_1}=\rho_{p_2}=\rho_x,\qquad
\rho_{p_3}=\rho_y,
\qquad k=2,
\]

\[
A(p_1)=A(p_2)=\{e_1\},\qquad
A(p_3)=\{e_2\}.
\tag{35}
\]

全部三个物理请求都保留；evaluation vectors 的最大秩为二，(10) 通过并支付
\(R=\langle\rho_x,\rho_y\rangle\)。错误地把三个请求都当独立角色会要求秩三并
拒绝这个合法 assignment。因此本卡严格扩大了此前独立请求定理的覆盖域。

### 并集秩仍不足

取 \(n=3,k=2\) 及

\[
\kappa(A(p_1))=\{e_1,e_2\},\qquad
\kappa(A(p_2))=\kappa(A(p_3))=\{0\}.
\tag{36}
\]

全部 menus 的并集秩为二，但任一选择的秩至多一。对
\(U=\{p_2,p_3\}\)，

\[
\operatorname{rank}\kappa(A(U))+3-|U|=0+1<2,
\]

故 (10) 精确抓住颜色集中缺口。

## 7. 统一选择器分派

~~~text
FIXED_TARGET_NAMED_WITNESSES_READY
  preserve every physical request and all occurrence obligations
  build the common elementary role space R
  construct ROLE_EVALUATION_PAIRING_CERT from the same closed source-SNF table:
    unavailable:
      ROLE_TO_COLUMN_EVALUATION_UNPROVED
    available:
      attach kappa(e) to every labeled column edge
  target key varies:
    VARIABLE_TARGET_COUPLED_HYPERGRAPH_REQUIRED
  fixed target:
    run shared-occurrence target precharge and residual deep map
    exact three-coordinate rectangularity fails:
      DEPENDENT_ROLE_COUPLED_HYPERGRAPH_REQUIRED
    rectangularity passes:
      run capacitated deep Hall and shallow Hall
      natural target is all of R*:
        run generalized Rado condition (10)
        deficit:
          emit U, Z_U, Q_U, delta(U)
          GENERALIZED_RADO_FIXED_QUOTIENT_DEFECT
        pass:
          ROLE_EVALUATION_PHYSICAL_ASSIGNMENT
      prescribed proper implementation subspace D:
        run cheap necessary generalized-rank/subspace cuts
        run exact tensor membership (21)
        pass:
          emit selected edges and coefficient matrix C
        fail:
          COLORED_ROLE_TENSOR_SUMSET_OBSTRUCTION
          preserve Fourier convolution and tensor quotient
  any successful arithmetic assignment:
    E4 and non-resetting E5 remain mandatory
~~~

## 8. 研究边界

本卡关闭了此前 DEPENDENT_ROLE_PHYSICAL_COUPLING_REQUIRED 的 fixed-target、
source-preserving、完整三维矩形且已有角色求值配对的子分支。它既不删除相关角色的
不同物理义务，也不再强迫 \(n\) 个物理请求支付 \(n\) 个独立角色方向。

第一项 typed 缺口现已在“exact finite source universe + fixed-order SNF lift + 每条
edge 的 ambient 群坐标”分支关闭：规范初等商直接构造 (1)--(2)。角色仍只登记在
\(\operatorname{Hom}(\Delta,\mu_\ell)\)、source contract 未闭合或 edge 超出 certified
span 时，才保留 ROLE_TO_COLUMN_EVALUATION_UNPROVED。第二项是实际候选未满足 (15) 时的联合
hypergraph--matroid 选择。第三项现已进一步分开：广义 Rado 的 (13) 有规范固定割商
与精确亏格，但 source saturation 同时排除了当前状态上的共同标量 annihilator。
裸 top exterior 已证明只重述 rank deficit；若拟议后继的固定 source 开销
\(X\) 满足 \(\dim X<\delta(U)\)，则
[Grassmann 切片容量定理](type-I-fg-exterior-grassmann-slice-successor-descent.md)
对任意非矩形可行完成集给出
\(\delta(U)-\dim X\) 维共同角色分支。否则输出严格开销边界，而不是继续寻找同类
annihilator。式 (31) 的 tensor Fourier 零表示仍须独立接到完整 kernel source box、
Type I/II 终端、整数后继及不可重置 marked E5；top-exterior 与可救的目标依赖
Plücker 边界见
[exterior--Fourier no-go](type-I-fg-exterior-fourier-plucker-boundary.md)。

## 聚焦验证

~~~bash
python3 \
  reproductions/type_i_fg_dependent_role_evaluation_rado_tensor_selector.py \
  --verify
~~~

验证器只穷尽 \(\mathbb F_2^2\) 的小菜单，交叉检查 generalized Rado、tensor
membership、projective-dual hitting 与 Fourier inversion，并重算 (34)--(36)；
不运行历史扫描。
