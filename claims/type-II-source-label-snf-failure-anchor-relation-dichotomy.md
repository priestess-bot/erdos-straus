---
kind: claim
claim_id: type-II-source-label-snf-failure-anchor-relation-dichotomy
title: Type II 源标签 SNF 失败的锚点外置—源关系二分
statement: 设 H 为有限阿贝尔群，u_1,...,u_r 为源列，t 为目标列，并给定有限根值标签。先对源列标签做 SNF 可解性检查。若源子系统不可解，SNF 第一失败行给出纯源关系障碍；若源子系统可解而加入目标后不可解，则按 t 是否属于 L=<u_i> 精确二分：t 不在 L 时存在平凡于 L、非平凡于 t 的锚点角色，并给出 H/L 的严格商缺失（L=1 时仅为环境 Fourier）；t 在 L 时目标标签与源关系不相容，给出带目标系数的 SOURCE_RELATION_LIFT_OBSTRUCTED。若二者均可解，则显式得到保持源标签和目标标签的真实角色。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-raw-finite-abelian-source-lift-snf
  - type-II-source-fiber-anchor-separating-character-certificate
  - type-II-source-fiber-cyclic-primary-digit-terminal
  - type-II-source-fiber-multiprimary-digit-terminal
  - type-II-source-fiber-elementary-rank-qheight-injection
  - type-II-annihilator-two-sided-subgroup-quotient-descent
  - type-II-hall-source-column-closure-relay
topics:
  - type-II
  - source-label
  - SNF
  - anchor
  - source-relation
  - quotient-descent
  - Fourier
  - lift-obstruction
  - primary-capacity
  - finite-abelian
  - proof-program
sources:
  - claim: type-II-raw-finite-abelian-source-lift-snf
    role: finite-label-SNF-system
  - claim: type-II-source-fiber-anchor-separating-character-certificate
    role: anchor-quotient-Fourier
  - claim: type-II-source-fiber-cyclic-primary-digit-terminal
    role: relation-to-primary-digit-capacity
  - claim: type-II-source-fiber-multiprimary-digit-terminal
    role: independent-primary-relation-capacity
  - claim: type-II-annihilator-two-sided-subgroup-quotient-descent
    role: full-source-closure-descent
visibility: public
last_checked: '2026-08-05'
---

# Type II 源标签 SNF 失败的锚点外置—源关系二分

## 1. 源标签与目标标签

令 \(H\) 为有限阿贝尔群，取源列
\[
u_1,\ldots,u_r\in H,\qquad
L=\langle u_1,\ldots,u_r\rangle\le H,
\tag{1}
\]
以及目标列 \(t\in H\)。固定一个有限标签群
\(\mu_e=\langle\zeta_e\rangle\)，给定源标签
\(a_1,\ldots,a_r\in\mathbb Z/e\mathbb Z\) 和目标标签
\(a_0\in\mathbb Z/e\mathbb Z\)。定义两个角色解集
\[
\mathcal X_{\mathrm{src}}
=\{\chi\in\widehat H:\chi(u_i)=\zeta_e^{a_i}\ (1\le i\le r)\},
\tag{2}
\]
\[
\mathcal X_{\mathrm{all}}
=\{\chi\in\mathcal X_{\mathrm{src}}:\chi(t)=\zeta_e^{a_0}\}.
\tag{3}
\]

\按有限阿贝尔源商 SNF 判据，\(\mathcal X_{\mathrm{src}}\) 和
\(\mathcal X_{\mathrm{all}}\) 的非空性分别等价于删除目标行和保留全部行后的
整数同余系统可解。因而“源先可解、加目标后失败”是一个可以逐行复核的状态，
不是抽象角色存在性假设。

## 2. 源子系统不可解

若
\[
\mathcal X_{\mathrm{src}}=\varnothing,
\tag{4}
\]
对删除目标行后的 SNF 矩阵取第一失败行。该行给出一个整数关系向量
\(w=(w_1,\ldots,w_r)\)，满足
\[
\sum_i w_i u_i=0\quad\text{在 }H\text{ 中},
\qquad
\sum_i w_i a_i\not\equiv0\pmod e.
\tag{5}
\]
输出
\[
\mathrm{SNF\_SOURCE\_ONLY\_OBSTRUCTED}
=\bigl(w,\sum_iw_i u_i,\sum_iw_i a_i\bigr).
\tag{6}
\]
这是纯源关系 Fourier/LIFT_OBSTRUCTED 见证，目标列尚未参与，不能把它登记为锚点
外置或目标容量缺口。

## 3. 源可解、目标加入后失败

现在假设
\[
\mathcal X_{\mathrm{src}}\ne\varnothing,
\qquad
\mathcal X_{\mathrm{all}}=\varnothing.
\tag{7}
\]
取 \(\chi_0\in\mathcal X_{\mathrm{src}}\)。任意另一个源一致角色都唯一写成
\[
\chi=\chi_0\psi,
\qquad
\psi\in L^\perp
:=\{\psi\in\widehat H:\psi|_L=1\}.
\tag{8}
\]
令 \(\bar t=t+L\in H/L\)，并记
\[
d=\operatorname{ord}_{H/L}(\bar t).
\tag{9}
\]
有限阿贝尔对偶性给出
\[
\{\psi(t):\psi\in L^\perp\}=\mu_d.
\tag{10}
\]
因此
\[
\mathcal X_{\mathrm{all}}\ne\varnothing
\iff
\zeta_e^{a_0}\chi_0(t)^{-1}\in\mu_d.
\tag{11}
\]

### A. 锚点外置

若
\[
d>1
\quad\Longleftrightarrow\quad
t\notin L,
\tag{12}
\]
则存在 \(\psi\in L^\perp\) 使 \(\psi(t)\ne1\)。对任何规范源支撑
\(R\subseteq L\)，有
\[
\widehat{1_R}(\psi)=|R|,
\qquad
\psi(t)\ne1.
\tag{13}
\]
输出
\[
\mathrm{SNF\_ANCHOR\_QUOTIENT\_SEPARATION}
=(H,L,t,\psi,|R|).
\tag{14}
\]
商
\[
\pi:H\to H/L
\tag{15}
\]
中源支撑落在单位元，而目标像 \(\bar t\ne0\)，所以目标仍缺失；若
\(1<|L|<|H|\)，则 \(|H/L|<|H|\) 给出严格群阶下降。若 \(L=1\)，商没有严格
变小，只保留纯锚点 Fourier，不能登记递降。

### B. 源关系中的目标错配

若
\[
d=1
\quad\Longleftrightarrow\quad
t\in L,
\tag{16}
\]
则 \(L^\perp\) 在 \(t\) 上恒为 1，式 (11) 失败只能来自
\[
\zeta_e^{a_0}\ne\chi_0(t).
\tag{17}
\]
取 \(c_i\in\mathbb Z\) 使
\[
t=\sum_i c_i u_i\quad\text{在 }H\text{ 中}.
\tag{18}
\]
则
\[
\left(-1,c_1,\ldots,c_r\right)
\tag{19}
\]
是一个包含目标行的有限关系，且其标签相位违反
\[
a_0-\sum_i c_i a_i\equiv0\pmod e.
\tag{20}
\]
输出
\[
\mathrm{SNF\_TARGET\_SOURCE\_RELATION\_OBSTRUCTED}
=\left(t-\sum_i c_i u_i,\ a_0-\sum_i c_i a_i\right).
\tag{21}
\]
这是一条目标在源差分群内的关系 Fourier 障碍，不产生商递降，也不得把纯锚点
幅度计入 q-height 容量。

## 4. 完整三分与构造性回执

源标签 SNF 与目标标签 SNF 的完整分派为
\[
\boxed{
\begin{array}{ll}
\mathcal X_{\mathrm{src}}=\varnothing
&\Longrightarrow \mathrm{SNF\_SOURCE\_ONLY\_OBSTRUCTED};\\
\mathcal X_{\mathrm{src}}\ne\varnothing,\ \mathcal X_{\mathrm{all}}\ne\varnothing
&\Longrightarrow \mathrm{SOURCE\_TARGET\_LABEL\_REALIZED};\\
\mathcal X_{\mathrm{src}}\ne\varnothing,\ \mathcal X_{\mathrm{all}}=\varnothing,\ t\notin L
&\Longrightarrow \mathrm{SNF\_ANCHOR\_QUOTIENT\_SEPARATION};\\
\mathcal X_{\mathrm{src}}\ne\varnothing,\ \mathcal X_{\mathrm{all}}=\varnothing,\ t\in L
&\Longrightarrow \mathrm{SNF\_TARGET\_SOURCE\_RELATION\_OBSTRUCTED}.
\end{array}}
\tag{22}
\]
每个分支都由源 SNF、目标 SNF 或有限群商中的显式角色给出；不存在“目标映射
失败但没有类型”的空回执。

## 5. 证明

若 (4) 成立，有限阿贝尔 SNF 的失败行直接给出 (5)--(6)。若 (7) 成立，取
\(\chi_0\)。两个源一致角色之比在每个 \(u_i\) 上为 1，故恰为 \(L^\perp\) 中的
角色，得到 (8)。对偶识别 \(L^\perp\simeq\widehat{H/L}\)；有限循环子群
\(\langle\bar t\rangle\) 的全部角色值正是 \(\mu_d\)，得到 (10)--(11)。

若 \(d>1\)，可选取非平凡 \(\psi\in L^\perp\) 作用于 \(t\)，并因其在 \(L\) 上
平凡得到 (13)--(15)；商阶在 \(L\ne1\) 时严格下降。若 \(d=1\)，(10) 只含
单位值，故 (11) 失败等价于 (17)。用 (18) 回译为关系 (19)，得到 (20)--(21)。
四个分支互斥且穷尽，证毕。

## 6. 边界例子

### 锚点外置

取 \(H=C_2\)、\(L=\{0\}\)、\(t=1\)，源标签为空。源子系统可解，而目标标签若
要求 \(\chi(t)=1\) 仍可由平凡角色实现；若要求一个不存在于
\(\widehat H\) 的更高阶标签，目标 SNF 失败但 \(\psi(1)=-1\) 给出纯锚点环境角色。
在普通二阶标签下，要求目标标签为非平凡值时，\(\psi\) 本身给出幅度 \(|R|\) 的
锚点证书，且 \(H/L=H\) 因 \(L=1\) 不提供严格下降。

### 目标源关系错配

取 \(H=C_2=\langle g\rangle\)、源列 \(u_1=g\)，源标签 \(a_1=0\)，目标
\(t=g\)，目标标签 \(a_0=1\)（二阶根值）。源角色 \(\chi_0(g)=1\) 可实现，
但 \(t\in L\) 且目标要求 \(\chi(g)=-1\)，式 (21) 给出单关系
\(t-u_1=0\) 的相位矛盾。

### 源子系统失败

取同一个 \(u_1=u_2=g\in C_2\)，标签分别为 \(0,1\)。删除目标行后的 SNF
已经失败，输出 (6)，不能把该失败误归因于目标锚点。

## 7. 源关系错配到 primary 进位容量

把目标在源群内的分支限制到一个已经三角化的单一 primary 纤维：
\[
H=C_{\ell^a},
\qquad
R=B_1+\cdots+B_m,
\qquad
B_j=\{0,v_j\},
\tag{23}
\]
其中每个二点块都保持同一个参数纤维、来源标签和整数 source-switch 合同，且所有
\(B_j\) 可以独立选择。设目标 \(t\notin R\)，并且第 3 节的目标源关系错配已经
产生一个非平凡 \(\ell\)-primary 角色方向。按
\[
c_k=\#\{j:\nu_\ell(v_j)=k\},
\qquad 0\le k<a,
\tag{24}
\]
记录每个精确进位层的合法块数。

则有构造性二分：

1. 若 \(c_k\ge\ell-1\) 对所有 \(k\)，循环 primary 进位终端给出
   \[
   R=C_{\ell^a},
   \tag{25}
   \]
   从而 \(t\in R\)，与目标缺失矛盾；在整数回译通过时，这直接升级为
   \(\mathrm{SNF\_RELATION\_CYCLIC\_PRIMARY\_HIT}\) 和 Type II 短证书。
2. 若目标仍缺失，则必存在
   \[
   \mathrm{SNF\_RELATION\_CYCLIC\_DIGIT\_DEFICIT}(\ell,k),
   \qquad c_k\le\ell-2.
   \tag{26}
   \]
   回执保存层号 \(k\)、全部合法源块、其 q-height 和来源标签；它是一个真实容量缺口，
   不能再把同一个关系角色重复计入 Fourier 容量。

### 证明

非平凡关系角色的阶含有某个素数 \(\ell\)；投影到对应的
\(C_{\ell^a}\) 后，(24) 正是循环 primary 进位终端的输入。若所有层满足
\(c_k\ge\ell-1\)，该终端证明二点块和集覆盖整个 \(C_{\ell^a}\)，得到 (25)，
与 \(t\notin R\) 矛盾。因此目标缺失只能由某一层的 (26) 解释。所有块均已要求
保持同一整数纤维，所以 (26) 是可计量的 q-height/来源容量缺口；若块分组或独立
选择门失败，则保留 PRIMARY\_SOURCE\_TRIANGULATION\_OBSTRUCTED，而不套用 (25)。
证毕。

## 8. 可分组多-primary 承接

若源关系商已经通过来源标签和参数纤维三角化为
\[
H=\bigoplus_{\nu=1}^{m}C_{\ell_\nu^{a_\nu}},
\tag{27}
\]
并且合法二点块可按 primary 分成互不相交的组
\[
R_\nu=\sum_{j\in J_\nu}\{0,v_j\},
\qquad
v_j\in C_{\ell_\nu^{a_\nu}},
\tag{28}
\]
其中每个组内的选择独立、不同组的选择不共享同一个 q 来源，则目标在源群内的
SNF 错配还有如下精化：

* 若每个 \((\nu,k)\) 都有至少 \(\ell_\nu-1\) 个合法块满足
  \(\nu_{\ell_\nu}(v_j)=k\)，则
  \[
  R_1+\cdots+R_m=H,
  \tag{29}
  \]
  所有目标坐标均被覆盖，输出
  \(\mathrm{SNF\_RELATION\_MULTIPRIMARY\_HIT}\) 并回译 Type II；
* 若目标仍缺失，则存在一个具体的
  \[
  \mathrm{SNF\_RELATION\_MULTIPRIMARY\_DIGIT\_DEFICIT}(\nu,k),
  \qquad
  c_{\nu,k}\le\ell_\nu-2.
  \tag{30}
  \]

证明是逐 primary 应用第 7 节并取直和；不同 primary 的块不能只凭抽象群分解
合并，必须保留 (28) 的 source-switch、shared-q 和独立选择记录。若 (28) 失败，
输出 \(\mathrm{MULTIPRIMARY\_SOURCE\_TRIANGULATION\_OBSTRUCTED}\)，不把跨组
数量直接相加。

## 9. SNF 关系角色的全源列闭包升级

回到目标在源群内的分支。假设目标源关系错配已经通过真实有限阿贝尔 SNF 提升为
一个素数阶角色
\[
\chi:H\longrightarrow\mu_\ell,
\qquad
K=\ker\chi,
\tag{31}
\]
并且当前参数纤维的全部真实源生成元
\(g_1,\ldots,g_s\) 满足
\[
\chi(g_i)=1\quad(1\le i\le s).
\tag{32}
\]
则 \(R\subseteq K\)，而全源列闭合给出以下互斥分派：

1. \(t\notin K\)：输出
   \(\mathrm{SNF\_RELATION\_ANNIHILATOR\_QUOTIENT\_RELAY}\)。源像在
   \(H/K\simeq C_\ell\) 的单位陪集，目标像非单位，若 \(|H|>\ell\) 则势的第一坐标
   严格下降；
2. \(t\in K\)：输出
   \(\mathrm{SNF\_RELATION\_ANNIHILATOR\_SUBGROUP\_RELAY}\)，把同一个目标缺失
   限制到真子群 \(K\)，其阶严格小于 \(|H|\)；
3. \(|H|=\ell\) 且 \(K=1\)：输出
   \(\mathrm{SNF\_RELATION\_TOP\_PRIMARY}\)，转入广义 \(2^j\) 或 Type I/F/G
   顶层终端；
4. 若 (32) 失败：输出
   \(\mathrm{SNF\_RELATION\_SOURCE\_COLUMN\_ESCAPE}\)，将被角色分离的源列加入
   source-column escape 扩张，不能静默使用前两项。

前三项的整数递降资格由 annihilator relay 的 G1--G4/标签/范围菜单决定；门通过时
才登记 verified_edge，门失败时保留具体 LIFT_OBSTRUCTED。因此，SNF 关系错配
不再是无后继终点：它要么产生明确 primary 容量缺口，要么在全源列闭包下产生
可检查的商/子群状态，要么暴露一个具体的逃逸源列。

## 研究边界

该引理把目标映射 SNF 障碍精确接回三条已有路线：源子系统失败进入源关系
Fourier；源可解但目标在源群外进入锚点商分离；目标在源群内则给出带目标系数的
关系障碍；在单一 primary 纤维中又可进一步精化为直接命中或明确进位层缺口。它
没有证明锚点商一定通过整数 source-switch，也没有证明多 primary 或跨纤维的关系
障碍必然产生 Type I/II 容量；这些仍需由 Q1--Q4、source-column escape 和
F/G/Hall 承接。
