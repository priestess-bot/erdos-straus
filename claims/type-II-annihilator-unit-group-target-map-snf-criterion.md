---
kind: claim
claim_id: type-II-annihilator-unit-group-target-map-snf-criterion
title: Type II annihilator relay 的单位群—目标带像满射 SNF 判据
statement: 设 A=U(4D') 与目标状态 J 为有限阿贝尔群，并固定 a=-1 在 A 的 invariant-factor 坐标以及 t_J 在 J 的坐标；还可给出有限个来源元素 alpha_i 及其目标像 u_i。把 A 到 J 的同态写成有限矩阵 Y；同态约束、Y a=t_J 以及全部 Y alpha_i=u_i 由一个整数同余系统的 SNF 精确判定，满射性等价于 [N|Y] 的商 SNF 全为 1。因而 G1 与带来源 G2 的联合菜单非空当且仅当存在一个满足全部标签的满射，失败时分别给出仿射同余矛盾或非平凡商群证书。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on: []
topics:
- type-II
- annihilator
- unit-group
- finite-abelian
- invariant-factor
- SNF
- surjection
- target-lift
- obstruction
sources:
  - claim: type-II-raw-finite-abelian-source-lift-snf
    role: finite-abelian-SNF-template
visibility: public
last_checked: '2026-08-05'
---

# Type II annihilator relay 的单位群—目标带像满射 SNF 判据

## 1. 问题的有限矩阵化

固定一个候选低模数 \(D'\)，写出

\[
A=U(4D')\simeq\bigoplus_{j=1}^{r} C_{m_j},
\qquad
J\simeq\bigoplus_{k=1}^{s} C_{n_k},
\tag{1}
\]

其中两侧均采用 invariant-factor 坐标。令

\[
a=(a_1,\ldots,a_r)\in A,
\qquad
t=(t_1,\ldots,t_s)\in J
\tag{2}
\]

分别是 \(a=-1\) 和 relay 目标 \(t_J\) 的坐标。\(A\) 到 \(J\) 的一个同态由矩阵

\[
Y=(y_{kj})_{1\le k\le s,\;1\le j\le r},
\qquad y_{kj}\in\mathbb Z/n_k\mathbb Z,
\tag{3}
\]

给出：第 \(j\) 个源生成元的像是第 \(j\) 列。它成为同态当且仅当

\[
m_j y_{kj}\equiv0\pmod{n_k}
\qquad(1\le k\le s,\ 1\le j\le r).
\tag{4}
\]

固定目标像的条件是

\[
\sum_{j=1}^{r}a_jy_{kj}\equiv t_k\pmod{n_k}
\qquad(1\le k\le s).
\tag{5}
\]

注意 (4)--(5) 是对同一个 \(Y\) 的联合条件；先分别检查同态存在和目标阶数，
不能把它们拼接成两个互不相干的映射。

## 2. 同态与目标像的 SNF 充要判据

把 \(y_{kj}\) 按任意固定顺序堆叠成整数向量 \(y\in\mathbb Z^{sr}\)。为每一个
(4) 引入整数辅助变量 \(z_{kj}\)，为每一个 (5) 引入 \(w_k\)，得到方程组

\[
\begin{cases}
m_jy_{kj}-n_kz_{kj}=0,&1\le k\le s,\ 1\le j\le r,\\
\displaystyle\sum_{j=1}^{r}a_jy_{kj}-n_kw_k=t_k,&1\le k\le s.
\end{cases}
\tag{6}
\]

记其整数矩阵为 \(B_{A,J,a,t}\)，未知向量为
\(x=(y,z,w)^{\mathsf T}\)，右端为
\(b=(0,\ldots,0,t_1,\ldots,t_s)^{\mathsf T}\)。取

\[
U B_{A,J,a,t} V
=\operatorname{diag}(\delta_1,\ldots,\delta_\rho,0,\ldots,0),
\qquad \delta_i>0,
\tag{7}
\]

并令 \(b'=Ub\)。则

\[
\boxed{
(4)\text{--}(5)\text{ 有解}
\iff
\delta_i\mid b'_i\ (i\le\rho),
\quad b'_i=0\ (i>\rho).
}
\tag{8}
\]

这是标准整数线性系统的 SNF 判据。若 (8) 通过，将 \(y\) 的每个分量约化到
\(0,\ldots,n_k-1\)，得到有限的候选集

\[
\mathcal Y_{\mathrm{tgt}}(A,J,a,t)
=\{Y:\text{满足 (4)--(5)}\}.
\tag{9}
\]

若 (8) 失败，某一整除行 \(\delta_i\nmid b'_i\)，或零行 \(b'_i\ne0\)，就是
一个可独立复核的 **G1_TARGET_CONGRUENCE_OBSTRUCTED** 证书。它表示没有任何同态
能够把 \(a=-1\) 送到给定的 \(t_J\)。特别地，

\[
\operatorname{ord}(t_J)\mid\operatorname{ord}(-1)=2
\tag{10}
\]

是 (8) 的廉价必要条件；若 (10) 失败，无需继续构造矩阵。

## 3. 满射性的商 SNF 判据

令

\[
N=\operatorname{diag}(n_1,\ldots,n_s),
\qquad
C_Y=[\,N\mid Y\,]\in\mathbb Z^{s\times(s+r)}.
\tag{11}
\]

列格 \(N\mathbb Z^s+Y\mathbb Z^r\) 正是 \(J\) 中由 \(Y\) 的列生成的像的整数
原像。因此

\[
\boxed{
Y:A\twoheadrightarrow J
\iff
\operatorname{coker}(C_Y)=0
\iff
\operatorname{SNF}(C_Y)=\operatorname{diag}(1,\ldots,1).
}
\tag{12}
\]

证明很直接：
\(\mathbb Z^s/N\mathbb Z^s\simeq J\)，而 \(Y\mathbb Z^r\) 在该商中的像就是
\(\operatorname{im}Y\)。所以商消失当且仅当 \(Y\) 满射。若某个 SNF 因子
\(\epsilon_i>1\)，则
\(\operatorname{coker}(C_Y)\) 含有一个非平凡循环因子
\(C_{\epsilon_i}\)；对应的 SNF 行给出一个具体 **G1_SURJECTIVITY_OBSTRUCTED**
见证，而不是仅仅知道“像太小”。

定义带目标的满射菜单

\[
\mathcal Y_{\twoheadrightarrow}(A,J,a,t)
=
\{Y\in\mathcal Y_{\mathrm{tgt}}(A,J,a,t):
\operatorname{SNF}(C_Y)=I_s\}.
\tag{13}
\]

于是得到精确二分

\[
\boxed{
\mathcal Y_{\twoheadrightarrow}(A,J,a,t)\ne\varnothing
\iff
\exists\,\eta:A\twoheadrightarrow J,
\quad\eta(-1)=t_J.
}
\tag{14}
\]

若 relay 状态要求 \(\eta\) 为同构，只需在 (13) 中再要求
\(|A|=|J|\)；满射随后自动为同构。若 \(|A|<|J|\)，或者 invariant-factor
条件本身排除满射，则可在枚举前直接输出 **G1_GROUP_ORDER_OBSTRUCTED**。

## 4. 有限失败账本与构造

G1 的规范执行顺序如下：

1. 计算 \(U(4D')\) 与 \(J\) 的 invariant factors 以及 \(a=-1,t_J\) 的坐标；
2. 用 (10) 做目标阶数预筛；
3. 对 (6) 做一次 SNF，得到 \(\mathcal Y_{\mathrm{tgt}}\) 或
   **G1_TARGET_CONGRUENCE_OBSTRUCTED**；
4. 对有限的每个 \(Y\in\mathcal Y_{\mathrm{tgt}}\) 计算 \(C_Y\) 的 SNF；
5. 首个 \(\operatorname{SNF}(C_Y)=I_s\) 的矩阵给出显式 \(\eta\)，并输出
   **G1_GROUP_MAP_REALIZED**；若所有 \(Y\) 都有某个 \(\epsilon_i>1\)，保存全部最小
   商因子和对应 SNF 行，输出 **G1_SURJECTIVITY_OBSTRUCTED**。

由于每个 \(y_{kj}\) 只需取模 \(n_k\)，第 4 步是有限且完备的，不依赖搜索顺序。
矩阵 \(Y\) 给出 \(\eta\) 后，目标条件 (5) 自动保证
\(\eta(-1)=t_J\)；没有额外的“抽象群同构”假设。

## 5. 两个结构边界

### \(U(4)\simeq C_2\) 不能满射到 \(C_4\)

取 \(A=C_2\)、\(J=C_4\)。同态条件允许的唯一非零像是 \(y=2\)，因为
\(2y\equiv0\pmod4\)。但

\[
\operatorname{SNF}[4\mid 2]=[2],
\]

故像只有 \(\{0,2\}\)，输出
**G1_SURJECTIVITY_OBSTRUCTED**。这正是 annihilator 菜单中
“\(U(4)\) 的指数结构不能产生 \(C_4\)”的精确证明。

### 目标像本身的同余冲突

取 \(A=C_2\oplus C_2\)、\(J=C_2\)，令 \(a=(0,0)\)、\(t=1\)。抽象上存在满射
\(A\twoheadrightarrow J\)，但任何同态都把 \(a\) 送到 \(0\)，所以 (5) 无解；
SNF 系统 (6) 的目标行留下非零零行，输出
**G1_TARGET_CONGRUENCE_OBSTRUCTED**。这说明“存在满射”和“满射把 \(-1\)
送到目标”必须同时检查。

## 6. 接入 annihilator 纤维菜单

在
[Type II annihilator relay 的带来源同余纤维提升判据](type-II-annihilator-congruence-fiber-lift-criterion.md)
的每个候选 \((D',A)\) 上，令

\[
\mathcal M_{G1}(D',J,t_J)
=\mathcal Y_{\twoheadrightarrow}
\bigl(U(4D'),J,-1,t_J\bigr).
\tag{15}
\]

则

\[
\mathcal M_{G1}(D',J,t_J)\ne\varnothing
\iff
\text{该候选通过 G1，且存在可用于 (3) 的 }\eta.
\tag{16}
\]

若 (16) 失败：

- (8) 失败时保存目标同余 SNF 行；
- (8) 通过但所有 (12) 失败时保存每个候选 \(Y\) 的最小非平凡商因子；
- \(|A|<|J|\) 或阶结构预筛失败时保存群阶/指数障碍。

只有 (16) 通过后，才进入原提升菜单的 G2--G4；因此 G1 失败不会被错误地
计入 Fourier 或 Hall 容量，也不会被误写为已经完成的整数递降。

## 7. 目标与来源标签的联合 SNF

为了把 G1 与 G2 的状态坐标合并，给定有限组
\[
\alpha^{(0)}=a=-1,\quad v^{(0)}=t_J,
\qquad
\alpha^{(i)}\in A,\quad v^{(i)}\in J\ (1\le i\le q).
\tag{17}
\]
对 annihilator 纤维菜单，通常取
\[
\alpha^{(i)}=h_i\bmod 4D',
\qquad
v^{(i)}=u_i.
\tag{18}
\]
在 (6) 的同态行之外，为每个 \(i\) 和每个目标坐标 \(k\) 加入
\[
\sum_{j=1}^{r}\alpha^{(i)}_j y_{kj}
-n_k w_{k,i}=v^{(i)}_k.
\tag{19}
\]
记由 (4) 与全部 (19) 组成的整数矩阵为
\(B_{A,J,\boldsymbol\alpha,\boldsymbol v}\)。其 SNF 给出
\[
\boxed{
\text{存在同态 }\eta:A\to J\text{ 满足 }
\eta(\alpha^{(i)})=v^{(i)}\ \forall i
\iff
\text{该联合 SNF 的整除/零行条件全部通过}.
}
\tag{20}
\]
证明与 (8) 相同：左侧的同态条件保证每列尊重源生成元阶，(19) 逐坐标编码全部
仿射标签；SNF 是整数方程组有解的充要判据。把每个 \(y_{kj}\) 约化到
\(0,\ldots,n_k-1\) 后得到有限菜单
\[
\mathcal Y_{\mathrm{label}}(A,J;\boldsymbol\alpha,\boldsymbol v).
\tag{21}
\]
再对每个 \(Y\) 应用 (12)，定义
\[
\mathcal Y_{\mathrm{label},\twoheadrightarrow}
=\{Y\in\mathcal Y_{\mathrm{label}}:
\operatorname{SNF}[N\mid Y]=I_s\}.
\tag{22}
\]
于是
\[
\boxed{
\mathcal Y_{\mathrm{label},\twoheadrightarrow}\ne\varnothing
\iff
\exists\,\eta:A\twoheadrightarrow J
\text{ 满足 }\eta(-1)=t_J,\
\eta(h_i\bmod4D')=u_i\ (1\le i\le q).
}
\tag{23}
\]
若联合 SNF 失败，失败行给出 **G2_SOURCE_IMAGE_OBSTRUCTED**（当 \(i\ge1\)）
或 **G1_TARGET_CONGRUENCE_OBSTRUCTED**（当 \(i=0\)）；若联合系统有解但所有
\(Y\) 的商 SNF 都有非单位因子，则输出
**G1\_G2\_SURJECTIVITY\_OBSTRUCTED**，并保存每个最小商因子。这样，状态像
约束不会被当作“事后选择的 \(\eta\)”而漏掉，也不会把抽象的源残数匹配误记为
整数提升。

## 8. 二阶目标的显式 G1 映射

当 \(J=C_2=\{1,\bar{-1}\}\) 且 \(t_J=\bar{-1}\) 时，G1 不需要一般的矩阵枚举。
自然的约化映射
\[
\rho_4:U(4D')\longrightarrow U(4)\simeq C_2,
\qquad
\rho_4(u)=u\bmod4,
\tag{24}
\]
是满射，并满足 \(\rho_4(-1)=\bar{-1}\)。满射性甚至不需要 CRT：
\(1\) 和 \(-1\) 本身就是 \(U(4D')\) 中分别映到 \(1\) 和 \(\bar{-1}\) 的两个元素。

因此
\[
\boxed{
J=C_2,\ t_J\ne1
\quad\Longrightarrow\quad
\mathcal Y_{\twoheadrightarrow}(U(4D'),J,-1,t_J)\ne\varnothing
}
\tag{25}
\]
对每个 \(D'\) 都成立。若再要求来源像
\(\eta(h_i\bmod4D')=u_i\)，则应将 \(\rho_4\) 作为联合标签系统 (17)--(23)
的一个候选；失败只能来自来源标签彼此冲突或算术合同，不是单位群本身的 G1
结构障碍。

这给出一个实际分流：二阶非平凡目标先固定 \(\rho_4\) 作为规范映射，再做
统一来源 CRT、联合标签 SNF 和 Type II 正规形；只有目标阶大于二或目标像为
更高 \(2^j\) 分量时，才需要回到一般的带目标满射菜单。

## 研究边界

该判据把 G1 从“存在一个合适的单位群满射”的抽象占位符变成有限可枚举的
同态矩阵与商 SNF 账本，并严格处理 \(-1\mapsto t_J\) 的目标约束。它不证明
G2--G4 对某个 \(D'\) 必然通过，也不把一个通过 G1 的抽象映射自动升级为 Type II
整数证书；后者仍需统一来源同余、范围、shared-q 和 \(B'>A\) 门。
