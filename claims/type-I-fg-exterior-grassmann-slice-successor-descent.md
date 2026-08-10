---
kind: claim
claim_id: type-I-fg-exterior-grassmann-slice-successor-descent
title: F/G 亏损商的 Grassmann 切片容量、矩阵 Fourier 与 kernel 后继递降接口
statement: >-
  设广义 Rado 正亏损割给出 Q=Q_U、m=dim Q、r=|P-U| 与
  delta=m-r>0。对任意非空且可含物理耦合的可行完成集 Omega，以及后继必须额外
  保留的固定 source-evaluation 开销 X<=Q，令 h=dim X。若 h<delta，则对每个
  1<=s<=delta-h，存在 s 维实际角色空间 L<=(Q/X)^*，使 Omega 中正比例的完成
  全部落在 L 的共同核；该比例至少为 Gaussian 比
  [delta-h choose s]_q/[m-h choose s]_q。更精确地，全部 Grassmann 分支的
  incidence 总数等于各完成 annihilator 维数对应的 Gaussian 系数之和。取
  s=delta-h 得到 residual capacity epsilon(U,X)=delta-h。L 拉回真实
  SNF-role space 后给出 perfect role quotient (R/L,L^perp)，并在
  SELECTED_SOURCE_OVERHEAD_RANK_CERT、独立实现的 exact kernel successor 与
  branch/certificate lift 成立时产生
  有限群子群--标量商二分；除 H=C_q 的 top-primary 边界外，该二分严格下降群阶。
  但整数 Type I/II 后继仍须另过 FIBER_REALIZED、来源、
  SNF/CRT、范围、E4 与不可重置 E5。在只知道至多 r 条 completion 列并统一使用
  completion-independent X 时，阈值 h<delta 最优；具体 exact successor 还可由
  selection-rank slack 精确改进。p=97,D=6 的单来源 C_2 角色给出“有限群
  quotient 存在而全部严格整数低层菜单为空”的严格边界。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fg-generalized-rado-fixed-quotient-defect
  - type-I-fg-snf-canonical-role-evaluation-quotient
  - type-I-II-fg-universal-finite-source-map-completion
  - type-II-annihilator-two-sided-subgroup-quotient-descent
  - type-II-annihilator-congruence-fiber-lift-criterion
topics:
  - type-I
  - type-II
  - F-state
  - G-state
  - Grassmannian
  - Gaussian-binomial
  - Fourier
  - matrix-Fourier
  - residual-capacity
  - kernel-subcontract
  - subgroup-descent
  - quotient-descent
  - strict-obstruction
  - proof-program
sources:
  - claim: type-I-fg-generalized-rado-fixed-quotient-defect
    role: fixed-defect-quotient-and-moving-annihilator-space
  - claim: type-I-fg-snf-canonical-role-evaluation-quotient
    role: perfect-role-evaluation-pairing
  - claim: type-I-II-fg-universal-finite-source-map-completion
    role: exact-finite-source-contract
  - claim: type-II-annihilator-two-sided-subgroup-quotient-descent
    role: finite-group-kernel-relay
  - claim: type-II-annihilator-congruence-fiber-lift-criterion
    role: integer-successor-lift-gates
  - reproduction: reproductions/type_i_fg_exterior_grassmann_slice_successor_descent.py
    role: focused-grassmann-incidence-fourier-threshold-filter-and-integer-boundaries
visibility: public
last_checked: '2026-08-10'
---

# F/G 亏损商的 Grassmann 切片容量、矩阵 Fourier 与 kernel 后继递降接口

## 1. 可行完成与后继开销

固定素数 \(q\)。由正广义 Rado 亏损割 \(U\subseteq P\) 取得

\[
Q=Q_U=K_R/W_U,\qquad
m=\dim Q,\qquad
C=P\setminus U,\qquad
r=|C|,\qquad
\delta=m-r>0.
\tag{1}
\]

这里 \(Q^*\simeq Z_U\le R\) 是真实 SNF-role space 的子空间。与只处理菜单
笛卡尔积不同，先让

\[
\varnothing\ne\Omega
\subseteq
\prod_{p\in C}\mathcal A(p)
\tag{2}
\]

是已经通过全部当前物理耦合门的**带标签可行完成集**。一个
\(\omega\in\Omega\) 在 \(Q\) 中给出 \(r\) 条列
\(b_p(\omega)\)。因此下述证明不会把非矩形 hypergraph 偷换成独立菜单。

令 \(X\le Q\) 是拟议后继除这些 \(r\) 条所选列外还必须保留的固定
source-evaluation 方向，置

\[
h=\dim X,\qquad
\bar Q=Q/X,\qquad
d=\dim\bar Q=m-h,\qquad
\varepsilon=d-r=\delta-h.
\tag{3}
\]

正向定理的严格门是

\[
\boxed{h<\delta\quad\Longleftrightarrow\quad\varepsilon>0.}
\tag{4}
\]

把 \(b_p(\omega)\) 在 \(\bar Q\) 中的像仍记为 \(b_p(\omega)\)，并令

\[
S_\omega=\operatorname{span}
\{b_p(\omega):p\in C\}\le\bar Q.
\tag{5}
\]

总有 \(\dim S_\omega\le r\)。

## 2. Grassmann 切片双计数定理

对 \(0\le s\le n\)，用

\[
{n\brack s}_q
=
\prod_{i=0}^{s-1}
\frac{q^{n-i}-1}{q^{s-i}-1}
\tag{6}
\]

表示 \(n\) 维 \(\mathbb F_q\) 空间中 \(s\) 维子空间的个数。固定
\(1\le s\le\varepsilon\)。对
\(L\in\operatorname{Gr}_s(\bar Q^*)\)，定义该角色切片支持的可行分支

\[
\Omega_L
=
\{\omega\in\Omega:
\ell(b_p(\omega))=0
\text{ 对所有 }\ell\in L,\ p\in C\}.
\tag{7}
\]

则有精确 incidence 恒等式

\[
\boxed{
\sum_{L\in\operatorname{Gr}_s(\bar Q^*)}
|\Omega_L|
=
\sum_{\omega\in\Omega}
{d-\dim S_\omega\brack s}_q.}
\tag{8}
\]

因为 \(\dim S_\omega\le r\)，Gaussian 系数随上维数单调，故

\[
\sum_L|\Omega_L|
\ge
{d-r\brack s}_q|\Omega|
=
{\varepsilon\brack s}_q|\Omega|.
\tag{9}
\]

而 \(|\operatorname{Gr}_s(\bar Q^*)|={d\brack s}_q\)，所以至少一个
\(L\) 满足

\[
\boxed{
\frac{|\Omega_L|}{|\Omega|}
\ge
\frac{{\varepsilon\brack s}_q}{{d\brack s}_q}>0.}
\tag{10}
\]

这不只是存在性证明。有限域、带标签边顺序及固定 RREF 规范给出有限枚举，
可输出达到最大 \(|\Omega_L|\) 的第一项作为构造性证书。

### 证明

固定 \(\omega\)。式 (7) 等价于

\[
L\le S_\omega^\perp\le\bar Q^*.
\tag{11}
\]

\(S_\omega^\perp\) 的维数为 \(d-\dim S_\omega\)，所以满足 (11) 的
\(L\) 恰有
\({d-\dim S_\omega\brack s}_q\) 个。先按 \(L\) 计数
\(\{(L,\omega):\omega\in\Omega_L\}\)，再按 \(\omega\) 计数，得到
(8)；(9)--(10) 随即成立。

## 3. 矩形菜单、Fourier 平均与 residual capacity

若当前物理合同确实给出矩形完成

\[
\Omega=\prod_{p\in C}B_p
\tag{12}
\]

（\(B_p\) 保留带标签重数），定义

\[
n_p(L)=
\#\{b\in B_p:\ell(b)=0\text{ 对所有 }\ell\in L\}.
\tag{13}
\]

此时 \(|\Omega_L|=\prod_p n_p(L)\)，故 (8)--(10) 化为

\[
\sum_L\prod_{p\in C}n_p(L)
=
\sum_{(b_p)}
{d-\operatorname{rank}\langle b_p:p\in C\rangle\brack s}_q
\ge
{\varepsilon\brack s}_q\prod_p|B_p|,
\tag{14}
\]

\[
\max_L\prod_{p\in C}\frac{n_p(L)}{|B_p|}
\ge
\frac{{\varepsilon\brack s}_q}{{d\brack s}_q}.
\tag{15}
\]

取非平凡加法角色
\(\psi:\mathbb F_q\to\mathbb C^\times\)，并令
\(\widehat\mu_p(\ell)=\sum_{b\in B_p}\psi(\ell(b))\)。角色正交性给出

\[
\boxed{
n_p(L)
=q^{-s}\sum_{\ell\in L}\widehat\mu_p(\ell).}
\tag{16}
\]

因此 (14) 是对所有 \(s\) 维 Fourier role slices 的精确平均，而不是仅按
支撑大小作松估计。

若以保证的角色维数为目标，最大可取 \(s=\varepsilon\)。由此定义新的后继剩余容量

\[
\boxed{
\varepsilon(U,X)
=\delta(U)-\dim X.}
\tag{17}
\]

它表示在支付固定开销 \(X\) 和全部 \(r\) 个补集请求后，仍保证可共同保留的
线性独立角色数。式 (10) 同时给出这些角色至少覆盖多少当前可行完成。

## 4. 辅助的 matrix-Fourier obstruction

在矩形分支且 \(1\le r<d\) 时还有一个不依赖所选基的行列式 Fourier 形式。令

\[
E=\operatorname{End}(\bar Q),
\qquad
(b\otimes\lambda)(x)=\lambda(x)b,
\tag{18}
\]

并对每个 \(p\in C\) 定义

\[
f_p(T)
=
\#\{(b,\lambda)\in B_p\times\bar Q^*:T=b\otimes\lambda\}.
\tag{19}
\]

用 trace pairing 的 Fourier 变换

\[
\widehat f_p(\Lambda)
=
\sum_{T\in E}f_p(T)
\psi(-\operatorname{tr}(\Lambda T)).
\tag{20}
\]

因为
\(\operatorname{tr}(\Lambda(b\otimes\lambda))
=\lambda(\Lambda b)\)，角色正交性给出

\[
\boxed{
\widehat f_p(\Lambda)
=q^d\#\{b\in B_p:\Lambda b=0\}.}
\tag{21}
\]

任意 \(r\) 个 rank-one endomorphisms 的和秩至多 \(r<d\)，不可能等于
\(I_{\bar Q}\)。所以

\[
(f_{p_1}*\cdots*f_{p_r})(I_{\bar Q})=0.
\tag{22}
\]

对 (22) 作 Fourier 反演并移去零频率，得到精确谱恒等式

\[
\boxed{
\sum_{\Lambda\ne0}
\psi(\operatorname{tr}\Lambda)
\prod_{p\in C}\#\{b\in B_p:\Lambda b=0\}
=-\prod_{p\in C}|B_p|.}
\tag{23}
\]

式 (23) 是严格非零的 determinantal/matrix-Fourier obstruction。不过其频率群
是 \(\operatorname{End}(\bar Q)\) 的加法群，不是当前整数 source group；没有新的
homomorphic arithmetic realization 时，不能把它误记成普通 Type I/II Fourier
角色。

## 5. 角色商与 selected-source 闭包

把 (10) 给出的
\(L\le(\bar Q)^*=(Q/X)^*\) 依次拉回

\[
L\le Q^*=Z_U\le R.
\tag{24}
\]

在原 perfect pairing
\(R\times K_R\to\mathbb F_q\) 中令

\[
K_L=L^\perp
=
\{x\in K_R:\rho(x)=0\text{ 对所有 }\rho\in L\}.
\tag{25}
\]

则配对下降为 perfect pairing

\[
\boxed{
(R/L)\times K_L\longrightarrow\mathbb F_q,}
\tag{26}
\]

且

\[
\dim(R/L)=\dim K_L=\dim R-s.
\tag{27}
\]

确实，若 \(\rho+L\) 湮灭 \(K_L\)，则
\(\rho\in(K_L)^\perp=L\)；另一侧由原配对非退化。故 (26) 是严格的
role-rank quotient，而不只是重新选基。

为了把它变成真实后继，必须对某个
\(\omega\in\Omega_L\) 证明

\[
\boxed{
\pi_U\kappa(g)
\in
X+\operatorname{span}
\{\pi_U\kappa(e_p(\omega)):p\in C\}
\quad
\text{对后继的每个真实 source generator }g.}
\tag{28}
\]

把 (28) 记为 `SELECTED_SOURCE_OVERHEAD_RANK_CERT`。因为 \(L\) 同时湮灭
\(X\) 与所选 \(b_p(\omega)\)，式 (28) 保证 \(L\) 湮灭该后继的全部真实源列。
没有 (28) 时，Grassmann 定理只给出完成列 annihilator，不能调用 source-closed
relay。

式 (28) 的 completion-independent \(X\) 给出统一下界，但不是具体后继的最小
开销。为区别于式 (5) 在 \(Q/X\) 中的像，令
\(S_\omega^Q=\operatorname{span}\{b_p(\omega):p\in C\}\le Q\) 是商映射前的
选择列空间。若后继已经独立实现，令 \(T_\omega\) 为其真实源列在 \(Q\) 中的张成
空间，则最小开销和精确角色容量分别为
\[
h_\omega^*
=\dim((T_\omega+S_\omega^Q)/S_\omega^Q),
\qquad
e_\omega
=\delta+(r-\dim S_\omega^Q)-h_\omega^*.
\tag{28a}
\]
所以 \(r-\dim S_\omega^Q\) 的选择秩松弛可支付额外 source directions；完整的
变开销与目标可见双计数见
[exact successor 的 source 开销与秩松弛选择器](type-I-fg-exact-successor-source-overhead-rank-slack-selector.md)。

## 6. kernel-filtered substate、exact successor 与有限群递降

设实际有限群状态由以下 exact contract 给出：

\[
H,\qquad
\mathcal U,\qquad
u:\mathcal U\to H,\qquad
\Gamma,\qquad
t\notin\Gamma(\mathcal U).
\tag{29}
\]

\(\Gamma(\mathcal V)\) 表示任意带标签子族
\(\mathcal V\subseteq\mathcal U\) 精确实现的源集合。这里必须给出一个保持
evaluation pairing 的**单射线性提升**

\[
\iota_L:
L\hookrightarrow\operatorname{Hom}(H,\mathbb F_q).
\tag{29a}
\]

仅分别声称每个角色“可提升”而不证明共同线性单射，不足以得到下面的联合秩。
以下沿用 \(L\) 表示其像。定义联合映射

\[
\eta_L:H\longrightarrow L^*\simeq\mathbb F_q^s,
\qquad
\eta_L(x)(\rho)=\rho(x),
\qquad
K=\ker\eta_L,
\tag{30}
\]

以及 kernel-filtered records

\[
\mathcal U_L
=
\{a\in\mathcal U:u(a)\in K\}.
\tag{31}
\]

若 contract 对菜单限制单调，并通过

\[
\boxed{
1_H\in\Gamma(\mathcal U_L)
\subseteq
\Gamma(\mathcal U)\cap K,}
\tag{32}
\]

则只能先得到一个 kernel-filtered substate 及

\[
t\notin\Gamma(\mathcal U_L).
\tag{33}
\]

把这一层严格记为 `KERNEL_FILTERED_SUBSTATE`，不能直接称为原状态的 quotient
relay。若要声称它是完整 kernel slice，还必须证明更强的等式

\[
\Gamma(\mathcal U_L)=\Gamma(\mathcal U)\cap K.
\tag{33a}
\]

即使 (33a) 成立，仍须证明过滤后的记录确实属于允许的递归状态族。有限群 relay
的准入数据应是一个独立实现的 exact successor

\[
\boxed{
\Sigma'
=(H,\mathcal U',u',\Gamma',t),\qquad
\Gamma'(\mathcal U')
=\Gamma(\mathcal U_L),\qquad
\Sigma'\in\mathfrak S_{\mathrm{admissible}},}
\tag{33b}
\]

并保存从 \(\Sigma'\) 回到原整数状态的 record provenance 与
branch/certificate lift。式 (33b) 记为
`SELECTED_SOURCE_STATE_REALIZATION`；其中 certificate lift 在整数层正是后述
marked E4 的一部分。没有 (33b) 时，任意删空菜单都会制造无意义的目标缺失。

这个边界有一个严格小型控制。取加法群

\[
H=\mathbb F_2^3,\qquad
L=\langle e_1^*\rangle,\qquad
K=\langle e_2,e_3\rangle,
\tag{33c}
\]

两条源记录为 \(e_1,e_1+e_2\)，并令
\(\Gamma(\mathcal V)\) 是这些记录的线性 span。则

\[
\mathcal U_L=\varnothing,\qquad
\Gamma(\mathcal U_L)=\{0\}
\subsetneq
\Gamma(\mathcal U)\cap K=\langle e_2\rangle.
\tag{33d}
\]

取 \(t=e_1+e_3\)，有
\(t\notin\Gamma(\mathcal U)=\langle e_1,e_2\rangle\)。过滤 substate 在
\(H/K\) 中把全部源投为零、目标投为 \(e_1+K\)；但原 source span 自身也投到
\(\langle e_1+K\rangle\)。所以该商分离不是原状态的 quotient relay，严格证明
(32) 不能替代 (33b)。

由于 \(L\) 的 \(s\) 个角色线性独立，\(\eta_L\) 满射：否则
\(\operatorname{im}\eta_L<L^*\) 的非零 annihilator 会对应一个在整个 \(H\)
上为零的非零 \(\rho\in L\)。从而

\[
[H:K]=q^s.
\tag{34}
\]

在 (33b) 成立后，令
\(R'=\Gamma'(\mathcal U')=\Gamma(\mathcal U_L)\)。此时才得到 successor
\((H,R',t)\) 的有限群二分：

1. 若 \(t\in K\)，则
   \((K,R',t)\) 保留同一目标缺失，且 \(K<H\)，是严格子群
   relay；
2. 若 \(t\notin K\)，选取
   \(\rho_0\in L\) 使 \(\rho_0(t)\ne0\)，并令
   \(K_0=\ker\rho_0\)。由
   \(R'\subseteq K\subseteq K_0\)，
   \(H/K_0\simeq C_q\) 中全部 filtered sources 投到单位元而目标非平凡。
   当 \(|H|>q\) 时是严格标量商 relay；当 \(H\simeq C_q\) 时才登记已有
   `TOP_PRIMARY_ANNIHILATOR`。

对 Type II 的 \(t=-1\)，若 \(q\) 为奇数，则任何
\(H\to\mathbb F_q\) 都湮灭二阶元，故自动走 \(t\in K\) 的子群分支。
\(q=2\) 时由 \(\eta_L(t)\) 是否为零决定两侧。递降后必须在 \(\Sigma'\) 及其
子群/商 contract 上重算
角色空间并商去 radical；\(L|_K=0\)，所以本次支付的 \(s\) 个方向不能在后继
重复收费。

## 7. 目标相位的精确线性判据

设一个具体后继的全部 source evaluation columns 张成

\[
T_\omega\le K_R\simeq R^*,
\tag{35}
\]

并且目标 \(t\) 有同一 ambient pairing 下的列

\[
\kappa_t\in R^*,
\qquad
\kappa_t(\rho)=\rho(t).
\tag{36}
\]

则存在一个湮灭全部后继源列、但在目标上非平凡的角色，当且仅当

\[
\boxed{
\exists\rho\in T_\omega^\perp,\ \rho(t)\ne0
\quad\Longleftrightarrow\quad
\kappa_t\notin T_\omega.}
\tag{37}
\]

证明只用有限维双对偶：
若所有 \(\rho\in T_\omega^\perp\) 都湮灭目标，则
\(\kappa_t\in(T_\omega^\perp)^\perp=T_\omega\)；逆命题相同。故
\(\kappa_t\in T_\omega\) 时，移动 annihilator 全部落在目标核中，只能依赖
subgroup 分支及原 exact contract 的 \(t\notin\Gamma\)，不能声称目标分离商。

## 8. \(h<\delta\) 的 completion-independent 严格最优性

取

\[
Q=\mathbb F_2^2,\qquad
r=1,\qquad
\delta=1,\qquad
X=\langle e_1\rangle,
\tag{38}
\]

补集菜单为

\[
B_1=\{e_2,e_1+e_2\}.
\tag{39}
\]

此时 \(h=\delta=1\)。对任一选择 \(b\in B_1\)，都有

\[
X+\langle b\rangle=Q.
\tag{40}
\]

所以不存在非零角色同时湮灭 \(X\) 与所选列；在 \(Q/X\) 中，两个带标签候选
都投到唯一非零向量。这证明在不读取具体选择秩与 exact-successor source span
时，统一条件 (4) 不能放松为 \(h\le\delta\)。

它也解释了为什么本定理不能伪装成当前饱和状态的下降。若当前 exact source
在 \(Q\) 中仍生成整个 \(Q\)，且每个源方向都必须由固定 \(X\) 加 \(r\) 条所选列
承载，则

\[
m\le h+r
\quad\Longrightarrow\quad
h\ge m-r=\delta.
\tag{41}
\]

因此 \(h<\delta\) 必须来自一个**真正收缩了 source directions 的后继合同**。
这正是新容量产生严格 role quotient 的数学内容。

具体后继存在一个严格精化：若选择列相关，令
\(a_\omega=r-\dim S_\omega>0\)，则即使最小开销
\(h_\omega^*=\delta\)，仍可能留下
\(e_\omega=a_\omega>0\)。因此本节证明的是 fixed-\(X\) 的 uniform sharpness，
不是逐后继必要条件。

## 9. 抽象角色不保证整数后继：\(p=97\)

取 Type II 参数

\[
p=97,\qquad D=6,\qquad (a,h_1)=(1,11).
\tag{42}
\]

因 \(11\mid97+24\)，这是合法来源因子。在
\(H=U(24)\) 上令

\[
\chi(u)=\chi_3(u)\left(\frac2u\right),
\tag{43}
\]

其中 \(\chi_3\) 是模 \(3\) 的非平凡二次角色。直接计算

\[
\chi(11)=1,\qquad
\chi(-1)=\chi(23)=-1.
\tag{44}
\]

所以来源落在 \(\ker\chi\)，目标在核外，并产生严格抽象
\(C_2\) quotient。

但保持同一来源的严格低层必须满足

\[
D'\mid6,\qquad D'<6,\qquad
A\mid D',\qquad D'/A\text{ 平方自由},
\qquad
AD'\equiv Da=6\pmod{11}.
\tag{45}
\]

全部候选 \(x=AD'\) 恰为

\[
\{1,2,3,4,9\},
\tag{46}
\]

没有一个同余于 \(6\pmod{11}\)。故整数提升菜单为空。唯一
\(D'=6,A=1\) 给出的 \(x=6\) 仍在原层，不满足严格 E5。这个例子严格证明

\[
\boxed{
\text{finite-group kernel quotient}
\not\Longrightarrow
\text{integer Type II successor}.}
\tag{47}
\]

## 10. 统一选择器分派

~~~text
GENERALIZED_RADO_FIXED_QUOTIENT_DEFECT(U,Q_U,delta)
  construct the physically feasible completion set Omega
  Omega empty:
    PHYSICAL_COUPLING_OBSTRUCTION
  choose a proposed successor overhead X <= Q_U
  dim(X) >= delta:
    SELECTED_SOURCE_OVERHEAD_EXHAUSTED
  dim(X) < delta:
    epsilon = delta - dim(X)
    enumerate Gr_epsilon((Q_U/X)^*)
    emit GRASSMANN_SLICE_CAPACITY_CERT
      exact_incidence
      supported_completion_branch
      role_space: L
      residual_capacity: epsilon
      perfect_role_quotient: (R/L,L^perp)
    source closure (28) absent:
      SELECTED_SOURCE_OVERHEAD_RANK_UNPROVED
    kernel filter closure (32) absent:
      KERNEL_FILTER_CLOSURE_UNPROVED
    kernel filter closure present:
      KERNEL_FILTERED_SUBSTATE
    selected source state realization (33b) absent:
      SELECTED_SOURCE_STATE_REALIZATION_UNPROVED
    selected source state realization present:
      target phase nonzero:
        choose rho_0 in L with rho_0(t) != 0
        H = C_q:
          TOP_PRIMARY_ANNIHILATOR
        |H| > q:
          ANNIHILATOR_QUOTIENT_RELAY via ker(rho_0)
      target phase zero:
        ANNIHILATOR_SUBGROUP_RELAY
      integer gates incomplete:
        GRASSMANN_KERNEL_INTEGER_LIFT_OBSTRUCTED
      FIBER_REALIZED + provenance + SNF/CRT + range + E4 + nonresetting E5:
        STRICT_LIFTABLE_SUCCESSOR
~~~

## 11. 研究边界

本卡第一次把移动 completion kernels 变成一个对**任意耦合可行完成集**都成立的
正比例分支定理，并给出严格 residual capacity
\(\varepsilon(U,X)=\delta(U)-\dim X\)。它还把切片角色下降为 perfect
\((R/L,L^\perp)\) 配对，并说明何种 exact subcontract 足以调用现有子群--商
relay。

它没有证明每个实际 F/G 亏损状态都存在 \(h<\delta\) 的统一 source contraction，
也没有证明 (28)、(32)、(33b) 或整数 E1--E5 对所有核心素数成立。特别地，
kernel filtering 本身只产生 substate，不能充当 descent。下一决定性缺口不再是
寻找另一个移动 annihilator，而是从实际 arithmetic provenance 构造一个
independently realized exact successor，并验证其精确容量
\(e_\omega>0\)；completion-independent 的 \(\dim X<\delta\) 仍是一个强充分条件。
若所有候选都强制 \(e_\omega=0\)，则需把 source saturation 转成 Type I/II
终端或另一良基下降。

## 聚焦验证

~~~bash
python3 reproductions/type_i_fg_exterior_grassmann_slice_successor_descent.py --verify
~~~

验证器只检查 \(q=2,3\) 的 Gaussian incidence、非矩形可行完成、阈值
\(h=\delta\) 的严格反例、\(r=1,2\) 的 matrix-Fourier 恒等式、Plücker
边界、kernel filter 非 relay 的 \(\mathbb F_2^3\) 反例及
\(p=97\) 的角色乘法性与整数空提升菜单；不运行历史测试。
