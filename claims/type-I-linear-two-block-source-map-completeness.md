---
kind: claim
claim_id: type-I-linear-two-block-source-map-completeness
title: 线性两块奇部 source-map 完备性与 q-秩逃逸二分
statement: 对 p=1 mod24 的线性状态 p=a+s+asR（s 奇、R=3 mod8），将 U=sR+1、V=aR+1 去掉固定二进因子得到奇部块 U°、V°。则 U°V°=K=(pR+1)/4，且两块的全部奇素数指数向量是有限、显式且完备的两行 source-map。对任意给定的块/目标相位标签，有限阿贝尔 SNF 在该两块源模型内给出源障碍、完整提升、锚点商分离或源内关系错配四分；若目标纤维差分群不包含于 L_blk=<U°,V°>，输出 LINEAR_BLOCK_SOURCE_ESCAPE，不得把两块映射冒充全源闭包。若 Delta_Q<=L_blk，则每个 q 初等源秩至多为2；r_q(Q)>2 时立即得到源模型不一致或 source escape。该结论把线性 source-map 的缺口从无限候选压缩为两块 SNF 与一个 rank/escape 检查，但不声称所有 F 状态都满足 block closure。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-linear-multi-active-fourier-carrier-vector
  - type-I-fg-role-snf-terminal-dispatch
  - type-I-fg-fourier-to-type-II-role-demand-bridge
  - type-II-raw-finite-abelian-source-lift-snf
  - type-II-source-fiber-elementary-rank-qheight-injection
topics:
- type-I
- linear-source
- F-state
- G-state
- source-map
- SNF
- q-rank
- carrier-vector
- block-closure
- escape
- quotient-descent
- proof-program
sources:
  - claim: type-I-linear-multi-active-fourier-carrier-vector
    role: explicit-block-carrier
  - claim: type-I-fg-role-snf-terminal-dispatch
    role: F-G-four-terminal
  - claim: type-II-raw-finite-abelian-source-lift-snf
    role: finite-abelian-SNF
  - claim: type-II-source-fiber-elementary-rank-qheight-injection
    role: source-rank-capacity
visibility: public
last_checked: '2026-08-05'
---

# 线性两块奇部 source-map 完备性与 q-秩逃逸二分

## 1. 两个实际源块

固定

\[
p=a+s+asR,\qquad s\ {\rm odd},\qquad R\equiv3\pmod8,
\]

并令

\[
K=\frac{pR+1}{4},\qquad
U=sR+1,\qquad V=aR+1.
\tag{1}
\]

因为 \(p\equiv1\pmod8\) 且 \(R\equiv3\pmod8\)，\(K\) 为奇数。令

\[
\epsilon_s=v_2(U),\qquad
\epsilon_a=v_2(V),\qquad
U^\circ=\frac{U}{2^{\epsilon_s}},\qquad
V^\circ=\frac{V}{2^{\epsilon_a}}.
\tag{2}
\]

由 \(UV=4K\) 和 \(K\) 奇，有

\[
\epsilon_s+\epsilon_a=2,\qquad
\boxed{U^\circ V^\circ=K.}
\tag{3}
\]

特别地，若 \(a\) 偶，则 \((\epsilon_s,\epsilon_a)=(2,0)\)；若 \(a\) 奇，则
\((\epsilon_s,\epsilon_a)=(1,1)\)。两块的奇部都是 \(K\) 的正除子，并满足

\[
U^\circ\equiv2^{-\epsilon_s}\pmod R,\qquad
V^\circ\equiv2^{-\epsilon_a}\pmod R.
\tag{4}
\]

令 \(H=\langle q\bmod R:q\mid K\rangle\le U(R)\)。由于 (3)，
\(U^\circ,V^\circ\in H\)。这两个元素是线性状态内实际存在的、不会随 Fourier 角色
选择而变化的源块。

## 2. 完整的两行载体数据

把 \(K\) 的不同奇素因子按固定顺序记为 \(q_1,\ldots,q_r\)，令

\[
\phi:\mathbb Z^r\to H,\qquad
\phi(z)=\prod_{i=1}^{r}q_i^{z_i},\qquad
\Lambda=\ker\phi.
\tag{5}
\]

定义两个显式指数向量

\[
b_s=\bigl(v_{q_i}(U^\circ)\bigr)_{i=1}^{r},\qquad
b_a=\bigl(v_{q_i}(V^\circ)\bigr)_{i=1}^{r}.
\tag{6}
\]

则

\[
\boxed{b_s+b_a=\kappa,\qquad
\kappa=\bigl(v_{q_i}(K)\bigr)_{i=1}^{r}.}
\tag{7}
\]

因此线性两块 source-map 的源行不是待搜索的标签，而是
\[
\bigl(U^\circ,b_s,s\bigr),\qquad
\bigl(V^\circ,b_a,a\bigr),
\tag{8}
\]
其中最后一项是实际整数颜色/端点标签。任意由 \(U^\circ,V^\circ\) 产生的源关系，
都由

\[
\mathcal R_{\rm blk}
=\{(x,y)\in\mathbb Z^2:x\,b_s+y\,b_a\in\Lambda\}
\tag{9}
\]

完整记录；不存在第三个未枚举的线性块行。对任意目标 \(t\in H\)，选择一个
\(b_t\in\mathbb Z^r\) 满足 \(\phi(b_t)=t\)，则带目标的关系行由

\[
\mathcal R_{\rm blk,t}
=\{(x,y,z)\in\mathbb Z^3:
x\,b_s+y\,b_a+z\,b_t\in\Lambda\}
\tag{10}
\]

给出，且不依赖 \(b_t\) 的选择。

## 3. 两块标签的有限 SNF 门

给定一个根群 \(\mu_e\) 和标签

\[
\lambda_s,\lambda_a,\lambda_t\in\mathbb Z/e\mathbb Z,
\tag{11}
\]

其含义是要求一个真实角色 \(\chi\in\widehat H\) 满足

\[
\chi(U^\circ)=\zeta_e^{\lambda_s},\qquad
\chi(V^\circ)=\zeta_e^{\lambda_a},\qquad
\chi(t)=\zeta_e^{\lambda_t}.
\tag{12}
\]

把 \(H\) 写成 invariant-factor 分解
\(H\simeq\bigoplus_{\nu=1}^{d}C_{m_\nu}\)，并将三个元素在该坐标中的系数写成
\(c_{s\nu},c_{a\nu},c_{t\nu}\)。取

\[
L_0=\operatorname{lcm}(e,m_1,\ldots,m_d).
\]

按有限阿贝尔 source-lift SNF 的标准构造，用三行

\[
A_{j\nu}=L_0\,\frac{c_{j\nu}}{m_\nu},\qquad
b_j=L_0\,\frac{\lambda_j}{e},
\qquad j\in\{s,a,t\},
\tag{13}
\]

组成整数增广系统 \(Bx=b\)。于是 (12) 有解当且仅当

\[
\delta_i\mid (Ub)_i\quad(i\le\rho),\qquad
(Ub)_i=0\quad(i>\rho),
\tag{14}
\]

其中 \(UBV=\operatorname{diag}(\delta_1,\ldots,\delta_\rho,0,\ldots,0)\) 是
\(B\) 的 Smith 正规形。由于源行只有 \(U^\circ,V^\circ\) 两条，这个 SNF 是两行源、
一行目标的有限完整检查，而不是依赖开放的标签枚举。

因此，在两块 source-map 已经封闭的前提下，F/G 角色请求严格进入四分：

\[
\begin{array}{ll}
\text{源两行 SNF 失败}
&\Rightarrow \mathrm{LINEAR\_BLOCK\_SOURCE\_OBSTRUCTED};\\
\text{三行 SNF 通过}
&\Rightarrow \mathrm{LINEAR\_BLOCK\_SOURCE\_TARGET\_LIFTED};\\
\text{源通过、目标失败且 }t\notin L_{\rm blk}
&\Rightarrow \mathrm{LINEAR\_BLOCK\_ANCHOR\_QUOTIENT};\\
\text{源通过、目标失败且 }t\in L_{\rm blk}
&\Rightarrow \mathrm{LINEAR\_BLOCK\_RELATION\_OBSTRUCTED}.
\end{array}
\tag{15}
\]

这里
\[
L_{\rm blk}=\langle U^\circ,V^\circ\rangle.
\tag{16}
\]

若目标纤维差分群 \(\Delta_Q\not\le L_{\rm blk}\)，则 (15) 不能冒充完整 source-map；
选择器必须先输出

\[
\boxed{\mathrm{LINEAR\_BLOCK\_SOURCE\_ESCAPE}}
\tag{17}
\]

并把逃逸元素送入更大的源列菜单、另一块分解、Type II 源关系或商递降。

## 4. q 初等秩与两块容量

在 block closure 条件

\[
\Delta_Q\le L_{\rm blk}
\tag{18}
\]

下，对每个素数 \(q\) 有

\[
\boxed{
r_q(Q)=\dim_{\mathbb F_q}(\Delta_Q/q\Delta_Q)
\le
\dim_{\mathbb F_q}(L_{\rm blk}/qL_{\rm blk})
\le2.
}
\tag{19}
\]

因此：

1. 若 \(r_q(Q)>2\)，则 block closure 不可能同时成立；真实回执只能是
   LINEAR_BLOCK_SOURCE_ESCAPE，或若账本声称只有两块源列，则为
   SOURCE_RANK_INCONSISTENT；
2. 若 \(r_q(Q)=2\)，两个独立的 block q 方向都必须保留，不能只用一个颜色或一个
   source row 收费；
3. 若 \(r_q(Q)=1\)，最多一个独立 q 方向是必需的，第二块只能增加有限阶/高度，
   不能按第二个独立秩重复收费。

同时，显式载体高度满足

\[
h_q^{(s)}=v_q(U^\circ),\qquad
h_q^{(a)}=v_q(V^\circ),\qquad
h_q^{(s)}+h_q^{(a)}=v_q(K),
\tag{20}
\]

并有
\[
\max\{h_q^{(s)},h_q^{(a)}\}
\ge\left\lceil\frac{v_q(K)}2\right\rceil.
\tag{21}
\]

式 (20)--(21) 是实际整数载体信息；式 (19) 是角色所需独立方向信息。二者必须分开
记录，不能把 \(r_q\) 自动替换成 \(h_q^{(s)}+h_q^{(a)}\)。

## 5. 证明

由 \(UV=4K\) 和 \(K\) 奇得到 (3)，按 \(a\) 的奇偶性得到二进分拆及 (4)。因
\(U^\circ,V^\circ\) 是 \(K\) 的除子，其所有素数均属于 (5) 的生成集，故 (6)--(8)
是完整的实际块数据。指数向量关系 (7) 直接来自 \(U^\circ V^\circ=K\)；任意块关系
都恰是 (9)，加入目标后恰是 (10)。

有限阿贝尔角色的三行相位约束正是 (13) 的整数同余系统，Smith 正规形给出 (14) 的
充要条件。因此 (15) 是前述 source-label SNF 四分在两块源表上的特化；若
\(\Delta_Q\not\le L_{\rm blk}\)，两块行无法覆盖该源差分，必须输出 (17)。

最后，(18) 是有限阿贝尔子群包含；子群的 q 初等商秩不超过母群，而两生成群的每个
q-primary 初等商秩不超过 2，得到 (19)。式 (20) 来自 (7)，(21) 是两个非负整数
之和的最大值界。证毕。

## 6. 边界例子

### 两块数据完全显式

取
\[
(p,R,a,s)=(73,11,6,1).
\]

则
\[
U=12,\quad V=67,\quad K=201=3\cdot67,
\qquad
U^\circ=3,\quad V^\circ=67.
\]

因此 \(b_s=(1,0)\)、\(b_a=(0,1)\)，两块奇部乘积精确恢复 \(K\)。模 \(11\) 时
\(V^\circ\equiv1\)，所以 \(L_{\rm blk}=\langle3\rangle\)；\(-1\equiv10\) 不在该
子群中，目标属于锚点外置/商分离分支，而不能被误记为两块 q 容量命中。

### rank 逃逸

取抽象 \(H=C_q\oplus C_q\oplus C_q\)，而 \(L_{\rm blk}\) 由两元素生成。若某个
目标差分群满足 \(r_q(Q)=3\)，则 \(\Delta_Q\not\le L_{\rm blk}\)，直接触发
\(\mathrm{LINEAR\_BLOCK\_SOURCE\_ESCAPE}\)。用两块高度相加支付三个独立方向是
不合法的。

## 7. 研究边界

本卡完成了线性两块模型内的 source-map 完备性：奇部载体、指数向量、两行 SNF 和
q 初等秩均是有限且显式的。它仍未证明所有线性 F 状态都满足
\(\Delta_Q\le L_{\rm blk}\)，也未证明 SNF 通过后的角色一定满足跨状态 q-prefix、
Kneser 或 E1--E5。故全局剩余被压缩为：

1. 证明线性 F 状态的目标纤维差分不会逃逸两块源子群，或为逃逸元素构造合法 alternate
   源/严格商下降；
2. 对通过两块 SNF 的真实标签建立跨状态 q 进容量超载或 Type II 命中；
3. 将 LINEAR_BLOCK_SOURCE_ESCAPE 接入已有 Type I/F/G/Type II 终端，而不是把它
   默认为失败。
